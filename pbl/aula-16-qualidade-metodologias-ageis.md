# PBL 11: Qualidade em Metodologias Ágeis (Local Eats)

**Integrante:** Lucas Sol Henrique Jacques de Oliveira (RA: 842100049)

## 🎯 Objetivo
Analisar o processo de desenvolvimento do projeto LocalEats sob a perspectiva ágil, identificando a aderência a práticas ágeis (Scrum/XP/Kanban) e estruturando critérios formais de Definition of Ready (DoR) e Definition of Done (DoD).

## 🏃 Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
| :--- | :---: | :--- | :--- |
| **Planejamento iterativo** | **Sim** | O desenvolvimento é focado em pequenos ciclos rápidos focando em entregas funcionais. | Sim, definindo iterações fixas (sprints) de 2 semanas. |
| **Priorização de funcionalidades** | **Sim** | O PO define a ordem de desenvolvimento no backlog das issues com base em valor de negócio. | Sim, utilizando frameworks de priorização formal, como MoSCoW. |
| **Entregas incrementais** | **Sim** | Cada nova regra de cálculo ou validação é integrada e disponibilizada de forma incremental na web. | Sim, utilizando Feature Flags para desacoplar a entrega técnica da liberação ao usuário. |
| **Feedback frequente** | **Sim** | Stakeholders revisam a aplicação diretamente nas entregas executadas no Vercel. | Sim, organizando sessões formais de Review/Demonstração ao fim de cada ciclo. |
| **Trabalho colaborativo** | **Sim** | A equipe compartilha repositório, realiza discussões nas issues e realiza alinhamento contínuo. | Sim, adotando práticas formais de Pair Programming para tarefas críticas. |
| **Controle visual das atividades** | **Sim** | Uso das colunas (A Fazer, Em Progresso, Concluído) no GitHub Projects. | Sim, definindo limites de WIP (Work in Progress) no quadro. |
| **Melhoria contínua** | **Sim** | Ajustes pontuais de fluxo ocorrem quando bugs ou gargalos operacionais são identificados. | Sim, padronizando cerimônias de retrospectiva quinzenais. |

**Conclusão (até 10 linhas):**
O processo do LocalEats está estruturado em princípios fundamentais do manifesto ágil, com bom controle visual de tarefas e foco em incremento de produto. Há uma excelente harmonia entre os requisitos (issues) e as suítes de testes que garantem a qualidade técnica antes do deploy. Para evoluir, a equipe deve focar em formalizar rituais de melhoria contínua e limitar o WIP para evitar gargalos em fases de testes e revisão, aumentando a vazão operacional e blindando o ciclo contra retrabalhos.

## 🚀 Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
| :--- | :--- | :--- |
| **Limites de WIP no Kanban** | Kanban (Lean) | Minimiza a multitarefa e o acúmulo de issues na fase de testes, reduzindo o Lead Time. |
| **Pair Programming em regras complexas** | XP (Extreme Programming) | Evita a inserção de erros na origem e acelera a troca de contexto e capacitação do time. |
| **Reuniões diárias (Daily Standups)** | Scrum | Melhora o alinhamento diário das atividades e a rápida identificação de impedimentos técnicos. |
| **Adoção Formal de DoR e DoD** | Scrum / Engenharia Ágil | Garante alinhamento nos requisitos de entrada e um selo padrão de qualidade técnica na saída. |

## 📝 Definition of Ready (DoR)
A história de usuário/funcionalidade deve atender a pelo menos **5 critérios** para iniciar o desenvolvimento:
1. Requisito escrito em formato de história de usuário (`Como... Quero... Para...`).
2. Critérios de aceitação detalhados no formato Gherkin (`Dado que... Quando... Então...`).
3. Protótipo ou tela definida anexada à Issue (se possuir interface).
4. Dependências de código ou de terceiros resolvidas.
5. Estimativa de esforço/complexidade validada pela equipe.

## 🏁 Definition of Done (DoD)
A funcionalidade deve atender a pelo menos **5 critérios** para ser considerada concluída:
1. Código desenvolvido e em conformidade com as regras e critérios de aceitação.
2. Testes unitários implementados e passando com cobertura superior a 80%.
3. Testes funcionais e de aceitação automatizados (Playwright) executados com sucesso.
4. Pull Request revisado e aprovado formalmente por outro integrante da equipe.
5. Código integrado com sucesso (Pipeline de CI do GitHub Actions verde) e deploy produtivo realizado no Vercel.

## ✅ Resultados
- Análise de 7 práticas ágeis com conclusão analítica.
- 4 propostas de melhoria ágil baseadas no Scrum, Kanban e XP.
- DoR e DoD compostos por 5 critérios objetivos cada.
