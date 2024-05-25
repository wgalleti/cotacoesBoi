import pandas as pd
from datetime import datetime, timedelta
from utils import separar_cidade_estado

from templates import EMAIL_HTML


def save_dataframe_to_csv(df, filename):
    """
    Salva um DataFrame em um arquivo CSV.

    :param df: DataFrame a ser salvo.
    :param filename: Nome do arquivo CSV.
    """
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M")
    df.to_csv(f"result/{current_time}-{filename}", index=False)
    print(f"Dados salvos em {filename}")


def gerar_html(data, df_estados):
    """
    Gera um HTML com títulos e tabelas a partir de uma lista de dicionários contendo títulos e DataFrames.

    :param data: Lista de dicionários contendo 'title' e 'dataframe'.
    :param df_estados: DataFrame contendo estados brasileiros.
    :return: String contendo o HTML gerado.
    """
    current_date = datetime.now() - timedelta(days=1)
    year, month, _ = current_date.strftime("%Y-%m-%d").split("-")
    date = current_date.strftime("%d/%m/%Y")
    for item in data:
        item["df"].insert(0, "Tipo", item.get("title"))

    df_result = pd.concat([i.get("df") for i in data], ignore_index=True)
    df_result[["Cidade", "Estado"]] = df_result["UF"].apply(
        lambda x: pd.Series(separar_cidade_estado(x, df_estados))
    )
    df_result = df_result.assign(Data=date, Ano=year, Mês=month)

    df_result = df_result[["Data", "Ano", "Mês", "Tipo", "Cidade", "Estado", "Valor"]]

    return EMAIL_HTML.replace(
        "%date%",
        datetime.now().strftime("%Y-%m-%d %H:%M"),
    ).replace(
        "%table%",
        df_result.to_html(index=False),
    )
