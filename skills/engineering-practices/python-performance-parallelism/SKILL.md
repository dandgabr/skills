---
name: python-performance-parallelism
description: Especialista em Otimização, Alta Performance e Paralelismo em Python baseado nas obras High Performance Python 2nd Edition (Gorelick & Ozsvald), Fast Python (Tiago Antão) e Parallel and High Performance Programming with Python 2nd Edition (Fabio Nelli). Cobre profiling (cProfile, line_profiler, py-spy, scalene), otimização de CPU e memória, NumPy/pandas vetorizados, multiprocessing vs threads vs asyncio (GIL/free-threading), Cython/Numba, GPUs (CUDA/RAPIDS), Dask/Ray/PySpark e paralelismo distribuído em cloud/serverless.
---

# Habilidade de IA: Alta Performance e Paralelismo em Python

Esta skill orienta a inteligência artificial a diagnosticar e eliminar gargalos de CPU, memória e I/O em Python, e a escalar cargas para múltiplos núcleos, máquinas e GPUs, baseada em *High Performance Python* (Gorelick & Ozsvald), *Fast Python* (Tiago Antão) e *Parallel and High Performance Programming with Python* (Fabio Nelli).

---

## 📏 1. Regras de Ouro da Otimização

1. **Meça antes de otimizar**: nunca otimize por intuição — profile primeiro (Flor regra 90/10: 90% do tempo está em 10% do código).
2. **Otimize o algoritmo antes do código**: downgrade de complexidade (O(n²) → O(n log n)) bate qualquer micro-otimização.
3. **Mova o hot loop para C**: builtin, NumPy, Cython, Numba ou biblioteca nativa — Python puro deve orquestrar, não iterar em hot paths.
4. **Trade-off consciente**: latência vs throughput vs memória vs legibilidade — documente o trade-off escolhido.
5. **Benchmark em ambiente representativo**: dados realistas, máquina isolada, warmup, repetições estatísticas (`timeit`, `pytest-benchmark`).

---

## 🔍 2. Profiling (o ponto de partida obrigatório)

| Ferramenta | Escopo | Uso típico |
| :--- | :--- | :--- |
| `cProfile` / `profile` | Funções (callers/callees, tottime/cumtime) | Primeira varredura: `python -m cProfile -s cumtime script.py` |
| `line_profiler` (`@profile`) | Linha a linha | Localizar a linha quente dentro da função identificada |
| `memory_profiler` / `tracemalloc` | Memória por linha/snapshot | Vazamentos e picos de RAM |
| `py-spy` | Sampling (CPU) em produção | Flamegraphs sem instrumentar código (`py-spy dump`/`py-spy top`) |
| `pyinstrument` | Profiler estatístico hierárquico | Overhead menor que cProfile, visão de pilha |
| `scalene` | CPU + memória + GPU juntos | Diagnóstico integrado com % interpretada vs nativa |
| `perf` + `python -X importtime` | OS level, imports | Cold start, startup time |

- **Fluxo**: cProfile → identifique a função quente → line_profiler → entenda a linha → só então otimize.

---

## 🧮 3. Otimização de CPU (Python puro → código nativo)

### 3.1 Estruturas de dados e algoritmos
- Escolha pela complexidade amortizada: `set`/`dict` (O(1) membership) vs `list` (O(n)); `collections.deque` para filas/frentes; `heapq` para prioridades; `Counter`/`defaultdict` para agregações.
- **Comprehensions > loops com append**; evite loops com chamadas de método repetidas (hoist invariants para fora do loop).
- Localize **string formatting**: f-strings/join > concatenação em loop; evite `+` acumulativo de strings (O(n²)).

### 3.2 NumPy e vetorização
- **Regra única: sem loops Python sobre arrays** — opere em vetores/ma trizes completas ( broadcasting, ufuncs).
- Vectorize fenômenos como Julia set, normalizações, distâncias: adição/subtração/array-wise em vez de elemento a elemento (ordem de 100×+ típica).
- Ideal: dados homogêneos numéricos; ruim: dados heterogêneos/estruturados (use pandas ou dicts).

