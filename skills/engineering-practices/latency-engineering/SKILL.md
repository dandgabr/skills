---
name: latency-engineering
description: "Especialista em Engenharia de Latência e Otimização de Delay em Sistemas de Software baseado na obra Latency: Reduce delay in software systems (Pekka Enberg). Cobre as Leis da Latência (Little, Amdahl, Teoria de Filas), latência de cauda (tail latency p99/p99.9) e Coordinated Omission, arquiteturas low-latency (sharding, replicação, consistência, RPC), otimização de hardware (CPU, cache hierárquico, NUMA, kernel bypass) e eliminação de trabalho desnecessário (lazy loading, caching, batching, pré-computação)."
---

# Habilidade de IA: Engenharia de Latência (Latency Engineering)

Esta skill orienta a inteligência artificial a analisar, modelar e reduzir a latência ponta a ponta de sistemas de software, cobrindo desde os fundamentos teóricos (teoria de filas) até técnicas de implementação de baixo nível, baseada na obra *Latency: Reduce delay in software systems* (Pekka Enberg, Manning).

---

## 📏 1. Leis Fundamentais da Latência

### Lei de Little (Little's Law)
Conecta latência (L), throughput (X) e concorrência (N): **N = L × X**
- Use para dimensionar pools de conexões, thread pools e buffers: com 1.000 req/s e latência alvo de 50 ms, o sistema precisa de ~50 requisições concorrentes.
- Se o throughput estiver saturado e N crescer indefinidamente, toda capacidade extra vai para a fila (latência explode).
- Atenção às premissas: vale apenas em regime estacionário; sistemas instáveis violam a premissa do teorema.

### Lei de Amdahl (Amdahl's Law)
Limite de speedup por paralelização: **Speedup = 1 / (F + (1 − F)/N)**, onde F é a fração serial.
- A fração serial é o divisor de águas: mesmo com infinitos núcleos, o speedup máximo é 1/F.
- Use para estimar retornos decrescentes de paralelização antes de investir em mais hardware.

### Teoria de Filas & Utilização
- A latência cresce de forma **não-linear** conforme a utilização (ρ) se aproxima de 1 (fila M/M/1: latência ∝ 1/(1−ρ)).
- Regra prática: mantenha a utilização de serviços de latência crítica abaixo de ~70–80%; acima disso, o p99 cresce exponencialmente.

---

## 📊 2. Latência de Cauda (Tail Latency) e Coordinated Omission

- **Percentis, não médias**: Meça e otimize p99/p99.9, pois em escala um único usuário faz poucas requisições e será afetado pela cauda.
- **Sistema distribuído amplifica a cauda**: um pipeline de 10 serviços com p99 de 100 ms pode ter latência ponta a ponta de cauda muito pior (fan-out multiplica a chance de um caminho lento).
- **Coordinated Omission (Gil Tene)**: load generators que sincronizam requisições (closed-loop) escondem períodos de stall e subestimam drasticamente a cauda. Corrija reportando latências das requisições que *deveriam* ter sido enviadas durante o stall.
- **Head-of-line blocking**: uma requisição lenta em fila (mesmo single-threaded como Node.js ou em filtros comuns de frameworks) atrasa todas as posteriores — mitigar com timeouts agressivos, isolamento de pools e filas por classe.
- **Hedged requests / request replication**: envie requisições redundantes após um limiar (ex: p95) para cortar a cauda em réplicas e caches (processo Retwis/fan-out do Google).

---

## ⚙️ 3. Redução de Latência por Camada

### Nível Aplicação (elimine trabalho desnecessário)
- **Não faça NFS/Disk I/O sincrono no caminho crítico**: tudo que não é estritamente necessário deve ser lazy, assíncrono ou pré-computado.
- **Caching (com invalidação cuidadosa)**: dados imutáveis/estáticos; atenção ao stampede (thundering herd) — use lock único de recompute e jitter de TTL.
- **Batching com trade-off consciente**: agrupar requisições aumenta throughput mas adiciona latência; em low latency prefira batching por tempo janela curtíssima (Nagle off, janelas de coalescência em ms).
- **Pré-computação e materialização**: calcule agregações off-line (event sourcing + projeções) em vez de on-request.
- **Serialização**: prefira binários compactos (Protobuf, Avro, FlatBuffers) a JSON no hot path; evite re-serializações múltiplas da mesma estrutura.

