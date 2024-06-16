import pandas as pd


def ler_login_credenciais(file_path):
    df = pd.read_csv(file_path)
    return df.iloc[0]['username'], df.iloc[0]['password']
