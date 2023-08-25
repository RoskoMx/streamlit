import streamlit as st
from ipywidgets import interact

st.write('Hola, *saludos desde México* 🇲🇽 :sunglasses:')
x = st.slider('Selecciona un valor en la barra deslizadora')
st.write(x, 'su cuadrado es: ', x * x)
