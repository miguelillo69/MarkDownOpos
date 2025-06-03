# 12 Reglas de Codd

- Edgar F. Codd formuló estas 12 reglas para definir las características que debe cumplir un sistema de gestión de bases de datos relacional:

1. **Regla de la información**: Toda la información en una base de datos debe representarse de manera explícita en tablas.

2. **Regla del acceso garantizado**: Cada valor atómico en la base de datos debe ser accesible de manera lógica mediante la combinación del nombre de la tabla, el valor de clave primaria, y el nombre de columna.

3. **Tratamiento sistemático de valores nulos**: Los valores nulos (información faltante o inaplicable) deben ser manejados de manera sistemática e independiente de los tipos de datos.

4. **Catálogo dinámico en línea basado en el modelo relacional**: El catálogo de la base de datos debe estar almacenado en la base de datos misma y ser accesible usando las mismas herramientas que se aplican a los datos.

5. **Regla del sublenguaje de datos comprensivo**: Debe haber un sublenguaje de datos, con soporte para definición, manipulación, restricciones, y transacciones de datos. Este sublenguaje debe tener una sintaxis bien definida.

6. **Regla de actualización**: Todas las vistas que son teóricamente actualizables deben ser actualizables por el sistema.

7. **Inserción, actualización y eliminación de alto nivel**: El sistema debe soportar inserciones, actualizaciones y eliminaciones de datos de una manera que opere sobre conjuntos de datos, no solo registros individuales.

8. **Independencia física de los datos**: Las aplicaciones no deben verse afectadas por cambios en la representación física o los métodos de almacenamiento de datos.

9. **Independencia lógica de los datos**: Los cambios en las tablas y vistas deben ser posibles sin tener que alterar las aplicaciones que las utilizan.

10. **Integridad de los datos**: El sistema debe mantener todas las restricciones de integridad especificadas por el usuario, así como las restricciones de integridad internas.

11. **Independencia de distribución**: El sistema debe ser capaz de gestionar una base de datos distribuida sin que las aplicaciones deban ser modificadas.

12. **Regla de no subversión**: Si el sistema proporciona una interfaz de bajo nivel, esta no debe ser capaz de subvertir las reglas de integridad y seguridad del sistema relacional.
