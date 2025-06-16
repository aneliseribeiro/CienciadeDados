import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Painel de Pronto Atendimento", layout="wide")

st.title("Painel de Dados - Pronto Atendimento Médico")

@st.cache_data
def carregar_dados():
    return pd.read_csv("atendimentos.csv")

try:
    dados = carregar_dados()

    st.subheader("Dados Carregados")
    st.dataframe(dados)

    st.subheader("Média de Idade dos Pacientes")
    media_idade = dados["Idade"].mean()
    st.write(f"Média de idade: {media_idade:.1f} anos")

    fig, ax = plt.subplots()
    sns.histplot(dados["Idade"], bins=10, kde=True, ax=ax)
    ax.set_xlabel("Idade")
    ax.set_ylabel("Número de Pacientes")
    ax.set_title("Distribuição das Idades dos Pacientes")
    st.pyplot(fig)

    st.subheader("Atendimentos por Médico")
    fig2, ax2 = plt.subplots()
    sns.countplot(y="Médico", data=dados, order=dados["Médico"].value_counts().index, ax=ax2)
    ax2.set_xlabel("Número de Atendimentos")
    ax2.set_ylabel("Médico")
    st.pyplot(fig2)

    st.subheader("Atendimentos por Hora")
    dados["Hora"] = pd.to_datetime(dados["Hora"], format="%H:%M").dt.hour
    fig3, ax3 = plt.subplots()
    sns.histplot(dados["Hora"], bins=range(0, 25), ax=ax3)
    ax3.set_xlabel("Hora do Atendimento")
    ax3.set_ylabel("Número de Atendimentos")
    st.pyplot(fig3)

    st.subheader("Casos de Síndromes Respiratórias")
    fig4, ax4 = plt.subplots()
    sns.countplot(x="Síndrome_Respiratória", data=dados, ax=ax4)
    ax4.set_xlabel("Síndrome Respiratória")
    ax4.set_ylabel("Quantidade")
    st.pyplot(fig4)

    st.subheader("Atestados Médicos Emitidos")
    fig5, ax5 = plt.subplots()
    sns.countplot(x="Atestado", data=dados, ax=ax5)
    ax5.set_xlabel("Atestado Médico")
    ax5.set_ylabel("Quantidade")
    st.pyplot(fig5)

except Exception as e:
    st.error(f"Ocorreu um erro ao carregar ou processar os dados: {e}")
