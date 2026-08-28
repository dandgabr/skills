---
name: academic-computer-graphics-image-processing
description: Especialista sênior em Computação Gráfica, Visão Computacional, Processamento Digital de Imagens e Composição Digital baseado nas obras Mathematics for Computer Graphics (John Vince), Computer Vision Metrics (Scott Krig), Mastering Computer Vision with PyTorch 2.0 (M. Arshad Siddiqui), The Art and Science of Digital Compositing (Ron Brinkmann), Numerical Algorithms (Justin Solomon) e Digital Image Processing (Gonzalez, Woods). Cobre Transformações Geométricas 3D, Quatérnios e SLERP, Geometria Projetiva, Curvas e Superfícies Paramétricas (Bézier, B-Splines, NURBS), Modelos de Iluminação (Phong, PBR Cook-Torrance BRDF/BSSRDF), Ray Tracing, Taxonomia de Descritores e Detectores de Features (SIFT, ORB, FAST, BRISK), Deep Learning com PyTorch 2.0 (YOLO, Mask R-CNN, UNet, ViT, TorchDynamo), Álgebra de Composição Digital (Porter-Duff, Alpha Premultiplication, Espaços de Cor ACES/Linear) e Métodos Numéricos Geométricos (Laplace-Beltrami, ICP, Simulação Física).
---

# Computação Gráfica, Visão Computacional e Processamento de Imagens

Esta skill estabelece os fundamentos matemáticos rigorosos, algoritmos de renderização, visão computacional moderna, composição digital de efeitos visuais e processamento numérico de geometria 2D/3D.

---

## 📐 1. Transformações Geométricas 3D e Álgebra de Projeção

### 1.1 Coordenadas Homogêneas e Pipeline de Transformação
Em computação gráfica, pontos no $\mathbb{R}^3$ são representados em coordenadas homogêneas $\mathbf{p} = [x, y, z, 1]^T$ para unificar operações afins (translação, rotação, escala e cisalhamento) em matrizes $4 \times 4$:

$$\mathbf{v}_{clip} = \mathbf{M}_{proj} \cdot \mathbf{M}_{view} \cdot \mathbf{M}_{model} \cdot \mathbf{v}_{local}$$

- **Matriz de Translação**:
  $$\mathbf{T}(t_x, t_y, t_z) = \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

- **Matriz de Rotação em torno do eixo arbitrário $\mathbf{u} = [u_x, u_y, u_z]^T$ com $\|\mathbf{u}\|=1$ (Fórmula de Rodrigues)**:
  $$\mathbf{R}(\theta, \mathbf{u}) = \cos\theta \mathbf{I} + (1 - \cos\theta) \mathbf{u}\mathbf{u}^T + \sin\theta [\mathbf{u}]_\times$$
  onde $[\mathbf{u}]_\times$ é a matriz antissimétrica (*skew-symmetric*):
  $$[\mathbf{u}]_\times = \begin{bmatrix} 0 & -u_z & u_y \\ u_z & 0 & -u_x \\ -u_y & u_x & 0 \end{bmatrix}$$

### 1.2 Quatérnios e Interpolação Esférica (SLERP)
Para evitar o travamento de cardan (*Gimbal Lock*) e garantir interpolações de rotação suaves de orientações 3D:
- **Quatérnio Unitário**: $\mathbf{q} = s + x\mathbf{i} + y\mathbf{j} + z\mathbf{k} = [\cos(\theta/2), \mathbf{u}\sin(\theta/2)]$ onde $\|\mathbf{q}\| = 1$.
- **Rotação de um Ponto**: $\mathbf{p}' = \mathbf{q} \mathbf{p} \mathbf{q}^{-1} = \mathbf{q} \mathbf{p} \mathbf{q}^*$.
- **SLERP (Spherical Linear Interpolation)**:
  $$\text{SLERP}(\mathbf{q}_1, \mathbf{q}_2; t) = \frac{\sin((1-t)\Omega)}{\sin\Omega} \mathbf{q}_1 + \frac{\sin(t\Omega)}{\sin\Omega} \mathbf{q}_2 \quad \text{onde } \cos\Omega = \mathbf{q}_1 \cdot \mathbf{q}_2$$

### 1.3 Matrizes de Projeção em Perspectiva e Ortográfica
- **Projeção em Perspectiva Simétrica (Frustum com $fov$, $aspect$, $z_{near}$, $z_{far}$)**:
  $$\mathbf{M}_{persp} = \begin{bmatrix} \frac{1}{\text{aspect} \cdot \tan(fov/2)} & 0 & 0 & 0 \\ 0 & \frac{1}{\tan(fov/2)} & 0 & 0 \\ 0 & 0 & -\frac{z_f + z_n}{z_f - z_n} & -\frac{2 z_f z_n}{z_f - z_n} \\ 0 & 0 & -1 & 0 \end{bmatrix}$$
