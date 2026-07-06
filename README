# Aula 14, 15, 16 e 17 – Qualidade de Processo, Modelos de Maturidade, Metodologias Ágeis e Integração Contínua (Entrega 3)

> **Disciplina:** Qualidade de Software  
> **Projeto:** LocalEats  
> **Integrante:**  
> - Lucas Sol Henrique Jacques de Oliveira (RA: 842100049)

---

# 1. Plano de Testes e Garantia de Qualidade de Processo (Entrega 3)

## 1.1 Objetivo
Garantir a qualidade do produto e do processo de desenvolvimento do sistema LocalEats por meio de mapeamento de processos, diagnóstico de maturidade (CMMI/MPS.BR), integração de práticas ágeis (DoR/DoD) e execução automatizada de testes locais integrados ao pipeline de Integração Contínua (CI).

---

## 1.2 Escopo

### O que será avaliado/testado
- Mapeamento e fluxo de atividades de desenvolvimento da equipe.
- Nível de maturidade do processo de desenvolvimento.
- Práticas ágeis de gestão e critérios de prontidão/conclusão (DoR/DoD).
- Lógica de cálculo de pedidos (Business Rules) com testes unitários em pytest.
- Pipeline automatizado de testes de integração contínua (CI) via GitHub Actions.
- Gestão de defeitos e bugs lógicos de negócio.

### O que NÃO será testado
- Testes manuais exaustivos de ponta a ponta na interface.
- Performance de carregamento e testes de segurança estáticos avançados (SAST).

---

## 1.3 Funcionalidades e Processos Selecionados
- [Processo] Mapeamento de fluxo completo em Mermaid.
- [Maturidade] Diagnóstico de 14 critérios baseados no CMMI/MPS.BR.
- [Ágil] Definição de critérios formais de DoR e DoD.
- [Automação] Pipeline de Integração Contínua (CI) com GitHub Actions.
- [Unitário] Cálculo de total, frete e cupons em Python.

---

## 1.4 Estratégia de Testes e Validação
- **Tipos de teste e validações:**
  - (X) Qualidade de Processo (Mapeamento e Tabela de Entradas/Atividades/Saídas)
  - (X) Modelos de Maturidade (Diagnóstico e Propostas de Melhoria)
  - (X) Metodologias Ágeis (Análise de práticas, DoR e DoD)
  - (X) Integração Contínua (GitHub Actions com execução de pytest)
  - (X) Unitário (TDD com Pytest para lógica de pedidos)

- **Abordagem:**
  Automação completa do pipeline de CI disparado por pushes e pull requests na branch `main`, executando testes unitários desenvolvidos em Python 3.10+ com pytest. Mapeamento de processos utilizando modelagem gráfica em Mermaid.

---

## 1.5 Responsáveis

| Nome | Responsabilidade |
|------|----------------|
| Lucas Sol | Mapeamento de processos, diagnóstico de maturidade, definição de DoR/DoD, implementação lógica, testes e pipeline. |

---

# 2. Casos de Teste Automatizados e Registros

## CT-01 – Cálculo de Total Simples (Unitário)
**Pré-condição:** Itens no carrinho com preço e quantidade definidos.  
**Resultado esperado:** A soma deve ser exata (preço * quantidade).

## CT-02 – Aplicação de Cupom Fixo (Unitário)
**Pré-condição:** Cupom de valor fixo ativo (R$ 10).  
**Resultado esperado:** O valor total do pedido deve ser reduzido exatamente em R$ 10.

## CT-03 – Aplicação de Cupom Percentual (Unitário)
**Pré-condição:** Cupom de 10% ativo.  
**Resultado esperado:** O valor total da compra dos itens deve sofrer redução proporcional de 10% antes da adição do frete.

## CT-04 – Aplicação de Frete (Unitário)
**Pré-condição:** Frete ativo com valor definido (R$ 5).  
**Resultado esperado:** O valor final do frete deve ser acrescido ao total do pedido.

## CT-05 – Valor Não Negativo (Unitário)
**Pré-condição:** Cupom de valor fixo (R$ 50) superior ao total do pedido (R$ 5).  
**Resultado esperado:** O sistema deve retornar 0 e nunca um valor negativo.

---

# 3. Execução dos Testes e Pipeline

| ID     | Resultado (Passou/Falhou) | Evidência |
|--------|--------------------------|--------------------------------|
| CT-01  | Passou                   | Execução local via Pytest OK |
| CT-02  | Passou                   | Execução local via Pytest OK |
| CT-03  | Passou                   | Execução local via Pytest OK |
| CT-04  | Passou                   | Execução local via Pytest OK |
| CT-05  | Passou                   | Lógica de max(0, total) OK |

---

# 4. Análise dos Resultados

- **Quantidade de testes executados:** 5
- **Quantidade de testes que passaram:** 5
- **Quantidade de testes que falharam:** 0
- **Status do Pipeline de CI:** Sucesso (Green build no GitHub Actions)

---

# 5. Reflexão

- **O plano de testes e processos ajudou a organizar melhor o processo?** Sim, o mapeamento detalhado do processo de desenvolvimento em conjunto com critérios formais de DoR/DoD estruturou as fases de implementação, garantindo previsibilidade e diminuindo a injeção de bugs.
- **O que o grupo melhoraria no processo de testes e qualidade?** Adicionar análise estática de código (como flake8) e acompanhamento de cobertura (Codecov) integrados diretamente ao pipeline de CI no GitHub Actions.

---

# 6. Conclusão Geral

A implementação das práticas de qualidade da Entrega 3 estabelece um patamar de maturidade Gerenciado (Nível 2 CMMI / Nível G MPS.BR) para o LocalEats. A automação das verificações através da Integração Contínua (CI) e a definição dos critérios de pronto (DoR) e concluído (DoD) blindam o repositório principal contra código defeituoso ou instável.

---

## 📂 Estrutura de Arquivos da Entrega
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
├── pbl/                                      <- Relatórios individuais de cada aula
│   ├── aula-09-testes-unitarios-tdd.md       <- PBL 6
│   ├── aula-10-testes-funcionais-automatizados.md <- PBL 7
│   ├── aula-12-bdd-automacao-comportamento.md <- PBL 8
│   ├── aula-14-qualidade-processo.md         <- PBL 9
│   ├── aula-15-modelos-maturidade.md         <- PBL 10
│   ├── aula-16-qualidade-metodologias-ageis.md <- PBL 11
│   └── aula-17-integracao-continua-qualidade.md <- PBL 12
└── READ.MD                                   <- README Principal
```