import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="Acidentes de Trânsito", layout="wide", page_icon="📈")

df = pd.read_excel("acidentes.xlsx", skiprows=1, engine="openpyxl")

dia_semana= [

    {"NOMEUP": "Minas Gerais", "ANO": 2023, "MORTES":23},
    {"NOMEUP": "Minas Gerais", "ANO": 2024, "MORTES":23},
    
  
    {"NOMEUP": "Rio de Janeiro", "ANO": 2023, "MORTES":23},
    {"NOMEUP": "Rio de Janeiro", "ANO": 2024, "MORTES":23}
    ]



df = pd.DataFrame(dia_semana)


df_filtrado = df[
    (df["NOMEUP"].isin(["Minas Gerais", "Rio de Janeiro"])) 
].copy()

df_tabela = df_filtrado[["NOMEUP", "ANO", "MORTES"]]


st.title("Acidentes de Trânsito 2023 - 2024")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])


if opcao == "Tabela":
    st.header("Tabela de Mortes")
    st.dataframe(dia_semana, df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos de Mortes — Minas e Rio")

    st.subheader("3. Gráfico de Barras")
    fig_barras = px.bar(
        df_tabela,
        x="dia_semana",
        y="total_acidentes",
        color="NOMEUP",
        barmode="group",
        title="Comparativo de mortes",
        color_discrete_map={"Minas": "#FF6B6B", "Rio": "#00F5D4"},
        template="plotly_dark"
    )
    fig_barras.update_xaxes(type="category")
    fig_barras.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_barras, use_container_width=True)

    


st.markdown("---")
st.caption("Fonte dos dados: — https://basedosdados.org/")
    