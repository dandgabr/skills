# Guia do Livro: Hands-On JavaScript High Performance (Justin Scherer)

> Referência consolidada por capítulo do livro *Hands-On JavaScript High Performance* (Justin Scherer, Packt Publishing). Autora: Justin Scherer. Fonte: /tmp/opencode/books/full2/full_Hands-On JavaScript High Performance (Justin Scherer) (z-library.sk, 1lib.sk, z-lib.sk).md.

---

## Capítulo 1 — Tools for High Performance on the Web

Ferramentas de profiling e benchmarking nos principais navegadores.

- **DevTools por browser**: Edge (fork Chromium), Safari (Web Inspector), Firefox, Chrome — cada motor otimiza diferente.
- **Chrome Performance tab** (in-depth): gravação de timeline de runtime com categorias Scripting/Rendering/Painting, flame chart de call stacks e event log de interações (click, paint, GC).
- **Chrome Memory tab** (in-depth): Heap Snapshot (comparação de snapshots para achar objetos retidos/vazamentos), Allocation instrumentation on timeline, Allocation sampling.
- **Chrome Rendering tab** (in-depth): Paint flashing, FPS meter, Layout Shift regions — telemetria visual em tempo real.
- **jsPerf**: benchmarking correto — cuidado com otimizações do motor (dead code), rode em múltiplos navegadores, sem código extrano nos casos de teste.

**Técnicas**: profiling-first methodology, comparação `for` loop vs `Array.filter` em benchmark (loop nativo vence em hot paths).

## Capítulo 2 — Immutability versus Mutability: The Balance between Safety and Speed

- **Fascínio atual pela imutabilidade**: Redux e o Flux pattern — store imutável, actions, reducers, mudança por referência para `connect`/`shouldComponentUpdate`.
- **Immutable.js**: `List`, `Map`, `Set` persistentes (tries com structural sharing) — código mais limpo, porém mais lento e mais memória que nativo em datasets grandes; comparação prática convertendo listas de listas em lista de objetos (CSV-like): vanilla vence.
- **Writing safe mutable code**: encapsular mutação, evitar estado compartilhado mutante entre módulos.
- **RAII (Resource Allocation Is Initialization / SBRM)**: liberar recursos no mesmo escopo que os criou (inspiração C++/Rust).
- **Functional style**: lazy evaluation (generators/iteradores avaliam sob demanda), tail-end recursion (prefira iteração; TCO não garantido nos engines), currying (composição com custo de closures).

## Capítulo 3 — Vanilla Land: Looking at the Modern Web

Feature set do ECMAScript até 2020 com lente de performance.

- `let`/`const` block scoping, arrow functions, classes e modules (ESM).
- **Collection types**: `Map`, `Set`, `WeakMap`, `WeakSet` (chaves fracas permitem GC).
- **Reflection e Proxies**: interceptação de operações (base de reatividade); custo por acesso.
- Spread operator, destructuring, power operator, parameter defaults, string templates.
- **Typed Arrays** (`Int8Array`...`Float64Array`, `ArrayBuffer`) para memória contígua/tipada; **BigInt** para inteiros arbitrários; Internationalization API.
- **DOM**: `querySelector`, `DocumentFragment` (inserções em lote = 1 reflow), Shadow DOM, Web Components, `<template>`.
- **Fetch API + Promises**: encadeamento, `AbortController` para cancelar requests.

## Capítulo 4 — Practical Example: A Look at Svelte and Being Vanilla

- Svelte = framework **compilado para vanilla JS**; sem virtual DOM e sem runtime em produção.
- `svelte` compila declarações reativas em código imperativo mínimo de atualização do DOM.
- Construção prática: Todo app e weather app — componentes pequenos, estado local, atualizações cirúrgicas.
- Lição: empurrar trabalho do runtime para o build time é arquitetura de performance.

## Capítulo 5 — Switching Contexts: No DOM, Different Vanilla (Node.js)

- Instalação do Node.js e papel do `package.json` (scripts, deps, type).
- Módulos nativos: `fs` (arquivos), `net` (sockets), `http` (servidor) — sem bibliotecas para o básico.
- **Primeira introdução a streams** (non-blocking I/O) e visão geral de módulos ES em Node.
- Debugging e inspeção de código Node (inspector).

