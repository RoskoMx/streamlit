import streamlit as st

st.write('Hello, *World!* :sunglasses:')
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
