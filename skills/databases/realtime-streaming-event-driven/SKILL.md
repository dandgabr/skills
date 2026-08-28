---
name: realtime-streaming-event-driven
description: Especialista em Arquiteturas de Streaming em Tempo Real, Unificação Batch-Stream e Bancos de Dados de Streaming baseado nas obras Streaming Databases (Hubert Dulay) e Building Real-Time Analytics Systems (Mark Needham). Cobre Apache Kafka, Apache Pinot, Apache Flink, ClickHouse, Change Data Capture (CDC via Debezium) e consultas OLAP em tempo real com sub-segundo de latência.
---

# Arquiteturas de Streaming em Tempo Real e Streaming Databases

Esta skill estabelece padrões para projetar e operar sistemas orientados a fluxos contínuos de eventos, processamento unificado batch-stream e análise OLAP em tempo real com latências na casa dos milissegundos.

---

## ⚡ 1. Arquitetura Lambda vs Kappa vs Unificação em Streaming DB

```
┌─────────────────────────────────────────────────────────────┐
│ Fontes Operacionais (OLTP: Postgres, MySQL, APIs, IoT)     │
└──────────────────────────────┬──────────────────────────────┘
                               │ CDC (Debezium) / Event Producer
┌──────────────────────────────▼──────────────────────────────┐
│ Log de Eventos Distribuído (Apache Kafka / Apache Pulsar)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            │                                     │
┌───────────▼───────────┐             ┌───────────▼───────────┐
│ Processador Stateful  │             │ Streaming OLAP DB     │
│ (Apache Flink)        │             │ (Apache Pinot /       │
│ (Janelas, Agregações) │             │  ClickHouse)          │
└───────────────────────┘             └───────────┬───────────┘
                                                  │
                                      ┌───────────▼───────────┐
                                      │ Dashboards & APIs     │
                                      │ (< 50ms Query Latency)│
                                      └───────────────────────┘
```

---

## 📊 2. Padrões de Change Data Capture (CDC) com Debezium

- **Log-Based CDC**: Leitura direta dos logs de transação do banco de dados (WAL no PostgreSQL, Binlog no MySQL) sem sobrecarga de queries `SELECT` de polling.
- **Outbox Pattern**: Gravação atômica na tabela `outbox` dentro da mesma transação do banco de dados relacional para garantir que eventos de domínio nunca sejam perdidos em falhas de rede.
