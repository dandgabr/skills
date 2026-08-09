---
name: "game-security-godot"
description: "Especialista em segurança para o motor de jogo Godot Engine, cobrindo proteção de arquivos .pck, criptografia AES, descompilação de GDScript (GDRETools), templates de exportação customizados e segurança de rede."
metadata:
  type: offensive
  phase: exploitation
  tools: [GDRETools, gdsdecomp, IDA Pro, Ghidra, x64dbg, SCons, Cheat Engine]
  mitre: [T1203, T1068, T1140, T1055, T1212]
---

# Habilidade de IA: Segurança e Hardening em Godot Engine (Godot Game Security)

Esta skill orienta o agente de IA a garantir a segurança e a integridade de jogos e aplicações criadas com o Godot Engine. Ela cobre a proteção contra engenharia reversa de scripts GDScript, criptografia de pacotes `.pck`, segurança de rede e sanitização de dados.

---

## 🎯 Objetivo da Skill
Evitar a descompilação e modificação de scripts de jogabilidade, extração de código e ativos do pacote principal do jogo (`.pck`/`.zip`), e assegurar a confiabilidade em comunicações cliente-servidor.

## 🛠️ Instruções de Uso para a IA

1. **Contexto de Ativação**:
   - Ative esta skill ao desenvolver ou auditar jogos usando Godot Engine (GDScript, C# ou C++ via GDExtension), configurando pipelines de exportação e projetando o backend de rede.

2. **Passo a Passo de Execução (Ciclo de Hardening)**:
   - **Passo 1 (Auditoria de PCK)**: Execute ferramentas de extração como o `GDRETools` sobre o executável exportado. Se conseguir extrair os scripts legíveis em texto plano, reforce a criptografia.
   - **Passo 2 (Verificação de Chaves)**: Use scanners de memória e descompiladores para verificar se a chave AES usada na criptografia do PCK pode ser facilmente extraída do executável.
   - **Passo 3 (Análise de Script)**: Identifique lógicas críticas de segurança escritas em GDScript e recomende migrá-las para C++ nativo usando GDExtension.
   - **Passo 4 (Auditoria de Rede)**: Verifique se as comunicações RPC de rede estão adequadamente sob a autoridade do servidor e se os pacotes enviados são validados.

---

## 🗺️ Tabela de Técnicas de Exploração & Mapeamento

| Técnica | MITRE ATT&CK | CWE | Objetivo de Exploração | Ferramentas |
| :--- | :--- | :--- | :--- | :--- |
| **PCK Package Extraction** | T1140 | CWE-200 | Extração de assets originais e scripts interpretados | `GDRETools` |
| **GDScript Bytecode Decompilation**| T1140 | CWE-200 | Conversão de arquivos `.gdc`/`.gde` para código legível | `GDRETools`, `gdsdecomp` |
| **AES Key Extraction (RAM)** | T1212 | CWE-200 | Dump da chave AES-256 usada para carregar o `.pck` | `x64dbg`, `GDB`, `Cheat Engine` |
| **GDExtension Reverse Engineering**| T1203 | CWE-120 | Análise de binários compilados dinâmicos nativos | `IDA Pro`, `Ghidra` |
| **RPC Network Injection** | T1055 | CWE-20 | Manipulação de chamadas do MultiplayerAPI do Godot | Depuradores de Rede |

---

## 🔍 Engenharia Reversa e Vetores de Ataque em Godot

### 1. Descompilação de GDScript e Extração de PCK
- Por padrão, o Godot compila scripts GDScript em bytecode `.gdc` e os armazena no pacote `.pck`. Ferramentas como o **GDRETools** descompilam perfeitamente de volta para o código-fonte original, expondo a lógica inteira do jogo.

### 2. Contorno de Criptografia PCK Estática
- Godot suporta criptografia de arquivos `.pck` com AES-256. Contudo, a chave de criptografia de 256 bits deve estar presente no binário do executável exportado para decodificar os assets em tempo de execução. Depuradores (GDB, x64dbg) ou varredura de memória localizam essa chave durante a inicialização do jogo.

---

## 🛡️ Controles de Hardening e Mitigações

### 1. Compilação de Export Templates Personalizados
- Em vez de usar os export templates padrão, compile seus próprios templates de exportação a partir dos fontes do Godot.
- Insira uma chave secreta e algoritmo personalizado diretamente no código-fonte do motor (em `core/io/file_access_pack.cpp`) antes de compilar com SCons. Descompiladores padrão falharão em ler seu jogo.

### 2. Uso de GDExtension / C++
- Escreva a lógica de segurança crítica do jogo (ex: checagem de conquistas, validação de compras, criptografia) em C++ usando **GDExtension** em vez de GDScript.
- O código compilado em C++ vira uma biblioteca dinâmica nativa (`.dll`, `.so`), cuja análise e descompilação são exponencialmente mais trabalhosas.

### 3. Proteção e Comunicação em Rede
- Garanta que a autoridade do jogo esteja no servidor (Server-Side Authority).
- Valide inputs no servidor e sanitize dados que entram via MultiplayerAPI da Godot. Use conexões seguras (SSL/TLS ou encriptação nativa do ENet).
