## 1. **Introducción a los patrones de diseño**

**Patrones de diseño:** soluciones habituales a problemas que ocurren con frecuencia en el diseño de software. No es una porción específica de código, sino un concepto general para resolver un problema particular. Puedes seguir los detalles del patrón e implementar una solución que encaje con las realidades de tu propio programa.

## 2. **Historia**

El concepto de los patrones fue descrito por Christopher Alexander en [El lenguaje de patrones](https://refactoring.guru/es/pattern-language-book), y la idea fue recogida por 4 autores: Erich Gamma, John Vlissides, Ralph Johnson y Richard Helm. En 1995, publicaron [Patrones de diseño](https://refactoring.guru/es/design-patterns), en el que aplicaron el concepto de los patrones de diseño a la programación. El libro presentaba 23 patrones que resolvían varios problemas del diseño OO y se convirtió en un éxito de ventas con rapidez. Al tener un título tan largo en inglés, la gente empezó a llamarlo “el libro de la ‘gang of four’ (banda de los cuatro)”, lo que pronto se abrevió a “el libro GoF”.

## 3. **Clasificación de los patrones**  
- A. **patrones creacionales:** proporcionan mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización de código existente.  
- B. **patrones estructurales:** explican cómo ensamblar objetos y clases en estructuras \+ grandes a la vez q se mantiene la flexibilidad y eficiencia d la estructura.  
- C. **patrones de comportamiento** se encargan de una comunicación efectiva y la asignación de responsabilidades entre objetos.

## 4. **Patrones creacionales FAB-PS**

- A. **Factory Method (Objetos superclase)**

  - Proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán.

- B. **Abstract Factory (Sin especificar clases)**

  - permite producir familias de objetos relacionados sin especificar sus clases concretas.

- C. **Builder (Construir objetos complejos paso a paso)**

  - Nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.

- D. **Prototype (Copiar objetos sin dependencia de código)**

  - Nos permite copiar objetos existentes sin que el código dependa de sus clases.

- E. **Singleton (Solo 1 instancia)**

  - Nos permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia.

## 5. **Patrones estructurales \- ABCD-FP**

- A. **Adapter (Adaptar interfaces entre objetos para colaboración)**

  - Permite la colaboración entre objetos con interfaces incompatibles.

- B. **Bridge (Divide clases en dos jerarquías que se desarrollan indep)**

  - Permite dividir una clase grande, o un grupo de clases estrechamente relacionadas, en dos jerarquías separadas (abstracción e implementación) que pueden desarrollarse independientemente la una de la otra.

- C. **Composite (Componer objetos en árbol y trabajar como si indiv.)**

  - Permite componer objetos en estructuras de árbol y trabajar con esas estructuras como si fueran objetos individuales.

- D. **Decorator (Añadir funcionalidades dinámicamente)**

  - Permite añadir funcionalidades a objetos colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.

- E. **Facade (Interfaz simplificada)**

  - Proporciona una interfaz simplificada a una biblioteca, un framework o cualquier otro grupo complejo de clases.

- F. **Flyweight (+ objetos dentro de memoria al compartir común)**

  - Permite mantener más objetos dentro de la cantidad disponible de RAM compartiendo las partes comunes del estado entre varios objetos en lugar de mantener toda la información en cada objeto.

- G. **Proxy (controlar acceso a otro objeto)**

  - Permite proporcionar un sustituto o marcador de posición para otro objeto. Un proxy controla el acceso al objeto original, permitiéndote hacer algo antes o después de que la solicitud llegue al objeto original.

## 6. **Patrones de comportamiento CIMOS-TV**

- A. **Chain of Responsibility (Cadena de solicitudes)**

  - Permite pasar solicitudes a lo largo de una cadena de manejadores. Al recibir una solicitud, cada manejador decide si la procesa o si la pasa al siguiente manejador de la cadena.

- B. **Command (Convierte solicitud en objeto con la información)**

  - Convierte una solicitud en un objeto independiente que contiene toda la información sobre la solicitud. Esta transformación te permite parametrizar los métodos con diferentes solicitudes, retrasar o poner en cola la ejecución de una solicitud y soportar operaciones que no se pueden realizar.

- C. **Iterator (Iterar sobre objeto sin exponer representación)**

  - Permite recorrer elementos de una colección sin exponer su representación subyacente (lista, pila, árbol, etc.).

- D. **Mediator (Reduce dependencias entre objetos)**

  - Permite reducir las dependencias caóticas entre objetos. El patrón restringe las comunicaciones directas entre los objetos, forzándolos a colaborar únicamente a través de un objeto mediador.

- E. **Memento (Guarda y restaura estado sin revelar implementación)**

  - Permite guardar y restaurar el estado previo de un objeto sin revelar los detalles de su implementación.

- F. **Observer (Notifica a varios objetos cuando ocurre evento)**

  - Permite definir un mecanismo de suscripción para notificar a varios objetos sobre cualquier evento que le suceda al objeto que están observando.

- G. **State (Cambia comportamiento al cambiar estado)**

  - Permite a un objeto alterar su comportamiento cuando su estado interno cambia. Parece como si el objeto cambiara su clase

- H. **Strategy (Familia de algoritmos para casos concretos)**

  - Permite definir una familia de algoritmos, colocar cada uno de ellos en una clase separada y hacer sus objetos intercambiables.

- I. **Template Method**

  - Define el esqueleto de un algoritmo en la superclase pero permite que las subclases sobrescriban pasos del algoritmo sin cambiar su estructura.

- J. **Visitor**

  - Permite separar algoritmos de los objetos sobre los que operan