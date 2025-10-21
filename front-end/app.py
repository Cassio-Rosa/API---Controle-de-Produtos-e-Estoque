import streamlit as st
import requests 

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador do Estoque", page_icon="🏬")
st.title("Gerenciador de Estoque")

menu = st.sidebar.radio("Navegação", ["Listar Produtos","Adicionar Produto","Deletar Produto","Atualizar Preço","Atualizar Quantidade de Produto"])

if menu == "Listar Produtos":
    st.subheader("Todos Produtos cadastrados")
    response = requests.get(f"{API_URL}/estoque")
    if response.status_code == 200:
        produtos = response.json().get("produtos",[])
        st.write(produtos)
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