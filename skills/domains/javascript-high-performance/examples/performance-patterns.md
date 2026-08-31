# Exemplos de Padrões de Performance em JavaScript

Padrões práticos extraídos do livro *Hands-On JavaScript High Performance* (Justin Scherer). Código em inglês, explicações em pt-BR. Cada exemplo mostra o anti-pattern ❌ e a versão otimizada ✅.

---

## 1. Debounce e Throttle (evitar trabalho redundante)

Eventos de alta frequência (`input`, `scroll`, `resize`) disparam handlers dezenas de vezes por segundo. **Debounce** executa só após a pausa; **throttle** executa no máximo 1x por janela de tempo.

```javascript
// ❌ Anti-pattern: handler pesado executado a cada tecla/frame
searchInput.addEventListener('input', (e) => runExpensiveSearch(e.target.value));
window.addEventListener('resize', relayoutEverything);

// ✅ Debounce: só executa quando o usuário para de digitar
function debounce(fn, delay) {
  let timer = null;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// ✅ Throttle: no máximo uma execução por intervalo
function throttle(fn, interval) {
  let last = 0;
  return (...args) => {
    const now = Date.now();
    if (now - last >= interval) {
      last = now;
      fn(...args);
    }
  };
}

searchInput.addEventListener('input', debounce((e) => runExpensiveSearch(e.target.value), 250));
window.addEventListener('resize', throttle(relayoutEverything, 100));
```

**Por que importa**: cada execução evitada é menos GC pressure e menos tempo de scripting na main thread (visível na aba Performance do Chrome DevTools).

---

## 2. Loops nativos vs. métodos de array em hot paths

O livro compara com jsPerf: em dados grandes, chains de métodos funcionais alocam arrays intermediários a cada etapa. Benchmarks do livro (cap. 1) mostram o `for` loop batendo o `filter` quando o código roda em altíssima frequência.

```javascript
// ❌ Anti-pattern: 2 arrays intermediários + iterações múltiplas
const positives = data.filter((x) => x > 0);
const doubled = positives.map((x) => x * 2);
let total = 0;
for (const x of doubled) total += x;

// ✅ Otimizado: um único loop, sem alocações intermediárias
let total = 0;
const result = new Array(data.length);
let count = 0;
for (let i = 0; i < data.length; i++) {
  const x = data[i];
  if (x > 0) {
    result[count++] = x * 2;
    total += x * 2;
  }
}
result.length = count;
```

**Regra**: use `map/filter/reduce` para legibilidade em código frio (roda poucas vezes); use loops nativos em hot paths (parse, transformação de dados, renderização de listas grandes).

---

## 3. Memoization e Cache com TTL/LRU

O livro constrói caches em workers (cap. 10) e no servidor estático (cap. 9), sempre lembrando: "cache infinito" vaza memória — limite por TTL (Time To Live) ou LRU (Least Recently Used).

```javascript
// ✅ Memoization com cache limitado por TTL
const cache = new Map(); // key -> { value, ts }
const TTL = 5 * 60 * 1000;
const MAX_ENTRIES = 1000;

function memoize(key, compute) {
  const hit = cache.get(key);
  if (hit && Date.now() - hit.ts <= TTL) {
    return hit.value; // cache hit: zero custo de processamento
  }
  const value = compute(key);
  // evict least-recently-used quando cheio (Map preserva ordem de inserção)
  if (cache.size >= MAX_ENTRIES) {
    const oldest = cache.keys().next().value;
    cache.delete(oldest);
  }
  cache.set(key, { value, ts: Date.now() });
  return value;
}

function getCustomerAttribution(customerId) {
  return memoize(`cust:${customerId}`, (id) => fetchAndDecorate(id));
}
```

**Erro clássico do livro**: "currently, we infinitely increase our cache" — sempre adicione TTL ou LRU destroy para caches crescentes.

---

## 4. Web Worker offloading com Transferrables (zero-copy)

