import pandas as pd
import matplotlib.pyplot as plt

from db_conexion import cerrar_conexion, establecer_conexion

conn, cursor = establecer_conexion()

# Consulta SQL para seleccionar los datos
query = "SELECT * FROM candidates"

# Leer los datos en un DataFrame de pandas
df = pd.read_sql_query(query, conn)

# Contar la cantidad de tecnologias
num_tecnologias = df['Technology'].value_counts()
print(num_tecnologias)


# Contar la Cantidad de aplicaciones por año
df['Application Year'] = pd.to_datetime(df['Application Date']).dt.year
applications_per_year = df['Application Year'].value_counts().sort_index()
print(applications_per_year)


# Contar la cantidad de Antiguedad
seniority = df['Seniority'].value_counts()
print(seniority)

# Contar la cantidad de aplicaciones por paise atraves de los años (USA, Brazil, Colombia, and Ecuador only)
df['Application Year'] = pd.to_datetime(df['Application Date']).dt.year
countries_of_interest = ['United States of America', 'Brazil', 'Colombia', 'Ecuador']
filtered_df = df[df['Country'].isin(countries_of_interest)]
applications_per_year_country = filtered_df.groupby(['Application Year', 'Country']).size().unstack(fill_value=0)
print(applications_per_year_country)

cerrar_conexion(conn)
