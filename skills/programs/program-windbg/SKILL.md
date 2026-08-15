---
name: program-windbg
description: Automates and executes commands in WinDbg (Windows Debugger) and captures output using cdb and native dbgeng.dll.
---

# program-windbg

A skill `program-windbg` permite automatizar e interagir com o depurador WinDbg (Windows Debugger) e com o motor de depuração do Windows. Ela fornece tanto uma interface nativa de alto desempenho via `dbgeng.dll` (através de chamadas COM em Python/ctypes) quanto uma automação robusta baseada em subprocessos do console de depuração do WinDbg (`cdb.exe`).

Esta skill é ideal para:
- Automatizar análise de crash dumps (`.dmp`).
- Depurar processos ativos (attach) e executar comandos como `k` (call stack), `lm` (loaded modules), `r` (registers), e análises automáticas (`!analyze -v`).
- Monitorar exceções e eventos em processos de destino.

## Requisitos

1. **WinDbg (Windows Kits / Windows SDK ou Microsoft Store version)** instalado.
2. Caminho de execução configurado ou acessível. A biblioteca `dbgeng.dll` padrão do Windows em `C:\Windows\System32\dbgeng.dll` é carregada automaticamente para as APIs nativas.
3. Privilégios de Administrador são altamente recomendados para depuração de processos ativos no sistema.

## Instalação da Estrutura

Esta skill está localizada na seguinte pasta:
`B:\Code\skills\skills\programs\program-windbg`

## Como Usar o Script

O script `program-windbg.py` pode ser executado via linha de comando:

```bash
# Executar comando em um processo ativo (por PID)
python program-windbg.py --pid 1234 --command "k; q"

# Executar análise automática em um arquivo de Crash Dump (.dmp)
python program-windbg.py --dump "C:\caminho\dump.dmp" --command "!analyze -v; q"

# Iniciar um novo processo sob o depurador
python program-windbg.py --exec "notepad.exe" --command "g; lm; q"
```

## Arquitetura da Skill

A skill suporta dois modos de operação:
1. **Modo Native API (`dbgeng.dll`)**: Interage diretamente com a API COM do motor do Windows Debugger através de ctypes em Python. Suporta carregamento dinâmico de símbolos, execução assíncrona de comandos e manipulação de eventos de depuração em memória sem criar processos adicionais de console.
2. **Modo CLI CDB (`cdb.exe`)**: Encapsula chamadas ao `cdbX64.exe` / `cdbX86.exe` (Console Debugger), enviando os comandos via STDIN e capturando todo o output de forma limpa e estruturada.
