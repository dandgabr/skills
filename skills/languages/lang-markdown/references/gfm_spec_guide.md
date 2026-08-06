# Guia Rápido de Especificações GFM e CommonMark

Este documento contém resumos de sintaxes e regras essenciais de acordo com a especificação oficial do GitHub Flavored Markdown (GFM) e CommonMark.

---

## 📌 Principais Regras de Renderização

1. **Blocos de Citação e Alertas**:
   - `> [!NOTE]` -> Caixa informativa (Azul)
   - `> [!TIP]` -> Dica ou conselho (Verde)
   - `> [!IMPORTANT]` -> Informação crucial (Roxo)
   - `> [!WARNING]` -> Aviso de atenção (Amarelo/Laranja)
   - `> [!CAUTION]` -> Perigo ou alto risco (Vermelho)

2. **Caracteres de Escape**:
   - Use a barra invertida `\` para escapar caracteres especiais de Markdown: `\*asteriscos\*`, `\[colchetes\]`, `\# tralha`.

3. **Autolinks**:
   - URLs precedidas por protocolo `http://` ou `https://` são convertidas em links automaticamente no GFM se estiverem dentro de `<>`.

4. **Regras de Espaçamento e Parágrafos**:
   - Parágrafos exigem ao menos uma linha totalmente em branco entre si.
   - Espaços consecutivos no meio de frases são ignorados no HTML final.
