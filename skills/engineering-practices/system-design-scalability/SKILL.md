---
name: system-design-scalability
description: Especialista em System Design, Engenharia de Sistemas em Larga Escala e Arquiteturas Distribuídas de Alta Disponibilidade. Cobre sharding, particionamento, replicação, consistência eventual (CAP/PACELC), caching distribuído, balanceamento de carga, rate limiting, circuit breakers e resiliência.
---

# System Design e Engenharia de Sistemas em Larga Escala

Esta skill fornece os princípios, padrões e heurísticas para projetar sistemas distribuídos escaláveis, confiáveis, tolerantes a falhas e de alta performance, baseando-se em obras de referência da indústria (*System Design* por Karan Pratap Singh e *Strategic Monoliths and Microservices* por Vaughn Vernon).

---

## 🏛️ 1. Princípios e Teoremas Fundamentais

### Teorema CAP & Teorema PACELC
- **CAP**: Em caso de Partição de Rede (**P**), o sistema deve escolher entre Consistência (**C**) ou Disponibilidade (**A**).
  - **CP (Consistency + Partition Tolerance)**: Bancos com locks estritos, consenso Paxos/Raft (ex: Spanner, etcd, ZooKeeper).
  - **AP (Availability + Partition Tolerance)**: Sistemas de alta disponibilidade com consistência eventual (ex: Cassandra, DynamoDB).
- **PACELC**: Se houver Partição (**P**), escolha entre Disponibilidade (**A**) e Consistência (**C**); **E**lse (em operação normal), escolha entre Latência (**L**) e Consistência (**C**).

### Modelos de Consistência
1. **Strong Consistency (Consistência Estrita)**: Toda leitura retorna a escrita mais recente.
2. **Sequential / Linearizable Consistency**: Ordem global de operações preservada.
3. **Eventual Consistency (Consistência Eventual)**: Se nenhuma nova atualização ocorrer, todas as réplicas eventualmente convergirão.
4. **Read-Your-Writes / Monotonic Reads**: Garantias essenciais para experiência do usuário em nós replicados.

---

## 🧱 2. Padrões de Escalabilidade de Dados

### Estratégias de Sharding e Particionamento
- **Horizontal Sharding (Range-Based)**: Divisão por faixas de chaves (ex: ID 1-1M no Shard A, 1M-2M no Shard B). Suscetível a *Hotspots*.
- **Hash-Based Sharding**: Distribuição via `hash(chave) % num_shards`. Requer re-sharding custoso ao adicionar nós.
- **Consistent Hashing**: Anel virtual com nós virtuais (V-Nodes). Minimiza o deslocamento de chaves ao adicionar ou remover servidores (utilizado por DynamoDB, Cassandra, CDNs).

### Estratégias de Replicação
- **Single-Leader (Master-Slave)**: Escritas no líder, leituras distribuídas nas réplicas. Risco de *replication lag*.
- **Multi-Leader**: Múltiplos datacenters ativos com reconciliação assíncrona (CRDTs ou Last-Write-Wins).
- **Leaderless (Quorum Reads/Writes)**: Baseado em fórmula de Quorum: $W + R > N$ (onde $N$ é o fator de replicação, $W$ nós para escrita e $R$ nós para leitura garantem consistência forte).

---

## ⚡ 3. Padrões de Caching Distribuído

| Estratégia | Fluxo de Operação | Prós | Contras |
| :--- | :--- | :--- | :--- |
| **Cache-Aside (Lazy Loading)** | Aplicação consulta cache; se miss, busca no BD e atualiza cache. | Apenas dados consultados são cacheados; resiliente a falhas no cache. | Penalidade de latência em cache miss; risco de dados desatualizados. |
| **Read-Through** | Aplicação consulta o cache; o cache busca no BD em caso de miss. | Código de aplicação limpo e unificado. | Requer plugins/handlers dedicados no cache. |
| **Write-Through** | Aplicação escreve no cache, e o cache atualiza o BD sincronamente. | Dados no cache sempre atualizados e consistentes. | Maior latência na escrita (espera confirmação de ambos). |
| **Write-Behind (Write-Back)** | Aplicação escreve no cache; cache grava no BD assincronamente em lote. | Latência mínima de escrita e absorção de picos de I/O. | Risco de perda de dados se o cache falhar antes do flush no BD. |

### Políticas de Evicção
- **LRU (Least Recently Used)**: Descarta o item menos acessado recentemente (padrão Redis).
- **LFU (Least Frequently Used)**: Descarta o item com menor contagem total de acessos.
- **TTL (Time to Live)**: Expiração determinística para balancear frescor e uso de memória.

---

## 🛡️ 4. Padrões de Resiliência e Concorrência

```
               ┌────────────────────────┐
               │    Cliente / Gateway   │
               └───────────┬────────────┘
                           │
                 [ Rate Limiting & WAF ]
                           │
              ┌────────────▼────────────┐
              │     Circuit Breaker     │
              │  (Closed / Open / Half) │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │   Bulkhead & Isolation  │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │    Serviço Dependente   │
              └─────────────────────────┘
```

1. **Circuit Breaker (Disjuntor)**:
   - **Closed**: Requisições passam normalmente; conta taxa de erros.
   - **Open**: Falhas excedem limiar; rejeita requisições imediatamente (*fail-fast*) sem onerar o backend.
   - **Half-Open**: Permite tráfego canário para testar se o serviço downstream recuperou-se.
2. **Bulkhead (Compartimentalização)**:
   - Isola pools de threads, conexões e memória entre serviços críticos para evitar que uma falha em cascata derrube todo o sistema.
3. **Rate Limiting & Throttling**:
   - Algoritmos: **Token Bucket**, **Leaky Bucket**, **Fixed Window**, **Sliding Window Log**.
4. **Idempotency Keys**:
   - Uso de chaves UUID únicas no cabeçalho `Idempotency-Key` com armazenamento temporário em Redis para evitar duplicação em retentativas de rede.

---

## 📊 5. Checklist de System Design Interview & Arquitetura Real

- [ ] **1. Clarificação de Requisitos**: Escopo funcional, volumetria (DAU/MAU), taxa de leituras vs escritas (RPS), tamanho médio dos dados.
- [ ] **2. Estimativa de Capacidade (Back-of-the-Envelope)**:
  - Throughput de escrita/leitura (QPS).
  - Armazenamento em 5 anos (com fator de replicação).
  - Largura de banda de rede (Ingress/Egress).
  - Tamanho da memória RAM de Cache (regra de 80/20: 20% das chaves geram 80% do tráfego).
- [ ] **3. Definição das APIs**: Contratos REST/gRPC com tipos de dados, paginação e status codes RFC 7807.
- [ ] **4. Modelo de Dados**: Escolha entre Relacional (ACID) vs NoSQL (Document/Key-Value/Columnar/Graph).
- [ ] **5. Diagrama de Alto Nível**: Componentes centrais e fluxo primário de requisição.
- [ ] **6. Deep Dives Técnicos**: Resolução de gargalos, particionamento, replicação, failover e observabilidade.
