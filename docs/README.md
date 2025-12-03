📘 Projeto de Machine Learning – Previsão de Tempo de Entrega
👥 Integrantes do Projeto

João Levi Bezerra da Silva - 01735303
Marcelo Vynicius de Lima Silva - 01700876
Fernando Antônio da Silva Neto - 01703313

📂 Dataset Utilizado

Nome: delivery_time.csv
Descrição: Contém dados de entregas (distância, clima, veículo, peso, condições de tráfego etc.) utilizados para prever o tempo total de entrega em horas.

📊 Etapa 1 — Análise Exploratória (EDA)

Objetivo: entender o dataset, problemas, padrões e estrutura inicial.

✔️ O que foi feito

Inspeção inicial (linhas, colunas, tipos, estatísticas).

Identificação de valores faltantes.

Histogramas e boxplots para variáveis numéricas.

Frequências e inconsistências para variáveis categóricas.

Heatmap de correlação.

Gráficos essenciais solicitados pelo professor.

📁 Entregável: notebooks/01_Analise_Exploratoria.ipynb

-------------------------------------------------------------

🧹 Etapa 2 — Pré-Processamento dos Dados

Objetivo: limpar e preparar os dados para modelagem.

✔️ O que foi feito

Valores faltantes:

Numéricos → mediana

Categóricos → moda

Outliers:

Tratamento via IQR (capping)

Correção de valores incoerentes

Encoding:

One-Hot Encoding (drop_first=True)

Normalização:

StandardScaler aplicado às colunas numéricas

Scaler salvo em models/scaler.pkl

Feature Engineering:

Criação de features simples derivadas

📁 Entregáveis:

notebooks/02_Preprocessamento.ipynb

data/delivery_clean.csv

models/scaler.pkl

-------------------------------------------------------------

🤖 Etapa 3 — Modelo Baseline (Regressão Linear)

Objetivo: criar o primeiro modelo para servir de referência.

✔️ O que foi feito

Uso do dataset delivery_clean.csv sem NaN

Target: delivery_time_hours

Remoção de IDs e colunas irrelevantes

One-Hot Encoding nas categóricas

Remoção de NaN restantes após encoding

Divisão dos dados:

60% treino

20% validação

20% teste (guardado)

Treinamento:

Modelo: Regressão Linear

Principais métricas:

R² treino: 0.887

R² validação: 0.830

Diferença: 0.056 → sem overfitting

Visualizações:

Predito vs Real

Distribuição dos resíduos

Salvamento:

models/baseline_model.pkl

📁 Entregáveis:

notebooks/03_Modelo_Baseline.ipynb

models/baseline_model.pkl

models/predicoes_vs_real.png

models/residuos.png

-------------------------------------------------------------

⚙️ Etapa 4 — Otimização e Tuning de Hiperparâmetros

Objetivo: melhorar o desempenho do modelo usando técnicas de otimização e validação avançada.

✔️ O que foi feito

Modelo escolhido para otimização:
👉 Random Forest Regressor (mais robusto e adequado que a Regressão Linear)

Técnica de tuning:
👉 RandomizedSearchCV
(mais rápido, eficiente e ideal para muitos hiperparâmetros)

Hiperparâmetros otimizados:

Número de árvores (n_estimators)

Profundidade máxima (max_depth)

min_samples_split

min_samples_leaf

bootstrap

Validação:

Cross-Validation (5 folds)

Treinamento final:

Modelo final treinado usando treino + validação

Apenas depois foi testado no conjunto de teste real

Avaliação final no conjunto de teste:

MAE, RMSE e R² calculados

Resultados mostraram desempenho superior ao modelo baseline

Visualizações:

Gráfico Predito vs Real

Distribuição dos resíduos

Análise dos erros extremos (maiores diferenças)

Salvamento do modelo:

models/modelo_final.pkl

📁 Entregáveis:

notebooks/04_Otimizacao.ipynb

models/modelo_final.pkl

Gráficos de avaliação final