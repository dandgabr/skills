---
name: "memory-manipulation"
description: "Atua como especialista em manipulação de memória e segurança de baixo nível, cobrindo alocação dinâmica, gerenciamento de ponteiros, vulnerabilidades (buffer overflows, UAF, double free), técnicas ofensivas (heap grooming, ROP) e mitigações modernas (MTE, CFI, ASan)."
metadata:
  type: offensive
  phase: exploitation
  tools: [pwntools, gdb-gef, pwndbg, radare2, ropper, ROPgadget, one_gadget, angr, WinDbg, IDA]
  mitre: [T1203, T1068, T1211, T1212, T1055]
---

# Habilidade de IA: Manipulação e Segurança de Memória (Memory Manipulation & Security)

Esta skill capacita o agente de IA a atuar como um especialista de baixo nível em gerenciamento, depuração, auditoria e segurança de memória. Ela aborda as principais técnicas de manipulação de memória, vulnerabilidades clássicas e modernas, vetores de exploração ofensiva e mecanismos de defesa no nível do compilador, do sistema operacional e do hardware.

---

## 🎯 Objetivo da Skill
Orientar o agente na identificação, correção e prevenção de falhas de segurança e bugs de gerenciamento de memória em linguagens de baixo nível e sistemas compilados (especialmente C, C++, Assembly, Rust e Go), garantindo a robustez do software contra ataques de corrupção de memória através de uma abordagem científica e baseada em evidências.

## 🛠️ Instruções de Uso para a IA

1. **Contexto de Ativação**:
   - Ative esta skill sempre que trabalhar com código C/C++, Rust (unsafe), Assembly ou ao analisar falhas de segmentação (Segfaults), vazamentos de memória (Memory Leaks) e vulnerabilidades de corrupção de memória.
   
2. **Passo a Passo de Execução (Ciclo de Vida do Finding)**:
   - **Passo 1 (Análise Estática/Taint Analysis)**: Rastreie caminhos de dados controlados pelo usuário (sources) até destinos críticos de memória (sinks). Inspecione o ciclo de vida dos ponteiros e limites de buffers.
   - **Passo 2 (Verificação de Crash & Causa Raiz)**: Ao analisar um crash, utilize rastreabilidade determinística (ex: `rr`) para retroceder até a instrução exata que corrompeu a memória.
   - **Passo 3 (Mapeamento de Mitigações)**: Não faça suposições estáticas. Teste a falha reconstruindo o cenário de execução sob diferentes perfis de compilação (*Permissive*, *Distro*, *Hardened*) para determinar a viabilidade real da exploração.
   - **Passo 4 (Defesa & Hardening)**: Formule mitigações aplicadas ao código (correções de lógica) e de compilação (flags de segurança, sanitizadores ASan/MSan/UBSan).

---

## 🧠 Conceitos Fundamentais de Memória

Para manipular ou depurar memória de forma eficaz, o agente deve entender a organização do Espaço de Endereçamento Virtual de um processo:

1. **Pilha (Stack)**:
   - Gerenciada automaticamente pelo compilador.
   - Armazena variáveis locais, parâmetros de função e endereços de retorno.
   - Cresce para baixo (em direção a endereços menores na arquitetura x86/x64).
   - Alocações são rápidas, mas de escopo estritamente local (LIFO).

2. **Heap**:
   - Gerenciado dinamicamente pelo programador em tempo de execução via chamadas como `malloc()`, `calloc()`, `realloc()`, `free()`, ou operadores `new`/`delete`.
   - Armazena dados de longa duração cuja dimensão não é conhecida em tempo de compilação.
   - Gerenciadores de heap (ex: *ptmalloc* no glibc, *jemalloc*, *Segment Heap* no Windows) organizam a memória livre em listas (bins, fastbins, tcache) para reutilização rápida.

3. **Segmentos Estáticos (Data, BSS e Text)**:
   - **Text**: Contém as instruções em código de máquina (geralmente somente-leitura e executável).
   - **Data**: Variáveis globais e estáticas inicializadas.
   - **BSS**: Variáveis globais e estáticas não inicializadas (zeradas na inicialização).

