import pandas as pd
import openpyxl
import os
from zipfile import BadZipFile

# Nome dos arquivos
arquivo_csv = "arquivos/arquivo_csv.csv"
arquivo_excel = "arquivos/arquivo_excel.xlsx"

# Criar diretório 'arquivos' se não existir
os.makedirs(os.path.dirname(arquivo_csv), exist_ok=True)

# Verificar se o arquivo CSV existe
if not os.path.exists(arquivo_csv):
    raise FileNotFoundError(f"O arquivo '{arquivo_csv}' não foi encontrado.")

# Ler os dados do CSV
df_csv = pd.read_csv(arquivo_csv, encoding='utf-8')  # Adicionando encoding para leitura correta

# Tentar carregar o arquivo Excel existente ou criar um novo
try:
    df_excel = pd.read_excel(arquivo_excel, engine='openpyxl')  # Especificando engine para leitura do Excel
    df_final = pd.concat([df_excel, df_csv], ignore_index=True)  # Adicionando novos dados
except FileNotFoundError:
    df_final = df_csv  # Se não existir, cria um novo
except BadZipFile:
    print(f"O arquivo '{arquivo_excel}' não é um arquivo Excel válido. Criando um novo arquivo.")
    df_final = df_csv  # Se o arquivo Excel estiver corrompido, cria um novo

# Salvando os dados no Excel
df_final.to_excel(arquivo_excel, index=False, engine='openpyxl')  # Especificando engine para salvar o Excel

print(f"Dados do '{arquivo_csv}' adicionados ao '{arquivo_excel}' com sucesso!")