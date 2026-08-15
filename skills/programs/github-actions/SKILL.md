---
name: "program-github-actions"
description: "Atua como especialista em GitHub Actions e CI/CD, dominando workflows YAML, reusable workflows, composite actions, matrix strategies, environments com proteção, autenticação OIDC, caching, container jobs e padrões avançados de automação."
---

# Habilidade de IA: GitHub Actions — CI/CD & Automação

Esta skill orienta a IA a atuar como **especialista em GitHub Actions**, projetando, otimizando e depurando pipelines de CI/CD e automações baseadas em workflows YAML dentro do ecossistema GitHub.

---

## 🎯 Objetivo da Skill

Capacitar a IA para projetar workflows robustos, seguros e escaláveis utilizando GitHub Actions, abrangendo desde pipelines simples até arquiteturas complexas com reusable workflows, OIDC, matrix strategies e GitOps.

---

## 🧭 Quando Ativar

Ative esta skill quando o pedido envolver:
- Criação ou depuração de workflows GitHub Actions (`.github/workflows/*.yml`).
- Reusable workflows (`workflow_call`) ou composite actions (`action.yml`).
- Matrix strategies para testes multi-plataforma ou multi-versão.
- Environments com proteção, revisores e regras de deployment.
- Autenticação OIDC para provedores de nuvem (AWS, Azure, GCP).
- Caching de dependências e otimização de performance de pipelines.
- Container jobs, service containers ou build/push de imagens Docker.
- Padrões avançados como concurrency groups, workflow chaining e dynamic matrices.

---

## 📐 Anatomia de um Workflow

### Estrutura Básica

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
    paths-ignore: ['docs/**', '*.md']
  pull_request:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        default: 'staging'
        type: choice
        options: [staging, production]
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 06:00 UTC

permissions:
  contents: read
  pull-requests: write

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io

jobs:
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run format:check

  test:
    name: Test
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: coverage/
          retention-days: 7
```

### Triggers Disponíveis

| Trigger | Descrição | Caso de Uso |
| :--- | :--- | :--- |
| `push` | Push em branches/tags | CI em merge para main |
| `pull_request` | Abertura/atualização de PR | Validação antes do merge |
| `workflow_dispatch` | Execução manual com inputs | Deploy manual, operações ad-hoc |
| `schedule` | Cron (UTC) | Testes noturnos, scans de segurança |
| `workflow_call` | Chamado por outro workflow | Reusable workflows |
| `repository_dispatch` | Evento externo via API | Integração com sistemas externos |
| `release` | Publicação de release | Build e publicação de artefatos |

---

## 🔄 Reusable Workflows

Reusable workflows encapsulam **jobs inteiros** e são reutilizados em nível organizacional para padronizar pipelines.

### Workflow Reutilizável (Callee)

```yaml
# .github/workflows/reusable-deploy.yml
name: Reusable Deploy

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
      image-tag:
        required: true
        type: string
      dry-run:
        required: false
        type: boolean
        default: false
    secrets:
      DEPLOY_TOKEN:
        required: true
    outputs:
      deployment-url:
        description: "URL of the deployed application"
        value: ${{ jobs.deploy.outputs.url }}

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    outputs:
      url: ${{ steps.deploy.outputs.url }}
    steps:
      - uses: actions/checkout@v4

      - name: Deploy application
        id: deploy
        run: |
          if [ "${{ inputs.dry-run }}" = "true" ]; then
            echo "DRY RUN: would deploy ${{ inputs.image-tag }} to ${{ inputs.environment }}"
            echo "url=https://dry-run.example.com" >> "$GITHUB_OUTPUT"
          else
            # Real deployment logic
            echo "url=https://${{ inputs.environment }}.example.com" >> "$GITHUB_OUTPUT"
          fi
        env:
          TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

### Workflow Chamador (Caller)

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to Production

on:
  push:
    tags: ['v*']

jobs:
  deploy-staging:
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: staging
      image-tag: ${{ github.ref_name }}
    secrets:
      DEPLOY_TOKEN: ${{ secrets.STAGING_TOKEN }}

  deploy-production:
    needs: deploy-staging
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: production
      image-tag: ${{ github.ref_name }}
    secrets:
      DEPLOY_TOKEN: ${{ secrets.PROD_TOKEN }}
```

### Boas Práticas para Reusable Workflows

- **Versionamento**: Use `org/repo/.github/workflows/deploy.yml@v1` (tag) ou `@sha` em produção.
- **Secrets**: Prefira `secrets: inherit` apenas em repositórios internos. Em repositórios abertos, passe secrets explicitamente.
- **Organização**: Mantenha reusable workflows em um repositório central (`.github` da organização).
- **OIDC Claims**: `job_workflow_ref` permite restringir trust policies a workflows específicos.

---

## 🧩 Composite Actions

Composite Actions encapsulam **steps reutilizáveis** dentro de um único action.

### Estrutura de uma Composite Action

```yaml
# .github/actions/setup-project/action.yml
name: 'Setup Project'
description: 'Sets up Node.js, installs dependencies, and restores cache'