### Nível RPC / Rede
- Reduza round-trips: combine chamadas, use pipelining de conexões, HTTP/2 multiplexing ou gRPC.
- **UDP e QUIC**: protocolos com 0-RTT e recuperação sem head-of-line blocking de transporte.
- Timeouts e retry budgets com backoff exponencial + jitter; nunca retries infinitos em cadeia (amplificação).

### Nível Hardware e Runtime
- **Hierarquia de cache da CPU**: organize estruturas de dados para data locality (arrays/AoS vs SoA, cache lines de 64 bytes, evite pointer chasing).
- **Branch prediction e prefetching**: o hardware prevê saltos e pré-carrega caches; estruturas de dados "hot" compactas batem estruturas "rsticas" genéricas.
- **NUMA**: em servidores multi-socket, ancore threads e memória no mesmo socket (`numactl`), evitando cross-socket traffic.
- **Kernel bypass / NICs modernas**: para latências de microssegundos, técnicas como busy-spin em vez de syscalls bloqueantes, huge pages, e cores isolados (isolcpus + IRQ affinity).
- **Alocação de memória**: evite the GC pause path em runtimes gerenciados; prefira objetos de vida curta (Gen0/Young gen) e pools de objetos para alocações grandes.

### Nível Sistemas Distribuídos (consistência × latência)
- **PACELC**: em operação normal, *Else* Latency vs Consistency — réplicas fortemente consistentes pagam round-trip; consistency eventual aceita leituras stale com menor latência.
- **Sharding**: consultas single-shard batem consultas cross-shard; escolha chaves de particionamento que agrupem dados acessados juntos.
- **Replicação assíncrona** reduz latência de escrita mas cria janela de stale reads; sincronia paga RTT por escrita.
- **Consensus (Raft/Paxos)** exige majoritário — preveja RTT de confirmção; deploy em topologias que minimizam a distância física entre réplicas.

---

## 🧪 4. Protocolo de Otimização em 6 Passos

1. **Defina o SLO de latência por operação** (p50/p99/p99.9 e peak) antes de otimizar; ausência de alvo = otimização cega.
2. **Meça com telemetria correta**: tracing distribuído (OpenTelemetry), timers de alta resolução, rédução de coordenated omission nos benchmarks.
3. **Modele a capacidade** com Little's Law/Amdahl para validar hipóteses numéricas antes de refatorar.
4. **Encontre o gargalo real** (profile flame graphs, DTrace/perf, métricas por etapa do pipeline) — não chute.
5. **Elimine o trabalho, depois otimize o trabalho restante** (a otimização mais rápida é não fazer).
6. **Valide sob carga real** com A/B ou blue/green; latência deve ser observada em produção continuamente (sintéticos + RUM).

---

## 🔗 Integração com Outras Skills

- [system-design-scalability](../system-design-scalability/SKILL.md): trade-offs CAP/PACELC, sharding e caching distribuído em larga escala.
- [data-intensive-systems](../../databases/data-intensive-systems/SKILL.md): réplicas, particionamento e filas que influenciam a latência ponta a ponta.
- [lang-python](../../languages/lang-python/SKILL.md) e [python-performance-parallelism](../python-performance-parallelism/SKILL.md): otimização de CPU/GC em runtimes interpretados.
- [observability-correlation](../../mapping/observability-correlation/SKILL.md): instrumentação (traces, métricas) para localizar gargalos.
- [lang-java](../../languages/lang-java/SKILL.md): ajustes de JVM (GC, JIT, thread pools incentives à latência).