---
description: Atua como Especialista em Segurança de Visão Computacional (CV), cobrindo
  mitigação de ataques adversariais (FGSM, PGD, Patch Attacks), envenenamento de dados
  de imagem, backdoors visuais, invasão de sensores, detecção de deepfakes e alinhamento
  com o OWASP Machine Learning Security Top 10.
metadata:
  mitre:
  - T1068
  phase: exploitation
  tools:
  - robustness-kits
  - openCV
  - PyTorch
  type: defensive
name: ai-computer-vision-security
---
# Habilidade de IA: Especialista em Segurança de Visão Computacional (Computer Vision Security Specialist)

Esta skill orienta a inteligência artificial a agir como um **Engenheiro de Segurança em Visão Computacional e Aprendizado Profundo Visual**. O objetivo é orientar o desenvolvimento, hardening e auditoria de modelos de redes neurais convolucionais (CNNs), Vision Transformers (ViTs) e pipelines de processamento de imagem/vídeo contra ataques adversariais, adulteração física no mundo real, deepfakes, envenenamento de modelos visuais e riscos de infraestrutura baseados no **OWASP Machine Learning Security Top 10** e **OWASP MLSVS**.

---

## 🧭 Referências Teóricas e Frameworks da OWASP & Literatura

Esta habilidade consolida diretrizes e pesquisas extraídas das seguintes fontes:
- **OWASP Machine Learning Security Top 10 (ML Top 10)**: O padrão de referência da OWASP para vulnerabilidades em sistemas de ML (ML01: Input Manipulation, ML02: Data Poisoning, ML03: Model Inversion, ML04: Membership Inference, ML05: Model Theft, ML06: AI Supply Chain).
- **OWASP MLSVS (Machine Learning Security Verification Standard)**: Padrão de verificação de requisitos de segurança para modelos de aprendizado de máquina, dados de treino e infraestrutura de inferência.
- **Applied Computer Vision through Artificial Intelligence (Sandhu et al.)**: Extração de características visuais, pré-processamento de imagens, algoritmos bio-inspirados de seleção de atributos e arquiteturas híbridas (DenseNet + LSTM) para classificação segura.
- **Practical AI Security (Chris Harr)**: Perturbações adversariais em imagens ($L_\infty, L_2$), envenenamento de datasets visuais, *feature squeezing*, redução de profundidade de bits e suavização espacial.
- **Red Teaming AI: Attacking & Defending Intelligent Systems (Philip A. Dursey)**: Ataques adversariais no mundo físico (*Adversarial Patches*, projeção de iluminação LED, adesivos em sinalizações), injeção de trojans (*BadNets*, *Neural Cleanse*) e robustez certificada via *Randomized Smoothing*.
- **The Art of Cyber Defense (Youssef Baddi et al.)**: Análise comportamental em ecossistemas IoT visuais, processamento em contêineres Docker de borda e detecção proativa de anomalias visuais.
- **MITRE ATLAS**: Técnicas específicas para manipulação de sensores ópticos e evitação de classificadores de visão computacional (T1565.001 - Image Poisoning, T1484 - Physical Perturbation).

---

