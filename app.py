import streamlit as st

st.set_page_config(
    page_title="MIM Template",
    page_icon="🧩",
    layout="centered"
)

st.title("🧩 MIM Template")
st.write("Transforme um problema em um protótipo funcional.")

problema = st.text_input(
    "Qual problema você quer resolver?"
)

st.button("Criar Protótipo")
