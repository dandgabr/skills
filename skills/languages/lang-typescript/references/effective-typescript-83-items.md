# Effective TypeScript (2ª Edição) — Os 83 Items Consolidados

Resumo organizado de *Effective TypeScript: 83 Specific Ways to Improve Your TypeScript, 2nd Edition* (Dan Vanderkam), agrupado pelos 10 capítulos do livro. Cada item tem uma explicação de 1 linha; os itens mais impactantes recebem trechos de código curtos.

---

## Capítulo 1 — Getting to Know TypeScript (Itens 1–5)

- **Item 1**: TypeScript e JavaScript são camadas separadas — entenda o TS como superset com sistema de tipos estático que desaparece em runtime.
- **Item 2**: Saiba quais opções do compilador (tsconfig) estão ativas no seu projeto — o comportamento do TS depende diretamente delas.
- **Item 3**: Geração de código é independente de tipos — erros de tipo não impedem o compilador de emitir JS (salvo `noEmitOnError`); tipos jamais corrigem bugs de runtime.
- **Item 4**: Structural typing: compatibilidade é definida pela **estrutura**, não pela declaração nominal.
- **Item 5**: Limite o uso de `any` — cada `any` desliga o verificador naquele ponto, quebra contratos e se espalha silenciosamente.

## Capítulo 2 — TypeScript's Type System (Itens 6–17)

- **Item 6**: Use o editor para interrogar o sistema de tipos (hover, quick info, definição) — entender o tipo inferido evita erros antes de existirem.
- **Item 7**: Penso em tipos como **conjuntos de valores**:
  ```typescript
  type A = string;          // conjunto infinito de strings
  type B = "left" | "right"; // conjunto de 2 valores
  type C = never;            // conjunto vazio (⊥)
  // Subtipo = subconjunto; assignable = ∈ conjunto
  ```
  `never` é vazio, `unknown` é o conjunto universal, `string` nunca é assignável a `"left" | "right"`, mas o inverso sim.
- **Item 8**: Distinga **type space** e **value space** — o mesmo símbolo pode existir nos dois (`type Foo` + `const Foo`); `typeof` significa coisas diferentes em cada espaço.
- **Item 9**: Prefira anotações a assertions (`as`) — anotação valida o valor; assertion não checa nada (exceto overlap) e mascara erros reais.
- **Item 10**: Evite wrapper types (`String`, `Number`, `Boolean`, `Symbol`, `BigInt`) — use os primitivos minúsculos.
- **Item 11**: Distinga **excess property checking** (só em object literals!) do type checking estrutural normal.
- **Item 12**: Aplique tipos à **expressão de função inteira** em vez de cada parâmetro:
  ```typescript
  const diceRoll: Record<number, number> = {}; // contexto para a variável
  fetchAll("users", (users: User[]) => {}); // ❌ anote o alvo, não o callback
  // ✅ type FetchAll = (table: string, cb: (rows: unknown[]) => void) => void
  ```
- **Item 13**: Conheça as diferenças entre `type` e `interface` (veja tabela na referência do Handbook); heurística: `interface` até precisar de features de `type`.
- **Item 14**: Use `readonly` para evitar erros associados a mutação (arrays `readonly T[]`, propriedades `readonly`).
- **Item 15**: Use operações de tipo e generics para **não se repetir** — derive tipos (`keyof`, `typeof`, indexed access, mapped types) de uma fonte única de verdade.
- **Item 16**: Prefira alternativas mais precisas a **index signatures** (`Record<K, V>`, mapear chaves com `as const`, unmarked interfaces) — index signature permite propriedades arbitrárias e perde checagem.
- **Item 17**: Evite index signatures numéricas (`{[i: number]: T}`) — são raramente o que se quer.

## Capítulo 3 — Type Inference and Control Flow Analysis (Itens 18–28)

- **Item 18**: Não polua o código com tipos inferíveis — anote só fronteiras de contrato.
- **Item 19**: Use variáveis diferentes para valores de tipos diferentes (evite reusar e alargar o tipo).
- **Item 20**: Entenda **como uma variável ganha seu tipo** (inicialização, anotação, contexto, `const`/`let`).
- **Item 21**: Crie objetos **de uma vez só** — atribuições incrementais produzem tipos fracos (`{}`/parciais).
- **Item 22**: Entenda **type narrowing** (checks que refinam tipos ao longo do fluxo de controle).
- **Item 23**: Seja **consistente nos aliases** que define — reutilize o mesmo nome de tipo em vez de reescrever estruturas:
  ```typescript
  interface UserInfo { id: string; name: string; }
  function getUser(id: string): UserInfo { ... }  // ✅
  function getUserName(user: { id: string; name: string }) { ... } // ❌ duplicado
  ```
