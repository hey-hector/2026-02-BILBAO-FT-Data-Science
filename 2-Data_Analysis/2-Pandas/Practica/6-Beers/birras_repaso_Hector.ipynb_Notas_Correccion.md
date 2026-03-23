# Informe: Revisión de Jupyter Notebook de Hector Yustos Betolaza

**Nombre de archivo:** Ejercicio pandas estadística.ipynb

---

## Calificación Global: **Mal**

### Resumen de Desempeño en Factores Principales

1.  **Comprensión de las Tareas**: Hector muestra una comprensión inicial de las tareas en la primera parte del notebook (Ejercicios 1-10), resolviendo correctamente varios de ellos. Sin embargo, hay una falta significativa de comprensión o capacidad para abordar la mayoría de los ejercicios de la segunda mitad (Ejercicios 11-15 y 19-24), los cuales quedan sin resolver. Además, se observan malentendidos conceptuales en tareas clave como la eliminación de columnas (Ejercicio 3) y la unión de DataFrames (Ejercicio 18), que son fundamentales en la manipulación de datos.
2.  **Corrección de las Respuestas**: Las respuestas en los primeros ejercicios son mayormente correctas, con algunas excepciones. En el Ejercicio 3, la columna no se elimina realmente del DataFrame. En el Ejercicio 8, la segunda parte no se aplica al subconjunto de datos correcto. El Ejercicio 18 utiliza un método de unión (`concat`) que no es apropiado para la relación entre los datasets, resultando en un DataFrame con muchos valores nulos y una estructura no deseada.
3.  **Ejercicios No Resueltos**: Un número muy elevado de ejercicios (14 de 24) no han sido resueltos. El estudiante incluso indica explícitamente que los Ejercicios 11-15 fueron omitidos por dificultad, lo que representa una parte considerable del trabajo.

### Resumen de Desempeño en Factores Secundarios

1.  **Legibilidad del Código**: El código escrito es generalmente legible, con nombres de variables claros y una estructura sencilla. Se aprecia el uso de múltiples formas para resolver el mismo punto en el Ejercicio 4.
2.  **Comentarios en el Código**: Se incluyen comentarios en varios ejercicios, lo cual es un punto positivo. Estos comentarios a menudo explican la lógica o las observaciones del estudiante, aunque en algunos casos revelan malentendidos (como en el Ejercicio 3 o 18). Se valora el uso de `info()` y `head()` para verificar los datos después de algunas operaciones.

---

## Lista de Ejercicios con Problemas

| Nº | Ejercicio | Problema Detectado | Recomendación |

## Comentarios Finales

Hector ha demostrado un buen inicio en la manipulación de datos con `pandas` en la primera parte del notebook, resolviendo correctamente varios ejercicios básicos y mostrando iniciativa al usar `info()` y `head()` para verificar los datos. Los comentarios en su código son un punto fuerte, ya que explican su razonamiento y observaciones.

Sin embargo, el desempeño general se ve gravemente afectado por un gran número de ejercicios sin resolver (más de la mitad del notebook) y por malentendidos conceptuales importantes en tareas como la eliminación de columnas (Ejercicio 3) y la unión de DataFrames (Ejercicio 18). La declaración explícita de haber omitido una sección por dificultad es una señal clara de que el material no ha sido asimilado completamente.

Para mejorar, se recomienda encarecidamente:

*   **Revisar los fundamentos de `pandas`**: Es crucial asegurarse de entender cómo funcionan los métodos que modifican DataFrames (`drop`, `rename`, etc.) y la diferencia entre `concat` y `merge` para unir datos de forma relacional.
*   **Completar todos los ejercicios**: Es fundamental intentar resolver cada problema, incluso si se requiere investigar en la documentación o pedir ayuda. Los ejercicios de visualización y agrupación son pilares en Data Science.
*   **No omitir secciones**: Si un ejercicio es difícil, es una oportunidad para aprender y buscar recursos adicionales.

Con un esfuerzo concentrado en estas áreas, Hector podrá mejorar significativamente su comprensión y habilidades en Data Science.