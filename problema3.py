import pandas as pd
import matplotlib.pyplot as plt

'''
    1. Leer el archivo CSV y cargar los datos en un DataFrame de pandas.
'''
print("****************\n****************\n****************\n Problema 1 \n****************\n****************\n****************")
# Lee el archivo CSV
df = pd.read_csv('./Covid-19 Dataset/country_wise_latest.csv')

'''
    2. Limpiar y preprocesar los datos (por ejemplo, tratar los valores faltantes, convertir tipos de datos
        si es necesario, cambiar el nombre de las columnas para que sean más descriptivas).
'''
print("****************\n****************\n****************\n Problema 2 \n****************\n****************\n****************")
# Reemplazar valores faltantes con la media de la columna
#df.fillna(df.mean(), inplace=True)

# Eliminar filas con valores faltantes
# df.dropna(inplace=True)

# Cambiar el nombre de las columnas
df.columns = ['PaisRegion','Confirmado','Muertes','Recuperado','Casos_Activos','Nuevos_casos','Nuevas_Muertes','Nuevas_Recuperaciones','Muertes_cada100_Casos','Recuperado_cada100_Casos','Muerte_cada100_Recuperados','Confirmados_UltimaSemana','Cambios_enUna_Semana','Porcentaje_deIncremento_enUna_Semana','queRegion']


# Muestra el dataFrame modificado
# print(df.head())

'''
    3. Calcular estadísticas descriptivas para las columnas numéricas (por ejemplo, media, mediana,
        desviación estándar, etc).
'''
print("****************\n****************\n****************\n Problema 3 \n****************\n****************\n****************")
# Seleccionar las columnas
columnas_seleccionadas = df[['Confirmado','Muertes','Recuperado','Casos_Activos','Nuevos_casos','Nuevas_Muertes','Nuevas_Recuperaciones','Muertes_cada100_Casos','Recuperado_cada100_Casos','Confirmados_UltimaSemana','Cambios_enUna_Semana','Porcentaje_deIncremento_enUna_Semana','queRegion']]

# Calcular estadísticas descriptivas para las columnas seleccionadas
estadisticas_descriptivas = columnas_seleccionadas.describe()

# Seleccionar solo las estadísticas específicas (media, mediana, desviacion estandar)
estadisticas_seleccionadas = estadisticas_descriptivas.loc[['mean', '50%', 'std']]

# mostrar resultados
print(estadisticas_seleccionadas)

'''
    4. Crear una nueva columna llamada Active que sea la cantidad de pacientes vivos.
'''
print("****************\n****************\n****************\n Problema 4 \n****************\n****************\n****************")
# Crear una nueva columna llamada 'Active' que sea la suma de 'Recuperado' y 'Casos_Activos'
df['Active'] = df[['Recuperado', 'Casos_Activos']].sum(axis=1)

# Imprimir el dataFrame con la nueva columna 'Active'
print(df)

'''
    5. Agrupar los datos por Country/Region y calcular el total de Confirmed , Deaths , Recovered , y
        Active para cada país.
'''
print("****************\n****************\n****************\n Problema 5 \n****************\n****************\n****************")
# Agrupa los datos por país y calcular el total de Confirmed, Deaths, Recovered y Active para cada país
datos_agrupados = df.groupby('PaisRegion').agg({
    'Confirmado': 'sum',
    'Muertes': 'sum',
    'Recuperado': 'sum',
    'Active': 'sum'
})

# Imprimir los datos agrupados
print(datos_agrupados)

'''
    6. Ordenar los países por el número total de casos confirmados y mostrar los 10 países con más
        casos confirmados.
'''
print("****************\n****************\n****************\n Problema 6 \n****************\n****************\n****************")
# Agrupar los datos por país y calcular el total de casos confirmados para cada país
total_confirmados_por_pais = df.groupby('PaisRegion')['Confirmado'].sum()

# Ordenar los países por el número total de casos confirmados de manera descendente
top_10_paises_confirmados = total_confirmados_por_pais.sort_values(ascending=False).head(10)

# Imprimir los 10 países con más casos confirmados
print("Los 10 países con más casos confirmados:")
print(top_10_paises_confirmados)

'''
    7. Visualizar la evolución de casos confirmados, muertes y recuperaciones a lo largo del tiempo para
        un país específico (por ejemplo, Estados Unidos, España o Brasil) utilizando gráficos de línea.
        Incluye comentarios explicativos en tu código y asegúrate de utilizar las funciones y métodos de
        pandas de manera adecuada.
'''
print("****************\n****************\n****************\n Problema 7 \n****************\n****************\n****************")
# Lee el archivo CSV
df = pd.read_csv('./Covid-19 Dataset/covid_19_clean_complete.csv')

# 1. Filtrar los datos para el país específico (por ejemplo, Basil)
pais_especifico = 'Brazil'
datos_pais_especifico = df[df['Country/Region'] == pais_especifico]

# 2. Agrupar los datos por fecha y calcular el total de casos confirmados, muertes y recuperaciones para cada fecha
datos_agrupados_por_fecha = datos_pais_especifico.groupby('Date').agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum'
}).reset_index()

# 3. Crear un gráfico de líneas para mostrar la evolución de casos confirmados, muertes y recuperaciones a lo largo del tiempo
plt.figure(figsize=(10, 6))
plt.plot(datos_agrupados_por_fecha['Date'], datos_agrupados_por_fecha['Confirmed'], label='Confirmados')
plt.plot(datos_agrupados_por_fecha['Date'], datos_agrupados_por_fecha['Deaths'], label='Muertes')
plt.plot(datos_agrupados_por_fecha['Date'], datos_agrupados_por_fecha['Recovered'], label='Recuperaciones')

# 4. Configuración del gráfico
plt.title(f'Evolución de COVID-19 en {pais_especifico}')
plt.xlabel('Fecha')
plt.ylabel('Número de Casos')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# 5. Mostrar el gráfico
plt.tight_layout()
plt.show()


