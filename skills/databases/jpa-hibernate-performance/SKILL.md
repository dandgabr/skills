---
name: jpa-hibernate-performance
description: Especialista em Performance de Persistência Java (JPA/Hibernate) baseado em High-Performance Java Persistence (Vlad Mihalcea). Cobre JDBC batching, N+1 query problem e fetch strategies (JOIN FETCH, EntityGraph), FlushOperationQueue e ActionQueue, dirty checking, cache de primeiro e segundo nível (read-through/nonstrict-read-write), locking otimista/pessimista, paginação eficiente (keyset vs OFFSET), transações e isolamento, e tuning SQL por banco (EXPLAIN, execution plans).
---

# Habilidade de IA: Alta Performance em Persistência Java (JPA/Hibernate)

Esta skill orienta a inteligência artificial a desenhar a camada de persistência Java/JPA com foco em performance, baseada na obra *High-Performance Java Persistence* (Vlad Mihalcea), cobrindo JDBC puro, JPA e Hibernate.

---

## 🧱 1. Arquitetura da Camada de Persistência

- **Escolha consciente da ferramenta**: JDBC batch puro para ETL/bulk; JPA+Hibernate para OLTP de domínio; SQL nativo/projection para consultas analíticas — **não force ORM em tudo**.
- ** stereotipos de acesso**: entidades de domínio (aggregates com transações curtas), DTO projections (queries de leitura), value types (embeddables imutáveis).
- **Transações curtas**: scope da transação = menor unidade atômica; nunca rode UI/remote calls dentro de transação aberta.

---

## 🔥 2. Problema N+1 e Estratégias de Fetch

### Diagnóstico
- **N+1**: uma query para a entidade raiz + N queries lazy ao navegar associações; detecte com `hibernate.generate_statistics=true`, `nullSafeGet`/SQL log, e testes de hidratação.

### Mitigações (em ordem de preferência)
1. **JOIN FETCH** em JPQL: `SELECT a FROM Author a JOIN FETCH a.books WHERE a.id = :id` — busca em ida única.
2. **@EntityGraph**: definição declarativa de fetch plan por caso de uso (sem poluir queries).
3. **`@_BATCH(size)` / `hibernate.default_batch_fetch_size`**: transform N consultas em N/size consultas `IN (...)` — o melhor equilíbrio para associações arbitrárias.
4. **`@Fetch(FetchMode.SUBSELECT)`**: para coleções acessadas em massa na mesma transação.
5. **`@BatchSize`** em lazy collections; `@LazyCollection(LazyCollectionOption.EXTRA)` para count-only.

### Regras
- `FetchType.LAZY` em **toda** associação (o padrão safe); UNI-side `@ManyToOne(optional=false)` pode ser EAGER com critério.
- Nunca use "open session in view" em produção — vilão clássico de N+1 e de transações longas.
- Para muitos-para-muitos grandes, prefira **duas bidirecionais unilaterais** com extra `@LazyCollection(ExtraLazyType)`. Acesso via DTO quando o modelo de escrita não precisa da coleção.

---

## 📦 3. Write-Behind, Flush e Batching

### ActionQueue e Flush Order
- Hibernate ordena operações na `ActionQueue` (inserts → updates → collection removes → deletions), já pensado para FK/UNIQUE; entenda a ordem em transações multi-entidade.
- `FlushModeType.AUTO` flutua em queries "[flush antes da query que pode tocar dados pendentes]"; use `COMMIT` para hot paths read-only e flush controle manual (`em.flush()`).

### JDBC Batching
- Ative: `hibernate.jdbc.batch_size` (30–50 típico), `order_inserts=true`, `order_updates=true`, `batch_versioned_data=true`.
- **Requisito do driver**: `rewriteBatchedStatements` (MySQL), `reWriteBatchedInserts` (PostgreSQL) para batch real no wire.
- **IDENTITY desabilita batching de inserts** (Hibernate precisa do id gerado); prefira `SEQUENCE` (com `allocationSize` 50+) ou `TABLE` com pooler (pooled-lo).
- Bulk: `JPQL/ HQL bulk update+delete` (bypassam contexto de persistência), ` StatelessSession`, ou `Session.doWork` com JDBC directo para grandes volumes.

### Dirty Checking e Estado
- Dirty checking default varre entidades do contexto; para entidades grandes/read-only use `@Immutable` ou `Session.refresh`.
- `@DynamicUpdate` gera UPDATE só das colunas alteradas (menos tráfego, evita sobrescrever) — cuidado com planos de consulta menos cacheáveis.
- Limite a **tamanho da Session/Persistence Context**: `clear()`/`detach()` em loops longos; meça com `em.getEntityManagerFactory().getPersistenceUnitUtil()`/estatísticas.

