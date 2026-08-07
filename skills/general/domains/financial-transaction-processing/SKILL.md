---
name: "financial-transaction-processing"
description: "Atua como especialista em processamento de transações financeiras e sistemas de pagamentos no Brasil (Pix, SPI, DICT, SPB, Boleto, CIP/Núclea) e no exterior (ISO 20022, SWIFT, FedNow, SEPA, Adquirencia, Gateways, Antifraude, Conciliacao e Idempotencia)."
---

# Habilidade de IA: Especialista em Processamento de Transações Financeiras

Esta skill orienta a inteligência artificial a agir como um **Especialista em Engenharia de Pagamentos e Sistemas Financeiros**, fornecendo arquiteturas de mensageria, protocolos de liquidação bancária no Brasil e no exterior, motores de adquirencia, prevenção à fraude, conciliação e garantia de resiliência transacional.

---

## 🇧🇷 1. Arranjos de Pagamentos e Sistemas Financeiros no Brasil (BCB / SPB)

### 1. Sistema Pix & SPI (Sistema de Pagamentos Instantâneos)
- **Componentes do Arranjo Pix**:
  - **SPI (Sistema de Pagamentos Instantâneos)**: Infraestrutura centralizada mantida pelo Banco Central do Brasil (BCB) para liquidação bruta em tempo real (*RTGS - Real-Time Gross Settlement*) de transferências Pix entre participantes diretos.
  - **DICT (Diretório de Identificadores de Contas Transacionais)**: Base de dados centralizada do BCB que mapeia Chaves Pix (CPF/CNPJ, E-mail, Telefone, Chave Aleatória/EVP) para as contas transacionais dos clientes (ISPB, Agência, Conta).
- **Protocolo de Comunicação e Segurança**:
  - Comunicação via mensagens XML assinadas digitalmente com certificados de segurança de hardware (**ICP-Brasil / RSADSSA-PSS**).
  - Uso de payloads de QR Code no padrão **EMVCo** (Estático e Dinâmico com suporte a JWS / assinatura de carga).
- **Mecanismos de Devolução e Proteção**:
  - **Pix Dev (Devolução)**: Transação acionada pelo usuário recebedor para estornar valores.
  - **MED (Mecanismo Especial de Devolução)**: Procedimento operacional padronizado pelo BCB para congelamento e devolução de valores em casos de fundada suspeita de fraude ou falha operacional no PSP do recebedor.

### 2. SPB (Sistema de Pagamentos Brasileiro) & Registradoras
- **STR (Sistema de Transferência de Reservas)**: Sistema de liquidação em tempo real mantido pelo BCB para operações interbancárias e TEDs (Transferência Eletrônica Disponível).
- **Boleto Bancário & CIP (Núclea)**:
  - Registro obrigatório de boletos na base da CIP/Núclea ou C3.
  - Validação em tempo real de código de barras / linha digitável com busca de dados do sacado e desconto de liquidação.

---

## 🌍 2. Sistemas Globais de Transações Financeiras (Cross-Border & Instant)

### 1. Padrão Mensageria ISO 20022
Padrão internacional em XML/JSON que substitui formatos legados de texto e padroniza a troca de informações financeiras entre instituições financeiras no mundo inteiro:

- **Mensagens Fundamentais (`pacs`, `camt`, `pain`)**:
  - `pacs.008` (Financial Customer Credit Transfer): Instrução de transferência de crédito entre clientes.
  - `pacs.002` (Payment Status Report): Relatório de confirmação, rejeição ou pendência de uma transação.
  - `camt.053` (Bank to Customer Statement): Extrato bancário de conta corrente para conciliação.
  - `pain.001` (Customer Credit Transfer Initiation): Solicitação de transferência iniciada pelo cliente.

### 2. SWIFT & Transferências Internacionais (Cross-Border)
- **Rede SWIFT (Society for Worldwide Interbank Financial Telecommunication)**:
  - Migração de mensagens MT legadas (MT103, MT202) para o padrão **ISO 20022 MX**.
  - **SWIFT gpi (Global Payments Innovation)**: Rastreamento em tempo real com transparência de taxas e confirmação de crédito imediato na ponta final via *Unique End-to-End Transaction Reference (UETR)*.

### 3. Redes de Pagamentos Instantâneos Internacionais
- **FedNow (Federal Reserve System - EUA)**: Infraestrutura de pagamentos instantâneos 24/7/365 nos Estados Unidos baseada em ISO 20022.
- **SEPA Instant Credit Transfer (SCT Inst - União Europeia)**: Transferências instantâneas em euros entre contas do espaço SEPA em menos de 10 segundos.

---

## 💳 3. Adquirencia, Gateways e Processamento de Cartões

