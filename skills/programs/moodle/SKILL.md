---
name: "program-moodle"
description: "Atua como especialista sênior em desenvolvimento e customização do Moodle LMS, cobrindo arquitetura de plugins (Frankenstyle), APIs principais (DB, Form, Page, Output), controle de acessos, Web Services, Hooks modernos e API de privacidade."
---

# 🎓 Especialista em Moodle LMS (program-moodle)

Esta skill fornece diretrizes rigorosas, padrões de arquitetura e boas práticas de engenharia de software para o ecossistema Moodle LMS (Learning Management System). Deve ser ativada sempre que tarefas de criação de plugins, modificações no core, desenvolvimento de integrações, consumo ou criação de Web Services ou depuração de ambientes Moodle forem solicitadas.

---

## 🎯 Objetivo da Skill
Capacitar o agente a atuar como um Desenvolvedor Moodle Sênior, garantindo que qualquer extensão ou código escrito respeite os padrões estritos do Moodle, a arquitetura modular, as APIs internas do core, as diretrizes de acessibilidade e a segurança de dados.

---

## 🛠️ Diretrizes de Desenvolvimento Moodle

### 1. Padrão de Nomenclatura (Frankenstyle)
Toda extensão no Moodle precisa seguir a convenção de nomenclatura única chamada **Frankenstyle**, que combina o tipo de plugin com o nome do plugin:
*   **Formato**: `[tipo]_[nome]` (ex: `mod_board`, `block_online_users`, `local_user_sync`).
*   **Regra**: Apenas letras minúsculas e caracteres alfanuméricos. O caractere `_` separa apenas o tipo de plugin do nome do plugin.
*   **Tipos Comuns**:
    *   `mod`: Módulos de Atividades (ex: `mod_assign`)
    *   `block`: Blocos laterais (ex: `block_html`)
    *   `local`: Funcionalidades locais genéricas (ex: `local_moodlebot`)
    *   `auth`: Plugins de autenticação (ex: `auth_oauth2`)
    *   `enrol`: Métodos de inscrição (ex: `enrol_manual`)
    *   `theme`: Temas visuais (ex: `theme_boost`)
    *   `tool`: Ferramentas administrativas (ex: `tool_generator`)

### 2. Estrutura de Diretórios Padrão (Exemplo para um plugin `local_myplugin`)
```text
local/myplugin/
├── classes/                # Classes autoloaded (PSR-4: local_myplugin\...)
│   ├── privacy/            # Provedores de Privacidade (GDPR/LGPD)
│   └── task/               # Tarefas agendadas ou ad-hoc
├── db/                     # Definições de banco de dados e APIs
│   ├── access.php          # Definições de Capabilities (permissões)
│   ├── events.php          # Observadores de eventos (Event Listeners)
│   ├── install.xml         # Definição do schema do banco de dados (XMLDB)
│   ├── services.php        # Definição de Web Services externos
│   ├── tasks.php           # Definição de tarefas agendadas (Cron)
│   └── upgrade.php         # Scripts de atualização de banco de dados
├── lang/
│   └── en/
│       └── local_myplugin.php # Textos internacionalizados do plugin
├── templates/              # Arquivos de visualização (Mustache .mustache)
├── version.php             # Arquivo obrigatório de metadados e versão
├── lib.php                 # Callbacks legados do core e funções globais
└── view.php                # Página principal exposta ao usuário
```

### 3. O Arquivo `version.php` Obrigatório
Todo plugin precisa definir seus metadados de versão:
```php
<?php
defined('MOODLE_INTERNAL') || die();

$plugin->component = 'local_myplugin'; // Frankenstyle completo
$plugin->version   = 2026081500;       // AAAAMMDDXX (Ano, Mês, Dia, Revisão)
$plugin->requires  = 2022111800;       // Versão mínima exigida do Moodle core
$plugin->maturity  = MATURITY_STABLE;  // Nível de maturidade (STABLE, BETA, etc.)
$plugin->release   = '1.0.0';
```

---

## 💾 Persistência de Dados (DML & DDL)