4. **Aritmética de Ponteiros**:
   - A manipulação direta de endereços de memória. Incrementos em ponteiros dependem do tipo base (ex: `char* ptr` avança 1 byte, enquanto `int* ptr` avança 4 bytes na maioria dos sistemas de 32/64 bits).

---

## 🗺️ Tabela de Técnicas de Exploração & Mapeamento

| Técnica | MITRE ATT&CK | CWE | Mitigações Ignoradas/Alvos | Ferramentas |
| :--- | :--- | :--- | :--- | :--- |
| **Stack Overflow -> ROP** | T1203 | CWE-121 | Contorna DEP/NX usando *gadgets* na memória | `pwntools`, `ropper`, `one_gadget` |
| **Ret2csu / SROP** | T1203 | CWE-121 | Contorna escassez de *gadgets* de registradores | `pwntools`, `ROPgadget` |
| **Tcache/Fastbin Poisoning** | T1203 | CWE-416 | Alvos de metadados do heap (glibc) | `pwndbg`, `gdb-gef` |
| **Bypass de Safe-Linking** | T1203 | CWE-416 | Ofuscação de ponteiros do heap (glibc) | Scripts XOR Customizados |
| **House of Orange / Einherjar** | T1203 | CWE-415 | Exploração de heap sem chamadas diretas a `free()` | `gdb-gef` |
| **FSOP (File Structure Oriented)**| T1203 | CWE-787 | Manipulação de estruturas `_IO_FILE` (glibc) | `pwndbg` |
| **Format String Arbitrary Write** | T1203 | CWE-134 | Leitura e escrita arbitrária via modificadores `%n` | `pwntools` |
| **Type Confusion (JIT V8)** | T1203 | CWE-843 | Escapes de sandbox de navegadores modernos | `d8`, `Ghidra` |

---

## ⚠️ Principais Problemas e Vulnerabilidades de Memória

### 1. Estouro de Buffer na Pilha (Stack-Based Buffer Overflow)
- **O que é**: Escrita além dos limites de um array local na pilha, sobrescrevendo metadados de controle.
- **Impacto**: Sobrescrita do endereço de retorno da função para desviar o fluxo de execução.

### 2. Corrupção e Estouro de Heap (Heap Overflow / Heap Corruption)
- **O que é**: Escrita além do limite de um buffer alocado dinamicamente no heap.
- **Impacto**: Sobrescreve metadados dos chunks vizinhos, permitindo redirecionar ponteiros de escrita livre (*arbitrary write*).

### 3. Use-After-Free (UAF)
- **O que é**: Utilização de um ponteiro após o bloco de memória associado ter sido liberado via `free()`.
- **Impacto**: Permite ler ou substituir estruturas de objetos novos alocados no mesmo endereço (ex: vtables).

### 4. Liberação Dupla (Double Free)
- **O que é**: Chamar `free()` no mesmo endereço mais de uma vez sem alocações intermediárias.
- **Impacto**: Corrompe a estrutura de lista encadeada livre do alocador de heap, permitindo o retorno de buffers sobrepostos em futuras alocações.

### 5. Estouro de Inteiro (Integer Overflow / Underflow)
- **O que é**: Operações aritméticas que extrapolam o valor máximo/mínimo suportado pelo tipo numérico.
- **Impacto**: Frequentemente resulta em alocações de tamanho muito reduzido que sofrem estouro de buffer subsequente durante transferências de dados.

### 6. Vulnerabilidade de String de Formatação (Format String)
- **O que é**: Passar entrada não sanitizada do usuário diretamente para argumentos de formatação (ex: `printf(user_input)`).
- **Impacto**: Permite leitura (usando `%p`, `%x`) e escrita arbitrária em endereços de memória (usando `%n`).

### 7. Leitura Fora dos Limites (Out-of-Bounds Read)
- **O que é**: O programa lê dados além do limite estabelecido do buffer.
- **Impacto**: Vazamento de informações em memória (como chaves criptográficas ou endereços para contornar ASLR).

### 8. Vazamentos de Memória (Memory Leaks)
- **O que é**: Alocações recorrentes no heap sem a correspondente liberação.
- **Impacto**: Esgotamento progressivo de RAM, levando ao travamento do sistema ou finalização pelo OOM Killer.

