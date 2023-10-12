# Contents of ~/my_app/streamlit_app.py
import streamlit as st

st.sidebar.image("logoCCTSF2-1.png",caption="Saludos desde México 🇲🇽")

def Home():
    st.markdown("# Home 🎈")
    st.sidebar.markdown("# Home 🎈")

def page2():
    st.markdown("# Página 2 ❄️")
    st.sidebar.markdown("# Página 2 ❄️")

def page3():
    st.markdown("# Página 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Home": Home,
    "Página 2": page2,
    "Página 3": page3,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
