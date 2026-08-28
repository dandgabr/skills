---
name: "program-containers"
description: "Especialista em tecnologias e ecossistemas de containers (locais e cloud), dominando padrões OCI, Docker, Podman, CRI-O, Buildah, Kubernetes, registries seguros, hardening e orquestração gerenciada em nuvem."
---

# 📦 Habilidade de IA: Tecnologias de Containers (Docker, Podman, CRI-O, Buildah & Kubernetes)

Esta skill orienta a inteligência artificial a atuar como **Especialista em Tecnologias de Containers**, cobrindo o ciclo de vida completo de empacotamento, distribuição, segurança, isolamento em runtime e orquestração de containers em ambientes locais, híbridos e multi-cloud.

---

## 📜 1. Padrão OCI (Open Container Initiative) & Arquitetura de Imagens

A **Open Container Initiative (OCI)** estabelece padrões abertos para formatos de imagens, runtimes e distribuição, garantindo interoperabilidade entre diferentes ferramentas (Docker, Podman, Buildah, containerd, CRI-O).

### Especificações Fundamentais
- **OCI Image Specification**: Define a estrutura de um arquivo de imagem em camadas (tarballs), o arquivo de configuração JSON (metadados de execução, variáveis de ambiente, entrypoint), o **Manifest** (descritor de camadas e config) e o **Manifest List / Image Index** (suporte a múltiplas arquiteturas de CPU, como `amd64`, `arm64`, `riscv64`).
- **OCI Runtime Specification**: Define a configuração do ambiente de execução de um container (`config.json`), o ciclo de vida dos processos (create, start, stop, delete) e a interface utilizada por runtimes de baixo nível como `runc`, `crun` e `youki`.
- **OCI Distribution Specification**: Padroniza a API HTTP/REST para push, pull, autenticação, catalogação e gerenciamento de blobs e manifests entre clientes de container e Registries.

### Anatomia das Camadas e Storage Drivers
- **Imutabilidade e Reutilização**: Imagens são compostas por camadas *read-only* empilhadas via SHA256 content addressability.
- **Copy-on-Write (CoW)**: Ao instanciar um container, uma camada fina gravável (*writable container layer*) é alocada no topo. Modificações em arquivos existentes disparam cópia para a camada superior.
- **OverlayFS (overlay2)**: Storage driver padrão no Linux que combina `lowerdir` (camadas read-only da imagem), `upperdir` (camada read-write do container), `workdir` (área intermediária) e `merged` (visão unificada montada no sistema de arquivos do container).

---

## 🐳 2. Docker & Melhores Práticas de Construção

O **Docker** continua sendo a plataforma de desenvolvimento mais disseminada para criação e execução de containers.

### Melhores Práticas para Dockerfile
1. **Ordem de Instruções e Caching de Camadas**: Posicione instruções raramente alteradas (como instalação de pacotes do SO e download de dependências) antes das instruções que mudam com frequência (cópia de código-fonte).
2. **Utilização Estrita do `.dockerignore`**: Exclua arquivos desnecessários (`.git`, `node_modules`, `target/`, `.env`, logs, documentação) para acelerar o envio do contexto de build e impedir vazamento de segredos.
3. **Execução sem Privilégios (Non-Root)**: Crie um usuário dedicado com UID/GID fixo no container e nunca execute a aplicação como `root` em produção.
4. **Combinação de Comandos**: Combine comandos de instalação e limpeza de cache de pacotes na mesma instrução `RUN` para evitar que arquivos temporários permaneçam gravados em camadas intermediárias.

### Exemplo Prático: Multi-Stage Build Otimizado (Go Backend com Scratch/Distroless)

