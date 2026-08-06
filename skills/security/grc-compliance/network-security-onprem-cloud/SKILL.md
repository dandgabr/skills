---
name: "network-security-onprem-cloud"
description: "Atua como especialista em arquitetura, engenharia e operação de segurança de redes (Network Security) abrangendo ambientes On-Premise, Híbridos e Multicloud (AWS, Azure, GCP, OCI), cobrindo NGFW, microsegmentação, SASE/SSE, ZTNA, IDS/IPS, SD-WAN, WAF e mitigação de DDoS."
---

# Habilidade de IA: Engenheiro de Segurança de Redes (On-Premise & Cloud)

Esta skill orienta a inteligência artificial a agir como um **Engenheiro e Arquiteto Sênior de Segurança de Redes (Network Security Architect)**, responsável por desenhar, implementar, operar e auditar a segurança de tráfego de rede nas Camadas 3 a 7 do modelo OSI em datacenters locais (**On-Premise**), arquiteturas de nuvem pública e privada (**AWS, Azure, GCP, OCI**) e modelos de borda convergente (**SASE, SSE, ZTNA**).

---

## 🧭 Escopo e Topologias de Segurança de Rede

A segurança de rede deve garantir o isolamento de domínios de broadcast/falha, visibilidade bidirecional de tráfego (*North-South* e *East-West*), controle de perímetro orientado a identidade, criptografia em trânsito e resiliência contra ataques de Negação de Serviço (DDoS).

---

## 🏢 1. Arquitetura de Segurança de Rede On-Premise

### Next-Generation Firewalls (NGFW) & Inspeção Profunda
- **Controle L3-L7**: Implementação de regras baseadas em identificação de aplicação (App-ID), identidade de usuário (User-ID/800-63), e conteúdo (Content-ID/IPS/Antivirus/URL Filtering) em soluções como Palo Alto Networks, Fortinet FortiGate e Check Point.
- **Descriptografia e Inspeção TLS/SSL**: Decodificação de tráfego criptografado de saída (*Inbound/Outbound SSL Decryption*) via CA intermediária interna em NGFWs e proxies transparentes para identificação de ameaças ocultas em HTTPS/TLS 1.3.

### Segmentação e Microsegmentação
- **Macro-segmentação L2/L3**: Separação de redes via VLANs, VRFs (Virtual Routing and Forwarding), subredes restritas e Firewalls em modo Routed ou Transparent (Virtual Wire).
- **Microsegmentação baseada em Software (SDN & Agent-based)**:
  - Aplicação de políticas de segurança no nível da Placa de Rede Virtual (vNIC) ou do Host sem depender da topologia física (ex: VMware NSX-T, Cisco ACI, Illumio, Guardicore).
  - Regras orientadas por marcadores lógicos (*Tags/Labels*): `App: Payment`, `Env: Prod`, `Role: DB` bloqueando comunicação lateral não autorizada entre pods/VMs na mesma VLAN.

### IDS/IPS, NTA & NDR (Network Detection and Response)
- **Sensor de Detecção e Prevenção de Intrusão (IDS/IPS)**: Sensores Snort 3, Suricata ou Zeek (Bro) posicionados em portas TAP/SPAN em links críticos de backbone e DMZ.
- **NDR & Telemetria**: Coleta e análise contínua de NetFlow, IPFIX, sFlow e siphoning de pacotes PCAP acoplada a algoritmos de detecção de anomalias (análise estatística e ML para identificar beaconing de C2, tunelamento DNS e exfiltração).

### Controle de Acesso à Rede Físico e Sem Fio (NAC)
- **Autenticação IEEE 802.1X**: Exigência de autenticação baseada em certificados **EAP-TLS** para todas as portas de switches corporativos e pontos de acesso Wi-Fi (WPA3-Enterprise).
- **Orquestração NAC (Cisco ISE / Aruba ClearPass)**: Troca dinâmica de VLANs e envio de regras dACLs/Downloadable ACLs com base na postura do dispositivo e identidade do usuário. MAB (MAC Authentication Bypass) restrito e auditado para dispositivos IoT/Impressoras.

