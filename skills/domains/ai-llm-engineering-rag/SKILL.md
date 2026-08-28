---
name: ai-llm-engineering-rag
description: Especialista em Engenharia de Aplicações com Modelos de Linguagem (LLMs), Pipelines RAG Avançados e Fine-Tuning baseado nas obras Hands-On Large Language Models (Jay Alammar) e Building Large Language Models. Cobre arquitetura Transformer (Self-Attention), Embeddings Vetoriais, Bancos de Dados Vetoriais (Milvus, Qdrant, Chroma), Estratégias de Chunking, Re-Ranking, HyDE (Hypothetical Document Embeddings) e Avaliação com RAGAS.
---

# Engenharia de Aplicações LLM e RAG Avançado

Esta skill estabelece os padrões para projetar e implementar sistemas baseados em **Modelos de Linguagem de Grande Escala (LLMs)** e **Geração Aumentada por Recuperação (RAG)** de nível corporativo.

---

## 🧠 1. Arquitetura de um Pipeline RAG Avançado

```
┌───────────────────────────┐
│ Pergunta do Usuário (Query│
└─────────────┬─────────────┘
              │
    [ HyDE / Query Expansion ]
              │
┌─────────────▼─────────────┐       ┌───────────────────────────┐
│ Gerador de Embeddings     │ ───>  │ Banco Vetorial (Vector DB)│
└─────────────┬─────────────┘       │ (Busca Híbrida: Dense+BM25│
              │                     └─────────────┬─────────────┘
              │ Recupera Top-K Chunks             │
              └───────────────────────────────────┘
                               │
                    [ Cross-Encoder Re-Ranker ]
                               │
              ┌────────────────▼────────────────┐
              │ Prompt com Contexto Enriquecido │
              └────────────────┬────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │ LLM Generator (Resposta Factual)│
              └─────────────────────────────────┘
```

---

## 🛠️ 2. Melhores Práticas de Chunking e Indexação
- **Chunking Semântico**: Divisão por parágrafos e cabeçalhos Markdown, evitando cortar sentenças no meio.
- **Tamanho Ideal**: Chunks entre 256 e 512 tokens com sobreposição (overlap) de 10% a 20%.
- **Busca Híbrida**: Combinação de busca densa (vetores de similaridade de cosseno) com busca esparsa (BM25) usando Reciprocal Rank Fusion (RRF).