- **Item 24**: Entenda o uso de **contexto** na inferência (contextual typing em callbacks/literals).
- **Item 25**: Entenda **evolving types** (`let x = []` evolui de `any[]` conforme usos).
- **Item 26**: Use construtos funcionais e bibliotecas (map/filter/reduce, lodash) para favorecer o **fluxo de tipos**.
- **Item 27**: Prefira `async`/`await` a callbacks — Promise modela `T | erro` melhor e preserva o fluxo de tipos.
- **Item 28**: Use classes e currying para criar novos **sites de inferência** (bind genérico de tipos em sub-partes).

## Capítulo 4 — Type Design (Itens 29–42)

- **Item 29**: Prefira tipos que **sempre representem estados válidos** — o desenho do tipo deve impossibilitar o estado inconsistente:
  ```typescript
  // ❌ Estado inválido representável: loaded mas sem dados, loading E erro
  interface State {
    pageError?: string;         // separados, coerentes entre si
    loading: boolean;
    page?: PageContent;
  }
  // ✅ União de estados fechada:
  type PageState =
    | { state: "loading" }
    | { state: "error"; error: string }
    | { state: "ready"; page: PageContent };
  ```
- **Item 30**: **Liberal no que aceita, estrito no que produz** (Postel): parâmetros com tipos largos (unions) e saídas com tipos precisos.
- **Item 31**: Não repita informação de tipo na documentação — o tipo É a fonte de verdade; use TSDoc para semântica não-codificada.
- **Item 32**: Evite incluir `null`/`undefined` dentro de type aliases — o opcional contamina todo uso (`type FetchResult = T | null` espalha null).
- **Item 33**: Empurre valores `null` para a **periferia** dos seus tipos (trate null cedo, no boundary).
- **Item 34**: Prefira **união de interfaces** a interface com uniões — cada variante com seus campos obrigatórios:
  ```typescript
  // ❌ interface Layer { type: "file"|"database"; layout: LayoutSpec; path?: string; db?: string }
  // ✅
  type Layer = FileLayer | DatabaseLayer; // cada variante com seus campos
  ```
- **Item 35**: Prefira alternativas mais precisas a `string` (unions de literals, branded, template literal types).
- **Item 36**: Use um tipo distinto para valores especiais (ex.: `-1` que significa "não encontrado" → `type NotFoundSentinel = -1` ou retorno `T | null`).
- **Item 37**: Limite propriedades opcionais — propriedades `?` criam `| undefined` e estados vagos; prefira unidade explícita.
- **Item 38**: Evite **parâmetros repetidos** do mesmo tipo (positionais confundíveis) — agrupe num objeto:
  ```typescript
  // ❌ function getListItem(index: number, count: number): number
  // ✅
  interface IndexAndCount { index: number; count: number }
  function getListItem(opts: IndexAndCount): number { ... }
  ```
- **Item 39**: Prefira **unificar tipos** a modelar as diferenças — nem toda variação merece um tipo próprio (ex.: `Vector3D` e `Vector2D` com coords idênticas podem ser unificados por interface única + dados por campo).
- **Item 40**: Prefira tipos **imprecisos a imprecisos-inacurados** (`imprecise` seguro > `inaccurate` que mente ao compilador).
- **Item 41**: Nomeie tipos com a **linguagem do domínio** do problema (não do framework/estrutura técnica).
- **Item 42**: Evite tipos baseados em **dados anedóticos** (modelar só os casos que pôde observar, ex.: só 3 categorias de erro vistas em logs).

## Capítulo 5 — Unsoundness and the any Type (Itens 43–49)