- **Divisão de Perspectiva**: Normalização de Coordenadas de Dispositivo Normalizadas (NDC): $\mathbf{v}_{ndc} = [x_c/w_c, y_c/w_c, z_c/w_c]^T$.

---

## 〰️ 2. Curvas Paramétricas e Superfícies 3D

### 2.1 Curvas de Bézier e Algoritmo de De Casteljau
Uma curva de Bézier de grau $n$ definida por $n+1$ pontos de controle $\mathbf{P}_0, \mathbf{P}_1, \dots, \mathbf{P}_n$:
$$\mathbf{C}(t) = \sum_{i=0}^n B_{i,n}(t) \mathbf{P}_i, \quad t \in [0, 1]$$
onde $B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}$ são os polinômios de Bernstein.

- **Bézier Cúbica ($n=3$)**:
  $$\mathbf{C}(t) = (1-t)^3 \mathbf{P}_0 + 3t(1-t)^2 \mathbf{P}_1 + 3t^2(1-t) \mathbf{P}_2 + t^3 \mathbf{P}_3$$
- **Algoritmo de De Casteljau**: Avaliação recursiva estável numericamente por interpolações lineares sucessivas $\mathbf{P}_i^{(k)}(t) = (1-t)\mathbf{P}_i^{(k-1)}(t) + t\mathbf{P}_{i+1}^{(k-1)}(t)$.

### 2.2 B-Splines e Superfícies NURBS
- **B-Splines**: Oferecem controle local e continuidade $C^k$ arbitrária usando um vetor de nós (*knot vector*) $U = \{u_0, u_1, \dots, u_m\}$ com funções base de Cox-de Boor.
- **NURBS (Non-Uniform Rational B-Splines)**: Permitem representação exata de cônicas (círculos, elipses, esferas) através de pontos de controle ponderados por pesos $w_i$:
  $$\mathbf{S}(u, v) = \frac{\sum_{i=0}^n \sum_{j=0}^m N_{i,p}(u) N_{j,q}(v) w_{i,j} \mathbf{P}_{i,j}}{\sum_{i=0}^n \sum_{j=0}^m N_{i,p}(u) N_{j,q}(v) w_{i,j}}$$

---

## 💡 3. Modelos de Iluminação, Shading e Renderização

### 3.1 Iluminação Empírica vs Fisicamente Baseada (PBR)
| Modelo | Equação Fundamental | Características Principais |
| :--- | :--- | :--- |
| **Phong Clássico** | $I = k_a I_a + k_d I_d (\mathbf{L} \cdot \mathbf{N}) + k_s I_s (\mathbf{R} \cdot \mathbf{V})^n$ | Empírico, não conserva energia, usa vetor de reflexão ideal $\mathbf{R}$. |
| **Blinn-Phong** | $I = k_a I_a + k_d I_d (\mathbf{L} \cdot \mathbf{N}) + k_s I_s (\mathbf{H} \cdot \mathbf{N})^n$ | Mais eficiente, usa vetor meio-caminho $\mathbf{H} = \frac{\mathbf{L} + \mathbf{V}}{\|\mathbf{L} + \mathbf{V}\|}$. |
| **PBR Cook-Torrance (Microfacet)** | $f_r(\mathbf{x}, \omega_i, \omega_o) = \frac{D(\mathbf{h}) F(\omega_i, \mathbf{h}) G(\omega_i, \omega_o, \mathbf{h})}{4 (\mathbf{n} \cdot \omega_i) (\mathbf{n} \cdot \omega_o)}$ | Fisicamente plausível, conserva energia, microfacetas. |

- **Termos da BRDF Cook-Torrance**:
  1. **Distribuição Normal $D(\mathbf{h})$ (GGX / Trowbridge-Reitz)**:
     $$D_{GGX}(\mathbf{h}) = \frac{\alpha^2}{\pi \left( (\mathbf{n} \cdot \mathbf{h})^2 (\alpha^2 - 1) + 1 \right)^2}$$
  2. **Fresnel $F(\omega_i, \mathbf{h})$ (Aproximação de Schlick)**:
     $$F_{Schlick}(\theta) = F_0 + (1 - F_0) (1 - \cos\theta)^5$$
  3. **Geometria / Sombreamento $G(\omega_i, \omega_o, \mathbf{h})$ (Smith GGX)**:
     $$G(\mathbf{n}, \mathbf{v}, \mathbf{l}) = G_1(\mathbf{n}, \mathbf{v}) G_1(\mathbf{n}, \mathbf{l}), \quad G_1(\mathbf{n}, \mathbf{v}) = \frac{2 (\mathbf{n} \cdot \mathbf{v})}{(\mathbf{n} \cdot \mathbf{v}) + \sqrt{\alpha^2 + (1-\alpha^2)(\mathbf{n} \cdot \mathbf{v})^2}}$$

