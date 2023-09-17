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


st.title('Gráfica de Dispersión')
valx = st.multiselect("Selecciona País, Liga o Club", columns, default="Country")
valy = st.multiselect("Selecciona la métrica", columns, default="Ratings")


valoresx = df[valx[0]]
valoresy = df[valy[0]]

st.text(type(valoresx))

st.text(len(valoresx))
st.text(len(valoresy))


st.text(valoresx.index)
st.text(valoresy.values)



trace2 = px.scatter(df,x=valoresx.values,y=valoresy.values).update_yaxes(categoryorder="total descending")
trace2.update_xaxes(type='category')
st.plotly_chart(trace2, theme="streamlit", use_container_width=True)

#layout2 = go.Layout(title = "FIFA 21")
#data2 = [trace2]
#fig2 = go.Figure(data=data2,layout=layout2)
#st.plotly_chart(fig2)

st.title('Gráfica de Dispersión')
clist = df["Country"].unique().tolist()

countries = st.multiselect("Select country", clist)
st.header("Seleccionaste: {}".format(", ".join(countries)))

dfs = {country: df[df["Country"] == country] for country in countries}

fig = go.Figure()
for country, df in dfs.items():
  fig = fig.add_trace(go.Bar(x=df["Name"], y=df["Ratings"], name=country))

st.plotly_chart(fig)
