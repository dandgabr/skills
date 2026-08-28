---
name: windows-internals-security
description: Especialista em Arquitetura Interna do Windows e Engenharia de Segurança baseado nas obras Windows Security Internals (James Forshaw) e Windows Internals Part 2 (Mark Russinovich). Cobre Security Tokens, Access Control (DACL/SACL, SIDs, Privilégios), Security Reference Monitor (SRM), IPC (ALPC, RPC, Named Pipes), LSASS, Kerberos/NTLM e autenticação via PowerShell.
---

# Arquitetura Interna e Segurança do Windows (Windows Internals)

Esta skill estabelece os fundamentos de arquitetura de segurança do sistema operacional Microsoft Windows, abordando o modelo de objetos do kernel, subsistema de segurança (**SRM/LSASS**) e controle de acesso baseado nas obras de **James Forshaw** e **Mark Russinovich**.

---

## 🏛️ 1. Arquitetura do Subsistema de Segurança do Windows

```
┌─────────────────────────────────────────────────────────────┐
│                       User Mode                             │
│  [ Processos / Apps ]  ──>  [ LSASS (Local Security Auth) ] │
│                                  │ (LSA Authentication)     │
└──────────────────────────────────┼──────────────────────────┘
                                   │ NtAccessCheck
┌──────────────────────────────────▼──────────────────────────┐
│                      Kernel Mode                            │
│  [ Security Reference Monitor (SRM) ]  <──> [ Objeto Kernel]│
│  (Valida Token contra Security Descriptor)   (DACL / SACL)  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔑 2. Estrutura do Security Token e Controle de Acesso

### A. Elementos de um Access Token (Token de Acesso)
- **User SID**: Identificador único de segurança do usuário.
- **Group SIDs**: Grupos aos quais o usuário pertence (ex: `S-1-5-32-544` para Administradores).
- **Privilégios (Privileges)**: Direitos operacionais do sistema (ex: `SeDebugPrivilege`, `SeImpersonatePrivilege`, `SeBackupPrivilege`).
- **Integrity Level (Nível de Integridade)**: Untrusted, Low (Sandbox/Browser), Medium (Usuário padrão), High (Admin elevado), System (Kernel/SYSTEM).

### B. Security Descriptor (Descritor de Segurança)
- **Owner SID** e **Group SID**.
- **DACL (Discretionary Access Control List)**: Lista de ACEs (Access Control Entries) que concedem ou negam acesso a sujeitos específicos.
- **SACL (System Access Control List)**: Controla auditoria e geração de logs de eventos de segurança.

---

## 📡 3. Comunicação Interprocesso Segura (IPC)
- **ALPC (Advanced Local Procedure Call)**: Transporte de alta performance no kernel para comunicação rápida entre processos locais (usado intensamente por LSASS, RPC e CSRSS).
- **RPC (Remote Procedure Call)**: Comunicação entre máquinas e processos locais com autenticação Kerberos/NTLM e níveis de autenticação (`RPC_C_AUTHN_LEVEL_PKT_PRIVACY` para encriptação).
