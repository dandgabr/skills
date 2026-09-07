---
name: framework-quarkus-jnosql
description: "Fornece padrões de desenvolvimento Cloud-Native com Quarkus, GraalVM Native Image e persistência poliglota NoSQL utilizando Eclipse JNoSQL, Jakarta NoSQL e Jakarta Data."
---

# Quarkus & Eclipse JNoSQL Cloud-Native Engineering

Esta skill estabelece padrões avançados de desenvolvimento Cloud-Native em Java utilizando o ecossistema **Quarkus** e **Eclipse JNoSQL** (Jakarta NoSQL / Jakarta Data).

---

## 🧭 1. Fundamentos e Filosofia Quarkus
- **Supersonic Subatomic Java**: Inicialização instantânea e pegada de memória ultrabaixa via compilação antecipada (*Ahead-of-Time - AOT*) com GraalVM Native Image.
- **Build-Time Metaprogramming**: Injeção de dependências via ArC (CDI estático resolvido em tempo de compilação) e eliminação de reflection dinâmica.
- **Arquitetura Reativa e Imperativa Unificada**: Suporte transparente a chamadas bloqueantes gerenciadas por Virtual Threads ou código reativo com Mutiny.

---

## 🗄️ 2. Persistência Poliglota com Eclipse JNoSQL e Jakarta Data
- **Modelos Suportados**:
  - *Documento*: MongoDB, Couchbase.
  - *Chave-Valor*: Redis, DynamoDB.
  - *Colunar*: Apache Cassandra, ScyllaDB.
  - *Grafo*: Neo4j.
- **Padrão de Repositórios Jakarta Data**:
  - Interface declarativa estendendo repositórios tipados:
    ```java
    @Repository
    public interface CustomerRepository extends CrudRepository<Customer, String> {
        List<Customer> findByCity(String city);
    }
    ```
- **Mapeamento de Entidades**: Anotações `@Entity`, `@Id`, `@Column` independentes do banco subjacente, garantindo portabilidade entre provedores NoSQL.

---

## 🚀 3. Boas Práticas para GraalVM Native Image
- Evitar classes dinâmicas, proxies CGLIB e reflection não declarada.
- Registrar DTOs e entidades de serialização JSON com `@RegisterForReflection`.
- Manter o Quarkus Dev Mode (`quarkus dev`) ativo para hot reload instantâneo durante o ciclo de desenvolvimento.
