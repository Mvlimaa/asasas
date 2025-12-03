📊 Etapa 1 — Análise Exploratória de Dados (EDA)

Projeto de Machine Learning – Entendimento dos Dados

🎯 Visão Geral

Na Etapa 1, o objetivo foi explorar, compreender e visualizar o dataset bruto para identificar problemas, padrões, distribuições e relações entre variáveis.
Essa fase é fundamental para orientar o que será feito no pré-processamento (Etapa 2) e na modelagem (Etapa 3).

Todo o trabalho foi documentado no notebook:
📁 notebooks/01_Analise_Exploratoria.ipynb

📝 Tarefas Realizadas
1️⃣ Carregamento e Inspeção Inicial
✔️ O que foi feito:

Carregamento do dataset bruto.

Visualização das primeiras linhas e dos tipos de dados.

Análise de:

Número de linhas e colunas

Tipos das variáveis (numéricas, categóricas, datas, texto)

Estatísticas gerais com .describe()

🎯 Objetivo: entender a estrutura do dataset e identificar possíveis problemas logo de início.

2️⃣ Análise de Valores Faltantes
✔️ O que foi feito:

Identificação de colunas com valores ausentes (NaN).

Quantificação do total de valores faltantes por coluna e porcentagem afetada.

Visualização gráfica (quando necessário) para destacar gravidade e impacto.

🎯 Importância: valores faltantes serão tratados apenas na Etapa 2, mas aqui foi fundamental detectar onde, quanto e por quê isso acontece.

3️⃣ Análise Estatística das Variáveis Numéricas
✔️ O que foi feito:

Histograma para cada variável numérica.

Boxplots para identificação de:

Distribuição

Assimetria

Presença de outliers

Cálculo de medidas importantes:

Média

Mediana

Desvio padrão

Quartis

🎯 Objetivo: entender o comportamento das variáveis, localizar outliers e possíveis transformações necessárias.

4️⃣ Análise das Variáveis Categóricas
✔️ O que foi feito:

Contagem de categorias (value_counts).

Gráficos de barras mostrando a frequência de cada categoria.

Verificação da qualidade das categorias:

Inconsistências

Categorias muito raras

Erros de digitação

🎯 Objetivo: mapear categorias antes de aplicar encoding na Etapa 2.

5️⃣ Correlação Entre Variáveis
✔️ O que foi feito:

Matriz de correlação entre variáveis numéricas.

Heatmap para visualizar relações fortes e fracas.

Identificação de:

Variáveis redundantes

Possíveis features importantes para o modelo

🎯 Objetivo: entender como variáveis se relacionam entre si e prever impacto na modelagem.

6️⃣ Geração dos Gráficos Principais (somente os mais importantes)

O professor pediu apenas os gráficos essenciais, então os principais incluídos foram:

📈 Histograma de variáveis mais relevantes

📦 Boxplot destacando outliers importantes

📊 Gráfico de barras das categorias mais significativas

🔥 Heatmap com as correlações principais

🎯 Esses gráficos serviram para comprovar visualmente que a exploração foi realizada corretamente.

