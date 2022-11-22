import streamlit as st
from PIL import Image
from utils.predict import predict


@st.cache
def upload_image(image_file):
    img = Image.open(image_file)
    return img


def load_image():
    col1, col2 = st.columns(2)
    col1.write(
        """<div style="color:#23688f;
                                margin-left:5%;">
                                <h3>Imagen</h3>
                    </div>""",
        unsafe_allow_html=True,
    )

    image_file = st.sidebar.file_uploader("", type=["jpg", "jpeg"])

    if image_file is not None:
        img = upload_image(image_file)
        col1.image(img, width=250)

        col2.write("""<div style="margin-top:25%;"> </div>""", unsafe_allow_html=True)
        if col2.button("Clasificar", key="1"):
            predicition = predict(img)
            col2.write(f"La afección se clasifica como {predicition}")