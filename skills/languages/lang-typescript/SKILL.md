---
name: "lang-typescript"
description: "Fornece padrões de engenharia de software seguro e robusto usando TypeScript baseado na documentação oficial do TypeScript Handbook (typescriptlang.org), Effective TypeScript 2nd Edition (Dan Vanderkam) e Total TypeScript Essentials (Matt Pocock), cobrindo tipos primitivos e avançados, narrowing e type guards, discriminated unions com exhaustiveness checking, generics com constraints, type manipulation (keyof, conditional, mapped, template literal types), utility types, segurança estrita de compilador e mapeamento defensivo de dados."
---

# Habilidade de IA: Engenharia de TypeScript (TypeScript Specialist)

Esta skill orienta a inteligência artificial a escrever código robusto, seguro e altamente tipado utilizando o superset **TypeScript**, alinhada ao **TypeScript Handbook oficial** (https://www.typescriptlang.org/docs/handbook/intro.html), a *Effective TypeScript 2nd Edition* (Dan Vanderkam) e a *Total TypeScript Essentials* (Matt Pocock). O objetivo principal é guiar a IA e desenvolvedores a evitar erros em tempo de execução, construir contratos de API autolimpantes e reutilizáveis, e usufruir ao máximo da segurança estrita fornecida pelo compilador.

> 📖 **Referência canônica**: consulte [references/typescript-handbook.md](references/typescript-handbook.md) para o guia consolidado do Handbook (everyday types, narrowing, generics, type manipulation, Utility Types e tabela de códigos de erro TS).
> 📖 **Effective TypeScript**: consulte [references/effective-typescript-83-items.md](references/effective-typescript-83-items.md) para os 83 items de melhor prática de *Effective TypeScript 2nd Edition* (type design, generics, unsoundness, migrations).
> 📖 **Total TypeScript**: consulte [references/total-typescript-essentials.md](references/total-typescript-essentials.md) para o resumo dos 16 capítulos de *Total TypeScript Essentials* (narrowing, mutability, classes, deriving types, tsconfig, declaration files).

---

## 🧭 Diretrizes de Desenvolvimento em TypeScript

Ao atuar nesta skill, aplique rigorosamente os seguintes padrões de codificação:

### 1. Configuração Estrita do Compilador (`tsconfig.json`)
- **Strict Mode**: Garanta que as seguintes flags estejam habilitadas para máxima proteção contra nulos e tipos indefinidos:
  ```json
  {
    "compilerOptions": {
      "strict": true,
      "noImplicitAny": true,
      "strictNullChecks": true,
      "strictFunctionTypes": true,
      "noImplicitThis": true,
      "alwaysStrict": true,
      "noUnusedLocals": true,
      "noUnusedParameters": true,
      "noImplicitReturns": true,
      "noFallthroughCasesInSwitch": true
    }
  }
  ```

### 2. Tipagem Fundamentada no Handbook
- **Primitivos Corretos**: Sempre use `string`, `number`, `boolean` (minúsculos). Nunca `String`/`Number`/`Boolean`. Sem `int`/`float` — tudo é `number` (exceto `bigint` para inteiros gigantes via literal `100n`).
- **Infração de Anotações**: Prefira deixar o TypeScript **inferir** tipos; anote apenas parâmetros/retorno de função expostos a contratos e fronteiras. Anotações ficam **após** o identificador (`let x: string`).
- **Generics com Constraints**: Construa componentes genéricos que adaptam-se a diferentes formatos — captures o tipo de entrada e trafegue-o para a saída (`<Type>(arg: Type): Type`), com `extends` para garantir capacidades (`Lengthwise`) e `Key extends keyof Type` para acesso seguro a propriedades. Nunca recorra a `any` para "resolver" o problema.
- **Preferência `interface` vs `type`**: Use `interface` até precisar de features de `type` (unions, renomeação de primitivos, conditional types). Interfaces têm declaration merge, aparecem nomeadas em mensagens de erro e costumam ser mais performáticas com `extends`.
- **Utility Types**: Utilize e combine tipos utilitários nativos (`Partial`, `Pick`, `Omit`, `Readonly`, `Record`, `ReturnType`, `NonNullable`, `Exclude/Extract`, `Awaited`) e **Type Manipulation** (`keyof`, `typeof` operator, Indexed Access, Conditional Types com `infer`, Mapped Types, Template Literal Types) para manter legibilidade e evitar duplicação de estruturas.
- **União Discriminada (Discriminated Unions + Exhaustiveness)**: Modele estados e mensagens com propriedade discriminante literal (`kind`, `type`, `status`) e `switch` com **exhaustiveness checking via `never`** — o compilador acusa erro quando um novo membro entra na união sem tratamento.

### 3. Narrowing e Type Guards
- Use o arsenal de narrowing nativo no lugar de assertions: `typeof`, truthiness (com consciência dos falsy: `0, NaN, "", 0n, null, undefined`), igualdade estrita (`===`), `in`, `instanceof`, **control flow analysis** (returns cedo).
- **Type Predicates**: Crie guards customizados com `pet is Fish` para reutilizar lógica de checagem (inclusive em `Array.filter`).
- **Assertions com Moderação**: `as T` é removido em compile-time (zero verificação em runtime). Use apenas com conversões "possíveis"; para coerções complexas, `expr as unknown as T`. Prefira `as const` em objetos para preservar literal types (evitar literal inference alargando `"GET"` → `string`).

### 4. Validação de Tipos em Fronteiras de Dados (API/JSON)
- **Tipagem Defensiva**: Nunca confie cegamente que os dados recebidos de uma requisição HTTP externa ou de arquivos batam com a tipagem declarada — *type assertions não validam em runtime*.
- **Runtime Validation**: Utilize bibliotecas de validação de esquema em tempo de execução (ex: **Zod**, **Valibot**, **Runtypes**) para inspecionar e garantir o contrato de entrada de dados, convertendo-os em tipos válidos TypeScript automaticamente (inference de schema).

---

## 🛠️ Padrões de Código Recomendados

### Evite o uso de `any` — prefira generics ou `unknown`
```typescript
// ❌ Ruim: Perda total de tipagem e segurança
function processData(data: any) {
  return data.name.toUpperCase();
}

//  Bom: Uso de tipos específicos ou Generics
function processData<T extends { name: string }>(data: T): string {
  return data.name.toUpperCase();
}

//  Bom: Entrada arbitrária com contrato explícito antes do uso
function parseJson(input: string): unknown {
  return JSON.parse(input);
}
```

### União Discriminada com Exhaustiveness Checking
```typescript
interface Circle { kind: "circle"; radius: number; }
interface Square { kind: "square"; sideLength: number; }
interface Triangle { kind: "triangle"; sideLength: number; }

type Shape = Circle | Square | Triangle;

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    case "triangle":
      return (shape.sideLength ** 2) / 2;
    default: {
      // Erro de compilação se um novo membro entrar na união sem case
      const _exhaustiveCheck: never = shape;
      return _exhaustiveCheck;
    }
  }
}
```

### Type Guard Customizado (Type Predicate)
```typescript
function isFish(pet: Fish | Bird): pet is Fish {
  return "swim" in pet;
}

const zoo: (Fish | Bird)[] = getZoo();
const fishes: Fish[] = zoo.filter(isFish); // narrowing preservado no filtro
```

---

## 🔒 Questões de Segurança e Práticas Seguras

- **Prototype Pollution**: Valide e sanitize chaves de objetos que sofrem mesclagem recursiva (deep merge) para evitar a injeção indesejada de propriedades nas classes base do JavaScript (como `__proto__`).
- **Injeção de Código Dinâmico**: Nunca utilize `eval()`, `Function()` ou passagem de strings para o manipulador `setTimeout()`.
- **Ataques de ReDoS**: Valide limites de tempo de execução e complexidade em padrões regex aplicados em validação de inputs no servidor Node.js.
- **Deserialização Insegura de JSON**: Trate o resultado de `JSON.parse` como `unknown` e valide com schema em runtime antes de operar sobre o valor.
- **Non-null Assertion (`!`) Responsável**: O postfix `!` remove `null`/`undefined` sem checagem — usar apenas com certeza absoluta; preferir narrowing explícito (`if (x !== null)`, `??`, `?.`).

## 🎯 Regras de Ouro de Type Design (Effective TypeScript)

Consolidação dos items de *Effective TypeScript 2nd Edition* (detalhes em [references/effective-typescript-83-items.md](references/effective-typescript-83-items.md)):

- **Item 29 — Estados válidos sempre**: Modele o tipo para que estados inválidos sejam **irrepresentáveis** (`type PageState = { state: "loading" } | { state: "error"; error: string } | { state: "ready"; page: Page }`) em vez de flags booleans soltas e campos opcionais.
- **Item 30 — Liberal em entradas, estrito em saídas**: Parâmetros aceitam tipos largos (unions); retornos/exports são precisos e fechados.
- **Item 34 — União de interfaces > interface com uniões**: Cada variante carrega seus campos obrigatórios (`FileLayer | DatabaseLayer`) em vez de campos opcionais misturados.
- **Item 32/33 — Null na periferia**: Não embuta `null`/`undefined` em aliases reutilizáveis; trate-os cedo, no boundary.
- **Item 35 — Não use `string` cru para domínios finitos**: Use literal unions, branded types ou template literal types para IDs, status, rotas e eventos.
- **Item 37 — Limite propriedades opcionais**: `?` gera `| undefined` e estado vago; prefira uniões discriminadas explícitas.
- **Item 38 — Evite parâmetros posicionais confundíveis**: Agrupe parâmetros repetidos do mesmo tipo num objeto (`{ index: number; count: number }`).
- **Item 40 — Impreciso > impreciso**: Prefira um tipo "largo mas correto" a um type assertion que mente ao compilador (`as never`), jamais um **tipo impreciso** que não reflete a realidade.
- **Item 9/45 — Anote, não asserte; isole o inseguro**: Prefira anotações a `as`; se inevitável, esconda a assertion unsafe dentro de uma função bem tipada.
- **Item 46/43 — `unknown` > `any`**: Use `unknown` para valores desconhecidos; `any`, quando inevitável, com o menor escopo possível.
- **Item 15/23 — Derive, não duplique**: Use `keyof`, `typeof`, indexed access e generics para evitar repetição e mantenha aliases consistentes em todo o codebase.
- **Item 67/68 — Exporte tipos e documente com TSDoc**: Todo tipo que aparece em API pública é exportado; semântica extra vai em comentários TSDoc (`@param`, `@returns`).
- **Item 64 — Brands para nominal typing**: Quando IDs tipados precisam não ser confundíveis (`UserId` ≠ `OrderId`), use branded types via interseção.
- **Item 72 — Prefira features ECMAScript**: Enums/parameter properties/namespaces são TS-only; prefira `as const` objects e modules ES puros.

## 🔍 Narrowing Eficiente (Total TypeScript)

Formas de narrowing (preferência nesta ordem — detalhes em [references/total-typescript-essentials.md](references/total-typescript-essentials.md)):

```typescript
type Format = "digital" | "physical";
type Album =
  | { format: "digital"; downloadUrl: string }
  | { format: "physical"; shippingAddress: string };

// 1) Discriminant / disjoint union (melhor desenho possível)
function refund(album: Album): string {
  if (album.format === "digital") return album.downloadUrl;  // narrowed: variante digital
  return album.shippingAddress;                              // narrowed: variante physical
}

// 2) typeof (primitivos) — cuidado com typeof null === "object"
function parse(input: string | number) {
  if (typeof input === "string") return input.trim();
  return input.toFixed(2);
}

// 3) Operador in — existência de propriedade
function hasDownload(album: Album) {
  return "downloadUrl" in album;
}

// 4) Truthiness/nullish (atenção aos falsy: 0, "", NaN, null, undefined)
function name(user: string | null) {
  return user?.toUpperCase() ?? "anonymous";
}

// 5) Exhaustiveness com never: o compilador acusa variante faltante
function label(album: Album): string {
  switch (album.format) {
    case "digital":  return "download";
    case "physical": return "shipping";
    default: {
      const _exhaustive: never = album; // erro se entrar novo formato sem case
      return _exhaustive;
    }
  }
}
```

Regras de ouro complementares (*Total TypeScript*): use `satisfies` em vez de `as` (valida sem alargar); prefira `@ts-expect-error` a `@ts-ignore` (falha quando o erro desaparece); `const` e `as const` estreitam literais que `let` e objetos mutáveis alargam.

---

## 🔗 Integração com Outras Skills
- [frontend-developer](../../roles/frontend-developer/SKILL.md): Utiliza TypeScript para criar aplicações com [framework-react](../../framework/framework-react/SKILL.md) e [framework-vue](../../framework/framework-vue/SKILL.md).
- [backend-developer](../../roles/backend-developer/SKILL.md): Constrói contratos tipados de APIs RESTful ([framework-rest-api](../../framework/framework-rest-api/SKILL.md)) e clientes/servidores gRPC ([framework-grpc](../../framework/framework-grpc/SKILL.md)).
- [dba-database-administrator](../../roles/dba-database-administrator/SKILL.md): Modela e otimiza acessos de dados em TypeScript (Prisma, TypeORM, Drizzle, Mongoose) alinhados aos motores [db-postgresql](../../databases/db-postgresql/SKILL.md), [db-mongodb](../../databases/db-mongodb/SKILL.md), [db-mariadb](../../databases/db-mariadb/SKILL.md) e [db-sqlite](../../databases/db-sqlite/SKILL.md).
- [clean-code-reusability](../../engineering-practices/clean-code-reusability/SKILL.md): Fornece princípios de reaproveitamento de código e documentação padrão (JSDoc) aplicados ao desenvolvimento com TypeScript.