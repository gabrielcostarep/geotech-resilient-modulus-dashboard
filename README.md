# 🔬 <a href="https://geotech-resilient-modulus-dashboard-xxhrjjseavblttwrruhyzf.streamlit.app" target="_blank">Dashboard Geotécnico: Módulo Resiliente (MR)</a>

Interactive dashboard for analysis and comparison of Resilient Modulus tests in steel slag mixtures with rubber addition.

🚧 **Status do Projeto:** Em desenvolvimento (Work In Progress) 🚧

## 📖 Sobre o Projeto

Este repositório contém uma aplicação web interativa dedicada à análise de ensaios de **Módulo Resiliente (MR)**. Diferente do dashboard de fadiga (contínuo), esta ferramenta é projetada para processar ensaios realizados em degraus de carga (procedimentos), permitindo a avaliação da rigidez e do acúmulo de dano do material sob diferentes estados de tensão.

O estudo foca na comparação entre a Escória de Aciaria (ASIC) pura e composições com 2,5% e 5% de borracha, visando aplicações em pavimentação e infraestrutura rodoviária.

## ✨ Principais Funcionalidades

* **Comparação Multimaterial:** Visualização sobreposta das três misturas em tempo real para análise de desempenho comparativo.
* **Análise de Energia Dissipada ($e_{diss}$):** Monitoramento da energia perdida por ciclo em cada procedimento de carga.
* **Cálculo de CASE (Cumulative Absolute Strain Energy):** Métrica acumulada para avaliar o potencial de degradação e fadiga precoce sob tensões específicas.
* **Conversão Percentual de Deformação:** Expressão automática da deformação axial em percentual (%) para melhor legibilidade técnica, conforme padrões de engenharia.
* **Inspeção de Histerese por Procedimento:** Gráficos interativos de Tensão ($q$) vs. Deformação ($\epsilon_a$) para isolar ciclos específicos (ex: Ciclo 50) de cada degrau de carga.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Web:** Streamlit
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização Interativa:** Plotly
* **Armazenamento:** Apache Parquet (Otimizado para performance em nuvem)
