import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson
import numpy as np

# Configuração da página
st.set_page_config(page_title="Painel de Atendimento Médico", layout="wide")

# Função para carregar os dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("atendimentos.csv", sep=';', encoding='latin-1')
    df.columns = df.columns.str.strip()
    return df

# Carregar os dados
df = carregar_dados()

# CSS personalizado para estilizar os cards
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-title {
        font-size: 16px;
        color: #6c757d;
        margin-bottom: 10px;
        font-weight: 600;
    }
    .metric-value {
        font-size: 28px;
        color: #212529;
        font-weight: 700;
    }
    .graph-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .graph-title {
        font-size: 16px;
        color: #212529;
        margin-bottom: 15px;
        font-weight: 600;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.title("Painel de Atendimento Médico")

# Seção de métricas (cards)
st.markdown("### Resumo dos Atendimentos")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">NOVOS ATENDIMENTOS</div>
        <div class="metric-value">{}</div>
    </div>
    """.format(df.shape[0]), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">PROCESSOS TOTAIS</div>
        <div class="metric-value">{}</div>
    </div>
    """.format(df.shape[0]), unsafe_allow_html=True)

with col3:
    taxa_sucesso = df[df["Atestado"] == 1].shape[0] / df.shape[0] * 100
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">TAXA DE SUCESSO</div>
        <div class="metric-value">{:.0f}%</div>
    </div>
    """.format(taxa_sucesso), unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">RECEITA (MILHÕES)</div>
        <div class="metric-value">R$7,2</div>
    </div>
    """, unsafe_allow_html=True)

# Primeira linha de gráficos
st.markdown("<br>", unsafe_allow_html=True)
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<div class="graph-title">Atendimentos por Médico</div>', unsafe_allow_html=True)
    fig1, ax1 = plt.subplots(figsize=(5, 3))
    sns.countplot(data=df, x="Medico", ax=ax1, palette="coolwarm")
    ax1.set_xlabel("")
    ax1.set_ylabel("Qtd")
    plt.xticks(rotation=45)
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

with col_graf2:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<div class="graph-title">Atendimentos por Turno</div>', unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    sns.countplot(data=df, x="Turno", order=df["Turno"].value_counts().index, ax=ax2, palette="viridis")
    ax2.set_xlabel("")
    ax2.set_ylabel("Qtd")
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

# Segunda linha de gráficos
col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<div class="graph-title">Casos Respiratórios por Idade</div>', unsafe_allow_html=True)
    respiratorio_df = df[df["SindRespiratoria"] == 1]
    fig3, ax3 = plt.subplots(figsize=(5, 3))
    sns.histplot(respiratorio_df["Idade"], bins=10, kde=True, color="purple", ax=ax3)
    ax3.set_xlabel("Idade")
    ax3.set_ylabel("Casos")
    st.pyplot(fig3)
    st.markdown('</div>', unsafe_allow_html=True)

with col_graf4:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<div class="graph-title">Distribuição por Gênero</div>', unsafe_allow_html=True)
    fig4, ax4 = plt.subplots(figsize=(5, 3))
    sns.countplot(data=df, x="Genero", ax=ax4, palette="pastel")
    ax4.set_xlabel("")
    ax4.set_ylabel("Qtd")
    st.pyplot(fig4)
    st.markdown('</div>', unsafe_allow_html=True)

# Terceira linha de gráficos (adicionei para ficar mais parecido com a imagem)
col_graf5, col_graf6 = st.columns(2)

with col_graf5:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<div class="graph-title">Conseguida 3</div>', unsafe_allow_html=True)
    # Gráfico de exemplo - você pode substituir por um gráfico real
    fig5, ax5 = plt.subplots(figsize=(5, 3))
    ax5.bar(['Sobre 1', 'Sobre 2', 'Sobre 3', 'Sobre 4'], [10, 15, 7, 12], color='skyblue')
    st.pyplot(fig5)
    st.markdown('</div>', unsafe_allow_html=True)