```dockerfile
# ==========================================
# Stage 1: Build & Compilation Environment
# ==========================================
FROM golang:1.24-alpine AS builder

# Install build dependencies and security certificates
RUN apk add --no-cache ca-certificates git tzdata

# Set working directory
WORKDIR /app

# Optimize layer caching by copying dependencies first
COPY go.mod go.sum ./
RUN go mod download && go mod verify

# Copy application source code
COPY . .

# Compile static binary without CGO dependencies
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build \
    -ldflags="-w -s -X main.version=1.0.0" \
    -trimpath \
    -o /app/server ./cmd/server

# Create a non-privileged user and group for runtime
RUN echo "nonroot:x:65532:65532:nonroot user:/:/sbin/nologin" > /etc/passwd_nonroot

# ==========================================
# Stage 2: Minimal Production Runtime
# ==========================================
FROM scratch AS production

# Copy essential runtime files from builder
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /etc/passwd_nonroot /etc/passwd
COPY --from=builder --chown=65532:65532 /app/server /server

# Use non-privileged user
USER 65532:65532

# Expose service port
EXPOSE 8080

# Configure healthcheck (via executable or API endpoints)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD ["/server", "--healthcheck"] || exit 1

# Set production entrypoint
ENTRYPOINT ["/server"]
```

### Exemplo de `.dockerignore`
```text
.git
.gitignore
.env
.env.*
node_modules
dist
target
bin
*.md
Dockerfile*
docker-compose*.yml
tests/
coverage/
```

### Redes e Volumes no Docker
- **Redes**:
  - `bridge`: Rede padrão isolada para containers na mesma máquina host.
  - `host`: Elimina o isolamento de rede do container, utilizando a interface de rede do host diretamente.
  - `overlay`: Viabiliza comunicação criptografada multi-host (usado no Docker Swarm e orquestradores).
  - `none`: Desabilita completamente interfaces de rede no container.
- **Volumes**:
  - **Named Volumes**: Gerenciados pelo Docker (`/var/lib/docker/volumes`), isolados do filesystem do host e com alta performance.
  - **Bind Mounts**: Mapeamento direto de um caminho do host para dentro do container (ideal para desenvolvimento local com hot-reloading).
  - **tmpfs Mounts**: Armazenamento volátil em memória RAM, ideal para segredos temporários e dados transitórios de alta performance.

### Exemplo Prático: `docker-compose.yml` Completo com Healthchecks e Isolamento

```yaml
version: "3.8"

networks:
  frontend-net:
    driver: bridge
  backend-net:
    driver: bridge
    internal: true # Isolated network without external internet access

volumes:
  postgres-data:
    driver: local

services:
  database:
    image: postgres:16-alpine
    container_name: app-postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: secure_database_password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - backend-net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U appuser -d appdb"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512M

  api-service:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: app-api
    restart: unless-stopped
    depends_on:
      database:
        condition: service_healthy
    environment:
      PORT: 8080
      DATABASE_URL: postgres://appuser:secure_database_password@database:5432/appdb?sslmode=disable
    ports:
      - "8080:8080"
    networks:
      - frontend-net
      - backend-net
    healthcheck:
      test: ["CMD", "/server", "--healthcheck"]
      interval: 15s
      timeout: 3s
      retries: 3
      start_period: 5s
    deploy:
      resources:
        limits:
          cpus: "0.5"
          memory: 256M
```

---

## 🦭 3. Podman (Pod Manager) & Arquitetura Daemonless

O **Podman** é uma engine de containers sem daemon central (*daemonless*) projetada para executar containers e pods de forma segura e com suporte nativo a *rootless*.

### Características Chave do Podman
- **Arquitetura Daemonless**: Utiliza o modelo tradicional fork-exec do Linux. Cada container é um processo filho direto monitorado pelo `conmon` e executado via OCI runtime (`runc` ou `crun`), eliminando o *single point of failure* de um daemon central com privilégios de root.
- **Rootless por Padrão**: Permite que usuários sem privilégios administrativos executem containers com segurança utilizando *User Namespaces* do Linux (`/etc/subuid` e `/etc/subgid`). O usuário é `root (UID 0)` dentro do container, mas mapeado para um UID regular e sem privilégios (ex: `UID 10001`) no host.
- **Conceito de Pods Locais**: Capacidade de criar e gerenciar grupos de containers que compartilham a mesma rede (`localhost`), IPC, namespace UTS e volumes, espelhando a semântica de Pods do Kubernetes:
  ```bash
  # Create a pod with exposed port
  podman pod create --name web-pod -p 8080:80

  # Run container inside the existing pod
  podman run -d --pod web-pod --name nginx-server nginx:alpine
  ```
