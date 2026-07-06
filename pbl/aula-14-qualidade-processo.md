# PBL 9: Qualidade de Processo (Local Eats)

**Integrante:** Lucas Sol Henrique Jacques de Oliveira (RA: 842100049)

## 🎯 Objetivo
Compreender como o software é produzido no projeto LocalEats e mapear o processo de trabalho da equipe, identificando oportunidades de melhoria e analisando o impacto da qualidade do processo na qualidade do produto final.

## 🗺️ Mapeamento do Processo Atual
O fluxo de desenvolvimento e validação de funcionalidades do LocalEats contempla o recebimento da demanda, planejamento, especificação, desenvolvimento local (TDD), testes funcionais (BDD), pipeline de Integração Contínua (CI), revisão e deploy em produção:

```mermaid
graph TD
    A[1. Recebimento da Demanda / Backlog PO] -->|DoR Atendido| B[2. Planejamento da Iteração]
    B --> C[3. Especificação do Requisito & Critérios de Aceitação BDD]
    C --> D[4. Desenvolvimento com TDD]
    
    subgraph TDD [Ciclo TDD]
        D -->|RED| E[Escrever Teste Unitário que Falha]
        E -->|GREEN| F[Implementar Código Mínimo]
        F -->|REFACTOR| G[Refatorar o Código]
        G --> H{Testes Locais Passam?}
        H -->|Não| E
        H -->|Sim| I[Código Implementado]
    end
    
    I --> J[5. Escrita e Execução de Testes BDD E2E Playwright]
    J --> K{Testes E2E Passam?}
    K -->|Não| D
    K -->|Sim| L[6. Criação de Pull Request para branch main]
    
    subgraph CI [Pipeline de CI - GitHub Actions]
        L --> M[Execução Automática de Testes Unitários pytest]
        M --> N{Build & Testes Verdes?}
    end
    
    N -->|Não| O[Feedback de Falha - Ajustar Código]
    O --> D
    N -->|Sim| P[7. Code Review por Par / Auto-Revisão]
    P --> Q[8. Merge na branch main]
    Q --> R[9. Deploy Automático no Vercel (Produção)]
    R --> S[10. DoD Atendido / Entrega Concluída]
    
    style TDD fill:#f9f,stroke:#333,stroke-width:2px
    style CI fill:#bbf,stroke:#333,stroke-width:2px
    style S fill:#bfb,stroke:#333,stroke-width:2px
```

## 📥 Identificação de Entradas, Atividades e Saídas

| Etapa | Entrada | Atividade | Saída |
| :--- | :--- | :--- | :--- |
| **Planejamento & Definição** | Necessidade do negócio ou bug relatado (Backlog bruto) | Reunião de planejamento e escrita da User Story com critérios de aceitação específicos | Issue detalhada e priorizada no GitHub Projects com Definition of Ready (DoR) atendido |
| **Desenvolvimento TDD** | Issue planejada e regras de negócio da funcionalidade | Escrita iterativa de testes unitários seguidos do código mínimo e posterior refatoração (Red-Green-Refactor) | Código-fonte desenvolvido localmente e testes unitários locais passando |
| **Validação Funcional BDD** | Funcionalidade implementada e cenários Gherkin definidos | Criação e execução de scripts automatizados de interface (E2E) com Playwright | Suíte de testes funcionais executada e validada |
| **Integração Contínua (CI)** | Pull Request aberto com a nova funcionalidade | Disparo automático do pipeline do GitHub Actions para executar testes unitários e linting | Pipeline aprovado com status "Success" e feedback imediato |
| **Homologação e Entrega** | Código validado no CI e Pull Request aprovado | Revisão do código (Code Review), merge na branch principal e deploy contínuo | Funcionalidade disponível em produção na plataforma Vercel e Definition of Done (DoD) atendido |

## 💭 Reflexão sobre o Processo

1. **O processo utilizado pela equipe está claramente definido?**  
   Sim, o processo está documentado e estruturado integrando TDD/BDD na máquina local com automação de testes no pipeline remoto de integração contínua (CI) do GitHub Actions.
2. **Todos os integrantes seguem o mesmo fluxo de trabalho?**  
   Sim, pois as restrições e automações do repositório (bloqueio de commits sem passar no pipeline de CI e regras para criação de Pull Requests) forçam a equipe a adotar e respeitar o mesmo fluxo.
3. **Em quais etapas a qualidade é verificada?**  
   A qualidade é verificada em três instâncias: na prevenção (ciclo local TDD/BDD), na integração (execução do pipeline remoto no GitHub Actions) e na homologação (Code Review de Pull Request).
4. **Quais melhorias poderiam tornar o processo mais eficiente?**  
   Integração de ferramentas de análise estática de código (como flake8 e SonarCloud) e definição de limites de WIP no Kanban para acelerar o tempo de entrega.
5. **Como a qualidade do processo impacta a qualidade do produto final?**  
   Um processo de qualidade estruturado previne a entrada de bugs em produção através de testes automatizados sistemáticos, economiza tempo de desenvolvimento e garante deploys mais seguros e previsíveis.

## ✅ Resultados
- Processo de desenvolvimento mapeado graficamente.
- Tabela de entradas, atividades e saídas preenchida com 5 etapas críticas.
- Análise reflexiva indicando a importância da qualidade do processo para a estabilidade do LocalEats.