- **Item 43**: Use o **escopo mais estreito possível** para `any` — jamais em retorno público; localize ao máximo (cast local, não assinatura inteira).
- **Item 44**: Prefira variantes mais precisas de `any` (`any[]` em vez de `any`; `unknown` na entrada; funções parcialmente tipadas a totalmente livres).
- **Item 45**: **Esconda assertions unsafe em funções bem tipadas** — a inconsistência fica contida num único ponto testável:
  ```typescript
  // ❌ espalhado: JSON.parse(...) as User
  // ✅
  function parseUser(json: string): User {
    return JSON.parse(json); // any contido aqui, retorno seguro
  }
  ```
  (Idealmente valide em runtime antes deste ponto.)
- **Item 46**: Use `unknown` (não `any`) para valores de tipo desconhecido — `unknown` exige narrowing, `any` não.
- **Item 47**: Prefira abordagens type-safe a **monkey patching** (interfaces com campos opcionais, `Object.assign`, symbol-keyed props).
- **Item 48**: Evite **armadilhas de soundness** do TS (covariância de arrays, `as`, getters mutáveis, `this` solto) — saiba onde o TS não protege.
- **Item 49**: Meça a **cobertura de tipos** (`type-coverage` package / `strict`) para prevenir regressões de type safety.

## Capítulo 6 — Generics and Type-Level Programming (Itens 50–58)

- **Item 50**: Pense em generics como **funções entre tipos** (entrada `T` → saída derivada):
  ```typescript
  type ShallowArrayOrSingle<T> = T[] | T;
  type Pick_<Obj, Keys extends keyof Obj> = {
    [K in Keys]: Obj[K];
  };
  ```
- **Item 51**: Evite **type parameters desnecessários** — não adicione generic que o chamador tem que explicitar; deixe a inferência trabalhar.
- **Item 52**: Prefira **conditional types** a overload signatures — condição no sistema de tipos substitui cadeias de overloads:
  ```typescript
  // Em vez de 3 overloads de getElementById, use conditional:
  type ElemById<Tag extends string> = Tag extends keyof HTMLElementTagNameMap
    ? HTMLElementTagNameMap[Tag]
    : HTMLElement;
  declare function getElementById<Tag extends string>(id: Tag): ElemById<Tag>;
  ```
- **Item 53**: Controle a **distribuição de unions sobre conditional types** — nuaked type params distribuem (ex.: filtro `T extends null ? never : T`); use `[T] extends [U]` para impedir distribuição.
- **Item 54**: Use **Template Literal Types** para modelar DSLs e relações entre strings:
  ```typescript
  type Route = `/${string}`;
  type OnEvent = `on${Capitalize<"click" | "focus">}`; // "onClick" | "onFocus"
  type Prop = `${"left" | "right"}${"Top" | "Bottom"}`; // CSS Position
  ```
- **Item 55**: **Escreva testes para seus tipos** (`Expect<Equal<A, B>>` idiom) — tipos complexos são código e merecem suite.
- **Item 56**: Preste atenção em **como os tipos são exibidos** (hover) — se a exibição confunde, o tipo está mal escrito.
- **Item 57**: Prefira generic types **tail-recursive** (recursão no último caso) para evitar profundidade de stack no compilador.
- **Item 58**: Considere **codegen** como alternativa a tipos complexos demais (sintetizar tipos a partir de dados reais).

## Capítulo 7 — TypeScript Recipes (Itens 59–64)

- **Item 59**: Use `never` para **exhaustiveness checking** (o compilador acusa caso faltante em switch de union):
  ```typescript
  function area(shape: Shape): number {
    switch (shape.kind) {
      case "circle": return Math.PI * shape.radius ** 2;
      case "square": return shape.sideLength ** 2;
      default: {
        const _exhaustive: never = shape; // erro se entrar "triangle"
        return _exhaustive;
      }
    }
  }
  ```
- **Item 60**: Saiba iterar objetos com segurança (`Object.entries` com helper genérico tipado, `keyof` + cast controlado).
- **Item 61**: Use **`Record` para manter valores em sincronia** — um `Record<Channel, Handler>` garante handler para cada variante:
  ```typescript
  const handlers: Record<Channel, () => void> = { sms: ..., email: ... };
  ```
- **Item 62**: Use **rest parameters + tuple types** para funções variádicas (`(...args: [string, number])`, spreads tipados, `Parameters<T>`).
- **Item 63**: Use propriedades **optional `never` para modelar XOR** — `a?: never` na variante bloqueia o campo b:
  ```typescript
  type ExclusiveProps =
    | { a: string; b?: never }
    | { a?: never; b: number };
  ```
