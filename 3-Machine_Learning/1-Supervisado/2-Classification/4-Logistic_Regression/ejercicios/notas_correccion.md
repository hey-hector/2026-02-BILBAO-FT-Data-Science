# Informe: Revisión de Jupyter Notebook de Hector

**Nombre de archivo:** Logistic-regression predict-ad-click_Hector.ipynb

---

## Calificación Global: **Excepcional**

### Resumen de Desempeño en Factores Principales

1. **Comprensión de las Tareas** – Hector demuestra un dominio total del flujo de trabajo de Machine Learning. No solo implementa los pasos técnicos, sino que explica con precisión el propósito de cada fase (EDA, preprocesamiento, validación y evaluación), demostrando que entiende la lógica de negocio tras las métricas.
2. **Corrección de las Respuestas** – El código es impecable y sigue las mejores prácticas de la industria:
   * **Prevención de Data Leakage:** El uso de `StandardScaler` es correcto, aplicando `fit_transform` solo en el set de entrenamiento.
   * **Robustez:** Implementa validación cruzada ($cv=5$) antes del entrenamiento final para asegurar que el modelo sea estable y no dependa de una partición aleatoria de los datos.
   * **Evaluación Completa:** Utiliza correctamente `predict_proba` para generar las curvas ROC y P-R, fundamentales para entender el umbral de decisión del modelo.
3. **Ejercicios No Resueltos** – Todas las secciones del proyecto están completas. Cada pregunta cuenta con su celda de código correspondiente y una interpretación de los resultados.

### Resumen de Desempeño en Factores Secundarios

1. **Legibilidad del Código** – El código es limpio, bien estructurado y utiliza nombres de variables estándar en la comunidad de Data Science (`logmodel`, `X_train_scal`, `y_probs`).
2. **Comentarios en el Código** – Excelente nivel de documentación. Hector incluye bloques de texto que explican el significado de métricas como el F1-Score o el AUC de forma pedagógica, lo cual añade un valor académico extra al notebook.

---

## Lista de Ejercicios con Problemas

No se han detectado errores técnicos o lógicos en la ejecución. Sin embargo, se sugiere una mejora menor en la parte de ingeniería de variables:

| Nº | Ejercicio | Problema Detectado | Recomendación |
| :--- | :--- | :--- | :--- |
| **2.1** | **Feature Engineering** | Uso de `LabelEncoder` para variables nominales con muchas categorías (`City`, `Country`). | En modelos lineales, el `LabelEncoder` puede introducir un orden jerárquico inexistente (ej. City 1 < City 2). Para la Regresión Logística, es preferible usar **One-Hot Encoding** o técnicas de reducción de cardinalidad si hay demasiadas categorías. |

---

## Comentarios Finales

Hector ha realizado un trabajo sobresaliente. Es especialmente destacable el uso de funciones de inspección de Pandas (`info`, `describe`, `head`) para validar cada paso de la ingeniería de variables. La interpretación de la **Matriz de Confusión** y de la **Curva ROC** es precisa y demuestra una capacidad analítica avanzada.

Para profundizar en cómo la Regresión Logística utiliza el umbral de probabilidad para clasificar, puedes observar el siguiente diagrama de la función sigmoide, que es el núcleo de este modelo:


El modelo está listo para producción. ¡Buen trabajo!