inputs:
  node-version:
    description: 'Node.js version to install'
    required: false
    default: '20'
  working-directory:
    description: 'Working directory for npm commands'
    required: false
    default: '.'

outputs:
  cache-hit:
    description: 'Whether the cache was hit'
    value: ${{ steps.cache.outputs.cache-hit }}

runs:
  using: 'composite'
  steps:
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}

    - name: Get npm cache directory
      id: npm-cache-dir
      shell: bash
      run: echo "dir=$(npm config get cache)" >> "$GITHUB_OUTPUT"

    - name: Restore npm cache
      id: cache
      uses: actions/cache@v4
      with:
        path: ${{ steps.npm-cache-dir.outputs.dir }}
        key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
        restore-keys: ${{ runner.os }}-npm-

    - name: Install dependencies
      shell: bash
      working-directory: ${{ inputs.working-directory }}
      run: npm ci
```

### Uso da Composite Action

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ./.github/actions/setup-project
        with:
          node-version: '20'
      - run: npm run build
```

### Diferenças Chave

| Aspecto | Reusable Workflow | Composite Action |
| :--- | :--- | :--- |
| Escopo | Job(s) inteiro(s) | Steps dentro de um job |
| Trigger | `workflow_call` | `uses` em steps |
| Secrets | Suporta herança/passagem | Apenas via `inputs` |
| Runners | Pode definir `runs-on` | Herda runner do job |
| Marketplace | Não publicável | Publicável |

---

## 🔢 Matrix Strategy

Matrix permite executar jobs em paralelo com combinações de parâmetros.

### Multi-plataforma e Multi-versão

```yaml
jobs:
  test:
    name: Test (${{ matrix.os }}, Node ${{ matrix.node }})
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      max-parallel: 6
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [18, 20, 22]
        include:
          - os: ubuntu-latest
            node: 22
            coverage: true
        exclude:
          - os: macos-latest
            node: 18
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm ci
      - run: npm test
      - if: matrix.coverage
        run: npm run test:coverage

  # Matrix with reusable workflow
  deploy-multi-region:
    strategy:
      max-parallel: 1
      matrix:
        region: [us-east-1, eu-west-1, ap-southeast-1]
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: production-${{ matrix.region }}
      image-tag: ${{ github.sha }}
    secrets: inherit
```

### Dynamic Matrix

```yaml
jobs:
  generate-matrix:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - uses: actions/checkout@v4
      - id: set-matrix
        run: |
          # Detect changed services in a monorepo
          SERVICES=$(find services/ -name 'package.json' -maxdepth 2 \
            | xargs -I{} dirname {} \
            | jq -R -s -c 'split("\n")[:-1]')
          echo "matrix={\"service\":${SERVICES}}" >> "$GITHUB_OUTPUT"

  build:
    needs: generate-matrix
    runs-on: ubuntu-latest
    strategy:
      matrix: ${{ fromJson(needs.generate-matrix.outputs.matrix) }}
    steps:
      - uses: actions/checkout@v4
      - run: echo "Building ${{ matrix.service }}"
```

---

## 🌍 Environments & Deployments

Environments controlam proteção, aprovação e rastreabilidade de deployments.

### Configuração de Environments

```yaml
jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying to staging"

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    concurrency:
      group: production-deploy
      cancel-in-progress: false
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying to production"
```

### Regras de Proteção (via Settings)

| Regra | Descrição |
| :--- | :--- |
| **Required reviewers** | Aprovação manual antes do deploy |
| **Wait timer** | Delay (minutos) antes do deploy |
| **Deployment branches** | Restringe quais branches podem fazer deploy |
| **Custom rules** | Integração com sistemas externos de aprovação |

---

## 🔐 Secrets & Segurança OIDC

### Hierarquia de Secrets

```
Organization Secrets → Repository Secrets → Environment Secrets
(menor precedência)                         (maior precedência)
```

### Autenticação OIDC (sem secrets de longa duração)

```yaml
jobs:
  deploy-aws:
    runs-on: ubuntu-latest
    permissions:
      id-token: write   # Required for OIDC
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials via OIDC
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: us-east-1

      - name: Deploy to S3
        run: aws s3 sync ./dist s3://my-bucket/

  deploy-azure:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: Azure Login via OIDC
        uses: azure/login@v2
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

  deploy-gcp:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: GCP Auth via OIDC
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: 'projects/123/locations/global/workloadIdentityPools/pool/providers/gh'
          service_account: 'deploy@project.iam.gserviceaccount.com'
```

### Bloco `permissions` — Princípio de Menor Privilégio

```yaml
# Top-level: restrict all by default
permissions: read-all

# Job-level: grant only what is needed
jobs:
  build:
    permissions:
      contents: read
      packages: write
```

### Boas Práticas de Segurança

1. **Prefira OIDC**: Elimine credenciais de longa duração para provedores de nuvem.
2. **Pin por SHA**: Use `uses: actions/checkout@<sha>` em vez de `@v4` para segurança máxima.
3. **`permissions` explícito**: Sempre defina o bloco no nível do workflow.
4. **Dependabot para Actions**: Configure alertas para atualizações de actions no `dependabot.yml`.
5. **Audit log**: Monitore execuções via API de audit log da organização.

