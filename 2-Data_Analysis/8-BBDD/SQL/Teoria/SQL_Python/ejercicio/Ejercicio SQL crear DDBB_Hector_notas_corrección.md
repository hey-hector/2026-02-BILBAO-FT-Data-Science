# Informe de Revisión del Jupyter Notebook de Hector

**Nombre de archivo:** Ejercicio SQL crear DDBB_Hector.ipynb

---

## Calificación Global: **Excepcional**

### Resumen de Desempeño en Factores Principales

1. **Comprensión de las Tareas** – Héctor demuestra una comprensión sobresaliente tanto de los conceptos de manipulación de datos con bases de datos relacionales como de la sintaxis de SQL. Aborda sin problemas operaciones avanzadas, como subconsultas para recuperar identificadores dinámicamente y agrupaciones condicionales (`HAVING COUNT`).
2. **Corrección de las Respuestas** – El código implementado es totalmente funcional y las consultas (JOINs múltiples, filtros por fechas, strings y agrupaciones) devuelven exactamente los resultados esperados. Las lógicas de agregación y los cruces de tablas están perfectamente planteados.
3. **Ejercicios No Resueltos** – Todas las tareas han sido abordadas mediante su correspondiente celda de código. No hay ejercicios en blanco.

### Resumen de Desempeño en Factores Secundarios

1. **Legibilidad del Código** – El cuaderno goza de una legibilidad excelente. Es una gran práctica haber encapsulado cada consulta en una función específica de Python y haber invertido esfuerzo en dar un formato visual claro a las salidas (usando f-strings espaciados y líneas divisorias) simulando las tablas de resultados.
2. **Comentarios en el Código** – El código está muy bien documentado. Cada bloque cuenta con comentarios que no solo explican lo que hace el código, sino también la lógica detrás de la consulta SQL y la interpretación final del resultado (por ejemplo, justificando por qué un bar o un empleado específico cumple los requisitos de la consulta).

---

## Lista de Ejercicios con Problemas

*Nota: Dado el alto nivel del cuaderno, los problemas detectados no son errores de código o de lógica, sino detalles operativos asociados a las buenas prácticas en la ejecución de cuadernos de Jupyter.*

| Nº | Ejercicio | Problema Detectado | Recomendación |
| --- | --- | --- | --- |
| 9 | **Actualizar sueldo por mayor actividad (`actualizar_sueldo_mayor_actividad`)** | La lógica de la consulta es matemáticamente y sintácticamente perfecta. Sin embargo, el resultado impreso muestra el sueldo de Vicente Merario en 121,275 (resultado de aplicarle el incremento del 5% dos veces: `110000 * 1.05 * 1.05`). Esto ocurre habitualmente cuando se ejecuta una celda de tipo `UPDATE` varias veces en el entorno Jupyter. | Al realizar operaciones de actualización (`UPDATE`) o borrado (`DELETE`) en bases de datos a través de Jupyter, hay que tener precaución con las ejecuciones múltiples, ya que mutan el estado de los datos. Para evitar estos "efectos secundarios", es buena práctica recargar los datos originales desde cero antes de volver a ejecutar la celda para testearla. |

---

## Comentarios Finales

Héctor ha presentado un trabajo excelente. La integración de Python con SQLite se ha ejecutado de manera profesional, garantizando en todo momento la integridad de la base de datos (por ejemplo, realizando subconsultas para evitar la inserción manual de claves foráneas). El uso adecuado del cierre de conexiones (`conexion.close()`) y los "commits" denota buenos hábitos de programación. ¡Excelente trabajo!