# PBL 10: Modelos de Maturidade (Local Eats)

**Integrante:** Lucas Sol Henrique Jacques de Oliveira (RA: 842100049)

## 🎯 Objetivo
Avaliar o nível de maturidade do processo de desenvolvimento da equipe no projeto LocalEats, identificando lacunas e propondo melhorias com base em modelos de referência (CMMI-DEV e MPS.BR).

## 📊 Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
| :--- | :---: | :---: | :---: |
| Os requisitos são documentados? | **X** | | |
| Existe controle de mudanças? | **X** | | |
| Há atividades de teste definidas? | **X** | | |
| Os defeitos são registrados? | **X** | | |
| O processo de desenvolvimento é conhecido por toda a equipe? | **X** | | |
| As tarefas são planejadas e acompanhadas regularmente? | **X** | | |
| Existe padronização para implementação de funcionalidades? | **X** | | |
| Os testes são executados antes da entrega das funcionalidades? | **X** | | |
| Há revisão de código ou validação por outro integrante da equipe? | | **X** | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | **X** | | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | **X** | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | **X** | | |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | **X** | |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | **X** | |

**Nível de Maturidade Identificado:** Nível 2 (Gerenciado) / Nível G (MPS.BR)

**Justificativa:**
O processo de desenvolvimento do LocalEats se enquadra no **Nível 2 (Gerenciado)** do CMMI. A equipe executa com sucesso o gerenciamento de requisitos, gerência de configuração (Git), garantia da qualidade do processo (testes locais e na nuvem) e monitoramento do progresso das tarefas (GitHub Projects). O processo não atinge o Nível 3 (Definido) porque a medição de métricas de qualidade é parcial e as cerimônias de retrospectiva e de revisão formal de código por pares ocorrem de forma assíncrona ou informal, sem padronização organizacional rígida.

## ⚠️ Lacunas Identificadas

| Lacuna | Impacto no Processo / Produto |
| :--- | :--- |
| **Ausência de Linters/SAST Automático** | Facilita a injeção de trechos de código fora do padrão e brechas básicas de segurança que escapam da validação manual do desenvolvedor. |
| **Escassez de Métricas Formais de Teste** | Sem indicadores formais de densidade de bugs e cobertura de testes (Code Coverage), o controle quantitativo e as melhorias dependem da intuição da equipe. |
| **Retrospectivas Assíncronas** | O aprendizado sobre defeitos operacionais ocorridos durante o ciclo produtivo não é estruturado, aumentando o risco de repetição de erros. |

## 🚀 Propostas de Melhoria

| Melhoria Proposta | Benefício Esperado | Ação Prática |
| :--- | :--- | :--- |
| **Integração de flake8 e bandit no CI** | Padronização automática de estilo PEP8 e detecção precoce de brechas de segurança estática a cada commit. | Incluir etapas de linting e segurança no arquivo `.github/workflows/quality.yml`. |
| **Implantação de Relatório de Cobertura** | Visualização da qualidade do código através de métricas formais de cobertura a cada Pull Request. | Conectar o repositório ao Codecov ou gerar artefatos XML de cobertura de teste no pytest. |
| **Cerimônia Formal de Retrospectiva** | Criação de um espaço contínuo para ajustar o fluxo operacional e aplicar melhorias preventivas no processo. | Agendar e realizar uma reunião quinzenal de retrospectiva, documentando lições aprendidas no repositório. |

## ✅ Resultados
- Diagnóstico de 14 itens preenchido com classificação no Nível 2 de maturidade.
- Identificação de 3 lacunas críticas de processo.
- Proposição de 3 ações específicas de engenharia de qualidade.