### 1. DDL (Definição de Estrutura) - `db/install.xml`
O Moodle utiliza uma abstração XML para definir tabelas de banco de dados, independente do SGBD utilizado (PostgreSQL, MySQL, MariaDB, MSSQL).
*   **Regra**: Use o gerador embutido no Moodle (Administração do Site -> Desenvolvimento -> Editor XMLDB) para criar e alterar arquivos `install.xml`.
*   **Padrão de Tabelas**: O nome da tabela deve iniciar com o nome Frankenstyle do plugin sem `_` (ex: `local_myplugin` cria a tabela `mdl_local_myplugin_log`).

### 2. DML (Manipulação de Dados) - O Objeto Global `$DB`
Nunca execute queries SQL cruas ou concatene variáveis diretamente para evitar SQL Injection. Utilize sempre os placeholders seguros (`:nomeparam` ou `?`).

```php
global $DB;

// 1. Busca de registro único
$user = $DB->get_record('user', ['id' => $userid, 'deleted' => 0], '*', MUST_EXIST);

// 2. Busca complexa com SQL parametrizado (Use placeholders nomeados)
$sql = "SELECT * FROM {user} WHERE email LIKE :email AND deleted = :deleted";
$params = ['email' => '%@example.com', 'deleted' => 0];
$users = $DB->get_records_sql($sql, $params);

// 3. Inserção segura
$record = new stdClass();
$record->name = 'Nova Categoria';
$record->timecreated = time();
$newid = $DB->insert_record('my_plugin_table', $record);

// 4. Atualização
$record->id = $newid;
$record->name = 'Categoria Atualizada';
$DB->update_record('my_plugin_table', $record);

// 5. Exclusão
$DB->delete_records('my_plugin_table', ['id' => $newid]);
```

---

## 🔒 Segurança, Controle de Acesso e Sanitização

### 1. Higienização de Inputs (`required_param` e `optional_param`)
Nunca leia superglobais do PHP (`$_GET`, `$_POST`, `$_REQUEST`). Use as funções nativas de sanitização do Moodle:
```php
// Parâmetro Obrigatório (se ausente, para a execução com erro)
$courseid = required_param('id', PARAM_INT);

// Parâmetro Opcional (com valor padrão)
$search = optional_param('search', '', PARAM_TEXT);
$page = optional_param('page', 0, PARAM_INT);
```
*Tipos de parâmetros comuns*: `PARAM_INT`, `PARAM_ALPHAEXT`, `PARAM_ALPHANUM`, `PARAM_TEXT`, `PARAM_RAW` (use com extrema cautela), `PARAM_BOOL`.

### 2. Fluxo Obrigatório de Autenticação e Autorização
Todo script de entrada de usuário (`view.php`, `index.php`) deve seguir a seguinte ordem de validação de segurança:
```php
require_once(__DIR__ . '/../../config.php'); // Inicializa o core do Moodle

// 1. Sanitiza os parâmetros de entrada
$courseid = required_param('courseid', PARAM_INT);

// 2. Define o Contexto da Página
$context = context_course::instance($courseid);

// 3. Garante que o usuário está logado e tem acesso ao curso
require_login($courseid);

// 4. Valida Capabilities (Permissões Específicas)
require_capability('local_myplugin:viewreport', $context);

// 5. Configura o Objeto de Visualização de Página ($PAGE)
$PAGE->set_url(new moodle_url('/local/myplugin/view.php', ['courseid' => $courseid]));
$PAGE->set_context($context);
$PAGE->set_title(get_string('pluginname', 'local_myplugin'));
$PAGE->set_heading($courseid ? format_string($course->fullname) : 'My Report');

// 6. Inicia a renderização
echo $OUTPUT->header();
```

---

## 🔌 APIs Avançadas do Moodle

### 1. Forms API (Criação de Formulários Seguros)
Os formulários devem estender a classe `moodleform` e possuir tokens CSRF gerados automaticamente pelo Moodle.