- **Item 64**: Considere **brands para nominal typing** (o sistema é estrutural; brand adiciona identidade a IDs):
  ```typescript
  type Brand<T, TBrand extends string> = T & { readonly __brand: TBrand };
  type UserId = Brand<string, "UserId">;
  type OrderId = Brand<string, "OrderId">;
  declare function fetchUser(id: UserId): Promise<User>;
  fetchUser(orderId); // ❌ erro — exatamente o que se quer
  ```

## Capítulo 8 — Type Declarations and @types (Itens 65–71)

- **Item 65**: Coloque `typescript` e `@types/*` em `devDependencies` (não afetam prod).
- **Item 66**: Entenda as **três versões envolvidas** em declarações de tipo (versão do TS, do `@types` e da lib) e desalinhamentos.
- **Item 67**: **Exporte todos os tipos que aparecem em APIs públicas** — não force usuários a redeclarar/recriar estruturas.
- **Item 68**: Use **TSDoc** (tags `@param`, `@returns`, `@remarks`) para comentários de API — aparecem no hover.
- **Item 69**: Forneça tipo para `this` em callbacks quando `this` faz parte da API:
  ```typescript
  type AddEventListener_ = (ev: string, cb: (this: HTMLElement, e: Event) => void) => void;
  ```
- **Item 70**: **Espelhe tipos (mirror types)** para quebrar dependências — defina interfaces próprias em vez de importar da biblioteca toda (acoplamento fraco).
- **Item 71**: Use **Module Augmentation** para melhorar tipos de terceiros sem editar o pacote:
  ```typescript
  // types/mirror.d.ts
  declare module "express-serve-static-core" {
    interface Request {
      currentUser?: User;
    }
  }
  // `req.currentUser` agora é tipado em todo o projeto
  ```

## Capítulo 9 — Writing and Running Your Code (Itens 72–78)

- **Item 72**: Prefira **features ECMAScript a features TypeScript** (enums vs `as const` objects, parameter properties, namespaces) — código "só-JS" sobrevive a refactors de bundler.
- **Item 73**: Use **source maps** para debugar TypeScript no debugger/Stack traces.
- **Item 74**: Saiba reconstruir tipos em **runtime** (serialização/roundtrip: `toJSON`/`reviver`, schemas Zod) — tipos não existem em runtime.
- **Item 75**: Entenda a **hierarquia do DOM** (`HTMLElement` → `HTMLCanvasElement`) para usar `instanceof` como narrowing correto.
- **Item 76**: Crie um **modelo preciso do ambiente** (DOM, Node, Web Worker) — o padrão do TS assume `dom`, que pode nem existir.
- **Item 77**: Entenda o relacionamento entre **type checking e testes unitários** — tipos checam compile-time; testes checam runtime; nenhum substitui o outro.
- **Item 78**: Preste atenção na **performance do compilador** (project references, `skipLibCheck`, interfaces incrementais).

## Capítulo 10 — Modernization and Migration (Itens 79–83)

- **Item 79**: Escreva **JavaScript moderno** — o que é válido em ES2015+ transpila menos e migra com menos atrito.
- **Item 80**: Use **`@ts-check` + JSDoc** para experimentar TypeScript num arquivo `.js` sem converter.
- **Item 81**: Use **`allowJs`** para misturar TS e JS no mesmo projeto durante a migração.
- **Item 82**: Converta **módulo por módulo, seguindo o grafo de dependências** (folhas → raiz), mantendo o projeto compilando a cada passo.
- **Item 83**: A migração **só está completa quando `noImplicitAny` estiver habilitado** — sem ele, `any` implícito continua contaminando.

---

### Itens de ouro (resumo executivo)
1. Tipos são conjuntos (Item 7) — sempre pergunte "quais valores cabem aqui?".
2. Estados válidos codificados no tipo (Item 29) — union de estados ≥ flags booleanas.
3. Aceite liberalmente, produza estritamente (Item 30).
4. `unknown` > `any`; `any` com escopo mínimo (Itens 43–46).
5. Derive tipos em vez de duplicar (Itens 15, 23).
6. `never` garante exaustividade (Item 59).
7. Templates literals + conditional types modelam relacionamentos textuais (Itens 52–54).
8. Brands fornecem nominal typing onde falta (Item 64).