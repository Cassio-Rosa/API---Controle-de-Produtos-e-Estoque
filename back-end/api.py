from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de Estoque")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindos ao gerenciador do Estoque"}

@app.post("/estoque")
def adicionar_produto(nome:str, categoria:str, preco:float, quantidade:int ):
    funcao.adicionar_produto(nome,categoria,preco,quantidade)
    return {"mensagem": "Produto adicionado com sucesso"}

@app.get("/estoque")
def listar_estoque():
    filmes = funcao.listar_produtos()
    lista = []
    for linhas in filmes:
        lista.append({

            "id": linhas[0],
            "nome": linhas[1],
            "categoria": linhas[2],
            "preco": linhas[3],
            "quantidade": linhas[4],
        })
    return {"produtos": lista}

@app.delete("/estoque/{id}")
def deletar_produtos(id: int):
    funcao.deletar_produto(id)
    return {"mensagem": "Produto deletado com sucesso"}

@app.put("/estoque/{id}")
def atualizar_estoque(id:int, novo_preco: float):
    funcao.atualizar_preço(id, novo_preco) 
    return {"mensagem": "Preço atualizado com sucesso"}

@app.put("/estoque/{id_estoque}")
def atualizar_estoque(id:int, novo_estoque: int):
    funcao.atualizar_quantidade(id, novo_estoque)
    return {"mensagem": "Estoque atualizado com sucesso"}


