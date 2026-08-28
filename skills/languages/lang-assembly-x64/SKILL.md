---
name: lang-assembly-x64
description: Fornece padrões de engenharia de software e programação em Assembly x86_64 (Linux POSIX e Windows x64) baseado na obra The Assembly Language Reimagined (John Schwartzman). Cobre sintaxe Intel e AT&T, registradores de uso geral e SIMD (AVX/SSE), chamadas de sistema diretas (syscalls), System V AMD64 ABI, manipulação de pilha e otimização de baixo nível.
---

# Engenharia em Assembly x86_64 (Intel 64 / AMD64)

Esta skill estabelece diretrizes e convenções de código limpo para desenvolvimento em **Assembly x86_64** (NASM/Yasm e GCC/GAS), cobrindo registradores, convenções de chamada de funções (ABIs), manipulação de ponteiros e chamadas de sistema no Linux.

---

## 💻 1. Registradores da Arquitetura x86_64

| 64-bit | 32-bit | 16-bit | 8-bit (Low/High) | Papel na System V ABI (Linux) |
| :--- | :--- | :--- | :--- | :--- |
| `rax` | `eax` | `ax` | `al` / `ah` | Valor de retorno de funções / Syscall Number |
| `rdi` | `edi` | `di` | `dil` | 1º Argumento de função |
| `rsi` | `esi` | `si` | `sil` | 2º Argumento de função |
| `rdx` | `edx` | `dx` | `dl` / `dh` | 3º Argumento de função |
| `rcx` | `ecx` | `cx` | `cl` / `ch` | 4º Argumento de função (ou `r10` em syscalls) |
| `r8`  | `r8d` | `r8w`| `r8b` | 5º Argumento de função |
| `r9`  | `r9d` | `r9w`| `r9b` | 6º Argumento de função |
| `rsp` | `esp` | `sp` | `spl` | Stack Pointer (Ponteiro do topo da pilha) |
| `rbp` | `ebp` | `bp` | `bpl` | Base Pointer (Ponteiro do frame da função) |

---

## 🛠️ 2. Exemplo: Hello World Puro em NASM (Linux Syscalls)

```nasm
section .rodata
    msg db "Hello, x86_64 Assembly!", 0x0A
    len equ $ - msg

section .text
    global _start

_start:
    ; write(1, msg, len)
    mov rax, 1          ; syscall: sys_write
    mov rdi, 1          ; fd: stdout
    lea rsi, [rel msg]  ; buffer address (Position-Independent)
    mov rdx, len        ; count
    syscall

    ; exit(0)
    mov rax, 60         ; syscall: sys_exit
    xor rdi, rdi        ; status: 0
    syscall
```
