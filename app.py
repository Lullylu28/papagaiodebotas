import streamlit as st

st.title("🚀 Meu primeiro app no Streamlit!")
st.write("Capivara Tech™ dominando a tecnologia! 🦫🔥")

import streamlit as st

# Configurar a página
st.set_page_config(
    page_title="Meu App Incrível 🚀",
    page_icon="🔥",
    layout="wide"  # Pode ser "centered" ou "wide"
)

# Título e descrição
st.title("🚀 Meu primeiro app no Streamlit!")
st.write("Capivara Tech™ dominando a tecnologia! 🦫🔥")

# Adicionando um botão
if st.button("Clique aqui"):
    st.success("Você clicou no botão! 🎉")
