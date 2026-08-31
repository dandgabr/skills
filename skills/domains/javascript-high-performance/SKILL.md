---
name: javascript-high-performance
description: "Especialista em Performance de JavaScript baseado na obra Hands-On JavaScript High Performance (Justin Scherer). Cobre profiling e observabilidade com ferramentas de DevTools (Chrome Performance/Memory/Rendering tabs, jsPerf e benchmarking correto), trade-offs de imutabilidade versus mutabilidade (Redux, Immutable.js, RAII, lazy evaluation, tail-call e currying), JavaScript moderno vanilla (Coleções, Proxies, Typed Arrays, DOM APIs, Fetch/Promises), Svelte como framework compilado para vanilla, Node.js sem DOM (fs, net, http, streams e non-blocking I/O), message passing (pipes, sockets, TCP/UDP, HTTP/2, QUIC), formatos de dados alternativos a JSON (MessagePack, Protocol Buffers schema-based), Web Workers (dedicated/shared, transferrables, SharedArrayBuffer), Service Workers (cache offline), build e deploy com Rollup/CircleCI e WebAssembly no navegador."
---

# Habilidade de IA: JavaScript High Performance

Esta skill orienta a inteligência artificial a atuar como especialista em **performance de JavaScript**, cobrindo desde o profiling com as ferramentas dos navegadores até a arquitetura de código (mutabilidade, streams, workers, formatos de dados e WASM), baseada na obra *Hands-On JavaScript High Performance* (Justin Scherer, Packt).

> 📖 **Referência canônica**: consulte [references/js-high-performance-book-guide.md](references/js-high-performance-book-guide.md) para o resumo por capítulo do livro e [examples/performance-patterns.md](examples/performance-patterns.md) para os padrões práticos.

---

## 🧭 Diretriz Geral

- **Meça antes de otimizar**: use a aba Performance do Chrome DevTools para localizar o gargalo real (scripting, rendering, painting) — nunca otimize com base em suposições.
- **Tudo é trade-off**: imutabilidade dá segurança à custa de velocidade/memória; coleções nativas batem bibliotecas; MessagePack pode não ser menor nem mais rápido que JSON nativo. Escolha consciente, não dogma.
- **Prefira as primitivas do runtime**: o motor (V8 etc.) otimiza built-ins melhor que bibliotecas; evite camadas de abstração em hot paths.
- **Mantenha a main thread livre**: qualquer processamento > ~16 ms deve ser offloaded para Workers, streams ou WASM.

---

## 🔍 1. Profiling e Observabilidade

### Abas do Chrome DevTools
- **Performance**: gravação de timeline de runtime (Scripting/Rendering/Painting, flame chart de call stacks, event log). Use para achar funções de longa duração, forced reflows e GC pauses.
- **Memory**: heap snapshots (comparação entre snapshots para detectar memory leaks — objetos retidos entre capturas), allocation instrumentation e allocation timeline.
- **Rendering**: FPS meter e paint flashing para detectar layouts/paints excessivos em tempo real.
- Outros motores: Safari (Web Inspector com Timeline), Firefox (Performance tools) e Edge (fork do Chromium) — motores diferentes otimizam diferente, valide em múltiplos navegadores.

### Benchmarking correto (jsPerf e afins)
- Cuidado com **otimizações do motor** que distorcem resultados (mortal code, dead code elimination) — consuma resultados das funções de teste.
- Compare em **múltiplos navegadores/motores**; nenhum resultado de um único motor é definitivo.
- Remova código extrano dos casos de teste — qualquer trabalho extra enviesa asmedições.

---

## ⚖️ 2. Imutabilidade versus Mutabilidade

- **Imutabilidade** (Redux, Immutable.js) traz previsibilidade, undo/redo e detecção de mudanças barata (referência igual = dados iguais), mas em aplicações de alto desempenho paga-se com aumento de velocidade e memória: cada mudança copia estruturas.
- **Immutable.js** (List, Map, Set com tries estruturais) dá código mais limpo e arquitetura funcional, porém para datasets grandes as operações nativas (`for` loops, arrays, objetos mutáveis) são mais rápidas e menos memory hungry.
- **Estratégia híbrida**: imutabilidade na camada de estado/UI (mudança de referência dispara re-render), mutabilidade disciplinada em hot paths computacionais (parsers, transformações de dados, joins em memória).
- **Escrita mutável segura**: encapsule mutação em módulos pequenos (padrão RAII / scope-bound resource management — libere/feche recursos no mesmo escopo que os criou, inspirado em C++/Rust), evite mutar objetos compartilhados entre módulos.

### Técnicas funcionais com custo consciente
- **Lazy evaluation**: gerecoleções sob demanda (generators/iteradores) em vez de materializar arrays gigantes.
- **Tail recursion**: prefira transformar recursão em iteração (loops) — engines não garantem TCO, e stack overflow é risco real.
- **Currying**: poderoso para composição, mas cria closures e funções intermediárias — evite em código de altíssima frequência.

