---
name: zero-trust-architecture-engineering
description: Especialista em Arquitetura e Engenharia de Redes Zero Trust (Zero Trust Networks) baseado na obra de Razi Rais, Christina Morillo e Evan Gilman. Cobre os pilares Never Trust, Always Verify, microsegmentação de rede, autenticação contínua, identidade forte de workloads (SPIFFE/SPIRE), ZTNA (Zero Trust Network Access), controle de acesso adaptativo e criptografia mTLS ponta a ponta.
---

# Engenharia e Arquitetura de Redes Zero Trust (ZTNA)

Esta skill estabelece os princípios de arquitetura **Zero Trust**, superando o modelo tradicional de segurança de perímetro baseado em muralhas e adotando o princípio fundamental: *"Nunca confie, sempre verifique continuamente"*.

---

## 🛡️ 1. Os 5 Pilares do Zero Trust

1. **Identidade Forte de Usuários e Dispositivos**: Autenticação contínua com MFA resistente a phishing (Passkeys/FIDO2) e verificação de postura de segurança do dispositivo (Device Health Attestation).
2. **Identidade de Workload (SPIFFE/SPIRE)**: Toda aplicação, pod ou microsserviço possui um certificado criptográfico X.509 efêmero (SVID) para identificação mutua via mTLS.
3. **Microsegmentação Dinâmica**: Políticas de rede granulares Pod-a-Pod e VM-a-VM que proíbem movimentação lateral não autorizada.
4. **Princípio do Menor Privilégio (PoLP / Just-in-Time Access)**: Acessos temporários concedidos com escopo estritamente necessário.
5. **Telemetria e Análise Contínua**: Monitoramento em tempo real de desvios comportamentais e anomalias de tráfego.
