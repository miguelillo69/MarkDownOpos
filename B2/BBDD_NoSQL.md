# Bases de datos NoSQL

## Orígenes
- **Carlo Strozzi** usó el término NoSQL (1998).
- **Eric Evans** (de Rackspace) reintrodujo el término para bases de datos no relacionales y distribuidas que no garantizaban ACID.

## Características de las bases de datos NoSQL
- No utilizan SQL como lenguaje de consultas (aunque no se "prohíbe").
    - Algunos tipos utilizan JSON, GQL, etc.
- No utilizan estructuras fijas como tablas para el almacenamiento, proporcionando un esquema de datos flexible.
- No permiten operaciones *Join* debido al gran volumen de datos.
- Emplean una arquitectura distribuida con alta disponibilidad y escalabilidad horizontal.
- No hay un modelo de datos único. Son **no relacionales** y no siguen un modelo entidad-relación.
- Suelen no garantizar las propiedades del modelo ACID.
- Utilizan otros formatos como **clave-valor**, mapeo de columnas o grafos en lugar de tablas.
- Una columna en NoSQL es un "campo".

## Ventajas
- Se ejecutan en máquinas con pocos recursos y, por lo tanto, de menor coste.
- Alta escalabilidad horizontal: para mejorar el rendimiento solo hace falta añadir más nodos.
- Manejan grandes cantidades de datos (data sheets).
- No generan cuellos de botella.
- Escalamiento sencillo y diseño simple.

## Inconvenientes
- Falta de estándares.
- Gestionar el esquema de la base de datos puede ser complejo.
- Dificultades en la administración de la base de datos.
- Existen funcionalidades que no están implementadas.
- Falta de madurez y soporte por parte de los fabricantes.
- Falta de especialistas y curva de aprendizaje.
- Es complicado determinar cuál es la mejor opción.
- Las transacciones ACID y las sentencias *JOIN* son típicas de las bases de datos relacionales y difíciles de implementar con NoSQL.

## Tipos de bases de datos NoSQL

### Clave-valor
- Cada elemento se asocia con una clave única, lo que permite la recuperación de la información de forma muy rápida.
- La información habitualmente se almacena como un objeto binario (BLOB).
- Muy eficientes tanto para las lecturas como para las escrituras.
- **Ejemplos**: Cassandra, BigTable, HBase, BerkeleyDB, Riak, Redis.

### Documentales
- Almacena la información como un documento, generalmente con una estructura simple como JSON o XML y clave única para cada registro.
- Permite búsquedas por clave-valor y consultas más avanzadas.
- Más versátiles.
- **Ejemplos**: MongoDB, CouchDB, Marklogic.

### Columnares
- Almacenan los datos como columnas en lugar de filas.
- Útil para datos no estructurados y semiestructurados.
- Basadas en el concepto de agregado, cada agregado se identifica por una clave.
- **Ejemplos**: MonetDB, Vertica, Cassandra, HBase, Amazon SimpleDB.

### Orientadas a objetos
- La información se representa mediante objetos, de la misma forma que en los lenguajes de programación orientada a objetos (POO).
- **Ejemplos**: Zope, Gemstone, Db4o.

### Orientadas a grafos
- La información se representa como nodos de un grafo y sus relaciones con las aristas del mismo.
- Navegación más eficiente entre relaciones que en el modelo relacional.
- Útil para dominios con múltiples y complejas interrelaciones entre los datos.
- **Ejemplos**: Neo4j, InfoGrid, Virtuoso.

### Bases de datos multimodelo
- Soportan múltiples modelos de datos.
- **Ejemplos**: ArangoDB, OrientDB, gunDB.

## Más Ejemplos de Bases de Datos NoSQL

### Clave/Valor
- Cassandra (Apache), BigTable (Google), Dynamo (Amazon), Project Voldemort (LinkedIn), Riak, Redis.
- Otros: Azure Table Storage, Aerospike, LevelDB, RocksDB, Berkeley DB, GenieDB, BangDB, entre muchos más.

### Documentales
- CouchDB (Apache), MongoDB (10gen), RavenDB (Hibernating Rhinos).
- Otros: Elastic, Cloud Datastore, Azure DocumentDB, RethinkDB, ToroDB, etc.

### Grafos
- Neo4j (Cypher), DEX/Sparksee, AllegroGraph, OrientDB, InfiniteGraph, entre otros.

### Multivalor
- Rocket D3 DBMS, Rocket mvBase DBMS, Rocket U2 Universe, Rocket U2 Unidata, OpenQM, Caché InterSystems, Reality, Jbase, entre otros.

### Orientadas a objetos
- ObjectDB, Zope Object Database, db4o, GemStone S, Objectivity/DB, Realm.io, entre otros.

### Tabular
- HBase (Apache), BigTable (Google), LevelDB, Hypertable, Hadoop Distributions (MapR, Hortonworks, Cloudera), Cassandra, entre otros.

### Arrays
- SciDB (Paradigm4).
- Otros: Globals, Intersystems Cache, GT.M, rasdaman, DaggerDB.

### Time Series / Streaming Databases
- Axibase, kdb+, quasardb, Riak TS, Informix Time Series Solution, InfluxData, PipelineDB, eXtremeDB, Akumuli, etc.

## Ejemplos adicionales

- **CouchDB**: Uso de RESTful HTTP API como interfaz y JavaScript como principal lenguaje de interacción. Utiliza archivos JSON para el almacenamiento de datos. Permite la creación de vistas y operaciones *JOIN*.
- **Cassandra**: Clave-Valor CQL (Cassandra Query Language). Aplicación Java que puede ejecutarse en cualquier plataforma con la JVM.
- **HBase**: Distribuida, persistente, dispersa y ordenada en un mapa multidimensional. Se sustenta en el sistema de archivos de Hadoop.
- **MongoDB** (2009): Escrito en C++, C y JavaScript para búsquedas. Utiliza BSON (una evolución de JSON).

## Apache Hadoop
- Framework de software que soporta aplicaciones distribuidas bajo una licencia libre.
- Permite a las aplicaciones trabajar con miles de nodos y petabytes de datos.
- Inspirado en los documentos de Google para MapReduce y Google File System (GFS).
- **MapReduce**: Modelo de programación para computación paralela sobre grandes colecciones de datos en grupos de computadoras.
