---
name: vcs-repository-management
description: Especialista em Sistemas de Controle de Versão (VCS) e Gestão Avançada de Repositórios. Domina Git de baixo nível (DAG, objetos, reflog, worktrees, sparse-checkout, LFS, submodules, bisect, filter-repo), Subversion/SVN (arquitetura FSFS, trunk/branches/tags, svn:mergeinfo, svn:externals, svnadmin, hooks), Mercurial (Hg), estratégias de branching (Trunk-based, GitFlow), migração de repositórios legados para Git e escalabilidade de monorepos (Scalar).
---

# 🛠️ vcs-repository-management: Engenharia Avançada de Controle de Versão e Gestão de Repositórios

Esta habilidade fornece os padrões de engenharia, arquitetura de dados de controle de versão, administração de repositórios e técnicas de migração entre ecossistemas VCS distribuídos (Git, Mercurial) e centralizados (Subversion, Perforce).

---

## 1. Fundamentos e Mecânica Interna do Git

### 1.1. Estrutura de Dados em Grafo Acíclico Dirigido (DAG)
O Git é um sistema de arquivos indexado por conteúdo (*content-addressable filesystem*). Toda informação é armazenada no banco de objetos (`.git/objects/`) identificada pelo hash criptográfico SHA-1 (40 caracteres hexadecimais) ou SHA-256 (64 caracteres hexadecimais):
- **`blob` (Binary Large Object)**: Armazena apenas os dados brutos de um arquivo, desprovido de nome, permissões ou data.
- **`tree`**: Representa um diretório. Mapeia identificadores de objetos (`blob` ou sub-`tree`), modos de permissão POSIX (`100644`, `100755`, `040000`) e nomes de arquivos.
- **`commit`**: Aponta para a `tree` raiz de um snapshot, referencia zero ou mais commits pais (`parent`), identifica autor e committer (com timestamp e fuso horário) e contém a mensagem explicativa.
- **`tag` (Anotada)**: Objeto permanente apontando para um commit específico, contendo tagger, timestamp, mensagem e opcionalmente assinatura criptográfica GPG/SSH.

```text
  [Commit C2] ──── parent ────> [Commit C1]
      │                             │
    tree                          tree
      ▼                             ▼
   [Tree T2]                    [Tree T1]
   ├── blob B1 (modificado)     ├── blob B1 (versão inicial)
   └── tree Sub                 └── blob B2
        └── blob B3
```

### 1.2. O Índice (Staging Area) e Mecanismo de Commits
O índice (`.git/index`) é uma estrutura binária em disco que representa o próximo snapshot planejado. As alterações migram entre os três estados fundamentais:
1. **Working Tree**: Arquivos no diretório de trabalho local.
2. **Index / Staging**: Árvore intermediária preparada via `git add`.
3. **Repository (HEAD)**: Histórico imutável de snapshots commitados no branch atual.

### 1.3. Otimização de Armazenamento e Delta Compression (Packfiles)
O Git armazena objetos inicialmente como objetos soltos (*loose objects* comprimidos via zlib). Quando o volume cresce, aciona o empacotamento (*packing*):
- **Packfile (`.pack`)**: Arquivo consolidado onde objetos semelhantes são armazenados através de compressão diferencial (deltas bidirecionais baseados no algoritmo de Rabin Fingerprint).
- **Index do Packfile (`.idx`)**: Tabela hash que mapeia SHA para offsets exatos dentro do `.pack`, permitindo busca $O(1)$.
- **Comandos de Manutenção**:
  ```bash
  # Verificação de integridade estrutural e objetos órfãos
  git fsck --full --strict
  
  # Repacotamento agressivo com compactação máxima
  git gc --aggressive --prune=now
  git repack -a -d -f --depth=250 --window=250
  ```

---

## 2. Manipulação Avançada de Histórico e Forense

### 2.1. Rebase Interativo e Higienização de Histórico
Permite refinar commits antes do compartilhamento com o time, garantindo commits atômicos e descritivos:
```bash
# Iniciar rebase interativo dos últimos 5 commits
git rebase -i HEAD~5
```
**Comandos do Rebase Interativo**:
- `pick`: Mantém o commit inalterado.
- `reword`: Altera apenas a mensagem do commit.
- `edit`: Interrompe a execução para permitir emendas no código (`git commit --amend`).
- `squash`: Funde o commit com o anterior, combinando as mensagens.
- `fixup`: Funde o commit com o anterior descartando a mensagem atual (ideal para correções rápidas com `git commit --fixup <SHA>`).
- `drop`: Remove completamente o commit do histórico.

