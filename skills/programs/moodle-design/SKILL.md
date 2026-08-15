---
name: "program-moodle-design"
description: "Atua como especialista em design de interfaces (UI), desenvolvimento de temas, templates Mustache, estilização SCSS, customização de formatos de curso e otimização de UX/acessibilidade no Moodle LMS."
---

# 🎨 Designer e Desenvolvedor Frontend Moodle (program-moodle-design)

Esta skill fornece diretrizes técnicas, padrões de arquitetura visual e boas práticas de User Experience (UX) e User Interface (UI) para o desenvolvimento de temas e customização frontend no Moodle LMS. Deve ser ativada sempre que o desenvolvedor precisar criar ou modificar temas, estilizar elementos com SCSS, sobrescrever layouts usando Mustache, alterar formatos de curso ou realizar melhorias de acessibilidade.

---

## 🎯 Objetivo da Skill
Garantir que as customizações visuais e de fluxo de usuário no Moodle sejam implementadas de forma limpa, sustentável e acessível, respeitando as boas práticas de herança do tema padrão (**Boost**), evitando modificações no core do sistema e seguindo os padrões WCAG de acessibilidade.

---

## 🛠️ Desenvolvimento de Temas no Moodle

### 1. A Regra de Ouro: Herança do Tema Boost
Nunca crie um tema do zero. Todos os temas modernos do Moodle devem ser "filhos" do tema **Boost** (baseado em Bootstrap), herdando sua estrutura responsiva e garantias de acessibilidade.
*   **Benefício**: O tema filho recebe automaticamente todas as correções e atualizações de layout do core do Moodle.
*   **Definição no `config.php` do Tema (`theme/mytheme/config.php`)**:
```php
<?php
defined('MOODLE_INTERNAL') || die();

$THEME->name = 'mytheme';
$THEME->sheets = []; // Não use arquivos CSS brutos; prefira SCSS
$THEME->parents = ['boost']; // Herança do Boost
$THEME->enable_dock = false;
$THEME->yuicssmodules = [];
$THEME->rendererfactory = 'theme_overridden_renderer_factory';
```

---

## 🎨 Estilização Moderna com SCSS

O Moodle possui um compilador SCSS integrado que processa os arquivos de estilo automaticamente. 

### 1. Estrutura de Arquivos SCSS
*   `theme/mytheme/scss/pre.scss`: Executado antes do Bootstrap. Ideal para definir variáveis do Bootstrap (ex: cores de marca, fontes).
*   `theme/mytheme/scss/post.scss`: Executado após o Bootstrap. Ideal para regras de estilo customizadas que sobrescrevem o padrão do Moodle.

### 2. Sobrescrevendo Variáveis de Cores (em `pre.scss`)
```scss
// Altera as cores da identidade visual do site
$primary: #1a5c87;
$secondary: #6c757d;
$success: #28a745;
$body-bg: #f8f9fa;
$font-family-sans-serif: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

---

## 🧩 Templates Mustache (Estrutura e Layout)

O Moodle utiliza **Mustache** para separar a lógica em PHP do código HTML.

### 1. Sobrescrevendo Templates (Template Overrides)
Se você precisa alterar o HTML de um componente de atividade, bloco ou rodapé:
1.  Localize o template original do core ou do plugin (ex: `mod/forum/templates/forum_discussion.mustache`).
2.  Copie o arquivo para a pasta de templates do seu tema respeitando a estrutura do componente: `theme/mytheme/templates/mod_forum/forum_discussion.mustache`.
3.  Modifique o arquivo Mustache no seu tema. O Moodle passará a carregar o seu arquivo customizado automaticamente.

### 2. Boas Práticas em Mustache
*   **Evite Lógica Complexa**: Templates Mustache devem ser declarativos. Use apenas condicionais simples (`{{#show_button}}...{{/show_button}}`) e loops.
*   **Exemplo de Template (`theme/mytheme/templates/custom_card.mustache`)**:
```html
<div class="card custom-card-style mb-3">
    <div class="card-body">
        <h5 class="card-title">{{title}}</h5>
        <p class="card-text">{{{description}}}</p> <!-- 3 chaves evitam o escape de HTML formatado -->
        {{#url}}
            <a href="{{url}}" class="btn btn-primary">{{buttontext}}</a>
        {{/url}}
    </div>
</div>
```

---

## 🖼️ Renderers (Passagem de Dados para o Template)

Os **Renderers** são classes PHP responsáveis por recolher dados do banco/negócio e enviá-los ao template Mustache para exibição.

### 1. Implementando `templatable` e `export_for_template`
Qualquer classe que forneça dados para um template deve implementar a interface `renderable` e `templatable`:

```php
namespace theme_mytheme\output;

defined('MOODLE_INTERNAL') || die();

class custom_card implements \renderable, \templatable {
    protected $title;
    protected $description;
    protected $url;

    public function __construct($title, $description, $url = null) {
        $this->title = $title;
        $this->description = $description;
        $this->url = $url;
    }

    // Prepara os dados para o Mustache
    public function export_for_template(\renderer_base $output) {
        return [
            'title' => format_string($this->title),
            'description' => format_text($this->description, FORMAT_HTML),
            'url' => $this->url ? $this->url->out() : null,
            'buttontext' => get_string('viewmore', 'theme_mytheme')
        ];
    }
}
```

### 2. Renderizando no PHP
```php
$card = new \theme_mytheme\output\custom_card('Título do Card', 'Descrição do Card', $url);
echo $OUTPUT->render($card);
```

---

## ⚡ Otimização de UX e Acessibilidade (WCAG)

### 1. Evitando o "Scroll of Death" (Rolagem Infinita)
*   **Formatos de Curso**: Prefira criar ou adotar formatos de curso que limitem a visualização a apenas um tópico por página (ex: *One section per page* ou formato *Grid*) em vez de renderizar todas as atividades em uma única página longa.
*   **Colapso de Tópicos**: Utilize componentes Bootstrap (`collapse` / `accordion`) para ocultar e exibir blocos de atividades dinamicamente.

### 2. Hardening de Acessibilidade
*   **Navegação Teclado**: Garanta que todos os elementos clicáveis possuam estados `:focus` altamente visíveis com outlines contrastantes.
*   **Contraste de Texto**: Respeite a taxa mínima de contraste WCAG AA (4.5:1 para texto normal, 3:1 para texto grande).
*   **Tags ARIA**: Use `aria-expanded`, `aria-controls` e `aria-label` para descrever adequadamente elementos dinâmicos para leitores de tela.

---

## 🔧 Workflow de Desenvolvimento Rápido
Durante a edição do design de temas, as alterações de CSS/SCSS e HTML (Mustache) são cacheadas agressivamente pelo Moodle.
*   **Modo de Desenvolvedor**: Ative temporariamente o modo de design de temas no arquivo `config.php` para desabilitar o cache de assets:
```php
$CFG->themedesignermode = true;
```
> [!WARNING]
> Nunca mantenha `$CFG->themedesignermode = true;` em servidores de produção, pois isso degrada drasticamente a performance de carregamento de páginas.

---

## 🔗 Habilidades Relacionadas
*   **Moodle Core**: [program-moodle](../moodle/SKILL.md) — APIs do core, controle de acesso e Frankenstyle.
*   **Plugins & Ciclo de Vida**: [program-moodle-plugins](../moodle-plugins/SKILL.md) — Criação de extensões e configurações administrativas.
*   **Metodologias & Tecnologia**: [edtech-andragogy](../../general/domains/edtech-andragogy/SKILL.md) — Design instrucional, Andragogia e experiência do usuário (UX).

