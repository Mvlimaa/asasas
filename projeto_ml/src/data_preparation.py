import pandas as pd

def load_data(path):
    """
    Função para carregar o dataset CSV e retornar um DataFrame.
    """
    try:
        df = pd.read_csv(path)
        print(f"✅ Dataset carregado com sucesso! {df.shape[0]} linhas e {df.shape[1]} colunas.")
        return df
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo não encontrado em '{path}'. Verifique o caminho.")
    except Exception as e:
        print(f"❌ Erro ao carregar o dataset: {e}")
