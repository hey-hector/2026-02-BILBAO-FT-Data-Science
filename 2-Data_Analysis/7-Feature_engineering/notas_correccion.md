# Informe de Revisión de Jupyter Notebooks de Hector

**Nombres de archivos:** `emails_Hector.ipynb` y `Ejercicio Apple_Hector.ipynb`

---

## Calificación Global: **Excepcional**

### Resumen de Desempeño en Factores Principales

1. **Comprensión de las Tareas** – Héctor demuestra una excelente comprensión analítica y técnica de los problemas planteados. El uso de métodos robustos como calcular la diferencia de días usando `max() - min()` (lo que hace que el código funcione sin importar el orden del índice) y el uso actualizado de la frecuencia `'BME'` en pandas, evidencian un alto nivel de asimilación de conceptos.
2. **Corrección de las Respuestas** – El código es completamente funcional y, en su gran mayoría, devuelve los resultados esperados. Solo se observan un par de detalles menores de interpretación en el agrupamiento de datos temporales y en los grupos de captura de la expresión regular, pero la lógica de programación aplicada es impecable.
3. **Ejercicios No Resueltos** – Todos los ejercicios en ambos notebooks han sido abordados y resueltos correctamente. Ninguno ha quedado en blanco.

### Resumen de Desempeño en Factores Secundarios

1. **Legibilidad del Código** – El código es limpio, bien estructurado y fácil de seguir. Además, Héctor ha aplicado **excelentes prácticas de Ciencia de Datos**, utilizando funciones como `.head()` e `.info()` de manera proactiva después de aplicar transformaciones (como en el Paso 5 y 6) para verificar que los cambios en el *DataFrame* se hayan realizado con éxito.
2. **Comentarios en el Código** – El nivel de documentación es sobresaliente. Héctor no se limita a escribir el código, sino que explica el "porqué" de cada parámetro utilizado (por ejemplo, `inplace=True`, `ascending=True` o el funcionamiento de `re.MULTILINE`), e incluso aporta una pequeña conclusión analítica al final de su gráfico.

---

## Lista de Ejercicios con Problemas

*Nota: Dado el gran nivel del trabajo, los siguientes puntos no son fallos críticos, sino correcciones de precisión y buenas prácticas para afinar aún más el código.*

| Nº | Ejercicio (Notebook) | Problema Detectado | Recomendación |
| --- | --- | --- | --- |
| N/A | **Extraer dominios** (`emails_Hector.ipynb`) | La expresión regular `r'@([\w.-]+\.[a-z]{2,})$'` es muy ingeniosa, pero al dejar la arroba (`@`) fuera del grupo de captura `()`, la salida omite este símbolo (ej. devuelve `thebridgeschool.tech` en lugar de `@thebridgeschool.tech`, como pedía el ejemplo). | Si se desea incluir la arroba en el resultado final usando `findall`, se debe ampliar el grupo de captura para que la abarque: `r'(@[\w.-]+\.[a-z]{2,})$'`. |
| 9 | **Get the last business day of each month** (`Ejercicio Apple_Hector.ipynb`) | Al usar `apple.resample('BME').mean()`, se están calculando los *promedios mensuales* de las acciones. Aunque el índice resultante mostrará el último día hábil del mes, los valores numéricos ya no serán los de ese día en específico. | Si el objetivo es extraer los datos exactos correspondientes al último día hábil de cada mes, es preferible utilizar el método `.last()` en lugar de `.mean()`: `<br>```python\napple_month = apple.resample('BME').last()\n``` ` |

---

## Comentarios Finales

Héctor ha presentado un trabajo fantástico. Su capacidad para documentar de forma clara cada paso y su iniciativa para verificar la integridad de los datos (`.info()`, `.is_unique`) son hábitos sumamente valiosos en el mundo real de la programación y el análisis de datos. La pequeña confusión con el método `.mean()` en las series temporales es un error de interpretación común, pero la sintaxis y la modernización de los comandos (como `'BME'`) son de primer nivel. ¡Un desempeño excelente!