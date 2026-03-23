# Video Game Sales Analysis

Análisis exploratorio para identificar qué factores predicen el éxito comercial
de un videojuego según plataforma, género y región (2010–2016), con el fin de
orientar la planificación de campañas.

## Objetivo del negocio

Una tienda de videojuegos en línea planifica su presupuesto publicitario para
2017. Para invertir de forma eficiente necesita saber:

- ¿Qué plataformas están ganando o perdiendo cuota de mercado?
- ¿Las reseñas de críticos o de usuarios realmente impulsan las ventas?
- ¿Qué géneros son más rentables en cada región?
- ¿Hay diferencias significativas de preferencia entre plataformas y géneros?

Se usa el histórico de ventas de 1980 a 2016, acotando a **2010–2016** como el
periodo más relevante para predecir el comportamiento cercano.

## Tecnologías

Python 3.11 · pandas · NumPy · SciPy · Matplotlib · Seaborn · Jupyter Notebook

## Dataset

`games.csv` — ~16 000 videojuegos.

| Columna | Descripción |
|---|---|
| `name` | Título del juego |
| `platform` | Consola/PC |
| `year_of_release` | Año de lanzamiento |
| `genre` | Género |
| `na_sales` / `eu_sales` / `jp_sales` / `other_sales` | Ventas por región (millones USD) |
| `critic_score` | Puntuación profesional (0–100) |
| `user_score` | Puntuación de usuarios (0–10) |
| `rating` | Clasificación ESRB |

## Estructura del proyecto

```
video-game-sales-analysis/
├── Notebook/
│   └── games_sales_analysis.ipynb
├── datasets/
│   └── games.csv
├── video_game_sales_analysis.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Metodología

**1. Limpieza.** Nombres de columnas a minúsculas; `tbd` → `NaN` en
`user_score` (a float); `year_of_release` a entero con manejo seguro de nulos;
columna `total_sales` (suma de ventas regionales); descarte de filas sin
`name`, `genre` o `year_of_release`.

**2. Análisis exploratorio.** Tendencia de lanzamientos por año (pico en
2008–2010); ciclo de vida de plataformas (~5–10 años); boxplots de ventas por
plataforma (escala log); dispersión reseñas vs ventas (PS4); barras de ventas
por género, región (NA/EU/JP) y clasificación ESRB.

**3. Pruebas de hipótesis.** Prueba t de Welch (`equal_var=False`), α = 0.05.

## Resultados

**Plataformas**

- **PS4 y Xbox One** son las más prometedoras de cara a 2017 por su trayectoria.
- X360, PS4 y Wii muestran las mayores ventas promedio por título.

**Reseñas vs ventas (PS4)**

| Tipo de reseña | Correlación con ventas |
|---|---|
| Crítica (Metacritic) | ~0.40 — relación moderada |
| Usuarios | ~0.10 — relación despreciable |

Las reseñas **profesionales** son un predictor de ventas más fiable que las de
usuarios.

**Géneros (2010–2016):** más rentables Acción, Shooter y Deportes; mayores
ventas por título Shooter y Plataforma; menos rentables Puzzle, Estrategia y
Aventura.

**Preferencias regionales**

| Región | Plataformas top | Géneros top |
|---|---|---|
| NA | PS4, XOne, X360 | Acción, Shooter, Deportes |
| EU | PS4, XOne, X360 | Acción, Shooter, Deportes |
| JP | 3DS, PS3, PSV | RPG, Acción, Misc |

Japón muestra un perfil distinto: dominan las portátiles y los RPG.

**Pruebas de hipótesis**

- **Xbox One vs PC (puntuación de usuarios):** no se rechaza H₀ — sin diferencia
  significativa.
- **Acción vs Deportes (puntuación de usuarios):** se rechaza H₀ — las
  puntuaciones difieren significativamente.

## Conclusiones

Para 2017 conviene priorizar títulos de Acción/Shooter en PS4 y Xbox One para NA
y EU, y un catálogo diferenciado de RPG (y portátiles) para Japón. La crítica
profesional es una señal más útil que la de usuarios al estimar el potencial de
ventas.

## Cómo ejecutar

```bash
git clone https://github.com/OrlandoCorona/video-game-sales-analysis.git
cd video-game-sales-analysis

python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook Notebook/games_sales_analysis.ipynb
```

El mismo análisis está disponible como script en
[`video_game_sales_analysis.py`](video_game_sales_analysis.py).

## Trabajo futuro

- Añadir comparativas gráficas región por región.
- Modelar la predicción de ventas con regresión.
- Incorporar datos posteriores a 2016 para validar las predicciones.
