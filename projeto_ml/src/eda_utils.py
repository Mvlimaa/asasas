import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------------------
# Função: Resumo de valores faltantes
# --------------------------------------------------------------
def missing_summary(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if len(missing) == 0:
        print("✅ Nenhum valor faltante encontrado.")
    else:
        print("Valores faltantes por coluna:\n")
        print(missing)

# --------------------------------------------------------------
# Função: Mapa de correlação
# --------------------------------------------------------------
def correlation_heatmap(df, target=None):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matriz de Correlação")
    plt.show()

# --------------------------------------------------------------
# Função: Detecção de outliers usando IQR
# --------------------------------------------------------------
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"{column}: {len(outliers)} outliers encontrados.")
