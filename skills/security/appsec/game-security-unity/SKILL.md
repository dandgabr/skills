---
name: "game-security-unity"
description: "Especialista em segurança para o motor de jogo Unity, cobrindo análise de código C# (Mono vs IL2CPP), engenharia reversa (dnSpy, Il2CppDumper, Ghidra), criptografia de dados, proteção de memória e segurança em rede."
metadata:
  type: offensive
  phase: exploitation
  tools: [dnSpy, Il2CppDumper, Ghidra, IDA Pro, BepInEx, Cheat Engine, GameGuardian, Obfuscar]
  mitre: [T1203, T1068, T1212, T1140, T1055]
---

# Habilidade de IA: Segurança e Hardening em Unity (Unity Game Security)

Esta skill orienta o agente de IA a atuar como especialista em segurança de aplicações e jogos construídos sobre a Unity Engine. Ela abrange a análise de vulnerabilidades comuns do ecossistema, técnicas de engenharia reversa e implementação de defesas e proteções anti-cheat.

---

## 🎯 Objetivo da Skill
Garantir o desenvolvimento de jogos e aplicações Unity seguros, aplicando proteções contra engenharia reversa do código compilado, trapaças na memória (memory editing), roubo de assets e garantindo a segurança de rede e persistência.

## 🛠️ Instruções de Uso para a IA

1. **Contexto de Ativação**:
   - Ative esta skill sempre que trabalhar com arquitetura de código C# em Unity, configurações de compilação (Player Settings), integração de rede ou pacotes anti-cheat.

2. **Passo a Passo de Execução (Ciclo de Hardening)**:
   - **Passo 1 (Análise de Build)**: Verifique se a compilação utiliza IL2CPP. Tente extrair assinaturas do binário usando `Il2CppDumper` para validar a exposição de metadados.
   - **Passo 2 (Teste de Memória)**: Simule varredura de valores críticos (vida, moeda, inventário) na memória usando depuradores ou editores para verificar se os dados estão expostos em texto plano.
   - **Passo 3 (Auditoria de Rede)**: Valide se as ações do jogo dependem de validação do lado do servidor ou se confiam cegamente nos dados enviados pelo cliente.
   - **Passo 4 (Obfuscação e Proteção)**: Sugira obfuscação de código e empacotamento criptografado de assets.

---

## 🗺️ Tabela de Técnicas de Exploração & Mapeamento

| Técnica | MITRE ATT&CK | CWE | Objetivo de Exploração | Ferramentas |
| :--- | :--- | :--- | :--- | :--- |
| **Mono Decompilation** | T1140 | CWE-200 | Decompilação direta para C# limpo | `dnSpy`, `ILSpy` |
| **Metadata Dumping (IL2CPP)**| T1140 | CWE-200 | Extração de classes e métodos do `global-metadata.dat` | `Il2CppDumper`, `Il2CppInspector` |
| **Memory Manipulation** | T1212 | CWE-200 | Alteração de valores de variáveis na RAM em runtime | `Cheat Engine`, `GameGuardian` |
| **Method Hooking** | T1055 | CWE-284 | Injeção e interceptação de métodos em DLLs nativas | `BepInEx`, `Frida` |
| **Asset Ripping** | T1140 | CWE-200 | Extração de modelos 3D, texturas e código compilado | `AssetRipper`, `UABE` |

---

## 🔍 Engenharia Reversa e Vetores de Ataque em Unity

### 1. Compilação Mono vs. IL2CPP
- **Mono**: Compila C# para IL (Intermediate Language) gerando arquivos `.dll` comuns (como `Assembly-CSharp.dll`). Ferramentas como **dnSpy** ou **ILSpy** conseguem decompilar o código-fonte perfeitamente.
- **IL2CPP**: Converte o código IL em código C++ nativo e depois compila para binário de máquina. Gera o executável principal e um arquivo de metadados chamado `global-metadata.dat`.

### 2. Dumps de Metadados (IL2CPP)
- Atacantes usam ferramentas como **Il2CppDumper** para ler o arquivo `global-metadata.dat`. Elas recuperam as assinaturas de métodos e classes, gerando scripts que auxiliam a depuração nativa no **Ghidra** ou **IDA Pro**.

### 3. Edição de Memória
- Modificação de valores brutos armazenados na RAM utilizando scanners de memória como o **Cheat Engine**.

---

## 🛡️ Controles de Hardening e Mitigações

### 1. Proteção de Memória
- Evite armazenar dados sensíveis em tipos primitivos comuns.
- Use padrões de dados obscurecidos (ex: classes wrapper que realizam operações XOR simples ou bitwise shifts sempre que o valor é atualizado ou lido).

### 2. Validação de Rede
- Adote o princípio de **Autoridade do Servidor** usando soluções como *Unity Netcode for GameObjects* ou *Photon*.
- O cliente Unity deve enviar apenas inputs ou intenções de ação (ex: "andar para frente"). O servidor calcula a física e valida a velocidade, posição e permissão do jogador antes de replicar a ação.

### 3. Obfuscação
- Recomende e estruture o uso de ferramentas de obfuscação de código (ex: *Obfuscar*, *Bolt*, *Odin*) para embaralhar os nomes de métodos e variáveis críticos antes da compilação IL2CPP.

### 4. Proteção de Assets (Asset Bundles / Addressables)
- Criptografe pacotes de assets confidenciais antes do empacotamento. Crie gerenciadores de leitura personalizados que descriptografam os dados em memória usando chaves seguras.

### 5. Integração Anti-Cheat
- Integre soluções robustas a nível de kernel ou cliente, como **Easy Anti-Cheat (EAC)**, **BattlEye** ou o *Unity Anti-Cheat* integrado.
