---
name: quantum-computing-algorithms
description: Especialista em Computação Quântica, Portas Lógicas e Algoritmos Quânticos baseado na obra Programming Quantum Computers (O'Reilly). Cobre Qubits, Superposição, Entrelaçamento (Entanglement), Esfera de Bloch, portas quânticas (Hadamard, CNOT, Pauli-X/Y/Z, Toffoli), algoritmos clássicos-quânticos (QFT, Grover, Shor, VQE) e desenvolvimento com frameworks Qiskit (IBM) e Cirq (Google).
---

# Computação Quântica e Algoritmos Quânticos

Esta skill estabelece os fundamentos de programação quântica, circuitos lógicos e algoritmos híbridos clássicos-quânticos baseados na obra **Programming Quantum Computers** da O'Reilly.

---

## ⚛️ 1. Fundamentos do Qubit e Esfera de Bloch

- **Qubit**: O estado de um qubit $|\psi\rangle$ é uma combinação linear de estados de base $|0\rangle$ e $|1\rangle$:
  $$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle \quad \text{onde } |\alpha|^2 + |\beta|^2 = 1$$
- **Superposição**: Criada aplicando a porta **Hadamard (H)** sobre o estado base $|0\rangle$:
  $$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}} = |+\rangle$$
- **Entrelaçamento (Entanglement)**: Criado combinando uma porta **Hadamard** com uma porta **CNOT (Controlled-NOT)** para gerar o estado de Bell:
  $$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

---

## 💻 2. Exemplo: Circuito Quântico de Bell State com Qiskit

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Cria circuito com 2 qubits e 2 bits clássicos
qc = QuantumCircuit(2, 2)

# Aplica Hadamard no Qubit 0
qc.h(0)

# Aplica CNOT com Qubit 0 (controle) e Qubit 1 (alvo)
qc.cx(0, 1)

# Mede ambos os qubits nos bits clássicos
qc.measure([0, 1], [0, 1])

# Simula a execução do circuito
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(qc)

# Resultado esperado: ~50% '00' e ~50% '11' (comprovando entrelaçamento)
print("Contagens de Medição:", counts)
```

---

## 📐 3. Algoritmos Quânticos Principais

| Algoritmo | Complexidade Clássica | Complexidade Quântica | Aplicação |
| :--- | :--- | :--- | :--- |
| **Grover's Search** | $O(N)$ | $O(\sqrt{N})$ | Busca não estruturada em bases de dados. |
| **Shor's Algorithm** | Sub-exponencial ($e^{\sqrt{\ln N}}$) | Polinomial ($O((\log N)^3)$) | Fatoração de inteiros e quebra de RSA. |
| **VQE (Variational Quantum Eigensolver)** | Exponencial | Híbrido Clássico-Quântico | Química quântica e modelagem molecular. |
