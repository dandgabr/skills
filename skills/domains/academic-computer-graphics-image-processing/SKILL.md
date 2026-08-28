---
name: academic-computer-graphics-image-processing
description: Especialista em Computação Gráfica e Processamento Digital de Imagens baseado nas obras Fundamentals of Computer Graphics (Shirley, Marschner) e Digital Image Processing (Gonzalez, Woods). Cobre Pipeline Gráfico 3D (Transformações Afins, Projeções), Shaders (GLSL/HLSL), Modelos de Iluminação (Phong, PBR - Physically Based Rendering), Ray Tracing, Filtragem Espacial e no Domínio da Frequência (FFT 2D, Wavelets) e Segmentação de Imagens.
---

# Computação Gráfica e Processamento Digital de Imagens

Esta skill estabelece os algoritmos geométricos, rasterização, ray tracing e manipulação matricial de imagens em tempo real e offline.

---

## 🎨 1. Pipeline de Transformações Geométricas 3D (Coordenadas Homogêneas)

$$\mathbf{v}_{clip} = \mathbf{M}_{proj} \cdot \mathbf{M}_{view} \cdot \mathbf{M}_{model} \cdot \mathbf{v}_{local}$$

- **Modelo de Iluminação de Phong**:
  $$I = I_a k_a + I_d k_d (\mathbf{L} \cdot \mathbf{N}) + I_s k_s (\mathbf{R} \cdot \mathbf{V})^n$$

---

## 🖼️ 2. Filtragem no Domínio da Frequência (Transformada de Fourier 2D)

$$\mathcal{F}\{f(x,y)\} = F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)}$$