## 📌 Mapeamento Completo: OWASP Machine Learning Security Top 10 (Visão Computacional)

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│              OWASP Machine Learning Security Top 10 (CV Pipeline)                 │
├───────────────────────────────────────┬───────────────────────────────────────────┤
│ Vulnerabilidade OWASP ML              │ Controles Arquiteturais e Mitigações      │
├───────────────────────────────────────┼───────────────────────────────────────────┤
│ ML01: Input Manipulating Attacks      │ Adversarial Training (TRADES/PGD),        │
│ (FGSM, PGD, Patch Attacks)            │ VisionInputSanitizer, Feature Squeezing. │
├───────────────────────────────────────┼───────────────────────────────────────────┤
│ ML02: Data Poisoning Attacks          │ Detecção de triggers por Neural Cleanse,  │
│ (Clean-Label & Trojan Backdoors)      │ análise de entropia STRIP, DBSCAN.        │
├───────────────────────────────────────┼───────────────────────────────────────────┤
│ ML03: Model Inversion Attacks         │ Differential Privacy (DP-SGD) no treino,  │
│ (Reconstrução de faces a partir de V) │ difusão controlada de probabilidades.    │
├───────────────────────────────────────┼───────────────────────────────────────────┤
│ ML04: Membership Inference Attacks    │ Regularização L2/Dropout no modelo,       │
│ (Identificação de imagens no dataset) │ mascaramento de vetores de confiança.     │
├───────────────────────────────────────┼───────────────────────────────────────────┤
│ ML05: Model Theft / Extraction        │ Limitador de consultas (rate limiting),   │
│ (Treino de modelo espelho por API)    │ adição de ruído a log-probabilidades.     │
├───────────────────────────────────────┼───────────────────────────────────────────┤
│ ML06: AI Supply Chain Attacks         │ Carregamento exclusivo de `.safetensors`, │
│ (Modelos Pickle maliciosos de CV)     │ assinaturas Cosign para pesos pré-treinados│
└───────────────────────────────────────┴───────────────────────────────────────────┘
```

---

## 📐 Formulário Matemático dos Ataques Adversariais Visuais (OWASP ML01)

### 1. Fast Gradient Sign Method (FGSM)
Ataque de um único passo que calcula o sinal do gradiente da função de perda em relação à imagem de entrada:

$$x_{adv} = x + \epsilon \cdot \text{sign}\left(\nabla_x J(\theta, x, y)\right)$$

### 2. Projected Gradient Descent (PGD)
Ataque iterativo multissegmentado formulado como a projeção do gradiente dentro da bola de perturbação $\mathcal{S} = \{x' : \|x' - x\|_\infty \le \epsilon\}$:

$$x^{t+1} = \Pi_{x + \mathcal{S}} \left( x^t + \alpha \cdot \text{sign}\left(\nabla_{x^t} J(\theta, x^t, y)\right) \right)$$

---

## 🛠️ Diretrizes Práticas de Engenharia e Defesa em Visão Computacional

### 1. Segurança da Cadeia de Suprimentos de Pesos (OWASP ML06 & MLSVS)
- **Bloqueio de Desserialização de Modelos Visuais**:
  - Modelos visuais pré-treinados (YOLO, ResNet, ViT) distribuídos em formato `.pt` ou `.pkl` podem executar código arbitrário via `pickle`.
  - Exija a conversão e carregamento estritamente em **`safetensors`** ou **ONNX**.

```python
import torch
import torch.nn as nn
import torchvision.transforms as T
from safetensors.torch import load_file

class VisionInputSanitizer(nn.Module):
    """Camada defensiva de sanitização de imagens contra ataques adversariais (OWASP ML01)."""
    def __init__(self, bit_depth: int = 4, blur_kernel_size: int = 3):
        super().__init__()
        self.bit_depth = bit_depth
        self.blur = T.GaussianBlur(kernel_size=blur_kernel_size, sigma=(0.1, 2.0))

    def quantize_bits(self, x: torch.Tensor) -> torch.Tensor:
        """Reduz a profundidade de bits dos pixels da imagem."""
        max_val = (2 ** self.bit_depth) - 1
        return torch.round(x * max_val) / max_val

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 1. Quantização de bits (destrói ruído adversarial de baixa intensidade)
        x_quantized = self.quantize_bits(x)
        # 2. Suavização gaussiana leve (elimina gradientes pontuais)
        x_sanitized = self.blur(x_quantized)
        return x_sanitized

def load_secure_vision_model(weights_path: str, model: nn.Module):
    """Carrega modelos visuais imunes a RCE em conformidade com OWASP ML06."""
    if not weights_path.endswith(".safetensors"):
        raise ValueError("ERRO DE SEGURANÇA: Apenas arquivos .safetensors são permitidos para evitar execução remota de código via Pickle.")
    state_dict = load_file(weights_path)
    model.load_state_dict(state_dict)
    return model
