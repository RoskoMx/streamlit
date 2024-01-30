# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pandas as pd
from PIL import Image #Para importar imágenes
import plotly.express as px #Ultimas dos librerías para la app de FIFA
import plotly.graph_objs as go

st.sidebar.image("images/rosko_hoja.png",caption ="Saludos desde Cannes, Francia 🇫🇷 ")

#Archivo de datos csv que está en este repositorio, se escribe la direción y después se hace el Data frame.
#Estos dos párrafos son exclusivos de las página de FIFA
url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/Fifa%2023%20Fut%20Players.csv'
df= pd.read_csv(url) 

rankings = df['Ratings'].max() #Mandamos a llamar el máximo Ranking
pais = df['Country'].mode()[0] #Método de Pandas, queremos saber qué país se repite más, con mode(0) (esto toma el primero)

#Página de Home
def Home():
    st.markdown("# Home Rosko 🦃")
    st.sidebar.markdown("# Estás en la casa 🎈")
    image = Image.open('images/rosko_xolo.png')
    st.image(image, caption='Logo de Xolo creado con IA')
    
    #Esta parte del código hace refrencia al repositorio lottie de web_company de Tony
    #Se agregan al archivo requirements el 'streamlottie' y 'requirements'
    lottie_file ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"
    with st.container():
        st.write("---")
        left_column, right_column= st.columns((2))
        with left_column:
            st.header("Sobre nosotros")
            st.write(
                """
                Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
                Seguramente te vamos a poder ayudar si:

                - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
                - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
                - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
                - Quieres mejorar la experiencia de tus clientes
                - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

                ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
                """
            )
            st.write("[Más sobre nosotros>](https://debutants-sur-internet.streamlit.app/")
        with right_column:
            st_lottie(load_lottieurl(lottie_file), height=400)


    
def page1():
    st.markdown("# Proyectos de Práctica")
    st.sidebar.markdown("# 1987")
    image01 = Image.open('images/rosko.jpg')
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

    image = Image.open('images/soccer-488700_1280.jpg')
    st.image(image, caption='Fútbol')
    
    #Definición de las columnas
    total1,total2=st.columns(2,gap='large') #Gap es el espacio entre columnas, puede ser omitido

    with total1:
        st.info('Ranking más alto',icon="📌")
        st.metric(label="Ranking",value=f"{rankings:,.0f}")

    with total2:
        st.info('País con más jugadores',icon="📌")
        st.metric(label="País",value=f"{pais}")

    #requirements.txt revisar las versiones utilizadas en el momento de la app
    #Se Importan las librerías plotly además de st y pandas
    #Gráfica de barras
    #https://www.youtube.com/watch?v=Vmhk04R40F8&t=247s liga para el video de youtube cctmx
    st.title('Gráfica de un dataframe: Selección de datos por los usuarios')
    url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/Fifa%2023%20Fut%20Players.csv'
    #Al parecer no está el archivo en el minuto 14:30 del tutorial, dice que solo con Ploty lo jala
    df= pd.read_csv(url)
    
    st.title('Gráfica de barras')
    
    columns = df.columns.tolist() #Convertimos las columnas a listas
    selected_columns = st.multiselect("Selecciona la columna a graficar (var=st.multiselect)", columns, default="League")# Valor que creemos sería más frecuente
    s = df[selected_columns[0]].str.strip().value_counts() #Si los datos tienen espacios, los quita, me parece

    #Todo esto se necesita para crear el objeto, solo se describe lo más indispensable
    trace = go.Bar(x=s.index,y=s.values) #Gráfica de tipo barra, x=letras de los que se seleccione, y=valores
    layout = go.Layout(title = "FIFA 21")
    data = [trace]
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig) #La gráfica aparece ordenada porque usamos el value_counts
    
    #Gráfica de dispersión
    st.title('Gráfica de Dispersión')
    valx = st.multiselect("Selecciona País, Liga o Club", columns, default="Country")
    valy = st.multiselect("Selecciona la métrica", columns, default="Ratings")
    
    valoresx = df[valx[0]]#Aquí no se ocupan los value_counts, se manda directo
    valoresy = df[valy[0]]
    
    trace2 = px.scatter(df,x=valoresx.values,y=valoresy.values)
    st.plotly_chart(trace2, theme="streamlit", use_container_width=True)
    
    #Multiselección gráfica de barras
    st.title('Gráfica de Dispersión: para Ratings')
    clist = df["Country"].unique().tolist() #Lista de valores únicos
    
    countries = st.multiselect("Selecciona el país", clist) #
    st.header("Seleccionaste: {}".format(", ".join(countries))) #Lo que el usuario vea qué seleccionó, países
    
    dfs = {country: df[df["Country"] == country] for country in countries} #
    
    fig = go.Figure()
    for country, df in dfs.items(): #Agregamos a cada una de las líneas a la gráfuca que ya existe
      fig = fig.add_trace(go.Bar(x=df["Name"], y=df["Ratings"], name=country))
    
    st.plotly_chart(fig)




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

    
    image = Image.open('images/cloud-4820504_1280.jpg')
    st.image(image, caption='Clima')


