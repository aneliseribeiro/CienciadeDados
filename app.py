import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard Atendimento", layout="wide")

# Carregar os dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("atendimentos.csv")

df = carregar_dados()

st.title("📊 Dashboard de Atendimento Médico")

# Organizar layout com colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Média de Idade dos Pacientes")
    media_idade = df["Idade"].mean()
    st.metric(label="Média de Idade", value=f"{media_idade:.1f} anos")

with col2:
    st.subheader("Quantidade de Atestados Médicos")
    total_atestados = df[df["Atestado"] == "Sim"].shape[0]
    st.metric(label="Atestados Emitidos", value=total_atestados)

st.divider()

# Gráfico de atendimentos por médico
st.subheader("Fluxo de Atendimento por Médico")
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x="Medico", ax=ax1, palette="coolwarm")
plt.xlabel("Médico")
plt.ylabel("Quantidade de Atendimentos")
st.pyplot(fig1)

# Gráfico de períodos de pico
st.subheader("Período de Pico de Atendimentos")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x="Horario", order=df["Horario"].value_counts().index, ax=ax2, palette="viridis")
plt.xlabel("Horário")
plt.ylabel("Atendimentos")
st.pyplot(fig2)

# Gráfico de Síndromes Respiratórias
st.subheader("Casos de Síndromes Respiratórias")
respiratorio_df = df[df["Diagnostico"] == "Síndrome Respiratória"]
fig3, ax3 = plt.subplots()
sns.histplot(respiratorio_df["Idade"], bins=10, kde=True, color="purple", ax=ax3)
plt.xlabel("Idade")
plt.ylabel("Quantidade de Casos")
st.pyplot(fig3)

# Exportação CSV
st.divider()
st.subheader("Exportar Dados Filtrados")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Baixar CSV",
    data=csv,
    file_name='atendimentos_export.csv',
    mime='text/csv',
)