### Roteamento Seguro, WAN & SD-WAN
- **Proteção de Roteamento BGP**: Implementação de **RPKI (Resource Public Key Infrastructure)** para prevenção de BGP Hijacking, autenticação MD5/Keychain em sessões BGP e OSPF.
- **SD-WAN Security**: Malha de comunicação SD-WAN com tunelamento IPsec automático habilitado por padrão (*Full-Mesh IPsec*), segregação por VRFs/VPN Segments e inspeção centralizada nos hubs de borda.

---

## ☁️ 2. Arquitetura de Segurança de Rede Cloud & Multicloud

### AWS Network Security
- **VPC Design & Isolamento**: Estrutura Hub-and-Spoke utilizando **AWS Transit Gateway (TGW)** com *TGW Appliance Mode* ativado para rotear e inspecionar tráfego de entrada e saída por pools de NGFWs.
- **Security Groups vs Network ACLs**:
  - *Security Groups*: Stateful, aplicados na ENI (Interface de Rede), permissões explícitas *Allow*.
  - *NACLs*: Stateless, aplicadas no nível da subrede, regras numeradas com suporte a regras explicitas de *Deny*.
- **Inspeção e Borda Nativas**:
  - **AWS Network Firewall**: Inspeção L3-L7 nativa gerenciada baseada em regras Suricata.
  - **Gateway Load Balancer (GWLB)**: Integração transparente de appliances de segurança de terceiros (Palo Alto, Fortinet, Check Point).
  - **AWS PrivateLink (VPC Endpoints)**: Interface Endpoints e Gateway Endpoints (S3, DynamoDB) para tráfego 100% privado via backbone da AWS, evitando navegação via Internet Gateway (IGW).

### Azure Network Security
- **Topologia Azure Virtual WAN (vWAN) / Hub-and-Spoke**: Hub centralizado contendo **Azure Firewall Premium** (com inspeção TLS, IDPS e filtragem de URL) gerenciando subredes raios (*Spoke VNets*).
- **Controle Granular com NSGs e ASGs**:
  - *Network Security Groups (NSG)*: Aplicados a subredes ou NICs.
  - *Application Security Groups (ASG)*: Agrupamento lógico de VMs para criação de regras simplificadas de microsegmentação sem dependência de IPs estáticos.
- **Conectividade Privada**: Azure Private Endpoints e Private Link Services para isolamento total de PaaS (SQL Database, Key Vault, Storage Accounts).

### GCP Network Security
- **Shared VPC & Hierarchical Firewalls**: Projeto Host de Rede (*Host Project*) centralizando VPCs compartilhadas com projetos de serviço (*Service Projects*).
- **Politicas Hierárquicas de Firewall**: Regras aplicadas no nível de Organização e Pasta herdadas por todas as VPCs filhas.
- **Regras baseadas em Service Accounts e Network Tags**: Substituição de IPs estáticos por identidades de Service Accounts no direcionamento de tráfego de firewall.
- **Private Service Connect (PSC)**: Consumo de serviços de infraestrutura e parceiros através de endpoints privados de VPC.

### OCI Network Security (Oracle Cloud Infrastructure)
- **VCNs & Dynamic Routing Gateway (DRG v2)**: Topologia Hub-and-Spoke conectada por DRG v2 permitindo roteamento transitivo e inspeção centralizada em VCN de segurança.
- **Security Lists vs Network Security Groups (NSGs)**:
  - *Security Lists*: Regras de segurança no nível de toda a Subrede VCN (Stateful/Stateless).
  - *NSGs*: Aplicação granular de regras diretamente nas VNICs de instâncias específicas (Recomendado).
- **OCI Network Firewall**: Appliance gerenciado nativo de firewall de próxima geração powered por tecnologia Palo Alto.

---

## 🌐 3. SASE, SSE & Zero Trust Network Access (ZTNA)

A evolução da segurança de borda substitui a arquitetura tradicional de "Castelo e Fossa" (*Castle-and-Moat*) por serviços de borda distribuídos em nuvem:

```
+-----------------------------------------------------------------------------------+
| CONVERGÊNCIA SASE (Secure Access Service Edge)                                    |
| SD-WAN / Conectividade Edge  +  SSE (Security Service Edge)                       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| COMPONENTES DO SSE (Security Service Edge)                                        |
| 1. ZTNA (Zero Trust Network Access): Acesso granular por aplicação (SDP).         |
| 2. SWG (Secure Web Gateway): Inspeção TLS, filtragem de URL, Sandbox, anti-malware.|
| 3. CASB (Cloud Access Security Broker): Visibilidade Shadow IT e DLP em SaaS.     |
| 4. FWaaS (Firewall as a Service): Inspeção L3-L7 unificada na borda global.       |
+-----------------------------------------------------------------------------------+
```

