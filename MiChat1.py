import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv() 

st.set_page_config(page_title="Wave", layout="centered")
st.title("🌊 Wave")

# estuve 3 horas sin saber porque no me andaba y al final era esto
MODELOS = {
    "Wave Mini": "llama-3.1-8b-instant",
    "Wave Pro": "llama-3.1-70b-versatile",
    "Wave Ultra": "mixtral-8x7b-32768"
}

st.sidebar.title("Configuración")
modelo_seleccionado = st.sidebar.selectbox("Elegí un modelo de Groq", options=list(MODELOS.keys()))

modelo_real = MODELOS[modelo_seleccionado]

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ No se encontró la API Key. Creá un archivo .env con GROQ_API_KEY='tu_clave_aquí'")
else:
    client = Groq(api_key=api_key)

    mensaje = st.chat_input("Escribí tu mensaje:")

    if mensaje:
        st.chat_message("user").write(mensaje)

        respuesta = client.chat.completions.create(
            model=modelo_real,
            messages=[{"role": "user", "content": mensaje}]
        )

        texto_respuesta = respuesta.choices[0].message.content
        st.chat_message("assistant").write(texto_respuesta)

        print(f"Usuario: {mensaje}")
        print(f"IA: {texto_respuesta}")

