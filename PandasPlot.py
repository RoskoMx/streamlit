import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

#requirements.txt

#Gráfica de barras
st.title('Gráfica de un dataframe: Selección de datos por los usuarios')
url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/Fifa%2023%20Fut%20Players.csv'
df= pd.read_csv(url)

st.title('Gráfica de barras')

columns = df.columns.tolist()
selected_columns = st.multiselect("Selecciona la columna a graficar", columns, default="League")
s = df[selected_columns[0]].str.strip().value_counts()

trace = go.Line(x=s.index,y=s.values)
layout = go.Layout(title = "FIFA 21")
data = [trace]
fig = go.Figure(data=data,layout=layout)
st.plotly_chart(fig)

#Gráfica de dispersión
st.title('Gráfica de Dispersión')
valx = st.multiselect("Selecciona País, Liga o Club", columns, default="Country")
valy = st.multiselect("Selecciona la métrica", columns, default="Ratings")

valoresx = df[valx[0]]
valoresy = df[valy[0]]

trace2 = px.scatter(df,x=valoresx.values,y=valoresy.values)
st.plotly_chart(trace2, theme="streamlit", use_container_width=True)

#Multiselección gráfica de barras
st.title('Gráfica de Dispersión: Ratings')
clist = df["Country"].unique().tolist()

countries = st.multiselect("Selecciona el país", clist)
st.header("Seleccionaste: {}".format(", ".join(countries)))

dfs = {country: df[df["Country"] == country] for country in countries}

fig = go.Figure()
for country, df in dfs.items():
  fig = fig.add_trace(go.Bar(x=df["Name"], y=df["Ratings"], name=country))

st.plotly_chart(fig)
