import streamlit as st
import cv2
from utils.predict import predict


def take_picture():
    st.sidebar.write("")
    col1, col2 = st.columns(2)

    col1.write(
        """<div style="color:#23688f;
                                margin-left:5%;">
                                <h3>Cámara Activa</h3>
                    </div>""",
        unsafe_allow_html=True,
    )
    FRAME_WINDOW = col1.image([])
    camera = cv2.VideoCapture(0)  # 0 corresponde al índice de la cámara

    col2.write("""<div style="margin-top:25%;"> </div>""", unsafe_allow_html=True)
    capture = col2.button("Tomar Foto", key="2")
    picture = False
    col2.write("")
    frames = []

    while picture == False:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        FRAME_WINDOW.image(frame)

        if capture == True:
            picture = True
            image = cv2.resize(frame, (224, 224))
            data = image.reshape(1, 224, 224, 3)
            # col2.write("El número en la imagen corresponde a")
            camera.release()
