---
name: "program-moodle-plugins"
description: "Atua como especialista no ciclo de vida, anatomia, configurações administrativas (settings.php), rotinas de backup/restauração, testes e publicação de plugins para o Moodle LMS."
---

# ⚙️ Desenvolvimento de Plugins Moodle (program-moodle-plugins)

Esta skill fornece diretrizes avançadas de engenharia de software focadas no ciclo de vida completo de plugins do Moodle LMS, englobando a anatomia interna de diferentes tipos de plugins, configurações globais administrativas, subsistema de backup e restauração (Backup 2.0 API), rotinas de desinstalação segura, testes automatizados e critérios de publicação.

---

## 🎯 Objetivo da Skill
Capacitar o agente a desenvolver plugins resilientes e integrados ao Moodle core, lidando com segurança com dados de instâncias de atividades e blocos, geranciando atualizações de banco de dados (`db/upgrade.php`) e implementando recursos cruciais de backup, restauração e desinstalação limpa.

---

## 🔄 Ciclo de Vida e Atualização de Plugins (`db/upgrade.php`)

Ao atualizar a versão de um plugin no `version.php`, o Moodle executa o arquivo de atualização do banco de dados correspondente para aplicar as migrações sem perda de dados.

### 1. Estrutura do `db/upgrade.php`
```php
function xmldb_local_myplugin_upgrade($oldversion) {
    global $CFG, $DB;

    $dbman = $DB->get_manager(); // Gerenciador de tabelas DDL

    if ($oldversion < 2026081501) {
        // Exemplo: Adicionar uma nova coluna na tabela
        $table = new xmldb_table('local_myplugin_items');
        $field = new xmldb_field('new_column', XMLDB_TYPE_CHAR, '255', null, XMLDB_NOTNULL, null, 'default_value', 'previous_column');

        if (!$dbman->field_exists($table, $field)) {
            $dbman->add_field($table, $field);
        }

        // Salva a versão atual executada com sucesso no banco
        upgrade_plugin_savepoint(true, 2026081501, 'local', 'myplugin');
    }

    return true;
}
```

---

## ⚙️ Configurações Administrativas (`settings.php`)

Se o seu plugin necessita de parâmetros de configuração globais (ex: chaves de API, credenciais, URLs de integração ou comportamentos globais), defina-os em `settings.php` na raiz do plugin.

### 1. Registrando Configurações no Painel de Administração
O arquivo é executado no contexto do menu de administração do site.
```php
<?php
defined('MOODLE_INTERNAL') || die();

if ($hassiteconfig) { // Garante que apenas administradores acessem
    // Cria uma nova página de configuração
    $settings = new admin_settings_page(
        'local_myplugin_settings', 
        get_string('pluginname', 'local_myplugin')
    );

    // Adiciona uma caixa de texto simples
    $settings->add(new admin_setting_configtext(
        'local_myplugin/api_key',
        get_string('apikey', 'local_myplugin'),
        get_string('apikey_desc', 'local_myplugin'),
        '', // Valor padrão
        PARAM_RAW // Sanitização
    ));

    // Adiciona uma caixa de seleção sim/não
    $settings->add(new admin_setting_configcheckbox(
        'local_myplugin/enable_feature',
        get_string('enable_feature', 'local_myplugin'),
        get_string('enable_feature_desc', 'local_myplugin'),
        0 // Valor padrão
    ));

    // Adiciona a página criada à categoria correta do Moodle (localplugins)
    $ADMIN->add('localplugins', $settings);
}
```
*   **Recuperando as Configurações no PHP**:
    ```php
    $apikey = get_config('local_myplugin', 'api_key');
    ```

---

## 💾 Subsistema de Backup e Restauração (Backup 2.0 API)

Para plugins de módulo de atividade (`mod`), bloco (`block`) ou plugins locais que salvam dados atrelados a cursos, é obrigatório implementar o suporte a backup e restauração para que o professor consiga clonar ou exportar cursos sem perder informações do plugin.

A estrutura de arquivos de backup deve ser criada em `backup/moodle2/`:

### 1. Definição da Estrutura de Backup (`backup/moodle2/backup_myplugin_activity_task.class.php`)
```php
class backup_myplugin_activity_task extends backup_activity_task {
    protected function define_my_steps() {
        // Adiciona a etapa de escrita do XML do plugin no pacote de backup
        $this->add_step(new backup_myplugin_activity_structure_step('myplugin_structure', 'myplugin.xml'));
    }
}
```

### 2. Definição do Esquema XML (`backup/moodle2/backup_myplugin_stepslib.php`)
```php
class backup_myplugin_activity_structure_step extends backup_activity_structure_step {
    protected function define_structure() {
        // Define o nó raiz XML do plugin
        $myplugin = new backup_nested_element('myplugin', array('id'), array('name', 'intro', 'timecreated'));
        $items = new backup_nested_element('items', array('id'), array('content', 'userid'));

        // Define a hierarquia dos elementos
        $myplugin->add_child($items);

        // Associa os elementos XML com as tabelas de banco correspondentes
        $myplugin->set_source_table('myplugin_table', array('id' => backup::VAR_ACTIVITYID));
        $items->set_source_table('myplugin_items', array('mypluginid' => backup::VAR_PARENTID));

        return $this->prepare_activity_structure($myplugin);
    }
}
```

---

## 🧹 Processo de Desinstalação Limpa

Ao desinstalar o plugin a partir da administração do site, o Moodle exclui automaticamente as tabelas definidas no `install.xml`. No entanto, se o plugin gera arquivos salvos em disco ou requer limpeza de banco de dados adicional:
*   **Método `lib.php`**: Implemente o callback `xmldb_pluginname_uninstall()` para limpar configurações globais adicionais, excluir caches do plugin, deletar arquivos físicos e remover dados residuais não mapeados diretamente no XMLDB.

---

## 🧪 Testes Automatizados (PHPUnit & Behat)

*   **PHPUnit**: Utilizado para testes de backend/APIs. O Moodle gera um ambiente com banco de dados em memória isolado para os testes.
    - Crie testes em `tests/my_test.php` estendendo a classe `\advanced_testcase`.
    - Inicialize os dados com `$this->resetAfterTest();`.
*   **Behat**: Utilizado para testes de interface de usuário de ponta a ponta (E2E) simulando o comportamento de alunos e professores.

---

## 🔗 Habilidades Relacionadas
*   **Moodle Core**: [program-moodle](../moodle/SKILL.md) — APIs fundamentais do Moodle, DB e Form API.
*   **Design & UX**: [program-moodle-design](../moodle-design/SKILL.md) — Customização visual e templates Mustache.
*   **Infraestrutura & Performance**: [program-moodle-infra](../moodle-infra/SKILL.md) — Dimensionamento e MUC Caching.
*   **Banco de Dados (DBA)**: [program-moodle-dba](../moodle-dba/SKILL.md) — Criação de índices e upgrades XMLDB.

