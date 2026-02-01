import streamlit as st
import openai

openai.api_key = "API_KEY"

st.title("Describí Fácil IA")
st.write("Generador de descripciones de productos con IA")

producto = st.text_input("Nombre del producto")
caracteristicas = st.text_area("Características")
estilo = st.selectbox("Estilo", ["Profesional", "Creativo", "Breve"])

if st.button("Generar descripción"):
    prompt = f"""
    Creá una descripción {estilo} para el siguiente producto:
    Producto: {producto}
    Características: {caracteristicas}
    """

    

    st.subheader("Descripción generada:")
st.write(
    "Esta es una descripción de ejemplo generada por la IA. "
    "El producto se destaca por su calidad, diseño y funcionalidad, "
    "ideal para el público objetivo seleccionado."
)

