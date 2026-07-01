"""
Análisis de ventas de videojuegos por plataforma, género y región.

Versión en script del notebook `games_sales_analysis.ipynb`. Limpia el dataset,
calcula ventas totales, analiza tendencias por plataforma/género/región y
contrasta dos hipótesis sobre las calificaciones de usuarios.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# --- Análisis de ventas de videojuegos ---

# Cargar el dataset
df = pd.read_csv('datasets/games.csv')

# Mostrar información general
print("Información general del dataset:")
print(df.info())
print("\nPrimeras filas del dataset:")
print(df.head())
print("\nEstadísticas descriptivas:")
print(df.describe())

# Convertir nombres de columnas a minúsculas
df.columns = df.columns.str.lower()
print("Nombres de columnas en minúsculas:")
print(df.columns)

# Reemplazar 'tbd' en user_score por NaN y convertir a float
df['user_score'] = df['user_score'].replace('tbd', np.nan).astype(float)

# Convertir year_of_release a entero, manejando valores ausentes
df['year_of_release'] = df['year_of_release'].fillna(-1).astype(int)
df['year_of_release'] = df['year_of_release'].replace(-1, np.nan)

# Verificar tipos de datos
print("Tipos de datos después de la conversión:")
print(df.dtypes)

# Calcular ventas totales y agregarlas como nueva columna
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']

# Verificar nueva columna
print("Primeras filas con ventas totales:")
print(df[['name', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'total_sales']].head())

# Contar juegos por año
games_per_year = df.groupby('year_of_release').size()

# Graficar
plt.figure(figsize=(10, 6))
games_per_year.plot(kind='bar')
plt.title('Cantidad de juegos lanzados por año')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Número de juegos')
plt.show()

# Calcular ventas totales por plataforma
platform_sales = df.groupby('platform')['total_sales'].sum().sort_values(ascending=False)

# Seleccionar las 5 plataformas con mayores ventas
top_platforms = platform_sales.head(5).index

# Ventas por año para las plataformas principales
platform_year_sales = df[df['platform'].isin(top_platforms)].groupby(['platform', 'year_of_release'])['total_sales'].sum().unstack()

# Graficar
plt.figure(figsize=(12, 8))
platform_year_sales.T.plot()
plt.title('Ventas por año de las plataformas principales')
plt.xlabel('Año')
plt.ylabel('Ventas totales (millones USD)')
plt.legend(title='Plataforma')
plt.show()

# Filtrar datos desde 2010
df = df[df['year_of_release'] >= 2010]
print("Dimensiones del dataset filtrado (2010-2016):", df.shape)

# Ventas totales por plataforma (2010-2016)
platform_sales_recent = df.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
print("Ventas totales por plataforma (2010-2016):")
print(platform_sales_recent)

# Graficar ventas por año para plataformas relevantes
platform_year_sales_recent = df.groupby(['platform', 'year_of_release'])['total_sales'].sum().unstack()
plt.figure(figsize=(12, 8))
platform_year_sales_recent.T.plot()
plt.title('Ventas por año de plataformas (2010-2016)')
plt.xlabel('Año')
plt.ylabel('Ventas totales (millones USD)')
plt.legend(title='Plataforma')
plt.show()

# Diagrama de caja para ventas globales por plataforma
plt.figure(figsize=(14, 8))
sns.boxplot(x='platform', y='total_sales', data=df)
plt.title('Ventas globales por plataforma (2010-2016)')
plt.xlabel('Plataforma')
plt.ylabel('Ventas totales (millones USD)')
plt.xticks(rotation=45)
plt.yscale('log')  # Escala logarítmica para mejor visualización
plt.show()

# Calcular ventas promedio por plataforma
platform_avg_sales = df.groupby('platform')['total_sales'].mean().sort_values(ascending=False)
print("Ventas promedio por plataforma:")
print(platform_avg_sales)

# Filtrar datos de PS4
ps4_data = df[df['platform'] == 'PS4']

# Gráfico de dispersión: reseñas vs ventas
plt.figure(figsize=(10, 6))
plt.scatter(ps4_data['critic_score'], ps4_data['total_sales'], alpha=0.5, label='Critic Score')
plt.scatter(ps4_data['user_score'], ps4_data['total_sales'], alpha=0.5, label='User Score')
plt.title('Reseñas vs Ventas (PS4)')
plt.xlabel('Puntuación')
plt.ylabel('Ventas totales (millones USD)')
plt.legend()
plt.yscale('log')
plt.show()

# Calcular correlaciones
critic_corr = ps4_data['critic_score'].corr(ps4_data['total_sales'])
user_corr = ps4_data['user_score'].corr(ps4_data['total_sales'])
print(f"Correlación Critic Score vs Ventas: {critic_corr:.2f}")
print(f"Correlación User Score vs Ventas: {user_corr:.2f}")

# Seleccionar juegos que están en múltiples plataformas
multi_platform_games = df[df['name'].duplicated(keep=False)]
multi_platform_sales = multi_platform_games.groupby(['name', 'platform'])['total_sales'].sum().unstack()

# Comparar ventas de algunos juegos populares
print("Ventas de juegos en múltiples plataformas:")
print(multi_platform_sales.head(10))

# Ventas totales por género
genre_sales = df.groupby('genre')['total_sales'].sum().sort_values(ascending=False)

# Gráfico de barras
plt.figure(figsize=(10, 6))
genre_sales.plot(kind='bar')
plt.title('Ventas totales por género (2010-2016)')
plt.xlabel('Género')
plt.ylabel('Ventas totales (millones USD)')
plt.show()

# Ventas promedio por género
genre_avg_sales = df.groupby('genre')['total_sales'].mean().sort_values(ascending=False)
print("Ventas promedio por género:")
print(genre_avg_sales)

# Ventas por plataforma en cada región
na_platforms = df.groupby('platform')['na_sales'].sum().sort_values(ascending=False).head(5)
eu_platforms = df.groupby('platform')['eu_sales'].sum().sort_values(ascending=False).head(5)
jp_platforms = df.groupby('platform')['jp_sales'].sum().sort_values(ascending=False).head(5)

print("Top 5 plataformas en NA:", na_platforms)
print("Top 5 plataformas en EU:", eu_platforms)
print("Top 5 plataformas en JP:", jp_platforms)

# Ventas por género en cada región
na_genres = df.groupby('genre')['na_sales'].sum().sort_values(ascending=False).head(5)
eu_genres = df.groupby('genre')['eu_sales'].sum().sort_values(ascending=False).head(5)
jp_genres = df.groupby('genre')['jp_sales'].sum().sort_values(ascending=False).head(5)

print("Top 5 géneros en NA:", na_genres)
print("Top 5 géneros en EU:", eu_genres)
print("Top 5 géneros en JP:", jp_genres)

# Ventas por clasificación ESRB en cada región
esrb_sales = df.groupby('rating')[['na_sales', 'eu_sales', 'jp_sales']].sum()
print("Ventas por clasificación ESRB:")
print(esrb_sales)

# Gráfico de barras
esrb_sales.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas por clasificación ESRB por región')
plt.xlabel('Clasificación ESRB')
plt.ylabel('Ventas totales (millones USD)')
plt.show()

# Filtrar datos
xone_scores = df[df['platform'] == 'XOne']['user_score'].dropna()
pc_scores = df[df['platform'] == 'PC']['user_score'].dropna()

# Prueba t de dos muestras
t_stat, p_value = stats.ttest_ind(xone_scores, pc_scores, equal_var=False)
print(f"Prueba t (Xbox One vs PC): t={t_stat:.2f}, p-value={p_value:.4f}")

# Decisión
alpha = 0.05
if p_value < alpha:
    print("Rechazamos H0: Las calificaciones promedio son diferentes.")
else:
    print("No rechazamos H0: No hay evidencia de diferencia en las calificaciones promedio.")

# Filtrar datos
action_scores = df[df['genre'] == 'Action']['user_score'].dropna()
sports_scores = df[df['genre'] == 'Sports']['user_score'].dropna()

# Prueba t de dos muestras
t_stat, p_value = stats.ttest_ind(action_scores, sports_scores, equal_var=False)
print(f"Prueba t (Acción vs Deportes): t={t_stat:.2f}, p-value={p_value:.4f}")

# Decisión
if p_value < alpha:
    print("Rechazamos H0: Las calificaciones promedio son diferentes.")
else:
    print("No rechazamos H0: No hay evidencia de diferencia en las calificaciones promedio.")

