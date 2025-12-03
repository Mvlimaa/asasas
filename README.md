📘 Projeto de Machine Learning – Previsão de Tempo de Entrega
👥 Integrantes do Projeto

João Levi Bezerra da Silva - 01735303

Marcelo Vynicius de Lima Silva - 01700876

Fernando Antônio da Silva Neto - 01703313

📂 Dataset Utilizado

Nome do Dataset: (coloque aqui)
Descrição rápida: Dataset contendo informações de entregas (distâncias, clima, peso, categoria, etc.) para prever o tempo total de entrega.

📊 Etapa 1 — Análise Exploratória (EDA)

Objetivo: entender o dataset, problemas, padrões e estrutura antes de preparar os dados.

✔️ O que foi feito

Carregamento e inspeção do dataset (linhas, colunas, tipos, estatísticas).

Identificação de valores faltantes e suas proporções.

Análise das variáveis numéricas (histogramas, boxplots, outliers).

Análise das categóricas (frequências, inconsistências).

Heatmap de correlação para entender relações entre variáveis.

Criação apenas dos gráficos essenciais solicitados pelo professor.

📁 Entregável

notebooks/01_Analise_Exploratoria.ipynb

🧹 Etapa 2 — Pré-Processamento dos Dados

Objetivo: limpar, padronizar e transformar os dados para deixá-los prontos para modelagem.

✔️ O que foi feito

Valores faltantes:

Numéricos → mediana

Categóricos → categoria mais frequente

Outliers:

Redução via IQR (capping)

Correção de valores incorretos quando necessário

Encoding:

One-Hot Encoding para variáveis categóricas

drop_first=True para evitar multicolinearidade

Normalização:

StandardScaler aplicado nas colunas numéricas

Scaler salvo em models/scaler.pkl

Feature Engineering:

Criação de features simples (ex.: relações derivadas entre variáveis)

📁 Entregáveis

notebooks/02_Preprocessamento.ipynb

data/delivery_clean.csv

models/scaler.pkl

🤖 Etapa 3 — Modelo Baseline (Regressão Linear)

Objetivo: criar um primeiro modelo simples e interpretável para servir de referência.

✔️ O que foi feito
1. Carregamento dos dados

Uso do delivery_clean.csv processado na etapa anterior

Garantia de dataset sem NaN

2. Preparação do modelo

Target: delivery_time_hours

Features: todas as demais colunas úteis

One-Hot Encoding aplicado nas categóricas

Remoção de IDs e colunas irrelevantes

Remoção de linhas com NaN após encoding

3. Divisão do dataset

60% treino

20% validação

20% teste (guardado para uso futuro)

4. Treinamento

Modelo escolhido: Regressão Linear (sklearn)
Simples, rápido e interpretável → ideal para baseline

5. Métricas calculadas

MSE

RMSE

MAE

R² (principal métrica)

📌 Nos resultados deste projeto:

R² treino ≈ 0.887

R² validação ≈ 0.830

Diferença ≈ 0.056 → sem overfitting

6. Análise dos coeficientes

Ranking das 5 variáveis mais impactantes

Coeficientes positivos aumentam o tempo de entrega

Coeficientes negativos diminuem

7. Visualizações

Predito vs Real

Distribuição dos resíduos
Ambos salvos na pasta models/

8. Salvamento do modelo

models/baseline_model.pkl

📁 Entregáveis

notebooks/03_Modelo_Baseline.ipynb

models/baseline_model.pkl

models/predicoes_vs_real.png

models/residuos.png