📁 Entregáveis
Arquivo	Descrição
📓 notebooks/01_Analise_Exploratoria.ipynb	Notebook completo com análises e gráficos
📁 data/raw/*	Dataset bruto utilizado
🎤 Apresentação (4–5 Minutos)
🖼️ Slide 1 — Visão Geral do Dataset

Quantidade de linhas e colunas

Tipos de variáveis

🧩 Slide 2 — Problemas Identificados

Valores faltantes

Outliers

Inconsistências

📊 Slide 3 — Principais Gráficos

Histogramas essenciais

Boxplot mais relevante

Heatmap de correlações

📌 Slide 4 — Conclusão

O que foi aprendido sobre os dados

Preparação para Etapa 2 (limpeza e transformação)

✅ Checklist de Sucesso

 Dataset carregado e analisado com clareza

 Valores faltantes identificados

 Outliers mapeados

 Variáveis categóricas entendidas

 Correlações visualizadas

 Gráficos principais gerados e revisados

🚀 Conclusão

A Etapa 1 forneceu entendimento profundo dos dados, revelando problemas e padrões cruciais para o pré-processamento.
Agora, com essa análise completa, foi possível seguir para a Etapa 2 com segurança, limpando e preparando os dados da forma correta.

📦 Etapa 2 — Pré-Processamento de Dados
Projeto de Machine Learning – Preparação dos Dados

🎯 Visão Geral
Nesta etapa, realizamos a limpeza, transformação e padronização dos dados brutos analisados na Etapa 1.
O objetivo é deixar o dataset pronto para treinar modelos de Machine Learning, garantindo qualidade, consistência e formato adequado.
Todo o trabalho desta etapa está documentado no notebook:
📁 notebooks/02_Preprocessamento.ipynb

📝 Tarefas Realizadas
1️⃣ Tratamento de Valores Faltantes
Por que fazer isso?
➡️ Algoritmos de Machine Learning não lidam com NaN. Deixar valores faltantes gera erros e prejudica o modelo.
✔️ O que foi feito:


Colunas numéricas: valores imputados usando mediana (mais segura contra outliers).

Colunas categóricas: preenchimento com a categoria mais frequente.

2️⃣ Tratamento de Outliers
Por que fazer isso?
➡️ Outliers distorcem escalas, atrapalham modelos lineares e podem influenciar negativamente os resultados.
✔️ O que foi feito:


Outliers foram identificados com base na análise da Etapa 1.


Aplicada a técnica de capping (limite pelo IQR) para reduzir impacto sem remover dados importantes.


Remoção apenas de valores claramente incorretos (quando identificado como erro de digitação/medição).



3️⃣ Encoding de Variáveis Categóricas
Por que fazer isso?
➡️ Modelos de ML não entendem texto. Precisamos converter para números.
✔️ O que foi feito:


One-Hot Encoding aplicado para variáveis categóricas nominais.


Utilizado drop_first=True para evitar multicolinearidade.


Variáveis com ordem natural (ordinais) foram codificadas com mapeamento numérico apropriado.



4️⃣ Normalização das Variáveis Numéricas
Por que fazer isso?
➡️ Colunas em escalas muito diferentes podem fazer o modelo priorizar algumas features sem necessidade.
✔️ O que foi feito:


Aplicado StandardScaler (média 0 e desvio padrão 1) após limpeza completa.


O scaler foi salvo para uso futuro:
📁 models/scaler.pkl



5️⃣ Feature Engineering (Opcional)
Por que fazer isso?
➡️ Novas features podem ajudar o modelo a aprender padrões mais profundos.
✔️ O que foi criado:


Features derivadas de relações entre variáveis (exemplo: velocidade média, razões entre colunas etc. — adapte conforme seu projeto).


Cada feature criada foi documentada e justificada no notebook.



📊 Entregáveis Principais
ArquivoDescrição📓 notebooks/02_Preprocessamento.ipynbCódigo + explicações da etapa📁 data/students_clean.csvDataset final tratado⚙️ models/scaler.pklScaler salvo para uso na modelagem

🎤 Apresentação (4–5 Minutos)
🖼️ Slide 1 — Problemas Corrigidos


Quantidade de valores faltantes tratados


Outliers identificados e qual estratégia foi usada


🧩 Slide 2 — Principais Transformações


Exemplo de One-Hot Encoding


Comparação de variáveis antes/depois da normalização


🛠️ Slide 3 — Feature Engineering


Novas features criadas


Motivação e impacto esperado


📊 Slide 4 — Resultado Final


Dimensões antes e depois


Confirmação de que o dataset está pronto para modelagem



✅ Checklist de Sucesso


 Notebook organizado com seções claras


 Justificativas detalhadas em Markdown


 Dataset final salvo corretamente


 Scaler salvo em models/scaler.pkl


 Notebook executa do início ao fim sem erros


🚀 Conclusão
A Etapa 2 garante que os dados estejam consistentes, completos e padronizados — prontos para avançarmos para a etapa de modelagem na fase 3!


# 📊 Etapa 3 — Modelo Baseline (Regressão Linear)
Projeto de Machine Learning – Construção do Primeiro Modelo

## 🎯 Visão Geral

Na Etapa 3, construímos nosso **primeiro modelo de Machine Learning** — um baseline usando **Regressão Linear**. 
Este modelo servirá como referência para comparar com modelos mais complexos no futuro.

O objetivo é:
- ✔️ Treinar um modelo simples e interpretável
- ✔️ Avaliar desempenho com métricas padrão
- ✔️ Detectar problemas como overfitting
- ✔️ Compreender quais variáveis mais impactam a previsão

Todo o trabalho desta etapa está documentado no notebook:
📁 **notebooks/03_Modelo_Baseline.ipynb**

---

## 📝 Tarefas Realizadas

### 1️⃣ Carregamento dos Dados Limpos

**Por que fazer isso?**
➡️ Usamos os dados já processados da Etapa 2, garantindo qualidade e consistência.

**✔️ O que foi feito:**

- Carregamento do arquivo `delivery_clean.csv` gerado na Etapa 2
- Verificação de integridade (formas, tipos de dados)
- Confirmação de que não há valores faltantes

---

### 2️⃣ Preparação das Features (X) e Target (y)

**Por que fazer isso?**
➡️ Precisamos separar variáveis de entrada (features) da variável que queremos prever (target).

**✔️ O que foi feito:**

- **Target (y):** `delivery_time_hours` — o que o modelo vai prever
- **Features (X):** todas as outras colunas relevantes
- Remoção de IDs e colunas não úteis (`delivery_id`)
- Sincronização entre X e y para garantir consistência

---

### 3️⃣ Codificação de Variáveis Categóricas

**Por que fazer isso?**
➡️ A Regressão Linear só funciona com números. Variáveis texto precisam ser convertidas.

**✔️ O que foi feito:**

- Identificação de colunas categóricas (texto)
- Aplicação de **One-Hot Encoding** com `pd.get_dummies()`
- Uso de `drop_first=True` para evitar multicolinearidade (armadilha de dummy)
- Resultado: features aumentaram de X colunas para Y colunas (mais features binárias)

---

### 4️⃣ Tratamento de Valores Faltantes (NaN)

**Por que fazer isso?**
➡️ Regressão Linear não aceita NaN nativamente e gera erros.

**✔️ O que foi feito:**

- Verificação de NaN por coluna após codificação
- **Remoção de linhas com valores faltantes** (mantém consistência)
- Sincronização: quando removemos linhas de X, removemos as mesmas de y
- Resultado: dataset limpo e pronto para treinamento

---

### 5️⃣ Divisão dos Dados (Train / Validation / Test)

**Por que fazer isso?**
➡️ Precisamos de dados separados para:
- **Treinar** o modelo
- **Validar** durante desenvolvimento
- **Testar** de forma imparcial no final

**✔️ O que foi feito:**

- **60% Treino** (X_train, y_train) — dados para ajustar os pesos do modelo
- **20% Validação** (X_val, y_val) — dados para avaliar e ajustar hiperparâmetros
- **20% Teste** (X_test, y_test) — dados **guardados** para avaliação final (NÃO USAR AGORA)

**Método:** 
1. Separar 20% para teste
2. Do restante, separar 25% para validação (25% de 80% = 20% do total)

---

### 6️⃣ Treinamento do Modelo Baseline

**Por que Regressão Linear?**
➡️ É simples, rápido, interpretável e fornece uma boa linha de base para comparação.

**✔️ O que foi feito:**

```python
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_train, y_train)
```

- Ajuste dos coeficientes β para minimizar o erro quadrático
- O modelo aprendeu a relação linear entre features e target
- **Resultado:** Modelo treinado pronto para fazer previsões

---

### 7️⃣ Análise dos Coeficientes (Feature Importance)

**Por que fazer isso?**
➡️ Entender quais variáveis mais impactam a previsão de tempo de entrega.

**✔️ O que foi feito:**

- Extração dos coeficientes do modelo
- Ranking das features por impacto (valor absoluto)
- **Top 5 Variáveis Mais Impactantes** identificadas
- Interpretação: coeficientes positivos aumentam o tempo, negativos diminuem

**Exemplo de saída:**
```
Feature                  Coeficiente
distance_km              3.45
package_weight_kg        0.82
shipping_class_Standard -0.50
...
```

---

### 8️⃣ Avaliação e Métricas

**Por que fazer isso?**
➡️ Quantificar o desempenho do modelo com métricas padrão e detectar problemas.

**✔️ Métricas Calculadas:**

| Métrica | O que significa | Fórmula | Melhor valor |
|---------|-----------------|---------|--------------|
| **MSE** | Erro Quadrático Médio | Média de (y - ŷ)² | Próximo de 0 |
| **RMSE** | Raiz do MSE | √MSE | Próximo de 0 |
| **MAE** | Erro Absoluto Médio | Média de \|y - ŷ\| | Próximo de 0 |
| **R²** | Coeficiente de Determinação | 1 - (SS_res / SS_tot) | Próximo de 1 |

**✔️ O que foi feito:**

- Previsões em Treino: `y_train_pred = modelo.predict(X_train)`
- Previsões em Validação: `y_val_pred = modelo.predict(X_val)`
- Cálculo de MSE, RMSE, MAE e R² para ambos os conjuntos
- **Comparação Treino vs Validação** em tabela clara

**Exemplo de saída:**
```
          MSE      RMSE     MAE      R²
Treino    2.34     1.53    0.98    0.87
Validação 2.67     1.63    1.05    0.84
```

---

### 9️⃣ Detecção de Overfitting

**Por que fazer isso?**
➡️ Overfitting ocorre quando o modelo memoriza treino mas falha em dados novos.

**✔️ O que foi feito:**

- Cálculo da diferença de R² entre Treino e Validação
- **Análise:** 
  - Diferença < 0.10 → ✅ Modelo generaliza bem
  - Diferença > 0.10 → ⚠️ Possível overfitting

**Exemplo:**
```
Diferença R²: 0.03 → ✅ SUCESSO: Modelo generaliza bem (sem overfitting grave)
```

---

### 🔟 Visualizações

**Por que fazer isso?**
➡️ Gráficos facilitam entendimento visual do desempenho.

**✔️ O que foi feito:**

#### **Gráfico 1: Predito vs Real (Scatter Plot)**
- Eixo X: Valores reais de tempo de entrega
- Eixo Y: Previsões do modelo
- Linha vermelha: previsão perfeita (y = x)
- Interpretação: quanto mais próximo da linha, melhor o modelo
- Salvo em: `models/predicoes_vs_real.png`

#### **Gráfico 2: Distribuição de Resíduos (Histogram)**
- Resíduos = Erro (Real - Previsto)
- Distribuição ideal: simétrica e centrada em zero
- Presença de cauda pesada pode indicar outliers
- Salvo em: `models/residuos.png`

---

### 1️⃣1️⃣ Salvamento do Modelo

**Por que fazer isso?**
➡️ Reutilizar o modelo em produção sem treinar novamente.

**✔️ O que foi feito:**

```python
import joblib

joblib.dump(modelo, 'models/baseline_model.pkl')
```

- Modelo serializado e salvo
- Pode ser carregado depois com: `joblib.load('models/baseline_model.pkl')`
- Localização: `📁 models/baseline_model.pkl`

---

## 📊 Entregáveis Principais

| Arquivo | Descrição |
|---------|-----------|
| 📓 `notebooks/03_Modelo_Baseline.ipynb` | Código + explicações do treinamento |
| 📁 `models/baseline_model.pkl` | Modelo treinado salvo |
| 📈 `models/predicoes_vs_real.png` | Gráfico Predito vs Real |
| 📉 `models/residuos.png` | Distribuição de resíduos |

---

## 🎤 Apresentação (4–5 Minutos)

### 🖼️ Slide 1 — Visão Geral do Modelo

- Tipo: Regressão Linear (Baseline)
- Dados: 2510 amostras, X features após encoding
- Divisão: 60% treino, 20% validação, 20% teste

### 🧩 Slide 2 — Processo de Preparação

- Codificação de categorias (One-Hot Encoding)
- Tratamento de NaN
- Divisão estratégica dos dados

### 📊 Slide 3 — Métricas e Desempenho

- Tabela comparativa Treino vs Validação
- R² do modelo
- Diferença de R² (análise de overfitting)
- **Conclusão:** Modelo generaliza bem? Há overfitting?

### 🔍 Slide 4 — Top Features e Interpretação

- 5 variáveis mais impactantes
- Qual aumenta/diminui tempo de entrega?
- Faz sentido com o negócio?

### 📈 Slide 5 — Gráficos Principais

- Predito vs Real (scatter plot)
- Distribuição de resíduos

---

## ✅ Checklist de Sucesso

- ✔️ Dados carregados e preparados sem erros
- ✔️ Features codificadas (One-Hot Encoding aplicado)
- ✔️ NaN tratados apropriadamente
- ✔️ Dados divididos em treino/validação/teste
- ✔️ Modelo treinado com sucesso
- ✔️ Métricas calculadas (MSE, RMSE, MAE, R²)
- ✔️ Overfitting analisado
- ✔️ Gráficos gerados e salvos
- ✔️ Modelo salvo em `.pkl`
- ✔️ Notebook executa do início ao fim sem erros

---

## 🚀 Próximos Passos

Agora que temos um modelo baseline:

1. **Etapa 4 (Modelos Avançados):** Testar Random Forest, XGBoost, etc.
2. **Ajustes:** Tuning de hiperparâmetros
3. **Validação Final:** Avaliar no conjunto de teste
4. **Deploy:** Colocar o melhor modelo em produção

---

## 🎓 Conclusão

A Etapa 3 estabeleceu uma **linha de base sólida** com Regressão Linear. 
Este modelo simples e interpretável serve como referência para futuras melhorias e fornece insights sobre quais features impactam mais o tempo de entrega.

**Com essa estrutura, estamos prontos para avançar para modelagem mais sofisticada!** 🚀