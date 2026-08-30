# TypeScript Handbook — Guia de Referência Essencial

Resumo consolidado da documentação oficial do TypeScript Handbook (typescriptlang.org/docs/handbook), cobrindo: The Basics, Everyday Types, Narrowing, Generics e Type Manipulation.

---

## 1. Tipos Primitivos e Regras Fundamentais (Everyday Types)

- **Primitivos**: `string`, `number`, `boolean` (sempre minúsculos — `String`, `Number`, `Boolean` são tipos built-in raros e não devem ser usados).
- **Arrays**: sintaxe `number[]` ou `Array<number>`. `[number]` é **tuple**, não array.
- **`any`**: desabilita toda checagem de tipos para o valor. Ative `noImplicitAny` para flagar `any` implícito como erro.
- **`unknown`**: alternativa segura a `any` — exige narrowing antes de operar sobre o valor.
- **Anotações de tipo** vão **depois** do identificador: `let myName: string = "Alice";`. Prefira deixar o TypeScript **inferir** (menos anotações que você imagina).
- **bigint**: `const big: bigint = 100n;`
- **symbol**: `const s = Symbol("name")` — referência única global, nunca igual a outro Symbol.

## 2. Funções

- Anotações de tipo em parâmetros (após o nome) e retorno (após a lista de parâmetros).
- Funções que retornam Promises: anotar com `Promise<T>` em funções `async`.
- **Contextual typing**: funções anônimas/callbacks parametrizados em locais onde o TS sabe como serão chamados recebem tipos automaticamente (`names.forEach((s) => ...)` — `s` é `string`).
- Parâmetros opcionais: `name?: string` → tipo `string | undefined`; checar antes de usar.

## 3. Tipos de Objetos

- Literais de objeto anônimos: `function printCoord(pt: { x: number; y: number })`.
- **Propriedades opcionais**: `last?: string` — leitura produz `string | undefined`; use `if (obj.last !== undefined)` ou `obj.last?.toUpperCase()`.
- `readonly` para imutabilidade de properties.

## 4. Union Types e Narrowing

- **Union**: `number | string` — valores que podem ser qualquer um dos membros. Só é possível operar com propriedades/funcionalidades válidas para **todos** os membros.
- **Narrowing** (refinar tipo conforme fluxo de runtime):
  - `typeof` type guards (`"string" | "number" | "bigint" | "boolean" | "symbol" | "undefined" | "object" | "function"`). Atenção: `typeof null === "object"` em JS!
  - **Truthiness** (valores falsy: `0`, `NaN`, `""`, `0n`, `null`, `undefined`). Cuidado: truthy check exclui a string vazia — prefira checagens específicas.
  - **Igualdade** (`===`, `!==`; `== null` cobre `null` E `undefined`).
  - Operador **`in`** (`"swim" in animal`) — propriedades opcionais aparecem em ambos os lados.
  - **`instanceof`** (`x instanceof Date`).
  - **Atribuições** e **control flow analysis** (return cedo remove membros do union nos branches seguintes).
- Type predicates (guards customizados):
  ```typescript
  function isFish(pet: Fish | Bird): pet is Fish {
    return (pet as Fish).swim !== undefined;
  }
  ```
  Uso: `zoo.filter(isFish)` produz `Fish[]`.
- Assertion functions (TS 3.7+): funções que "assumem" tipo após a chamada sem error.

## 5. Type Aliases vs Interfaces

| Aspecto | `interface` | `type` |
| :--- | :--- | :--- |
| Estender | `interface Bear extends Animal {...}` | `type Bear = Animal & {...}` |
| Reabrir/acrescentar campos | ✅ (declaration merging) | ❌ (erro de duplicata) |
| Renomear primitivos/unhões | ❌ | ✅ (`type ID = number \| string`) |
| Erros no compilador | Sempre nomeadas (boas mensagens) | Aliases pré-4.2 podiam sumir |
| Performance do compilador | `extends` costuma ser mais rápido | Intersections podem ser mais caras |

**Heurística**: use `interface` até precisar de features de `type`.

## 6. Type Assertions

- `const el = document.getElementById("id") as HTMLCanvasElement;` ou sintaxe angle-bracket `<HTMLCanvasElement>` (não em `.tsx`).
- Removidas em compile-time — **sem checagem em runtime**. Só converta para versões mais específicas/gerais do tipo; para coerções "impossíveis" passe primeiro por `any` ou `unknown` (`expr as unknown as T`).
- **`as const`** converte todo objeto para tipos literais (`method: "GET"` em vez de `string`) — evita erros de literal inference em objetos.

## 7. Literal Types

- Tipos de valores exatos: `"left" | "right" | "center"`, `-1 | 0 | 1`, `true`/`false` (o `boolean` é alias de `true | false`).
- **Literal inference**: propriedades de objetos mutáveis alargam literais para `string` — resolva com assertion no campo ou `as const` no objeto.