---

## 🌐 2. JavaScript Moderno Vanilla

- **let/const com escopo de bloco**, arrow functions e modules — código moderno também é código que o motor otimiza previsivelmente.
- **Coleções**: `Map`/`Set`/`WeakMap`/`WeakSet` — `WeakMap`/`WeakSet` permitem GC de chaves (metadados sem vazamentos); `Map` supera objetos como dicionário em chaves dinâmicas.
- **Typed Arrays** (`Int32Array`, `Float64Array`, `ArrayBuffer`): memória contígua e tipada, essencial para dados numéricos grandes, binários e transferência com Workers.
- **Proxies e getters/setters**: habilitam reatividade (a base de frameworks como Svelte/Vue), mas cada acesso intercepta — não use em hot loops.
- **DOM eficiente**: `querySelector`/`querySelectorAll` centralizados; **Document Fragments** para inserções em lote (uma reflow só); Shadow DOM e Web Components para encapsulamento; `<template>` para clonagem barata de markup.
- **Fetch + Promises**: Promises são lazy-friendly; suporte a `AbortController` para cancelar requisições (evita trabalho de rede e parsing desnecessário).

---

## 🧩 3. Svelte e o Paradigma "Compilado para Vanilla"

- Svelte compila componentes para JS vanilla imperativo — sem virtual DOM, sem runtime em produção; cada mutação de estado gera código de atualização mínima e preciso do DOM.
- A lição de performance: **menos runtime = mais velocidade**. Quando uma biblioteca de framework é o gargalo, considere alternativas que empurram trabalho para o build time (compiladores, tree shaking agressivo).
- Aplicações práticas (Todo, app de clima) mostram que componentes pequenos com estado local evitam re-renders em cascata.

---

## 🟩 4. Node.js sem DOM

- `package.json` como centro de configuração (scripts, dependencies, type module).
- **Módulos nativos**: `fs` (I/O de arquivos), `net` (sockets TCP), `http` (servidor/serviços) — nada de bibliotecas para o básico; a lib padrão é a mais rápida.
- **Streams e non-blocking I/O**: nunca leia arquivos grandes inteiros na memória — pipeline com Readable/Writable/Duplex/Transform streams processa em chunks, mantenho a memória constante e o event loop livre.
- **Streams customizados**: implemente `Readable`/`Writable`/`Transform` (com `highWaterMark` para backpressure) e use generators para simplificar pipelines.

---

## 📬 5. Message Passing e Protocolos (Node.js)

- Comunicação local/processos: `net` com sockets de domínio Unix / TCP, IPC entre processos (cluster).
- `cluster` module: multiplique processos por núcleo de CPU para saturar o hardware (Node é single-threaded por processo).
- **TCP/UDP**: TCP para ordenação e confiabilidade; UDP para latência mínima sem handshake.
- **HTTP/2**: multiplexing de streams numa conexão (elimina head-of-line blocking de HTTP/1.1), header compression.
- **HTTP/3/QUIC**: UDP-based, 0-RTT handshake, sem TCP head-of-line blocking — a direção futura de transporte na web.

---

## 📦 6. Formatos de Dados

- **JSON**: onipresente, mas verboso e com custo de encode/decode em payloads grandes.
- **Formatos schema-less**: JSON, XML — autodescritivos, maiores na rede.
- **MessagePack** (ex.: lib `what-the-pack`): binário compacto com pré-alocação de buffer; pode não ser menor nem mais rápido que `JSON.parse`/`stringify` nativos — sempre meça.
- **Protocol Buffers (proto3)**: schema compartilhado antecipadamente, encoding muito compacto e rápido — padrão para sistemas enterprise; IDs numéricos de campo tornam a codificação e a indexação baratas.
- **Formato próprio**: para casos extremos, um encoder/decoder binário customizado (ex.: schema na frente dos dados) dá o máximo controle sobre tamanho e velocidade.

---

## 👷 7. Web Workers e Paralelismo no Browser

- **Dedicated Workers**: mova trabalho pesado (parsing, transformação, joins de dados, computação) para fora da main thread; comunique-se via `postMessage`.
- **Structured clone tem custo real**: enviar milhares de objetos serializa/deserializa tudo — exemplo do livro: 100.000 objetos levaram de 800 ms a 1,7 s e 80–100 MB de heap. Use `Date.now()` + Profiler para visualizar o custo.
- **Transferrables**: envie o `ArrayBuffer` (`postMessage(view, [view.buffer])`) — **zero cópia**; o remetente perde acesso, o receptor ganha. Para dados binários grandes é ordens de escala mais rápido.
- **Shared Workers**: um worker compartilhado por múltiplas páginas/abas (ex.: cache compartilhado em memória, conexão única).
- **SharedArrayBuffer + Atomics**: memória compartilhada de verdade com sincronização; exija COOP/COEP corretos.

