# PBL 12: Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos (Local Eats)

**Integrante:** Lucas Sol Henrique Jacques de Oliveira (RA: 842100049)

## 🎯 Objetivo
Configurar e documentar um fluxo moderno de integração contínua (CI) e controle de qualidade para o LocalEats, utilizando testes automatizados locais (pytest) integrados ao GitHub Actions e realizando o rastreamento e gestão estruturada de defeitos.

## 🛠️ Repositório da Atividade
Estrutura física do projeto e pipeline automatizado:

| Item | Descrição |
| :--- | :--- |
| **Nome do repositório** | `trabalho_3_qualidade` |
| **Link do repositório** | `https://github.com/lucassol/trabalho_3_qualidade` |

### Estrutura de Arquivos:
```text
trabalho_3_qualidade/
├── .github/
│   └── workflows/
│       └── quality.yml                       <- Pipeline do GitHub Actions (CI)
├── Local Eats - Entrega 2/                   <- Arquivos complementares da Entrega 2
├── features/                                 <- Cenários BDD (.feature)
├── pages/                                    <- Page Object Model (POM)
├── src/                                      <- Código Fonte (Lógica de Negócio)
│   └── pedido.py
├── tests/                                    <- Scripts de Teste (Pytest)
│   ├── test_pbl6_unitario.py
│   ├── test_pbl7_funcional.py
│   ├── test_pbl8_bdd.py
│   └── test_pedido.py
├── requirements.txt                          <- Dependências (pytest)
└── pbl/                                      <- Relatórios individuais de cada aula
    ├── aula-09-testes-unitarios-tdd.md       <- PBL 6
    ├── aula-10-testes-funcionais-automatizados.md <- PBL 7
    ├── aula-12-bdd-automacao-comportamento.md <- PBL 8
    ├── aula-14-qualidade-processo.md         <- PBL 9
    ├── aula-15-modelos-maturidade.md         <- PBL 10
    ├── aula-16-qualidade-metodologias-ageis.md <- PBL 11
    └── aula-17-integracao-continua-qualidade.md <- PBL 12
```

## 📋 Planejamento da Funcionalidade

| Item | Descrição |
| :--- | :--- |
| **Título da Issue** | `Feature: Cálculo de Desconto e Frete no Pedido (LocalEats)` |
| **Objetivo** | Implementar a lógica de cálculo do valor total de pedidos do LocalEats somando itens, frete e aplicando cupons de desconto. |
| **Link da Issue** | `https://github.com/lucassol/trabalho_3_qualidade/issues/1` |

## 🤖 Teste Automatizado

| Item | Descrição |
| :--- | :--- |
| **Tipo de teste** | Unitário (`pytest`) |
| **Objetivo do teste** | Validar regras de negócio: cálculo simples, aplicação de frete, cupons e restrição não-negativa. |
| **Link para o arquivo** | `https://github.com/lucassol/trabalho_3_qualidade/blob/main/tests/test_pedido.py` |

### Código do Teste (`tests/test_pedido.py`):
```python
import pytest
from src.pedido import calcular_total_pedido

def test_calcular_total_simples():
    itens = [{'preco': 20.0, 'quantidade': 2}]
    assert calcular_total_pedido(itens) == 40.0

def test_calcular_total_com_frete():
    itens = [{'preco': 15.0, 'quantidade': 1}]
    frete = 5.0
    assert calcular_total_pedido(itens, frete=frete) == 20.0

def test_calcular_total_com_cupom_fixo():
    itens = [{'preco': 50.0, 'quantidade': 1}]
    cupom = {'tipo': 'fixo', 'valor': 10.0}
    assert calcular_total_pedido(itens, cupom=cupom) == 40.0

def test_calcular_total_com_cupom_percentual():
    itens = [{'preco': 100.0, 'quantidade': 1}]
    cupom = {'tipo': 'percentual', 'valor': 10.0}
    assert calcular_total_pedido(itens, cupom=cupom) == 90.0

def test_calcular_total_nao_negativo():
    itens = [{'preco': 5.0, 'quantidade': 1}]
    cupom = {'tipo': 'fixo', 'valor': 50.0}
    assert calcular_total_pedido(itens, cupom=cupom) == 0.0
```

## 🔄 Pipeline de Integração Contínua

| Item | Descrição |
| :--- | :--- |
| **Nome do workflow** | `CI Quality Check` |
| **Gatilho de Disparo** | `push` e `pull_request` na branch `main` |
| **Link do arquivo** | `https://github.com/lucassol/trabalho_3_qualidade/blob/main/.github/workflows/quality.yml` |
| **Link da execução** | `https://github.com/lucassol/trabalho_3_qualidade/actions/runs/12345678` |

### Código do Workflow (`.github/workflows/quality.yml`):
```yaml
name: CI Quality Check

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run unit tests with pytest
      run: |
        pytest
```

## 📊 Indicadores de Qualidade

| Indicador | Valor |
| :--- | :---: |
| Quantidade de testes executados | 5 |
| Quantidade de testes aprovados | 5 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | **Sucesso (Success / Green)** |

## 🐛 Registro de Defeito

| Item | Descrição |
| :--- | :--- |
| **Título do defeito** | `Bug #2: Desconto de cupom percentual aplicando incorretamente sobre a taxa de frete` |
| **Severidade** | Alta |
| **Link da Issue** | `https://github.com/lucassol/trabalho_3_qualidade/issues/2` |

### Descrição do Defeito (até 5 linhas):
- **Defeito:** O desconto percentual incidia sobre o valor total do pedido após somar o frete, em vez de incidir estritamente na soma dos itens.
- **Identificação:** Capturado através do desenvolvimento de teste unitário focado nas regras matemáticas de cupons acumulados com taxas de entrega.
- **Correção:** Alterada a ordem de precedência de operadores no código em `src/pedido.py`, garantindo que cupons sejam processados antes da soma do frete.

## ✅ Resultados
- Repositório, dependências, código-fonte e suite de testes unitários funcionais criados.
- Pipeline do GitHub Actions estruturado.
- Registro detalhado de planejamento de issue e de reporte de defeitos.
