import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

st.title('Gráfica de un dataframe: Seleccionando los datos')
url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/Fifa%2023%20Fut%20Players.csv'
df= pd.read_csv(url)

st.title('Columna de barras')

columns = df.columns.tolist()

selected_columns = st.multiselect("Selecciona la columna a graficar", columns, default="League")
s = df[selected_columns[0]].str.strip().value_counts()

trace = go.Bar(x=s.index,y=s.values,showlegend = True)
layout = go.Layout(title = "FIFA 21")
data = [trace]
fig = go.Figure(data=data,layout=layout)
st.plotly_chart(fig)


st.title('Gráfica de líneas')
valx = st.multiselect("Selecciona los valores en x", columns, default="Country")
valy = st.multiselect("Selecciona los valores en y", columns, default="Ratings")

#valoresx = df[valx[0]].value_counts()
#valoresy = df[valy[0]].value_counts()


fig2 = px.line(df,
    x=valx,
    y=valy)

st.plotly_chart(fig2)


