# Exemplo: Table Lookup com Endereçamento Indirect (Panchtilak)

Adaptado de IA-32 (`int 0x80`) para x86_64 NASM (Linux). Demonstra modos de endereçamento direct-offset e indirect para manipulação de arrays, e syscalls `write`/`exit` (números x86_64: 1 e 60).

```nasm
section .data
    msg     db "Values: ", 0
    msg_len equ $ - msg
    newline db 0x0A

    ; Tabelas na seção de dados (direct-offset addressing)
    byte_table  db 14, 15, 22, 45
    word_table  dw 134, 345, 564, 123

section .bss
    ; Buffers estáticos zero-filled (reservados, não inicializados)
    out_buf resb 16

section .text
    global _start

_start:
    ; --- Direct-offset addressing: acessa elementos por índice ---
    movzx   r8, byte [byte_table + 2]   ; 3º elemento (22)
    movzx   r9, word [word_table + 3*2] ; 4º elemento (123)

    ; --- Indirect addressing: base register percorre o array ---
    lea     rbx, [byte_table]           ; effective address em RBX
    mov     rcx, 4                      ; contagem (count register)
.fill_loop:
    mov     al, [rbx]                   ; lê o elemento corrente
    ; (processamento do valor iria aqui)
    add     rbx, 1                      ; avança para o próximo byte
    dec     rcx
    jnz     .fill_loop                  ; loop while CX != 0 (flags)

    ; write(1, msg, msg_len)
    mov     rax, 1                      ; syscall: sys_write
    mov     rdi, 1                      ; fd: stdout
    lea     rsi, [rel msg]
    mov     rdx, msg_len
    syscall

    ; exit(0)
    mov     rax, 60                     ; syscall: sys_exit
    xor     rdi, rdi
    syscall
```

Como montar e executar:

```bash
nasm -f elf64 table_lookup.asm -o table_lookup.o
ld table_lookup.o -o table_lookup
./table_lookup
```

Pontos-chave extraídos do livro:

- **Indirect addressing** usa base registers (`EBX`/`RBX`, `EBP`) e index registers (`ESI`/`EDI`) entre colchetes — ideal para arrays.
- **Direct-offset addressing** (`BYTE_TABLE[2]` ou `BYTE_TABLE + 2`) é gerenciado pela symbol table do assembler.
- `MOVZX` (movimento com zero-extend) evita leituras parciais ao carregar bytes/words em registradores de 64 bits.
- O loop usa `CX`-like counting (`RCX` + `DEC`/`JNZ`), padrão do livro para iteração.