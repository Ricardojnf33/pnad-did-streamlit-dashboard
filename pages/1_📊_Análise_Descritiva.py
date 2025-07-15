import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Análise Descritiva")

@st.cache_data
def load_data():
    return pd.read_csv('pnad_did_para_dashboard.csv')

df = load_data()

st.title("📊 A Premissa Chave: Tendências Paralelas")
st.markdown(
    """
    A credibilidade de toda a nossa análise depende de uma suposição fundamental: a **premissa de tendências paralelas**.
    Ela afirma que, se a política de ETI nunca tivesse sido implementada, a renda média dos grupos de tratamento e controle
    teria seguido trajetórias paralelas ao longo do tempo.

    Não podemos provar isso diretamente, mas podemos buscar evidências observando as tendências no **período pré-tratamento**.
    Se as linhas no gráfico abaixo forem aproximadamente paralelas antes de 2020, isso fortalece nossa confiança no modelo.
    """
)

# --- Lógica do Gráfico ---
df_trends = df.copy()
df_trends['renda_ponderada'] = df_trends['log_renda'] * df_trends['peso_amostral']
summary_trends = df_trends.groupby(['ano', 'treat']) \
                          .agg(renda_ponderada_sum=('renda_ponderada', 'sum'),
                               peso_sum=('peso_amostral', 'sum')) \
                          .reset_index()
summary_trends['log_renda_media'] = summary_trends['renda_ponderada_sum'] / summary_trends['peso_sum']
summary_trends['Grupo'] = summary_trends['treat'].map({0: 'Controle', 1: 'Tratamento'})

# --- Gráfico Interativo com Plotly ---
fig = px.line(
    summary_trends,
    x='ano',
    y='log_renda_media',
    color='Grupo',
    labels={'ano': 'Ano', 'log_renda_media': 'Log da Renda Média Ponderada', 'Grupo': 'Grupo'},
    title='<b>Tendências da Renda Média: Grupos de Tratamento vs. Controle</b>',
    markers=True,
    color_discrete_map={'Controle': '#0072B2', 'Tratamento': '#D55E00'}
)

fig.add_vline(x=2019.5, line_width=2, line_dash="dash", line_color="red",
              annotation_text="Início da Política", annotation_position="top right")

fig.update_layout(
    title_font_size=22,
    legend_title_font_size=16,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

st.info(
    """
    **Observação:** As linhas antes de 2020 (à esquerda da linha vermelha) seguem uma trajetória semelhante,
    embora não perfeitamente idêntica. Isso fornece suporte visual para a plausibilidade da premissa de tendências paralelas.
    """,
    icon="✅"
)