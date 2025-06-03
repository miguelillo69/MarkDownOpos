# Chuleta de SQL
## 1. DQL (Data Query Language) - Lenguaje de Consulta de Datos
> ``DQL`` se utiliza para realizar consultas a bases de datos. La instrucción más común es SELECT.

#### Ejemplos:
````php
-- Selecciona todas las columnas de la tabla "empleados"
SELECT * FROM empleados;

-- Selecciona solo las columnas "nombre" y "edad" de la tabla "empleados"
SELECT nombre, edad FROM empleados;

-- Selecciona empleados mayores de 30 años
SELECT * FROM empleados WHERE edad > 30;

-- Ordena los resultados por la columna "nombre" de forma ascendente
SELECT * FROM empleados ORDER BY nombre ASC;

-- Selecciona los 5 primeros empleados
SELECT * FROM empleados LIMIT 5;
````

## 2. DDL (Data Definition Language) - Lenguaje de Definición de Datos
> ``DDL`` se utiliza para definir y modificar la estructura de la base de datos, como crear, alterar o eliminar tablas y otros objetos.

#### Ejemplos:
````php
-- Crea una tabla llamada "clientes"
CREATE TABLE clientes (
id INT PRIMARY KEY,
nombre VARCHAR(50),
email VARCHAR(100),
fecha_registro DATE
);

-- Modifica la tabla "clientes" añadiendo una columna "telefono"
ALTER TABLE clientes ADD telefono VARCHAR(15);

-- Elimina la tabla "clientes"
DROP TABLE clientes;

-- Renombra la tabla "clientes" a "clientes_archivados"
ALTER TABLE clientes RENAME TO clientes_archivados;
````

## 3. DML (Data Manipulation Language) - Lenguaje de Manipulación de Datos
> ``DML`` se utiliza para manipular los datos almacenados en las tablas, incluyendo insertar, actualizar y eliminar datos.

#### Ejemplos:
````php
-- Inserta un nuevo registro en la tabla "clientes"
INSERT INTO clientes (id, nombre, email, fecha_registro)
VALUES (1, 'Juan Pérez', 'juan.perez@gmail.com', '2023-09-01');

-- Actualiza el correo electrónico de un cliente específico
UPDATE clientes
SET email = 'juan.nuevoemail@gmail.com'
WHERE id = 1;

-- Elimina un cliente cuyo ID es 1
DELETE FROM clientes WHERE id = 1;
````

## 4. DCL (Data Control Language) - Lenguaje de Control de Datos
> ``DCL`` se utiliza para controlar el acceso a los datos almacenados en la base de datos, a través de permisos.

#### Ejemplos:
````php
-- Concede permisos de SELECT a un usuario llamado "usuario1"
GRANT SELECT ON empleados TO usuario1;

-- Revoca permisos de INSERT de un usuario llamado "usuario1"
REVOKE INSERT ON empleados FROM usuario1;
````

## 5. DTL (Data Transaction Language) - Lenguaje de Transacciones de Datos
> ``DTL`` se utiliza para gestionar las transacciones en la base de datos, permitiendo confirmar o deshacer cambios.

#### Ejemplos:
````php
-- Inicia una transacción
BEGIN TRANSACTION;

-- Inserta un nuevo registro dentro de una transacción
INSERT INTO clientes (id, nombre, email, fecha_registro)
VALUES (2, 'Ana López', 'ana.lopez@gmail.com', '2024-01-01');

-- Confirma los cambios realizados en la transacción
COMMIT;

-- Deshace los cambios realizados en la transacción
ROLLBACK;
````

## 6. CCL (Cursor Control Language) - Lenguaje de Control de Cursores
> ``CCL`` se utiliza para trabajar con cursores, que permiten manejar conjuntos de registros de una consulta de manera individual.

#### Ejemplos:
````php
-- Declara un cursor para recorrer los registros de la tabla "empleados"
DECLARE empleados_cursor CURSOR FOR
SELECT nombre, edad FROM empleados;

-- Abre el cursor
OPEN empleados_cursor;

