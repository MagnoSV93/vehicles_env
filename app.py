import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Escoge tu Gráfico de "Anuncio de venta de coches"')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir scatterplot')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Gráfico de un scatterplot para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)