### 3.2 Equação de Renderização de Kajiya (Ray Tracing Global)
$$L_o(\mathbf{x}, \omega_o) = L_e(\mathbf{x}, \omega_o) + \int_{\Omega} f_r(\mathbf{x}, \omega_i, \omega_o) L_i(\mathbf{x}, \omega_i) (\mathbf{n} \cdot \omega_i) \, d\omega_i$$
- **Algoritmos de Aceleração Espacial**: BVH (Bounding Volume Hierarchy), Octrees e KD-Trees com Heurística de Área de Superfície (SAH - Surface Area Heuristic).

---

## 🔍 4. Taxonomia de Métricas de Visão Computacional & Descritores

### 4.1 Detectores e Descritores Locais de Features (Scott Krig Taxonomy)
```
Taxonomia de Features Visuais:
├── Detectores de Cantos & Bordas:
│   ├── Gradiente Espacial: Sobel, Prewitt, Scharr
│   ├── Autovalores de Autocorrelação: Harris Corner Detector, Shi-Tomasi (Good Features to Track)
│   └── Testes de Segmento Acelerados: FAST (Features from Accelerated Segment Test), AGAST
├── Descritores Baseados em Histograma de Gradiente:
│   ├── SIFT (Scale-Invariant Feature Transform) - DoG (Difference of Gaussians), 128-dim vetor
│   ├── SURF (Speeded-Up Robust Features) - Box Filters e Imagens Integrais, 64-dim vetor
│   └── HOG (Histogram of Oriented Gradients) - Detecção densa de pedestres/objetos
└── Descritores Binários (Baixo Custo / Mobile):
    ├── BRIEF (Binary Robust Independent Elementary Features)
    ├── ORB (Oriented FAST and Rotated BRIEF) - Rotação invariante e resistente a ruído
    ├── BRISK (Binary Robust Invariant Scalable Keypoints) - Padrão de amostragem circular
    └── FREAK (Fast Retina Keypoint) - Amostragem inspirada na retina humana
```

### 4.2 Métricas de Similaridade, Distância e Qualidade de Imagem
- **Distância de Hamming para Descritores Binários**:
  $$D_H(\mathbf{a}, \mathbf{b}) = \text{popcount}(\mathbf{a} \oplus \mathbf{b})$$
- **PSNR (Peak Signal-to-Noise Ratio)**:
  $$\text{PSNR} = 10 \log_{10} \left( \frac{\text{MAX}_I^2}{\text{MSE}} \right), \quad \text{MSE} = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} [I(x,y) - K(x,y)]^2$$
- **SSIM (Structural Similarity Index Measure)**:
  $$\text{SSIM}(x, y) = \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}$$

---

## 🤖 5. Visão Computacional Moderna com PyTorch 2.0

### 5.1 PyTorch 2.0 Stack de Alta Performance (`torch.compile`)
- **TorchDynamo**: Captura grafos de execução Python sem modificar o código do modelo.
- **TorchInductor**: Compilador com geração de código C++/Triton de alta performance para GPUs NVIDIA.
- **AOTAutograd**: Rastreamento adiantado do grafo de retropropagação para fusão de operadores.

```python
import torch
import torchvision.models as models

# Modelo Vision Transformer compilado com PyTorch 2.0
model = models.vit_b_16(weights=models.ViT_B_16_Weights.DEFAULT).cuda()
model.eval()

# Otimização TorchDynamo + TorchInductor
compiled_model = torch.compile(model, mode="max-autotune")

with torch.inference_mode():
    dummy_input = torch.randn(1, 3, 224, 224, device="cuda")
    output = compiled_model(dummy_input)
```

### 5.2 Arquiteturas de Visão Computacional de Ponta
1. **Detecção de Objetos**:
   - **One-Stage**: YOLOv8 / YOLOv9 / RetinaNet (Focal Loss para desbalanceamento de classes).
   - **Two-Stage**: Faster R-CNN com RPN (Region Proposal Network) e RoIAlign.
   - **Transformer-Based**: DETR (Detection Transformer) com casamento bipartido via Hungarian Loss.
2. **Segmentação de Imagens**:
   - **Semântica**: UNet, DeepLabV3+ (com Atrous Spatial Pyramid Pooling - ASPP).
   - **Instância / Panóptica**: Mask R-CNN, Segment Anything Model (SAM).
