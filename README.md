# 🧾 Gerenciamento de Produtos (PostgreSQL + Python)

Este projeto é um simples script em **Python** que realiza operações básicas (CRUD) em uma tabela de produtos dentro de um banco de dados **PostgreSQL**.

## ⚙️ Funcionalidades

- **Criar tabela:** Cria a tabela `produtos` caso ainda não exista.  
- **Adicionar produto:** Insere novos produtos no banco.  
- **Listar produtos:** Retorna todos os produtos cadastrados.  
- **Atualizar quantidade:** Modifica a quantidade de um produto existente.  
- **Atualizar preço:** Altera o preço de um produto.  
- **Deletar produto:** Remove um produto do banco.

## 🧩 Estrutura da Tabela

| Coluna      | Tipo         | Descrição                        |
|--------------|--------------|----------------------------------|
| id           | SERIAL (PK)  | Identificador único do produto.  |
| nome         | VARCHAR(100) | Nome do produto.                 |
| categoria    | VARCHAR(50)  | Categoria do produto.            |
| preco        | NUMERIC(10,2)| Preço do produto.                |
| quantidade   | INT          | Quantidade em estoque.           |

## 📂 Arquivos

- `main.py` → Contém as funções CRUD e a criação da tabela.  
- `conexao.py` → Responsável pela conexão com o banco de dados PostgreSQL. Deve conter algo como:
  ```python
  import psycopg2

  def conectar():
      try:
          conexao = psycopg2.connect(
              host="localhost",
              database="seu_banco",
              user="seu_usuario",
              password="sua_senha"
          )
          cursor = conexao.cursor()
          return conexao, cursor
      except Exception as erro:
          print(f"Erro ao conectar: {erro}")
          return None, None
