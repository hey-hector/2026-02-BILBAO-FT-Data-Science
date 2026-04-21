# Informe de Revisión de los Jupyter Notebooks de Hector

**Nombres de archivos:** `1 Height_Hector.ipynb` y `2 Diabetes_Hector.ipynb`

---

## Calificación Global: **Excepcional**

### Resumen de Desempeño en Factores Principales

1. **Comprensión de las Tareas** – Héctor demuestra una comprensión analítica y algorítmica sobresaliente de los modelos de regresión lineal. Entiende de forma clara el flujo de trabajo en Machine Learning: desde la importación de datos hasta el entrenamiento del modelo y la predicción.
2. **Corrección de las Respuestas** – El código es robusto y funcional. Se valora muy positivamente que haya implementado un Análisis Exploratorio de Datos (EDA) proactivo utilizando `.info()` y `.describe()`, lo cual garantiza que los datos están limpios antes del entrenamiento. Las métricas principales se calculan correctamente. No obstante, existe un pequeño error metodológico (fuga de datos o *data leakage*) al escalar los datos en el dataset de Diabetes, y se omite el cálculo del MAPE en el dataset de Altura.
3. **Ejercicios No Resueltos** – Impecable. Todas las tareas y preguntas teóricas cuentan con sus correspondientes celdas de código y texto, y han sido resueltas en su totalidad.

### Resumen de Desempeño en Factores Secundarios

1. **Legibilidad del Código** – La legibilidad es de primer nivel. El código está escrito de manera muy "pythonica", estructurado lógicamente y haciendo uso de nombres de variables claros y estándar (`X_train`, `y_test`, `y_pred`).
2. **Comentarios en el Código** – El nivel de documentación es excelente. Héctor no solo escribe código funcional, sino que añade anotaciones explicando la lógica detrás de sus decisiones (como el motivo para elegir ciertas variables predictoras), lo cual facilita mucho la revisión y es una gran práctica profesional.

---

## Lista de Ejercicios con Problemas

| Nº | Ejercicio (Notebook) | Problema Detectado | Recomendación |
| --- | --- | --- | --- |
| 3 | **Cálculo de métricas de error** (`1 Height_Hector.ipynb`) | El código calcula de manera exacta el MAE, MSE y RMSE, pero se ha olvidado de incluir el cálculo del Error Porcentual Absoluto Medio (MAPE), el cual también formaba parte del ejercicio. | Para calcular el MAPE, se puede importar la función `mean_absolute_percentage_error` directamente desde `sklearn.metrics`, o bien calcularlo matemáticamente usando numpy: `np.mean(np.abs((y_test - y_pred) / y_test))`. |
| - | **Preparación y escalado de datos** (`2 Diabetes_Hector.ipynb`) | Se aplica la estandarización (`StandardScaler`) a todo el conjunto de datos **antes** de hacer la división con `train_test_split`. Esto produce un problema conocido como *Data Leakage* (fuga de información), ya que la media y la desviación estándar aplicadas incluyen información de los datos de validación (test). | El escalado siempre debe ajustarse (`.fit()`) **solo** sobre el conjunto de entrenamiento (`X_train`) y luego transformarse (`.transform()`) sobre ambos conjuntos. La mejor práctica para evitar esto es integrar el escalador y el modelo predictivo dentro de un `Pipeline` de `scikit-learn`. |

---

## Comentarios Finales

Héctor ha presentado un trabajo técnico de altísima calidad. Su dominio de `pandas`, `numpy` y `scikit-learn` es muy sólido, y la costumbre de explorar descriptivamente los datos antes de entrenar un modelo evidencia que tiene la mentalidad rigurosa que exige la Ciencia de Datos.

El detalle metodológico del *Data Leakage* en el escalado de variables es un error conceptual muy común en esta etapa de aprendizaje, pero es crucial corregirlo para garantizar que la evaluación del modelo en el mundo real sea honesta y precisa. Implementar el uso de `Pipelines` en sus próximos proyectos no solo solucionará esto, sino que hará que su código sea aún más elegante y profesional. ¡Sigue con este excelente nivel!