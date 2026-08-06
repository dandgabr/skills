---
name: "lang-cpp"
description: "Fornece padrões de engenharia de software em C++ moderno (C++23, C++20, C++17). Cobre metaprogramação de templates, conceitos (Concepts), módulos, corrotinas, intervalos (Ranges), gestão de memória via RAII e smart pointers, tratamento de erro tipado (std::expected), compilação com CMake/vcpkg/Conan e testes com Catch2/GTest."
---

# Habilidade de IA: Engenharia de C++ (C++ Specialist)

Esta skill orienta a inteligência artificial a atuar como especialista na linguagem **C++ moderno**, cobrindo principalmente **C++23 (ISO/IEC 14882:2023)** e **C++20**, com visões sobre **C++26**. O objetivo é orientar a construção de sistemas de altíssima performance, engines, sistemas distribuídos, microsserviços e bibliotecas de alto desempenho alinhados aos **C++ Core Guidelines**, promovendo abstrações de custo zero (*zero-overhead abstractions*), gestão determinística de recursos via RAII, type safety estrita, metaprogramação de templates moderna e compilabilidade limpa.

---

## 🧭 Diretrizes de Desenvolvimento em C++ Moderno

Ao atuar nesta skill, aplique rigorosamente os seguintes padrões de engenharia:

### 1. Padrões Modernos e Recursos de Linguagem (C++23 & C++20)
- **Recursos Fundamentais de C++20**:
  - **Concepts & Constraints**: Substitua metaprogramação SFINAE complexa (`std::enable_if_t`) por conceitos nativos (`template<typename T> requires ...` ou `std::integral auto`).
  - **Módulos (`import std;` / `export module`)**: Substitua a inclusão tradicional de cabeçalhos por Módulos C++ sempre que o suporte de toolchain permitir, isolando macros e acelerando dramaticamente a compilação.
  - **Ranges & Views (`std::ranges`, `std::views`)**: Escreva pipelines de transformação de dados declarativos, composíveis e preguiçosos (*lazy evaluation*) sem alocações desnecessárias.
  - **Corrotinas (`co_await`, `co_yield`, `co_return`)**: Utilize corrotinas para geradores sequenciais e programação assíncrona orientada a eventos.
  - **Utilitários Tipados**: Use `std::span` para visões de memória contíguas sem cópia, `std::format` para formatação segura de strings e `std::jthread` / `std::stop_token` para concorrência com encerramento automático RAII.
- **Recursos Avançados de C++23**:
  - **Tratamento de Erros Declarativo (`std::expected<T, E>`)**: Substitua exceções custosas em caminhos de alto fluxo e códigos de erro numéricos por `std::expected` com operações monádicas (`.and_then()`, `.transform()`, `.or_else()`).
  - **E/S Formatada de Alta Performance**: Prefira `std::print` e `std::println` a `<iostream>` ou `printf`.
  - **Parâmetro de Objeto Explícito ("Deduced this")**: Simplifique o padrão CRTP (Curiously Recurring Template Pattern) e elimine duplicações de métodos `const` e `non-const`.
  - **Abstrações Adicionais**: Explore `std::mdspan` para matrizes multidimensionais, `std::generator` para geradores de corrotinas padronizados, e contêineres de memória contígua `std::flat_map` e `std::flat_set`.

### 2. Gerenciamento de Memória, RAII e Tipagem Defensiva
- **RAII (Resource Acquisition Is Initialization) Estrito**:
  - Proíba o uso manual de `new` e `delete`. Gerencie todo o ciclo de vida de memória e recursos (arquivos, sockets, mutexes) através de escopos de objetos.
  - Use `std::unique_ptr` para posse exclusiva e `std::shared_ptr` / `std::weak_ptr` apenas quando a posse for compartilhada de forma indispensável. Prefira `std::make_unique` e `std::make_shared`.
