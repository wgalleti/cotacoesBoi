ESTADOS = [
    {"sigla": "AC", "nome": "Acre"},
    {"sigla": "AL", "nome": "Alagoas"},
    {"sigla": "AP", "nome": "Amapá"},
    {"sigla": "AM", "nome": "Amazonas"},
    {"sigla": "BA", "nome": "Bahia"},
    {"sigla": "CE", "nome": "Ceará"},
    {"sigla": "DF", "nome": "Distrito Federal"},
    {"sigla": "ES", "nome": "Espírito Santo"},
    {"sigla": "GO", "nome": "Goiás"},
    {"sigla": "MA", "nome": "Maranhão"},
    {"sigla": "MT", "nome": "Mato Grosso"},
    {"sigla": "MS", "nome": "Mato Grosso do Sul"},
    {"sigla": "MG", "nome": "Minas Gerais"},
    {"sigla": "PA", "nome": "Pará"},
    {"sigla": "PB", "nome": "Paraíba"},
    {"sigla": "PR", "nome": "Paraná"},
    {"sigla": "PE", "nome": "Pernambuco"},
    {"sigla": "PI", "nome": "Piauí"},
    {"sigla": "RJ", "nome": "Rio de Janeiro"},
    {"sigla": "RN", "nome": "Rio Grande do Norte"},
    {"sigla": "RS", "nome": "Rio Grande do Sul"},
    {"sigla": "RO", "nome": "Rondônia"},
    {"sigla": "RR", "nome": "Roraima"},
    {"sigla": "SC", "nome": "Santa Catarina"},
    {"sigla": "SP", "nome": "São Paulo"},
    {"sigla": "SE", "nome": "Sergipe"},
    {"sigla": "TO", "nome": "Tocantins"},
]

EMAIL_HTML = """
<html>
  <head>
    <style>
      * {
        font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
          "Lucida Sans", Arial, sans-serif;
      }
      table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-size: 18px;
        text-align: left;
      }
      table thead tr {
        background-color: #009879;
        color: #ffffff;
        text-align: left !important;
        font-weight: bold;
      }
      table th,
      table td {
        padding: 12px 15px;
        border: 1px solid #dddddd;
      }
      table tbody tr {
        border-bottom: 1px solid #dddddd;
      }
      table tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
      }
      table tbody tr:last-of-type {
        border-bottom: 2px solid #009879;
      }
      table tbody tr:hover {
        background-color: #f1f1f1;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <div>
      <h2>Dados extraidos em %date%</h2>
      %table%
    </div>
  </body>
</html>   
"""
