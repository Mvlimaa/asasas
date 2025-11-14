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