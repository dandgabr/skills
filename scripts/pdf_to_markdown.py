#!/usr/bin/env python3
"""
PDF to Markdown Converter for Skill Generation Reference Books
--------------------------------------------------------------
Converte livros e documentos PDF em arquivos Markdown (.md) estruturados,
preservando sumários (TOC), cabeçalhos por tamanho de fonte, listas e blocos de código.

Uso:
    python scripts/pdf_to_markdown.py <caminho_para_pdf> [caminho_saida_md]
    python scripts/pdf_to_markdown.py --dir <pasta_com_pdfs>
    python scripts/pdf_to_markdown.py <caminho_para_pdf> --toc-only
    python scripts/pdf_to_markdown.py <caminho_para_pdf> --split-chapters
"""

import sys
import os
import re
import argparse
from typing import List, Tuple, Dict, Any

# Reconfigura a saída padrão para UTF-8 no Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERRO: PyMuPDF (fitz) não está instalado. Instale com: pip install PyMuPDF")
    sys.exit(1)


def clean_text(text: str) -> str:
    """Limpa o texto extraído, corrigindo hifenização no final de linhas."""
    # Corrigir palavras hifenizadas quebradas entre linhas (ex: secu-\nrity -> security)
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    # Remover múltiplos espaços mantendo quebras de linha
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def extract_toc_map(doc: fitz.Document) -> Dict[int, str]:
    """Mapeia número da página -> Título do capítulo/seção a partir do TOC do PDF."""
    toc_map = {}
    toc = doc.get_toc()
    if toc:
        for level, title, page in toc:
            if page > 0:
                header_prefix = "#" * min(level, 6)
                clean_title = title.strip()
                toc_map[page] = f"{header_prefix} {clean_title}"
    return toc_map


def get_heading_level(font_size: float, avg_font_size: float, max_font_size: float) -> int:
    """Determina o nível do cabeçalho (#, ##, ###) com base no tamanho da fonte."""
    if font_size >= max_font_size * 0.85:
        return 1
    elif font_size >= avg_font_size * 1.4:
        return 2
    elif font_size >= avg_font_size * 1.2:
        return 3
    elif font_size >= avg_font_size * 1.1:
        return 4
    return 0


def convert_pdf_to_markdown(pdf_path: str, output_path: str = None, split_chapters: bool = False, toc_only: bool = False) -> str:
    """Converte um arquivo PDF em Markdown bem formatado."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Arquivo PDF não encontrado: {pdf_path}")

    doc = fitz.open(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    if output_path is None:
        output_dir = os.path.dirname(pdf_path) if os.path.dirname(pdf_path) else "."
        output_path = os.path.join(output_dir, f"{base_name}.md")

    print(f"📖 Processando PDF: {base_name} ({len(doc)} páginas)...")

    toc_list = doc.get_toc()
    toc_map = extract_toc_map(doc)

    # Se for apenas para extrair o índice (TOC)
    if toc_only:
        toc_md_lines = [f"# Tabela de Conteúdos: {base_name}\n"]
        if toc_list:
            for level, title, page in toc_list:
                indent = "  " * (level - 1)
                toc_md_lines.append(f"{indent}- **{title.strip()}** (p. {page})")
        else:
            toc_md_lines.append("_Nenhum índice interno (TOC/Bookmarks) foi encontrado neste PDF._")

        toc_content = "\n".join(toc_md_lines)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(toc_content)
        print(f"✅ Índice extraído com sucesso para: {output_path}")
        return output_path

    # Análise de tamanhos de fontes para heurística de cabeçalhos
    font_sizes = []
    for page_num in range(min(15, len(doc))):
        page = doc[page_num]
        try:
            blocks = page.get_text("dict")["blocks"]
            for b in blocks:
                if "lines" in b:
                    for line in b["lines"]:
                        for span in line["spans"]:
                            if span["text"].strip():
                                font_sizes.append(span["size"])
        except Exception:
            pass

    avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 10.0
    max_font_size = max(font_sizes) if font_sizes else 18.0

    md_lines = []
    md_lines.append(f"# {base_name}\n")
    md_lines.append(f"> Documento convertido de PDF para Markdown para referência de skills.\n")

    # Adicionar Índice se existir
    if toc_list:
        md_lines.append("## 📌 Índice do Documento\n")
        for level, title, page in toc_list[:50]:  # Limitar aos primeiros 50 itens no topo
            indent = "  " * (level - 1)
            md_lines.append(f"{indent}- [{title.strip()}](#p{page})")
        md_lines.append("\n---\n")

    for page_idx in range(len(doc)):
        page_num = page_idx + 1
        page = doc[page_idx]

        # Início de página com âncora
        page_header = f"\n<a id='p{page_num}'></a>\n<!-- Página {page_num} -->\n"

        # Se houver um título de capítulo no TOC para esta página
        if page_num in toc_map:
            page_header += f"\n{toc_map[page_num]}\n\n"

        md_lines.append(page_header)

        # Processar blocos de texto da página
        blocks = page.get_text("blocks")
        for b in blocks:
            # b = (x0, y0, x1, y1, text, block_no, block_type)
            if b[6] == 0:  # Bloco de texto
                text = b[4].strip()
                if not text:
                    continue

                # Checar se é um marcador de lista
                if text.startswith(('•', '-', '*', '1.', '2.', '3.')):
                    md_lines.append(text)
                # Checar se parece um bloco de código
                elif 'def ' in text or 'import ' in text or 'class ' in text or 'const ' in text or 'function ' in text or 'public class' in text:
                    md_lines.append(f"```\n{text}\n```")
                else:
                    md_lines.append(text + "\n")

    full_md_content = "\n".join(md_lines)
    full_md_content = clean_text(full_md_content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_md_content)

    print(f"✅ Conversão concluída com sucesso! Salvo em: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Converte PDF para Markdown estruturado para criação de skills.")
    parser.add_argument("pdf_path", nargs="?", help="Caminho para o arquivo PDF")
    parser.add_argument("output_path", nargs="?", help="Caminho para o arquivo de saída (.md)")
    parser.add_argument("--dir", help="Pasta contendo múltiplos PDFs para conversão em lote")
    parser.add_argument("--toc-only", action="store_true", help="Extrai apenas a Tabela de Conteúdos (TOC) para o arquivo .md")
    parser.add_argument("--split-chapters", action="store_true", help="Divide o arquivo em arquivos Markdown por capítulos")

    args = parser.parse_args()

    if args.dir:
        pdf_dir = args.dir
        if not os.path.exists(pdf_dir):
            print(f"ERRO: Diretório não encontrado: {pdf_dir}")
            sys.exit(1)
        
        pdf_files = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]
        print(f"📂 Encontrados {len(pdf_files)} arquivos PDF na pasta '{pdf_dir}'")
        for pdf in pdf_files:
            try:
                convert_pdf_to_markdown(pdf, toc_only=args.toc_only, split_chapters=args.split_chapters)
            except Exception as e:
                print(f"❌ Erro ao converter {pdf}: {e}")
    elif args.pdf_path:
        convert_pdf_to_markdown(args.pdf_path, args.output_path, split_chapters=args.split_chapters, toc_only=args.toc_only)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
