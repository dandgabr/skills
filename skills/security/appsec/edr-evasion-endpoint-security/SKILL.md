---
name: edr-evasion-endpoint-security
description: Especialista em Arquitetura de Defesa de Endpoints (EDR/XDR) e Mecanismos de Evasão/Detecção baseado na obra Evading EDR (Matt Hand). Cobre fontes de telemetria (Kernel Callbacks, ETW, AMSI, API Hooking em ntdll), técnicas de inspeção de pilha (Call Stack Spoofing, Synthetic Frames), Direct/Indirect System Calls e hardening defensivo de agentes EDR.
---

# Defesa de Endpoints e Análise de Mecanismos de Evasão (EDR Security)

Esta skill estabelece o entendimento profundo do funcionamento de soluções de Detecção e Resposta em Endpoints (**EDR**), suas fontes de telemetria, limites arquiteturais e técnicas de engenharia ofensiva/defensiva documentadas na obra **Evading EDR: The Definitive Guide to Defeating Endpoint Detection Systems** de Matt Hand.

---

## 🛡️ 1. Pilares da Telemetria de EDR

```
┌─────────────────────────────────────────────────────────────┐
│ 1. User-Mode Hooking (Inline Patches na ntdll.dll / APIs)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 2. Kernel Callbacks (PsSetCreateProcessNotifyRoutine, etc.) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 3. Event Tracing for Windows (ETW / ETW-Ti no Kernel)       │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 4. AMSI (Antimalware Scan Interface em Scripts/Runtimes)    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔬 2. Mecanismos de Telemetria e Pontos Cego

### A. User-Mode API Hooking
- **Como Funciona**: O EDR injeta uma DLL no processo e insere instruções `JMP` no prólogo das funções da `ntdll.dll` (ex: `NtAllocateVirtualMemory`, `NtWriteVirtualMemory`, `NtCreateThreadEx`) para inspecionar parâmetros antes da execução.
- **Técnicas de Bypass & Detecção**:
  - **Direct Syscalls (Syswhispers/Hell's Gate/Halo's Gate)**: Invocar a instrução `syscall` diretamente no código sem passar pelos hooks da `ntdll`.
  - **Indirect Syscalls**: Saltar para a instrução `syscall; ret` localizada dentro da própria `ntdll.dll` legítima, preservando a assinatura do módulo de origem nos logs de kernel.
  - **Module Unhooking**: Ler uma cópia limpa da seção `.text` da `ntdll.dll` do disco (`\KnownDlls\` ou arquivo físico) e sobrescrever a memória do processo para remover os patches do EDR.

### B. Análise de Pilha de Chamadas (Call Stack Analysis)
- **Synthetic Call Stacks & Spoofing**: EDRs modernos inspecionam o endereço de retorno na pilha. Chamadas diretas de memória anônima (unbacked memory) acionam alertas. Técnicas de Call Stack Spoofing criam frames sintéticos simulando fluxos de execução legítimos (ex: chamando via `RtlUserThreadStart` -> `BaseThreadInitThunk`).

### C. Kernel ETW-Ti (Threat Intelligence)
- Telemetria gerada diretamente do kernel pelo driver EDR inscrito no canal ETW-Ti. Não pode ser desativada a partir do User-Mode sem permissões de driver/kernel.

---

## 📋 3. Matriz de Hardening e Caça a Ameaças

| Vetor de Execução | Telemetria Gerada | Regra de Detecção / Mitigação |
| :--- | :--- | :--- |
| **Alocação de Memória RWX** | `PAGE_EXECUTE_READWRITE` | Alertar sobre transições de memória `PAGE_READWRITE` para `PAGE_EXECUTE_READ` em regiões não mapeadas por DLLs. |
| **Injeção de Processo Remoto** | `OpenProcess` com `PROCESS_VM_WRITE` | Restringir abertura de handles em processos críticos (lsass, svchost) com drivers de kernel e regras PPL (Protected Process Light). |
| **AMSI Patching** | Memória protegida em `amsi.dll` | Monitorar integridade de `AmsiScanBuffer` e interceptar alterações via hardware breakpoints. |
