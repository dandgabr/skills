# ADR-0001: Seleção de Banco de Dados Relacional para o Módulo Financeiro

- **Status**: Aprovado
- **Data**: 2026-08-06
- **Autores**: Equipe de Arquitetura de Software

---

##  Contexto e Problema

O módulo financeiro do sistema necessita de forte garantia de integridade ACID, transações complexas e suporte a consultas relacionais de alto desempenho para geração de relatórios regulatórios.

---

## 🎯 Opções Consideradas

1. **PostgreSQL 15** (Relacional)
2. **MongoDB 6.0** (Documentos)
3. **MySQL 8.0** (Relacional)

---

## ⚡ Decisão

Decidimos adotar o **PostgreSQL 15** como o banco de dados principal do módulo financeiro.

### Justificativa
- Suporte nativo robusto a transações ACID e isolamento de transações.
- Excelente desempenho com consultas complexas e suporte nativo ao tipo `JSONB` quando necessário flexibilidade.
- Ferramentas maduras de backup, replicação e monitoramento no ecossistema cloud.

---

## 📊 Consequências

### Positivas
- Garantia de consistência transacional sem necessidade de compensações manuais na aplicação.
- Facilidade de integração com ORMs modernos (Prisma, TypeORM).

### Negativas / Riscos
- Requer ajuste fino de índices para tabelas de grande volume de auditoria.
- Necessidade de gerenciar migrações de schema de forma automatizada no pipeline de CI/CD.
