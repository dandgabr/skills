import os
import json

# Definições dos Padrões de Projeto (GoF) baseados no Refactoring.Guru e boas práticas
patterns = {
    # ----------------------------------------------------
    # CRIACIONAIS (Creational)
    # ----------------------------------------------------
    "factory-method": {
        "name": "dp-factory-method",
        "category": "Criacional",
        "description": "Fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.",
        "intent": "Definir uma interface para criar um objeto, mas deixar as subclasses decidirem qual classe instanciar. O Factory Method permite a uma classe adiar a instanciação para subclasses.",
        "problem": "Quando um sistema precisa ser independente de como seus produtos são criados, compostos e representados, e quando a classe criadora não pode antecipar a classe dos objetos que deve criar.",
        "solution": "Substituir chamadas diretas de construção de objetos (usando o operador new) por chamadas a um método fábrica especial. Os objetos ainda são criados via new, mas a partir do método fábrica.",
        "structure": [
            "Produto (Product): Declara a interface comum a todos os objetos que o criador e suas subclasses podem produzir.",
            "Produto Concreto (Concrete Product): Implementações distintas da interface do produto.",
            "Criador (Creator): Declara o método fábrica que retorna novos objetos produto. Pode fornecer uma implementação padrão.",
            "Criadores Concretos (Concrete Creators): Sobrescrevem o método fábrica base para retornar uma instância de um Produto Concreto diferente."
        ],
        "pros": [
            "Evita acoplamento firme entre o criador e os produtos concretos.",
            "Princípio de responsabilidade única: move o código de criação do produto para um único lugar.",
            "Princípio do aberto/fechado: introduz novos tipos de produtos sem quebrar o código cliente existente."
        ],
        "contras": [
            "O código pode se tornar mais complicado, pois exige a criação de novas subclasses para implementar o padrão."
        ],
        "implementation_guidelines": [
            "1. Defina uma interface comum para todos os produtos (Product).",
            "2. Crie um método abstrato ou padrão de fabricação na classe Creator (Creator).",
            "3. Encontre todas as chamadas a construtores diretos e substitua-as por chamadas ao método fábrica.",
            "4. Crie subclasses de Creator para cada tipo de produto concreto e sobrescreva o método fábrica correspondente."
        ]
    },
    "abstract-factory": {
        "name": "dp-abstract-factory",
        "category": "Criacional",
        "description": "Permite produzir famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.",
        "intent": "Fornecer uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.",
        "problem": "Quando seu código precisa funcionar com várias famílias de produtos relacionados, mas você não quer depender das classes concretas desses produtos — eles podem mudar no futuro ou o sistema precisa suportar novas famílias.",
        "solution": "Declarar explicitamente interfaces para cada produto individual que faz parte da família. Em seguida, criar uma interface de fábrica abstrata com métodos de criação para todos os produtos abstratos.",
        "structure": [
            "Produtos Abstratos (Abstract Products): Interfaces para uma família de produtos distintos porém relacionados.",
            "Produtos Concretos (Concrete Products): Implementações dessas interfaces agrupadas por variantes.",
            "Fábrica Abstrata (Abstract Factory): Declara um conjunto de métodos para criação de cada um dos produtos abstratos.",
            "Fábricas Concretas (Concrete Factories): Implementam os métodos de criação da fábrica abstrata para produzir variantes específicas de produtos."
        ],
        "pros": [
            "Garante a compatibilidade entre os produtos criados pela mesma fábrica.",
            "Evita acoplamento forte entre o cliente e os produtos concretos.",
            "Princípio da responsabilidade única e princípio do aberto/fechado."
        ],
        "contras": [
            "O código pode se tornar muito complexo devido à introdução de múltiplas novas interfaces e classes."
        ],
        "implementation_guidelines": [
            "1. Mapeie uma matriz de tipos de produtos versus variantes desses produtos.",
            "2. Declare interfaces abstratas para todos os tipos de produtos.",
            "3. Declare a interface Abstract Factory com um conjunto de métodos de criação para todos os produtos abstratos.",
            "4. Implemente uma classe concreta de fábrica para cada variante de produto.",
            "5. Inicialize a fábrica correspondente na inicialização da aplicação e passe-a para as classes cliente."
        ]
    },
    "builder": {
        "name": "dp-builder",
        "category": "Criacional",
        "description": "Permite construir objetos complexos passo a passo. Permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção.",
        "intent": "Separar a construção de um objeto complexo da sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.",
        "problem": "Classes com construtores gigantescos (telescópicos) contendo dezenas de parâmetros opcionais, ou processos de criação que envolvem várias etapas sequenciais complexas.",
        "solution": "Extrair o código de construção do objeto de sua própria classe e colocá-lo em objetos separados chamados builders. A construção ocorre passo a passo através de métodos encadeados.",
        "structure": [
            "Builder Interface: Declara etapas de construção de objetos comuns a todos os tipos de construtores.",
            "Concrete Builders: Oferecem implementações diferentes das etapas de construção. Produzem produtos que não seguem necessariamente uma interface comum.",
            "Produto (Product): O objeto complexo resultante sendo construído.",
            "Diretor (Director): Define a ordem em que as etapas de construção devem ser chamadas, permitindo criar configurações específicas de produtos de forma reutilizável."
        ],
        "pros": [
            "Permite construir objetos passo a passo, adiar etapas ou executá-las recursivamente.",
            "Reutilização de código de construção para diferentes representações.",
            "Princípio da responsabilidade única: isola a construção complexa da lógica de negócio do produto."
        ],
        "contras": [
            "A complexidade geral do código aumenta, pois o padrão exige a criação de múltiplas novas classes."
        ],
        "implementation_guidelines": [
            "1. Defina claramente as etapas de construção comuns para criar todas as representações do produto.",
            "2. Declare essas etapas na interface do construtor (Builder).",
            "3. Crie classes de construtores concretos para cada representação e implemente suas etapas de construção.",
            "4. Pense em criar uma classe Diretor (Director) para encapsular as configurações mais comuns do produto.",
            "5. O cliente cria tanto o objeto builder quanto o diretor, passando o builder para o diretor para iniciar a construção."
        ]
    },
    "prototype": {
        "name": "dp-prototype",
        "category": "Criacional",
        "description": "Permite copiar objetos existentes sem tornar seu código dependente de suas classes.",
        "intent": "Especificar os tipos de objetos a serem criados usando uma instância-protótipo e criar novos objetos copiando este protótipo.",
        "problem": "Você precisa copiar um objeto, mas não pode depender das classes concretas dele (p. ex. quando o código lida com objetos através de interfaces) ou deseja evitar o custo de instanciar e inicializar do zero se um estado similar já existe.",
        "solution": "Delegar o processo de clonagem aos próprios objetos que estão sendo clonados. O padrão declara uma interface comum com um método de clonagem (clone) para todos os objetos que suportam clonagem.",
        "structure": [
            "Protótipo (Prototype): Declara os métodos de clonagem. Normalmente, é apenas um método clone.",
            "Protótipo Concreto (Concrete Prototype): Implementa o método de cópia. Copia os dados do objeto original para o novo objeto, inclusive lidando com clonagem rasa (shallow copy) ou profunda (deep copy).",
            "Cliente (Client): Cria um novo objeto solicitando ao protótipo que se clone."
        ],
        "pros": [
            "Você pode clonar objetos sem acoplamento com suas classes concretas.",
            "Evita código de inicialização repetitivo clonando protótipos pré-configurados.",
            "Gera objetos complexos de forma mais conveniente."
        ],
        "contras": [
            "Clonar objetos complexos que têm referências circulares pode ser muito difícil."
        ],
        "implementation_guidelines": [
            "1. Crie a interface Prototype e declare o método clone nela.",
            "2. Uma classe de protótipo concreta deve definir o construtor que aceita um objeto daquela mesma classe como argumento para copiar todos os campos privados.",
            "3. O método clone geralmente executa um return new ConcretePrototype(*this) (ou equivalente da linguagem).",
            "4. Opcionalmente, crie um registro centralizado de protótipos (Prototype Registry) para catalogar instâncias prontas para cópia."
        ]
    },
    "singleton": {
        "name": "dp-singleton",
        "category": "Criacional",
        "description": "Garante que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para essa instância.",
        "intent": "Garantir que uma classe tenha apenas uma instância e fornecer um ponto de acesso global para ela.",
        "problem": "Garantir que uma classe tenha apenas uma única instância (ex: conexões com banco de dados, sistema de logs, caches compartilhados) e fornecer um ponto de acesso global simples sem expor variáveis globais vulneráveis.",
        "solution": "Tornar o construtor padrão privado para impedir instanciações diretas. Criar um método estático de acesso que atua como construtor, instanciando o objeto de forma tardia (lazy initialization) se necessário, e armazenando a instância em um campo estático.",
        "structure": [
            "Singleton: Declara o método estático (ex: getInstance) que retorna a mesma instância de sua própria classe. O construtor é privado."
        ],
        "pros": [
            "Garantia absoluta de uma única instância ativa da classe.",
            "Ponto de acesso global flexível e controlado.",
            "Inicialização tardia (Lazy initialization): o objeto só é criado quando é solicitado pela primeira vez."
        ],
        "contras": [
            "Viola o Princípio de Responsabilidade Única (a classe gerencia seu ciclo de vida além de sua lógica de negócios).",
            "Pode mascarar um design ruim, introduzindo dependências globais difíceis de testar em testes unitários."
        ],
        "implementation_guidelines": [
            "1. Adicione um campo estático privado na classe Singleton para armazenar a instância única.",
            "2. Declare um método de criação estático público para obter a instância.",
            "3. Implemente a inicialização tardia dentro do método estático (crie a instância se o campo for nulo).",
            "4. Torne o construtor da classe privado.",
            "5. Em ambientes multi-thread, implemente sincronização (p. ex., double-checked locking) para evitar condições de corrida na criação do Singleton."
        ]
    },

    # ----------------------------------------------------
    # ESTRUTURAIS (Structural)
    # ----------------------------------------------------
    "adapter": {
        "name": "dp-adapter",
        "category": "Estrutural",
        "description": "Permite que objetos com interfaces incompatíveis colaborem entre si.",
        "intent": "Converter a interface de uma classe em outra interface esperada pelos clientes. O Adapter permite que classes com interfaces incompatíveis trabalhem juntas.",
        "problem": "Você quer utilizar uma classe existente, mas a interface dela não corresponde à interface que o seu código cliente espera.",
        "solution": "Criar um adaptador: um objeto intermediário que converte a interface de um objeto para que outro possa compreendê-la. O adaptador envolve (wraps) um dos objetos para traduzir as chamadas.",
        "structure": [
            "Cliente (Client): Contém a lógica de negócio do programa e se comunica via Target interface.",
            "Interface do Cliente (Client Interface/Target): Descreve o protocolo que outras classes devem seguir para colaborar com o cliente.",
            "Adaptado (Adaptee): A classe de terceiros ou legado que possui a interface incompatível.",
            "Adaptador (Adapter): Uma classe que implementa a Interface do Cliente enquanto envolve o objeto Adaptado, traduzindo as requisições do Cliente em chamadas compreensíveis pelo Adaptado."
        ],
        "pros": [
            "Princípio da responsabilidade única: separa a lógica de conversão de dados da lógica de negócio.",
            "Princípio do aberto/fechado: introduz novos adaptadores sem quebrar o código cliente existente."
        ],
        "contras": [
            "A complexidade geral do código aumenta porque você precisa introduzir um conjunto de novas interfaces e classes."
        ],
        "implementation_guidelines": [
            "1. Certifique-se de ter pelo menos duas classes com interfaces incompatíveis (o serviço útil e o cliente).",
            "2. Declare a interface do cliente que descreve como ele deseja interagir com os serviços.",
            "3. Crie a classe Adapter e faça com que ela implemente a interface do cliente.",
            "4. Adicione um campo de referência para o objeto do serviço adaptado (Adaptee) no Adapter (composição).",
            "5. Implemente todos os métodos da interface do cliente no Adapter redirecionando as chamadas para o Adaptee."
        ]
    },
    "bridge": {
        "name": "dp-bridge",
        "category": "Estrutural",
        "description": "Divide uma classe grande ou um conjunto de classes intimamente ligadas em duas hierarquias separadas — abstração e implementação — que podem ser desenvolvidas independentemente.",
        "intent": "Desacoplar uma abstração de sua implementação, de modo que as duas possam variar independentemente.",
        "problem": "Explosão combinatória de subclasses (p. ex., se você tem classes de formas geométricas como Círculo e Quadrado, e quer variantes de cores como CírculoVermelho, QuadradoAzul, etc., o número de subclasses cresce exponencialmente).",
        "solution": "Substituir a herança por composição. Extrair a dimensão independente (ex: as cores) em sua própria hierarquia de classes (Implementação), e manter uma referência para ela na classe original (Abstração).",
        "structure": [
            "Abstração (Abstraction): Fornece lógica de controle de alto nível. Depende de um objeto de implementação.",
            "Abstração Refinada (Refined Abstraction): Variantes da lógica de controle.",
            "Implementação (Implementation): Declara a interface comum para todas as implementações concretas.",
            "Implementações Concretas (Concrete Implementations): Contêm código específico de plataforma ou infraestrutura."
        ],
        "pros": [
            "Cria plataformas e aplicativos independentes.",
            "Código cliente interage apenas com a abstração de alto nível, escondendo detalhes da plataforma.",
            "Princípio do aberto/fechado e Princípio da responsabilidade única."
        ],
        "contras": [
            "Pode tornar o código altamente estruturado e difícil de ler para desenvolvedores juniores."
        ],
        "implementation_guidelines": [
            "1. Identifique as dimensões independentes nas suas classes (ex: GUI vs. APIs de Sistema Operacional).",
            "2. Declare as operações que o cliente precisa na classe Abstração base.",
            "3. Declare as operações de baixo nível na interface Implementador.",
            "4. Para todas as variantes da abstração, crie classes Abstrações Refinadas.",
            "5. Crie classes de Implementação Concreta e aponte a referência da Abstração para um desses implementadores."
        ]
    },
    "composite": {
        "name": "dp-composite",
        "category": "Estrutural",
        "description": "Permite compor objetos em estruturas de árvore e trabalhar com essas estruturas como se fossem objetos individuais.",
        "intent": "Compor objetos em estruturas de árvore para representar hierarquias partes-todo. O Composite permite aos clientes tratarem de maneira uniforme objetos individuais e composições de objetos.",
        "problem": "Se o seu aplicativo pode ser representado como uma árvore de objetos (ex: caixas contendo produtos, que podem conter caixas menores com produtos), calcular o total ou processar a árvore exige varrer loops aninhados complexos e checar classes concretas a todo momento.",
        "solution": "Fazer com que caixas (compostos) e produtos (folhas) compartilhem uma interface comum que declare um método para executar a operação. Para um produto concreto, o método calcula o preço direto; para a caixa, varre seus itens filhos acumulando os preços.",
        "structure": [
            "Componente (Component): Declara a interface comum para elementos simples e complexos da árvore.",
            "Folha (Leaf): Elemento básico de uma árvore que não tem sub-elementos. Realiza o trabalho real.",
            "Container/Composite: Elemento que possui sub-elementos (folhas ou outros containers). Delega o trabalho real para seus filhos."
        ],
        "pros": [
            "Permite trabalhar com estruturas de árvore complexas mais convenientemente: polimorfismo facilita o uso de recursão.",
            "Princípio do aberto/fechado: novos tipos de elementos de árvore podem ser adicionados sem quebrar o código existente."
        ],
        "contras": [
            "Pode ser difícil fornecer uma interface comum para classes cujos comportamentos diferem muito. Pode ser necessário enfraquecer o encapsulamento ou a tipagem."
        ],
        "implementation_guidelines": [
            "1. Garanta que o modelo central da sua aplicação possa ser representado como uma estrutura de árvore.",
            "2. Declare a interface Componente com as operações que façam sentido tanto para folhas quanto para containers.",
            "3. Crie a classe Folha para representar elementos simples.",
            "4. Crie a classe Composite para representar containers, incluindo um array de Componentes filhos e métodos para gerenciar filhos (add/remove).",
            "5. Implemente os métodos da interface no Composite delegando as tarefas aos sub-elementos."
        ]
    },
    "decorator": {
        "name": "dp-decorator",
        "category": "Estrutural",
        "description": "Permite acoplar novos comportamentos a objetos ao colocá-los dentro de invólucros (wrappers) de objetos reais.",
        "intent": "Dinamicamente, anexar responsabilidades adicionais a um objeto. Os decorators fornecem uma alternativa flexível à herança para extensão de funcionalidade.",
        "problem": "Herança é estática e não permite alterar o comportamento de um objeto em tempo de execução. Além disso, estender classes com herança para todas as combinações de comportamentos leva a uma explosão de subclasses.",
        "solution": "Composição e Wrappers (Decorators). O Decorator implementa a mesma interface do objeto envolvido e delega as chamadas originais para ele, adicionando seu próprio comportamento antes ou depois da delegação.",
        "structure": [
            "Componente (Component): Declara a interface comum tanto para os wrappers quanto para os objetos envolvidos.",
            "Componente Concreto (Concrete Component): A classe de objetos sendo envolvida que define o comportamento básico.",
            "Decorador Base (Base Decorator): Mantém uma referência ao objeto envolvido e delega todo o trabalho a ele.",
            "Decoradores Concretos (Concrete Decorators): Sobrescrevem métodos do Decorador Base para adicionar comportamentos adicionais dinamicamente."
        ],
        "pros": [
            "Estende o comportamento de um objeto sem criar uma nova subclasse.",
            "Adiciona ou remove responsabilidades de um objeto em tempo de execução.",
            "Combina múltiplos comportamentos ao envolver um objeto em vários decoradores."
        ],
        "contras": [
            "É difícil remover um wrapper específico do meio da pilha de decorators.",
            "Dificuldade de depurar objetos com comportamento dependente da ordem dos invólucros."
        ],
        "implementation_guidelines": [
            "1. Certifique-se de que seu método de negócio principal e os decorators compartilham a mesma interface.",
            "2. Crie uma classe base Decorator com um campo de referência para o Componente original.",
            "3. Redirecione todas as operações do Decorator base para o objeto referenciado.",
            "4. Crie decoradores concretos herdando do Decorator base e adicione comportamento customizado nas operações."
        ]
    },
    "facade": {
        "name": "dp-facade",
        "category": "Estrutural",
        "description": "Fornece uma interface simplificada para uma biblioteca, um framework, ou qualquer outro conjunto complexo de classes.",
        "intent": "Fornecer uma interface unificada para um conjunto de interfaces em um subsistema. A Facade define uma interface de nível mais alto que torna o subsistema mais fácil de usar.",
        "problem": "Sua aplicação precisa interagir com um subsistema complexo contendo dezenas de classes, inicializações específicas e dependências intrincadas.",
        "solution": "Criar uma classe Fachada (Facade) que fornece um ponto de entrada simplificado para os recursos mais comuns do subsistema. O cliente chama apenas a Fachada, que sabe como orquestrar as classes internas.",
        "structure": [
            "Fachada (Facade): Fornece acesso conveniente a uma parte específica da funcionalidade do subsistema, sabendo para onde direcionar a requisição do cliente.",
            "Fachada Adicional (Additional Facade): Pode ser criada para evitar poluir uma única fachada com recursos não relacionados.",
            "Subsistema Complexo (Complex Subsystem): Dezenas de objetos diversos que realizam tarefas de baixo nível."
        ],
        "pros": [
            "Isola seu código das complexidades de um subsistema de terceiros ou legado.",
            "Facilita o uso e reduz o acoplamento entre clientes e subsistemas."
        ],
        "contras": [
            "Uma fachada pode se tornar um objeto deus (god object) acoplado a todas as classes de um aplicativo se não for bem gerenciada."
        ],
        "implementation_guidelines": [
            "1. Determine se uma interface mais simples já ajudaria a reduzir o acoplamento com o subsistema.",
            "2. Declare e implemente essa interface em uma classe Facade.",
            "3. A Facade deve ser responsável por inicializar e gerenciar o ciclo de vida dos componentes do subsistema.",
            "4. Faça com que o código cliente chame apenas a Facade, ocultando o subsistema."
        ]
    },
    "flyweight": {
        "name": "dp-flyweight",
        "category": "Estrutural",
        "description": "Permite ajustar mais objetos na quantidade disponível de RAM ao compartilhar partes comuns de estado entre múltiplos objetos em vez de manter todos os dados em cada objeto.",
        "intent": "Usar compartilhamento para suportar grandes quantidades de objetos de grão fino de maneira eficiente.",
        "problem": "A aplicação cria milhares ou milhões de instâncias semelhantes, esgotando a memória RAM por carregar dados repetitivos (ex: dados visuais de árvores em um jogo florestal).",
        "solution": "Dividir o estado do objeto em duas partes: Estado Intrínseco (dados constantes que podem ser compartilhados e armazenados no Flyweight) e Estado Extrínseco (dados variáveis que dependem do contexto de uso e são mantidos fora do Flyweight).",
        "structure": [
            "Flyweight: Contém a parte do estado do objeto original que pode ser compartilhada por múltiplas instâncias (ex: textura e modelo 3D).",
            "Contexto (Context): Contém o estado extrínseco, único para todas as situações (ex: coordenadas X, Y da árvore individual) e uma referência ao Flyweight correspondente.",
            "Fábrica Flyweight (Flyweight Factory): Gerencia o cache de objetos Flyweight existentes para garantir que novos só sejam criados se não existirem no cache."
        ],
        "pros": [
            "Economiza muita memória RAM se o programa tiver muitos objetos parecidos."
        ],
        "contras": [
            "Pode aumentar o uso de CPU para recalcular ou buscar o estado extrínseco.",
            "Torna o código consideravelmente complexo devido à separação de dados."
        ],
        "implementation_guidelines": [
            "1. Divida os campos da classe que consome muita RAM em: estado intrínseco (imutável, compartilhável) e estado extrínseco (mutável, dependente de contexto).",
            "2. Mantenha os campos intrínsecos em uma classe Flyweight separada e torne seus campos imutáveis.",
            "3. Crie uma Fábrica Flyweight para gerenciar o pool de instâncias Flyweight.",
            "4. Os clientes usam o Flyweight chamando seus métodos e passando o estado extrínseco como argumentos."
        ]
    },
    "proxy": {
        "name": "dp-proxy",
        "category": "Estrutural",
        "description": "Fornece um substituto ou um espaço reservado para outro objeto. Um proxy controla o acesso ao objeto original, permitindo fazer algo antes ou depois que a requisição chegue a ele.",
        "intent": "Fornecer um substituto ou marcador de localização para outro objeto para controlar o acesso a esse objeto.",
        "problem": "Você tem um objeto pesado que consome muitos recursos (ex: banco de dados, leitor de arquivos grandes) e quer controlar seu acesso, fazer carregamento sob demanda (lazy loading), registrar logs de acesso (logging), ou caching, sem alterar a classe do objeto original.",
        "solution": "Criar uma classe Proxy com a mesma interface do objeto original. O Proxy intercepta todas as chamadas do cliente, realiza a operação secundária (verificação, log, cache) e, se apropriado, delega o trabalho real ao objeto de serviço real.",
        "structure": [
            "Interface do Serviço (Service Interface): Declara a interface comum ao Serviço Real e ao Proxy.",
            "Serviço Real (Real Service): Classe de serviço que contém a lógica de negócio real.",
            "Proxy: Contém uma referência ao objeto de serviço. Gerencia o ciclo de vida do serviço real e delega chamadas a ele."
        ],
        "pros": [
            "Permite controlar o objeto de serviço sem que o cliente saiba disso.",
            "Gerencia o ciclo de vida do objeto de serviço quando o cliente não se importa com isso.",
            "O Proxy funciona mesmo se o serviço real não estiver pronto ou disponível."
        ],
        "contras": [
            "O código pode se tornar mais complicado devido à introdução de novas classes.",
            "A resposta do serviço pode sofrer pequenos atrasos pela passagem pelo proxy."
        ],
        "implementation_guidelines": [
            "1. Crie uma interface comum para o serviço real e o proxy (caso não exista).",
            "2. Crie a classe Proxy e armazene uma referência ao objeto de serviço nela.",
            "3. Implemente os métodos da interface no Proxy e intercale a lógica de controle necessária antes/depois de delegar para o serviço real."
        ]
    },

    # ----------------------------------------------------
    # COMPORTAMENTAIS (Behavioral)
    # ----------------------------------------------------
    "chain-of-responsibility": {
        "name": "dp-chain-of-responsibility",
        "category": "Comportamental",
        "description": "Permite passar requisições por uma corrente de manipuladores. Ao receber uma requisição, cada manipulador decide se processa a requisição ou a passa para o próximo manipulador.",
        "intent": "Evitar o acoplamento do remetente de uma solicitação ao seu receptor, dando a mais de um objeto a oportunidade de tratar a solicitação. Encadear os objetos receptores e passar a solicitação ao longo da cadeia até que um objeto a trate.",
        "problem": "Um sistema precisa processar diferentes tipos de requisições sequencialmente (ex: autenticação, autorização, sanitização de dados, caching), e a ordem ou os componentes envolvidos podem mudar em tempo de execução.",
        "solution": "Transformar os comportamentos em objetos independentes chamados manipuladores (handlers). Cada manipulador possui um campo para armazenar uma referência ao próximo na corrente. A requisição viaja pela corrente até ser tratada ou interrompida.",
        "structure": [
            "Manipulador (Handler): Declara a interface comum a todos os manipuladores da cadeia (geralmente um método handle).",
            "Manipulador Base (Base Handler): Classe opcional para manter a referência ao próximo manipulador e gerenciar a cadeia.",
            "Manipuladores Concretos (Concrete Handlers): Contêm o código real para processar a requisição. Ao receber a requisição, decidem se a tratam e/ou se a enviam adiante.",
            "Cliente (Client): Monta a corrente de manipuladores e dispara a requisição inicial."
        ],
        "pros": [
            "Você pode controlar a ordem de tratamento de requisições.",
            "Princípio da responsabilidade única: desacopla classes que chamam operações de classes que as executam.",
            "Princípio do aberto/fechado: introduz novos manipuladores no aplicativo sem quebrar o código existente."
        ],
        "contras": [
            "Algumas requisições podem chegar ao final da cadeia sem serem tratadas se nenhum manipulador a interceptar."
        ],
        "implementation_guidelines": [
            "1. Declare a interface do manipulador com um método de processamento.",
            "2. Crie uma classe abstrata base para eliminar o código padrão de encadeamento.",
            "3. Implemente os manipuladores concretos herdando da base e definindo as condições de tratamento.",
            "4. O cliente encadeia os manipuladores usando setters apropriados e inicia o fluxo chamando o primeiro manipulador."
        ]
    },
    "command": {
        "name": "dp-command",
        "category": "Comportamental",
        "description": "Transforma uma solicitação em um objeto independente que contém toda a informação sobre a solicitação, permitindo parametrizar, enfileirar ou desfazer operações.",
        "intent": "Encapsular uma solicitação como um objeto, desta forma permitindo parametrizar clientes com diferentes solicitações, enfileirar ou registrar solicitações e suportar operações que podem ser desfeitas.",
        "problem": "Vincular comandos de interface de usuário (como botões e atalhos de teclado) diretamente a classes de negócio acopla fortemente os componentes visuais com as regras de negócio, além de dificultar o suporte a operações de desfazer/refazer (undo/redo).",
        "solution": "Extrair detalhes da solicitação em classes separadas que implementam uma interface comum com um método execute. O acionador (invoker) chama execute sem saber qual comando está sendo executado.",
        "structure": [
            "Comando (Command): Declara a interface comum com o método execute.",
            "Comandos Concretos (Concrete Commands): Implementam o método execute e delegam chamadas para um ou mais objetos receptores.",
            "Remetente/Invocador (Invoker/Sender): Classe responsável por iniciar a solicitação (ex: botão). Mantém uma referência ao Comando.",
            "Receptor (Receiver): A classe que contém a lógica de negócio real a ser executada pelo comando.",
            "Cliente (Client): Cria e configura objetos comandos concretos e os associa aos invocadores."
        ],
        "pros": [
            "Desacopla a classe que invoca a operação da classe que realiza a operação.",
            "Permite implementar operações reversíveis (desfazer/refazer) salvando o histórico de comandos executados.",
            "Permite enfileirar ou agendar a execução de comandos.",
            "Permite criar comandos compostos (padrão macro)."
        ],
        "contras": [
            "O código pode ficar mais complexo, pois introduz uma camada completamente nova de comandos."
        ],
        "implementation_guidelines": [
            "1. Declare a interface do comando com o método execute (e opcionalmente undo).",
            "2. Crie classes de comandos concretos, injetando o objeto receptor adequado no construtor.",
            "3. Implemente execute nos comandos concretos mapeando para chamadas de métodos no receptor.",
            "4. Configure os remetentes (invokers) para aceitar e disparar os comandos."
        ]
    },
    "iterator": {
        "name": "dp-iterator",
        "category": "Comportamental",
        "description": "Permite percorrer elementos de uma coleção sem expor sua representação subjacente (lista, pilha, árvore, etc.).",
        "intent": "Fornecer uma maneira de acessar sequencialmente os elementos de um objeto agregado sem expor sua representação subjacente.",
        "problem": "Diferentes estruturas de dados (listas ligadas, árvores, pilhas) exigem algoritmos de travessia totalmente diferentes. Misturar esses algoritmos de busca dentro da lógica de negócio polui as classes e expõe suas estruturas internas.",
        "solution": "Extrair o algoritmo de travessia de uma coleção para um objeto independente chamado iterador. O iterador encapsula o estado de iteração atual (como índice e ponteiros) e fornece métodos simples como next e hasMore.",
        "structure": [
            "Iterador (Iterator): Declara as operações necessárias para percorrer uma coleção.",
            "Iteradores Concretos (Concrete Iterators): Implementam algoritmos específicos para percorrer uma coleção específica.",
            "Coleção (Iterable/Collection): Declara um método para obter iteradores compatíveis com a coleção.",
            "Coleções Concretas (Concrete Collections): Retornam novas instâncias de um iterador concreto associado à sua estrutura interna."
        ],
        "pros": [
            "Princípio da responsabilidade única: limpa as coleções movendo algoritmos de busca complexos para classes separadas.",
            "Permite percorrer a mesma coleção em paralelo usando múltiplos iteradores independentes.",
            "Permite adiar uma iteração e continuá-la depois."
        ],
        "contras": [
            "Aplicar o padrão pode ser exagero se o aplicativo funcionar apenas com listas simples."
        ],
        "implementation_guidelines": [
            "1. Declare a interface do iterador com métodos como next, current, e hasNext.",
            "2. Declare a interface da coleção com o método para gerar um iterador.",
            "3. Crie os iteradores concretos implementando a interface do iterador para varrer a coleção específica.",
            "4. Faça a coleção implementar o método gerador retornando uma instância do iterador correto passando self/this."
        ]
    },
    "mediator": {
        "name": "dp-mediator",
        "category": "Comportamental",
        "description": "Reduz as dependências caóticas entre objetos. Restringe comunicações diretas entre objetos e os força a colaborar apenas através de um objeto mediador.",
        "intent": "Definir um objeto que encapsula como um conjunto de objetos interage. O Mediator promove o acoplamento fraco ao impedir que os objetos se refiram uns aos outros explicitamente, e permite variar sua interação independentemente.",
        "problem": "Conexões e comunicações excessivas entre dezenas de classes diferentes (como componentes de tela de um formulário complexo) tornam qualquer alteração em um componente propensa a quebrar os demais (código espaguete).",
        "solution": "Cessar comunicações diretas entre os componentes e criar uma classe central (Mediador). Todos os componentes reportam eventos para o Mediador, e este decide como redirecionar ou tratar a ação entre os outros componentes.",
        "structure": [
            "Mediador (Mediator): Declara a interface de comunicação com os componentes (geralmente um método notify).",
            "Mediador Concreto (Concrete Mediator): Encapsula a relação entre vários componentes e coordena suas ações.",
            "Componentes (Colleagues): Classes que realizam lógica de negócio individual. Elas não se conhecem mutuamente e referenciam apenas o Mediador."
        ],
        "pros": [
            "Princípio da responsabilidade única: extrai redes de comunicação complexas para um único local centralizado.",
            "Princípio do aberto/fechado: introduz novos mediadores sem alterar os componentes individuais.",
            "Reduz o acoplamento entre os vários componentes do sistema."
        ],
        "contras": [
            "Com o tempo, o mediador pode evoluir para um Objeto Deus (God Object)."
        ],
        "implementation_guidelines": [
            "1. Identifique um grupo de classes fortemente acopladas que se beneficiariam de maior independência.",
            "2. Declare a interface Mediator com o método genérico de notificação.",
            "3. Implemente a classe ConcreteMediator mantendo referências a todos os componentes envolvidos.",
            "4. Modifique as classes de componentes para aceitar a referência do Mediador e disparar notificações para ele ao invés de chamarem outros componentes diretamente."
        ]
    },
    "memento": {
        "name": "dp-memento",
        "category": "Comportamental",
        "description": "Permite salvar e restaurar o estado anterior de um objeto sem revelar os detalhes de sua implementação.",
        "intent": "Sem violar o encapsulamento, capturar e externar o estado interno de um objeto, de modo que o objeto possa ser restaurado para este estado mais tarde.",
        "problem": "Você quer salvar e restaurar backups do estado de um objeto (para comandos undo, histórico), mas os campos do objeto são privados e expô-los violaria gravemente o encapsulamento básico da POO.",
        "solution": "Delegar a criação do backup ao próprio objeto dono do estado (Originador). O Originador cria um objeto Memento contendo um instantâneo de seus campos. O Memento é imutável e seus dados são lidos apenas pelo próprio Originador.",
        "structure": [
            "Originador (Originator): O objeto que tem o estado interno. Ele sabe como criar um Memento e como restaurar seu estado a partir dele.",
            "Memento: Um objeto de valor imutável que atua como instantâneo do estado do Originador.",
            "Cuidador (Caretaker): Gerencia a pilha de mementos (histórico) sem ler ou modificar o estado interno dos mementos."
        ],
        "pros": [
            "Salva e restaura o estado de um objeto sem violar o encapsulamento.",
            "Simplifica o código do Originador delegando a guarda do histórico ao Cuidador."
        ],
        "contras": [
            "O consumo de memória RAM pode disparar se os clientes criarem mementos frequentemente e eles não forem descartados.",
            "O Cuidador deve gerenciar o ciclo de vida do histórico ativamente."
        ],
        "implementation_guidelines": [
            "1. Defina a classe Memento contendo os atributos que precisam ser arquivados.",
            "2. Adicione na classe Originator métodos para salvar o estado (retorna um Memento) e restaurar o estado (aceita um Memento).",
            "3. Crie a classe Caretaker com um histórico de mementos coletados e controle para push/pop na pilha de undo/redo."
        ]
    },
    "observer": {
        "name": "dp-observer",
        "category": "Comportamental",
        "description": "Permite definir um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.",
        "intent": "Definir uma dependência um-para-muitos entre objetos, de modo que, quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.",
        "problem": "Quando um objeto muda seu estado, outros objetos precisam executar ações decorrentes dessa mudança, mas você quer evitar acoplamento direto ou pesquisas em loops infinitos (polling).",
        "solution": "Criar um mecanismo de assinatura. O objeto que possui o estado interessante (Sujeito/Publisher) mantém uma lista de referências de objetos interessados (Observadores/Subscribers) e chama seus métodos de notificação quando ocorrem mudanças.",
        "structure": [
            "Publicador (Publisher/Subject): Mantém a lista de assinantes e fornece métodos para adicionar e remover assinantes. Dispara eventos.",
            "Assinante (Subscriber/Observer Interface): Declara a interface de notificação (normalmente contendo um método update).",
            "Assinantes Concretos (Concrete Subscribers): Implementam as ações em resposta às notificações do publicador."
        ],
        "pros": [
            "Princípio do aberto/fechado: você pode introduzir novos assinantes sem alterar o código do publicador.",
            "Estabelece relações dinâmicas em tempo de execução entre objetos."
        ],
        "contras": [
            "Os assinantes são notificados em ordem aleatória, e se não forem removidos (unsubscribe) podem gerar vazamento de memória (lapsed listener problem)."
        ],
        "implementation_guidelines": [
            "1. Identifique o publicador (Publisher) que dispara os eventos de alteração de estado.",
            "2. Declare a interface Observer com um método update.",
            "3. Na classe Publisher, adicione uma lista/array de Observers e métodos de gerência (subscribe/unsubscribe).",
            "4. Ao disparar uma mudança, percorra a lista de assinantes chamando update de cada um."
        ]
    },
    "state": {
        "name": "dp-state",
        "category": "Comportamental",
        "description": "Permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe.",
        "intent": "Permitir a um objeto alterar seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe.",
        "problem": "Uma classe possui condicionais gigantescos (switch-case ou if-else aninhados) que alteram completamente as operações da classe com base nos valores de seus atributos de estado atuais.",
        "solution": "Extrair as lógicas de comportamento associadas a cada estado em classes separadas de Estado Concreto. O objeto de contexto principal armazena uma referência para o objeto de estado atual e delega a ele toda a lógica.",
        "structure": [
            "Contexto (Context): Mantém uma referência a um dos objetos de estado concreto e delega o trabalho.",
            "Estado (State Interface): Declara os métodos que todos os estados concretos devem implementar.",
            "Estados Concretos (Concrete States): Implementam comportamentos específicos associados a um estado do Contexto. Podem transicionar o contexto para outro estado."
        ],
        "pros": [
            "Princípio da responsabilidade única: organiza o código relacionado a estados particulares em classes separadas.",
            "Princípio do aberto/fechado: introduz novos estados sem alterar as classes de estado existentes ou o contexto.",
            "Elimina condicionais de estado monolíticos e difíceis de testar."
        ],
        "contras": [
            "Pode ser um exagero se a máquina de estados tiver poucas transições ou condições simples."
        ],
        "implementation_guidelines": [
            "1. Declare a interface State contendo métodos correspondentes a todas as ações iniciadas pelo contexto.",
            "2. Crie classes de estados concretos para cada estado possível da aplicação.",
            "3. Faça o Contexto expor um método setter público para alterar seu estado em tempo de execução.",
            "4. Delegue os métodos de comportamento do Contexto para o objeto State atual."
        ]
    },
    "strategy": {
        "name": "dp-strategy",
        "category": "Comportamental",
        "description": "Define uma família de algoritmos, coloca cada um deles em uma classe separada, e faz seus objetos intercambiáveis.",
        "intent": "Definir uma família de algoritmos, encapsular cada um deles e torná-los intercambiáveis. O Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam.",
        "problem": "Você tem várias alternativas para executar uma determinada lógica de negócio (ex: diferentes métodos de ordenação, rotas de navegação, métodos de pagamento) e quer alternar entre elas em tempo de execução sem encher o código cliente de condicionais complexos.",
        "solution": "Extrair os algoritmos em classes separadas chamadas Estratégias (Strategies). A classe original (Contexto) mantém uma referência a uma interface Estratégia e delega a execução do algoritmo a ela.",
        "structure": [
            "Contexto (Context): Mantém uma referência para uma das estratégias e se comunica via interface genérica da estratégia.",
            "Estratégia (Strategy Interface): Comum a todas as variantes dos algoritmos. Declara o método de execução.",
            "Estratégias Concretas (Concrete Strategies): Implementações variadas do algoritmo."
        ],
        "pros": [
            "Substitui herança por composição, dando mais flexibilidade em tempo de execução.",
            "Isola os detalhes de implementação do algoritmo do código que o consome.",
            "Princípio do aberto/fechado: novas estratégias podem ser introduzidas sem mexer no contexto."
        ],
        "contras": [
            "Se você tiver apenas alguns algoritmos estáveis, a introdução de novas interfaces e classes apenas complica desnecessariamente o projeto."
        ],
        "implementation_guidelines": [
            "1. Declare a interface Strategy com a assinatura do método do algoritmo.",
            "2. Crie classes concretas implementando as variações do algoritmo.",
            "3. Na classe Context, armazene uma referência à interface Strategy e implemente um método setter para injetar a estratégia desejada.",
            "4. Chame o método da estratégia no fluxo de execução do Contexto."
        ]
    },
    "template-method": {
        "name": "dp-template-method",
        "category": "Comportamental",
        "description": "Define o esqueleto de um algoritmo na superclasse mas deixa as subclasses sobrescreverem etapas específicas do algoritmo sem modificar sua estrutura.",
        "intent": "Definir o esqueleto de um algoritmo em uma operação, adiando a definição de alguns passos para subclasses. O Template Method permite que as subclasses redefinam certas etapas de um algoritmo sem mudar a sua estrutura.",
        "problem": "Várias classes executam algoritmos que seguem passos muito semelhantes, com pequenas diferenças em etapas específicas (ex: leitores de relatórios PDF, CSV e JSON que abrem, leem e fecham arquivos da mesma forma, diferindo apenas na análise do conteúdo).",
        "solution": "Criar uma classe base abstrata e declarar o método modelo (Template Method) que define a sequência de chamadas de etapas. Algumas etapas podem ser implementadas diretamente na base (etapas padrão) e outras declaradas como abstratas (ganchos/hooks) para serem implementadas pelas subclasses.",
        "structure": [
            "Classe Abstrata (Abstract Class): Declara o método modelo e as etapas abstratas/concretas do algoritmo.",
            "Classe Concreta (Concrete Class): Sobrescreve as etapas abstratas para personalizar o comportamento sem mexer na estrutura do algoritmo principal."
        ],
        "pros": [
            "Evita duplicação de código ao puxar as etapas repetitivas para a superclasse.",
            "Permite controle rigoroso sobre a estrutura e extensão permitida do algoritmo por meio de ganchos (hooks)."
        ],
        "contras": [
            "Alguns clientes podem se sentir limitados pelo esqueleto rígido do algoritmo fornecido pela superclasse.",
            "Pode violar o Princípio de Substituição de Liskov se as subclasses mudarem as premissas de execução das etapas herdadas."
        ],
        "implementation_guidelines": [
            "1. Analise o algoritmo alvo para ver se você pode dividi-lo em etapas sequenciais.",
            "2. Declare a classe base abstrata e crie o método modelo contendo o fluxo das etapas.",
            "3. Declare as etapas que diferem entre as variações como métodos abstratos (devem ser implementadas) ou métodos virtuais com comportamento básico (hooks).",
            "4. Crie subclasses concretas e implemente os métodos de etapas correspondentes."
        ]
    },
    "visitor": {
        "name": "dp-visitor",
        "category": "Comportamental",
        "description": "Permite separar algoritmos dos objetos nos quais eles operam.",
        "intent": "Representar uma operação a ser realizada sobre os elementos de uma estrutura de objetos. O Visitor permite definir uma nova operação sem mudar as classes dos elementos sobre os quais opera.",
        "problem": "Você precisa aplicar uma operação em toda uma estrutura complexa de objetos (ex: árvore de nós do compilador, grafo de nós XML) sem poluir o código das classes desses nós com lógicas não-relacionadas a eles, e novas operações são adicionadas constantemente.",
        "solution": "Colocar o novo comportamento em uma classe separada chamada Visitante (Visitor) em vez de integrá-lo diretamente nas classes de nós. O objeto que executa o método é passado como argumento para o método visit do visitante (técnica de Double Dispatch).",
        "structure": [
            "Visitante (Visitor Interface): Declara um conjunto de métodos de visita correspondendo às classes de elementos concretos.",
            "Visitantes Concretos (Concrete Visitors): Implementam operações de negócio diferentes para serem executadas sobre a estrutura.",
            "Elemento (Element Interface): Declara o método accept para aceitar o visitante.",
            "Elementos Concretos (Concrete Elements): Implementam o método accept chamando o método visit correspondente no visitante passado."
        ],
        "pros": [
            "Princípio do aberto/fechado: introduz operações que funcionam com várias classes sem alterá-las.",
            "Princípio da responsabilidade única: move comportamentos não relacionados para a classe do visitante.",
            "Pode acumular estados úteis enquanto visita os vários nós da estrutura."
        ],
        "contras": [
            "Adicionar ou remover uma classe de elemento exige atualizar a interface do visitante e todas as suas implementações."
        ],
        "implementation_guidelines": [
            "1. Declare a interface Visitor com métodos visit correspondendo a cada elemento concreto.",
            "2. Declare o método abstrato accept(visitor) na interface Element.",
            "3. Implemente accept nas classes concretas para chamarem visitor.visit(this).",
            "4. Crie classes de visitantes concretos implementando as operações que deseja realizar sobre os elementos."
        ]
    }
}

