# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pandas as pd
from PIL import Image #Para importar imágenes

st.sidebar.image("rosko_hoja.png",caption ="Saludos desde Cannes, Francia 🇫🇷 ")

#Archivo de datos csv que está en este repositorio, se escribe la direción y después se hace el Data frame.
url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/Fifa%2023%20Fut%20Players.csv'
df= pd.read_csv(url)

rankings = df['Ratings'].max() #Mandamos a llamar el máximo Ranking
pais = df['Country'].mode()[0] #Método de Pandas, queremos saber qué país se repite más, con mode(0) (esto toma el primero)

#Página de Home
def Home():
    st.markdown("# Home Rosko 🎈")
    st.sidebar.markdown("# Home Jenkins 🎈")
    image = Image.open('rosko_xolo.png')
    st.image(image, caption='Estadísticas')
    
    image = Image.open('Streamlit8.png')
    st.image(image, caption='Guía del programa')
    
def page1():
    st.markdown("Proyectos de Práctica")

def page2():
    st.markdown("# Datos FIFA ⚽")
    st.sidebar.markdown("# Datos FIFA ⚽")

    image = Image.open('soccer-488700_1280.jpg')
    st.image(image, caption='Fútbol')
    
    #Definición de las columnas
    total1,total2=st.columns(2,gap='large') #Gap es el espacio entre columnas, puede ser omitido

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


    image = Image.open('cloud-4820504_1280.jpg')
    st.image(image, caption='Clima')



#Definimos los nombres de las páginas para llamarlas
page_names_to_funcs = {
    "Home": Home,
    "Proyectos": page1,
    "Datos FIFA ⚽": page2,
    "Deltas 🚥": page3,
}
#Aquí trabaja como un diccionario y manda a llamar a la parte de las keys
selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]() #Manda a llamar la función seleccionada
