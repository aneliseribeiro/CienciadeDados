import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Atendimento", layout="wide")

@st.cache_data
def carregar_dados():
    return pd.read_csv("atendimentos.csv", sep=';', encoding='latin-1')

df = carregar_dados()

# Mostrar colunas para debug (pode remover depois)
st.write("Colunas do DataFrame:", df.columns.tolist())

st.title("📊 Dashboard de Atendimento Médico")

# Calcular métricas
media_idade = df["Idade"].mean()
total_atestados = df[df["Atestado"] == 1].shape[0]

# Layout com métricas no topo em 2 colunas
col_metric1, col_metric2 = st.columns(2)
col_metric1.metric("Média de Idade", f"{media_idade:.1f} anos")
col_metric2.metric("Atestados Emitidos", total_atestados)

st.divider()

# Criar grade 2x2 para gráficos pequenos
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

with row1_col1:
    st.subheader("Atendimentos por Médico")
    fig1, ax1 = plt.subplots(figsize=(4,3))
    sns.countplot(data=df, x="Médico", ax=ax1, palette="coolwarm")
    ax1.set_xlabel("Médico")
    ax1.set_ylabel("Atendimentos")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

with row1_col2:
    st.subheader("Atendimentos por Turno")
    if "Turno" in df.columns:
        ordem_turno = df["Turno"].value_counts().index
        fig2, ax2 = plt.subplots(figsize=(4,3))
        sns.countplot(data=df, x="Turno", order=ordem_turno, ax=ax2, palette="viridis")
        ax2.set_xlabel("Turno")
        ax2.set_ylabel("Atendimentos")
        st.pyplot(fig2)
    else:
        st.warning("Coluna 'Turno' não encontrada no arquivo CSV.")

with row2_col1:
    st.subheader("Casos de Síndromes Respiratórias por Idade")
    if "Síndrome Respiratória" in df.columns:
        respiratorio_df = df[df["Síndrome Respiratória"] == 1]
        fig3, ax3 = plt.subplots(figsize=(4,3))
        sns.histplot(respiratorio_df["Idade"], bins=10, kde=True, color="purple", ax=ax3)
        ax3.set_xlabel("Idade")
        ax3.set_ylabel("Casos")
        st.pyplot(fig3)
    else:
        st.warning("Coluna 'Síndrome Respiratória' não encontrada no arquivo CSV.")

with row2_col2:
    st.subheader("Distribuição de Gênero")
    if "Genero" in df.columns:
        fig4, ax4 = plt.subplots(figsize=(4,3))
        sns.countplot(data=df, x="Genero", ax=ax4, palette="pastel")
        ax4.set_xlabel("Gênero")
        ax4.set_ylabel("Quantidade")
        st.pyplot(fig4)
    else:
        st.warning("Coluna 'Genero' não encontrada no arquivo CSV.")

st.divider()

# Botão para exportar CSV
st.subheader("Exportar Dados")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Baixar CSV",
    data=csv,
    file_name='atendimentos_export.csv',
    mime='text/csv',
)
