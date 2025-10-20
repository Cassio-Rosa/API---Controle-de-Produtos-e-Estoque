from conexao import conectar


def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco NUMERIC(10,2),
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

def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao adicionar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "SELECT * FROM produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_quantidade(id,nova_quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "UPDATE produtos SET quantidade = %s WHERE id = %s",
            (nova_quantidade, id)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar quantidade: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_preço(id,novo_preco):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "UPDATE produtos SET preco = %s WHERE id = %s",
            (novo_preco, id)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar preço: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM produtos WHERE id = %s",(id_produto,))
            print("Deu certo")
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()



