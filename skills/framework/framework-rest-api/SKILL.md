---
name: "framework-rest-api"
description: "Fornece padrões de engenharia e design para APIs RESTful baseados na especificação OpenAPI 3.1 e RFCs do IETF. Cobre semântica de verbos HTTP, status codes, padronização de erros RFC 7807, paginação, HATEOAS, versionamento, rate limiting e segurança OAuth2/JWT."
---

# Habilidade de IA: Design e Engenharia de APIs RESTful (framework-rest-api)

Esta skill orienta a inteligência artificial a atuar como especialista em design, arquitetura e implementação de **APIs RESTful**, alinhada rigorosamente às especificações do IETF, especificações **OpenAPI 3.1** e padrões da indústria para construção de serviços web interoperáveis, performáticos e seguros.

---

## 🧭 Princípios de Design de Recursos e Semântica HTTP

### 1. Nomenclatura e Hierarquia de URIs
- Use substantivos no plural para identificar coleções de recursos (`/api/v1/users`, `/api/v1/orders`).
- Reflita hierarquia e relacionamentos na estrutura da URL (`/api/v1/users/{userId}/orders`).
- Utilize letras minúsculas e hífens para separar palavras (`snake-case` ou `kebab-case` na URL, mantendo consistência).

### 2. Semântica dos Verbos HTTP
| Verbo | Propósito | Idempotente? | Seguro (Safe)? | Resposta Típica de Sucesso |
| :--- | :--- | :---: | :---: | :--- |
| **GET** | Recuperar representação de recurso(s) | Sim | Sim | `200 OK` |
| **POST** | Criar um novo recurso subordinado ou ação | Não | Não | `201 Created` (com header `Location`) |
| **PUT** | Substituir integralmente um recurso existente | Sim | Não | `200 OK` ou `204 No Content` |
| **PATCH** | Modificar parcialmente um recurso | Não* | Não | `200 OK` ou `204 No Content` |
| **DELETE** | Remover um recurso | Sim | Não | `204 No Content` ou `200 OK` |
| **HEAD** | Recuperar apenas os cabeçalhos (metadados) | Sim | Sim | `200 OK` (sem corpo) |
| **OPTIONS** | Consultar métodos e opções suportadas (CORS) | Sim | Sim | `204 No Content` |

---

## 🛠️ Tratamento de Erros Padronizado (RFC 7807 - Problem Details)

Não retorne formatos de erro proprietários ou códigos de status genéricos `200 OK` com payload de erro. Adote o padrão **RFC 7807 (Problem Details for HTTP APIs)** com `Content-Type: application/problem+json`:

```json
{
  "type": "https://api.empresa.com/errors/insufficient-funds",
  "title": "Saldo insuficiente para transação",
  "status": 422,
  "detail": "A conta 12345 possui R$ 50,00 disponíveis, mas a operação exige R$ 120,00.",
  "instance": "/api/v1/accounts/12345/transfers/txn_998877",
  "invalid_params": [
    {
      "name": "amount",
      "reason": "O valor excede o limite disponível"
    }
  ]
}
```

---

## 🔍 Paginação, Filtragem, Ordenação e Rate Limiting

### 1. Paginação de Alto Desempenho
- **Paginação baseada em Cursor (Recomendada para alta escala)**:
  - `GET /api/v1/events?limit=20&starting_after=evt_12345`
- **Paginação Offset/Limit (Uso em tabelas com navegação direta de páginas)**:
  - `GET /api/v1/users?page=2&limit=50`

### 2. Rate Limiting e Cabeçalhos de Resposta (RFC 6585)
Sempre informe os limites de requisição nos cabeçalhos de resposta:
```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1770460000
```

---

## 🔒 Segurança em APIs REST

1. **Autenticação & Autorização**:
   - Utilize tokens bearer **JWT (JSON Web Token)** transmitidos no cabeçalho `Authorization: Bearer <token>`.
   - Implemente controle de acesso granular baseados em escopos (**OAuth 2.0 / OpenID Connect**).
2. **CORS (Cross-Origin Resource Sharing)**:
   - Configure o cabeçalho `Access-Control-Allow-Origin` para origens estritamente confiáveis. Proíba o uso de wildcard `*` em APIs autenticadas.
3. **Idempotência em Operações Críticas**:
   - Suporte o cabeçalho `Idempotency-Key` em operações `POST` de pagamento ou criação de pedidos para evitar duplicações por retentativas de rede.

---

## 🔗 Integração com Outras Skills

- Para projetar a arquitetura completa e integração com backend, consulte [backend-developer](../../general/roles/backend-developer/SKILL.md) e [software-architect](../../general/roles/software-architect/SKILL.md).
- Para auditoria de vulnerabilidades em APIs REST segundo o OWASP API Security Top 10 2023, consulte [pentester-owasp-api-security-2023](../../security/appsec/pentester-owasp-api-security-2023/SKILL.md) e [appsec-owasp-asvs](../../security/appsec/appsec-owasp-asvs/SKILL.md).
- Para implementar APIs RESTful em TypeScript ou Python, consulte [lang-typescript](../../languages/lang-typescript/SKILL.md) e [lang-python](../../languages/lang-python/SKILL.md).
