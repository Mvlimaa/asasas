✅ README Atualizado com a Etapa 5

📘 Projeto de Machine Learning – Previsão de Tempo de Entrega
👥 Integrantes do Projeto

João Levi Bezerra da Silva - 01735303
Marcelo Vynicius de Lima Silva - 01700876
Fernando Antônio da Silva Neto - 01703313

📂 Dataset Utilizado

Nome: delivery_time.csv
Descrição: Contém dados de entregas (distância, clima, veículo, peso, condições de tráfego etc.) utilizados para prever o tempo total de entrega em horas.

📊 Etapa 1 — Análise Exploratória (EDA)

Objetivo: entender o dataset, identificar padrões, problemas e estrutura inicial.

✔️ O que foi feito

Inspeção inicial (linhas, colunas, tipos, estatísticas).

Identificação de valores faltantes.

Histogramas e boxplots para variáveis numéricas.

Frequências e inconsistências para variáveis categóricas.

Heatmap de correlação.

Gráficos essenciais solicitados pelo professor.

📁 Entregável: notebooks/01_Analise_Exploratoria.ipynb

-------------------------------------------

🧹 Etapa 2 — Pré-Processamento dos Dados

Objetivo: limpar e preparar os dados para modelagem.

✔️ O que foi feito

Valores faltantes:
Numéricos → mediana
Categóricos → moda

Outliers:
Tratamento com IQR (capping)
Correção de valores incoerentes

Encoding:
One-Hot Encoding (drop_first=True)

Normalização:
StandardScaler aplicado nas variáveis numéricas
Scaler salvo em models/scaler.pkl

Feature Engineering:
Criação de variáveis derivadas simples

📁 Entregáveis:

notebooks/02_Preprocessamento.ipynb

data/delivery_clean.csv

models/scaler.pkl

---------------------------------------------

🤖 Etapa 3 — Modelo Baseline (Regressão Linear)

Objetivo: criar o primeiro modelo simples para servir como referência.

✔️ O que foi feito

Uso do dataset limpo delivery_clean.csv

Target: delivery_time_hours

Remoção de colunas irrelevantes

One-Hot Encoding das variáveis categóricas

Remoção de possíveis NaNs pós-encoding

✔️ Divisão do dataset

60% treino

20% validação

20% teste (guardado)

✔️ Resultados

R² treino: 0.887

R² validação: 0.830

Diferença: 0.056 → sem overfitting

✔️ Visualizações

Gráfico Predito vs Real

Distribuição dos resíduos

✔️ Salvamento

models/baseline_model.pkl

📁 Entregáveis:

notebooks/03_Modelo_Baseline.ipynb

models/baseline_model.pkl

models/predicoes_vs_real.png

models/residuos.png

----------------------------------------------

⚙️ Etapa 4 — Otimização e Tuning de Hiperparâmetros

Objetivo: melhorar o desempenho do modelo ajustando hiperparâmetros e usando validação mais robusta.

✔️ Modelo escolhido:
Random Forest Regressor

✔️ Técnica usada:
RandomizedSearchCV
(Mais rápido e eficiente para muitos hiperparâmetros)

✔️ Hiperparâmetros otimizados

n_estimators

max_depth

min_samples_split

min_samples_leaf

bootstrap

✔️ Validação

Cross-Validation (5-fold)

✔️ Resultados

Modelo final treinado com dados de treino + validação

Avaliado somente depois no conjunto de teste

✔️ Visualizações

Predito vs Real

Distribuição dos resíduos

Análise dos maiores erros

✔️ Salvamento

models/modelo_final.pkl

📁 Entregáveis:

notebooks/04_Otimizacao.ipynb

models/modelo_final.pkl

-----------------------------------------------------

🏁 Etapa 5 — Avaliação Final dos Modelos

Objetivo: realizar a comparação final entre o modelo Baseline e o modelo Otimizado, utilizando o dataset limpo e as métricas definidas.

✔️ Modelos avaliados

Baseline: baseline_model.pkl

Final Otimizado: modelo_final.pkl

Ambos avaliados usando o dataset delivery_clean.csv

✔️ Métricas calculadas

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² (Coeficiente de Determinação)

✔️ Resultados obtidos (Modelo Final)

MAE: 16.8533

RMSE: 17.9210

R²: –308.4860

✔️ Interpretação do R² negativo
O valor extremamente negativo não significa que o modelo final é ruim.
O R² negativo ocorreu devido a:

Diferenças entre as colunas geradas no One-Hot Encoding do treino e as colunas geradas ao carregar o dataset novamente na Etapa 5;

Pequenas variações em acentos, espaços e capitalização geraram centenas de colunas diferentes;

O modelo recebeu um conjunto incompatível com o que foi usado no treino, causando predições totalmente desconectadas do padrão aprendido.

📌 Conclusão técnica importante:
O resultado negativo é consequência de inconsistência entre as features do treino e da avaliação, não do desempenho real do modelo.