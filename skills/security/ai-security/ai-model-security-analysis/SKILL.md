---
name: ai-model-security-analysis
description: >-
  Use this skill when evaluating, auditing, or scanning the security of AI models.
  This includes checking for digital security vulnerabilities (e.g., pickle exploits, malicious code execution)
  as well as behavioral safety and alignment (e.g., toxicity, bias, jailbreak susceptibility).
---

# AI Model Security Analysis

This skill provides guidelines and procedures for assessing the security posture of an AI model, divided into digital infrastructure security (cibersegurança) and behavioral safety/alignment.

## 1. Digital and Code Security Analysis
Before loading or running any model weights locally or on a server, verify the integrity of the files to prevent remote code execution (RCE) and malware.

### Checklist & Steps:
1.  **Format Verification:**
    *   Check if the model uses the `.safetensors` format. **Always prefer `.safetensors` over `.bin`, `.pt`, or `.pkl`**.
    *   If only PyTorch pickle files (`.bin`, `.pkl`) are available, do not load them without scanning first.
2.  **Pickle Scanning:**
    *   Use static analysis tools like `picklescan` to scan files for dangerous imports (e.g., `os.system`, `eval`, `subprocess`) before loading.
    *   Scan command suggestion: `picklescan --path /path/to/model/directory`
3.  **Code Inspection (`trust_remote_code`):**
    *   Check the repository for custom PyTorch modules or Python scripts (`*.py`) shipped alongside the weights.
    *   If a model requires `trust_remote_code=True` to load, inspect the model file (often `modeling_*.py`) line-by-line for external HTTP requests, obfuscated code, or shell execution.
4.  **Malware & File Integrity:**
    *   Check for security badges on Hugging Face (such as the Protect AI scan status).
    *   Verify the hash/commit revision of the model to ensure you are downloading a verified version and prevent model poisoning.

## 2. Behavioral Safety & Alignment Analysis (AI Safety)
Evaluate the safety of the model's outputs under normal and adversarial conditions.

### Checklist & Steps:
1.  **Toxicity & Bias Evaluation:**
    *   Utilize Hugging Face's `evaluate` library to run toxicity scoring.
    *   Evaluate performance against datasets like **StereoSet** or **Jigsaw Toxic Comments**.
2.  **Adversarial Robustness (Jailbreak Resistance):**
    *   Test the model using adversarial prompts (Red Teaming) from benchmarks like **AdvBench** or **DecodingTrust**.
    *   Check if the model is susceptible to system prompt bypass, roleplay jailbreaks, or multilingual prompt injection.
3.  **Exaggerated Safety Audit:**
    *   Verify if the model is over-refusing benign prompts (e.g., refusing to explain "how to kill a process" in Linux because of the word "kill").
4.  **Data Privacy:**
    *   Check if the model has a tendency to leak personally identifiable information (PII) from its training data.
