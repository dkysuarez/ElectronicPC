import streamlit as st
import pandas as pd
import altair as alt

# Cargar los datos desde un archivo Excel
data = pd.read_excel('pages\\CopilotAnswers-20240929-193714.xlsx')

# Convertir la columna 'Precio' a numérico y manejar errores
data['Precio'] = pd.to_numeric(data['Precio'], errors='coerce')
data = data.dropna(subset=['Precio'])

# Mostrar los datos en una tabla
st.write("### Lista de Discos Duros")
st.dataframe(data)

# Filtrar los productos más baratos por tipo de disco
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

# Agregar filtros para que los usuarios puedan seleccionar el tipo de disco
tipo_disco = st.selectbox('Selecciona el tipo de disco', data['Tipo de Disco'].unique())
filtered_data = data[data['Tipo de Disco'] == tipo_disco]

st.write(f"### Productos del tipo {tipo_disco}")
st.dataframe(filtered_data)

# Calcular el precio promedio por tipo de disco
average_prices = data.groupby('Tipo de Disco')['Precio'].mean().reset_index()
average_prices.columns = ['Tipo de Disco', 'Precio Promedio']

st.write("### Precio Promedio por Tipo de Disco")
st.dataframe(average_prices)

promedio_por_tipo = data.groupby('Tipo de Disco')['Precio'].mean().reset_index()

# Crear un DataFrame con los tipos de disco y sus respectivos precios promedio
chart_data = pd.DataFrame({
    'Tipo de Disco': promedio_por_tipo['Tipo de Disco'],
    'Precio Promedio': promedio_por_tipo['Precio']
})

# Crear el gráfico de barras
st.bar_chart(
    chart_data,
    x='Tipo de Disco',
    y='Precio Promedio',
    color='#0066cc',  # Color personalizado para los barras
    width=800,
    height=600
)





# Convertir la columna 'Precio' a numérico y manejar errores
data['Precio'] = pd.to_numeric(data['Precio'], errors='coerce')
data = data.dropna(subset=['Precio'])

# Agregar un selector para el tipo de disco
tipo_disco = st.selectbox('Selecciona el tipo de disco', data['Tipo de Disco'].unique(), key='1')

# Filtrar los datos por tipo de disco
filtered_data = data[data['Tipo de Disco'] == tipo_disco]

# Agregar un selector para la capacidad
capacidad = st.selectbox('Selecciona la capacidad', filtered_data['Capacidad'].unique(), key='2')

# Filtrar los datos por capacidad
filtered_data = filtered_data[filtered_data['Capacidad'] == capacidad]

# Calcular el precio promedio del tipo de disco y capacidad seleccionados
average_price = filtered_data['Precio'].mean()

# Mostrar el promedio en la columna correspondiente
st.write("Vida Útil de los Monitores")
st.write(f"Precio promedio para {tipo_disco} con capacidad {capacidad}: {average_price:.2f}")

# Función para aplicar color a las celdas
def color_df(val):
    if val > average_price:
        color = 'red'
    else:
        color = 'green'
    return f'background-color: {color}'



# Mostrar el precio promedio total en la parte inferior del gráfico
st.write(f"Precio promedio total: {promedio_por_tipo['Precio'].mean():.2f}")




# Aplicar estilo al DataFrame filtrado
st.dataframe(filtered_data.style.map(color_df, subset=['Precio']))
