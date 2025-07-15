import streamlit as st
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np

st.set_page_config(layout="wide", page_title="Resultados Causais")

@st.cache_data
def load_data():
    return pd.read_csv('pnad_did_para_dashboard.csv')

@st.cache_resource
def run_did_model(_df):
    formula_did = 'log_renda ~ treat * post + idade + C(sexo) + C(cor_raca)'
    model = smf.wls(
        formula=formula_did,
        data=_df,
        weights=_df['peso_amostral']
    ).fit(
        cov_type='cluster',
        cov_kwds={'groups': _df['UF']}
    )
    return model

df = load_data()
did_model = run_did_model(df)

st.title("💡 O Efeito Causal Estimado")
st.markdown(
    """
    Após validar a premissa chave, estimamos o modelo de Diferenças em Diferenças para quantificar
    o impacto da política de ETI. O resultado abaixo representa nossa melhor estimativa do **efeito causal**
    na renda dos jovens.
    """
)

# --- Extrair e Apresentar Resultados ---
coef_did = did_model.params['treat:post']
p_value_did = did_model.pvalues['treat:post']
conf_int = did_model.conf_int().loc['treat:post']

st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric(
    label="Aumento Causal na Renda (Efeito DiD)",
    value=f"{coef_did:.2%}",
    delta_color="normal"
)
col2.metric(
    label="Intervalo de Confiança (95%)",
    value=f"[{conf_int[0]:.2%}, {conf_int[1]:.2%}]"
)
col3.metric(
    label="Valor-P",
    value=f"{p_value_did:.3f}"
)

st.markdown("---")

# --- Interpretação dos Resultados ---
st.subheader("O que isso significa?")
if p_value_did < 0.05:
    st.success(
        f"""
        **Os resultados são estatisticamente significativos.** Nossa análise sugere que a expansão das
        Escolas de Tempo Integral causou um aumento médio de **{coef_did:.2%}** na renda dos jovens
        no grupo de tratamento, em comparação com o que teria acontecido na ausência da política.

        O intervalo de confiança nos diz que temos 95% de certeza de que o verdadeiro efeito está entre
        **{conf_int[0]:.2%}** e **{conf_int[1]:.2%}**. Como este intervalo não contém o zero,
        podemos rejeitar a hipótese de que a política não teve efeito.
        """,
        icon="🚀"
    )
else:
    st.warning(
        f"""
        **Os resultados não são estatisticamente significativos.** Embora o efeito estimado seja de
        **{coef_did:.2%}**, o alto valor-p ({p_value_did:.3f}) e o intervalo de confiança
        ([{conf_int[0]:.2%}, {conf_int[1]:.2%}]) — que inclui o zero — indicam que não podemos
        descartar a possibilidade de que este resultado seja devido ao acaso.

        Não encontramos evidências estatísticas robustas de que a política teve um impacto na renda.
        """,
        icon="⚠️"
    )

st.subheader("Resultados Completos da Regressão")
st.text(did_model.summary())

st.caption("Nota: Os erros-padrão são clusterizados por Unidade da Federação (UF) para garantir a robustez estatística.")