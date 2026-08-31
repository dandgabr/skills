# Assembly Fundamentals — Guia para Iniciantes (Panchtilak, Kavishankar)

Consolidado da obra *Assembly Programming Language For Beginners — Learn Assembly Programming Language* (Panchtilak, Kavishankar). O livro cobre os fundamentos de Assembly IA-32/x86 com NASM em Linux: arquitetura de memória segmentada, registradores, flags, modos de endereçamento, instruções essenciais, syscalls `int 0x80`, procedures, stack, recursion, macros, strings, file I/O e alocação dinâmica com `sys_brk`.

> **Nota de adaptação para x86_64**: os exemplos do livro usam a interface IA-32 (`int 0x80`, registradores de 32 bits). Em x86_64, os fundamentos são os mesmos, mas use a interface `syscall` (números e convenções diferem — ver SKILL.md principal). Os conceitos (flags, modos de endereçamento, stack, procedures) transpõem diretamente.

---

## 1. Modelo de Memória (Segments)

O programa assembly organiza a memória em três segmentos:

| Segmento | Seção NASM | Característica |
| :--- | :--- | :--- |
| **Data segment** | `.data` | Estático; elementos de dados declarados; não pode ser expandido after the fact |
| **BSS** | `.bss` | Buffers estáticos **zero-filled** para dados declarados mais tarde (`resb`, `resw`, `resd`) |
| **Code segment** | `.text` | Área fixa com instruções |
| **Stack** | (implícito) | Valores passados a funções/procedures |

---

## 2. Registradores (IA-32 / x86)

O livro agrupa os registradores em **gerais**, **de controle** e **de segmento**:

- **Data registers** (32/16/8 bits): `EAX/AX/AL/AH`, `EBX/BX/BL/BH`, `ECX/CX/CL/CH`, `EDX/DX/DL/DH`:
  - `AX` — primary accumulator (E/S e aritmética em geral);
  - `BX` — base register (endereçamento indexado);
  - `CX` — count register (loops, `LOOP`);
  - `DX` — data register (E/S; par `DX:AX` em multiply/divide com valores grandes).
- **Pointer registers**: `EIP/IP` (instruction pointer — offset da próxima instrução, com `CS:IP`), `ESP/SP` (stack pointer, com `SS:SP`), `EBP/BP` (base pointer — referência a parâmetros de subroutines).
- **Index registers**: `ESI/SI` (source index — operações de string) e `EDI/DI` (destination index).
- **Segment registers**: `CS` (code), `DS` (data), `SS` (stack), `ES` (extra).

---

## 3. Flags do CPU (Control Registers)

O registrador de flags registra o estado de cada operação aritmética/lógica:

| Flag | Papel |
| :--- | :--- |
| **OF** (Overflow) | Overflow do bit de ordem alta em operação **com sinal** |
| **DF** (Direction) | Direção de movimentação de strings (`0` = esquerda→direita; `cld`/`std`) |
| **IF** (Interrupt) | Trata/ignora interrupções externas (`sti`/`cli`) |
| **TF** (Trap) | Modo single-step (debug) |
| **SF** (Sign) | Sinal do resultado (bit mais significativo) |
| **ZF** (Zero) | Resultado zero (comparações: `CMP`/`TEST` setam ZF) |
| **AF** (Auxiliary Carry) | Carry do nibble (BCD) |
| **PF** (Parity) | Paridade do resultado |
| **CF** (Carry) | Carry/borrow do bit de ordem alta em operação **sem sinal** |

Padrões idiomáticos do livro:
- `XOR EAX, EAX` — zera o registrador (e limpa CF para `LODSD`/aritmética longa);
- `TEST AL, 01H` + `JZ EVEN_NUMBER` — testa o bit menos significativo para paridade;
- `CMP AL, BL` + `JE EQUAL` — comparação que produz desvio condicional.

---

## 4. Modos de Endereçamento

| Modo | Descrição | Exemplo (NASM) |
| :--- | :--- | :--- |
| **Register** | Operandos apenas em registradores — processamento **mais rápido** (sem acesso à memória) | `MOV EAX, EBX` |
| **Immediate** | Segundo operando é constante; o primeiro define o tamanho | `ADD BYTE_VALUE, 65` |
| **Direct memory** | Offset embutido na instrução (nome da variável); o assembler mantém a symbol table | `MOV BX, WORD_VALUE` |
| **Direct-offset** | Operadores aritméticos modificam o endereço (indexação de tabelas) | `MOV CL, BYTE_TABLE[2]` ou `BYTE_TABLE + 2` |
| **Indirect memory** | Base/index registers entre colchetes (`EBX`, `EBP`, `SI`, `DI`); típico para arrays | `MOV EBX, [MY_TABLE]` / `MOV [EBX], 110` / `ADD EBX, 2` |

Tamanhos de dados NASM: `DB` (byte, 1), `DW` (word, 2), `DD` (dword, 4), `DQ` (qword, 8), `DT` (tbyte, 10); reservas com `TIMES`/`RESB` series. Constantes com `EQU`:

```nasm
MY_TABLE TIMES 10 DW 0   ; 10 words inicializadas a 0
MOV EBX, [MY_TABLE]      ; effective address
MOV [EBX], 110           ; MY_TABLE[0] = 110
ADD EBX, 2               ; EBX = EBX + 2
MOV [EBX], 123           ; MY_TABLE[1] = 123
```

---

