import pandas as pd

from extractor import extract_table_data, fetch_page_content
from processor import save_dataframe_to_csv, gerar_html
from templates import ESTADOS


def raspar_cotacoes():
    """
    Raspa cotações das páginas especificadas e salva os dados em arquivos CSV.
    """
    df_estados = pd.DataFrame(ESTADOS)

    extracts = [
        {
            "link": "boi-gordo",
            "parametros": [
                {
                    "title": "Boi gordo China",
                    "table_identifiers": {
                        "cellpadding": "0",
                        "cellspacing": "0",
                        "width": "660px",
                    },
                    "headers": ["UF", "Valor"],
                    "save_to": "boi_china_prazo.csv",
                },
                {
                    "title": "Boi gordo mercado físico",
                    "table_identifiers": {
                        "border": "0",
                        "cellpadding": "0",
                        "cellspacing": "0",
                        "width": "660",
                    },
                    "headers": ["UF", "Valor"],
                    "save_to": "boi_mercado_fisico.csv",
                },
            ],
        },
        {
            "link": "vaca-gorda",
            "parametros": [
                {
                    "title": "Vaca Gorda",
                    "table_identifiers": {
                        "cellpadding": "0",
                        "cellspacing": "0",
                        "width": "660px",
                    },
                    "headers": ["UF", "Valor"],
                    "save_to": "vaca_mercado_fisico.csv",
                }
            ],
        },
        {
            "link": "novilha",
            "parametros": [
                {
                    "title": "Novilha",
                    "table_identifiers": {
                        "border": "0",
                        "cellpadding": "0",
                        "cellspacing": "0",
                        "width": "660",
                        "style": "margin-top: 10px",
                    },
                    "headers": ["UF", "Valor"],
                    "save_to": "novilha_mercado_fisico.csv",
                }
            ],
        },
    ]

    data = []

    # Scot Consultoria
    for extract in extracts:
        url = f"https://www.scotconsultoria.com.br/cotacoes/{extract['link']}/?ref=smn"
        soup = fetch_page_content(url)

        if soup:
            for parametros in extract["parametros"]:
                table_identifiers = parametros.get("table_identifiers")
                headers = parametros.get("headers")
                save_to = parametros.get("save_to")
                df = extract_table_data(soup, table_identifiers, headers)
                data.append({"title": parametros.get("title"), "df": df})
                save_dataframe_to_csv(df, save_to)
        else:
            print(f"Não foi possível acessar a página {url}")

    # CEPEA
    url = "https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx"
    soup = fetch_page_content(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        },
    )

    if soup:
        table = soup.find("table", {"id": "imagenet-indicador1"})
        if table:
            first_row = table.find("tbody").find("tr")
            date = first_row.find_all("td")[0].text.strip()
            value = first_row.find_all("td")[1].text.strip()

            df = pd.DataFrame([[date, value]], columns=["UF", "Valor"])
            data.append({"title": "CEPEA", "df": df})
        else:
            print("Tabela não encontrada.")

    file_name = "index.html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(gerar_html(data, df_estados))


if __name__ == "__main__":
    raspar_cotacoes()
