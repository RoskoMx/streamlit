# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pandas as pd
from PIL import Image

st.sidebar.image("logoCCTSF2-1.png",caption="Saludos desde México 🇲🇽")


url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/Fifa%2023%20Fut%20Players.csv'
df= pd.read_csv(url)

rankings = df['Ratings'].max()
pais = df['Country'].mode()[0]


def Home():
    st.markdown("# Home 🎈")
    st.sidebar.markdown("# Home 🎈")
    image = Image.open('internet-4463031_1280.jpg')
    st.image(image, caption='Estadísticas')
    


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



url2 = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/netflix_titles.csv'
df2 = pd.read_csv(url2)

paisp = df2['country'].mode()[0]
durat = df2['duration'].mode()[0]
year = df2['release_year'].mode()[0]
tipo = df2['type'].mode()[0]

def page3():
    st.markdown("# Netflix 🎞️")
    st.sidebar.markdown("# Netflix 🎞️")
    total3,total4,total5,total6 = st.columns(4,gap='large')
    
    with total3:
        st.info('País',icon="📌")
        st.metric(label="País con más producción",value=f"{paisp}")

    with total4:
        st.info('Duración',icon="📌")
        st.metric(label="Duración más repetida",value=f"{durat}")

    with total5:
        st.info('Año',icon="📌")
        st.metric(label="Año donde se produjo más",value=f"{year}")

    with total6:
        st.info('Tipo',icon="📌")
        st.metric(label="Tipo de producción",value=f"{tipo}")




page_names_to_funcs = {
    "Home": Home,
    "Datos FIFA ⚽": page2,
    "Netflix 🎞️": page3,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
