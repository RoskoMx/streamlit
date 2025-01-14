# Contents of ~/my_app/streamlit_app.py

import requests
import streamlit as st
#from streamlit_lottie import st_lottie

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
    
    with st.container():
      st.subheader("Hola bienvenido a mi sitio web de proyectos :wave:")
      #st.title("Información random de contacto")
      st.write("El apartado HOME está destinado a probar las distribuciones de una página web en Streamlit. Además incluye una forma interesante de poner un enlace en la palabra o frase que mejor describa el lugar.")
          
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

                ***Si lo prefieres, también puedes visitar un sitio web mucho más sencillo donde te mostramos cómo poder hacer uso del mismo.*** 
                """
            )
            st.write("[Este es el enlace](https://debutants-sur-internet.streamlit.app)")

        with right_column:
            st.image(Image.open('images/_289490e8-96c2-420d-a924-a976d48429f0.jpeg'))

    
def page1():
    st.markdown("# Animación")
    st.sidebar.markdown("# HTML y Js aquí")

    # Código HTML con la animación Lottie
    animacion_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Animación Lottie</title>
        <!-- Incluye la biblioteca Lottie desde CDN -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.3/lottie.js"></script>
    </head>
    <body>
        <!-- Contenedor para la animación Lottie -->
        <div id="animation-container" style="width: 300px; height: 300px;"></div>
    
        <script>
            // Configuración de la animación Lottie desde una URL
            var animationConfig = {
                container: document.getElementById('animation-container'),
                renderer: 'canvas',
                loop: true,
                autoplay: true,
                path: 'https://assets3.lottiefiles.com/packages/lf20_C9wLez.json' // URL de una animación relacionada con México
            };
    
            // Cargar la animación Lottie
            var animacion = lottie.loadAnimation(animationConfig);
        </script>
    </body>
    </html>
    """
    
    # Mostrar el contenido HTML en Streamlit
    st.components.v1.html(animacion_html, height=400, scrolling=False)
    
      
    with st.container():
      st.write("---") 
      left_column, right_column = st.columns(2)
      with left_column:
        st.header("Increíble, ¿no?")
        st.write(
          """
            En esta parte del sitio te mostramos cómo es posible incluir código HTML y JS
            para poder incluir imágenes animadas o archivos Json. Existe otra manera, al parecer, más
            sencilla que otros canales de Youtube abordan pero por alguna extraña razón
            la manera de utilizar lotties no nos es posible en este intento.
          """
        )
        st.write("Manera de incluir un enlace para un video musical en [Youtube >](https://www.youtube.com/watch?v=_vnF1nYcUys)")
      
      with right_column:
          st.write("Esta parte incluye el mismo video mostrado en la columna de la izquierda pero ahora mostrado directamente en la página:.")
          st.video("https://www.youtube.com/watch?v=_vnF1nYcUys", format="video/mp4", start_time=0)

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


    st.write('Hola, *saludos desde México* 🇲🇽 :sunglasses:')
    x = st.slider('Selecciona un valor en la barra deslizadora', min_value=1, max_value=100, step=2)
    st.write(x, 'su cuadrado es: ', x * x)


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
    "Otros lenguajes 🎎": page1,
    "Datos FIFA ⚽": page2,
    "Deltas 🚥": page3,
    "Formula1 🏎": page4,
}
#Aquí trabaja como un diccionario y manda a llamar a la parte de las keys
selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]() #Manda a llamar la función seleccionada


