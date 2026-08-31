# Total TypeScript: The Essentials — Resumo dos 16 Capítulos

Resumo consolidado de *Total TypeScript: The Essentials* (Matt Pocock, Taylor Bell), cobrindo setup, fundamentos, narrowing, mutabilidade, classes, features exclusivas do TS, derivação de tipos, tsconfig e design de tipos.

---

## Parte I — Getting Started

### 1. Kickstart Your TypeScript Setup
- Setup com `tsc --init`, modo **watch** (`tsc --watch`), TS Playground para experimentos.
- TS nunca roda no navegador: compila para JS; o feedback do compilador é local e instantâneo.

### 2. IDE Superpowers
- **Hover/Quick Info** para inspecionar tipos inferidos; Go to Definition; Rename Symbol refatora com segurança de tipos.
- Quick Fix (Ctrl+.) sugere correções; inlay hints mostram tipos implícitos.
- O editor é a interface primária com o sistema de tipos — errar é barato quando o hover é rápido.

### 3. TypeScript in the Development Pipeline
- TS no pipeline: `tsc` em CI, erro quebra build; integração com linters (ESLint typescript-eslint) e bundlers.
- Diferença entre **erros de tipo** (compile-time) e a transpilação (que não valida por padrão).

## Parte II — Fundamentals

### 4. Essential Types and Annotations
- Primitivos `string | number | boolean | null | undefined`, arrays, objetos, funções com anotações explícitas em fronteiras.
- Objetos anidados tipados campo a campo; funções anotam parâmetros e (opcionalmente) retorno — inferência cuida do corpo.

### 5. Unions, Literals, and Narrowing
- **Union types** (`string | null`) modelam "ou isso ou aquilo"; operável apenas o comum aos membros; unions de unions se achatam.
- **Literal types** (`"yes" | "no"`, `200 | 404`) alimentam autocomplete como em `addEventListener`.
- **Narrowing** (o coração do capítulo) refinamento do tipo conforme fluxo de runtime:
  ```typescript
  type Format = "MP3" | "LP" | "CD"; // literal union
  type Album = DigitalAlbum | PhysicalAlbum;

  const refund = (album: Album) => {
    if (album.format === "digital") {
      // narrowed: DigitalAlbum — acessa só campos dessa variante
      return album.downloadUrl;
    }
    // narrowed: PhysicalAlbum
    return album.shippingAddress;
  };
  ```
- Formas de narrowing (em ordem de preferência):
  - **`typeof x === "..."`** — guard nativo para primitivos (cuidado com `typeof null === "object"`).
  - **Operador `in`** — testa existência de propriedade: `"downloadUrl" in album`.
  - **Disjoint unions / discriminants** — campo literal comum (`kind`, `type`, `status`) que separa variantes; `switch (album.kind)` estreita cada branch.
  - **Igualdade estrita** (`===`) e truthiness (com atenção aos falsy: `0`, `""`, `NaN`, `null`, `undefined`).
  - Returns cedo e `??`/`?.` para remover `null | undefined` do fluxo.

## Parte III — Objects, Classes, and Mutability

### 6. Objects
- Tipos de objeto anônimos, interfaces e type aliases; propriedades opcionais (`?`) geram `| undefined` na leitura.
- Excess property checking aplica-se apenas a object literals; união de tipos de objeto funciona por interseção de campos obrigatórios.

### 7. Mutability
- **`let` alarga, `const` estreita**: `let albumGenre = "rock"` infere `string` (rejeitado onde se espera `AlbumGenre=`); `const albumGenre = "rock"` infere o literal `"rock"`.
  ```typescript
  let genre = "rock";   // string  (widened)
  const genre2 = "rock"; // "rock"
  ```
- Propriedades de objetos **sempre alargam** literais (mesmo em `const`), pois objetos são mutáveis:
  ```typescript
  const album = { format: "LP" };        // format: string  ❌
  const album2 = { format: "LP" } as const; // format: "LP" ✅
  ```
