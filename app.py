import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Painel de Atendimento Médico", layout="wide")

# Função para carregar os dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("atendimentos.csv", sep=';', encoding='latin-1')
    df.columns = df.columns.str.strip()  # remove espaços extras nos nomes das colunas
    return df

# Carregar os dados
df = carregar_dados()

# Título
st.title("📊 Painel de Atendimento Médico")

# Cards de métricas
media_idade = df["Idade"].mean()
total_atestados = df[df["Atestado"] == 1].shape[0]
total_respiratorio = df[df["SindRespiratoria"] == 1].shape[0]

st.markdown("### 📊 Resumo dos Atendimentos")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📈 Média de Idade", f"{media_idade:.1f} anos")
with col2:
    st.metric("📄 Atestados Emitidos", total_atestados)
with col3:
    st.metric("💨 Casos Respiratórios", total_respiratorio)

st.divider()

# Linha de gráficos
with st.container():
    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        st.markdown("#### 📑 Atendimentos por Médico")
        if df["Medico"].nunique() > 0:
            fig1, ax1 = plt.subplots(figsize=(3.5, 2.5))
            sns.countplot(data=df, x="Medico", ax=ax1, palette="coolwarm")
            ax1.set_xlabel("")
            ax1.set_ylabel("Qtd")
            plt.xticks(rotation=45)
            st.pyplot(fig1)
        else:
            st.warning("Nenhum dado disponível para Médicos.")

    with col_graf2:
        st.markdown("#### 🕑 Atendimentos por Turno")
        if df["Turno"].nunique() > 0:
            fig2, ax2 = plt.subplots(figsize=(3.5, 2.5))
            sns.countplot(data=df, x="Turno", order=df["Turno"].value_counts().index, ax=ax2, palette="viridis")
            ax2.set_xlabel("")
            ax2.set_ylabel("Qtd")
            st.pyplot(fig2)
        else:
            st.warning("Nenhum dado disponível para Turnos.")

# Segunda linha de gráficos
with st.container():
    col_graf3, col_graf4 = st.columns(2)

    with col_graf3:
        st.markdown("#### 💨 Casos Respiratórios por Idade")
        respiratorio_df = df[df["SindRespiratoria"] == 1]
        if not respiratorio_df.empty:
            fig3, ax3 = plt.subplots(figsize=(3.5, 2.5))
            sns.histplot(respiratorio_df["Idade"], bins=10, kde=True, color="purple", ax=ax3)
            ax3.set_xlabel("Idade")
            ax3.set_ylabel("Casos")
            st.pyplot(fig3)
        else:
            st.warning("Nenhum caso respiratório registrado.")

    with col_graf4:
        st.markdown("#### 👥 Distribuição por Gênero")
        if df["Genero"].nunique() > 0:
            fig4, ax4 = plt.subplots(figsize=(3.5, 2.5))
            sns.countplot(data=df, x="Genero", ax=ax4, palette="pastel")
            ax4.set_xlabel("")
            ax4.set_ylabel("Qtd")
            st.pyplot(fig4)
        else:
            st.warning("Nenhum dado disponível para Gênero.")

st.divider()

# Exportar CSV
st.markdown("### 📥 Exportar Dados")
csv = df.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')
st.download_button(
    label="📥 Baixar CSV",
    data=csv,
    file_name='atendimentos_export.csv',
    mime='text/csv',
)