def page4():
    #Encabezado, tratar de evitar el header en subpáginas.
    #st.header('Gráficas utilizando Pandas', divider='rainbow')
    st.title("Resultados del Grand Prix de Países Bajos (con st.title)")
    
    #Imagen tal cuál está nombrada en el repositorio
    image = Image.open('images/Verstappen-pole-lap-Zandvoort-Netherlands-2021.jpg')
    st.image(image, caption='La imagen de arriba sale igualando una variable a Image.open(ruta de acceso)')
    #Descripción de la imagen
    
    #Usuario
    st.text_input("¿Cuál es tu nombre? (Este input sale con st.text_input) y se asigna una key", key="name")
    st.session_state.name #Para mostrar lo que guardamos en key
    
    #Como un print y no es necesario escribir st.text
    st.text('¡Hola '+st.session_state.name+' ! (Aquí concatenamos con st.text y con st.session_state.key)') 
    'Esta es otra forma de poner lo que pusimos en st.session_state.key, sin st.text, mi querid@ ',st.session_state.name
    
    #Generamos el Dataframe como si estuvieramos en Pandas
    'Importante generar el raw para el dataframe'
    df = pd.read_csv('https://raw.githubusercontent.com/LilianaC/streamlit3/main/Datos%20F1%20Dutch%20GP%20-%20Sheet1.csv')
    #Estos Dataframes se copian y pegan con la opción de raw, se pega la dirección de arriba del navegador
    
    
    #Sí el checkbox es verdadero y solo escribimos df
    if st.checkbox('Mostrar dataframe (con el código st.checkbox en un if)'):
        df
    
    #Lista desplegable
    option = st.selectbox(
        'Selecciona tu corredor favorito (con st.selectbox y dentro invocamos con df la casilla que va a llamar): ',
        #De dónde va a sacar la información
         df['DRIVER'])
    
    'Tu selección: ', option
    
    #Línea que muestra toda la info del renglón
    'Mostramos todo lo que haya en un renglón de a cuerdo con: df.loc[df[´Columna_Select´]==variable]'
    df.loc[df['DRIVER'] == option]
    
    #Gráfica
    'La gráfica aparece, de manera sencilla, con st.line_chart(df, x=´AVG_Speed´, y=´LAP´ )'
    st.line_chart(
        df,
        x = 'AVG SPEED',
        y = 'LAP'
    )



#Definimos los nombres de las páginas para llamarlas
page_names_to_funcs = {
    "Home 🥇": Home,
    "Proyectos 🎎": page1,
    "Datos FIFA ⚽": page2,
    "Deltas 🚥": page3,
    "Formula1 🏎": page4,
}
#Aquí trabaja como un diccionario y manda a llamar a la parte de las keys
selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]() #Manda a llamar la función seleccionada