- **Compatibilidade Docker**: Compatibilidade CLI total via alias `alias docker=podman` e suporte à API Docker via socket de serviço systemd (`podman.socket`).
- **`podman-compose`**: Execução de especificações Compose sem necessidade do daemon do Docker.

### Integração Nativa com Systemd & Quadlets

O Podman permite a geração de unidades systemd (`podman generate systemd`) e adota a tecnologia **Quadlets** como padrão moderno declarativo para gerenciar containers como serviços systemd nativos.

#### Exemplo de Arquivo Quadlet (`~/.config/containers/systemd/api-service.container`)
```ini
[Unit]
Description=Production API Microservice
After=network-online.target

[Container]
Image=ghcr.io/myorg/api-service:v1.0.0
ContainerName=api-microservice
AutoUpdate=registry
PublishPort=8080:8080
Environment=NODE_ENV=production
Environment=PORT=8080
Volume=/var/log/app:/app/logs:Z
Network=host
RunInit=true
SecurityLabelDisable=false

[Service]
Restart=always
TimeoutStartSec=900

[Install]
WantedBy=default.target
```

Para aplicar e iniciar:
```bash
systemctl --user daemon-reload
systemctl --user start api-service
systemctl --user status api-service
```

---

## 🔨 4. Buildah & Construção de Imagens sem Daemon

O **Buildah** é uma ferramenta de linha de comando especializada em construir imagens OCI e Docker sem necessidade de um daemon de container em execução e sem depender de privilégios de root.

### Diferenciais do Buildah
- **Isolamento e Scripting Flexível**: Permite construir imagens usando comandos tradicionais de shell (Bash/Zsh) ou via Dockerfiles (`buildah bud`).
- **Construção `FROM scratch` Absoluta**: Criação de imagens partindo de um filesystem completamente vazio, montando o sistema de arquivos da imagem temporariamente no host para injeção cirúrgica de binários e dependências:
  ```bash
  # Initialize empty container
  new_container=$(buildah from scratch)

  # Mount container filesystem on host
  mount_point=$(buildah mount $new_container)

  # Copy compiled binary and configuration into mounted filesystem
  cp ./my-binary $mount_point/
  chmod 755 $mount_point/my-binary

  # Configure image metadata
  buildah config --entrypoint '["/my-binary"]' $new_container
  buildah config --user 65532:65532 $new_container
  buildah config --created-by "Buildah Script" $new_container

  # Commit image into local storage
  buildah commit --squash $new_container my-minimal-app:latest

  # Unmount and clean temporary container
  buildah unmount $new_container
  buildah rm $new_container
  ```
- **Controle Granular de Camadas**: Controle explícito sobre a criação de camadas (`--layers=false`), possibilitando squash de camadas, inclusão de anotações OCI e redução máxima do tamanho final da imagem.

---

## ⚡ 5. CRI-O & Runtimes Nativos para Kubernetes

O **CRI-O** é uma implementação leve e otimizada da **Container Runtime Interface (CRI)** do Kubernetes, projetada exclusivamente para servir como runtime de containers em nós de clusters Kubernetes.

### Comparativo: CRI-O vs containerd

| Critério | CRI-O | containerd |
| :--- | :--- | :--- |
| **Foco Principal** | Kubernetes exclusivamente | Uso geral (Kubernetes, Docker, CLI local) |
| **Escopo de Funcionalidades** | Apenas o necessário para atender ao CRI | Amplo (suporte a plugins, multi-namespaces, containerd CLI) |
| **Consumo de Recursos** | Mínimo footprint de memória e CPU por nó | Muito baixo, porém ligeiramente mais abrangente |
| **Adotantes Principais** | Red Hat OpenShift, clusters Kubernetes hardened | EKS, GKE, AKS, distribuições Kubernetes padrão |
| **OCI Runtimes Suportados** | `runc`, `crun` (C rápido), `kata-containers` | `runc`, `crun`, `gVisor (runsc)`, `kata` |

