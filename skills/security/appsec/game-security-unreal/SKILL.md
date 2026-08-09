---
name: "game-security-unreal"
description: "Especialista em segurança para o motor de jogo Unreal Engine, cobrindo segurança em replicação de rede (RPCs), proteção de arquivos .pak, desativação de comandos de console, hardening C++ e anti-cheats."
metadata:
  type: offensive
  phase: exploitation
  tools: [Cheat Engine, IDA Pro, Ghidra, x64dbg, Fiddler, Wireshark, DefaultEncryption.ini]
  mitre: [T1203, T1068, T1055, T1040, T1565]
---

# Habilidade de IA: Segurança e Hardening em Unreal Engine (Unreal Game Security)

Esta skill capacita o agente de IA a projetar e auditar segurança em jogos desenvolvidos com Unreal Engine (C++ e Blueprints), focando em integridade de memória, replicação segura em arquiteturas cliente-servidor e proteção de dados proprietários.

---

## 🎯 Objetivo da Skill
Prevenir trapaças (cheating), engenharia reversa de blueprints/binários C++, extração de assets protegidos de arquivos `.pak` e abusos de lógica em jogos multiplayer baseados na Unreal Engine.

## 🛠️ Instruções de Uso para a IA

1. **Contexto de Ativação**:
   - Ative esta skill ao analisar códigos C++ em UE (ex: `UFUNCTION(Server, Reliable, WithValidation)`), estruturas de replicação de dados, manipulação de arquivos de configuração (.ini) e exportação de builds finais.

2. **Passo a Passo de Execução (Ciclo de Validação)**:
   - **Passo 1 (Auditoria de RPCs)**: Identifique todas as funções do tipo `Server` em C++ ou Blueprints. Verifique se possuem rotinas de validação de dados e física correspondentes.
   - **Passo 2 (Verificação de Pak)**: Tente extrair recursos da build final utilizando desempacotadores públicos de arquivos `.pak`. Certifique-se de que a criptografia AES está ativada.
   - **Passo 3 (Verificação de Hardening)**: Valide se flags de compilação como `UE_BUILD_SHIPPING` estão habilitadas, removendo comandos de depuração internos.
   - **Passo 4 (Controle de Símbolos)**: Confirme que os arquivos de depuração (`.pdb`) não estão sendo distribuídos com a build do cliente.

---

## 🗺️ Tabela de Técnicas de Exploração & Mapeamento

| Técnica | MITRE ATT&CK | CWE | Objetivo de Exploração | Ferramentas |
| :--- | :--- | :--- | :--- | :--- |
| **RPC Parameter Injection** | T1565 | CWE-20 | Execução de ações inválidas sem validação do servidor | `Cheat Engine`, Injetores Customizados |
| **Pak Key Dumping** | T1140 | CWE-200 | Descriptografia e extração de assets do jogo | `IDA Pro`, `x64dbg` |
| **GNames/GUObject Scanning** | T1212 | CWE-200 | Identificação de instâncias de classes na memória RAM | `Cheat Engine`, Memory Scanners |
| **Console Injection** | T1055 | CWE-284 | Acesso a cheats nativos habilitados em runtime | Injetores de DLL |
| **Network Sniffing** | T1040 | CWE-200 | Interceptação de dados trocados via protocolo UDP da UE | `Wireshark` |

---

## 🔍 Engenharia Reversa e Vulnerabilidades em Unreal

### 1. RPCs sem Validação
- Se uma função executada no servidor (como `ServerDamageEnemy`) não for validada pelo servidor (`WithValidation`), o cliente pode forçar parâmetros falsos, permitindo matança instantânea de inimigos (instakill).

### 2. Desempacotamento de Arquivos .pak
- Unreal empacota assets em arquivos `.pak`. Sem criptografia AES-256 ativa, atacantes extraem modelos 3D, texturas e códigos das Blueprints compiladas.

### 3. Modificações de Memória
- Sendo baseada em C++, atacantes vasculham a RAM em busca de tabelas globais (GNames e GUObjectArray) para localizar objetos e instâncias de atores em tempo de execução para aplicar modificações na física (ex: voar, atravessar paredes).

---

## 🛡️ Controles de Hardening e Mitigações

### 1. Criptografia Integrada (.pak)
- Habilite a criptografia de arquivos `.pak` no arquivo `Config/DefaultEncryption.ini`.
- Use chaves AES de 256 bits geradas de forma pseudo-aleatória.
- Remova e oculte chaves estáticas da memória assim que o processo de montagem de arquivos for concluído na inicialização.

### 2. Validação Estrita de Rede (Replication Security)
- Sempre implemente a validação C++ nos métodos de RPC:
  ```cpp
  // No cabeçalho (.h)
  UFUNCTION(Server, Reliable, WithValidation)
  void Server_RequestMove(FVector NewLocation);

  // Na implementação (.cpp)
  bool AMyCharacter::Server_RequestMove_Validate(FVector NewLocation)
  {
      // Validar se o cliente não está se movendo rápido demais (Speedhack check)
      float Distance = FVector::Dist(GetActorLocation(), NewLocation);
      return Distance <= MaxAllowedDistanceStep;
  }

  void AMyCharacter::Server_RequestMove_Implementation(FVector NewLocation)
  {
      SetActorLocation(NewLocation);
  }
  ```

### 3. Proteção Contra Console Commands
- Verifique se a flag de compilação `UE_BUILD_SHIPPING` está habilitada no script de build. Isso remove automaticamente comandos de depuração integrados e o console do desenvolvedor (`~`).
