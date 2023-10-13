# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pandas as pd

st.sidebar.image("logoCCTSF2-1.png",caption="Saludos desde México 🇲🇽")


url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/Fifa%2023%20Fut%20Players.csv'
df= pd.read_csv(url)

rankings = df['Ratings'].max()
pais = df['Country'].mode()[0]


def Home():
    st.markdown("# Home 🎈")
    st.sidebar.markdown("# Home 🎈")

def page2():
    st.markdown("# Datos FIFA ⚽")
    st.sidebar.markdown("# Datos FIFA ⚽")
    
    total1,total2=st.columns(2,gap='large')
    
    with total1:
        st.info('Ranking más alto',icon="📌")
        st.metric(label="Ranking",value=f"{rankings:,.0f}")

    with total2:
        st.info('País con más jugadores',icon="📌")
        st.metric(label="País",value=f"{pais}")



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
