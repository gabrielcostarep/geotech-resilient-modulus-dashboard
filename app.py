import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="MR Dashboard", layout="wide")
st.title("Módulo Resiliente: Comparativo de Misturas")

@st.cache_data
def load_mr_data():
    df_macro = pd.read_parquet('mr_macro.parquet')
    df_micro = pd.read_parquet('mr_micro.parquet')
    
    # Criando a coluna que o gráfico está pedindo e convertendo para %
    df_macro['ea_max_pct'] = df_macro['ea_max'] * 100.0
    df_micro['ea_pct'] = df_micro['ea'] * 100.0
    
    return df_macro, df_micro

df_macro, df_micro = load_mr_data()

# --- FILTROS ---
st.sidebar.header("Configurações")
proc_selecionado = st.sidebar.selectbox("Escolha o Procedimento (Degrau de Carga):", 
                                        options=sorted(df_macro['Procedimento'].unique()))

df_filtrado = df_macro[df_macro['Procedimento'] == proc_selecionado]

# --- DASHBOARD ---
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Energia Dissipada (e_diss) - Proc {proc_selecionado}")
    fig_ediss = px.line(df_filtrado, x='Ciclo', y='Energia_Dissipada', color='Mistura',
                        labels={'Energia_Dissipada': 'Energia (J/m³)'})
    st.plotly_chart(fig_ediss, use_container_width=True)

with col2:
    st.subheader(f"Energia Acumulada (case) - Proc {proc_selecionado}")
    # Este é o gráfico que o professor Rubens usava para ver o dano acumulado
    fig_case = px.line(df_filtrado, x='Ciclo', y='case', color='Mistura',
                       labels={'case': 'CASE (Energia Acumulada)'})
    st.plotly_chart(fig_case, use_container_width=True)

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader("Deformação Permanente (%)")
    fig_ea = px.line(df_filtrado, x='Ciclo', y='ea_max_pct', color='Mistura')
    st.plotly_chart(fig_ea, use_container_width=True)

with col4:
    st.subheader(f"Laço de Histerese (Ciclo 50) - Proc {proc_selecionado}")
    df_laco_filtrado = df_micro[df_micro['Procedimento'] == proc_selecionado]
    fig_laco = px.line(df_laco_filtrado, x='ea_pct', y='q', color='Mistura')
    st.plotly_chart(fig_laco, use_container_width=True)