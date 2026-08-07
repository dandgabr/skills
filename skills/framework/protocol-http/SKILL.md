---
name: "protocol-http"
description: "Fornece padrões de arquitetura e engenharia do protocolo HTTP (HTTP/1.1, HTTP/2, HTTP/3, RFC 9110/9112/9113/9114 e RFC 10008). Cobre semântica completa de verbos incluindo QUERY, códigos de status, negociação de conteúdo, cabeçalhos de segurança, CORS, estratégias de caching e suporte de proxies/CDNs."
---

# Habilidade de IA: Engenharia e Arquitetura do Protocolo HTTP (protocol-http)

Esta skill orienta a inteligência artificial a atuar como especialista no **Protocolo de Transferência de Hipertexto (HTTP)**, alinhada rigorosamente às especificações do IETF (RFC 9110 HTTP Semantics, RFC 9112 HTTP/1.1, RFC 9113 HTTP/2, RFC 9114 HTTP/3) e ao padrão **RFC 10008 (HTTP QUERY Method)**. Cobre a semântica de métodos, códigos de status, negociação de conteúdo, políticas de caching, cabeçalhos de segurança, suporte a CORS e evolução de transporte sobre TCP e QUIC.

---

## 🧭 Semântica dos Verbos e Métodos HTTP (RFC 9110 & RFC 10008)

### 1. Métodos Padronizados e Suas Propriedades

| Método | Corpo na Requisição | Corpo na Resposta | Seguro (Safe)? | Idempotente? | Cacheável? | Padrão IETF |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **GET** | Não | Sim | Sim | Sim | Sim | RFC 9110 |
| **QUERY** | **Sim** | **Sim** | **Sim** | **Sim** | **Sim** | **RFC 10008** |
| **POST** | Sim | Sim | Não | Não | Condicional | RFC 9110 |
| **PUT** | Sim | Sim | Não | Sim | Não | RFC 9110 |
| **PATCH** | Sim | Sim | Não | Não | Condicional | RFC 5789 / RFC 9110 |
| **DELETE** | Opcional | Sim | Não | Sim | Não | RFC 9110 |
| **HEAD** | Não | Não | Sim | Sim | Sim | RFC 9110 |
| **OPTIONS** | Opcional | Sim | Sim | Sim | Não | RFC 9110 |
| **TRACE** | Não | Sim | Sim | Sim | Não | RFC 9110 |
| **CONNECT** | Não | Sim | Não | Não | Não | RFC 9110 |

### 2. O Método `QUERY` (RFC 10008)
O método `QUERY` foi introduzido pelo IETF para resolver a dicotomia histórica entre `GET` (seguro/idempotente, mas sem corpo na requisição) e `POST` (suporta corpo, mas não é seguro nem idempotente):
- **Casos de Uso**: Consultas complexas com múltiplos filtros, expressões DSL, buscas full-text ou payloads JSON/XML que excederiam limites de tamanho de URL ou vazariam dados sensíveis em logs de acesso Web/CDN.
- **Regras de Caching**: Caches e proxies reversos podem armazenar respostas de `QUERY`. A **chave de cache (*Cache Key*)** deve obrigatoriamente incluir a URI e o *digest* do corpo da requisição (`Content-Type` + corpo).
- **Semântica CORS**: Por não fazer parte dos *CORS-safelisted methods* (`GET`, `HEAD`, `POST`), requisições `QUERY` em navegadores web sempre exigem uma chamada preflight via `OPTIONS`.

```http
QUERY /api/v1/analytics/reports HTTP/1.1
Host: api.empresa.com
Content-Type: application/json
Accept: application/json

{
  "dimensions": ["country", "device_type"],
  "metrics": ["page_views", "conversion_rate"],
  "date_range": {
    "start": "2026-01-01",
    "end": "2026-06-30"
  },
  "filter": {
    "field": "revenue",
    "operator": "gt",
    "value": 5000
  }
}
```

---

## 🚦 Códigos de Status HTTP (HTTP Status Codes)

- **1xx (Informativos)**: `100 Continue`, `101 Switching Protocols`, `103 Early Hints`.
- **2xx (Sucesso)**:
  - `200 OK`: Requisição processada com sucesso.
  - `201 Created`: Recurso criado com sucesso (retornar header `Location`).
  - `202 Accepted`: Processamento assíncrono aceito (retornar endpoint de status).
  - `204 No Content`: Ação executada com sucesso sem corpo de resposta.
  - `206 Partial Content`: Resposta a requisições com cabeçalho `Range`.
- **3xx (Redirecionamento & Cache)**:
  - `301 Moved Permanently`: Redirecionamento permanente (pode alterar verbo para GET).
  - `304 Not Modified`: Conteúdo não alterado com base em validação (`ETag` / `If-None-Match`).
  - `307 Temporary Redirect`: Redirecionamento temporário (preserva o método HTTP original).
  - `308 Permanent Redirect`: Redirecionamento permanente (preserva o método HTTP original).
