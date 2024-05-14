import streamlit as st

# Define a largura do layout como "wide"
st.set_page_config(layout="wide")

# Adiciona um título para a barra lateral
st.sidebar.title("INFORMAÇÕES GERAIS")

# Primeiro radio para selecionar um grupo
grupo_selecionado = st.sidebar.radio(
    "Selecione uma opção:", ["Panorama Geral", "Produção Intelectual"]
)

# Lista de opções para o selectbox
opcoes_selectbox = []

# Dependendo do grupo selecionado, definir as opções para o selectbox
if grupo_selecionado == "Panorama Geral":
    opcoes_selectbox = ["Status Jurídico", "Grau do Curso", "Conceitos do Curso"]
elif grupo_selecionado == "Produção Intelectual":
    opcoes_selectbox = ["Trabalho Completo", "Patentes"]

# Segundo selectbox para selecionar uma opção
opcao_selectbox = st.sidebar.selectbox(
    "Escolha uma opção:",
    opcoes_selectbox
)

ano_selectbox = st.sidebar.selectbox(
    "Selecione o ano:",
    ["2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013"])

# Função para carregar imagens com base na configuração do radio e selectbox
def carregar_imagens(grupo, select_box, ano, largura):
    imagens = []

    # Condições para exibir imagens com base no grupo e no selectbox
    if grupo == "Panorama Geral":
        if select_box == "Status Jurídico":
            imagens = [("figuras\\status_juridico_{0}.jpg".format(ano), "Status Jurídico")]
        elif select_box == "Grau do Curso":
            imagens = [("figuras\\grau_curso_{0}.jpg".format(ano), "Grau do Curso")]
        elif select_box == "Conceitos do Curso":
            imagens = [("figuras\\conceito_curso_{0}.jpg".format(ano), "Conceito do Curso")]
    elif grupo == "Produção Intelectual":
        if select_box == "Trabalho Completo":
            imagens = [("figuras\\grupo01_natureza_trabalho_b_{0}.jpg".format(ano), "Trabalho Completo")]
        elif select_box == "Patentes":
            imagens = [("figuras\\grupo01_patentes_{0}.jpg".format(ano), "Patentes")]

    # Exibir as imagens se houver uma lista de imagens válida
    if imagens:
        st.image(imagens[0][0], caption=imagens[0][1], width=largura)
    else:
        st.write("Nenhuma imagem encontrada.")

# Chamar a função para mostrar as imagens com base no selectbox e radio button
carregar_imagens(grupo_selecionado, opcao_selectbox, ano_selectbox, largura=900)