3. **Vision Transformers (ViT & Swin)**:
   - Divisão de imagem em patches não-sobrepostos ($16 \times 16$).
   - Mecanismo de Multi-Head Self-Attention e Patch Merging hierárquico (Swin).

---

## 🎨 6. Álgebra de Composição Digital & Efeitos Visuais (Brinkmann)

### 6.1 Operadores de Composição de Porter-Duff
Em composição digital profissional, a manipulação de imagens com canal Alpha segue a álgebra de Porter-Duff:

| Operador | Equação de Cor ($C_o$) | Equação de Alpha ($A_o$) | Descrição Técnica |
| :--- | :--- | :--- | :--- |
| **$A \text{ OVER } B$** | $C_A + C_B(1 - A_A)$ | $A_A + A_B(1 - A_A)$ | A sobre B (composição padrão em camadas). |
| **$A \text{ IN } B$** | $C_A \cdot A_B$ | $A_A \cdot A_B$ | Região de A contida dentro do alpha de B. |
| **$A \text{ OUT } B$** | $C_A(1 - A_B)$ | $A_A(1 - A_B)$ | Região de A que não intercepta o alpha de B. |
| **$A \text{ ATOP } B$** | $C_A \cdot A_B + C_B(1 - A_A)$ | $A_B$ | A dentro do alpha de B, com B nas demais partes. |
| **$A \text{ XOR } B$** | $C_A(1 - A_B) + C_B(1 - A_A)$ | $A_A(1 - A_B) + A_B(1 - A_A)$ | A ou B, excluindo a intersecção de ambos. |

### 6.2 Premultiplied Alpha vs Straight Alpha
- **Premultiplied (RGB Pré-multiplicado)**: O valor de cor já vem multiplicado pelo canal Alpha: $R' = R \cdot A$, $G' = G \cdot A$, $B' = B \cdot A$.
  - *Vantagem Crítica*: Permite interpolações lineares, filtros de convolução (blur, transformações) e composição sem artefatos escuros de borda (*fringing*).
- **Straight (Unassociated Alpha)**: RGB e Alpha são independentes. Deve ser pré-multiplicado antes de operações de mistura ou filtragem.

### 6.3 Gestão de Cor Linear e Padrão ACES
- O processamento de renderização e composição de luz **deve sempre ocorrer em espaço linear** ($I_{linear} = I_{sRGB}^\gamma$, com $\gamma \approx 2.2$).
- **ACES (Academy Color Encoding System)**: Padrão industrial para gestão de cor com ampla gama (ACEScg para CGI/VFX e ACEScc para gradação de cor).

---

## 🧮 7. Métodos Numéricos para Geometria e Gráficos (Solomon)

### 7.1 Operador de Laplace-Beltrami em Malhas Triangulares 3D
O Laplaciano em superfícies discretas trianguladas governa suavização de malha, parametrização conforme e análise espectral de formas 3D através da fórmula dos cotangentes (*Cotangent Weights*):

$$(\Delta_S f)_i = \frac{1}{2 A_i} \sum_{j \in N(i)} (\cot \alpha_{ij} + \cot \beta_{ij}) (f_i - f_j)$$

onde $A_i$ é a área de Voronoi ao redor do vértice $i$, e $\alpha_{ij}, \beta_{ij}$ são os ângulos opostos à aresta $(i, j)$.

### 7.2 Alinhamento de Formas 3D: Algoritmo ICP (Iterative Closest Point)
Dado conjunto de pontos de origem $\mathcal{P} = \{\mathbf{p}_i\}$ e destino $\mathcal{Q} = \{\mathbf{q}_i\}$:
1. Encontrar o ponto mais próximo $\mathbf{q}_i \in \mathcal{Q}$ para cada $\mathbf{p}_i \in \mathcal{P}$ usando KD-Tree.
2. Calcular a matriz de covariância cruzada centralizada $\mathbf{H} = \sum_{i=1}^N (\mathbf{p}_i - \bar{\mathbf{p}})(\mathbf{q}_i - \bar{\mathbf{q}})^T$.
3. Fatorar via SVD: $\mathbf{H} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$.
4. Rotação ótima: $\mathbf{R} = \mathbf{V} \mathbf{U}^T$ (com correção $\det(\mathbf{R}) = 1$) e translação $\mathbf{t} = \bar{\mathbf{q}} - \mathbf{R} \bar{\mathbf{p}}$.
5. Atualizar $\mathbf{p}_i \leftarrow \mathbf{R}\mathbf{p}_i + \mathbf{t}$ e repetir até convergência $\|\mathbf{e}\| < \epsilon$.