### 1. O Fluxo da Transação de Cartão (Ciclo de 4 Partes)

```text
  Portador do Cartão  --->  Estabelecimento (POS / E-commerce)
                                        |
                                        v
                                 Gateway / Subadquirente
                                        |
                                        v
                                    Adquirente (Cielo, Rede, Stone, etc.)
                                        |
                                        v
                                 Bandeira (Visa, Mastercard, Elo)
                                        |
                                        v
                                  Banco Emissor
```

### 2. Protocolo ISO 8583 (Mensageria Financeira de Cartão)
- **MTI (Message Type Identifier)**:
  - `0100`: Solicitação de Autorização (*Authorization Request*).
  - `0110`: Resposta de Autorização (*Authorization Response*).
  - `0200`: Transação Financeira / Captura (*Financial Transaction Request*).
  - `0400`: Estorno / Reversão (*Reversal Request*).
- **Campos Principais (Data Elements / Bitmaps)**:
  - DE-3 (Processing Code), DE-4 (Amount), DE-11 (SYSTEM Trace Audit Number - STAN), DE-39 (Response Code - Ex: `00` Aprovada, `51` Margem Insuficiente, `05` Não Honrar), DE-55 (Dados EMV / Chip ICC).

### 3. Motores de Antifraude e Risco
- **3D Secure 2.0 (EMV 3DS)**: Autenticação silenciosa de cliente baseada em dados contextuais (Dispositivo, Geolocalização, Histórico) enviada ao Emissor para evitar fricção no checkout.
- **Score de Risco & Regras de Decisão**: Análise pré-autorização via modelos de ML (detecção de velocidade de cartões, bin attack, proxy/VPN suspeito, fingerprinting).

---

## 🔄 4. Resiliência Criptográfica, Conciliação e Arquitetura

### 1. Idempotência Estrita
Garantia de que requisições duplicadas enviadas por falha de rede nunca resultem em débitos em duplo:

```json
// Header de requisição obrigatório na API de Pagamento
HTTP/1.1 POST /v1/payments
Idempotency-Key: 7b9e83c2-84b1-4c6e-821a-298317a9412d
```

- **Motor de Idempotência**: Bloqueio concorrente em Redis/Cache com verificação de payload hash e chave de idempotência. Se a requisição já foi processada, o resultado anterior é retornado imediatamente sem reenviar a transação ao adquirente/banco.

### 2. Motor de Conciliação Financeira (Financial Reconciliation)
- **Tríplice Conciliação**:
  1. *Conciliação de Vendas*: Comparação entre Pedidos da Aplicação vs Transações Aprovadas no Gateway.
  2. *Conciliação de Recebíveis*: Comparação entre Vendas Aprovadas no Gateway vs Arquivos de Edi/MDR das Adquirentes (ex: Arquivo 200/Vendas, 202/Ajustes, 204/Pagamentos).
  3. *Conciliação Bancária*: Comparação entre Pagamentos Prometidos pelas Adquirentes vs Extrato Real de Conta Corrente (camt.053 / OFX).

### 3. Padrão SAGA e Compensação Distribuída
- Implementação de arquitetura SAGA orquestrada/coreografada para fluxos financeiros com múltiplos passos (Reservar Saldo -> Processar Cartão -> Confirmar Estoque -> Efetivar Débito).
- Execução de transações de compensação (Cancelamento/Estorno) automáticas em caso de falhas intermediárias.

---

## ⚙️ Protocolo de Decisão do Engenheiro de Transações Financeiras

1. **Exija Idempotência na Camada de API**: Nenhuma rota de pagamento ou transferência pode ser aceita sem uma chave de idempotência válida.
2. **Separe Autorização de Captura**: Para vendas de e-commerce e serviços que dependem de validação de estoque, utilize Autorização prévia e Captura posterior (*Two-Step Authorization*).
3. **Audite os Códigos de Resposta ISO 8583 / Pix**: Mapeie de forma unificada as rejeições de pagamentos diferenciando falhas humanas (saldo insuficiente), falhas operacionais (timeout) e bloqueios de segurança (fraude).

---

## 🔗 Integração com Outras Skills

- Para adequação de ambiente a normas de segurança de cartões de crédito e escopo CDE, consulte a skill [pci-dss-compliance](../../../security/grc-compliance/pci-dss-compliance/SKILL.md).
- Para assinaturas digitais RSADSSA-PSS e encriptação de payloads Pix/SPB, consulte a skill [cryptography-pqc-standards](../../../security/crypto-pki/cryptography-pqc-standards/SKILL.md).
- Para desenvolvimento de APIs REST resilientes e microsserviços de pagamento, consulte a skill [backend-developer](../../roles/backend-developer/SKILL.md).
