# **Passo a passo para criar um banco de dados no DBeaver (SQLite)**

## **1. Criar o banco de dados**

1. **Abra o DBeaver.**
2. No menu superior, clique em:
   - **Arquivo** > **Novo**.
3. Na janela que abrir, selecione:
   - **DBeaver** > **Conexão com banco de dados** e clique em **Avançar**.
4. Será exibida uma lista com vários tipos de banco de dados.
   - Selecione **SQLite** e clique em **Avançar**.
5. Na tela **Configurações de Conexão JDBC**, clique em **Criar** (ícone de pasta com **+**) para criar um novo arquivo de banco de dados.
6. Escolha o diretório onde deseja salvar o banco de dados e defina um **nome** para o arquivo (ex: `meu_banco.db`).
   - Depois, clique em **Salvar**.
7. De volta à tela anterior, clique em **Concluir**.

## **2. Adicionar um script SQL**

1. No menu superior, clique em:
   - **Editor SQL** > **Novo script SQL**.
2. Digite os comandos SQL abaixo para criar tabelas no banco de dados:

```sql
-- Criar a tabela Gerencia_Regiao
CREATE TABLE Gerencia_Regiao (
    gerencia_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Regiao TEXT(10) NOT NULL,
    pessoas_brancas INTEGER NOT NULL,
    pessoas_pretas_pardas INTEGER NOT NULL,
    gerencia_branca INTEGER NOT NULL,
    gerencia_preta_parda INTEGER NOT NULL,
    CONSTRAINT fk_regiao FOREIGN KEY (Regiao) REFERENCES Municipios_Brasileiros (Regiao)
);

-- Criar a tabela Municipios_Brasileiros
CREATE TABLE Municipios_Brasileiros (
    Cidade NVARCHAR(50) NOT NULL,
    Estado NVARCHAR(2) NOT NULL,
    Regiao NVARCHAR(20) NOT NULL,
    municipio_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
);

-- Criar a tabela Municipios_Status
CREATE TABLE Municipios_Status (
    status_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    populacao_residente INTEGER NOT NULL,
    IDHM_rank INTEGER NOT NULL,
    educacao INTEGER NOT NULL,
    renda INTEGER NOT NULL,
    municipio_ID INTEGER NOT NULL,
    CONSTRAINT fk_municipio FOREIGN KEY (municipio_ID) REFERENCES Municipios_Brasileiros(municipio_ID)
);
```
