## `javax.json.stream` - Resumen

El paquete `javax.json.stream` forma parte de la API de procesamiento de JSON en Java (Java API for JSON Processing, o **JSON-P**). Este paquete proporciona un **API de bajo nivel** para procesar JSON de manera eficiente utilizando el enfoque de **streaming** (flujo de datos).

### Principales Interfaces en `javax.json.stream`

1. **`JsonParser`**
    - Proporciona una forma de **analizar** un flujo de datos JSON secuencialmente.
    - Permite leer y procesar eventos JSON como **inicio de objetos**, **final de objetos**, **inicio de arreglos**, etc.
    - Los eventos se obtienen utilizando el método `next()`.

2. **`JsonGenerator`**
    - Ofrece una forma de **escribir** datos JSON secuencialmente.
    - Se utiliza para generar (o construir) JSON de manera eficiente, controlando directamente el flujo de salida.
    - Proporciona métodos como `writeStartObject()`, `writeEndObject()`, `writeStartArray()`, y `writeEndArray()`.

3. **`JsonParserFactory`**
    - Proporciona un método para crear instancias de `JsonParser`.
    - Permite configurar cómo se comportará el `JsonParser` durante el análisis.

4. **`JsonGeneratorFactory`**
    - Proporciona un método para crear instancias de `JsonGenerator`.
    - Permite configurar cómo se comportará el `JsonGenerator` durante la generación de JSON.
    
5. **`JsonLocation`**
   - Proporciona información sobre la **ubicación** del token JSON actual dentro del flujo de entrada.
   - Se utiliza principalmente con `JsonParser` para obtener detalles como el número de línea, columna y offset del carácter actual en el documento JSON.
   - Útil para depurar errores o manejar excepciones durante el análisis de JSON.

### Uso de las Interfaces

Estas interfaces son útiles para trabajar con grandes volúmenes de datos JSON o para aplicaciones en las que se requiere una **mayor eficiencia** en el manejo de JSON, dado que el enfoque de streaming consume menos memoria que el modelo de documento completo.

#### Ejemplo de Uso: `JsonParser`

```java
JsonParser parser = Json.createParser(new StringReader("{\"name\":\"John\"}"));
while (parser.hasNext()) {
    JsonParser.Event event = parser.next();
    if (event == JsonParser.Event.KEY_NAME) {
        JsonLocation location = parser.getLocation();
        System.out.println("Clave encontrada en línea: " + location.getLineNumber());
    }
}
parser.close();
```

#### Ejemplo de Uso: `JsonGenerator`
````java
JsonGenerator generator = Json.createGenerator(System.out);
        generator.writeStartObject()
        .write("name", "John")
        .writeEnd()
        .close();
````


