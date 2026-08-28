---
name: hpc-supercomputing-clusters
description: Especialista em Arquitetura, Engenharia e Operação de Clusters HPC (High Performance Computing) e Supercomputadores baseado na obra Supercomputers for Linux SysAdmins (Sergey Zhumatiy). Cobre gerenciadores de carga (Slurm Workload Manager), interconexões de baixa latência (InfiniBand/RDMA), bibliotecas de paralelismo (OpenMPI, MPICH), sistemas de arquivos paralelos (Lustre, GPFS, Ceph) e computação acelerada por GPUs.
---

# Clusters HPC e Engenharia de Supercomputadores

Esta skill estabelece as diretrizes para projeto, implantação e operação de ambientes de **Computação de Alta Performance (HPC)** e Supercomputadores em Linux, baseando-se no livro de **Sergey Zhumatiy**.

---

## 🚀 1. Topologia de um Cluster HPC

```
                       ┌─────────────────────────┐
                       │  Nó Mestre / Head Node  │
                       │   (Slurm Controller)    │
                       └────────────┬────────────┘
                                    │
           ┌────────────────────────┴────────────────────────┐
   [ Rede de Gerenciamento 10GbE ]           [ Rede InfiniBand / RDMA 200Gbps ]
           │                                                 │
 ┌─────────▼─────────┐                             ┌─────────▼─────────┐
 │ Storage Paralelo  │                             │  Nós de Computo   │
 │ (Lustre / CephFS) │                             │ (CPUs + GPUs H100)│
 └───────────────────┘                             └───────────────────┘
```

---

## 📋 2. Gestão de Jobs com Slurm Workload Manager

### Exemplo de Script de Job em Lote (`submit_job.sh`)
```bash
#!/bin/bash
#SBATCH --job-name=scientific_sim
#SBATCH --output=logs/sim_%j.log
#SBATCH --error=logs/sim_%j.err
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:4
#SBATCH --time=12:00:00
#SBATCH --partition=gpu_cluster

module load openmpi/4.1.5-cuda-12.2

srun --mpi=pmix ./bin/simulation_engine --dataset /shared/lustre/input.dat
```
