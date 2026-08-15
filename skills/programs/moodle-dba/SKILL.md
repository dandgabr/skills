---
name: "program-moodle-dba"
description: "Atua como Administrador de Banco de Dados (DBA) sênior especialista em Moodle LMS, cobrindo modelagem XMLDB, otimização de consultas (EXPLAIN), indexação segura, transações delegadas, particionamento de logs e tuning de MySQL e PostgreSQL."
---

# 🗄️ Administrador de Banco de Dados Moodle (program-moodle-dba)

Esta skill fornece diretrizes rigorosas, padrões de projeto DDL/DML, e boas práticas de tuning de bancos de dados voltadas especificamente para o ecossistema Moodle LMS. Deve ser ativada sempre que o desenvolvedor/DBA precisar projetar tabelas compatíveis com o XMLDB, analisar consultas lentas, implementar transações seguras, otimizar índices ou configurar parâmetros de desempenho para MySQL, MariaDB ou PostgreSQL.

---

## 🎯 Objetivo da Skill
Capacitar o agente a gerenciar, otimizar e manter o banco de dados do Moodle saudável e performático, minimizando deadlocks, otimizando queries geradas por relatórios complexos, estruturando migrações seguras (Upgrades DDL) e saneando tabelas gigantescas (como logs).

---

## 🗃️ Escolha e Configuração do SGBD

### 1. PostgreSQL (Recomendado para Larga Escala)
O PostgreSQL é o motor preferido para ambientes corporativos e acadêmicos com alto volume de acessos concorrentes por lidar melhor com índices parciais, tabelas gigantescas e concorrência de escrita.
*   **Configuração de Conexão no `config.php`**:
```php
$CFG->dbtype    = 'pgsql';      // Driver PostgreSQL
$CFG->dblibrary = 'native';
$CFG->dbhost    = 'db-master.example.com';
$CFG->dbname    = 'moodle';
$CFG->dbuser    = 'moodle_user';
$CFG->dbpass    = 'secure_password';
$CFG->prefix    = 'mdl_';
$CFG->dboptions = array(
    'dbpersist' => false,       // Conexões persistentes degradam a performance em alto tráfego
    'dbport' => '',
    'dbsocket' => '',
    'dbcollation' => 'utf8_bin',
);
```

---

## 🧠 Transações Delegadas e Isolamento no Moodle

O Moodle possui uma API robusta para controle de transações que suporta blocos aninhados de forma segura (Transações Delegadas).
*   **Regra de Ouro**: Sempre use transações ao realizar múltiplas operações de escrita ligadas logicamente para evitar dados inconsistentes se houver uma falha no meio do processo.

```php
global $DB;

try {
    // Inicia a transação delegada
    $transaction = $DB->start_delegated_transaction();

    // Executa operações de escrita no banco
    $DB->insert_record('my_table', $record1);
    $DB->update_record('my_other_table', $record2);

    // Confirma a transação
    $transaction->allow_commit();
} catch (Exception $e) {
    // Caso ocorra qualquer exceção, a transação realiza Rollback automaticamente
    // Faça o log do erro ou propague a exceção
    throw $e;
}
```

---

## 📉 Gerenciamento de Tabelas Gigantes (Estratégias de Logs)

A tabela `mdl_logstore_standard_log` armazena o histórico de todas as ações de usuários dentro da plataforma e é a maior causa de lentidão e estouro de armazenamento.

### 1. Políticas de Retenção e Limpeza
*   **Configuração**: Ajuste o período de retenção de logs nas configurações da plataforma (*Administração do site > Plugins > Logging > Standard log*) para um tempo razoável (ex: 90 a 180 dias) em vez de manter logs vitalícios.
*   **Expurgo via Task**: Garanta que a tarefa agendada `\logstore_standard\task\cleanup_task` esteja habilitada no cron para executar fora do horário de pico.

### 2. Particionamento e Archiving (Enterprise)
Para instâncias com milhões de usuários ativos:
*   Use particionamento de tabela nativo no PostgreSQL/MySQL baseado no campo `timecreated`.
*   Considere configurar o Moodle para usar logs externos ou duplicar a escrita para bancos de BI analíticos, mantendo a tabela operacional limpa.

---

## 🔍 Análise e Criação de Índices Customizados

A criação de índices ajuda a acelerar consultas de relatórios customizados, mas exige cautela.

*   **Evite Conflitos nos Upgrades**: Nunca crie índices diretamente no banco de dados operacional usando comandos SQL puros. Se precisar adicionar um índice a uma tabela própria do plugin, defina-o no arquivo `install.xml` e no script `upgrade.php` usando a API DDL. Do contrário, futuras atualizações de versão do Moodle falharão acusando inconsistências de schema.
*   **Uso de `EXPLAIN`**: Sempre analise queries lentas de relatórios (`local_myreport`) usando `EXPLAIN ANALYZE` (PostgreSQL) ou `EXPLAIN FORMAT=JSON` (MySQL) para identificar se estão realizando *Full Table Scans* e criar índices compostos específicos sobre as chaves mais buscadas.

---

## ⚙️ Parametrização Recomendada (Database Tuning)

### 1. Tuning para MySQL/MariaDB
*   `innodb_buffer_pool_size`: Deve ser definido como ~70-80% da memória RAM física disponível se o servidor de banco for dedicado.
*   `innodb_log_file_size`: Ajuste para `512M` ou `1G` para evitar gargalos durante escrita em lote.
*   `innodb_flush_log_at_trx_commit = 2`: Configuração recomendada para Moodle. Reduz drasticamente a latência de escrita em disco, descarregando o log do buffer uma vez por segundo no disco (ao invés de a cada commit), aceitando um risco mínimo de perda de 1 segundo de dados em caso de queda de energia física.

### 2. Tuning para PostgreSQL
*   `shared_buffers`: Ajuste para 25% da memória RAM total do servidor dedicado.
*   `work_mem`: Aumente para `32MB` ou `64MB` para permitir que consultas com ordenações complexas e `JOINs` rodem diretamente na memória sem gerar escrita temporária em disco.
*   `maintenance_work_mem`: Defina para `256MB` ou `512MB` para acelerar operações de `VACUUM`, `INDEX` e `ALTER TABLE`.
*   `effective_cache_size`: Defina como 50% a 75% da RAM disponível.
*   `autovacuum`: Ajuste a sensibilidade do autovacuum para rodar com mais frequência em tabelas de transição rápida (como logs e tentativas de questionários) para evitar acúmulo de *bloat* (espaço inutilizado).

---

## 🔗 Habilidades Relacionadas
*   **Moodle Core**: [program-moodle](../moodle/SKILL.md) — APIs fundamentais do Moodle e persistência global via `$DB`.
*   **Infraestrutura & Performance**: [program-moodle-infra](../moodle-infra/SKILL.md) — Arquitetura de servidores, caches e locks distribuídos.
*   **Plugins & Ciclo de Vida**: [program-moodle-plugins](../moodle-plugins/SKILL.md) — Scripts de migração `db/upgrade.php` e backup de tabelas.

