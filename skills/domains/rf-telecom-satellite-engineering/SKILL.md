---
name: rf-telecom-satellite-engineering
description: Especialista em Engenharia de Telecomunicações, Radiofrequência (RF), Antenas e Comunicações por Satélite baseado nas obras The Telecommunications Handbook (Jyrki Penttinen), Antennas From Theory to Practice (Yi Huang) e Satellite Basics For Everyone (C. Robert Welti). Cobre propagação de ondas eletromagnéticas, parâmetros S (S11/VSWR), diagramas de irradiação de antenas, enlaces de satélite (Uplink/Downlink, Orbits LEO/MEO/GEO), modulações digitais (QPSK, QAM, OFDM) e redes móveis celulares.
---

# Engenharia de Radiofrequência (RF), Antenas e Telecomunicações via Satélite

Esta skill estabelece os princípios da física e engenharia de comunicações sem fio, propagação eletromagnética em espaço livre, projeto de antenas e arquitetura de enlaces espaciais via satélite.

---

## 📡 1. Equação de Transmissão de Friis e Link Budget

A potência recebida $P_r$ em um enlace de rádio em espaço livre é calculada pela fórmula de Friis:

$$P_r = P_t + G_t + G_r - 20 \log_{10}\left(\frac{4\pi d}{\lambda}\right) - L_{\text{losses}}$$

onde:
- $P_t$: Potência transmitida (dBm).
- $G_t, G_r$: Ganhos das antenas transmissora e receptora (dBi).
- $d$: Distância entre antenas (m).
- $\lambda$: Comprimento de onda da portadora ($\lambda = c/f$).

---

## 🛰️ 2. Classificação de Órbitas de Satélites

| Órbita | Altitude | Período Orbital | Latência de Propagação | Aplicações Típicas |
| :--- | :--- | :--- | :--- | :--- |
| **LEO (Low Earth Orbit)** | 160 – 2.000 km | ~90 – 120 minutos | Baixa (20 – 40 ms) | Starlink, OneWeb, Observação da Terra. |
| **MEO (Medium Earth Orbit)** | 2.000 – 35.786 km | ~2 – 12 horas | Média (100 – 150 ms) | GPS, Galileo, GLONASS, O3b. |
| **GEO (Geostationary Orbit)**| 35.786 km | 24 horas (síncrono) | Alta (~250 – 280 ms) | TV Broadcast, Meteorologia, Telefonia Fixa. |
