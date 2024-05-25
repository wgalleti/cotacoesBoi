import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_page_content(url, headers=None):
    """
    Faz a requisição HTTP para obter o conteúdo da página e retorna o BeautifulSoup.

    :param url: URL da página.
    :param headers: Cabeçalhos HTTP opcionais.
    :return: BeautifulSoup object.
    """
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")
    else:
        print(f"Erro ao acessar a página {url}: {response.status_code}")
        return None


def extract_table_data(soup, table_identifiers, headers):
    """
    Extrai dados de uma tabela específica do BeautifulSoup e retorna um DataFrame.

    :param soup: BeautifulSoup object contendo o HTML.
    :param table_identifiers: Dicionário com atributos para identificar a tabela.
    :param headers: Lista com os cabeçalhos das colunas.
    :return: DataFrame com os dados extraídos.
    """
    table = soup.find("table", table_identifiers)
    if not table:
        print(f"Tabela com identificadores {table_identifiers} não encontrada.")
        return pd.DataFrame()

    rows = []
    for tr in table.find_all("tr", {"class": "conteudo"}):
        cells = tr.find_all("td")
        if cells[0].text.strip() in headers:
            continue
        row = [cells[0].text.strip(), cells[1].text.strip()]
        rows.append(row)

    return pd.DataFrame(rows, columns=headers)
