---
name: academic-medical-imaging-dicom
description: Especialista em Sistemas de Imagens Médicas e Informática em Saúde baseado na obra The Essential Physics of Medical Imaging (Bushberg). Cobre Raio-X, Tomografia Computadorizada (CT - Retroprojeção Filtrada e Transformada de Radon), Ultrassonografia Doppler, Ressonância Magnética Nuclear (MRI - Equações de Bloch e Espaço k), Medicina Nuclear (PET/SPECT) e interoperabilidade com DICOM, HL7 e SMART on FHIR.
---

# Física das Imagens Médicas e Padrões DICOM/HL7 (Bushberg)

Esta skill estabelece os princípios da física de radiação ionizante e não-ionizante para formação de imagens diagnósticas tridimensionais.

---

## 🩻 1. Tomografia Computadorizada e Transformada de Radon

A projeção radiográfica $p(\theta, r)$ através de um coeficiente de atenuação linear $\mu(x,y)$:
$$p(\theta, r) = \mathcal{R}\{\mu(x,y)\} = \int_{-\infty}^\infty \int_{-\infty}^\infty \mu(x,y) \delta(x\cos\theta + y\sin\theta - r) \, dx \, dy$$
Reconstrução Tomográfica via **Teorema do Corte Central (Fourier Slice Theorem)** e Retroprojeção Filtrada (FBP).
