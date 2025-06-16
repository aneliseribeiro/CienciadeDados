import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Painel de Pronto Atendimento", layout="wide")

# Estilo de título
st.title("🏥 Painel de Dados - Pronto Atendimento Médico")

# Leitura do CSV direto do arquivo
@st.cache_data
def carregar_dados():
    return pd.read_csv("atendimentos.csv")

# Botão para atualizar dados
if st.button("🔄 Recarregar dados"):
    dados = carregar_dados()
else:
    dados = carregar_dados()

# Exibe tabela de dados
st.subheader("📄 Dados Carregados")
st.dataframe(dados)

# Gráfico: Média de idade
st.subheader("📊 Média de Idade dos Pacientes")
media_idade = dados["Idade"].mean()
st.write(f"📌 Média de idade: **{media_idade:.1f} anos**")

# Histograma de idades
fig, ax = plt.subplots()
sns.histplot(dados["Idade"], bins=10, kde=True, color='skyblue', ax=ax)
ax.set_xlabel("Idade")
ax.set_ylabel("Quantidade de Pacientes")
st.pyplot(fig)

# Gráfico: Médico que mais atendeu
st.subheader("📊 Quantidade de Atendimentos por Médico")
fig2, ax2 = plt.subplots()
sns.countplot(y="Médico", data=dados, order=dados["Médico"].value_counts().index, palette="viridis", ax=ax2)
st.pyplot(fig2)

# Gráfico: Horário de pico de atendimento
st.subheader("📊 Distribuição de Atendimentos por Hora")
dados["Hora"] = pd.to_datetime(dados["Hora"], format="%H:%M").dt.hour
fig3, ax3 = plt.subplots()
sns.histplot(dados["Hora"], bins=range(0, 25), color="coral", ax=ax3)
ax3.set_xlabel("Hora do Dia")
ax3.set_ylabel("Quantidade de Atendimentos")
st.pyplot(fig3)

# Gráfico: Casos de Síndromes Respiratórias
st.subheader("📊 Casos de Síndromes Respiratórias")
fig4, ax4 = plt.subplots()
sns.countplot(x="Síndrome_Respiratória", data=dados, palette="pastel", ax=ax4)
st.pyplot(fig4)

# Gráfico: Atestados médicos emitidos
st.subheader("📊 Atestados Médicos Emitidos")
fig5, ax5 = plt.subplots()
sns.countplot(x="Atestado", data=dados, palette="Set2", ax=ax5)
st.pyplot(fig5)

# Download dos dados
st.subheader("📥 Exportar dados atualizados")
csv = dados.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Baixar CSV dos Dados",
    data=csv,
    file_name="atendimentos_exportado.csv",
    mime="text/csv",
)