### Características de Produção
- **Alinhamento com Versões do Kubernetes**: Cada versão do CRI-O (ex: 1.30) segue rigidamente a versão correspondente do Kubernetes (1.30).
- **Sem Superfície Desnecessária**: Elimina abstrações de CLI de desenvolvedor, focando estritamente em segurança, performance de inicialização de pods e conformidade OCI.

---

## ☸️ 6. Kubernetes Containers & Workloads em Produção

No Kubernetes, o container é a unidade fundamental de execução encapsulada dentro de **Pods**.

### Anatomia e Ciclo de Vida do Pod Spec
- **`initContainers`**: Containers executados sequencialmente antes do início dos containers da aplicação (utilizados para migrações de banco, aguardo de dependências ou download de configurações).
- **`sidecarContainers`** (Sidecars Nativos): Suportados nativamente a partir do Kubernetes 1.28+ via `restartPolicy: Always` em `initContainers` para proxies de rede (Envoy/Istio), coleta de logs (Fluentbit) e agentes de métricas.
- **Resource Management (Requests & Limits)**:
  - `requests`: Recursos mínimos garantidos pelo scheduler do Kubernetes para alocação do Pod no nó.
  - `limits`: Limite rígido imposto pelo cgroups do Linux (CPU throttling quando ultrapassado; OOMKilled se a memória ultrapassar o limit).
  - **Quality of Service (QoS)**: `Guaranteed` (requests = limits), `Burstable` (requests < limits), `BestEffort` (sem requests/limits definidos).

### Hardening com Security Context & Pod Security Standards (PSS)
- **Pod Security Standards**:
  - `Privileged`: Sem restrições (usado para componentes de sistema e CNI).
  - `Baseline`: Previne escalonamento de privilégios conhecido com configuração mínima.
  - `Restricted`: Máximo nível de hardening (non-root obrigatório, filesystem read-only, drop de todas as capabilities).

### Exemplo Prático: Manifesto Kubernetes Hardened (Deployment & Service)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: microservice-payment
  namespace: production
  labels:
    app.kubernetes.io/name: microservice-payment
    app.kubernetes.io/part-of: checkout-platform
spec:
  replicas: 3
  revisionHistoryLimit: 5
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: microservice-payment
  template:
    metadata:
      labels:
        app: microservice-payment
    spec:
      # Pod-level security context
      securityContext:
        runAsNonRoot: true
        runAsUser: 10001
        runAsGroup: 10001
        fsGroup: 10001
        seccompProfile:
          type: RuntimeDefault

      initContainers:
        - name: wait-for-database
          image: busybox:1.36
          command: ['sh', '-c', 'until nc -z -w 2 postgres-service.production.svc.cluster.local 5432; do echo waiting for db; sleep 2; done;']
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          resources:
            requests:
              cpu: 50m
              memory: 32Mi
            limits:
              cpu: 100m
              memory: 64Mi

      containers:
        - name: payment-api
          image: ghcr.io/myorg/payment-api:v2.1.0@sha256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
              name: http-api
              protocol: TCP

          # Container-level security context (Restricted Profile)
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
                - NET_RAW

          resources:
            requests:
              cpu: 250m
              memory: 256Mi
            limits:
              cpu: 500m
              memory: 512Mi

          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 15
            timeoutSeconds: 3
            failureThreshold: 3

          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
            timeoutSeconds: 2
            failureThreshold: 2

          volumeMounts:
            - name: tmp-volume
              mountPath: /tmp

      volumes:
        - name: tmp-volume
          emptyDir:
            medium: Memory
            sizeLimit: 64Mi
---
apiVersion: v1
kind: Service
metadata:
  name: payment-service
  namespace: production
spec:
  type: ClusterIP
  selector:
    app: microservice-payment
  ports:
    - name: http
      port: 80
      targetPort: 8080
      protocol: TCP
