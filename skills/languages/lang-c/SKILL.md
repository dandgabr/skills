---
name: "lang-c"
description: "Fornece padrões de engenharia de software em C moderno (C23, C17, C11). Cobre gestão segura de memória, prevenção de comportamentos indefinidos (UB), concorrência POSIX/C11, metaprogramação com preprocessador, macros genéricas (_Generic), compilação modular com CMake/Meson e integração com sanitizers e análise estática."
---

# Habilidade de IA: Engenharia de C (C Specialist)

Esta skill orienta a inteligência artificial a atuar como especialista na linguagem **C moderno**, com foco em **C23 (ISO/IEC 9899:2024)**, **C17** e **C11**. O objetivo é orientar a construção de sistemas de alta performance, firmware, software embarcado e componentes de baixo nível com máxima segurança de memória, ausência de comportamentos indefinidos (Undefined Behavior - UB), código limpo e integração com ferramentas modernas de compilação, análise estática e teste.

---

## 🧭 Diretrizes de Desenvolvimento em C Moderno

Ao atuar nesta skill, aplique rigorosamente os seguintes padrões de engenharia:

### 1. Padrões Modernos e Recursos de Linguagem (C23 & C11)
- **Adoção do C23**:
  - Use as novas palavras-chave nativas: `nullptr` (substituindo `NULL` para ponteiros tipados), `bool`, `true`, `false`, `static_assert`, `alignas`, `alignof` e `thread_local`.
  - Utilize inferência de tipo com `auto` para variáveis inicializadas quando isso aumentar a legibilidade e a manutenibilidade do código.
  - Empregue a nova diretiva de pré-processador `#embed` para inclusão direta de recursos binários sem depender de ferramentas de geração externas (`objcopy` ou `xxd`).
  - Aplique os atributos padronizados do C23: `[[nodiscard]]`, `[[maybe_unused]]`, `[[deprecated]]`, `[[fallthrough]]`, `[[unsequenced]]` e `[[reproducible]]`.
  - Utilize inicializadores vazios `{}` para zerar estruturas e arrays de forma limpa e inequívoca.
  - Utilize `stdckdint.h` (`ckd_add`, `ckd_sub`, `ckd_mul`) para aritmética com checagem de overflow integrada e `stdbit.h` para manipulação de bits portável.
  - Utilize `typeof` e `typeof_unqual` para metaprogramação com tipos em macros sem perda de qualificadores.
- **Seleção Genérica com `_Generic` (C11/C23)**:
  - Implemente sobrecarga de funções segura por tipo em tempo de compilação usando a construção `_Generic`, evitando `void*` desnecessários.
- **Uso Seguro de Arrays**:
  - Evite Arrays de Tamanho Variável (VLAs - Variable Length Arrays) na pilha devido a riscos de estouro de pilha (*stack overflow*) e vulnerabilidades de segurança. Prefira alocação dinâmica explícita na heap ou buffers de tamanho fixo com limites validados.

### 2. Gerenciamento de Memória e Segurança
- **Prevenção de Undefined Behavior (UB)**:
  - Inicialize sempre todas as variáveis antes da primeira leitura.
  - Valide obrigatoriamente ponteiros contra `nullptr` antes de qualquer desreferenciação.
  - Evite *dangling pointers* definindo ponteiros liberados como `nullptr` após a chamada de `free()`.
  - Garanta que operações aritméticas não causem *integer overflow* utilizando as funções de `stdckdint.h` ou verificações explícitas.
  - Respeite as regras de aliasing utilizando a palavra-chave `restrict` apenas em ponteiros garantidamente não sobrepostos.
- **Substituição de Funções Inseguras**:
  - Proíba o uso de `gets()`, `strcpy()`, `strcat()`, `sprintf()` e `scanf()` sem especificação de tamanho.
  - Use `snprintf()`, `memcpy()` / `memmove()` com verificação rigorosa do tamanho de buffer remanescente.
- **Padrão de Liberação de Recursos (RAII / Cleanup Determinístico)**:
  - Adote o padrão de tratamento de erros com `goto cleanup` para garantir a liberação sequencial e determinística de múltiplos recursos alocados em caso de falha.
  - Em compiladores como GCC e Clang que oferecem suporte, considere o uso de `__attribute__((cleanup(func)))` para simular escopo RAII quando autorizado pelas regras do projeto.
