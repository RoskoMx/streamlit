import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

st.title('Gráfica de un dataframe: Seleccionando los datos')
url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/Fifa%2023%20Fut%20Players.csv'
df= pd.read_csv(url)

st.title('Gráfica de barras')

columns = df.columns.tolist()

selected_columns = st.multiselect("Selecciona la columna a graficar", columns, default="League")
s = df[selected_columns[0]].str.strip().value_counts()

trace = go.Bar(x=s.index,y=s.values)
layout = go.Layout(title = "FIFA 21")
data = [trace]
fig = go.Figure(data=data,layout=layout)
st.plotly_chart(fig)


st.title('Gráfica de líneas')
valx = st.multiselect("Selecciona País, Liga o Club", columns, default="Country")
valy = st.multiselect("Selecciona la métrica", columns, default="Ratings")

valoresx = df[valx[0]].str.strip().value_counts()
valoresy = df[valy[0]].str.strip().value_counts()

st.text(len(valoresx))
st.text(len(valoresy))


st.text(valoresx.index)
st.text(valoresy.values)



trace2 = px.line(df,x=valoresx.index,y=valoresy.values)
st.plotly_chart(trace2, theme="streamlit", use_container_width=True)

#layout2 = go.Layout(title = "FIFA 21")
#data2 = [trace2]
#fig2 = go.Figure(data=data2,layout=layout2)
#st.plotly_chart(fig2)


