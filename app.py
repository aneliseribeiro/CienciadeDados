import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Dashboard Atendimento", layout="wide")

# Função para carregar dados com encoding e separador corretos
@st.cache_data
def carregar_dados():
    df = pd.read_csv("atendimentos.csv", sep=';', encoding='latin-1')
    # Normalizar nomes das colunas
    df.columns = [col.strip() for col in df.columns]
    return df

df = carregar_dados()

# Título da página
st.title("📊 Dashboard de Atendimento Médico")

# Cálculo de métricas
media_idade = df["Idade"].mean()
total_atestados = df[df["Atestado"] == 1].shape[0]
total_respiratorio = df[df["Síndrome_Respiratória"] == 1].shape[0]

# Layout de cards de métricas
col1, col2, col3 = st.columns(3)
col1.metric("📈 Média de Idade", f"{media_idade:.1f} anos")
col2.metric("📄 Atestados Emitidos", total_atestados)
col3.metric("💨 Casos Respiratórios", total_respiratorio)

st.divider()

# Grade de gráficos 2x2 compacta
linha1_col1, linha1_col2 = st.columns(2)
linha2_col1, linha2_col2 = st.columns(2)

with linha1_col1:
    st.subheader("Atendimentos por Médico")
    fig1, ax1 = plt.subplots(figsize=(4, 2.8))
    sns.countplot(data=df, x="Médico", ax=ax1, palette="coolwarm")
    ax1.set_xlabel("")
    ax1.set_ylabel("Qtd")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

with linha1_col2:
    st.subheader("Atendimentos por Turno")
    fig2, ax2 = plt.subplots(figsize=(4, 2.8))
    sns.countplot(data=df, x="Turno", order=df["Turno"].value_counts().index, ax=ax2, palette="viridis")
    ax2.set_xlabel("")
    ax2.set_ylabel("Qtd")
    plt.xticks(rotation=0)
    st.pyplot(fig2)

with linha2_col1:
    st.subheader("Casos Respiratórios por Idade")
    respiratorio_df = df[df["Síndrome_Respiratória"] == 1]
    fig3, ax3 = plt.subplots(figsize=(4, 2.8))
    sns.histplot(respiratorio_df["Idade"], bins=10, kde=True, color="purple", ax=ax3)
    ax3.set_xlabel("Idade")
    ax3.set_ylabel("Casos")
    st.pyplot(fig3)

with linha2_col2:
    st.subheader("Distribuição por Gênero")
    fig4, ax4 = plt.subplots(figsize=(4, 2.8))
    sns.countplot(data=df, x="Gênero", ax=ax4, palette="pastel")
    ax4.set_xlabel("")
    ax4.set_ylabel("Qtd")
    st.pyplot(fig4)

st.divider()

# Botão para exportar CSV
st.subheader("📥 Exportar Dados")
csv = df.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')
st.download_button(
    label="📥 Baixar CSV",
    data=csv,
    file_name='atendimentos_export.csv',
    mime='text/csv',
)