## Capítulo 6 — Message Passing: Learning about the Different Types

- Comunicação local com `net` (sockets locais/TCP) e IPC entre processos.
- **cluster module**: workers por núcleo para escalar além do single-thread.
- TCP (confiável, ordenado) vs **UDP** (latência mínima, sem handshake).
- **HTTP/2**: multiplexing, binário, header compression — sem head-of-line blocking do HTTP/1.1.
- **HTTP/3/QUIC**: UDP-based, 0-RTT; biblioteca `node-quic`.

## Capítulo 7 — Streams: Understanding Streams and Non-Blocking I/O

- Interfaces Readable/Writable/Duplex/Transform e backpressure via `highWaterMark`.
- Implementação de um Readable customizado, Writable, Duplex e Transform do zero.
- **Generators com streams** para pipelines concisos.

## Capítulo 8 — Data Formats: Different Data Types Other Than JSON

- JSON nativo (`JSON.parse`/`stringify`) como baseline; schema-less vs schema-based.
- Implementação de um **encoder/decoder binário próprio** (schema enviado com os dados).
- **MessagePack** (lib `what-the-pack`): buffer pré-alocado (`initialize(2**22)`), payload binário compacto — mas pode não ser menor nem mais rápido que JSON nativo; trade-offs.
- **Protocol Buffers (proto3)**: schema compartilhado, IDs numéricos de campo, encoding compacto; libs em Node e browser.

## Capítulo 9 — Practical Example: Building a Static Server

- Aplicação dos capítulos 5–8: servidor estático com `fs` + `http` + streams.
- Sistema de templating (server-side rendering básico).
- **Caching** (com TTL / LRU — "ubiquitous with caches") e **clustering** para escala.

## Capítulo 10 — Workers: Dedicated and Shared Workers

- **Dedicated Workers**: offload de processamento da main thread; comunicação via `postMessage`.
- **Custo do structured clone**: 100.000 objetos levaram 800 ms–1,7 s e 80–100 MB de heap (medido com `Date.now()` + Performance tab).
- **Transferrables**: `postMessage(view, [view.buffer])` — transferência zero-copy de binários (Int32Array de 1M elementos), remetente perde acesso (buffer detached).
- Enviando dados binários no browser; **Shared Workers** para compartilhar entre páginas/abas.
- **Shared cache em worker**: "decorating data" (join/attribution no frontend) com cache em memória no worker; menciona TTL/LRU.

## Capítulo 11 — Service Workers: Caching and Making Things Faster

- Ciclo de vida do ServiceWorker (install → waiting → activate), escopo.
- **Cache de páginas/templates para uso offline** (Cache Storage) — base de PWA.
- **Save requests for later**: enfileirar mutações offline e reproduzir ao voltar a rede.

## Capítulo 12 — Building and Deploying a Full Web Application

- **Rollup**: bundler de ES modules com tree shaking; build do servidor estático em single distributable; incluir asset types; integração via npm scripts.
- **CircleCI**: pipeline de CI/CD — build steps, checks de segurança, deploy do build.

## Capítulo 13 — WebAssembly: A Brief Look into Native Code on the Web

- Modelo de programa e sandbox (não vaza memória entre módulos WASM).
- Escrever módulos **WAT** diretos; setup de ambiente e loading via servidor estático (`application/wasm`).
- **Memória compartilhada** entre WebAssembly e JavaScript (Linear Memory / `WebAssembly.Memory`).
- **FizzBuzz em WASM** e escrita de **C/C++ para web** (compilação para wasm).
- Case: gerador de **código de Hamming** em C++; **SQLite no browser** via WASM.

---

## Ferramentas/Tecnologias citadas no livro

- DevTools (Chrome Performance/Memory/Rendering, Firefox, Safari Web Inspector, Edge), jsPerf
- Redux, Immutable.js
- Svelte
- Node.js (`fs`, `net`, `http`, `cluster`, streams), `node-quic`
- `what-the-pack` (MessagePack), Protocol Buffers (proto3)
- Web Workers (Dedicated/Shared), Transferrables, Cache Storage, Service Workers
- Rollup, CircleCI
- WebAssembly (WAT, Emscripten/C++), SQLite-in-WASM