- **Semântica de Movimento (Move Semantics)**:
  - Utilize referências Rvalue (`T&&`), `std::move` para transferência de propriedade de recursos e `std::forward` para repasse perfeito (*perfect forwarding*) em templates.
- **Tipos de Valor em Vez de Ponteiros Nulos**:
  - Substitua o uso de ponteiros brutos opcionais por `std::optional<T>`.
  - Substitua `void*` e `unions` não seguras por `std::variant<Ts...>` e `std::any`.
  - Evite parâmetros de saída por ponteiro/referência (`out parameters`); retorne tuplas, estruturas ou `std::expected`.
- **Constness & Avaliação em Tempo de Compilação**:
  - Declare variáveis, parâmetros e métodos como `const` ou `constexpr` / `consteval` por padrão. Mova computações pesadas ou validações para o tempo de compilação sempre que possível.

### 3. Estrutura de Projeto e Ferramental Moderno
- **Modern CMake (3.25+)**:
  - Utilize CMake orientado a alvos (*target-based CMake*).
  - Configure o padrão C++23:
    ```cmake
    target_compile_features(my_target PRIVATE cxx_std_23)
    set(CMAKE_CXX_STANDARD 23)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    set(CMAKE_CXX_EXTENSIONS OFF)
    ```
- **Gerenciadores de Pacotes**:
  - Utilize **vcpkg** ou **Conan 2.x** para declarar e consumir dependências de forma reprodutiva.
- **Análise Estática e Sanitizers**:
  - Aplique regras do **C++ Core Guidelines** via **Clang-Tidy**.
  - Execute testes automatizados habilitando AddressSanitizer (`-fsanitize=address`), UndefinedBehaviorSanitizer (`-fsanitize=undefined`) e ThreadSanitizer (`-fsanitize=thread`).
- **Flags de Compilador Estritas**:
  - **GCC/Clang**: `-Wall -Wextra -Wpedantic -Wshadow -Wnon-virtual-dtor -Wold-style-cast -Wcast-align -Wunused -Woverloaded-virtual -Wconversion -Wsign-conversion -Wnull-dereference -Wdouble-promotion -Wformat=2 -Werror`
  - **MSVC**: `/W4 /WX /permissive-`

### 4. Testabilidade e Qualidade
- **Frameworks de Testes Modernos**:
  - Adote **Catch2 v3**, **GoogleTest (gtest/gmock)** ou **doctest**.
  - Escreva testes unitários expressivos utilizando BDD (`SCENARIO`, `GIVEN`, `WHEN`, `THEN`) ou fixtures bem encapsuladas.

---

## 🧰 Padrões de Código Recomendados

### 1. Tratamento de Erros Monádico com `std::expected` (C++23)

```cpp
#include <expected>
#include <string>
#include <string_view>
#include <print>

enum class ParseError {
    EmptyInput,
    InvalidCharacter,
    OutOfRange
};

[[nodiscard]] constexpr std::expected<int, ParseError> parse_port(std::string_view str) noexcept {
    if (str.empty()) {
        return std::unexpected(ParseError::EmptyInput);
    }
    
    int port = 0;
    for (char ch : str) {
        if (ch < '0' || ch > '9') {
            return std::unexpected(ParseError::InvalidCharacter);
        }
        port = port * 10 + (ch - '0');
        if (port > 65535) {
            return std::unexpected(ParseError::OutOfRange);
        }
    }
    
    return port;
}

int main() {
    auto result = parse_port("8080")
        .transform([](int port) {
            return std::format("Server listening on port: {}", port);
        })
        .or_else([](ParseError err) -> std::expected<std::string, ParseError> {
            return std::string("Failed to parse configuration port.");
        });

    if (result) {
        std::println("{}", *result);
    }
}
```

### 2. Processamento com C++20 Ranges e Views