# Criar a pasta skills se não existir
os.makedirs("skills", exist_ok=True)

# Loop para gerar os arquivos
for key, data in patterns.items():
    folder_path = os.path.join("skills", f"dp-{key}")
    os.makedirs(folder_path, exist_ok=True)
    
    # Criar subdiretórios
    for sub in ["scripts", "examples", "resources", "references"]:
        os.makedirs(os.path.join(folder_path, sub), exist_ok=True)
        # Arquivo gitkeep
        with open(os.path.join(folder_path, sub, ".gitkeep"), "w", encoding="utf-8") as f:
            f.write(f"# Mantem a pasta de {sub} ativa\n")

    # Gerar conteúdo do SKILL.md
    skill_content = f"""---
name: "{data['name']}"
description: "Padrão de Projeto {data['category']}: {data['description']}"
---

# Design Pattern: {data['name'].replace('dp-', '').replace('-', ' ').title()} ({data['category']})

## 🎯 Intenção
{data['intent']}

## ❓ Problema
{data['problem']}

## 💡 Solução
{data['solution']}

## 🏗️ Estrutura do Padrão
{chr(10).join(f"- {item}" for item in data['structure'])}

## ⚖️ Prós e Contras

### ✅ Prós:
{chr(10).join(f"- {item}" for item in data['pros'])}

### ❌ Contras:
{chr(10).join(f"- {item}" for item in data['contras'])}

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

{chr(10).join(data['implementation_guidelines'])}

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
"""

    skill_file_path = os.path.join(folder_path, "SKILL.md")
    with open(skill_file_path, "w", encoding="utf-8") as f:
        f.write(skill_content.strip() + "\n")
    
    print(f"Gerado: {skill_file_path}")

print("Todos os padrões foram gerados com sucesso!")