## 8. `null`, `undefined` e Non-null Assertion

- Com `strictNullChecks` ON (sempre recomendado): testar antes de usar; narrowing remove `null`/`undefined`.
- **Postfix `!`** remove null/undefined sem checagem — usar apenas quando houver certeza absoluta (preferir narrowing explícito).
- `nullish coalescing` `??` e optional chaining `?.` são os idiomas preferidos.

## 9. Discriminated Unions (padrão central)

```typescript
interface Circle { kind: "circle"; radius: number; }
interface Square { kind: "square"; sideLength: number; }
type Shape = Circle | Square;

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle": return Math.PI * shape.radius ** 2;
    case "square": return shape.sideLength ** 2;
  }
}
```

- Propriedade literal comum (`kind`) = **discriminant**. `switch`/`if` no discriminant estreita o union automaticamente.
- **Exhaustiveness checking** com `never`:
  ```typescript
  default: {
    const _exhaustiveCheck: never = shape; // erro de compilação se sobrar caso
    return _exhaustiveCheck;
  }
  ```
- `never` = estado impossível; atribuível a todo tipo, nada é atribuível a `never` (exceto ele mesmo).
- Ideal para esquemas de mensagens (client/server), estados de máquina e mutações de state management.

## 10. Generics

- **Identity function** genérica: `function identity<Type>(arg: Type): Type { return arg; }` — captura o tipo de entrada e trafega para o retorno (diferente de `any`, que perde informação).
- **Inferência de argumentos de tipo**: `identity("myString")` → `Type = string`. Passe tipo explícito apenas quando a inferência falhar.
- Type variables fazem parte da estrutura: `function loggingIdentity<Type>(arg: Type[]): Type[]`.
- **Constraints** com `extends`:
  ```typescript
  interface Lengthwise { length: number; }
  function loggingIdentity<Type extends Lengthwise>(arg: Type): Type { ... }
  ```
- **Type parameters referenciando outros type parameters**:
  ```typescript
  function getProperty<Type, Key extends keyof Type>(obj: Type, key: Key) {
    return obj[key];
  }
  ```
- **Class types em factories**: `function create<Type>(c: { new (): Type }): Type { return new c(); }` (base para mixins).
- **Defaults de parâmetros genéricos**: `create<T extends HTMLElement = HTMLDivElement>` — regras: param com default é opcional; obrigatórios não podem seguir opcionais; default deve satisfazer a constraint.
- **Classes genéricas**: genéricas apenas na **instance side** (static members não usam o type parameter). Não existem enums/namespaces genéricos.
- **Variance annotations** (`in`/`out`/`in out`): recurso avançado e raro — TS infere variance estruturalmente; nunca escrever annotation que não case com a estrutura. Usar apenas em debugging de performance/extremo caso.

## 11. Criação de Tipos a partir de Tipos (Type Manipulation)

- **Keys**: keyof — `const Key extends keyof Type` (nomes de propriedades como união de literals).
- **Value→Type**: `typeof` operator — `type Config = typeof DEFAULT_CONFIG;`.
- **Indexed Access**: `Type["a"]` — extrai o tipo de uma propriedade.
- **Conditional types**: `T extends U ? X : Y` (if/else do sistema de tipos); combinado com `infer` e distribuição condicional sobre unions.
- **Mapped types**: `{ [K in keyof T]: readonly T[K] }` (base de `Partial`, `Readonly`, etc.).
- **Template Literal Types**: tipos construídos concatenando literals: `type EventName = \`${"on"}${Capitalize<Event>}\``.
- **Utility types** principais a reutilizar: `Partial`, `Required`, `Readonly`, `Pick`, `Omit`, `Record`, `Exclude`, `Extract`, `NonNullable`, `ReturnType`, `InstanceType`, `Parameters`, `Awaited`, `ThisType`.

## 12. Erros de Compilador Comuns (numeração oficial)

| Código | Erro | Causa típica |
| :-: | :--- | :--- |
| 2322 | `'X' is not assignable to type 'Y'` | Atribuição de valor de tipo incompatível |
| 2345 | Argument não assignable | Parâmetro de função com tipo incompatível |
| 2339 | `Property 'x' does not exist on type ...` | Acesso sem narrowing (union/inexistente) |
| 18048 | `'x' is possibly 'undefined'` | Propriedade opcional sem checagem |
| 18047 | `'x' is possibly 'null'` | Valor anulável sem checagem |
| 2352 | Conversion may be a mistake | Type assertion entre tipos sem sobreposição (usar `as unknown as`) |
| 2367 | Comparison appears to be unintentional | Comparação sem overlap (literal errado, typo) |
| 2872 | This kind of expression is always truthy | Truthiness check desnecessário |