### 2.2. O Reflog (Reference Log) e Recuperação de Desastres
O `git reflog` rastreia todas as atualizações de ponteiros de branches e `HEAD` nos últimos 90 dias (por padrão):
```bash
# Inspecionar histórico de movimentações da HEAD
git reflog show HEAD

# Restaurar commit acidentalmente deletado via reset hard
git reset --hard HEAD@{2}

# Resgatar branch deletada a partir do SHA identificado no reflog
git checkout -b branch-restaurada e4a81c2
```

### 2.3. Depuração Bissexual Automatizada (`git bisect`)
Localiza o commit exato que introduziu uma regressão através de busca binária $O(\log n)$ no histórico:
```bash
# Iniciar sessão de bisect
git bisect start
git bisect bad HEAD              # Versão atual está com defeito
git bisect good v2.4.0           # Versão v2.4.0 estava íntegra

# Execução 100% automatizada com script de teste de saída (exit 0 = good, exit != 0 = bad)
git bisect run pytest tests/unit/test_payment.py
```

### 2.4. Purga Forense com `git-filter-repo`
Substituto moderno, seguro e ordens de magnitude mais rápido que o obsoleto `git filter-branch`:
```bash
# Instalação
pip install git-filter-repo

# 1. Purgar arquivo sensível (.env ou chave privada) de TODO o histórico
git-filter-repo --invert-paths --path secrets.env --path id_rsa

# 2. Purgar arquivos maiores que 50MB que entraram indevidamente no histórico
git-filter-repo --strip-blobs-bigger-than 50M

# 3. Reescrever histórico alterando e-mails ou nomes de autores
git-filter-repo --mailmap my-mailmap.txt
```

---

## 3. Gestão de Workspaces, Dependências e Monorepos

### 3.1. Múltiplas Árvores de Trabalho com `git worktree`
Permite alternar de contexto ou rodar testes longos sem precisar de `git stash` ou clonar o repositório novamente:
```bash
# Criar uma worktree isolada para hotfix em diretório paralelo
git worktree add ../hotfix-auth-service hotfix/login-bug

# Listar worktrees ativas
git worktree list

# Remover worktree concluída
git worktree remove ../hotfix-auth-service
git worktree prune
```

### 3.2. Clones Leves e `sparse-checkout` para Monorepos Gigantes
Para repositórios de dezenas de gigabytes, evite baixar todo o histórico e árvores:
```bash
# Clone sem blobs (baixa apenas a árvore e histórico de commits; blobs baixados sob demanda)
git clone --filter=blob:none https://github.com/org/monorepo.git

# Clone raso com profundidade limitada
git clone --depth=1 --no-single-branch https://github.com/org/monorepo.git

# Sparse-checkout em modo cone (baixa apenas pastas selecionadas)
git sparse-checkout init --cone
git sparse-checkout set services/payment services/auth shared/libs
```

### 3.3. Git LFS (Large File Storage)
Mantém ponteiros de texto no Git e os arquivos binários volumosos (vídeos, modelos de ML, datasets) em servidores de storage dedicados:
```bash
# Inicializar LFS no repositório
git lfs install

# Rastrear extensões de binários
git lfs track "*.onnx" "*.zip" "*.tar.gz" "*.mp4"
git add .gitattributes

# Validar arquivos gerenciados pelo LFS
git lfs ls-files
```

### 3.4. Git Submodules vs. Git Subtree
- **Submodules**: Aponta para um commit específico de um repositório remoto via arquivo `.gitmodules`. Menor acoplamento, mas exige gerenciamento explícito (`git submodule update --init --recursive`).
- **Subtrees**: Mescla o histórico de outro repositório diretamente em uma subpasta do repositório principal sem alterar metadados de clonagem. Maior facilidade para desenvolvedores downstream (`git subtree add --prefix=vendor/lib https://github.com/org/lib.git main --squash`).

---

## 4. Arquitetura e Engenharia de Subversion (SVN)