- **Análise Estática e Sanitizers**:
  - Compile sempre com detecção de vazamentos e erros de memória ativados: AddressSanitizer (`-fsanitize=address`), UndefinedBehaviorSanitizer (`-fsanitize=undefined`) e ThreadSanitizer (`-fsanitize=thread`).
  - Submeta o código a linters e analisadores estáticos: **Clang-Tidy**, **Cppcheck**, **Flawfinder** e **Valgrind**.

### 3. Estrutura de Projeto, Compilação e Build
- **Modern CMake (3.20+)**:
  - Estruture o projeto utilizando apenas alvos (*target-based CMake*): `add_library()`, `add_executable()`, `target_include_directories()`, `target_compile_options()` e `target_link_libraries()`.
  - Defina o padrão C23 explicitamente: `set(CMAKE_C_STANDARD 23)` e `set(CMAKE_C_STANDARD_REQUIRED ON)`.
- **Flags de Compilador Estritas**:
  - **GCC/Clang**: `-Wall -Wextra -Wpedantic -Wconversion -Wshadow -Wdouble-promotion -Wformat=2 -Wimplicit-fallthrough -Werror`
  - **MSVC**: `/W4 /WX /sdl`
- **Encapsulamento e Tipos Opacos**:
  - Oculte detalhes de implementação de estruturas de dados expondo apenas ponteiros opacos (*Opaque Pointers*) no arquivo de cabeçalho (`.h`), mantendo a definição do `struct` restrita ao arquivo de implementação (`.c`).
  - Utilize `#pragma once` ou *header guards* rigorosos (`#ifndef HEADER_NAME_H ... #endif`).

### 4. Testabilidade e Qualidade
- **Frameworks de Testes Unitários**:
  - Utilize **Unity**, **CMocka**, **Criterion** ou **CTest** para criar suites de testes automatizados e isolados.
- **Assertivas**:
  - Use `static_assert` (C23/C11) no nível de compilação para verificar tamanhos de tipos e alinhamentos de memória.
  - Use `assert()` de `<assert.h>` para invariantes de pré-condição e pós-condição em builds de desenvolvimento.

---

## 🧰 Padrões de Código Recomendados

### 1. Padrão `goto cleanup` para Gerenciamento Limpo de Recursos

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    char *buffer;
    FILE *file;
} ResourceContext;

[[nodiscard]] bool process_file_data(const char *filepath) {
    if (filepath == nullptr) {
        return false;
    }

    ResourceContext ctx = { .buffer = nullptr, .file = nullptr };
    bool success = false;

    ctx.file = fopen(filepath, "rb");
    if (ctx.file == nullptr) {
        perror("Failed to open file");
        goto cleanup;
    }

    ctx.buffer = (char *)malloc(1024);
    if (ctx.buffer == nullptr) {
        fprintf(stderr, "Allocation failed\n");
        goto cleanup;
    }

    // Processamento do arquivo...
    size_t read_bytes = fread(ctx.buffer, 1, 1024, ctx.file);
    if (read_bytes == 0 && ferror(ctx.file)) {
        goto cleanup;
    }

    success = true;

cleanup:
    if (ctx.buffer != nullptr) {
        free(ctx.buffer);
        ctx.buffer = nullptr;
    }
    if (ctx.file != nullptr) {
        fclose(ctx.file);
        ctx.file = nullptr;
    }
    return success;
}
```

### 2. Tipo Opaco (Encapsulamento de Estrutura em C23)

**`buffer.h`** (Interface Pública):
```c
#pragma once

#include <stddef.h>
#include <stdbool.h>

// Ponteiro opaco para ocultar o layout da estrutura interna
typedef struct ByteBuffer ByteBuffer;

[[nodiscard]] ByteBuffer *byte_buffer_create(size_t initial_capacity);
void byte_buffer_destroy(ByteBuffer *buf);
[[nodiscard]] bool byte_buffer_append(ByteBuffer *buf, const unsigned char *data, size_t len);
[[nodiscard]] size_t byte_buffer_get_length(const ByteBuffer *buf);
```

**`buffer.c`** (Implementação Privada):
```c
#include "buffer.h"
#include <stdlib.h>
#include <string.h>

