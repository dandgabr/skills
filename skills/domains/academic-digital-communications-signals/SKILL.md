---
name: academic-digital-communications-signals
description: "Especialista em Comunicações Digitais, Teoria da Informação, Redes Ópticas, Radiofrequência e Sistemas Sem Fio baseado em John G. Proakis (Digital Communications), Gerd Keiser (Optical Fiber Communications), Andrea Goldsmith e Simon Haykin. Cobre Teorema da Amostragem de Nyquist-Shannon, Capacidade de Canal de Shannon-Hartley, modulações em banda passante (ASK, FSK, PSK, QAM, OFDM), códigos corretores de erro (Hamming, Reed-Solomon, Convolucionais, LDPC, Turbo Codes), equalização adaptativa e DSP, propagação em fibras ópticas (monomodo, dispersão cromática/PMD, atenuação, amplificadores EDFA, WDM/DWDM), teoria de antenas e parâmetros S (S11, VSWR), equação de transmissão de Friis, enlaces de satélite (LEO, MEO, GEO) e redes celulares 4G LTE / 5G NR (Massive MIMO, Beamforming, Open RAN)."
---

# Comunicações Digitais, Teoria da Informação, Redes Ópticas e Sem Fio

Esta skill estabelece os fundamentos teóricos, matemáticos e de engenharia para transmissão de informação através de canais guiados (fibras ópticas) e não-guiados (radiofrequência, satélites e redes celulares 5G/6G), fundamentada nas obras de **John G. Proakis** (*Digital Communications*), **Gerd Keiser** (*Optical Fiber Communications*) e **Andrea Goldsmith** (*Wireless Communications*).

---

## 📡 1. Teoria da Informação, Amostragem e Modulações Digitais

### 1.1 Teorema de Nyquist-Shannon e Capacidade de Canal de Shannon-Hartley
- **Taxa de Nyquist**: Para evitar aliasing na amostragem de um sinal com largura de banda $B$, a frequência de amostragem mínima é $f_s \ge 2B$.
- **Capacidade de Canal em AWGN**:
  $$C = B \log_2\left(1 + \frac{S}{N}\right) = B \log_2\left(1 + \frac{P}{N_0 B}\right) \quad [\text{bits/s}]$$
  No limite de banda infinita ($B \rightarrow \infty$):
  $$C_{\infty} = \frac{P}{N_0 \ln 2} \approx 1.44 \frac{P}{N_0}$$

### 1.2 Modulações em Banda Passante e Probabilidade de Erro de Bit (BER)
- **BPSK / QPSK**:
  $$P_{b,\text{BPSK}} = Q\left(\sqrt{\frac{2E_b}{N_0}}\right), \quad \text{onde } Q(x) = \frac{1}{\sqrt{2\pi}} \int_x^\infty e^{-u^2/2} du$$
- **$M$-QAM ($M = 16, 64, 256, 1024$)**: Modulação em quadratura com alta eficiência espectral ($\eta = \log_2 M\text{ bps/Hz}$).
- **OFDM (Orthogonal Frequency Division Multiplexing)**: Divisão de um canal de alta taxa em $N$ subportadoras ortogonais de banda estreita com Intervalo de Guarda (*Cyclic Prefix*) para eliminar Interferência Inter-Simbólica (ISI).

```mermaid
graph LR
    Bits[Bits de Informação] --> FEC[Codificação de Canal LDPC/Turbo]
    FEC --> Map[Mapeador de Constelação QAM]
    Map --> IFFT[iFFT Modulador OFDM]
    IFFT --> CP[Inserção de Prefixo Cíclico]
    CP --> DAC[DAC & Upconverter RF/Óptico]
    DAC --> Channel[Canal AWGN / Fibra / Fading]
```

### 1.3 Códigos Corretores de Erro (Forward Error Correction - FEC)
- **Códigos de Bloco Lineares & Hamming**: Detecção de $d_{min}-1$ erros e correção de $\lfloor (d_{min}-1)/2 \rfloor$ erros.
- **Reed-Solomon (RS)**: Códigos não-binários ideais para rajadas de erros (*burst errors*) em mídia de armazenamento e enlaces de satélite.
- **Códigos LDPC (Low-Density Parity-Check) e Códigos Turbo**: Códigos com algoritmos de decodificação iterativa (*Belief Propagation*) que operam a frações de décimos de dB do Limite de Shannon. Padrão no 5G NR e DVB-S2X.

---

## 💡 2. Comunicações Ópticas e Sistemas WDM/DWDM

### 2.1 Propagação e Condição Monomodo em Fibras
Abertura Numérica ($NA$) e parâmetro de frequência normalizada ($V$-number):
$$NA = \sqrt{n_1^2 - n_2^2} = \sin \theta_{max}, \quad V = \frac{2\pi a}{\lambda_0} \sqrt{n_1^2 - n_2^2}$$
A fibra opera em modo único transversal ($\text{LP}_{01}$) se $V < 2.405$.

### 2.2 Atenuação e Dispersão
- **Atenuação**: $P(z) = P(0) \cdot 10^{-\frac{\alpha z}{10}}$, com mínimo histórico de $\alpha \approx 0.18\text{ dB/km}$ em $\lambda = 1550\text{ nm}$ (janela C-Band).
- **Amplificação com EDFA**: Amplificadores ópticos de fibra dopada com Érbio operando com bombeamento a laser de 980 nm ou 1480 nm, amplificando simultaneamente centenas de canais DWDM sem conversão eletrônica.

---

## 🛰️ 3. Radiofrequência (RF), Antenas, Enlaces de Satélites e Redes 5G NR

### 3.1 Equação de Friis e Parâmetros de Antena
- **Potência Recebida em Espaço Livre**:
  $$P_r = P_t + G_t + G_r - 20 \log_{10}\left(\frac{4\pi d}{\lambda}\right) - L_{\text{losses}} \quad [\text{dBm}]$$
- **Coeficiente de Reflexão ($\Gamma$) e Perda de Retorno ($S_{11}$)**:
  $$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}, \quad S_{11} = 20 \log_{10} |\Gamma|, \quad \text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}$$

### 3.2 Órbitas de Satélites e Redes Móveis 5G
- **Classificação Orbital**: LEO ($160-2.000\text{ km}$, latência $20-40\text{ ms}$, Starlink), MEO ($2.000-35.786\text{ km}$, GPS/Galileo) e GEO ($35.786\text{ km}$, síncrono).
- **Massive MIMO & Beamforming Digital (5G NR)**: Matrizes de $64\text{T}64\text{R}$ que sintetizam feixes eletromagnéticos estreitos e direcionais focados em tempo real no usuário, aumentando a capacidade da célula por divisão espacial (MU-MIMO).
