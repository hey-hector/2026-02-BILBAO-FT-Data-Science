# Informe: Revisión de Jupyter Notebook de Hector Yustos Betolaza - Lanbide 2026

**Nombre de archivo:** Fictitious_Names.ipynb

---

## Calificación Global: **Regular**

### Resumen de Desempeño en Factores Principales

1.  **Comprensión de las Tareas**: Hector demuestra una buena comprensión general de las tareas de creación y fusión de DataFrames. Sin embargo, hay una confusión significativa en el **Paso 5** al intentar unir DataFrames por columnas, y el **Paso 6** quedó sin resolver. En el **Paso 4**, la operación se realizó correctamente, pero se omitió la asignación del resultado a la variable solicitada (`all_data`).
2.  **Corrección de las Respuestas**: La mayoría de las soluciones implementadas son correctas. Los ejercicios de `merge` (Pasos 7, 8, 9) están bien resueltos y demuestran un buen entendimiento de los diferentes tipos de uniones. No obstante, la solución del **Paso 5** es incorrecta, ya que realiza una concatenación por filas en lugar de por columnas. El **Paso 4** es funcional pero incompleto al no asignar el resultado.
3.  **Ejercicios No Resueltos**: El **Paso 6** no fue resuelto.

### Resumen de Desempeño en Factores Secundarios

1.  **Legibilidad del Código**: El código es generalmente legible y claro. Se utilizan nombres de variables adecuados, aunque `all_data_col` en el Paso 5 es confuso dado el error lógico en la operación.
2.  **Comentarios en el Código**: Los comentarios son un punto fuerte. Hector incluye explicaciones detalladas y útiles sobre la lógica de las operaciones (`concat`, `merge`, `ignore_index`, `how='outer'`), lo que facilita enormemente la comprensión del código y demuestra un esfuerzo por entender los conceptos. El comentario en el Paso 6 también es muy honesto y útil para el revisor.

---

## Lista de Ejercicios con Problemas

| Nº | Ejercicio                                                                                                                                                                                                                                                                | Problema Detectado                                                                                                            | Recomendación                                                                                                                                                                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4   | **Join the two first dataframes along rows and assign to all_data**                                                                                                                                                                                                      | La operación de concatenación es correcta, pero el resultado no se asigna a la variable `all_data` como se solicita.         | Asignar el resultado de `pd.concat([data_1, data_2], ignore_index=True)` a la variable `all_data`.                                                                                       |
| 5   | **Join the two first dataframes along columns and assing to all_data_col**                                                                                                                                                                                               | Se realiza una concatenación por filas (`axis=0` implícito) en lugar de por columnas (`axis=1`), lo que resulta en un DataFrame con más filas en lugar de más columnas. | Utilizar `pd.concat([data_1, data_2], axis=1)` para unir los DataFrames por columnas. Esto creará un DataFrame más ancho con columnas de ambos.                                          |
| 6   | **Print the unique values of data3**                                                                                                                                                                                                                                     | El ejercicio no fue resuelto. El estudiante indica que le resultó complicado.                                                 | Utilizar `data_3['test_id'].unique()` para obtener los valores únicos de la columna 'test_id'.                                                                                          |

---

## Comentarios Finales

Hector ha demostrado un buen esfuerzo y una comprensión sólida de las operaciones de `merge` en pandas. Sus comentarios son excepcionalmente útiles y demuestran un pensamiento crítico sobre las funciones utilizadas. Sin embargo, la calificación "Regular" se debe a la confusión en la concatenación por columnas (Paso 5) y al ejercicio no resuelto (Paso 6), así como la omisión de la asignación en el Paso 4.

Para mejorar en futuras entregas, se recomienda:
*   Prestar especial atención a la diferencia entre `concat` por filas (`axis=0`) y por columnas (`axis=1`).
*   Asegurarse de que todos los ejercicios sean resueltos y que los resultados se asignen a las variables solicitadas.
*   Continuar con la excelente práctica de añadir comentarios explicativos, ya que son muy valiosos para el aprendizaje y la revisión.

Con estas mejoras, Hector tiene el potencial de alcanzar una calificación de "Bien" o "Excepcional".