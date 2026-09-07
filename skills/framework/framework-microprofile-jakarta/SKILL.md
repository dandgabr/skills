---
name: framework-microprofile-jakarta
description: "Fornece padrões e convenções corporativas para servidores e microsserviços Java baseados em Eclipse MicroProfile 6.x+ e Jakarta EE 10/11+ (JAX-RS, CDI, JSON-P/B, Config, Fault Tolerance, Health/Metrics)."
---

# MicroProfile & Jakarta EE Server Engineering

Esta skill orienta a construção de microsserviços e aplicações corporativas em conformidade com as especificações abertas **Eclipse MicroProfile 6.x+** e **Jakarta EE 10/11+** (Payara, Open Liberty, WildFly, Helidon).

---

## 🧭 1. Pilares da Especificação MicroProfile
1. **JAX-RS (Jakarta RESTful Web Services)**: Definição de endpoints HTTP com anotações `@Path`, `@GET`, `@POST`, `@Produces(MediaType.APPLICATION_JSON)`.
2. **CDI (Contexts and Dependency Injection)**: Gerenciamento de ciclo de vida com escopos estritos (`@ApplicationScoped`, `@RequestScoped`).
3. **MicroProfile Config**: Parametrização desacoplada via `microprofile-config.properties` e variáveis de ambiente com `@ConfigProperty`.
4. **MicroProfile Fault Tolerance**: Resiliência nativa com `@Timeout`, `@Retry`, `@CircuitBreaker`, `@Bulkhead` e `@Fallback`.
5. **Health & Metrics**: Endpoints padronizados de liveness/readiness (`/health/live`, `/health/ready`) e telemetria aberta com MicroProfile Telemetry / Metrics.

---

## 🏢 2. Regras de Isolamento Arquitetural
- Manter regras de domínio puras e desacopladas das anotações de transporte JAX-RS.
- Usar Bean Validation (`@Valid`) na borda da aplicação para rejeição precoce de payloads inválidos.
- Em projetos que utilizam arquitetura Boundary-Control-Entity (BCE), o boundary implementa os recursos JAX-RS e os injeta nos controls de negócio.