### 9. Confusão de Tipos (Type Confusion)
- **O que é**: Alocação de memória interpretada sob uma tipagem incompatível em tempo de acesso.
- **Impacto**: Permite adulteração de ponteiros de funções internas ou tabelas de métodos virtuais.

### 10. Condições de Corrida na Memória (TOCTOU / Race Conditions)
- **O que é**: Acesso dessincronizado a dados compartilhados em multithreading, onde a memória é alterada entre a checagem lógica (*time-of-check*) e seu uso real (*time-of-use*).
- **Impacto**: Bypasses de autenticação e corrupção de variáveis críticas.

---

## 🧪 Pipeline Empírico de Validação (Crash-to-Exploitability)

Para analisar vulnerabilidades de corrupção de memória de forma rigorosa, siga este protocolo de validação:

### 1. Gravação e Reprodução (Causa Raiz)
Use ferramentas de gravação determinística de execução, como o **`rr`** no Linux:
- Grave o crash: `rr record ./executavel < payload`
- Reproduza e depure retroativamente: `rr replay`
- Retrocena a instrução de escrita exata que corrompeu o ponteiro ou registrador usando *hardware watchpoints* reverso.

### 2. Validação de Alcance (Reachability)
- Compile a aplicação com instrumentação de cobertura de código (como `gcov`/`lcov` ou flags de profile do Clang).
- Certifique-se de documentar evidências físicas e de cobertura de que o caminho do exploit realmente aciona e passa pela linha de código afetada antes de rotular uma falha como confirmada.

### 3. Matriz de Mitigação Empírica
Compile a prova de conceito sob diferentes perfis para aferir a eficácia de segurança:

| Perfil | Objetivo | Flags de Compilação Críticas |
| :--- | :--- | :--- |
| **Permissive** | O bug básico é explorável? | `-fno-stack-protector -z execstack -no-pie -Wl,-z,norelro` |
| **Distro** | Exploração em ambiente padrão | `-D_FORTIFY_SOURCE=2 -fstack-protector-strong -fPIE -pie -Wl,-z,relro` |
| **Hardened** | Resiliência sob proteções estritas | `-D_FORTIFY_SOURCE=3 -fstack-protector-all -pie -Wl,-z,now -fsanitize=safe-stack` |
| **Sanitized** | Comportamento sob análise dinâmica | `-fsanitize=address,undefined -fno-omit-frame-pointer` |

---

## 🛡️ Mitigações e Defesas Modernas

### 1. Proteções Baseadas em Hardware
- **Memory Tagging Extension (MTE / ARMv8.5+)**: Validação física de chaves (*tags*) associadas a ponteiros, gerando exceções imediatas em caso de mismatch.
- **Pointer Authentication (PAC)**: Criptografia de integridade aplicada a ponteiros de controle e de retorno de chamada de função.
- **Control-flow Enforcement Technology (CET / Intel & AMD)**: Shadow stacks implementadas em hardware para verificação de ROP.

### 2. Proteções Baseadas em Software e Compilador
- **ASLR (Address Space Layout Randomization)**: Randomização dos endereços base de carregamento.
- **DEP / NX (No-Execute)**: Bloqueio de execução de instruções em segmentos de dados (stack e heap).
- **Stack Canaries**: Valores randômicos de guarda verificados antes do retorno de funções.
- **CFI (Control Flow Integrity)**: Validação em runtime de destinos legítimos de jumps indiretos e desvios de controle.

### 3. Proteções de Espaço do Kernel (SMEP & SMAP)
- **SMEP (Supervisor Mode Execution Prevention)**: Impede o kernel de executar códigos do espaço do usuário.
- **SMAP (Supervisor Mode Access Prevention)**: Impede o acesso de leitura/escrita do kernel a dados de páginas de usuário, mitigando sequestro de fluxo de execução em exploits de privilégio local.

---

## 🔒 Diretrizes Globais de Segurança e Conformidade
- Siga estritamente as diretivas estabelecidas no [appsec-owasp-asvs](../../../security/appsec/appsec-owasp-asvs/SKILL.md) e [clean-code-reusability](../../../engineering-practices/clean-code-reusability/SKILL.md).
- Substitua funções e padrões legados inseguros por tipos de alocação de memória gerenciada e abstrações seguras modernas.