### 3.3 pandas eficiente
- **Chainable e vectorized**: `.assign`, `.query`, `.eval` (numexpr backend); **nunca** `iterrows()` (use `itertuples` na pior hipótese, ou operações vetorizadas).
- `category` dtype para colunas repetidas (memória ~10× menor); downcast numéricos (`pd.to_numeric(..., downcast=)`).
- Evite `apply` em eixo row — vetorize ou use métodos nativos; índice alinhado custa: reset quando não for necessário.

### 3.4 Compilação e aceleração nativa
- **Cython**: superset tipo-estático opcional (`cdef`, typed memoryviews) — acelera loops puros; use `cython -a` para analisar interações Python↔C.
- **Numba**: `@njit(parallel=True)` (prange) — JIT LLVM para funções numéricas; `@vectorize`/`@guvectorize` para ufuncs; primeira chamada paga compilação (cache=True).
- Regra: profile → função quente isolada → Numba se numérica pura, Cython se mistura estruturas Python.

---

## 💾 4. Otimização de Memória

- **Iteradores e generators** em vez de listas materializadas (streaming de arquivos/linhas); `yield from` composição.
- Estruturas compactas: `array.array` homogêneo, `__slots__` em classes de muitos objetos, `dataclasses(slots=True)`, NumPy tipos reduzidos (float32/int32 quando suficiente).
- Del e GC: quebre ciclos de referências; `gc.collect()` em pontos de fronteira (batchs); atenção a caches LRU (`functools.lru_cache(maxsize=...)`).
- Persistência colunar: **Parquet** (schema embutido, compressão, leitura parcial por colunas/predicates) sobre CSV; memmap para arrays maiores que RAM (`np.memmap`, zarr).
- Chunk processing: pandas `chunksize`/dask para datasets maiores que memória.

---

## 🧵 5. Concorrência e Paralelismo (o mapa de decisão)

### 5.1 O GIL e o Python moderno
- **GIL**: um único thread executa bytecode Python por vez — threads puros não aceleram CPU-bound (mas liberam GIL em I/O e em chamadas NumPy/C).
- **Python 3.13+ free-threading (PEP 703, experimental)**: builds sem GIL; contexto histórico — verifique suporte de libs antes de adotar.
- `concurrent.futures.uninterruptible` não existe — conheça `ThreadPoolExecutor` (I/O-bound) vs `ProcessPoolExecutor` (CPU-bound).

### 5.2 Árvore de decisão
```
Tarefa CPU-bound?
├─ Numérica/Array → NumPy/Numba (@njit parallel)/GPU
├─ Função Python pura isolável → multiprocessing/ProcessPoolExecutor
│   └─ serializável (pickle)? Não → shared memory (multiprocessing.shared_memory)
└─ Mixed → joblib/Swarm paralelismo nivelado
I/O-bound?
├─ Muitas conexões/concorrência alta (1000+) → asyncio (uvloop)
├─ I/O bloqueante legado → threads (ThreadPoolExecutor)
└─ Firewall de subprocessos → multiprocess na borda apenas
Máquina cheia → Dask (distribuído local) / Ray (clusters)
```

### 5.3 multiprocessing correto
- `ProcessPoolExecutor` / `Pool.map` com chunks eficientes (`chunksize` ajustado — muito pequeno = overhead de IPC, muito grande = load imbalance).
- Custo de serialização: `pickle` de argumentos/retorno — prefira funções puras com entradas/saídas compactas (arrays NumPy).
- **Compartilhamento**: `multiprocessing.shared_memory.SharedMemory`/`Array`; manager proxy só em baixa frequência; fork vs spawn (Linux fork rápido, spawn seguro multiplataforma; vê compatibilidade com CUDA).