-- Obtiene el siguiente registro del cursor
FETCH NEXT FROM empleados_cursor;

-- Cierra el cursor
CLOSE empleados_cursor;

-- Elimina el cursor
DEALLOCATE empleados_cursor;
````


## 7. ANSI-SQL (American National Standards Institute SQL)
> ``ANSI-SQL`` es el estándar ``SQL`` establecido para garantizar la compatibilidad entre diferentes sistemas de bases de datos. La mayoría de las instrucciones SQL que hemos visto son parte de ``ANSI-SQL``, pero algunos comandos específicos o extensiones pueden variar según el motor de la base de datos (como ``PostgreSQL``, ``MySQL``, ``Oracle``, ``SQL Server``, etc.).

#### Ejemplos:
````php
-- Uso estándar de ANSI SQL para seleccionar datos
SELECT nombre, email
FROM clientes
WHERE fecha_registro > '2023-01-01'
ORDER BY nombre ASC;

-- Creación de índices estándar ANSI SQL
CREATE INDEX idx_nombre ON clientes(nombre);

-- Uso de vistas ANSI SQL
CREATE VIEW vista_clientes_activos AS
SELECT * FROM clientes WHERE estado = 'activo';
````

### Resumen Rápido de los Principales Comandos SQL
``DQL``: SELECT, WHERE, ORDER BY, GROUP BY, HAVING.
``DDL``: CREATE, ALTER, DROP, RENAME.
``DML``: INSERT, UPDATE, DELETE.
``DCL``: GRANT, REVOKE.
``DTL``: BEGIN TRANSACTION, COMMIT, ROLLBACK.
``CCL``: DECLARE CURSOR, OPEN, FETCH, CLOSE, DEALLOCATE.

#### ``ANSI-SQL``
> La mayoría de los comandos mencionados siguen el estándar ``ANSI-SQL`` y son compatibles con la mayoría de los sistemas de bases de datos relacionales. Algunos comandos específicos pueden tener diferencias menores en sintaxis o funcionalidad, dependiendo del motor de la base de datos.

## Otros comandos ejecutables en SQL

## 1. Seleccionar Datos Básicos
* ``SELECT``: Selecciona columnas específicas de una tabla.
* ``FROM``: Indica la tabla de donde se obtendrán los datos.
#### Ejemplo:

````php
SELECT columna1, columna2 FROM tabla;

// Obtiene los nombres y edades de la tabla personas.
SELECT nombre, edad FROM personas;
````

## 2. Renombrar Columnas con AS
* ``AS``: Renombra una columna o tabla temporalmente en los resultados.
````php
SELECT columna AS alias FROM tabla;

// Renombra la columna nombre como NombreCompleto y edad como EdadActual.
SELECT nombre AS NombreCompleto, edad AS EdadActual FROM personas;
````

## 3. Filtrar Resultados con WHERE
* ``WHERE``: Filtra los resultados que cumplen una condición específica.
````php
SELECT * FROM tabla WHERE condicion;

//   Selecciona todas las personas cuya edad sea mayor a 18.
SELECT * FROM personas WHERE edad > 18;
````

## 4. Contar Filas con COUNT
* ``COUNT``: Devuelve el número de filas que cumplen una condición.
````php
SELECT COUNT(*) FROM tabla WHERE condicion;
 
 // Cuenta el número de personas mayores de 18 años.
SELECT COUNT(*) FROM personas WHERE edad > 18;
````

## 5. Ordenar Resultados con ORDER BY
* ``ORDER BY``: Ordena los resultados por una o más columnas, de manera ascendente (ASC) o descendente (DESC).
````php
SELECT * FROM tabla ORDER BY columna [ASC|DESC];

//Ordena las personas por edad en orden descendente.
SELECT nombre, edad FROM personas ORDER BY edad DESC;
````

## 6. Seleccionar Resultados Únicos con DISTINCT
* ``DISTINCT``: Selecciona únicamente los valores únicos de una columna.
`````php
SELECT DISTINCT columna FROM tabla;

// Selecciona todas las ciudades únicas de la tabla personas.
SELECT DISTINCT ciudad FROM personas;
`````

