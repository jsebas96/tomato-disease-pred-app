import streamlit as st
from views.about_app import about_app
from views.camera import take_picture
from views.load_image import load_image


def sidebar():
    menu = ["Sobre la app", "Cargar Imagen", "Cámara"]
    st.sidebar.write(
        """<div style="color:#23688f"><h3>Bienvenido</h3></div>""",
        unsafe_allow_html=True,
    )
    choice = st.sidebar.selectbox("Selecciona una opción", menu)

    if choice == menu[1]:
        load_image()
    elif choice == menu[2]:
        take_picture()
    else:
        about_app()
