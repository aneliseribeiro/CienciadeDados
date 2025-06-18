import pandas as pd

df = pd.read_csv("atendimentos.csv")
st.write(df.head())
st.write(df.columns)