---

## 📦 Caching & Artifacts

### Cache de Dependências

```yaml
steps:
  # npm
  - uses: actions/setup-node@v4
    with:
      node-version: '20'
      cache: 'npm'  # Built-in caching

  # pip (manual)
  - uses: actions/cache@v4
    with:
      path: ~/.cache/pip
      key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
      restore-keys: ${{ runner.os }}-pip-

  # Gradle
  - uses: actions/cache@v4
    with:
      path: |
        ~/.gradle/caches
        ~/.gradle/wrapper
      key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}

  # Docker layers
  - uses: docker/build-push-action@v6
    with:
      context: .
      cache-from: type=gha
      cache-to: type=gha,mode=max
```

### Upload/Download de Artifacts

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: dist-${{ github.sha }}
          path: dist/
          retention-days: 5
          compression-level: 9

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: dist-${{ github.sha }}
          path: dist/
      - run: echo "Deploying from artifact"
```

---

## 🐳 Container Jobs & Service Containers

### Job em Container

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: node:20-slim
      env:
        NODE_ENV: test
      options: --user root

    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: testdb
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

      redis:
        image: redis:7
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
        env:
          DATABASE_URL: postgresql://test:test@postgres:5432/testdb
          REDIS_URL: redis://redis:6379
```

### Build & Push Docker

```yaml
jobs:
  build-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4

      - uses: docker/setup-buildx-action@v3

      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=sha,prefix=
            type=ref,event=branch
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}

      - uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          platforms: linux/amd64,linux/arm64
```

---

## ⚡ Padrões Avançados

### Concurrency Groups

```yaml
# Cancel stale runs on PR update
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}
```

### Conditional Execution

```yaml
steps:
  - name: Deploy only on main
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    run: ./deploy.sh

  - name: Run only if previous step failed
    if: failure()
    run: ./notify-failure.sh

  - name: Always run cleanup
    if: always()
    run: ./cleanup.sh

  - name: Skip for Dependabot PRs
    if: github.actor != 'dependabot[bot]'
    run: npm run e2e
```

### Workflow Chaining (repository_dispatch)

```yaml
# Trigger from another workflow
- name: Trigger downstream
  uses: peter-evans/repository-dispatch@v3
  with:
    token: ${{ secrets.PAT }}
    repository: org/deploy-repo
    event-type: deploy-request
    client-payload: '{"ref": "${{ github.sha }}", "env": "production"}'
```

### Self-Hosted Runners

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux, gpu]
    steps:
      - uses: actions/checkout@v4
      - run: nvidia-smi
      - run: python train.py
```

### Workflow Completo — CI/CD com Release

```yaml
name: Release Pipeline

on:
  push:
    tags: ['v*.*.*']

permissions:
  contents: write
  packages: write
  id-token: write

jobs:
  test:
    uses: ./.github/workflows/reusable-test.yml

  build:
    needs: test
    runs-on: ubuntu-latest
    outputs:
      image-digest: ${{ steps.build.outputs.digest }}
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - id: build
        uses: docker/build-push-action@v6
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.ref_name }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  sign:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: sigstore/cosign-installer@v3
      - run: cosign sign --yes ghcr.io/${{ github.repository }}@${{ needs.build.outputs.image-digest }}

  deploy:
    needs: [build, sign]
    strategy:
      max-parallel: 1
      matrix:
        env: [staging, production]
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: ${{ matrix.env }}
      image-tag: ${{ github.ref_name }}
    secrets: inherit

  release:
    needs: deploy
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: softprops/action-gh-release@v2
        with:
          generate_release_notes: true
          draft: false
```

---

## ⚙️ Regras de Decisão

- **Prefira reusable workflows** para padronizar pipelines inteiros em uma organização.
- **Prefira composite actions** para agrupar steps repetitivos reutilizáveis em múltiplos jobs.
- **Use OIDC** em vez de secrets de longa duração para autenticação em provedores de nuvem.
- **Pin actions por SHA** em pipelines de produção para evitar supply-chain attacks.
- **Defina `permissions`** explicitamente no nível do workflow — nunca confie nos defaults.
- **Use `concurrency`** para cancelar runs obsoletas e economizar minutos de runner.
- **Cache agressivamente**: camadas Docker (GHA cache), dependências (`actions/cache`), e builds intermediários.

---

## 🔗 Habilidades Relacionadas

- [program-github](../github/SKILL.md): use para dominar a plataforma GitHub como um todo — repositórios, PRs, Issues, Packages, Codespaces, segurança e API.
- [containers](../containers/SKILL.md): use quando o pipeline envolver build, scan, sign ou push de imagens OCI (Docker, Podman, Buildah).
- [devops-engineer](../../general/roles/devops-engineer/SKILL.md): use quando o contexto envolver Terraform, Ansible, Kubernetes, Backstage ou estratégias de deploy.
- [devsecops-engineer](../../security/ops-architecture/devsecops-engineer/SKILL.md): use quando o pipeline precisar incluir SAST, SCA, secret scanning ou hardening de segurança.
