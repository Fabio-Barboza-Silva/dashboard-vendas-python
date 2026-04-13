import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da página
st.set_page_config(page_title="Dashboard do Fabio", layout="wide")

st.title("📊 Meu Primeiro Dashboard em Python")
st.markdown("Criado para demonstrar interatividade sem Power BI pago.")

# 2. Criando dados fictícios (Você poderia ler de um SQL ou Excel aqui)
dados = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
    'Vendas': [16000, 18000, 12000, 25000, 30000],
    'Meta': [10000, 10000, 10000, 10000, 10000]
}
df = pd.DataFrame(dados)

# 3. Barra Lateral (Filtros)
st.sidebar.header("Filtros do Projeto")
mes_selecionado = st.sidebar.multiselect("Selecione os meses:", df['Mês'].unique(), default=df['Mês'].unique())

# Filtrando os dados com base na escolha do usuário
df_filtrado = df[df['Mês'].isin(mes_selecionado)]

# 4. Exibindo métricas no topo
col1, col2 = st.columns(2)
col1.metric("Total de Vendas", f"R$ {df_filtrado['Vendas'].sum():,.2f}")
col2.metric("Meta Alcançada", "Sim" if df_filtrado['Vendas'].sum() > 50000 else "Não")

# 5. Gráfico Interativo (Usando Plotly)
fig = px.bar(df_filtrado, x='Mês', y='Vendas', title="Performance de Vendas Mensal")
st.plotly_chart(fig, use_container_width=True)

# 6. Tabela de dados (Opcional)
if st.checkbox("Mostrar tabela de dados brutos"):
    st.write(df_filtrado)