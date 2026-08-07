---
name: "lang-c"
description: "Fornece padrões de engenharia de software em C moderno baseados na norma internacional ISO/IEC 9899 (com foco em C23 - ISO/IEC 9899:2024, C17, C11 e C99), cobrindo novas palavras-chave (nullptr, bool, constexpr), atributos ([[nodiscard]], [[deprecated]]), matemática segura (<stdckdint.h>), operações binárias (<stdbit.h>), depuração de memória e CMake."
---

# Habilidade de IA: Engenharia de C Moderno (ISO/IEC 9899 Specialist)

Esta skill orienta a inteligência artificial a atuar como especialista na linguagem **C moderno**, baseando-se estritamente na norma internacional oficial **ISO/IEC 9899** (publicada pelo ISO JTC1/SC22/WG14 em [iso-9899.info](https://www.iso-9899.info/wiki/The_Standard)). O foco principal é a versão mais recente **C23 (ISO/IEC 9899:2024)**, mantendo suporte às revisões C17, C11 e C99 para a construção de sistemas de baixo nível de alta performance, seguros e isentos de Comportamentos Indefinidos (*Undefined Behavior - UB*).

---

## 🧭 Evolução dos Padrões ISO/IEC 9899

Ao desenvolver em C, alinhe os recursos da linguagem com a revisão apropriada do padrão:

### 1. ISO/IEC 9899:2024 (C23 - Padrão Mais Recente)
- **Novas Palavras-Chave Nativas**:
  - `nullptr`: Substitui `NULL` (ponteiro nulo com tipo próprio `nullptr_t` prevenindo ambiguidades com números).
  - `bool`, `true`, `false`: Tornam-se palavras-chave nativas sem necessidade de `<stdbool.h>`.
  - `static_assert`, `alignas`, `alignof`, `thread_local`: Palavras-chave simplificadas (sem o prefixo `_` do C11).
  - `constexpr`: Avaliação de constantes imutáveis em tempo de compilação.
  - `auto`: Inferência de tipos de variáveis em tempo de compilação.
  - `typeof` e `typeof_unqual`: Operadores de inspeção de tipos.
- **Atributos Padronizados (`[[attribute]]`)**:
  - Sintaxe unificada para metadados: `[[nodiscard]]`, `[[maybe_unused]]`, `[[deprecated]]`, `[[likely]]`, `[[unlikely]]`, `[[fallthrough]]`, `[[noreturn]]`.
- **Novas Bibliotecas e Funções de Segurança**:
  - `<stdckdint.h>`: Operações aritméticas com detecção de estouro (*checked integer arithmetic*): `ckd_add`, `ckd_sub`, `ckd_mul`.
  - `<stdbit.h>`: Manipulação de bits padronizada: `stdc_count_ones`, `stdc_leading_zeros`, `stdc_has_single_bit`.
  - `memset_explicit`: Limpeza segura de dados confidenciais na memória que previne otimizações de eliminação do compilador.
  - `memalignment`: Verificação de alinhamento de ponteiros.
  - `strdup` e `strndup`: Duplicação dinâmica de strings padronizada na libc.
- **Melhorias de Sintaxe e Pré-processador**:
  - Diretiva `#embed`: Inclusão direta de arquivos binários em arrays no tempo de compilação.
  - Diretivas `#elifdef` e `#elifndef`, macros `__has_include` e `__VA_OPT__`.
  - Formato de inteiros binários `%b` e `%B` em `printf`/`scanf` e literais `0b1010`.
  - Inicialização estática de structs com chaves vazias: `struct Point p = {};`.

### 2. ISO/IEC 9899:2018 (C17) & 9899:2011 (C11)
- **C11**: Suporte nativo a threads (`<threads.h>`), operações atômicas (`<stdatomic.h>`), seletores genéricos (`_Generic`), structs/unions anônimas e exclusão da função insegura `gets()`.
- **C17**: Revisão de correção de defeitos técnicos (TCs) sem introdução de novas sintaxes.

### 3. ISO/IEC 9899:1999 (C99)
- Comentários de linha `//`, inicializadores nomeados (`.field = val`), literais compostos, `inline`, qualificador `restrict`, suporte a VLA (evitar em código seguro) e inteiros de largura fixa em `<stdint.h>`.

---

## 🛠️ Diretrizes de Engenharia e Prevenção de Defeitos

### 1. Prevenção Estrita de Comportamento Indefinido (Undefined Behavior - UB)
- **Gestão de Memória Segura**:
  - Sempre zere ou inicialize memória alocada dinamicamente (`malloc`/`calloc`).
  - Atribua `NULL` ou `nullptr` a ponteiros imediatamente após liberá-los com `free()`.
  - Em alocações contendo dados de senhas ou chaves, utilize `memset_explicit()` antes do `free()`.
- **Estouro de Inteiros**: Evite estouro de inteiros sinalizados utilizando as funções checked de `<stdckdint.h>` (C23) ou verificações prévias de limites.
- **Evitar VLAs (Variable Length Arrays)**: Prefira alocação dinâmica em heap ou tamanhos fixos para evitar estouro de pilha (*stack overflow*).

### 2. Análise Estática e Sanitizers
- Compilação com avisos estritos ativados: `-Wall -Wextra -Wpedantic -Wconversion -Wshadow -std=c23`.
- Execução com Sanitizers durante os testes: `-fsanitize=address,undefined,leak`.

---

## 🧰 Padrões de Código C23 Recomendados

### 1. Aritmética Inteira Segura e Atributos (`<stdckdint.h>` & C23)
```c
#include <stdio.h>
#include <stdckdint.h>

[[nodiscard]] bool safe_multiply_and_add(int a, int b, int c, int *result) {
    int temp = 0;
    
    // Multiplicação com checagem de estouro em C23
    if (ckd_mul(&temp, a, b)) {
        return false; // Estouro detectado
    }
    
    // Adição com checagem de estouro em C23
    if (ckd_add(result, temp, c)) {
        return false; // Estouro detectado
    }
    
    return true;
}

int main(void) {
    int val = 0;
    if (safe_multiply_and_add(100000, 200000, 50, &val)) {
        printf("[+] Resultado seguro: %d\n", val);
    } else {
        printf("[-] Erro: Estouro de inteiro prevenido!\n");
    }
    return 0;
}
```

### 2. Uso do `nullptr`, Atributos e Limpeza Segura de Memória (`memset_explicit`)
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char username[32];
    char password_hash[64];
} [[deprecated("Use UserAccountSecure no C23")]] LegacyUser;

typedef struct {
    char username[32];
    char secret_token[64];
} UserAccountSecure;

void wipe_sensitive_data(UserAccountSecure *account) {
    if (account == nullptr) {
        return;
    }
    
    // memset_explicit garante que o compilador não otimizará a exclusão
    memset_explicit(account->secret_token, 0, sizeof(account->secret_token));
}

int main(void) {
    // Inicialização vazia C23
    UserAccountSecure user = {};
    snprintf(user.username, sizeof(user.username), "alice");
    snprintf(user.secret_token, sizeof(user.secret_token), "secret_12345");

    printf("[+] Usuário ativado: %s\n", user.username);

    wipe_sensitive_data(&user);
    return 0;
}
```

---

## ⚙️ Configuração de Build System Moderno (CMakeLists.txt C23)

```cmake
cmake_minimum_required(VERSION 3.25)
project(c23_modern_project C)

# Define o padrão C23 (ISO/IEC 9899:2024)
set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

add_executable(app_main src/main.c)

# Bateria estrita de avisos do compilador
if (MSVC)
    target_compile_options(app_main PRIVATE /W4 /WX)
else()
    target_compile_options(app_main PRIVATE -Wall -Wextra -Wpedantic -Wconversion -Wshadow -Werror)
endif()
```

---

## 🔗 Integração com Outras Skills

- Para compilar componentes em C++23 e interoperabilidade com C, consulte [lang-cpp](../lang-cpp/SKILL.md).
- Para realizar testes unitários seguros de funções em C utilizando o framework Criterion, consulte [framework-criterion](../../framework/framework-criterion/SKILL.md).
- Para auditoria de vulnerabilidades de estouro de buffer, format strings e ponteiros em código C, consulte [sast-code-review](../../security/appsec/sast-code-review/SKILL.md) e [appsec-owasp-asvs](../../security/appsec/appsec-owasp-asvs/SKILL.md).
