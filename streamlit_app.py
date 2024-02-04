import streamlit as st

st.write('Hola, *saludos desde México* 🇲🇽 :sunglasses:')
x = st.slider('Selecciona un valor en la barra deslizadora', min_value=1, max_value=10, step=1)
st.write(x, 'su cuadrado es: ', x * x)