```

---

## 🏢 7. Container Registries & Estratégias de Versionamento

Os Registries armazenam, distribuem e controlam o acesso a imagens de container OCI.

### Principais Registries de Produção
- **GitHub Container Registry (`ghcr.io`)**: Integração profunda com GitHub Actions e permissões granulares por organização/repositório.
- **AWS Elastic Container Registry (ECR)**: Alta integração com IAM, KMS, replicação multi-região e scanning nativo via Amazon Inspector.
- **Azure Container Registry (ACR)**: Suporte a private endpoints, georreplicação global e tarefas automáticas de build.
- **Google Artifact Registry (GAR)**: Registry universal no GCP com suporte a OCI, repositórios de pacotes (npm, maven, python) e integração com Artifact Analysis.
- **Harbor (Self-Hosted)**: Registry open-source corporativo da CNCF com RBAC avançado, replicação entre registries, assinatura via Notary/Cosign, auditoria e políticas de retenção.

### Estratégias de Tagging e Imutabilidade
1. **Evitar `:latest` em Produção**: O tag `latest` é mutável e não determinístico, impossibilitando rollbacks confiáveis e rastreabilidade.
2. **Versionamento Semântico (SemVer)**: Tags claras como `v1.2.3`, `v1.2` e `v1`.
3. **Imutabilidade por Git SHA / Commit**: Utilização do commit SHA completo ou abreviado (ex: `sha-a1b2c3d`) vinculado ao pipeline de CI/CD.
4. **Digest Pinning (`@sha256:...`)**: O formato mais seguro para ambientes de missão crítica, garantindo que o payload exato assinado seja executado independentemente de mutações de tags.
5. **Multi-Architecture Builds**: Publicação de manifest lists com Docker Buildx para suportar arquiteturas heterogêneas (`linux/amd64`, `linux/arm64`).

```bash
# Multi-platform build and push using Docker Buildx
docker buildx create --name multiarch-builder --use
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t ghcr.io/myorg/api:v1.2.3 \
  -t ghcr.io/myorg/api:latest \
  --push .
