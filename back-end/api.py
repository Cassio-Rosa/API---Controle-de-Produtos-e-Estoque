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