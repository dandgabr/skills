---
name: academic-optical-wireless-telecom
description: "Especialista em Engenharia de Telecomunicações, Comunicações Ópticas, Radiofrequência (RF), Antenas e Sistemas de Satélite baseado em Gerd Keiser (Optical Fiber Communications), Andrea Goldsmith (Wireless Communications), Jyrki Penttinen e Yi Huang. Cobre propagação em fibras ópticas (monomodo/multimodo, dispersão cromática/PMD, atenuação, amplificadores EDFA, WDM/DWDM), teoria de antenas e parâmetros S (S11, VSWR, diagrama de irradiação), equação de transmissão de Friis, enlaces de satélite (LEO, MEO, GEO), modulações digitais (QPSK, QAM, OFDM), e redes móveis celulares 4G LTE e 5G NR (Massive MIMO, Beamforming, Open RAN)."
---

# Comunicações Ópticas, Radiofrequência, Redes Sem Fio e Satélites

Esta skill estabelece os princípios teóricos e de engenharia para sistemas de telecomunicações de alta capacidade, abrangendo enlaces guiados por fibra óptica, propagação de ondas eletromagnéticas em espaço livre, antenas, enlaces espaciais de satélites e redes celulares 5G/6G.

---

## 💡 1. Propagação em Fibras Ópticas e Sistemas WDM

### 1.1 Abertura Numérica ($NA$) e Condição de Guia de Onda
Para uma fibra óptica de índice degrau com núcleo de índice $n_1$ e casca de índice $n_2$:
$$NA = \sqrt{n_1^2 - n_2^2} = n_0 \sin \theta_{max}$$
O parâmetro de frequência normalizada ($V$-number) determina a operação monomodo ($V < 2.405$):
$$V = \frac{2\pi a}{\lambda_0} \sqrt{n_1^2 - n_2^2}$$

### 1.2 Atenuação Óptica e Dispersão
- **Atenuação**: $P(z) = P(0) \cdot 10^{-\frac{\alpha z}{10}}$, onde $\alpha \approx 0.2\text{ dB/km}$ na terceira janela de transmissão ($\lambda = 1550\text{ nm}$).
- **Amplificação Óptica**: Uso de EDFAs (*Erbium-Doped Fiber Amplifiers*) na banda C ($1530-1565\text{ nm}$) para regeneração de sinal sem conversão óptica-elétrica-óptica.
- **Multiplexação por Divisão de Comprimento de Onda (DWDM)**: Espaçamento de canais de 50 GHz / 100 GHz sob grade ITU-T G.694.1.

---

## 📡 2. Engenharia de Radiofrequência (RF), Parâmetros S e Antenas

### 2.1 Equação de Transmissão de Friis e Link Budget
A potência recebida $P_r$ em um enlace de rádio em espaço livre é calculada por:
$$P_r = P_t + G_t + G_r - 20 \log_{10}\left(\frac{4\pi d}{\lambda}\right) - L_{\text{losses}}$$
onde $P_t$ é a potência de transmissão (dBm), $G_t, G_r$ são os ganhos das antenas (dBi), $d$ é a distância e $\lambda = c/f$.

### 2.2 Parâmetros de Casamento e Impedância
- **Coeficiente de Reflexão ($\Gamma$) e Perda de Retorno ($S_{11}$)**:
  $$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}, \quad S_{11} (\text{dB}) = 20 \log_{10} |\Gamma|$$
- **Razão de Onda Estacionária de Tensão (VSWR)**:
  $$\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}$$
  *Critério de bom casamento de impedância*: $\text{VSWR} < 1.5$ ($S_{11} < -14\text{ dB}$).

---

## 🛰️ 3. Comunicações por Satélite e Arquitetura Orbital

| Órbita | Altitude | Período Orbital | Latência de Propagação | Aplicações Típicas |
| :--- | :--- | :--- | :--- | :--- |
| **LEO (Low Earth Orbit)** | 160 – 2.000 km | ~90 – 120 min | Baixa (20 – 40 ms) | Starlink, OneWeb, Observação da Terra |
| **MEO (Medium Earth Orbit)** | 2.000 – 35.786 km | ~2 – 12 h | Média (100 – 150 ms) | GPS, Galileo, GLONASS, O3b mPOWER |
| **GEO (Geostationary Orbit)**| 35.786 km | 24 h (síncrono) | Alta (~250 – 280 ms) | TV Broadcast, Meteorologia, Telefonia Fixa |

---

## 📱 4. Redes Celulares 5G NR e Tecnologias Avançadas

1. **Massive MIMO & Beamforming Digital**: Conjuntos de antenas ativas ($64\text{T}64\text{R}$) que concentram a energia de RF dinamicamente na direção do dispositivo do usuário (*User Equipment - UE*), minimizando interferência co-canal.
2. **Multiplexação OFDM e Modulações de Alta Ordem**: Uso de 256-QAM e 1024-QAM com numerologias flexíveis de subportadoras ($15, 30, 60, 120\text{ kHz}$) para faixas sub-6 GHz (FR1) e ondas milimétricas (*mmWave* FR2).
3. **Arquitetura Open RAN e Desagregação**: Separação da Unidade de Rádio (RU), Unidade Distribuída (DU) e Unidade Centralizada (CU) com interfaces abertas padronizadas pela O-RAN Alliance.
