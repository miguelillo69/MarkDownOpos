# Modelo Entidad Relación
## Diseño de Base de Datos  

![](https://github.com/miguelillo69/Imagenes/blob/main/dise%C3%B1o_bbDD.png?raw=true)

## Diseño Conceptual (MER)  
- ¿Cuáles son las entidades y relaciones de la aplicación?  
- ¿Qué información de estas entidades y relaciones deberían ser almacenadas?  
- ¿Cuáles son las restricciones de integridad y las reglas de negocio?  
- Representación gráfica del modelo MER  
- Mapeo de un diagrama ER a un esquema relacional  

## Modelo Entidad-Relación
- **Entidad**: Objeto del mundo real distinguible de otros objetos. Una entidad se describe usando un conjunto de atributo.
- **Conjunto de entidades (tipo de entidad)**: Una colección de entidades similares (ej. todos los empleados).
  - Todas las entidades de un conjunto tiene los mismos atributos (a excepción de una jerarquía)
  - Cada conjunto de entidades tiene una llave
  - Cada atributo tiene un dominio  

````java
    Rut      nombre
      \        /
      Empleados
````
- Empleados  
Rut  
nombre  

## MER (2)  
Un tipo de entidad define el **esquema** o **intensión** para el conjunto de entidades que comparten la misma estructura. La colección de entidades de un tipo particular de entidad definen la **extensión** del tipo de entidad.  

## MER (3)  
- **Atributos**: En un MER existen diferentes tipos de atributos:  
  - Atributos **simples o atómicos**: son atributos no divisibles.  
  - Atributos **compuestos**: son atributos que se pueden dividir en sus componentes, pudiendo formar jerarquías.  
  - Atributos **monovaluado**s: son atributos que tienen un solo valor para una entidad en particular.  
  - Atributos **multivaluados**: son atributos que tienen límites inferior y superior en el número de valores para una entidad.  
  - Atributos **almacenados**  
  - Atributos **derivados**  
  - Valores **nulos**  
  - Atributos **complejos**: son atributos compuestos o multivaluados anidados de una manera arbitraria (lista, conjuntos).  

- Atributos clave de una entidad: Un tipo de entidad casi siempre tiene un atributo que es distinto para cada entidad.  
Hay ocasiones en que un conjunto de atributos constituyen la clave de una entidad (atributos subrayados en los diagramas).  
Algunas entidades tienen más de un atributo clave.  
- Dominio de los atributos: Cada uno de los atributos simples tienen asociado un conjunto de valores posibles.  

# MER (4)  
- Relación: Asociación entre dos o más entidades.  
Por ejemplo, X trabajo en departamento Y.  
- Conjunto de relaciones: Colección de relaciones similares:  
  - Un conjunto de relaciones n-area R relaciona n conjuntos de entidades E1,…,En; cada conjunto de entidades Ej en la relación R involucra alguna entidad de Ej.  
  - El mismo conjunto de entidades puede participar en distintos conjuntos de relaciones, o en diferentes “roles” en el mismo conjunto.  

## Modelo MER (5)  

![](https://github.com/miguelillo69/Imagenes/blob/main/mer_5.png?raw=true)

## Restricciones de llave  
- Relación “Trabaja_en”:  
  - Un empleado puede trabajar en un departamento  
  - Un departamento puede tener varios empleados  
  - Sin embargo, cada departamento puede tener a lo más un jefe por la restricción de llave de la relación administra  

![](https://github.com/miguelillo69/Imagenes/blob/main/res_llave.png?raw=true)

## Restricciones de llave (2)  

![](https://github.com/miguelillo69/Imagenes/blob/main/res_llave_2.png?raw=true)

##Restricciones estructurales  
- Es una notación alternativa a las restricciones de llave (cardinalidad) que incluye un par de números enteros (mín, máx) a cada participación.  

![](https://github.com/miguelillo69/Imagenes/blob/main/res_estructural.png?raw=true)

## Restricciones de participación  
La existencia de una entidad depende de que esté relacionado con otra entidad a través de un tipo de vínculo.  

![](https://github.com/miguelillo69/Imagenes/blob/main/res_parti.png?raw=true)

## Entidades Débiles  
- Una entidad es identificada únicamente por medio de su llave más la llave de la entidad padre.  
  - Un conjunto de entidades padres y de entidades débiles deben participar en una relación uno a muchos (un padre, muchas entidades débiles)  
  - Un conjunto de entidades débiles debe tener participación total en este conjunto de relaciones identificadores (o propietarias).  
  - Se denomina relación identificadora a la relación de un tipo de entidad débil con su propietario.  

![](https://github.com/miguelillo69/Imagenes/blob/main/ent_debiles.png?raw=true)

## Consideraciones de Diseño  
- ¿Debe ser un concepto ser modelado como entidad o como atributo?  
- ¿Debe ser un concepto ser modelado como entidad o como relación?  
- Idenficación de relaciones  
- Restricciones:  
  - Gran parte de la semántica de los datos puede ser capturada  
  - Algunas restricciones no pueden ser capturadas  
  
## Entidad versus Atributos  
- ¿Debiera ser dirección ser un atributo de empleado o una entidad?  
- Depende del uso y semántica:  
  - Si tenemos varias direcciones por empleado, debe ser una entidad  
  - Si la estructura (ciudad, calle, etc) es importante, debe ser modelada como entidad  

## Entidad versus Atributos (2)  
- Trabaja\_en no permite trabajar a un mismo empleado en un departamento por dos o más períodos  

![](https://github.com/miguelillo69/Imagenes/blob/main/ent_versus_atr_2.png?raw=true)

## Entidad versus Atributos (3)  
- El problema es similar al de “dirección” cuando se quiere tener un empleado trabajando en uno o más perídos en un departamento.  

![](https://github.com/miguelillo69/Imagenes/blob/main/ent_versus_atr_3.png?raw=true)

## Entidad versus relación  
- ER está bien si el administrador tiene un presupuesto separado por cada departamento  

![](https://github.com/miguelillo69/Imagenes/blob/main/ent_versus_relacion.png?raw=true)

## Entidad versus relación (2)  
- Ahora, si un administrador recibe un presupuesto para todos sus departamentos  

![](https://github.com/miguelillo69/Imagenes/blob/main/ent_versus_relacion_2.png?raw=true)

## Relaciones Binarias versus Terciarias  
- Si cada póliza pertenece a sólo un empleado, cada dependiente es atado a la póliza y el siguiente ER no es bueno  

![](https://github.com/miguelillo69/Imagenes/blob/main/rel_bin_versus_ter.png?raw=true)

## Relaciones Binarias versus Terciarias (2)  
- Una solución es, donde dos relaciones binarias son mejor que una terciaria.  

![](https://github.com/miguelillo69/Imagenes/blob/main/rel_bin_versus_ter_2.png?raw=true)

## Relaciones Binarias versus Terciarias (3)  
- Puede ocurrir que dos relaciones binarias sean mejor modeladas como una relación terciaria. Ejemplo, una relación de contrato relaciona Partes, Departamentos y Proveedres con una atributo cantidad.  

## Resumen de ER  
- Existen muchos tipos de restricciones de integridad que pueden ser expresados en  
- ER:  
  - Restricciones de claves  
  - Restricciones de participación  
  - Algunas restricciones, en particular, dependencias funcionales no pueden ser expresadas en el modelo ER  
- Modelos ER son subjetivos  
- Esquema relacional resultante debe ser analizado y refinado. Información de dependencias funcionales y técnicas de normalización son muy útiles para ello.  

# Transformación de Modelo Lógico a Modelo Físico

## Descripción

- Cada elemento del modelo lógico se transforma en un elemento del modelo físico. En algunos casos, la transformación es directa, pero en otros se requiere una transformación que mantenga la semántica y la eficiencia.

### Transformación de Entidades

- Una entidad se transforma en una tabla.

### Transformación de Atributos de Entidades

- Cada atributo se convierte en una columna de la tabla correspondiente a la entidad. El identificador único se convierte en clave primaria. Las restricciones asociadas a los atributos pueden implementarse como disparadores si el sistema de gestión de base de datos lo permite.

### Transformación de Relaciones

Según el tipo de correspondencia:

- **Relaciones 1:N**: Se propaga el identificador de la entidad con cardinalidad 1 a la entidad con cardinalidad N.
  - Si es una relación de asociación, la clave propagada es clave ajena.
  - Si es una relación de dependencia, la clave primaria de la tabla correspondiente a la entidad débil se forma con la concatenación de los identificadores de ambas entidades.

- **Relaciones 1:1**: Se propaga la clave en ambas direcciones, intentando capturar la mayor semántica posible y evitando valores nulos.

- **Relaciones de agregación**: Se transforman como relaciones 1:N.

### Transformación de Relaciones Exclusivas

- Después de realizar la transformación según las relaciones 1:N, se debe verificar que sólo una de las claves propagadas es nula en cada ocurrencia.

### Transformación de la Jerarquía

- Existen tres opciones:

  - **Opción A**: Crear una tabla para el supertipo con su identificador como clave primaria, y una tabla para cada subtipo con el identificador del supertipo como clave ajena.

  - **Opción B**: Crear una tabla para cada subtipo, incluyendo los atributos comunes y utilizando el identificador del supertipo como clave primaria.

  - **Opción C**: Agrupar en una tabla todos los atributos del supertipo y los subtipos, añadiendo un atributo discriminante que indique a qué subtipo pertenece cada ocurrencia.

## Notación

### Tabla

- La representación gráfica de una tabla es un rectángulo con una línea horizontal que lo divide en dos partes: la parte superior contiene el nombre de la tabla.

![](https://github.com/miguelillo69/Imagenes/blob/main/tabla.png?raw=true)

### Relación

- La relación entre tablas se representa con una línea que las une, con símbolos en sus extremos que indican la cardinalidad de la relación.

![](https://github.com/miguelillo69/Imagenes/blob/main/relacion.png?raw=true)

## Ejemplo

- Se parte del diagrama entidad-relación sobre conocimientos de técnicos informáticos y su asignación a proyectos.

![](https://github.com/miguelillo69/Imagenes/blob/main/ROMF-ejemplo.png?raw=true)

### Ejemplo de Obtención del Modelo Físico

- El modelo físico muestra que cada entidad se convierte en una tabla con atributos correspondientes. Las tablas adicionales **POSEEN** y **ASIGNACIONES** surgen de las relaciones respectivas.

- **POSEEN** contiene los atributos `grado`, `cod_empresa`, `cod_tecnico`, y `cod_conoc`.
- **ASIGNACIONES** incluye `cod_empresa`, `cod_tecnico`, `cod_proyecto`, `f_asignacion`, y `f_cese`.

- La relación entre **EMPRESAS** y **TÉCNICOS** es 1:N, y se representa adecuadamente en el modelo físico. Las relaciones adicionales se describen de forma similar, con cardinalidades especificadas como (1,N) o (0,N).

- Por ejemplo, en la relación **TÉCNICOS-POSEEN-CONOCIMIENTOS**:
  - Un técnico posee varios conocimientos (1,n).
  - Un conocimiento puede no ser poseído por ningún técnico (0,n).

- Finalmente, en la relación **TÉCNICOS-ASIGNACIONES-PROYECTOS**:
  - Un proyecto puede tener varios técnicos asignados (1,n).
  - Un técnico puede no estar asignado a ningún proyecto en un momento dado (0,n).