### ZTNA (Zero Trust Network Access) vs VPN Tradicional
- **Eliminação de Acesso de Rede Completo**: A VPN tradicional insere o dispositivo do usuário dentro da rede local (camada L3). O ZTNA fornece acesso de camada L7 estritamente à aplicação autorizada.
- **Conectores de Saída (*Outbound-Only Connectors*)**: Conectores instalados dentro do datacenter ou VPC estabelecem conexões de saída TLS seguras para a nuvem do provedor ZTNA (ex: Zscaler, Cloudflare One, Palo Alto Prisma Access), fechando todas as portas de entrada (*Inbound*) da infraestrutura corporativa na internet.

---

## 🛡️ 4. Proteção contra DDoS (Distributed Denial of Service)

- **Mitigação Volumétrica e de Camada de Rede (L3/L4)**:
  - Proteção contra SYN Floods, UDP Amplification (NTP, DNS, Memcached), ICMP Floods.
  - Utilização de **Scrubbing Centers**, Anycast BGP Routing e serviços nativos gerenciados (**AWS Shield Advanced**, **Azure DDoS Protection**, **GCP Cloud Armor**, **Cloudflare / Akamai Prolexic**).
- **Mitigação na Camada de Aplicação (L7)**:
  - Proteção contra HTTP Floods, Slowloris, solicitações custosas a bancos de dados.
  - Defesas via WAF (Web Application Firewall): **Rate Limiting dinâmico**, desafios de JavaScript invisível, mitigação de bots baseada em reputação de IP e CAPTCHA/Turnstile.

---

## ⚙️ Protocolo de Decisão do Engenheiro de Segurança de Redes

Ao projetar, analisar ou auditar uma infraestrutura de rede:

1. **Princípio do Perímetro Zero (Nenhum IP é Confiável)**: Trate redes locais, VPCs e redes de parceiros como inerentemente não confiáveis. Force criptografia TLS 1.3/IPsec em todos os fluxos.
2. **Eliminar Portas Públicas Diretas**: Nenhuma VM, banco de dados ou servidor de aplicação deve possuir IP público direto. Utilize Bastion Hosts / SSM Session Manager / ZTNA para acesso administrativo e Load Balancers/WAF para tráfego web público.
3. **Impor Inspeção Centralizada em Topologias Hub-and-Spoke**: Garanta que todo o tráfego transitivo entre spokes (VPCs/VNets) e o tráfego de saída para a internet passem obrigatoriamente pela VCN/VPC Hub de inspeção antes de serem roteados.
4. **Automatizar a Regra "Deny All" por Padrão**: Toda regra de roteamento, Security Group, NSG e Firewall deve encerrar com bloqueio explícito e log de descarte ativado.

---

## 🔗 Integração com Outras Skills de Segurança

- Para alinhar o uso de criptografia e suítes nos túneis IPsec, TLS 1.3, QUIC e mTLS, consulte a skill [cryptography-pqc-standards](..\..\crypto-pki\cryptography-pqc-standards/SKILL.md).
- Para alinhar o controle de acesso e federação de redes aos provedores de identidade IAM, consulte a skill [iam-access-management](..\..\cloud-iam\iam-access-management/SKILL.md).
- Para integrar a segurança de rede às matrizes de controles da Cloud Security Alliance (CCM v4 - IVS & IPY), consulte a skill [csa-cloud-security](..\..\cloud-iam\csa-cloud-security/SKILL.md).
- Para implementar o hardening de infraestrutura de rede alinhado aos CIS Controls (Control 12 e 13) e CIS Benchmarks de Redes, consulte a skill [cis-controls](..\cis-controls/SKILL.md).
- Para alinhar os controles de rede com a ISO/IEC 27001 (A.8.20 - Network Security e A.8.21 - Security of network services), consulte a skill [iso-27000-series](..\iso-27000-series/SKILL.md).
- Para monitoramento e resposta a incidentes de rede via SIEM/SOAR e análise PCAP, consulte a skill [secops-incident-responder](..\..\ops-architecture\secops-incident-responder/SKILL.md).
