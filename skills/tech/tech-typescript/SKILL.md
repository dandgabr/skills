---
name: "tech-typescript"
description: "Fornece padrões de engenharia de software seguro e robusto usando TypeScript, cobrindo generics, tipos avançados, segurança estrita de compilador e mapeamento defensivo de dados."
---

# Habilidade de IA: Engenharia de TypeScript (TypeScript Specialist)

Esta skill orienta a inteligência artificial a escrever código robusto, seguro e altamente tipado utilizando o superset **TypeScript**. O objetivo principal é guiar a IA e desenvolvedores a evitar erros em tempo de execução, construir contratos de API autolimpantes e reutilizáveis, e usufruir ao máximo da segurança estrita fornecida pelo compilador.

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

### 2. Tipagem Avançada e Reutilização
- **Generics**: Construa interfaces, tipos e classes genéricos que se adaptem com segurança a diferentes formatos de dados sem recorrer ao tipo `any`.
- **Utility Types**: Utilize e combine tipos utilitários nativos (`Partial`, `Pick`, `Omit`, `Readonly`, `Record`, `ReturnType`) para manter a legibilidade e evitar duplicação de estruturas de tipos.
- **União Discriminada (Discriminated Unions)**: Use padrões de design que utilizem propriedades literais comuns (como `type` ou `status`) para guiar o compilador TypeScript a inferir tipos corretos em estruturas condicionais (`switch` ou `if`).

### 3. Validação de Tipos em Fronteiras de Dados (API/JSON)
- **Tipagem Defensiva**: Nunca confie cegamente que os dados recebidos de uma requisição HTTP externa ou de arquivos batam com a tipagem declarada.
- **Runtime Validation**: Utilize bibliotecas de validação de esquema em tempo de execução (ex: **Zod**, **Valibot**, **Runtypes**) para inspecionar e garantir o contrato de entrada de dados de forma assíncrona, convertendo-os em tipos válidos TypeScript automaticamente.

---

## 🛠️ Padrões de Código Recomendados

### Evite o uso de `any`
```typescript
// ❌ Ruim: Perda total de tipagem e segurança
function processData(data: any) {
  return data.name.toUpperCase();
}

//  Bom: Uso de tipos específicos ou Generics
function processData<T extends { name: string }>(data: T): string {
  return data.name.toUpperCase();
}
```

### União Discriminada
```typescript
interface NetworkLoadingState {
  state: "loading";
}

interface NetworkFailedState {
  state: "failed";
  code: number;
}

interface NetworkSuccessState {
  state: "success";
  response: { title: string };
}

type NetworkState = NetworkLoadingState | NetworkFailedState | NetworkSuccessState;

function renderState(state: NetworkState) {
  switch (state.state) {
    case "loading":
      return "Carregando...";
    case "failed":
      return `Erro: ${state.code}`; // TypeScript sabe que 'code' existe aqui
    case "success":
      return state.response.title; // TypeScript sabe que 'response' existe aqui
  }
}
```

---

## 🔗 Integração com Outras Skills
- [frontend-developer](../../general/frontend-developer/SKILL.md): Utiliza TypeScript para modular estados e componentes visuais estáveis.
- [backend-developer](../../general/backend-developer/SKILL.md): Constrói contratos tipados de APIs e validações de banco de dados robustas no lado do servidor.
- [clean-code-reusability](../../general/clean-code-reusability/SKILL.md): Fornece princípios de reaproveitamento de código e documentação padrão (JSDoc) aplicados ao desenvolvimento com TypeScript.