### 4.1. Paradigma Centralizado e Backend FSFS
Diferente do Git (onde todo clone possui todo o histórico), o SVN opera em modelo cliente-servidor centralizado:
- **Revisões Globais Atômicas**: Cada commit incrementa um número de revisão inteiro global ($r1, r2, \dots, rN$) que representa o estado completo de todo o sistema de arquivos na árvore do servidor.
- **FSFS (Filesystem on Filesystem)**: Mecanismo de persistência baseado em arquivos planos que agrupa revisões em shards para alta tolerância a falhas.
- **Peg Revisions vs. Operative Revisions**:
  - `svn cat -r 15 foo.c@10`: Mostra o arquivo `foo.c` como ele existia na revisão operativa 15, rastreando a linhagem do arquivo denominado `foo.c` na revisão peg 10 (resolvendo renomeações e deleções passadas).

### 4.2. Convenção Canônica de Diretórios no SVN
```text
meu-projeto/
├── trunk/            # Linha principal de desenvolvimento contínuo (HEAD)
├── branches/         # Bifurcações temporárias para features, manutenções ou releases
│   ├── feature-pix/
│   └── release-2.0/
└── tags/             # Cópias estáticas e congeladas de releases específicos (ex: v1.0.0)
```
No SVN, branches e tags são **cópias baratas** (*cheap copies* / cópias com cópia na escrita — Copy-on-Write) criadas pelo comando `svn copy`.

### 4.3. Propriedades de Versão (`svn:props`)
Metadados versionados anexados a arquivos e diretórios:
- **`svn:ignore`**: Equivalente ao `.gitignore`, define padrões ignorados localmente.
- **`svn:keywords`**: Expansão de variáveis no código (ex.: `$Id$`, `$Date$`, `$Revision$`).
- **`svn:eol-style`**: Normalização de quebras de linha (`LF`, `CRLF` ou `native`).
- **`svn:externals`**: Mapeia repositórios ou pastas externas dentro da árvore local (análogo aos submodules do Git).
- **`svn:mergeinfo`**: Rastreia quais intervalos de revisão foram mesclados entre branches para evitar repetição de conflitos.

### 4.4. Administração de Repositórios SVN (`svnadmin`)
```bash
# Criar novo repositório com backend FSFS
svnadmin create /var/svn/repos/financeiro --fs-type fsfs

# Realizar backup completo (dump stream)
svnadmin dump /var/svn/repos/financeiro > backup_financeiro.dump

# Restaurar ou carregar histórico em repositório novo
svnadmin load /var/svn/repos/novo_financeiro < backup_financeiro.dump

# Verificação de integridade do banco FSFS
svnadmin verify /var/svn/repos/financeiro

# Sincronização e espelhamento contínuo entre servidores
svnsync initialize https://svn-mirror.local/repos/financeiro https://svn-master.local/repos/financeiro
svnsync sync https://svn-mirror.local/repos/financeiro
```

### 4.5. Hooks de Servidor SVN
Scripts executados no servidor acionados por eventos de commit e controle transacional:
- **`pre-commit`**: Executado dentro de uma transação antes da confirmação. Pode abortar o commit retornando status code != 0 e emitindo mensagem de erro no `stderr`.
  ```bash
  #!/bin/bash
  # Validação de mensagem de commit não vazia
  REPOS="$1"
  TXN="$2"
  LOGMSG=$(svnlook log -t "$TXN" "$REPOS")
  if [ -z "$LOGMSG" ]; then
      echo "ERRO: Commits sem mensagem explicativa são proibidos." >&2
      exit 1
  fi
  ```
- **`post-commit`**: Executado após a confirmação para disparar webhooks, e-mails ou gatilhos de build CI/CD.

---

## 5. Mercurial (Hg) e Perforce Helix Core

### 5.1. Mercurial (Hg)
- **Estrutura Revlog**: Armazena histórico em arquivos append-only com index (`.i`) e dados (`.d`), garantindo leituras e escritas rápidas.
- **Fases de Mutabilidade**:
  - `public`: Commits compartilhados publicamente, imutáveis por padrão.
  - `draft`: Commits locais, ainda passíveis de rebase ou emendas.
  - `secret`: Commits privados que nunca são propagados durante o `hg push`.
- **Extensões Oficiais**: `evolve` (evolução distribuída de histórico sem quebra de commits) e `hg-git` (interoperabilidade nativa com remotos Git).

### 5.2. Perforce Helix Core
- Sistema centralizado de alta performance, padrão em indústrias de jogos e semicondutores para arquivos binários multimídia gigantes (terabytes).
- Utiliza **Client Workspaces** mapeadas para **Depots**, gerencia alterações por **Changelists** atômicas numeradas e implementa controle de concorrência com **File Locking** exclusivo (`p4 edit` / `p4 submit`).

