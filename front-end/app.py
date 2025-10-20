import streamlit as st
import requests 

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador do Estoque", page_icon="🏬")
st.title("Gerenciador de Estoque")

menu = st.sidebar.radio("Navegação", ["Listar Produtos","Adicionar Produto","Deletar Produto","Atualizar Preço","Atualizar Quantidade de Produto"])
