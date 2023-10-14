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




def page3():
    st.markdown("# Deltas 🚥")
    st.sidebar.markdown("# Deltas 🚥")
    
    col1, col2, col3 = st.columns(3,gap='large')
    
    with col1:
        st.info('Temperatura',icon="🌡️")
        st.metric("Cambio en la temperatura", "20 °C", "10 °C")

    with col2:
        st.info('Viento',icon="🍃")
        st.metric("Velocidad viento","9 kph", "-8%")

    with col3:
        st.info('Humedad',icon="💧")
        st.metric("Cantidad de humedad","86%", "4%")




page_names_to_funcs = {
    "Home": Home,
    "Datos FIFA ⚽": page2,
    "Netflix 🎞️": page3,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
