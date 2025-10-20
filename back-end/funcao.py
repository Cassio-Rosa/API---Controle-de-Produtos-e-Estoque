from conexao import conectar
#pip install psycopg2 dotenv streamlit fastapi uvicorn requests

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco DECIMAL(10,2),
                quantidade INT
                );
            """)
            conexao.commit()
            print("Deu bom")
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()