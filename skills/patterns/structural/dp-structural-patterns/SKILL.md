---
name: dp-structural-patterns
description: "Especialista em Padrões de Projeto Estruturais (GoF Structural Patterns) baseado em Design Patterns (Gang of Four) e Refactoring to Patterns. Cobre Adapter, Bridge, Composite, Decorator, Facade, Flyweight e Proxy, explicando como compor classes e objetos em estruturas maiores e mais flexíveis mantendo o baixo acoplamento."
---

# Padrões de Projeto Estruturais (GoF Structural Patterns)

Os padrões estruturais explicam como compor classes e objetos em estruturas maiores, mantendo essas estruturas flexíveis e eficientes. A composição de objetos oferece muito mais flexibilidade em tempo de execução do que a herança estática de classes.

---

## 🔌 1. Adapter (Adaptador)

### 1.1 Intenção e Motivação
Converte a interface de uma classe em outra interface esperada pelos clientes. Permite que classes com interfaces incompatíveis trabalhem juntas.

```mermaid
classDiagram
    class Client
    class Target {
        <<interface>>
        +request()
    }
    class Adapter {
        -adaptee: Adaptee
        +request()
    }
    class Adaptee {
        +specificRequest()
    }
    Client --> Target
    Target <|.. Adapter
    Adapter o-- Adaptee : traduz chamada
```

---

## 🌉 2. Bridge (Ponte)

### 2.1 Intenção e Motivação
Desacopla uma abstração de sua implementação, permitindo que ambas possam variar independentemente através de hierarquias separadas ligadas por composição.

```mermaid
classDiagram
    class Abstraction {
        -impl: Implementation
        +feature()
    }
    class RefinedAbstraction {
        +feature()
        +advancedFeature()
    }
    class Implementation {
        <<interface>>
        +method1()
        +method2()
    }
    class ConcreteImplA {
        +method1()
        +method2()
    }
    class ConcreteImplB {
        +method1()
        +method2()
    }
    Abstraction <|-- RefinedAbstraction
    Abstraction o-- Implementation : ponte
    Implementation <|.. ConcreteImplA
    Implementation <|.. ConcreteImplB
```

---

## 🌳 3. Composite (Composto)

### 3.1 Intenção e Motivação
Compõe objetos em estruturas de árvore para representar hierarquias do tipo parte-todo. Permite que clientes tratem objetos individuais e composições de objetos de maneira uniforme.

```mermaid
classDiagram
    class Component {
        <<interface>>
        +execute()
    }
    class Leaf {
        +execute()
    }
    class Composite {
        -children: List~Component~
        +add(c: Component)
        +remove(c: Component)
        +execute()
    }
    Component <|.. Leaf
    Component <|.. Composite
    Composite o-- Component : contém
```

---

## 🎀 4. Decorator (Decorador / Wrapper)

### 4.1 Intenção e Motivação
Acopla responsabilidades adicionais a um objeto dinamicamente. Os decoradores fornecem uma alternativa flexível ao uso de subclasses para extensão de funcionalidades.

```mermaid
classDiagram
    class Component {
        <<interface>>
        +operation()
    }
    class ConcreteComponent {
        +operation()
    }
    class BaseDecorator {
        -wrappee: Component
        +operation()
    }
    class ConcreteDecoratorA {
        +operation()
        +addedBehavior()
    }
    Component <|.. ConcreteComponent
    Component <|.. BaseDecorator
    BaseDecorator o-- Component
    BaseDecorator <|-- ConcreteDecoratorA
```

---

## 🏛️ 5. Facade (Fachada)

### 5.1 Intenção e Motivação
Fornece uma interface simplificada e de alto nível para um subsistema complexo composto por múltiplas classes, tornando o subsistema mais fácil de usar e desacoplando clientes de detalhes internos.

```mermaid
classDiagram
    class Client
    class VideoConverterFacade {
        +convertVideo(file, format)
    }
    class AudioMixer
    class BitrateReader
    class CodecFactory
    Client --> VideoConverterFacade
    VideoConverterFacade ..> AudioMixer
    VideoConverterFacade ..> BitrateReader
    VideoConverterFacade ..> CodecFactory
```

---

## 🪶 6. Flyweight (Peso-Mosca)

### 6.1 Intenção e Motivação
Permite ajustar uma enorme quantidade de objetos na memória RAM compartilhando partes comuns de estado (estado intrínseco) entre múltiplos objetos em vez de manter todos os dados em cada instância (estado extrínseco).

```mermaid
classDiagram
    class FlyweightFactory {
        -flyweights: Map
        +getFlyweight(key) Flyweight
    }
    class TreeType {
        -name
        -color
        -texture
        +draw(canvas, x, y)
    }
    class Tree {
        -x
        -y
        -type: TreeType
        +draw(canvas)
    }
    FlyweightFactory o-- TreeType
    Tree o-- TreeType : compartilha estado intrínseco
```

---

## 🛡️ 7. Proxy (Procurador)

### 7.1 Intenção e Motivação
Fornece um substituto ou espaço reservado para outro objeto para controlar o acesso a ele. Tipos comuns: Proxy Remoto, Proxy Virtual (Lazy Loading), Proxy de Proteção (Controle de Acesso) e Proxy de Cache/Log.

```mermaid
classDiagram
    class ServiceInterface {
        <<interface>>
        +operation()
    }
    class RealService {
        +operation()
    }
    class Proxy {
        -realService: RealService
        +operation()
    }
    ServiceInterface <|.. RealService
    ServiceInterface <|.. Proxy
    Proxy o-- RealService : controla acesso
```

---

## ⚖️ Matriz Comparativa dos Padrões Estruturais

| Padrão | Problema Resolvido | Estratégia Estrutural |
| :--- | :--- | :--- |
| **Adapter** | Interfaces incompatíveis entre sistemas legados/terceiros | Encapsula um objeto existente traduzindo chamadas |
| **Bridge** | Explosão combinatória de subclasses em 2 dimensões ortogonais | Separa Abstração e Implementação via referência |
| **Composite** | Manipulação recursiva de estruturas hierárquicas (árvores) | Trata folhas e nós compostos com a mesma interface |
| **Decorator** | Adição dinâmica de responsabilidades sem herança | Envolve o objeto real delegando e adicionando comportamento |
| **Facade** | Complexidade de inicialização/orquestração de subsistemas | Ponto de entrada simplificado para múltiplos componentes |
| **Flyweight** | Alto consumo de memória com milhões de objetos semelhantes | Separa estado intrínseco (compartilhado) de extrínseco |
| **Proxy** | Acesso direto a objeto pesado, remoto ou protegido | Intercepta requisições aplicando lazy load, auth ou cache |
