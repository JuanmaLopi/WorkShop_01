import pandas as pd
import matplotlib.pyplot as plt

from db_conexion import establecer_conexion

conn, cursor = establecer_conexion()

# Consulta SQL para seleccionar los datos
query = "SELECT * FROM candidates"

# Leer los datos en un DataFrame de pandas
df = pd.read_sql_query(query, conn)

# Contar la cantidad de tecnologias y guardarlas en una variable
num_tecnologias = df['Technology'].value_counts()
tecnologias = df['Technology'].unique()
#Pie Chart de Tecnologías
plt.pie(num_tecnologias,  labels = tecnologias, autopct='%0.2f%%')
plt.axis("equal")
plt.show()


# Horizontal Bar Chart by Year
df['Application Year'] = pd.to_datetime(df['Application Date']).dt.year
applications_per_year = df['Application Year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
bars = plt.barh(applications_per_year.index, applications_per_year.values, color='lightgreen')
plt.xlabel('Número de Aplicaciones')
plt.ylabel('Año de Aplicación')
plt.title('Número de Aplicaciones por Año')
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2, str(int(width)),
             va='center', ha='left')
plt.show()


# Bar Chart by Seniority
seniority = df['Seniority'].value_counts()
plt.figure(figsize=(10, 6))
bars = plt.bar(seniority.index, seniority.values, color='lightblue')
plt.xlabel('Seniority')
plt.ylabel('Número de Candidatos')
plt.title('Número de Candidatos por Seniority')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, str(int(yval)),
             va='bottom', ha='center')
plt.show()


# Multiline Chart by country over years (USA, Brazil, Colombia, and Ecuador only)
df['Application Year'] = pd.to_datetime(df['Application Date']).dt.year
countries = ['United States of America', 'Brazil', 'Colombia', 'Ecuador']
filtered_df = df[df['Country'].isin(countries)]
applications_per_year_country = filtered_df.groupby(['Application Year', 'Country']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 8))
for country in countries:
    plt.plot(applications_per_year_country.index, applications_per_year_country[country], marker='o', label=country) 
    for year, value in zip(applications_per_year_country.index, applications_per_year_country[country]):
        plt.text(year, value, str(value), va='bottom', ha='center')
plt.xlabel('Año de Aplicación')
plt.ylabel('Número de Aplicaciones')
plt.title('Número de Aplicaciones por Año para Países Seleccionados')
plt.legend(title='País')
plt.show()