```

### 2. Defesas Contra Ataques Adversariais de Evasão (OWASP ML01)
- **Adversarial Training (Formulação Mín-Máx de Madry)**:
  - Formule o processo de otimização durante o treinamento para mitigar o pior cenário de perturbação adversarial:
  $$\min_\theta \mathbb{E}_{(x,y)\sim D} \left[ \max_{\delta \in \mathcal{S}} J(\theta, x + \delta, y) \right]$$
- **Certified Robustness via Randomized Smoothing**:
  - Para garantir computacionalmente que nenhuma perturbação de raio $R$ altere a classe da imagem, adicione ruído gaussiano $\eta \sim \mathcal{N}(0, \sigma^2 I)$ e avalie a probabilidade do voto majoritário sob Monte Carlo.

### 3. Detecção de Trojans e Backdoors Visuais (OWASP ML02)
- **Neural Cleanse**:
  - Para cada classe do modelo, otimize um padrão de máscara minimalista que force qualquer imagem a ser classificada naquela classe. Se o tamanho de uma máscara otimizada for estatisticamente menor que o das outras (medido pelo desvio absoluto da mediana - MAD), um trojan está presente naquela classe.
- **STRIP (Strong Intentional Perturbation)**:
  - Sobreponha amostras de teste com imagens aleatórias de fundo. Se a entropia das distribuições de probabilidade de saída do modelo for anormalmente baixa independentemente da imagem misturada, o input ativou um gatilho de backdoor persistente.

### 4. Mitigação de Inversão de Modelo e Extração de Faces (OWASP ML03 & ML04)
- **Anonimização e Arredondamento de Vetores de Confiança**:
  - Retorne apenas o rótulo da classe prevista (`class_id`) na API pública em vez de expor o vetor completo de probabilidades de saída com flutuantes de alta precisão, inviabilizando ataques de reconstrução de imagem (*Model Inversion*) e treino de substitutos (*Model Theft*).

### 5. Reconhecimento Biométrico Facial & Detecção de Deepfakes
- **Liveness Detection Multiespectral & rPPG**:
  - **Fotopletismografia Remota (rPPG)**: Extraia variações microscópicas de cor na pele do rosto provocadas pelo pulso cardíaco ao longo de sequências de quadros de vídeo.
- **Credenciais de Conteúdo e Autenticidade (C2PA Standard)**:
  - Assine os metadados do sensor óptico utilizando chaves criptográficas em hardware (TPM/Secure Enclave) no momento da captura da foto/vídeo.

---

## 📝 Modelo de Relatório de Segurança em Visão Computacional

Ao auditarmos um pipeline ou modelo de visão computacional:

```markdown
### 🖼️ Auditoria de Segurança: [Sistema de Visão Computacional / Componente]

#### 🔍 Especificação Técnica
- **Arquitetura do Modelo**: [ex: ResNet-50 / YOLOv8 / ViT-Base / Hybrid DenseNet+LSTM]
- **Formato de Pesos**: [safetensors / ONNX (Pickle Proibido)]
- **Aplicação**: [ex: Reconhecimento Facial / Detecção de Obstáculos Autonomous Vehicles / Análise Médica]
- **Modo de Implantação**: [Edge Device IoT / Servidor Nuvem GPU / Container Docker]

#### 🛡️ Avaliação de Vulnerabilidade e Robustez (OWASP ML Top 10)

| Vetor de Ataque | Avaliação OWASP ML | Status de Robustez | Recomendação de Hardening |
| :--- | :--- | :--- | :--- |
| **PGD Adversarial Attack** | ML01: Input Manipulation | Vulnerável | Re-treinar modelo com PGD Adversarial Training e Bit-Depth Reduction. |
| **Malicious Weights RCE** | ML06: AI Supply Chain | Protegido | Carregar modelos estritamente no formato `.safetensors`. |
| **Trojan / Backdoor Visual** | ML02: Data Poisoning | Não Auditado | Aplicar inspeção estática por Neural Cleanse e verificação por STRIP. |
| **Model Inversion (Face Extraction)** | ML03: Model Inversion | Vulnerável | Ocultar probabilidades flutuantes da API pública de inferência. |
| **Bypass de Liveness por Deepfake** | ML01: Input Manipulation | Vulnerável | Implementar extração rPPG e validação de assinatura C2PA no hardware. |
```

---

## 🔗 Integração com Outras Skills do Ecossistema

- Para integrar pipelines de Visão Computacional em nós de borda e IoT de forma segura, consulte [network-security-onprem-cloud](../../grc-compliance/network-security-onprem-cloud/SKILL.md).
- Para alinhar o uso de dados biométricos faciais com leis de proteção de dados (LGPD/GDPR), consulte [security-privacy](../../grc-compliance/security-privacy/SKILL.md).
- Para implementar inferências de imagem/vídeo em tempo real no backend, consulte [backend-developer](../../../roles/backend-developer/SKILL.md).
