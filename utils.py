import re
import pandas as pd


def separar_string(texto):
    """
    Expressão regular para verificar se a primeira palavra tem dois caracteres.

    :param texto: Texto a ser verificado.
    :return: Lista contendo as partes separadas do texto.
    """
    padrao = r"^(\w{2})\s(.+)$"
    match = re.match(padrao, texto)
    if match:
        return [match.group(1), match.group(2)]

    return texto.split()


def separar_cidade_estado(uf, df_estados):
    """
    Procura o estado pelo nome no DataFrame de estados.

    :param uf: String contendo a UF ou cidade e estado.
    :param df_estados: DataFrame contendo estados brasileiros.
    :return: Tupla contendo cidade e sigla do estado.
    """
    original_uf = uf
    splited_data = separar_string(uf)

    if len(splited_data) == 2:
        if len(splited_data[0]) == 2:
            uf = splited_data[0]
        else:
            uf = splited_data[0]
    elif len(splited_data) > 2:
        uf = " ".join(splited_data[:1])

    estado = df_estados[
        df_estados.apply(lambda row: uf in row["sigla"] or uf in row["nome"], axis=1)
    ]

    if not estado.empty:
        estado_sigla = estado.iloc[0]["sigla"]
        cidade = original_uf.replace(estado.iloc[0]["sigla"], "").strip()
    else:
        cidade, estado_sigla = original_uf, None

    return cidade, estado_sigla