```

---

## 🛡️ 8. Segurança de Containers, Hardening & Supply Chain

A segurança em containers requer abordagem em camadas (*defense-in-depth*), desde o código-fonte até a execução em runtime.

### 1. Escaneamento de Vulnerabilidades (Image Scanning)
- **Trivy**: Scanner de vulnerabilidades em SO, dependências de pacotes de linguagens, segredos e misconfigurations em IaC.
  ```bash
  # Scan container image with failure threshold for Critical/High CVEs
  trivy image --severity HIGH,CRITICAL --exit-code 1 ghcr.io/myorg/api:v1.2.3
  ```
- **Grype**: Scanner rápido desenvolvido pela Anchore focado em CVEs mapeadas em SBOMs.

### 2. Geração de SBOM (Software Bill of Materials)
- **Syft**: Criação de inventários estruturados de componentes e dependências em formatos padronizados (SPDX, CycloneDX).
  ```bash
  # Generate SBOM in CycloneDX JSON format
  syft ghcr.io/myorg/api:v1.2.3 -o cyclonedx-json > sbom.json
  ```

### 3. Assinatura e Verificação Criptográfica (Cosign / Sigstore)
- Assinatura digital de imagens no pipeline de CI/CD sem necessidade de gerenciamento manual de chaves privadas (Keyless signing via OIDC):
  ```bash
  # Sign image using Cosign and Sigstore
  cosign sign --yes ghcr.io/myorg/api:v1.2.3

  # Verify image signature before deployment
  cosign verify --certificate-identity-regexp "https://github.com/myorg/.*" \
    --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
    ghcr.io/myorg/api:v1.2.3
  ```

### 4. Imagens Base Mínimas e Redução de Superfície de Ataque
- **Distroless (`gcr.io/distroless/*`)**: Contém apenas a aplicação e suas dependências de runtime direto, sem shells (`sh`, `bash`), gerenciadores de pacotes (`apt`, `apk`) ou utilitários GNU.
- **Scratch**: Imagem vazia (0 bytes), perfeita para binários estáticos compilados em Go, Rust ou C++.
- **Alpine**: Base minimalista (~5MB) baseada em musl libc e BusyBox (requer atenção a compatibilidades com glibc).

### 5. Hardening de Runtime
- **Remoção de Linux Capabilities**: Remover todas as capabilities (`drop: ["ALL"]`) e adicionar apenas as estritamente necessárias (ex: `CAP_NET_BIND_SERVICE`).
- **Filesystem Read-Only**: Configurar `readOnlyRootFilesystem: true` montando diretórios voláteis (`/tmp`, `/run`) em `emptyDir` isolado.
- **Seccomp & AppArmor/SELinux**: Restringir chamadas de sistema (syscalls) permitidas usando o perfil `RuntimeDefault` ou perfis customizados.

---

## ☁️ 9. Orquestração Cloud & Containers Gerenciados / Serverless

A computação em nuvem oferece modelos variados de abstração para execução de containers.

### 1. Clusters Kubernetes Gerenciados
- **AWS Elastic Kubernetes Service (EKS)**: Control plane gerenciado, integração com AWS IAM Roles for Service Accounts (IRSA), Pod Identity e autoscaling avançado com **Karpenter**.
- **Azure Kubernetes Service (AKS)**: Integração nativa com Microsoft Entra ID (Azure AD), Azure CNI com Cilium e Azure Linux Nodes.
- **Google Kubernetes Engine (GKE)**: Referência em orquestração com modos **Standard** e **Autopilot** (onde o Google gerencia nós, autoscaling, security hardening e bin-packing automaticamente).

### 2. Serviços de Containers Gerenciados & Serverless
- **AWS ECS (Elastic Container Service)**: Orquestrador proprietário de alta performance e baixa complexidade operacional, com suporte a nós EC2 ou **AWS Fargate** (serverless compute engine).
- **Google Cloud Run**: Plataforma serverless baseada em Knative para execução de containers orientados a eventos e requisições HTTP, com suporte a *scale-to-zero* e cobrança estritamente por milissegundo de CPU/memória consumida.
- **Azure Container Apps (ACA)**: Plataforma serverless para microserviços construída sobre Kubernetes, KEDA (event-driven autoscaling), Dapr e Envoy, ideal para microsserviços e background workers.

---

## 📋 10. Checklist de Engenharia de Containers

Ao planejar, construir ou revisar soluções baseadas em containers, valide:

- [ ] **Base Image Mínima**: A imagem utiliza `scratch`, `distroless` ou `alpine` sem ferramentas desnecessárias?
- [ ] **Usuário Não-Root**: O container executa com usuário e grupo sem privilégios (`runAsNonRoot: true`)?
- [ ] **Multi-Stage Build**: O Dockerfile separa o ambiente de compilação do artefato final de produção?
- [ ] **Contexto Limpo**: O arquivo `.dockerignore` está presente e bloqueia segredos, logs e arquivos de teste?
- [ ] **Imutabilidade e Tags**: A imagem é identificada por versão semântica ou digest imutável (sem `:latest`)?
- [ ] **Verificação de Vulnerabilidades**: A imagem foi escaneada por ferramentas como Trivy ou Grype no pipeline de CI?
- [ ] **Assinatura e Proveniência**: A imagem possui assinatura Cosign e SBOM associado?
- [ ] **Healthchecks Declarados**: Probes de liveness, readiness e startup estão configurados com tolerâncias realistas?
- [ ] **Limites de Recursos**: `requests` e `limits` de CPU e memória foram definidos para evitar contenção e starvation no cluster?
- [ ] **Hardening de Runtime**: O container roda com `readOnlyRootFilesystem: true`, `allowPrivilegeEscalation: false` e `capabilities.drop: ["ALL"]`?

---

## 🔗 Habilidades Relacionadas

- [devops-engineer](../../roles/devops-engineer/SKILL.md)
- [program-github](../github/SKILL.md)
- [github-actions](../github-actions/SKILL.md)
- [devsecops-engineer](../../security/ops-architecture/devsecops-engineer/SKILL.md)
