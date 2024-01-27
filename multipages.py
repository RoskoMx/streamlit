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
    st.header('Gráficas utilizando Pandas', divider='rainbow')
    image = Image.open('rosko_xolo.png')
    st.image(image, caption='Primer página de proyectos 2024')
    
    image = Image.open('Streamlit8.png')
    st.image(image, caption='Guía del programa')
    
def page1():
    st.markdown("# Proyectos de Práctica")
    st.sidebar.markdown("# 1987")
    image01 = Image.open('rosko.jpg')
    st.image(image01, caption='Vamos a poner cualqier cosa')

    with st.container():
      st.subheader("Hola bienvenido a mi sitio web dentro de una función :wave:")
      st.title("Información random de contacto")
      st.write("Bienvenido a mi canal. Mi canal de Youtube está destinado a compartir música que aparece en películas y series del mundo.")
      st.write("[Mas informacion >](https://www.youtube.com/channel/UCAd74yI_c0q9b7UA1KLBqMA")

    with st.container():
      st.write("---") #Separa la primer sección de la segunda
      left_column, right_column = st.columns(2)
      with left_column:
        st.header("Mi objetivo")
        st.write(
          """
            Como esto es un texto más grande vamos a escribir entre comillas triples
            con saltos de línea y todo lo va a tomar como un string
            Veremos si lo centra o lo pone desrodenado.
          """
        )
        st.write("[Youtube >](https://www.youtube.com/watch?v=_vnF1nYcUys)")
      
      with right_column:
          st.write("DesBiiiienvenido a mi canal. Mi canal de Youtube está destinado a compartir música que aparece en películas y series del mundo.")
      

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


def page4():
    #Encabezado, tratar de evitar el header en subpáginas.
    #st.header('Gráficas utilizando Pandas', divider='rainbow')
    st.title("Resultados del Grand Prix de Países Bajos")
    
    #Imagen tal cuál está nombrada en el repositorio
    image = Image.open('Verstappen-pole-lap-Zandvoort-Netherlands-2021.jpg')
    st.image(image, caption='Max Verstappen')
    #Descripción de la imagen
    
    #Usuario
    st.text_input("¿Cuál es tu nombre?", key="name")
    st.session_state.name
    
    #Como un print y no es necesario escribir st.text
    st.text('¡Hola '+st.session_state.name+' !') 
    'Hola cómo estás? ',st.session_state.name
    
    #Generamos el Dataframe como si estuvieramos en Pandas
    df = pd.read_csv('https://raw.githubusercontent.com/LilianaC/streamlit3/main/Datos%20F1%20Dutch%20GP%20-%20Sheet1.csv')
    #Estos Dataframes se copian y pegan con la opción de raw, se pega la dirección de arriba del navegador
    #Sí el checkbox es verdadero y solo escribimos df
    if st.checkbox('Mostrar dataframe'):
        df
    
    #Lista desplegable
    option = st.selectbox(
        'Selecciona tu corredor favorito: ',
        #De dónde va a sacar la información
         df['DRIVER'])
    
    'Tu selección: ', option
    
    #Línea que muestra toda la info del renglón
    df.loc[df['DRIVER'] == option]
    
    #Gráfica
    st.line_chart(
        df,
        x = 'AVG SPEED',
        y = 'LAP'
    )



#Definimos los nombres de las páginas para llamarlas
page_names_to_funcs = {
    "Home": Home,
    "Proyectos": page1,
    "Datos FIFA ⚽": page2,
    "Deltas 🚥": page3,
    "Formula1": page4,
}
#Aquí trabaja como un diccionario y manda a llamar a la parte de las keys
selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]() #Manda a llamar la función seleccionada