---

## 🔁 8. Service Workers e Cache

- Ciclo de vida do ServiceWorker: install → waiting → activate; intercepte requests com `fetch` event.
- **Cache de páginas/templates para offline** (Cache Storage API), habilitando comportamento PWA.
- **Save requests for later**: enfileire mutações offline e reproduza quando a rede voltar (padrão de filas no SW).
- Cache bem-feito é a otimização mais barata: custo zero de rede e processamento nas requisições subsequentes (TTL/LRU para limitar crescimento, como no capítulo do servidor estático).

---

## 🏗️ 9. Build, Deploy e CI/CD

- **Rollup**: bundler otimizado para ES modules (ESM) — tree shaking efetivo, bundles menores; use para distribuir a aplicação (server + assets) num single distributable.
- Integre o build aos scripts npm (`npm run build`) e ao pipeline **CircleCI** (build → testes → checks de segurança → deploy).
- Menos bytes = menos parse/compile da main thread; tree shaking é otimização de primeira ordem.

---

## ⚙️ 10. WebAssembly no Navegador

- Para hot paths que mesmo JS otimizado não satisaz (geradores de códigos corretivos como Hamming, parsing pesado, matemática numérica).
- Escrita direta de módulos WAT, compilação de **C/C++ para o browser** e memória compartilhada entre WASM e JavaScript (Linear Memory sobre `WebAssembly.Memory`).
- Case real do livro: **SQLite compilado para WASM** rodando no navegador — banco de dados completo client-side.
- Sandbox: código WASM não vazia memória entre módulos; carregue via servidor estático com MIME `application/wasm`.

---

## 🧪 Padrões de Código Recomendados

### Loop nativo em hot path (vs. abstração)
```javascript
// ❌ chain de high-order functions em dados grandes: múltiplos arrays intermediários
const positive = data.filter((x) => x > 0).map((x) => x * 2);

// ✅ um único loop, sem alocações intermediárias
const result = new Array(data.length);
let count = 0;
for (let i = 0; i < data.length; i++) {
  if (data[i] > 0) {
    result[count++] = data[i] * 2;
  }
}
```

### Transfer de binário para Workers (zero-copy)
```javascript
const view = new Int32Array(1_000_000);
// ... populate ...
worker.postMessage(view, [view.buffer]); // transfere, não copia
// ⚠️ view agora está neutered/detached no remetente
```

### Fragmento para inserção DOM em lote
```javascript
const frag = document.createDocumentFragment();
for (const item of items) {
  frag.appendChild(createRow(item));
}
container.appendChild(frag); // um único reflow/layout
```

### Cache LRU/TTL simples
```javascript
const cache = new Map();
const TTL = 5 * 60 * 1000;
function getCached(key) {
  const hit = cache.get(key);
  if (!hit) return null;
  if (Date.now() - hit.ts > TTL) {
    cache.delete(key); // evita crescimento infinito
    return null;
  }
  return hit.value;
}
```

---

## ⚠️ Pegadinhas

- **GC non-determinístico**: alocação massiva em hot paths (cada evento do usuário gerando objetos) causa GC pauses difíceis de prever; reduza taxa de alocação, não confie em "o GC resolve".
- **Layout thrashing / forced synchronous layout**: intercalar leitura e escrita de propriedades de layout (`offsetHeight` ↔ `style.height`) força reflow a cada iteração — separe leituras das escritas (ou use requestAnimationFrame batching).
- **postMessage com objetos gigantes**: structured clone duplica memória e congela a thread — transfira `ArrayBuffer`s ou use `SharedArrayBuffer`.
- **Benchmarks enganosos**: um único motor, código morto eliminado ou código extrano enviesam resultados; teste em vários navegadores e certifique-se de consumir os resultados.
- **Dependências em runtime**: bibliotecas de imutabilidade/functional helpers em datasets grandes custam mais que nativo — "tudo é trade-off".

---

## 🔗 Integração com Outras Skills

- [latency-engineering](../../engineering-practices/latency-engineering/SKILL.md): leis da latência, tail latency e eliminação de trabalho desnecessário aplicadas à web.
- [code-optimizer](../../roles/code-optimizer/SKILL.md): hierarquia algoritmo → estrutura → runtime → paralelismo aplicada a aplicações JS.
- [webassembly](../webassembly/SKILL.md): Wasm como destino definitivo para hot paths (Emscripten, wasm-pack, SharedArrayBuffer/Atomics).
- [framework-react](../../framework/framework-react/SKILL.md): imutabilidade de estado, memoization e re-renders no ecossistema React.
- [framework-vue](../../framework/framework-vue/SKILL.md): reatividade baseada em getters/setters e Proxies (mesmos fundamentos do capítulo vanilla).
- [frontend-developer](../../roles/frontend-developer/SKILL.md): integração de otimizações de performance no ciclo de construção da UI.