### 5.4 asyncio
- Para I/O bound de alta concorrência (HTTP websockets, scrapers, microservices mesh).
- `async/await` correto: nunca bloqueie o event loop (I/O síncrono pesado, CPU-bound); rode bloco CPU em `run_in_executor`.
- `asyncio.gather` (fan-out), `Semaphore` (limite), `aiohttp`/`httpx.AsyncClient` reutilizado (connection pooling habilitado).

### 5.5 Distribuído: Dask, Ray ou Spark
- **Dask**: parallelize pandas/NumPy scaláveis (`dask.dataframe`), scheduler local → cluster (SLURM/K8s); particionamento colunar lazy.
- **Ray**: tasks (stateless remote functions), actors (stateful), Ray Data/Datasets para ML pipelines; autoscaling cloud.
- **PySpark**: >= TB scale; DataFrames com Catalyst optimizer; prefira UDFs pandas (Arrow) a row UDFs Python.
- **joblib**: embarrassingly parallel simples com backend memmap (NumPy grande, Zero-copy).

---

## 🎮 6. GPU e Aceleração por Hardware

- **CUDA via Python**: Numba `@cuda.jit` (kernels manuais), CuPy (API espelhada do NumPy na GPU), PyTorch ops tensor.
- **RAPIDS**: cuDF (pandas-like na GPU) e cuML (sklearn-like) para pipelines de dados ml em datasets médios/grandes.
- Regra do transferência: opere *no local* — minimize transferências CPU↔GPU (batch operations, kernels fundidos); dias de transferência você paga caro.
- Consideração de engenharia: a GPU compensa quando ocompute dominates; dados tabulares pequenos ficam melhor em CPU/vectorized.

---

## 🏹 7. Multiprocessamento Avançado (FPGA, Quantum e Serverless)

- **Servidores sem sentido** (serverless, cap. 14): map-reduce sem servidor com AWS Lambda (fan-out com SQS/Step Functions); adequado para embaralhar processos event-driven.
- **FPGA (cap. globais)**: via PYNQ/Zynq com Python — nicho high-frequency trading/inference; altíssimo custo de engenharia.
- **Computação quântica (cap. 16)**: Qiskit em simulação — apenas experimental.

---

## 🧪 8. Protocolo de Otimização (checklist executável)

1. **Meça o estado base**: tempo (wall + CPU) e memória (tracemalloc) com dados representativos.
2. **Profile**: cProfile → line_profiler → scalene (CPU vs nativa vs memória).
3. **Descarte o trabalho desnecessário**: caching (`lru_cache`), lazy loading, dedupe, early exit, reuso de resultados.
4. **Aplique a hierarquia de melhorias**: algoritmo/estrutura → vetorização NumPy/pandas → compilação (Numba/Cython) → concorrência (async/threads/processes) → distribuído (Dask/Ray/Spark) → hardware (GPU).
5. **Valide**: mesmo resultado (testes de igualdade), benchmark estatístico (n ≥ 5, variância), memória monitorada.
6. **Documente**: gargalo original, técnica aplicada, ganho (∞ tempo / memória) e trade-off assumido.

---

## 🔗 Integração com Outras Skills

- [latency-engineering](../latency-engineering/SKILL.md): modelagem de capacidade (Little/Amdahl) antes de escalar verticalmente.
- [lang-python](../../languages/lang-python/SKILL.md): idiomas e estilo base da linguagem.
- [lang-java](../../languages/lang-java/SKILL.md): contraste de concorrência (GIL vs virtual threads) e JVM vs CPython.
- [lang-csharp](../../languages/lang-csharp/SKILL.md): contraste de async/await e paralelismo Task Parallel Library.
- [data-intensive-systems](../../databases/data-intensive-systems/SKILL.md): batch processing e pipelines data-intensive (MapReduce/Dataflow).
- [code-optimizer](../../roles/code-optimizer/SKILL.md): o agente de otimização orquestra esta skill em refatorações Python.