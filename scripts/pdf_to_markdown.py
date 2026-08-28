#!/usr/bin/env python3
"""
PDF to Markdown Converter for Skill Generation Reference Books
--------------------------------------------------------------
Converte livros e documentos PDF em arquivos Markdown (.md) estruturados,
preservando sumários (TOC), cabeçalhos, listas, blocos de código e páginas.

Suporta PyMuPDF (fitz) e fallback nativo ultra-rápido via pdftotext (Poppler).

Uso:
    python scripts/pdf_to_markdown.py <caminho_para_pdf> [caminho_saida_md]
    python scripts/pdf_to_markdown.py --dir <pasta_com_pdfs> --output-dir <pasta_saida>
    python scripts/pdf_to_markdown.py <caminho_para_pdf> --toc-only
    python scripts/pdf_to_markdown.py <caminho_para_pdf> --split-chapters
"""

import sys
import os
import re
import argparse
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List, Tuple, Dict, Any, Optional

# Reconfigura a saída padrão para UTF-8 no Windows e Linux
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

HAS_FITZ = False
try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False


def clean_text(text: str) -> str:
    """Limpa o texto extraído, corrigindo hifenização no final de linhas."""
    # Corrigir palavras hifenizadas quebradas entre linhas (ex: secu-\nrity -> security)
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    # Remover múltiplos espaços mantendo quebras de linha
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def extract_with_pdftotext(pdf_path: str) -> Tuple[List[str], List[Tuple[int, str]]]:
    """Extrai o texto do PDF página a página usando pdftotext do sistema."""
    cmd = ['pdftotext', '-layout', pdf_path, '-']
    result = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext falhou com código {result.returncode}: {result.stderr}")

    raw_output = result.stdout
    pages = raw_output.split('\x0c')
    if pages and not pages[-1].strip():
        pages.pop()

    toc_hints = []
    for idx, page in enumerate(pages[:25]):
        lines = page.splitlines()
        for line in lines:
            line_str = line.strip()
            toc_match = re.match(r'^(?:(?:Chapter|Capítulo)\s+\d+[:.]?\s*|(?:\d+\.)+\s+)([A-Za-z0-9\s,\-\'\"]+?)(?:\.{2,}|\s{3,})(\d+)$', line_str)
            if toc_match:
                title = toc_match.group(1).strip()
                try:
                    p_num = int(toc_match.group(2).strip())
                    toc_hints.append((p_num, title))
                except ValueError:
                    pass

    return pages, toc_hints


def convert_pdf_to_markdown_pdftotext(pdf_path: str, output_path: str, toc_only: bool = False) -> str:
    """Converte PDF para Markdown usando pdftotext como motor de extração."""
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pages, toc_hints = extract_with_pdftotext(pdf_path)

    if toc_only:
        toc_lines = [f"# Tabela de Conteúdos: {base_name}\n"]
        if toc_hints:
            for p_num, title in toc_hints:
                toc_lines.append(f"- **{title}** (p. {p_num})")
        else:
            toc_lines.append("_Nenhum índice tabular identificado nas primeiras páginas do PDF._")
        content = "\n".join(toc_lines)
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return output_path

    md_lines = []
    md_lines.append(f"# {base_name}\n")
    md_lines.append(f"> Documento convertido de PDF para Markdown para referência de skills.\n")

    if toc_hints:
        md_lines.append("## 📌 Sumário Identificado\n")
        for p_num, title in toc_hints[:40]:
            md_lines.append(f"- [{title}](#p{p_num})")
        md_lines.append("\n---\n")

    for page_idx, page_text in enumerate(pages):
        page_num = page_idx + 1
        page_header = f"\n<a id='p{page_num}'></a>\n<!-- Página {page_num} -->\n"
        md_lines.append(page_header)

        lines = page_text.splitlines()
        in_code_block = False
        code_lines = []

        for line in lines:
            stripped = line.strip()
            if not stripped:
                if in_code_block:
                    code_lines.append("")
                else:
                    md_lines.append("")
                continue

            if len(stripped) < 80 and (stripped.isupper() or stripped.startswith(('Chapter ', 'CHAPTER ', 'Capítulo '))):
                if in_code_block:
                    md_lines.append("```\n" + "\n".join(code_lines) + "\n```\n")
                    in_code_block = False
                    code_lines = []
                md_lines.append(f"\n## {stripped}\n")
                continue

            is_code_line = (
                line.startswith('    ') or line.startswith('\t') or
                any(stripped.startswith(kw) for kw in ['def ', 'import ', 'from ', 'class ', 'const ', 'let ', 'var ', 'function ', '#include', 'package ', 'func '])
            )

            if is_code_line:
                if not in_code_block:
                    in_code_block = True
                    code_lines = [stripped]
                else:
                    code_lines.append(stripped)
            else:
                if in_code_block:
                    md_lines.append("```\n" + "\n".join(code_lines) + "\n```\n")
                    in_code_block = False
                    code_lines = []

                if stripped.startswith(('•', '-', '*', '1.', '2.', '3.')):
                    md_lines.append(stripped)
                else:
                    md_lines.append(stripped)

        if in_code_block:
            md_lines.append("```\n" + "\n".join(code_lines) + "\n```\n")

    full_md_content = "\n".join(md_lines)
    full_md_content = clean_text(full_md_content)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_md_content)

    return output_path