struct ByteBuffer {
    unsigned char *data;
    size_t length;
    size_t capacity;
};

ByteBuffer *byte_buffer_create(size_t initial_capacity) {
    if (initial_capacity == 0) {
        initial_capacity = 64;
    }

    ByteBuffer *buf = (ByteBuffer *)malloc(sizeof(ByteBuffer));
    if (buf == nullptr) {
        return nullptr;
    }

    buf->data = (unsigned char *)malloc(initial_capacity);
    if (buf->data == nullptr) {
        free(buf);
        return nullptr;
    }

    buf->length = 0;
    buf->capacity = initial_capacity;
    return buf;
}

void byte_buffer_destroy(ByteBuffer *buf) {
    if (buf == nullptr) {
        return;
    }
    free(buf->data);
    buf->data = nullptr;
    free(buf);
}

bool byte_buffer_append(ByteBuffer *buf, const unsigned char *data, size_t len) {
    if (buf == nullptr || data == nullptr || len == 0) {
        return false;
    }

    if (buf->length + len > buf->capacity) {
        size_t new_cap = buf->capacity * 2 + len;
        unsigned char *new_data = (unsigned char *)realloc(buf->data, new_cap);
        if (new_data == nullptr) {
            return false;
        }
        buf->data = new_data;
        buf->capacity = new_cap;
    }

    memcpy(buf->data + buf->length, data, len);
    buf->length += len;
    return true;
}

size_t byte_buffer_get_length(const ByteBuffer *buf) {
    return (buf != nullptr) ? buf->length : 0;
}
```

### 3. Aritmética Checada C23 (`stdckdint.h`) e Atributos de Função

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdckdint.h>

[[nodiscard]] bool calculate_total_allocation(size_t count, size_t element_size, size_t *out_total) {
    if (out_total == nullptr) {
        return false;
    }

    // Previne de forma portável integer overflow na multiplicação
    if (ckd_mul(out_total, count, element_size)) {
        fprintf(stderr, "Error: Integer overflow detected in allocation calculation.\n");
        return false;
    }

    return true;
}
```

### 4. Overload Tipo-Seguro com `_Generic` e `typeof`

```c
#include <stdio.h>
#include <math.h>

static inline void print_int(int val) {
    printf("Integer: %d\n", val);
}

static inline void print_double(double val) {
    printf("Double: %f\n", val);
}

static inline void print_string(const char *val) {
    printf("String: %s\n", val);
}

#define print_val(X) _Generic((X), \
    int: print_int, \
    double: print_double, \
    const char*: print_string, \
    char*: print_string \
)(X)
```

---

## 🔗 Integração com Outras Skills

- [clean-code-reusability](..\..\general\engineering-practices\clean-code-reusability/SKILL.md): Garante eliminação de código duplicado, modularização de bibliotecas C e aplicação de boas práticas de documentação Doxygen.
- [backend-developer](..\..\general\roles\backend-developer/SKILL.md): Orienta a construção de drivers de rede, proxies, serviços IPC e integrações nativas de alto desempenho.
- [devsecops-engineer](..\..\security\ops-architecture\devsecops-engineer/SKILL.md): Orienta a integração de sanitizers (ASan/UBSan), verificação estática no pipeline CI/CD e compilação hardening.
- [appsec-owasp-asvs](..\..\security\appsec\appsec-owasp-asvs/SKILL.md): Fornece requisitos de segurança contra estouros de pilha/heap, acesso de memória inválido e vulnerabilidades de formato de string.
- [software-architect](..\..\general\roles\software-architect/SKILL.md): Apoia no desenho de arquiteturas modulares de baixo nível, APIs orientadas a componentes e abstrações de hardware.

---

## ⚙️ Regras de Decisão

- **Segurança sobre Micro-otimização**: Nunca comprometa a segurança de memória em prol de otimizações de performance prematuras.
- **Zero Warnings**: Todo código C deve compilar sem nenhum aviso (*warning*) sob a flag `-Werror` nas principais ferramentas de build.
- **Validação Estrita de Limites**: Exija validação prévia em todas as operações de cópia de memória ou ponteiros passados por APIs públicas.