with col_graf6:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<div class="graph-title">Conseguida 4</div>', unsafe_allow_html=True)
    # Gráfico de exemplo - você pode substituir por um gráfico real
    fig6, ax6 = plt.subplots(figsize=(5, 3))
    ax6.bar(['Sobre 1', 'Sobre 2', 'Sobre 3', 'Sobre 4'], [8, 12, 9, 11], color='lightgreen')
    st.pyplot(fig6)
    st.markdown('</div>', unsafe_allow_html=True)

# Seção de exportação de dados
st.markdown("""
<div class="graph-container">
    <div class="graph-title">Exportar Dados</div>
""", unsafe_allow_html=True)
csv = df.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')
st.download_button(
    label="Baixar CSV",
    data=csv,
    file_name='atendimentos_export.csv',
    mime='text/csv',
)
st.markdown('</div>', unsafe_allow_html=True)

# Seção de análises estatísticas
st.markdown("""
<div class="graph-container">
    <div class="graph-title">Análises Estatísticas (Distribuições)</div>
""", unsafe_allow_html=True)

# BINOMIAL - probabilidade de atestados
st.markdown("### Probabilidade de Atestados (Distribuição Binomial)")
p_atestado = df["Atestado"].mean()

col_a, col_b = st.columns(2)
with col_a:
    n = st.slider("Número de pacientes simulados", min_value=5, max_value=50, value=10, step=1)
with col_b:
    k = st.slider("Número de atestados desejados (ou mais)", min_value=1, max_value=50, value=5, step=1)

if k > n:
    st.error("O número de atestados desejados não pode ser maior que o número de pacientes.")
else:
    prob_5oumais = 1 - binom.cdf(k - 1, n, p_atestado)
    st.write(f"Com base em uma taxa observada de {p_atestado:.1%} de emissão de atestados,")
    st.write(f"a probabilidade de pelo menos {k} atestados em {n} pacientes é **{prob_5oumais:.2%}**.")

    # Gráfico da distribuição binomial
    probs_binom = [binom.pmf(i, n, p_atestado) for i in range(n+1)]
    fig_b, ax_b = plt.subplots(figsize=(5, 3))
    bars = ax_b.bar(range(n+1), probs_binom, color=["gray" if i < k else "orange" for i in range(n+1)])
    ax_b.set_xlabel("Número de Atestados")
    ax_b.set_ylabel("Probabilidade")
    ax_b.set_title("Distribuição Binomial")
    st.pyplot(fig_b)

# POISSON - probabilidade de casos respiratórios
st.markdown("### Casos Respiratórios por Turno (Distribuição de Poisson)")
casos_por_turno = df.groupby("Turno")["SindRespiratoria"].sum().mean()

k_poisson = st.slider("Número de casos respiratórios desejados (ou mais)", min_value=0, max_value=10, value=3, step=1)
prob_3oumais = 1 - poisson.cdf(k_poisson - 1, casos_por_turno)

st.write(f"A média de casos respiratórios por turno é **{casos_por_turno:.2f}**.")
st.write(f"A probabilidade de pelo menos {k_poisson} casos em um turno é **{prob_3oumais:.2%}**.")

# Gráfico da distribuição de Poisson
max_k = 10
probs_poisson = [poisson.pmf(i, casos_por_turno) for i in range(max_k+1)]
fig_p, ax_p = plt.subplots(figsize=(5, 3))
bars_p = ax_p.bar(range(max_k+1), probs_poisson, color=["gray" if i < k_poisson else "orange" for i in range(max_k+1)])
ax_p.set_xlabel("Número de Casos")
ax_p.set_ylabel("Probabilidade")
ax_p.set_title("Distribuição de Poisson")
st.pyplot(fig_p)

st.markdown('</div>', unsafe_allow_html=True)