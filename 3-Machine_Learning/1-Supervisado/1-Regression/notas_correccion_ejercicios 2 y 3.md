# Informe: Revisión de Jupyter Notebook de Hector

**Nombre de archivo:** `Advertising_RidgeLasso_Hector.ipynb` y `3 Polynomial_Regression_Hector.ipynb`

---

## Calificación Global: **Excepcional**

### Resumen de Desempeño en Factores Principales

1. **Comprensión de las Tareas** – Hector demuestra un dominio excelente de los conceptos de regresión y regularización. No solo aplica los modelos, sino que justifica la elección de cada uno basándose en la naturaleza de los datos (ej. captura de sinergias mediante interacciones polinómicas).
2. **Corrección de las Respuestas** – El código es impecable y técnicamente preciso. Realiza correctamente la eliminación de variables redundantes (`RAD`) para evitar la multicolinealidad y aplica el escalado de datos (`StandardScaler`) necesario para modelos penalizados como Ridge y Lasso.
3. **Ejercicios No Resueltos** – Todos los ejercicios han sido resueltos. En el notebook de `Advertising`, aunque indica que los resultados están en las celdas de código, integra la interpretación de forma narrativa en el flujo de trabajo.

### Resumen de Desempeño en Factores Secundarios

1. **Legibilidad del Código** – El código está muy bien estructurado, con bloques lógicos definidos y un uso profesional de librerías como `pandas`, `seaborn` y `scikit-learn`.
2. **Comentarios en el Código** – El nivel de documentación es sobresaliente. Hector incluye explicaciones detalladas sobre qué significan las métricas (RMSE, R2) y por qué los resultados cambian al aumentar la complejidad del modelo.

---

## Lista de Ejercicios con Problemas

| Nº | Ejercicio | Problema Detectado | Recomendación |
| :--- | :--- | :--- | :--- |
| 1.3 | **Interpretación de resultados** | Falta la redacción explícita de la "fórmula" final y la respuesta numérica a cuánto cambian las ventas por cada unidad de radio/TV/news. | Aunque se analizan los coeficientes, se recomienda imprimir `model.intercept_` y `model.coef_` para redactar la ecuación final: $Sales = \beta_0 + \beta_1(TV)...$. |
| 2.1 | **Carga de datos (Boston)** | El dataset presentaba líneas de descripción iniciales que dificultaban la carga automática. | Hector resolvió esto correctamente usando `header=1` tras un primer intento fallido, demostrando capacidad de resolución de problemas técnicos. |

---

## Comentarios Finales

Hector ha realizado un trabajo de nivel avanzado. Es especialmente destacable su capacidad para analizar la **multicolinealidad** mediante matrices de correlación y tomar decisiones ejecutivas sobre qué variables eliminar. Además, el uso de `PolynomialFeatures` junto con `Lasso` para realizar una selección automática de variables (filtrando coeficientes que van a cero) muestra un uso maduro de la regularización.

Para mejorar aún más, se sugiere:
* Consolidar la respuesta final en un bloque de texto que responda directamente a las preguntas de negocio (la fórmula exacta), facilitando la lectura para un perfil no técnico.
* Explorar `RidgeCV` o `LassoCV` para automatizar la búsqueda del `alpha` óptimo en lugar de probar valores manuales en un bucle.

La experimentación con grados 2, 3 y 4 en el modelo polinómico ilustra perfectamente el compromiso entre sesgo y varianza: a mayor grado, el modelo se ajusta mejor al entrenamiento pero corre el riesgo de fallar en datos nuevos (overfitting).