**Definição do Formulário (`classes/form/edit_form.php`):**
```php
namespace local_myplugin\form;

defined('MOODLE_INTERNAL') || die();
require_once($CFG->libdir . '/formslib.php');

class edit_form extends \moodleform {
    protected function definition() {
        $mform = $this->_form;

        // Adiciona campo de texto simples
        $mform->addElement('text', 'name', get_string('name', 'local_myplugin'));
        $mform->setType('name', PARAM_TEXT);
        $mform->addRule('name', get_string('required'), 'required', null, 'client');

        // Adiciona botões de Ação (Submit/Cancel)
        $this->add_action_buttons();
    }
}
```

**Uso no Controlador (`view.php`):**
```php
$mform = new \local_myplugin\form\edit_form();

if ($mform->is_cancelled()) {
    // Redireciona se o usuário cancelar
    redirect(new moodle_url('/course/view.php', ['id' => $courseid]));
} else if ($data = $mform->get_data()) {
    // Processa os dados validados com sucesso
    $DB->insert_record('local_myplugin_items', $data);
    redirect(new moodle_url('/local/myplugin/view.php', ['courseid' => $courseid]));
}

// Renderiza o formulário
$mform->display();
```

### 2. Web Services Externos (`db/services.php`)
Permite expor endpoints de API para sistemas externos ou integrações.
*   Defina as funções no arquivo `db/services.php`.
*   Crie a classe correspondente em `classes/external/my_function.php` herdando de `external_api`.
*   Sempre valide parâmetros de entrada e saída com `external_value` e `external_single_structure`.

### 3. Sistema de Hooks (Moodle 4.x+)
Moodle introduziu um padrão moderno de gerenciamento de dependências e Hooks baseados no padrão PSR-14.
*   **Uso**: Prefira registrar e escutar Hooks do core (como interações em fluxos de cadastro de usuários ou conclusão de atividades) em vez de usar callbacks legados em `lib.php` sempre que desenvolver para Moodle 4.x.

### 4. API de Privacidade (GDPR & LGPD)
Todo plugin que armazene dados de usuários (PII) **deve** implementar a API de Privacidade definindo uma classe `provider` em `classes/privacy/provider.php` estendendo as interfaces correspondentes (ex: `\core_privacy\local\metadata\provider`, `\core_privacy\local\request\plugin\provider`).
Isso garante que:
*   Os dados do usuário no plugin sejam exportados quando o usuário solicitar exportação de dados pessoais.
*   Os dados do usuário no plugin sejam devidamente apagados ou anonimizados na exclusão da conta.

---

## 🎨 Interface Visual e Templates (Mustache)
*   **Mustache**: Todo HTML deve ser escrito em arquivos `.mustache` dentro da pasta `templates/` e renderizado via renderers de página, evitando a escrita de HTML hardcoded no PHP.
*   **Javascript**: Use módulos Javascript ES6 modernos na pasta `amd/src/` compilados para garantir carregamento assíncrono seguro via RequireJS no Moodle.

---

## 🔒 Diretrizes de Segurança e Conformidade
*   **OWASP Top 10**: Evite XSS sanitizando todas as saídas com funções adequadas como `format_string()`, `format_text()`, ou escapando strings no Mustache.
*   **Princípio do Menor Privilégio**: Garanta que as capacidades do seu plugin (`db/access.php`) possuam o nível de acesso correto e padrão seguro (evitando dar permissões administrativas por padrão a papéis de estudante).

---

## 🔗 Habilidades Relacionadas
*   **Design & UX**: [program-moodle-design](../moodle-design/SKILL.md) — Customização de temas, Mustache e CSS/SCSS.
*   **Plugins & Ciclo de Vida**: [program-moodle-plugins](../moodle-plugins/SKILL.md) — Anatomia e empacotamento de extensões.
*   **Infraestrutura & Performance**: [program-moodle-infra](../moodle-infra/SKILL.md) — Arquitetura de servidores, MUC e Redis.
*   **Banco de Dados (DBA)**: [program-moodle-dba](../moodle-dba/SKILL.md) — Modelagem XMLDB e performance SQL.
*   **Metodologias & Tecnologia**: [edtech-andragogy](../../domains/edtech-andragogy/SKILL.md) — Andragogia, ADDIE/SAM e padrões SCORM/LTI/xAPI.