## 7. Consultas con Varias Tablas (JOINs)
* ``INNER JOIN``: Selecciona registros que tienen coincidencias en ambas tablas.

````php
SELECT a.columna1, b.columna2 FROM tabla1 a INNER JOIN tabla2 b ON a.columna = b.columna;
 
// Selecciona el nombre de la persona y la fecha de la orden de las tablas personas y ordenes donde el id de la persona coincide con persona_id en las órdenes.
SELECT p.nombre, o.fecha FROM personas p INNER JOIN ordenes o ON p.id = o.persona_id;
````

* ``LEFT JOIN``: Selecciona todos los registros de la tabla de la izquierda, y los registros coincidentes de la tabla de la derecha.
````php
SELECT a.columna1, b.columna2 FROM tabla1 a LEFT JOIN tabla2 b ON a.columna = b.columna;
// Selecciona todas las personas y sus órdenes, incluso si no tienen órdenes asociadas.
SELECT p.nombre, o.fecha FROM personas p LEFT JOIN ordenes o ON p.id = o.persona_id;
````

* ``RIGHT JOIN``: Selecciona todos los registros de la tabla de la derecha, y los registros coincidentes de la tabla de la izquierda.
````php
SELECT a.columna1, b.columna2 FROM tabla1 a RIGHT JOIN tabla2 b ON a.columna = b.columna;

// Selecciona todas las órdenes y sus personas asociadas, incluso si hay órdenes sin una persona.
SELECT p.nombre, o.fecha FROM personas p RIGHT JOIN ordenes o ON p.id = o.persona_id;
````

## 8. Agrupar Resultados con GROUP BY
* ``GROUP BY``: Agrupa los resultados por una o más columnas.

````php
SELECT columna, COUNT(*) FROM tabla GROUP BY columna;

// Cuenta cuántas personas hay por ciudad.
SELECT ciudad, COUNT(*) FROM personas GROUP BY ciudad;
````

## 9. Filtrar Grupos con HAVING
* ``HAVING``: Filtra resultados después de aplicar GROUP BY.

````php
SELECT columna, COUNT(*) FROM tabla GROUP BY columna HAVING COUNT(*) > valor;

// Muestra solo las ciudades con más de 2 personas.
SELECT ciudad, COUNT(*) FROM personas GROUP BY ciudad HAVING COUNT(*) > 2;
````

## 10. Limitar Resultados con LIMIT
* ``LIMIT``: Limita el número de resultados devueltos.
````php
SELECT * FROM tabla LIMIT cantidad;

// Devuelve los primeros 5 registros de la tabla personas.
SELECT * FROM personas LIMIT 5;
````

## 11. Usar Subconsultas
* ``Subconsulta``: Una consulta dentro de otra consulta.
````php
SELECT columna1 FROM (SELECT columna1 FROM tabla WHERE condicion) AS subconsulta; 

//Selecciona los nombres de las personas que tienen órdenes con un total mayor a 100.
SELECT nombre FROM personas WHERE id IN (SELECT persona_id FROM ordenes WHERE total > 100);
````

## 12. Actualizar Datos con UPDATE
* ``UPDATE``: Actualiza los registros que cumplen una condición.

````php
UPDATE tabla SET columna = valor WHERE condicion;

//Actualiza la edad de Juan a 30.
UPDATE personas SET edad = 30 WHERE nombre = 'Juan';
````

## 13. Eliminar Datos con DELETE
* ``DELETE``: Elimina registros que cumplen una condición.
````php
DELETE FROM tabla WHERE condicion;

// Elimina todas las personas menores de 18 años.
DELETE FROM personas WHERE edad < 18;
````

## 14. Crear Tablas con CREATE TABLE
* ``CREATE TABLE``: Crea las tablas de la BBDD.
````php
CREATE TABLE tabla (columna1 tipo_dato,columna2 tipo_dato,...);

// Crea una tabla personas con columnas para id, nombre, edad y ciudad.
CREATE TABLE personas (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(100),edad INT,ciudad VARCHAR(100));
````

