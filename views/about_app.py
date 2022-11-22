import streamlit as st


def about_app():
    message = """
        Bienvenido\n 
        Esta es una aplicación que te permitirá realizar la clasificación de afecciones en cultivos de tomate.
        Puedes cargar una imagen o utilizar la cámara de tu dispositivo.
    """
    with st.container():
        st.write(message)