- **`as const`** congela toda a árvore de objetos/arrays em literals `readonly` — o idioma para configs, mapas de evento e constantes.
- **`Object.freeze`** fornece proteção contra mutação **em runtime** (complemento do `as const`, que é só de tipo); arrays: `readonly T[]` e `ReadonlyArray<T>`.
- Propriedades `readonly` no tipo impedem reatribuição em compile-time, mas não profundidade — para deep immutability modele `Readonly<T>` recursivo / use `as const`.

### 8. Classes
- Propriedades de classe exigem inicialização (ou `strictPropertyInitialization` reclama) — resolva via constructor, inicializador inline ou `!` (com moderação).
- **Parameter properties** (TS-only): `constructor(private title: string) {}` declara e atribui campo de uma vez — econômico mas é feature TS; equipe pode preferir atribuição explícita.
- **`implements`** valida que a classe adere a um contrato:
  ```typescript
  interface IAlbum { displayInfo(): string }
  class Album implements IAlbum { /* erro se displayInfo faltar */ }
  ```
  `implements` não altera o tipo da classe — é uma checagem; herança de tipo vem de `extends`.
- Modificadores: `public` (default), `protected`, `private` — apagados em runtime. O `#private` do JS é **encapsulamento real** (não visível fora, nem por type cast). `private` TS é só compile-time. Para libs, prefira `#private`.
- `abstract` classes/métodos definem contratos que subclasses devem concretizar; `override` explícito evita erros de typo em sobrescritas (com `noImplicitOverride`).

## Parte IV — Working with the Compiler

### 9. TypeScript-Only Features
- **Enums**: feature TS com runtime próprio (IIFE) — código extra no bundle. Alternativa idiomática:
  ```typescript
  // enum vs objeto as const:
  const AlbumFormat = {
    Digital: "MP3",
    Physical: "LP",
  } as const;
  type AlbumFormat = (typeof AlbumFormat)[keyof typeof AlbumFormat];
  ```
  `const` enum (`const enum Enum`) é inline pelo compilador, mas incompatível com transpiladores só-JS (Babel, esbuild) no modo isolado.
- **Namespaces**: legado (pré-módulos ES) — preferir módulos ES `import/export`; útil apenas para tipagem de globals/ambient.
- **Ambient types / `declare`**: descrevem código JS existente sem emitir runtime (`declare global`, `declare module`, `.d.ts`).
- Parameter properties também se encaixam aqui: feature TS que não existe no JS puro (Item 72 do Effective Typescripts segue a mesma diretriz: prefira ECMAScript).

### 10. Deriving Types
- Derive de dados concretos em vez de redeclarar — **single source of truth**:
  ```typescript
  const album = { title: "Loop Finding Jazz Records", artist: "Jan Jelinek", releaseYear: 2001 };
  type Album = typeof album;           // value → type
  type AlbumKey  = keyof Album;        // "title" | "artist" | "releaseYear"
  type YearTag   = Album["releaseYear"]; // indexed access: number
  ```
- **`keyof` + indexed access + arrays**: `Album["title"]`, `(typeof list)[number]` (tipo do elemento de array/tuple).
- `typeof` em funções → `Parameters<typeof fn>` e `ReturnType<typeof fn>`; `Record<keyof Obj, X>` mapeia todas as chaves.
- **`ReturnType`** extrai o retorno de função:
  ```typescript
  type SellAlbumReturn = ReturnType<typeof sellAlbum>;
  ```
- **`Awaited`** desembrulha a Promise (incluindo aninhadas), essencial para funções async:
  ```typescript
  type User = Awaited<ReturnType<typeof getUser>>; // T de Promise<T>
  ```
- Padrão factory inferido: `ReturnType<typeof createUser>` deriva o tipo de usuário sem interface duplicada.

