---
name: academic-digital-communications-signals
description: Especialista em Comunicações Digitais e Teoria da Informação baseado na obra Digital Communications (John G. Proakis). Cobre Teorema da Amostragem de Nyquist-Shannon, Modulações em Banda Passante (ASK, FSK, PSK, QAM, OFDM), Capacidade de Canal de Shannon, Códigos Corretores de Erro (Hamming, Reed-Solomon, Convolucionais, LDPC, Turbo Codes), Equalização Adaptativa e Processamento Digital de Sinais (DSP).
---

# Comunicações Digitais e Teoria da Informação (Proakis & Shannon)

Esta skill estabelece a modelagem probabilística de transmissão de dados através de canais com ruído AWGN e desvanecimento Rayleigh/Rician.

---

## 📡 1. Capacidade de Canal de Shannon-Hartley

A taxa máxima teórica de transmissão sem erros em um canal com largura de banda $B$ (Hz) e relação sinal-ruído $S/N$:
$$C = B \log_2\left(1 + \frac{S}{N}\right) \quad [\text{bits/s}]$$

Taxa de Erro de Bit (BER) para modulação BPSK em canal AWGN:
$$P_b = Q\left(\sqrt{\frac{2E_b}{N_0}}\right) \quad \text{onde } Q(x) = \frac{1}{\sqrt{2\pi}} \int_x^\infty e^{-u^2/2} du$$
