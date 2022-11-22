import streamlit as st
from components.sidebar import sidebar


def main():
    st.write(
        """<div style="text-align:center; 
                                background_color:#23688f;
                                color:white;
                                font-weight:50%;
                                font-family:"Gill Sans EXtrabold", Helvetica, sans-serif;"><h2>
        Clasificación de Afecciones en Cultivos de Tomate</h2></div>""",
        unsafe_allow_html=True,
    )
    sidebar()


if __name__ == "__main__":
    main()
