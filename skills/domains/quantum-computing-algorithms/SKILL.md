---
name: quantum-computing-algorithms
description: "Especialista em Mecânica Quântica Avançada, Física Teórica, Circuitos Quânticos e Algoritmos Quânticos baseado em J. J. Sakurai (Modern Quantum Mechanics), Claude Cohen-Tannoudji (Quantum Mechanics) e Michael A. Nielsen & Isaac L. Chuang (Quantum Computation and Quantum Information). Cobre Formalismo de Dirac no Espaço de Hilbert, Oscilador Harmônico Quântico via Operadores Escada, Momento Angular e Spin 1/2 (Matrizes de Pauli, Coeficientes de Clebsch-Gordan), Teoria de Perturbações e Regra de Ouro de Fermi, Fundamentos do Qubit e Esfera de Bloch, Portas Quânticas Universais (Hadamard, Pauli-X/Y/Z, Phase-S/T, CNOT, Toffoli), Entrelaçamento Quântico (Estados de Bell, GHZ), Transformada Quântica de Fourier (QFT), Algoritmo de Shor (Fatoração Polinomial), Algoritmo de Grover (Busca com Aceleração Quadrática), Variational Quantum Eigensolver (VQE para Química Quântica) e Implementação Prática com Qiskit (IBM) e Cirq (Google)."
---

# Mecânica Quântica, Informação Quântica e Algoritmos Quânticos

Esta skill estabelece a fundamentação física em espaços de Hilbert, álgebra de operadores e portas lógicas quânticas, unificando a mecânica quântica teórica (**Sakurai & Cohen-Tannoudji**) com a ciência da computação quântica (**Nielsen & Chuang** e ecossistemas Qiskit/Cirq).

---

## ⚛️ 1. Formalismo de Dirac no Espaço de Hilbert $\mathcal{H}$

### 1.1 Vetores de Estado, Postulados e Álgebra de Pauli
- **Equação de Schrödinger**:
  $$i\hbar \frac{d}{dt} |\psi(t)\rangle = \hat{H} |\psi(t)\rangle \implies |\psi(t)\rangle = e^{-i\hat{H}t/\hbar} |\psi(0)\rangle$$
- **Spin 1/2 e Matrizes de Pauli $\boldsymbol{\sigma}$**:
  $$\hat{\mathbf{S}} = \frac{\hbar}{2}\boldsymbol{\sigma}, \quad \sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad \sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad \sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$
  com comutação $[\sigma_i, \sigma_j] = 2i\varepsilon_{ijk} \sigma_k$ e anti-comutação $\{\sigma_i, \sigma_j\} = 2\delta_{ij} I$.

### 1.2 Teoria de Perturbações e Regra de Ouro de Fermi
Para um sistema submetido a uma perturbação harmônica $\hat{V}(t) = \hat{V} e^{-i\omega t}$, a taxa de transição por unidade de tempo para um contínuo de estados com densidade $\rho(E_f)$ é dada pela **Regra de Ouro de Fermi**:
$$W_{i \to f} = \frac{2\pi}{\hbar} |\langle f | \hat{V} | i \rangle|^2 \rho(E_f)$$

---

## 🌐 2. Qubits, Esfera de Bloch e Portas Quânticas Universais

```
                 |0⟩ (Polo Norte)
                   ▲
                   │     / (vetor de estado |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩)
                   │    /
                   │   /
                   │  /
                   │ /
  ─────────────────┼─────────────────► Y
                  /│
                 / │
                /  │
               ▼   ▼
              X   |1⟩ (Polo Sul)
```

- **Qubit**: $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$.
- **Porta Hadamard ($H$)**: Cria superposição balanceada $H|0\rangle = |+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$, $H|1\rangle = |-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$.
- **Porta CNOT ($CX$) e Estado de Bell**:
  $$\text{CNOT}(H \otimes I)|00\rangle = |\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

---

## 💻 3. Simulação e Circuitos com Qiskit

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Circuito Quântico de Entrelaçamento Máximo (Bell State)
qc = QuantumCircuit(2, 2)
qc.h(0)          # Superposição no Qubit 0
qc.cx(0, 1)      # Entrelaçamento controlado (Q0 -> Q1)
qc.measure([0, 1], [0, 1])

# Execução em simulador quântico
simulator = AerSimulator()
compiled_qc = transpile(qc, simulator)
job = simulator.run(compiled_qc, shots=2048)
counts = job.result().get_counts(qc)
print("Distribuição das Medições:", counts)
# Saída esperada: ~50% '00' e ~50% '11'
```

---

## 📐 4. Algoritmos Quânticos Fundamentais

| Algoritmo | Complexidade Clássica | Complexidade Quântica | Impacto & Aplicação |
| :--- | :---: | :---: | :--- |
| **Shor's Algorithm** | Sub-exponencial $\mathcal{O}(e^{c \sqrt[3]{\ln N (\ln \ln N)^2}})$ | Polinomial $\mathcal{O}((\log N)^3)$ | Quebra de criptografia RSA/ECC via Transformada Quântica de Fourier (QFT) para estimativa de fase. |
| **Grover's Search** | Linear $\mathcal{O}(N)$ | Quadrática $\mathcal{O}(\sqrt{N})$ | Busca em base não-estruturada via amplificação de amplitude por inversão sobre a média. |
| **VQE (Variational Quantum Eigensolver)** | Exponencial $\mathcal{O}(2^n)$ | Híbrido Clássico-Quântico | Minimização variacional da energia do estado fundamental $\langle \psi(\theta) | \hat{H} | \psi(\theta) \rangle$ para química quântica e novos materiais. |
| **QPE (Quantum Phase Estimation)** | Exponencial | Polinomial $\mathcal{O}(n^2)$ | Determinação dos autovalores unitários de $\hat{U}|\psi\rangle = e^{2\pi i \theta}|\psi\rangle$. |
