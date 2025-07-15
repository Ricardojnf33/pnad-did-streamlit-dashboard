import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Análise Causal | ETI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Carregamento dos Dados ---
@st.cache_data
def load_data():
    return pd.read_csv('pnad_did_para_dashboard.csv')

df = load_data()

# --- Barra Lateral ---
st.sidebar.title("Sobre o Projeto")
st.sidebar.info(
    """
    Este dashboard apresenta uma análise de **inferência causal** sobre o impacto
    das Escolas de Tempo Integral (ETI) na renda de jovens adultos no Brasil.

    A análise utiliza um modelo de **Diferenças em Diferenças (DiD)**
    com microdados da PNAD Contínua (2016-2023).

    **Navegue pelas páginas para explorar a análise.**
    """
)
st.sidebar.markdown("---")
st.sidebar.write("Desenvolvido com base em metodologias de nível PhD.")

# --- Conteúdo da Página Principal ---
st.title("🎓 Impacto Causal da Escola em Tempo Integral")
st.markdown("### Uma avaliação de políticas públicas através da ciência de dados")
st.markdown("---")

st.header("O Desafio: Medir o Verdadeiro Impacto de uma Política")
st.markdown(
    """
    O Brasil tem investido na expansão das **Escolas de Tempo Integral (ETI)** como uma
    estratégia para melhorar a educação e os resultados futuros dos alunos. Mas como saber
    se o programa realmente funciona?

    Uma simples comparação entre ex-alunos de ETI e de escolas de tempo parcial pode ser enganosa.
    Alunos mais motivados ou de famílias com mais recursos podem ter maior probabilidade de se matricular
    em uma ETI, e esses fatores, não a escola em si, poderiam explicar seu sucesso futuro.
    Isso é o que chamamos de **viés de seleção**.

    Para superar esse desafio, usamos uma abordagem quasi-experimental chamada **Diferenças em Diferenças (DiD)**.
    Esta técnica nos permite isolar o **efeito causal** da política, nos aproximando de uma resposta confiável.
    """
)

st.image(
    "https://placehold.co/1200x400/0072B2/FFFFFF?text=Visualiza%C3%A7%C3%A3o+da+Narrativa+Causal",
    caption="A jornada da correlação para a causalidade."
)

st.info("Use o menu à esquerda para navegar pelas etapas da nossa análise.", icon="👈")