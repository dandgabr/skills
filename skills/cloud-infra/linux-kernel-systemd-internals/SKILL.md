---
name: linux-kernel-systemd-internals
description: Especialista em Arquitetura do Kernel Linux, Subsistema de Inicialização systemd e Administração Avançada de Servidores baseado nas obras systemd for Linux SysAdmins (David Both) e Understanding Linux Kernel Development. Cobre gerenciamento de Units (.service, .socket, .timer, .mount), cgroups v2, journald, namespaces, rede no kernel (Netfilter, eBPF, sockets) e tunagem de performance com sysctl.
---

# Kernel Linux, systemd e Administração Avançada de Sistemas

Esta skill estabelece os padrões e práticas de engenharia de sistemas operacionais Linux, gerenciamento de serviços via **systemd**, controle de recursos com **cgroups v2** e tunagem de rede/kernel documentados por **David Both**, **Lincoln Boucher** e **Christian Benvenuti**.

---

## 🐧 1. Arquitetura do systemd e Tipos de Units

```
┌─────────────────────────────────────────────────────────────┐
│                          systemd (PID 1)                    │
├──────────────┬──────────────┬──────────────┬────────────────┤
│   .service   │   .socket    │    .timer    │     .mount     │
│ (Daemons e   │ (Ativação    │ (Agendamento │ (Pontos de     │
│  Processos)  │  por Rede)   │  preciso)    │  Montagem)     │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

### Anatomia de um Serviço Seguro (`/etc/systemd/system/myapp.service`)
```ini
[Unit]
Description=Plataforma de Microsserviço de Alta Disponibilidade
After=network.target postgresql.service
Requires=postgresql.service

[Service]
Type=notify
ExecStart=/usr/local/bin/myapp --config /etc/myapp/config.yaml
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5s

# Hardening e Isolamento de Segurança
User=appuser
Group=appgroup
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true
PrivateDevices=true
ProtectKernelModules=true
ProtectKernelTunables=true
ProtectControlGroups=true
RestrictRealtime=true
MemoryMax=2G
CPUQuota=200%

[Install]
WantedBy=multi-user.target
```

---

## ⚙️ 2. Tunagem de Performance do Kernel (`/etc/sysctl.d/99-custom.conf`)

| Parâmetro Sysctl | Valor Recomendado | Finalidade |
| :--- | :--- | :--- |
| `net.core.somaxconn` | `65535` | Aumenta o tamanho da fila de conexões pendentes do TCP listener. |
| `net.ipv4.tcp_max_syn_backlog` | `65535` | Protege contra picos de tráfego e SYN flood. |
| `net.ipv4.ip_local_port_range` | `1024 65535` | Expande o range de portas efêmeras para conexões de saída. |
| `vm.swappiness` | `10` | Evita uso agressivo de swap preservando a memória RAM para cache. |
| `fs.file-max` | `2097152` | Limite global de descritores de arquivos abertos. |