---

## 6. Interoperabilidade e Migração entre Sistemas VCS

### 6.1. Ponte Bidirecional com `git-svn`
Permite utilizar a flexibilidade local do Git em bases de código centralizadas em SVN:
```bash
# Clonar repositório SVN com layout padrão (trunk, branches, tags)
git svn clone --stdlayout --authors-file=authors.txt http://svn.empresa.com/repos/app app-git

# Atualizar base local com novos commits do SVN (rebase limpo)
git svn rebase

# Desenvolver commits locais normalmente no Git
git commit -m "feat: implementa nova rota de pagamentos"

# Publicar commits locais de volta para o repositório SVN
git svn dcommit
```

### 6.2. Migração Integral de SVN para Git Nativo
Procedimento canônico para migrar histórico completo sem perda de linhagem, branches ou autores:

#### Passo 1: Extrair e Mapear Autores do SVN para o Git
```bash
# Extrair todos os autores únicos do histórico do SVN
svn log -q http://svn.empresa.com/repos/app | awk -F '|' '/^r/ {sub("^ ", "", $2); sub(" $", "", $2); print $2}' | sort -u > svn-authors.txt

# Mapear para o formato: svnuser = Nome Completo <email@empresa.com>
sed -i 's/^\(.*\)$/\1 = \1 <\1@empresa.com>/' svn-authors.txt
```

#### Passo 2: Clonagem via `git-svn`
```bash
git svn clone --stdlayout --authors-file=svn-authors.txt http://svn.empresa.com/repos/app app-migrado
```

#### Passo 3: Converter Branches e Tags Remotas do SVN para Referências Git Locais
```bash
cd app-migrado

# Converter tags remotas em tags reais anotadas do Git
for tag in $(git branch -r | grep 'tags/'); do
    tag_name=$(echo $tag | sed 's/.*tags\///')
    git tag -a -m "Convertido do SVN tag: $tag_name" "$tag_name" "$tag"
    git branch -r -d "$tag"
done

# Converter branches remotas em branches locais rastreáveis
for branch in $(git branch -r | grep -v 'trunk' | grep -v 'tags/'); do
    branch_name=$(echo $branch | sed 's/.*///')
    git branch "$branch_name" "$branch"
    git branch -r -d "$branch"
done
```

#### Passo 4: Migração de `svn:ignore` para `.gitignore`
```bash
git svn show-ignore > .gitignore
git add .gitignore
git commit -m "chore: migra propriedades svn:ignore para .gitignore"
```

#### Passo 5: Vincular ao Novo Repositório Remoto Git e Publicar
```bash
git remote add origin git@github.com:empresa/app.git
git push --all origin
git push --tags origin
```

---

## 7. Governança, Estratégias de Branching e Segurança

### 7.1. Estratégias de Branching
1. **Trunk-Based Development (Recomendado para CI/CD Moderno)**:
   - Todos os desenvolvedores integram alterações pequenas e frequentes diretamente no `main` (ou em branches de curta duração $< 1$ dia).
   - Utilização de **Feature Flags** para desacoplar deploy de release e manter o branch principal sempre estável e deployável.
2. **GitFlow (Tradicional para Ciclos de Release Agendados)**:
   - Estrutura com branches de longa duração: `main` (produção) e `develop` (integração contínua).
   - Branches auxiliares: `feature/*`, `release/*` e `hotfix/*`.

### 7.2. Assinatura Criptográfica de Commits e Tags (GPG & SSH)
Garante o não-repúdio e impede falsificação de identidade de committers:
```bash
# Configurar assinatura de commits com chave SSH moderna
git config --global user.signingkey "~/.ssh/id_ed25519.pub"
git config --global gpg.format ssh
git config --global commit.gpgsign true
git config --global tag.gpgsign true

# Validar assinatura de commits
git log --show-signature -n 5
```

### 7.3. Proteção de Branches e `CODEOWNERS`
- Configuração de políticas de pull request: aprovações mínimas, exigência de status checks de CI aprovados e proibição de push forçado (`force-push`).
- Mapeamento de revisores obrigatórios por domínio em `.github/CODEOWNERS`:
  ```text
  # Regras de revisão por path
  *                   @org/core-team
  /services/billing/  @org/billing-engineers
  /infra/             @org/devops-architects
  *.sql               @org/dba-specialists
  ```
