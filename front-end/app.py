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
        st.write(dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso")
        else:
            st.error("Erro ao adicionar filme no estoque")