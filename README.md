# CI/CD Quality Gates - AI vs Manual

> **Qualidade de Software | Prof. Nuno Pombo | 2025/26**  
> Stack: GitHub + GitHub Actions + SonarCloud + Python

---

## 📌 O que é este projeto

Este projeto compara dois tipos de **quality gates** num pipeline CI/CD:

- **Gate Manual** - um humano revê e aprova ou rejeita o código
- **Gate AI (SonarCloud)** - uma ferramenta analisa automaticamente e decide pass/fail
  O objetivo é recolher dados reais de Pull Requests e responder a duas questões:
- **RQ1:** Como é que os quality gates com AI afetam os resultados do pipeline?
- **RQ2:** Com que frequência é que alguém ignorou a decisão da AI (override)?

---

## 📁 Estrutura do Projeto

```
cicd-quality-gates/
  src/
    __init__.py              <- ficheiro vazio (obrigatório)
    calculator.py            <- código Python de exemplo
  tests/
    __init__.py              <- ficheiro vazio (obrigatório)
    test_calculator.py       <- testes unitários
  scripts/
    save_metrics.py          <- script que guarda dados automaticamente
  data/
    metrics.json             <- registo de todos os PRs e resultados
  .github/
    workflows/
      ci-with-sonar.yml      <- pipeline com AI gate (SonarCloud)
      ci-manual-only.yml     <- pipeline com gate manual
  sonar-project.properties   <- configuração do SonarCloud
  requirements.txt           <- dependências Python
  conftest.py                <- configuração do pytest
  README.md                  <- este ficheiro
```

---

## ⚙️ Como configurar o projeto (primeira vez)

### 1. Clonar o repositório

```bash
git clone https://github.com/RivaldoPinto26/cicd-quality-gates.git
cd cicd-quality-gates
```

### 2. Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 3. Correr os testes localmente

```bash
pytest --cov=src --cov-report=term
```

---

## 🔑 Configurar o SonarCloud (só o dono do repo faz isto)

1. Ir a [sonarcloud.io](https://sonarcloud.io) e fazer login com GitHub
2. Criar organização com o username do GitHub
3. Adicionar o repositório e desativar **Automatic Analysis**
4. Ir a **My Account -> Security -> Generate Token**
5. Copiar o token
6. No GitHub ir a **Settings -> Secrets and variables -> Actions**
7. Criar secret com nome `SONAR_TOKEN` e colar o token
8. Em **Settings -> Actions -> General -> Workflow permissions** selecionar **Read and write permissions**

---
