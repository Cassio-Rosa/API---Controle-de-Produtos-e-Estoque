import streamlit as st
import requests 

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador do Estoque", page_icon="🏬")
st.title("Gerenciador de Estoque")

menu = st.sidebar.radio("Navegação", ["Listar Produtos","Adicionar Produto","Deletar Produto","Atualizar Preço","Atualizar Quantidade de Produto"])


response = requests.get(f"{API_URL}/estoque")
if response.status_code == 200:
    produto = response.json().get("produtos",[])
    ids = [linha["id"] for linha in produto]


if menu == "Listar Produtos":
    st.subheader("Todos Produtos cadastrados")
    response = requests.get(f"{API_URL}/estoque")
    if response.status_code == 200:
        produtos = response.json().get("produtos",[])

        if produtos:
            tabela_estoque = {

                "ID": [estoque["id"] for estoque in produtos],
                "Nome": [estoque["nome"] for estoque in produtos],
                "Categorias": [estoque["categoria"] for estoque in produtos],
                "Preço": [f"{estoque["preco"]:,.2f}" for estoque in produtos],
                "Quantidade": [estoque["quantidade"] for estoque in produtos]
            }

            st.table(tabela_estoque)
        else:
            st.warning("Não tem produtos")
    else:
        st.error("Erro as acessar a API")

elif menu == "Adicionar Produto":
    st.subheader("Adicionar Produto no Estoque")
    nome = st.text_input("Insira o nome do Produto")
    categoria = st.text_input("Insira a/as categorias do seu Produto")
    preco = st.number_input("Insira o valor do produto", min_value=0.00)
    quantidade = st.number_input("Insira a quantidade do Produto", min_value=0)
    if st.button("Salvar Produto"):
        dados = {"nome": nome, "categoria":categoria, "preco":preco,"quantidade":quantidade}
        response = requests.post(f"{API_URL}/estoque", params=dados)

        if response.status_code == 200:
            st.success("Produto adicionado com sucesso")
        else:
            st.error("Erro ao adicionar filme no estoque")

elif menu == "Deletar Produto":
    st.header("Deletar Produtos")
    id = st.selectbox("Escolha o ID do Produto que você desejar deletar", ids)
    response = requests.get(f"{API_URL}/estoque")
    if response.status_code == 200:
        if st.button("Deletar Produto"):
            response = requests.delete(f"{API_URL}/estoque/{id}")
            if response.status_code == 200:
                st.success("Produto deletado com sucesso!")
            else:
                st.error("Erro ao deletar produto")

elif menu == "Atualizar Preço":
    st.header("Atualizar o Preço de um produto")
    id = st.selectbox("Escolha o ID do Produto que você desejar alterar o preço", ids)
    response = requests.get(f"{API_URL}/estoque")

    if id:
        produtos = response.json().get("produtos",[])
        produto_selecionado = next(produto for produto in produtos if produto ['id'] == id)
        st.warning(f"informações do id inserido: {produto_selecionado}")
    if response.status_code == 200:
        preço =  st.number_input("Insira o valor do produto", min_value=0.00)
        if st.button("Atualizar o preço"):
            dados = {"preco": preço}

            response = requests.put(f"{API_URL}/estoque/{id}", params=dados)
            if response.status_code == 200:
                st.success("Preço alterado com sucesso")
            else:
                st.error("Erro ao trocar o preço do produto")

elif menu == "Atualizar Quantidade de Produto":
    st.header("Atualizar a Quantidade de um produto")
    id = st.selectbox("Escolha o ID do Produto que você desejar alterar a Quantidade", ids)
    response = requests.get(f"{API_URL}/estoque/{id}")
    
    if id:
        produtos = response.json().get("produtos",[])
        produto_selecionado = next(produto for produto in produtos if produto ['id'] == id)
        st.warning(f"informações do id inserido: {produto_selecionado}")
    if response.status_code == 200:
        nova_quantidade = st.number_input("Insira a nova quantidade do produto selecionado")
        dados = {"id": id, "quantidade": nova_quantidade}
        if st.button("Trocar"):
            response = requests.put(f"{API_URL}/estoque/{id}", params=dados)
            if response.status_code == 200:
                st.success("Quantidade alterado com sucesso")
            else:
                st.error("Erro ao trocar a quantidade do produto")

