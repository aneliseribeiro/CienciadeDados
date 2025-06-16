import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações da página
st.set_page_config(page_title="Dashboard Pronto Atendimento", layout="wide")

st.title("Dashboard - Pronto Atendimento Emergência")

# Upload do CSV
uploaded_file = st.file_uploader("Carregue a planilha de atendimentos (dados.csv)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Exibir dataframe
    st.subheader("Visualização dos Dados")
    st.dataframe(df)

    # Média de Idade
    st.subheader("Média de Idade dos Pacientes")
    st.write(f"Média de idade: **{df['Idade'].mean():.1f} anos**")

    # Fluxo por médico
    st.subheader("Atendimentos por Médico")
    medico_counts = df['Médico'].value_counts()
    fig1, ax1 = plt.subplots()
    sns.barplot(x=medico_counts.index, y=medico_counts.values, palette="crest", ax=ax1)
    ax1.set_xlabel("Médico")
    ax1.set_ylabel("Número de Atendimentos")
    st.pyplot(fig1)

    # Horários de pico
    st.subheader("📊 Atendimentos por Horário")
    df['Hora'] = pd.to_datetime(df['Hora'], format='%H:%M')
    df['Hora_decimal'] = df['Hora'].dt.hour + df['Hora'].dt.minute / 60
    fig2, ax2 = plt.subplots()
    sns.histplot(df['Hora_decimal'], bins=24, kde=False, color="royalblue", ax=ax2)
    ax2.set_xlabel("Hora do dia")
    ax2.set_ylabel("Número de Atendimentos")
    st.pyplot(fig2)

    # Síndromes Respiratórias
    st.subheader("Casos de Síndromes Respiratórias")
    sindrome_counts = df['Síndrome_Respiratória'].value_counts()
    fig3, ax3 = plt.subplots()
    sns.barplot(x=sindrome_counts.index, y=sindrome_counts.values, palette="light:#5A9", ax=ax3)
    ax3.set_xlabel("Possui Síndrome Respiratória")
    ax3.set_ylabel("Quantidade")
    st.pyplot(fig3)

    # Atestados emitidos
    st.subheader("Atestados Médicos Emitidos")
    atestado_counts = df['Atestado'].value_counts()
    fig4, ax4 = plt.subplots()
    sns.barplot(x=atestado_counts.index, y=atestado_counts.values, palette="flare", ax=ax4)
    ax4.set_xlabel("Atestado Emitido")
    ax4.set_ylabel("Quantidade")
    st.pyplot(fig4)

else:
    st.info("Faça upload de um arquivo CSV para começar.")
    
# Rodapé
st.markdown("---")
st.markdown("Criado por: **Anelise Dias** | Ciência de Dados 2024")