### 11. Annotations and Assertions
- **`satisfies`** valida o shape **sem alargar** o tipo do valor (substitui `as` com segurança):
  ```typescript
  const config = {
    port: 8080,
    env: "production",
  } satisfies Config; // valida contra Config, mas port continua 8080 e env o literal "production"
  ```
- **Double casting** (`expr as unknown as T`) é um code smell — sinaliza que o tipo declarado não bate com a realidade; conserte o tipo ou valide em runtime.
- **`@ts-expect-error` > `@ts-ignore`**: `@ts-expect-error` **falha quando não há erro** — auto-documenta supressão e não apodrece; `@ts-ignore` silencia cegamente para sempre.
  ```typescript
  // @ts-expect-error O endpoint ainda não foi tipado
  legacyApi.call();
  ```
- Non-null assertion `!` e `as` — use apenas em fronteiras já validadas.

### 12. The Weird Parts
- Casos-limite: `any` vs `unknown` vs `never`, narrowing com closures (funções perdem refinamento se a variável for mutável), typeof `null === "object"`, comparações sem overlap (TS 2367), evolução de tipos e contextual typing em objetos anônimos.

## Parte V — Understanding the Environment

### 13. Modules, Scripts, and Declaration Files
- Módulos (com `import/export`) têm escopo próprio; **scripts** (sem imports) poluem o global — um arquivo sem import/export pode virar script acidental e gerar erros de duplicação.
- **Declaration files (`.d.ts`)** descrevem APIs JS existentes; `@types/*` do DefinitelyTyped; escrever `.d.ts` próprios para libs sem tipos (ambient `declare module "lib"`).
- `export type`/`import type` para garantir que a importação de tipo não gere runtime.

### 14. Configuring TypeScript
- `tsconfig.json` é o contrato do projeto; **`strict: true`** liga o conjunto (incluindo `noImplicitAny`, `strictNullChecks`).
- Flags de segurança extras: `noUncheckedIndexedAccess` (indexing pode retornar `undefined`), `exactOptionalPropertyTypes`, `noImplicitOverride`.
- **`moduleResolution`**: `"bundler"` com `module: "esnext"` para bundlers modernos (Vite/esbuild); `"node16"`/`"nodenext"` para Node ESM; `"node10"` legado.
- `paths`/`baseUrl` para aliases; `skipLibCheck: true` para velocidade; `noEmit` quando o bundler transpila.

## Parte VI — Advanced Application Development

### 15. Designing Your Types
- Desenho de tipos busca **representar exatamente os estados possíveis** (alinha-se ao Item 29 do Effective TypeScript): uniões de variantes fechadas, literal types para opções finitas, impossibilidade de estados inválidos.
- Tipos como documentação executável: nomes de domínio, aliases legíveis, evite espalhar `string`/`number` crus em fronteiras públicas.

### 16. Building Powerful Shared Utilities
- Construa utilities genéricas reutilizáveis combinando generics + conditional types + mapped types com `infer` (base de `Partial`, `Pick`, `Awaited`).
- Padrão de biblioteca: contratos explícitos nos exports, tipos derivados em vez de reconstruídos, e utilitários testados com `Expect<Equal<...>>` (Item 55 do Effective TypeScript).

---

### Resumo executivo (Total TypeScript)
- **Narrowing**: `typeof` → `in` → discriminant → igualdade estrita → control flow.
- **Mutabilidade**: `const` e `as const` para estreitar; `Object.freeze`/`readonly` para runtime/tipo respectivamente.
- **Classes**: `implements` para contratos; `#private` para encapsulamento real; parameter properties com parcimônia.
- **TS-only**: prefira `as const` objects a enums; namespaces apenas para ambient.
- **Derivação**: `typeof`, `keyof`, indexed access, `ReturnType`, `Awaited` — nunca duplique estruturas.
- **Supressões**: `satisfies` > `as`; `@ts-expect-error` > `@ts-ignore`.
- **tsconfig**: `strict: true` como piso, não teto.