#Codigo pra converter datas em formato errado
#Formato de entrada 2020-08-18 19:34:37.655 -0300
#Formato de saída 2021-08-18T19:34:37.655Z
#Especificar colunas e caminho dos arquivos, mudar nome do arquivo de output


import pandas as pd


path = "C:\\Users\\Usuario\\caminho\\arquivo.csv"


df = pd.read_csv(path)

# Formatar a data 
def format_date_with_three_digits(dt):
    if not pd.isnull(dt):
        formatted_date = dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        return formatted_date
    return ''

# Converte a coluna "last_paid_indication"
df["last_paid_indication"] = pd.to_datetime(df["last_paid_indication"], errors='coerce').apply(format_date_with_three_digits)

# Converte a coluna "last_waiting_indication"
df["last_waiting_indication"] = pd.to_datetime(df["last_waiting_indication"], errors='coerce').apply(format_date_with_three_digits)

df.to_csv("C:\\Users\\Usuario\\caminho\\arquivo_saida.csv", index=False)