Mover objetos gigantes via `postMessage` usa **structured clone** (serializa + copia): o livro mediu 100.000 objetos em 800 ms–1,7 s e 80–100 MB de heap.

```javascript
// main.js
const worker = new Worker('heavy.js');

// ❌ Anti-pattern: structured clone de milhares de objetos
// worker.postMessage(dataToSend); // cópia completa + GC pressure

// ✅ Otimizado: TypedArray + transferrable (zero cópia)
const view = new Int32Array(1_000_000);
for (let i = 0; i < view.length; i++) view[i] = i + 1;
worker.postMessage(view, [view.buffer]); // transfere o ArrayBuffer
// ⚠️ view agora está detached — remetente não pode mais acessar

worker.onmessage = (ev) => {
  console.log('result length', ev.data.byteLength);
};
```

```javascript
// heavy.js
self.onmessage = (ev) => {
  const data = ev.data; // recebe instantaneamente, sem cópia
  let sum = 0;
  for (let i = 0; i < data.length; i++) sum += data[i];
  // para devolver, também transfira (novamente zero-copy):
  const result = new Int32Array(1);
  result[0] = sum;
  self.postMessage(result, [result.buffer]);
};
```

**Regra**: dados binários grandes → transferrables; dados estruturados pequenos → `postMessage` normal; memória compartilhada de verdade → `SharedArrayBuffer` + `Atomics`.

---

## 5. Evitando layout thrashing (forced synchronous layout)

Intercalar leitura e escrita de propriedades de layout força o navegador a recalcular layout a cada iteração (reflow síncrono). Aparece como picos em amarelo/roxo na aba Performance.

```javascript
// ❌ Anti-pattern: read-write intercalado = reflow a cada iteração
const rows = document.querySelectorAll('.row');
for (const row of rows) {
  const h = row.offsetHeight;    // READ (invalida layout)
  row.style.height = h * 2 + 'px'; // WRITE (invalida de novo)
}

// ✅ Otimizado: batch de leituras, depois batch de escritas
const rows = document.querySelectorAll('.row');
const heights = Array.from(rows, (row) => row.offsetHeight); // READ phase
rows.forEach((row, i) => {
  row.style.height = heights[i] * 2 + 'px'; // WRITE phase
});
```

Variante com `requestAnimationFrame` para inserções que alteram layout dentro de um frame:

```javascript
function addRows(container, items) {
  const frag = document.createDocumentFragment();
  for (const item of items) {
    const row = document.createElement('div');
    row.textContent = item.label;
    frag.appendChild(row);
  }
  requestAnimationFrame(() => {
    container.appendChild(frag); // um único layout/paint
  });
}
```

**Regra**: separe leitura de escrita; use `DocumentFragment` para inserções em lote e monitore com Paint flashing (Rendering tab).

---

## 6. Streaming de dados grandes (Node.js / browser)

Não carregue arquivos ou payloads inteiros na memória — processe em chunks com streams (cap. 7) ou formatos binários compactos (cap. 8).

```javascript
// ❌ Anti-pattern: arquivo inteiro na memória (OOM em arquivos grandes)
const content = fs.readFileSync('big.log', 'utf8');
const lines = content.split('\n').filter((l) => includesError(l));
fs.writeFileSync('errors.log', lines.join('\n'));

// ✅ Otimizado: pipeline de streams, memória constante
import { pipeline } from 'node:stream/promises';
import { createReadStream, createWriteStream } from 'node:fs';
import { Transform } from 'node:stream';

const errorFilter = new Transform({
  transform(chunk, enc, cb) {
    const kept = chunk
      .toString()
      .split('\n')
      .filter((l) => l.includes('ERROR'))
      .join('\n');
    cb(null, kept + '\n');
  },
});

await pipeline(
  createReadStream('big.log'),
  errorFilter,
  createWriteStream('errors.log'),
);
```

**Por que importa**: memória constante independente do tamanho do arquivo, event loop livre (non-blocking I/O) e backpressure automática via `highWaterMark`.