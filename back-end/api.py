from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de Estoque")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindos ao gerenciador do Estoque"}

@app.post("/estoque")
def adicionar_produto(nome:str, categoria:str, preco:float, quantiade:int ):
    funcao.adicionar_produto(nome,categoria,preco,quantiade)
    return {"mensagem": "Produto adicionado com sucesso"}

@app.get("/estoque")
def listar_estoque():
    filmes = funcao.listar_produtos()
    lista = []
    for linhas in filmes:
        lista.append({

            "ID": linhas[0],
            "Nome": linhas[1],
            "Categorias": linhas[2],
            "Preço": linhas[3],
            "Quantidade": linhas[4],
        })
    return {"filmes": lista}

@app.delete("/estoque")
def deletar_filmes(id: int):
    funcao.deletar_produto(id)
    return {"mensagem": "Filme Deletado com Sucesso"}

@app.put("/estoque/{id_estoque}/preço")
def atualizar_estoque(id:int, novo_preco: float):
    funcao.atualizar_preço(id, novo_preco)
    return {"mensagem": "Preço atualizado com sucesso"}

@app.put("/estoque/{id_estoque}/estoque")
def atualizar_estoque(id:int, novo_estoque: int):
    funcao.atualizar_quantidade(id, novo_estoque)
    return {"mensagem": "Estoque atualizado com sucesso"}


