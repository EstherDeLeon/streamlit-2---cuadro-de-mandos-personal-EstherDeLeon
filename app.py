

import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Carga el archivo CSV en un dataframe de pandas
data = pd.read_csv('AirBnb.csv')

# Muestra el dataframe en una tabla
#print(data)
st.header('Tabla de datos de airbnb de new york')
st.write(data)



# Leer el archivo CSV y almacenar los datos en un DataFrame
df = pd.read_csv("AirBnb.csv")

print(df.columns)
print(df.describe())


# Crear una lista de opciones de barrios únicos en el DataFrame
barrios = df['neighbourhood'].unique().tolist()

# Crear un menú desplegable en Streamlit que muestre las opciones de barrios
selected_barrio = st.sidebar.selectbox("Selecciona un barrio", barrios)

# Filtrar el DataFrame para mostrar los datos del barrio seleccionado
filtered_df = df[df['neighbourhood'] == selected_barrio]

# Mostrar la tabla en Streamlit
st.subheader('Tabla de datos filtrados por barrio seleccionado')
st.write(filtered_df)

#hago lo mismo con los precios
precios = df['price'].unique().tolist()
selected_precio = st.sidebar.selectbox("Selecciona un precio", precios)
filtered_df2 = df[df['price'] == selected_precio]
st.subheader('Tabla de datos filtrados por precio seleccionado')
st.write(filtered_df2)

#hago lo mismo con la disponibilidad
disponibilidad = df['availability_365'].unique().tolist()
selected_disponibilidad = st.sidebar.selectbox("Selecciona una disponibilidad", disponibilidad)
filtered_df3 = df[df['availability_365'] == selected_disponibilidad]
st.subheader('Tabla de datos filtrados por disponibilidad seleccionada')
st.write(filtered_df3)





# Seleccionar las filas que corresponden al barrio de Chinatown
chinatown_df = df[df["neighbourhood"] == "Chinatown"]

# Mostrar la tabla en Streamlit
st.subheader('Tabla de datos de airbnb del barrio de Chinatown de new york')
st.write(chinatown_df)
print(df.isnull().sum())


# Visualizar la distribución de precios
fig, ax = plt.subplots()
ax.hist(df['price'], bins=50)
plt.title('Grafico de la distribución de precios de las propiedades de Airbnb en Nueva York')
plt.xlabel('Precio')
plt.ylabel('Cantidad de propiedades ')
st.pyplot(fig)


# Obtener la cantidad de habitaciones por tipo
room_types = df['room_type'].value_counts()

# Crear un gráfico de barras
fig, ax = plt.subplots()
ax.bar(room_types.index, room_types.values)

# Agregar etiquetas y título
ax.set_xlabel('Tipo de habitación')
ax.set_ylabel('Número de propiedades')
ax.set_title('Grafico de cantidad de propiedades por tipo de habitación')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

neighbourhood = df['neighbourhood'].value_counts()[:10]

st.header('Grafico de barrios con más propiedades de Airbnb en Nueva York')
st.bar_chart(neighbourhood)



# Filtro para los precios por debajo de 150
df_filtered = df[df['price'] < 150]

# Histograma de precios
fig, ax = plt.subplots()
ax.hist(df_filtered['price'], bins=50)
ax.set_title("Gráfico de precios de Airbnb por debajo de 150 $")
ax.set_xlabel("Precio por noche (USD)")
ax.set_ylabel("Cantidad de propiedades")
st.pyplot(fig)

# Convertir el campo 'last_review' a datetime y crear el campo 'month'
df['last_review'] = pd.to_datetime(df['last_review'])
df['month'] = df['last_review'].dt.month

# Agrupar por mes y calcular el promedio de reseñas por mes
reviews_per_month = df.groupby('month')['reviews_per_month'].mean()

# Calcular el porcentaje de reseñas por mes
total_reviews = df['number_of_reviews'].sum()
reviews_percentage = (reviews_per_month / total_reviews) * 100

# Crear un gráfico de barras
fig, ax = plt.subplots()
ax.bar(reviews_percentage.index, reviews_percentage.values)
ax.set_xlabel('Mes')
ax.set_ylabel('Porcentaje de reseñas')
ax.set_title('Porcentaje de reseñas por mes')
st.pyplot(fig)





