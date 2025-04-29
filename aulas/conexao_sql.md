# Criar o banco de dados no DBeaver e salvar

# 1. No DBeaver, criar um novo banco de dados SQLite.

# 2. Definir a estrutura das tabelas e inserir dados conforme necessário.

# 3. Salvar o arquivo do banco de dados localmente.

# Enviar esse arquivo para o Google Drive

# 1. Fazer upload do arquivo do banco de dados SQLite para o Google Drive.

# 2. Garantir que o caminho do arquivo esteja correto para ser acessado posteriormente.

# Abrir o Copilot e fazer a conexão com o banco de dados

# Importar a biblioteca sqlite3 para estabelecer a conexão com o banco de dados SQLite

import sqlite3

# Estabelecer a conexão com o banco de dados no Google Drive

coxecao = sqlite3.connect('/content/drive/MyDrive/ProgaMaria/status_brasil')

# Agora, a conexão está pronta para ser usada para consultas SQL!

# Criar uma query para selecionar dados da tabela Municipios_Brasileiros

query = "SELECT \* FROM Municipios_Brasileiros WHERE Cidade='Itaquaquecetuba';"

# Executar a query e carregar os resultados em um DataFrame usando Pandas

pd.read_sql(query, con=coxecao)