## 5. Instruções Essenciais

- **MOV** — copia dados entre registradores/memória/imediato.
- **Aritmética**: `ADD`/`SUB`/`INC`/`DEC`; `MUL`/`IMUL` (unsigned/signed — `MOV AL, 10` + `MOV DL, 25` + `MUL DL`); `DIV`/`IDIV`; aritmética BCD com `AAA`/`AAS`/`AAM`/`AAD`/`DAA`/`DAS`.
- **Lógicos**: `AND`, `OR`, `XOR`, `NOT`, `TEST` (AND sem armazenar resultado — para flags).
- **Desvio condicional** (baseado no status flags): `JZ`/`JE`, `JNZ`/`JNE`, `JG`/`JGE` (signed), `JA`/`JAE` (unsigned), `JL`/`JLE`, `JB`/`JBE`, `JC`, `JOF` etc.
- **Loop**:

```nasm
MOV CL, 10
L1:
  ; loop body
  DEC CL        ; (ou LOOP L1, que decrementa CX e salta se != 0)
  JNZ L1
```

- **Strings** (com pares `DS:SI` origem / `ES:DI` destino e sufixos B/W/D):

| Instrução | Operação | Sufixos |
| :--- | :--- | :--- |
| `MOVS` | Move byte/word/dword de memória para memória | `MOVSB/W/D` |
| `LODS` | Carrega da memória para `AL/AX/EAX` | `LODSB/W/D` |
| `STOS` | Armazena de `AL/AX/EAX` para memória | `STOSB/W/D` |
| `CMPS` | Compara dois itens em memória | `CMPSB/W/D` |
| `SCAS` | Compara `AL/AX/EAX` com item em memória | `SCASB/W/D` |

  Prefixos de repetição: `REP`, `REPE`/`REPZ`, `REPNE`/`REPNZ` (combinam com `CX` e DF — ex.: `REP STOSD` usado no exemplo de alocação de memória, precedido de `STD`/`CLD`).

---

## 6. Procedures, Stack e Recursion

- **Procedure**: bloco nomeado finalizado com `RET`, chamado via `CALL proc_name`.

```nasm
sum:
    mov eax, ecx
    add eax, edx
    add eax, '0'
    ret
```

- **Stack (LIFO)**: `PUSH`/`POP` usando `SS:ESP`. O stack é usado para salvar/restaurar registradores, passar parâmetros e retornar endereços.
- **Recursion**: cada chamada recursiva empilha contexto próprio; exige **condição de término** (ex.: `Fact(n) = n * fact(n-1)` para `n > 0`, terminando em `n == 0`).

---

## 7. Macros

Mecanismo de modularização: sequência de instruções atribuída a um nome, expandida textualmente em cada uso (diferentemente de procedures, que são chamadas/jumped).

---

## 8. Linux System Calls (`int 0x80`)
Passos do livro (IA-32):

```nasm
1. Número da syscall em EAX
2. Argumentos em EBX, ECX, EDX, ESI, EDI, EBP (ordem consecutiva)
3. Interrupção: int 0x80
4. Resultado (código de retorno) em EAX
```

Mais de seis argumentos: `EBX` guarda o ponteiro de memória do primeiro argumento.

| EAX | Syscall | EBX | ECX | EDX | ESI | EDI |
| :-- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `sys_exit` | int (status) | – | – | – | – |
| 2 | `sys_fork` | `struct pt_regs *` | – | – | – | – |
| 3 | `sys_read` | `unsigned int` (fd) | `char *` (buf) | `size_t` | – | – |
| 4 | `sys_write` | `unsigned int` (fd) | `const char *` | `size_t` | – | – |
| 5 | `sys_open` | `const char *` | int (flags) | int (mode) | – | – |
| 6 | `sys_close` | `unsigned int` (fd) | – | – | – | – |

Exemplo de leitura + escrita:

```nasm
; leitura (sys_read = 3)
MOV ECX, num
MOV EDX, 5
INT 80H
; escrita (sys_write = 4)
MOV ECX, dispMsg
MOV EDX, lenDispMsg
INT 80H
```

A lista completa de syscalls fica em /usr/include/asm/unistd.h.

---

## 9. File Handling (syscalls)

Criar/abrir (`sys_creat` nº 8, `sys_open` nº 5), escrever (`sys_write` nº 4), fechar (`sys_close` nº 6):

```nasm
; criação: EAX=8, EBX=filename, ECX=permissões (ex.: 0377 octal)
; escrita: EAX=4, EBX=fd, ECX=buffer, EDX=comprimento
; fechamento: EAX=6, EBX=fd
```

---

## 10. Gerenciamento de Memória (`sys_brk`)

`sys_brk` (syscall nº 45) aloca memória **imediatamente após a imagem do aplicativo**, definindo o endereço mais alto da seção de dados; recebe o endereço em `EBX` e retorna `-1` ou o código de erro negativo em caso de falha.

```nasm
MOV EAX, 45        ; sys_brk
XOR EBX, EBX
INT 80H            ; endereço atual
ADD EAX, 16384     ; + 16 KB
MOV EBX, EAX
MOV EAX, 45
INT 80H            ; nova quebra definida
```

Fill do bloco com `REP STOSD` (com `STD`/`CLD` para direção).

---

Fonte completa: arquivo convertido em `/tmp/opencode/books/full/Assembly Programming Language For Beginners ...` (para extração de novos detalhes, se necessário).