```cpp
#include <iostream>
#include <vector>
#include <ranges>
#include <string>
#include <print>

struct Product {
    std::string name;
    double price;
    bool in_stock;
};

int main() {
    const std::vector<Product> catalog = {
        {"Laptop", 1200.0, true},
        {"Mouse", 25.0, true},
        {"Keyboard", 75.0, false},
        {"Monitor", 300.0, true},
        {"USB Cable", 10.0, true}
    };

    // Pipeline de transformação em tempo de execução sem criar vetores intermediários
    auto premium_in_stock_names = catalog
        | std::views::filter([](const Product& p) { return p.in_stock && p.price > 50.0; })
        | std::views::transform([](const Product& p) { return p.name; });

    std::println("Produtos em estoque acima de $50:");
    for (const auto& name : premium_in_stock_names) {
        std::println(" - {}", name);
    }
}
```

### 3. Concepts e Constraints em Tempo de Compilação (C++20)

```cpp
#include <concepts>
#include <iostream>
#include <vector>
#include <print>

// Definição de um conceito customizado
template<typename T>
concept Serializable = requires(T a) {
    { a.serialize() } -> std::same_as<std::string>;
};

class User {
public:
    explicit User(std::string name) : name_(std::move(name)) {}
    
    [[nodiscard]] std::string serialize() const {
        return std::format(R"({{"user": "{}"}})", name_);
    }
private:
    std::string name_;
};

// Função genérica restrita pelo conceito
template<Serializable T>
void send_over_network(const T& payload) {
    std::println("Sending payload: {}", payload.serialize());
}

int main() {
    User user{"Alice"};
    send_over_network(user); // Compila perfeitamente

    // int val = 42;
    // send_over_network(val); // Erro de compilação claro: int não satisfaz Serializable
}
```

### 4. RAII com Smart Pointers e Custom Deleter

```cpp
#include <memory>
#include <cstdio>
#include <print>

struct FileCloser {
    void operator()(FILE* fp) const noexcept {
        if (fp) {
            std::println("Closing file handle via RAII...");
            std::fclose(fp);
        }
    }
};

using UniqueFile = std::unique_ptr<FILE, FileCloser>;

[[nodiscard]] UniqueFile make_unique_file(const char* filename, const char* mode) {
    return UniqueFile(std::fopen(filename, mode));
}

void write_log(const char* message) {
    auto file = make_unique_file("app.log", "a");
    if (!file) {
        std::println(stderr, "Could not open log file");
        return;
    }
    std::fputs(message, file.get());
    // O arquivo é fechado automaticamente ao sair da função
}
```

---

## 🔗 Integração com Outras Skills

- [clean-code-reusability](../../general/clean-code-reusability/SKILL.md): Assegura reutilização de componentes e modelos de design modernos sem duplicação de templates ou classes.
- [backend-developer](../../general/backend-developer/SKILL.md): Orienta o desenvolvimento de micro-serviços C++ gRPC/HTTP de alta throughput e baixa latência.
- [devsecops-engineer](../../security/devsecops-engineer/SKILL.md): Guia o uso de sanitizers, análise de dependências (SCA) e ferramentas de análise estática nos pipelines de CI/CD.
- [appsec-owasp-asvs](../../security/appsec-owasp-asvs/SKILL.md): Garante conformidade contra falhas de segurança de memória, estouro de inteiros e gerenciamento incorreto de ponteiros.
- [software-architect](../../general/software-architect/SKILL.md): Apoia no desenho de arquiteturas de sistemas distribuídos, motores de jogos, compiladores e abstrações DDD de alto desempenho.

---

## ⚙️ Regras de Decisão

- **C++ Core Guidelines**: Siga impreterivelmente os C++ Core Guidelines da comunidade.
- **Zero Raw Ownership**: Nunca utilize ponteiros brutos para representar posse de memória.
- **Preferir Abstrações Nativas**: Use `std::expected`, `std::optional`, `std::variant`, `std::span` e `std::ranges` em vez de construir tipos próprios equivalentes.
