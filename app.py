import streamlit as st
import pandas as pd

# 🔥 CONFIGURAÇÃO DA PÁGINA (tem que ser a primeira coisa no código)
st.set_page_config(page_title="Busca de Dados 📊", page_icon="🔍", layout="wide")

# Simulando permissões de usuários
usuarios_admin = ["admin1", "admin2"]  # Quem pode editar
usuario_atual = st.sidebar.text_input("Digite seu usuário:")

# Carregar dados das planilhas
@st.cache_data
def carregar_dados():
    df1 = pd.read_excel("planilha1.xlsx")
    df2 = pd.read_excel("planilha2.xlsx")
    df = pd.concat([df1, df2])  # Junta as planilhas
    return df

df = carregar_dados()

# Barra lateral de filtros
st.sidebar.header("🔍 Filtros")
coluna_filtro = st.sidebar.selectbox("Escolha uma coluna para filtrar:", df.columns)
valor_filtro = st.sidebar.text_input("Digite o valor para buscar:")

# Aplicar filtro
if valor_filtro:
    df_filtrado = df[df[coluna_filtro].astype(str).str.contains(valor_filtro, case=False)]
else:
    df_filtrado = df

# Exibir resultados
st.write("### 📊 Resultados da Busca")
st.dataframe(df_filtrado)

# Opção de edição (apenas para admins)
if usuario_atual in usuarios_admin:
    st.write("📝 Modo de Edição Ativado")
    edit_df = st.data_editor(df_filtrado)
    if st.button("Salvar Alterações"):
        edit_df.to_excel("planilha_editada.xlsx", index=False)
        st.success("Alterações salvas com sucesso! ✅")
else:
    st.warning("Você só pode visualizar os dados. Entre como admin para editar.")