- **4xx (Erros do Cliente)**:
  - `400 Bad Request`: Sintaxe da requisição malformada.
  - `401 Unauthorized`: Autenticação necessária ou token inválido.
  - `403 Forbidden`: Autenticado, mas sem permissão de acesso ao recurso.
  - `404 Not Found`: Recurso não encontrado.
  - `405 Method Not Allowed`: Método HTTP não suportado pela rota.
  - `409 Conflict`: Conflito de estado no servidor (ex: chave duplicada).
  - `412 Precondition Failed`: Falha nas pré-condições (ex: `If-Match` para Lock Otimista).
  - `415 Unsupported Media Type`: `Content-Type` não suportado.
  - `422 Unprocessable Entity`: Erro de validação semântica dos dados.
  - `429 Too Many Requests`: Limite de requisições excedido (Rate Limit).
- **5xx (Erros do Servidor)**:
  - `500 Internal Server Error`: Erro não tratado no backend.
  - `502 Bad Gateway`: Resposta inválida recebida do servidor upstream.
  - `503 Service Unavailable`: Servidor indisponível ou em manutenção.
  - `504 Gateway Timeout`: Tempo limite esgotado ao aguardar upstream.

---

## ⚡ Caching e Negociação de Conteúdo

### 1. Cabeçalhos de Caching Revalidação
- **Controle Primário**: `Cache-Control: public, max-age=3600, stale-while-revalidate=60`.
- **Validação de Frescor (Fresness Validation)**:
  - `ETag: W/"59-18c72a80f08"` e `If-None-Match: W/"59-18c72a80f08"`
  - `Last-Modified: Fri, 07 Aug 2026 10:00:00 GMT` e `If-Modified-Since: Fri, 07 Aug 2026 10:00:00 GMT`

### 2. Negociação de Conteúdo e Compressão
- **Formato**: `Accept: application/json, text/plain`, `Content-Type: application/json; charset=utf-8`.
- **Compressão de Transporte**: `Accept-Encoding: gzip, deflate, br, zstd` e `Content-Encoding: br`.

---

## 🔒 Segurança de Protocolo e CORS

### 1. Cabeçalhos Recomendados de Segurança Web (Security Headers)
```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; frame-ancestors 'none'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), camera=(), microphone=()
```

### 2. Cross-Origin Resource Sharing (CORS)
- Para requisições de origem cruzada que utilizam métodos não-safelisted (`PUT`, `DELETE`, `PATCH`, `QUERY`) ou cabeçalhos customizados, o navegador enviará uma requisição **Preflight**:

```http
OPTIONS /api/v1/analytics/reports HTTP/1.1
Host: api.empresa.com
Origin: https://app.empresa.com
Access-Control-Request-Method: QUERY
Access-Control-Request-Headers: Content-Type, Authorization

HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://app.empresa.com
Access-Control-Allow-Methods: GET, QUERY, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 86400
```

---

## 🚀 Evolução das Camadas de Transporte (HTTP/1.1 vs HTTP/2 vs HTTP/3)

1. **HTTP/1.1**: Baseado em texto claro sobre TCP. Sofre de *Head-of-Line (HoL) Blocking* na camada de aplicação. Requer múltiplas conexões TCP paralelas.
2. **HTTP/2 (RFC 9113)**: Binário e multiplexado sobre uma única conexão TCP. Introduz *Framing*, compressão de cabeçalhos **HPACK** e *Server Push* (descontinuado em prol de Early Hints).
3. **HTTP/3 (RFC 9114)**: Construído sobre **QUIC** (UDP com TLS 1.3 integrado). Elimina o *Head-of-Line Blocking* na camada de transporte TCP, suportando migração suave de conexão de rede (WiFi -> 5G).

---

## 🔗 Integração com Outras Skills

- Para design e construção de APIs RESTful utilizando OpenAPI e semântica de recursos, consulte [framework-rest-api](../framework-rest-api/SKILL.md).
- Para APIs RPC e GraphQL sobre HTTP, consulte [framework-grpc](../framework-grpc/SKILL.md), [framework-graphql](../framework-graphql/SKILL.md) e [framework-soap](../framework-soap/SKILL.md).
- Para testes de penetração e segurança de aplicações Web e APIs, consulte [pentest-web-application-modern](../../security/appsec/pentest-web-application-modern/SKILL.md) e [pentester-owasp-api-security-2023](../../security/appsec/pentester-owasp-api-security-2023/SKILL.md).
- Para criptografia de transporte TLS 1.3, ECH e mTLS em HTTP, consulte [cryptography-pqc-standards](../../security/crypto-pki/cryptography-pqc-standards/SKILL.md).
