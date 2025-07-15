# 🎓 Análise de Impacto Causal: Escolas de Tempo Integral e Resultados no Mercado de Trabalho

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pnad-did-streamlit-dashboard.streamlit.app/)

## 1. Visão Geral do Projeto

Este repositório contém uma análise de **inferência causal** que estima o impacto da expansão das **Escolas de Tempo Integral (ETI)** sobre os resultados de jovens adultos no mercado de trabalho brasileiro. O objetivo principal é ir além da simples correlação e medir o **efeito causal** de frequentar uma ETI na renda e na probabilidade de emprego formal.

Para superar desafios clássicos de análise de políticas públicas, como o **viés de seleção** (onde alunos mais propensos a ter sucesso podem ser também os mais propensos a se matricular em ETIs), este projeto emprega um modelo econométrico quasi-experimental: **Diferenças em Diferenças (DiD)**.

O projeto está dividido em duas partes principais:
1.  **Análise e Modelagem:** Um notebook Jupyter (`Projeto_DiD_PNAD.ipynb`) que detalha todo o processo CRISP-DM, desde a coleta e tratamento dos dados da PNAD Contínua até a estimação do modelo DiD.
2.  **Dashboard Interativo:** Uma aplicação web construída com **Streamlit** que apresenta os resultados da análise de forma visual e interativa, permitindo um *storytelling* eficaz sobre a metodologia e as conclusões.

## 2. Metodologia

A metodologia é o pilar desta análise, garantindo que as conclusões sejam robustas e defensáveis.

### Fonte de Dados
- **PNAD Contínua (IBGE):** Foram utilizados os microdados anuais do 4º trimestre, abrangendo o período de **2016 a 2023**. Os dados foram acessados via o *datalake* público do `basedosdados`.
- **Amostra:** Jovens entre 20 e 25 anos.

### Modelo de Diferenças em Diferenças (DiD)
A análise utiliza um modelo DiD, cuja equação geral é:

$$ Y_{ist} = \beta_0 + \beta_1 \cdot \text{Treat}_s + \beta_2 \cdot \text{Post}_t + \delta \cdot (\text{Treat}_s \times \text{Post}_t) + \gamma \cdot X_{ist} + \epsilon_{ist} $$

Onde:
- **\(Y_{ist}\)** é a variável de resultado (log da renda) para o indivíduo *i* no estado *s* e ano *t*.
- **\(\text{Treat}_s\)** é uma variável que indica se o estado *s* pertence ao grupo de tratamento.
- **\(\text{Post}_t\)** indica se o período *t* é posterior ao início da política (definido como 2020).
- **\(\delta\)** é o **coeficiente de interesse (estimador DiD)**. Ele captura o efeito causal médio da política.
- **\(X_{ist}\)** são covariadas de controle (idade, sexo, cor/raça).

Para a validação do modelo, foi realizada a verificação da **premissa de tendências paralelas**, que assume que os grupos de tratamento e controle teriam trajetórias de resultado paralelas na ausência da política.

### Definição dos Grupos (Simulação)
Para fins de demonstração da metodologia, os grupos foram definidos da seguinte forma:
- **Grupo de Tratamento:** Estados da região Nordeste, que hipoteticamente expandiram as ETIs.
- **Grupo de Controle:** Estados da região Sul.

## 3. Estrutura do Repositório

```
Projeto_DiD_PNAD/
│
├── .streamlit/
│   └── config.toml
├── pages/
│   ├── 1_📊_Análise_Descritiva.py   # Script da página de análise exploratória
│   └── 2_💡_O_Efeito_Causal.py     # Script da página de resultados do modelo
│
├── app.py                          # Script principal da aplicação Streamlit
├── pnad_did_para_dashboard.csv       # Dataset final, limpo e processado
├── requirements.txt                # Dependências Python do projeto
├── Projeto_DiD_PNAD.ipynb          # Notebook com a análise completa
└── README.md                       # Este arquivo
```

## 4. Como Executar o Projeto Localmente

Para explorar a análise ou rodar o dashboard no seu próprio computador, siga os passos abaixo.

### Pré-requisitos
- Python 3.9+
- `pip` e `venv`

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/SEU-USUARIO/pnad-did-streamlit-dashboard.git
    cd pnad-did-streamlit-dashboard
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    # No Windows, use: .venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run app.py
    ```

    A aplicação abrirá automaticamente no seu navegador.

## 5. Dashboard Interativo

O dashboard interativo, disponível online, serve como a principal ferramenta de comunicação dos resultados. Ele é estruturado em três seções:

1.  **Página Inicial:** Apresenta o problema de negócio, a questão causal e a metodologia utilizada.
2.  **Análise Descritiva:** Permite a exploração visual das características dos grupos de tratamento e controle ao longo do tempo.
3.  **O Efeito Causal:** Mostra o resultado central da análise — o gráfico de tendências paralelas e o coeficiente DiD estimado, com sua interpretação e significância estatística.

---
*Este projeto foi desenvolvido como um portfólio de análise de dados e econometria aplicada, demonstrando competências em inferência causal, manipulação de microdados e desenvolvimento de produtos de dados. Feito por Ricardo Fernandes e Raymundo Martins* 