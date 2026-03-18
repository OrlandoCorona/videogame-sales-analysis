# Video Game Sales Analysis

Análisis del histórico mundial de ventas de videojuegos para identificar qué
**plataformas y géneros** tienen mayor potencial comercial y orientar la
planificación de campañas del siguiente año.

## Objetivo del negocio

Una tienda de videojuegos necesita decidir en qué títulos invertir para la
campaña de 2017. El análisis responde:

> ¿Qué plataformas y géneros son más rentables, y qué factores (reseñas,
> región, clasificación ESRB) influyen en las ventas?

## Tecnologías

- Python 3.11
- pandas / NumPy — limpieza y agregación
- SciPy — pruebas de hipótesis (t de Welch)
- Matplotlib / Seaborn — visualización
- Jupyter Notebook

## Dataset

Un archivo `games.csv` con ventas por región, puntuaciones y clasificación
ESRB de miles de títulos. Detalle en [`datasets/README.md`](datasets/README.md).

## Proceso de análisis

1. **Carga y exploración** del dataset.
2. **Limpieza:** nombres de columnas a minúsculas, `tbd` → `NaN` en
   `user_score`, conversión de tipos y tratamiento de valores ausentes.
3. **Enriquecimiento:** columna `total_sales` (suma de ventas regionales).
4. **Análisis temporal:** lanzamientos por año y ciclo de vida de plataformas;
   se acota el estudio al periodo relevante 2010-2016.
5. **Plataformas y géneros:** ventas totales y promedio, distribución (boxplots).
6. **Reseñas vs ventas:** correlación de `critic_score` y `user_score` con las
   ventas (caso PS4).
7. **Análisis regional:** preferencias de plataforma, género y ESRB en NA, EU y JP.
8. **Pruebas de hipótesis:** Xbox One vs PC y Acción vs Deportes.

## Resultados

- **PS4 y Xbox One** son las plataformas más prometedoras para 2017.
- **Acción** y **Shooter** son los géneros más rentables; **Puzzle** y
  **Aventura**, los menos.
- Las reseñas **profesionales** se correlacionan más con las ventas que las de
  usuarios.
- Las preferencias regionales difieren: NA/EU favorecen consolas de sobremesa y
  shooters; Japón, portátiles y RPG.

## Conclusiones

Para 2017 conviene priorizar títulos de Acción/Shooter en PS4 y Xbox One para
los mercados de NA y EU, y un catálogo diferenciado de RPG para Japón. Las
puntuaciones de la crítica son una señal más útil que las de los usuarios al
estimar el potencial de ventas.

## Estructura del proyecto

```
video-game-sales-analysis/
├── Notebook/
│   └── games_sales_analysis.ipynb     # análisis exploratorio
├── datasets/
│   └── games.csv
├── video_game_sales_analysis.py       # análisis en formato script
├── requirements.txt
├── LICENSE
└── README.md
```

## Cómo ejecutar

```bash
git clone https://github.com/OrlandoCorona/video-game-sales-analysis.git
cd video-game-sales-analysis

python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook Notebook/games_sales_analysis.ipynb
```

El análisis también está disponible como script en
[`video_game_sales_analysis.py`](video_game_sales_analysis.py).

## Capturas sugeridas

En una carpeta `images/` puedes añadir:

- Ventas por año de las plataformas principales.
- Ventas totales por género (2010-2016).
- Dispersión reseñas vs ventas (PS4).

## Trabajo futuro

- Añadir comparativas gráficas región por región (sugerencia del análisis).
- Modelar la predicción de ventas con regresión.
- Incorporar datos posteriores a 2016 para validar las predicciones.