---

## 🗄️ 4. Cache (L1, L2 e Query Cache)

| Cache | Escopo | Uso recomendado |
| :--- | :--- | :--- |
| **First-level (Session)** | Transação/Sessão | Identidade e byteaço de objeto; sempre ativo |
| **Second-level (L2)** | SessionFactory (multi-sessão) | Dados read-mostly, referências; datasense TTL/versionado |
| **Query cache** | Resultado de consulta | Só com poucos results e tabelas estáveis (invalidação é carreg) |

- **Concurrence strategies** (da mais estrita para a mais leve): `READ_WRITE` →`NONSTRICT_READ_WRITE`→ `READ_ONLY`.
  - `NONSTRICT_READ_WRITE`: lock assíncrono leve; ok em read-mostly; nunca em alta escrita concorrente (invalida demais).
- **Providers**: JCache (Ehcache 3, Infinispan, Caffeine-bridge); dimensione TIs de L2 do tamaño do working set (não "cache tudo").
- **Read-through no app**: padrão Cache-Aside explícito ([system-design-scalability](../../engineering-practices/system-design-scalability/SKILL.md)) muitas vezes supera L2 quando o domínio é propício.

---

## 🔒 5. Locking, Concurrency e Transações

- **Otimista (versão/numérica)**: trate `OptimisticLockException` com retry (transação curta); ideal para contenda média/baixa. Increment manual de version em bulk actions.
- **Pessimista**: `PESSIMISTIC_WRITE` (SELECT FOR UPDATE) para filas de job, contadores críticos, bid[reserve]-stock; tempo de lock mínimo.
- **Lost update**: a maior plaga silenciosa — leitor+escritor em transações separadas; mitigações: lock otimista, `PESSIMISTIC_FORCE_INCREMENT`, ou atomicidade no SQL (`UPDATE ... SET x = x + 1`).
- **Isolamento**: READ_COMMITTED + versionamento resolve 90%; SERIALIZABLE só com boa justificativa (custo em locks/anomalias até no Postgres SSI).

---

## 📑 6. Paginação e Consultas

- **OFFSET escalonadamente ruim** (varre e descarta): para deep pagination use **keyset/seek**(`WHERE (a.id > :last) ORDER BY a.id LIMIT :n`) — custo constante.
- SQL padrão moderno: `OFFSET ? ROWS FETCH FIRST ? ROWS ONLY` (SQL:2008); dialetos variam — deixe o Hibernate mapear.
- **Projections**: `SELECT new com.x.Dto(...)` para leituras (contra tráfego de entidades geridas); `Tuple`/interface-based projections para flexibilidade.
- **Criteria API** para filtros dinâmicos; cuidado com geração de planos não-cachaveis (use query plan cache com eps constantes).
- Medição por banco: `EXPLAIN (ANALYZE, BUFFERS)` (Postgres), set showplan (SQL Server), autotrace (Oracle) — valide o plano antes e depois ([db-postgresql](../db-postgresql/SKILL.md)).

---

## 🧭 7. Protocolo de Otimização de Persistência

1. **Meça primeiro**: `hibernate.generate_statistics=true` em dev; APM em prod; identifique N+1, queries repetidas, sessões longas.
2. **Corrija fetch** (JOIN FETCH/EntityGraph) antes de mexer em cache.
3. **Ative batching** e verifique wire (logs do driver) — batch que não chega ao banco é só overhead.
4. **Cache com política**: L2 para read-mostly com TTL-versions; query cache raramente.
5. **Locking por caso**: otimista default; pessimista só micro-intervalos.
6. **Paginação keyset**; OFFSET só em páginas iniciais pequenas.
7. **Testes de carga** com dados realistas (cardinalidade e skew) e verificação de planos pós-índices/migração.
8. **Django-like prproviders**: driver e dialeto sempre atualizados (otimizações chegam por versão do Hibernate/driver JDBC).

---

## 🔗 Integração com Outras Skills

- [lang-java](../../languages/lang-java/SKILL.md): fundamentos de JPA sob concorrência e JVM.
- [db-postgresql](../db-postgresql/SKILL.md), [db-mariadb](../db-mariadb/SKILL.md), [db-sqlite](../db-sqlite/SKILL.md): tuning do banco de destino (EXPLAIN, índices, buffer).
- [dba-database-administrator](../../roles/dba-database-administrator/SKILL.md): modelagem, índices e consultas de referência.
- [backend-developer](../../roles/backend-developer/SKILL.md): integração em serviços/APIs Java com transações curtas.
- [latency-engineering](../../engineering-practices/latency-engineering/SKILL.md): round-trips do pool de conexões e N+1 como vilões de p99.