import streamlit as st
import pandas as pd
import altair as alt

# Cargar los datos desde un archivo CSV
@st.cache
def load_data():
    data = pd.read_csv('F:\Dani\pages\CopilotAnswers-20240929-193714.csv')
    return data

data = load_data()

# Mostrar los datos en una tabla
st.write("### Lista de Discos Duros")
st.dataframe(data)

# Filtrar los productos más baratos
cheapest_products = data.loc[data.groupby('Tipo de Disco')['Precio'].idxmin()]

st.write("### Productos Más Baratos por Tipo de Disco")
st.dataframe(cheapest_products)

# Crear un gráfico de barras para visualizar los precios
chart = alt.Chart(data).mark_bar().encode(
    x='Tipo de Disco',
    y='Precio',
    color='Tipo de Disco',
    tooltip=['Modelo/Marca', 'Capacidad', 'Precio', 'Vendedor']
).interactive()

st.altair_chart(chart, use_container_width=True)
