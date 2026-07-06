

| Centro Universitário Senac-RS ADS \- Análise e Desenvolvimento de Sistemas / SPI \- Sistemas para Internet Unidade Curricular: Qualidade de Software  Prof.: Luciano Zanuz  |
| :---- |

# **🧩 Atividade PBL – Aula 17**

**Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos – LocalEats**

### **📌 Contexto**

Nas aulas anteriores, a equipe estudou testes automatizados, TDD, BDD e práticas de qualidade em metodologias ágeis.

Agora o objetivo é aplicar esses conceitos em um fluxo moderno de desenvolvimento, utilizando GitHub Issues, GitHub Actions e Integração Contínua para automatizar verificações de qualidade e acompanhar defeitos do projeto.

👉 Link para o sistema LocalEats: [https://local-eats-unisenac.vercel.app/](https://local-eats-unisenac.vercel.app/)

## **🎯 Objetivo da Atividade**

Aplicar os conceitos de:

* GitHub Issues  
* GitHub Projects  
* Testes automatizados  
* Integração Contínua (CI)  
* GitHub Actions  
* Métricas de qualidade  
* Gestão de defeitos

👉 O foco da atividade é demonstrar a utilização de um fluxo de qualidade automatizado.

## **📝 Tarefas**

### **🔹 1\. Repositório da Atividade**

Criem um repositório específico para esta atividade.

Preencham a tabela:

| Item | Descrição |
| :---- | :---- |
| Nome do repositório |  |
| Link do repositório |  |

Apresentem a estrutura de diretórios utilizada:  
\<colar estrutura de arquivos e pastas\>

Exemplo:  
localeats-ci-laboratorio/  
├── tests/  
│   ├── test\_order.py  
│   ├── test\_order\_bdd.py  
│   └── features/  
│       └── order\_total.feature  
├── .github/  
│   └── workflows/  
│       └── quality.yml  
├── order.py  
└── requirements.txt

### **🔹 2\. Planejamento da Funcionalidade**

Criem uma Issue para uma funcionalidade simples.

Preencham a tabela:

| Item | Descrição |
| :---- | :---- |
| Título da Issue |  |
| Objetivo da funcionalidade |  |
| Link da Issue |  |

### **🔹 3\. Teste Automatizado**

Criem pelo menos 1 teste automatizado relacionado à funcionalidade escolhida.

Preencham a tabela:

| Item | Descrição |
| :---- | :---- |
| Tipo de teste | Unitário ou BDD |
| Objetivo do teste |  |
| Link para o arquivo do teste |  |

Colem o código do teste criado:

\# código do teste

### **🔹 4\. Pipeline de Integração Contínua**

Configurem um workflow do GitHub Actions para executar automaticamente os testes.

Preencham a tabela:

| Item | Descrição |
| :---- | :---- |
| Nome do workflow |  |
| Evento que dispara a execução |  |
| Link para o arquivo do workflow |  |
| Link de uma execução do workflow |  |

Colem o código do workflow:

\# workflow GitHub Actions

### **🔹 5\. Indicadores de Qualidade**

Após executar o pipeline, registrem os seguintes indicadores:

| Indicador | Valor |
| :---- | :---- |
| Quantidade de testes executados |  |
| Quantidade de testes aprovados |  |
| Quantidade de testes com falha |  |
| Status final do pipeline |  |

### **🔹 6\. Registro de Defeito**

Criem uma Issue de defeito (bug) relacionada à funcionalidade ou simulem um defeito simples.

Preencham a tabela:

| Item | Descrição |
| :---- | :---- |
| Título do defeito |  |
| Severidade | Baixa, Média, Alta ou Crítica |
| Link da Issue |  |

Descrevam brevemente:

* Qual foi o defeito?  
* Como ele foi identificado?  
* Como foi corrigido?

(Máximo 5 linhas)

## **📦 Entrega**

**Formato:** arquivo Markdown (.md)

**Entrega:** repositório do grupo no GitHub

/aula-17-integracao-continua-qualidade.md

👉 Trabalho individual ou em grupo (até 4 integrantes)

## **📎 Exemplo de Estrutura**

[https://github.com/lucianozanuz/pbl-qualidade-software-2026-1/blob/main/pbl/aula-17-integracao-continua-qualidade.md](https://github.com/lucianozanuz/pbl-qualidade-software-2026-1/blob/main/pbl/aula-17-integracao-continua-qualidade.md)

* Repositório da Atividade  
* Planejamento da Funcionalidade  
* Teste Automatizado  
* Pipeline de Integração Contínua  
* Indicadores de Qualidade  
* Registro de Defeito

## **📊 Avaliação (Rubrica – Unisenac-RS)**

### **🔴 D — Não atingiu**

* Atividade incompleta.  
* Não apresentou evidências da utilização do GitHub.  
* Pipeline inexistente ou não funcional.

### **🟡 C — Parcial**

* Issue criada, mas com poucas informações.  
* Teste ou pipeline implementado parcialmente.  
* Indicadores preenchidos de forma incompleta.

### **🔵 B — Pleno**

* Fluxo de qualidade implementado corretamente.  
* Teste automatizado funcional.  
* Pipeline executando corretamente.  
* Registro adequado do defeito.

### **🟢 A — Excelência**

* Excelente organização das evidências.  
* Boa utilização de Issues e GitHub Actions.  
* Indicadores corretamente analisados.  
* Registro de defeito consistente e bem classificado.  
* Demonstração clara da aplicação dos conceitos estudados em aula.

## **💡 Dica final**

Para obter conceito A, demonstrem que a funcionalidade foi desenvolvida seguindo um fluxo de qualidade, utilizando testes automatizados, pipeline de Integração Contínua e registro adequado de defeitos.

👉 Mentalidade esperada:

**"Como podemos garantir automaticamente que uma alteração no sistema não introduza novos problemas?"**