def convert_pdf_to_markdown_fitz(pdf_path: str, output_path: str, split_chapters: bool = False, toc_only: bool = False) -> str:
    """Converte PDF para Markdown usando PyMuPDF (fitz)."""
    doc = fitz.open(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    toc_list = doc.get_toc()
    toc_map = {}
    if toc_list:
        for level, title, page in toc_list:
            if page > 0:
                header_prefix = "#" * min(level, 6)
                clean_title = title.strip()
                toc_map[page] = f"{header_prefix} {clean_title}"

    if toc_only:
        toc_md_lines = [f"# Tabela de Conteúdos: {base_name}\n"]
        if toc_list:
            for level, title, page in toc_list:
                indent = "  " * (level - 1)
                toc_md_lines.append(f"{indent}- **{title.strip()}** (p. {page})")
        else:
            toc_md_lines.append("_Nenhum índice interno (TOC/Bookmarks) foi encontrado neste PDF._")

        toc_content = "\n".join(toc_md_lines)
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(toc_content)
        return output_path

    md_lines = [
        f"# {base_name}\n",
        "> Documento convertido de PDF para Markdown para referência de skills.\n"
    ]

    if toc_list:
        md_lines.append("## 📌 Índice do Documento\n")
        for level, title, page in toc_list[:50]:
            indent = "  " * (level - 1)
            md_lines.append(f"{indent}- [{title.strip()}](#p{page})")
        md_lines.append("\n---\n")

    for page_idx in range(len(doc)):
        page_num = page_idx + 1
        page = doc[page_idx]
        page_header = f"\n<a id='p{page_num}'></a>\n<!-- Página {page_num} -->\n"
        if page_num in toc_map:
            page_header += f"\n{toc_map[page_num]}\n\n"
        md_lines.append(page_header)

        blocks = page.get_text("blocks")
        for b in blocks:
            if b[6] == 0:
                text = b[4].strip()
                if not text:
                    continue
                if text.startswith(('•', '-', '*', '1.', '2.', '3.')):
                    md_lines.append(text)
                elif any(k in text for k in ['def ', 'import ', 'class ', 'const ', 'function ', 'public class']):
                    md_lines.append(f"```\n{text}\n```")
                else:
                    md_lines.append(text + "\n")

    full_md_content = clean_text("\n".join(md_lines))
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_md_content)

    return output_path


