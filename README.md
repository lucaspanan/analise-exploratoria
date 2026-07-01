# Análise Exploratória de Dados

Este projeto realiza uma **Análise Exploratória de Dados (EDA)** em uma base de clientes de marketing, com o objetivo de entender o perfil dos consumidores e identificar padrões de comportamento relacionados à renda, gastos e características demográficas.


# Objetivo

O objetivo principal deste projeto é explorar a base de dados e responder perguntas como:

- Qual o perfil dos clientes?
- Existe relação entre renda e gastos?
- Como o número de filhos varia entre estados civis?
- Como os dados estão distribuídos (média, mediana, desvio padrão)?

---

# Tecnologias utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn



# Etapas da análise

Durante este projeto, foram realizadas as seguintes etapas:

# 1 Importação e inspeção dos dados
- Verificação de tipos de dados
- Identificação de valores nulos
- Detecção de duplicados

# 2 Tratamento dos dados
- Remoção de colunas desnecessárias
- Criação de variáveis booleanas para valores ausentes

# 3 Análise estatística
- Média, mediana e desvio padrão
- Coeficiente de variação
- Assimetria (Skewness)

# 4 Visualização de dados
- Histogramas
- Boxplots
- Countplots
- Scatter plots

# Principais insights

A análise revelou alguns padrões importantes:

- A renda dos clientes apresenta **assimetria positiva**, com concentração em valores mais baixos e alguns valores muito altos.
- Existe uma **relação positiva entre renda e gastos**, indicando que clientes com maior renda tendem a gastar mais.
- O número de filhos varia de acordo com o estado civil.
- Existem possíveis **outliers na variável de renda**.

---

# Exemplos de visualizações

# Renda vs Gastos
(images/renda_vs_gastos.png)


# Como executar o projeto

Clone o repositório:

# bash
git clone https://github.com/seu-usuario/analise-exploratoria-marketing.git