def convert_single_pdf(pdf_path: str, output_path: Optional[str] = None, split_chapters: bool = False, toc_only: bool = False) -> Tuple[bool, str, str]:
    """Função wrapper para converter um único PDF."""
    try:
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        if output_path is None:
            output_dir = os.path.dirname(pdf_path) if os.path.dirname(pdf_path) else "."
            output_path = os.path.join(output_dir, f"{base_name}.md")

        if HAS_FITZ:
            res = convert_pdf_to_markdown_fitz(pdf_path, output_path, split_chapters=split_chapters, toc_only=toc_only)
        else:
            res = convert_pdf_to_markdown_pdftotext(pdf_path, output_path, toc_only=toc_only)

        return True, pdf_path, res
    except Exception as e:
        return False, pdf_path, str(e)


def process_batch(pdf_dir: str, output_dir: str, toc_only: bool = False, workers: int = 4):
    """Processa um diretório inteiro de PDFs de forma concorrente."""
    if not os.path.exists(pdf_dir):
        print(f"ERRO: Diretório não encontrado: {pdf_dir}")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)
    pdf_files = []
    for root, dirs, files in os.walk(pdf_dir):
        for f in files:
            if f.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, f))

    total = len(pdf_files)
    print(f"🚀 Iniciando conversão de {total} PDFs para Markdown...")
    print(f"📂 Origem: {pdf_dir}")
    print(f"🎯 Destino: {output_dir}")
    print(f"⚡ Motor: {'PyMuPDF (fitz)' if HAS_FITZ else 'pdftotext (Poppler nativo)'}")
    print(f"🧵 Concorrência: {workers} workers\n")

    success_count = 0
    fail_count = 0

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {}
        for pdf in pdf_files:
            rel = os.path.relpath(pdf, pdf_dir)
            base_name = os.path.splitext(os.path.basename(pdf))[0]
            rel_dir = os.path.dirname(rel)
            out_folder = os.path.join(output_dir, rel_dir) if rel_dir else output_dir
            out_md = os.path.join(out_folder, f"{base_name}.md")
            
            f = executor.submit(convert_single_pdf, pdf, out_md, False, toc_only)
            futures[f] = (base_name, out_md)

        for idx, f in enumerate(as_completed(futures), 1):
            base_name, out_md = futures[f]
            success, pdf_p, msg = f.result()
            if success:
                success_count += 1
                size_kb = os.path.getsize(out_md) / 1024 if os.path.exists(out_md) else 0
                print(f"[{idx:03d}/{total:03d}] ✅ Concluído: {base_name} ({size_kb:.1f} KB)")
            else:
                fail_count += 1
                print(f"[{idx:03d}/{total:03d}] ❌ Falha em: {base_name} -> {msg}")

    print("\n" + "=" * 50)
    print(f"🏁 Processamento Finalizado!")
    print(f"✅ Sucessos: {success_count}/{total}")
    print(f"❌ Falhas: {fail_count}/{total}")
    print(f"📁 Arquivos salvos em: {output_dir}")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(description="Converte PDF para Markdown estruturado para criação de skills.")
    parser.add_argument("pdf_path", nargs="?", help="Caminho para o arquivo PDF")
    parser.add_argument("output_path", nargs="?", help="Caminho para o arquivo de saída (.md)")
    parser.add_argument("--dir", help="Pasta contendo múltiplos PDFs para conversão em lote")
    parser.add_argument("--output-dir", help="Pasta de destino para os arquivos Markdown")
    parser.add_argument("--toc-only", action="store_true", help="Extrai apenas a Tabela de Conteúdos (TOC)")
    parser.add_argument("--split-chapters", action="store_true", help="Divide o arquivo em capítulos")
    parser.add_argument("--workers", type=int, default=4, help="Número de processos concorrentes (padrão: 4)")

    args = parser.parse_args()

    if args.dir:
        out_dir = args.output_dir if args.output_dir else args.dir
        process_batch(args.dir, out_dir, toc_only=args.toc_only, workers=args.workers)
    elif args.pdf_path:
        success, pdf_p, msg = convert_single_pdf(args.pdf_path, args.output_path, split_chapters=args.split_chapters, toc_only=args.toc_only)
        if success:
            print(f"✅ Conversão concluída com sucesso! Salvo em: {msg}")
        else:
            print(f"❌ Erro ao converter {args.pdf_path}: {msg}")
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
