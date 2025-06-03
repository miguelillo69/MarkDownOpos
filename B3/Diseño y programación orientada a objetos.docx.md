# **La Programación Orientada a Objetos (OOP)**

- Paradigma de programación en el que los conceptos del mundo real, como los objetos y las interacciones, se representan mediante clases y objetos en el código. Ayuda a modularizar y estructurar el código, facilitando su mantenimiento y ampliación

## **Objetos**

- Instancias d clases. Encapsulan datos para el objeto y funciones para manipular estos datos. Representan entidades con estado y comportamientos específicos.

## **Clases**

- Plantillas para crear objetos. Definen atributos (características) y métodos (comportamientos). Proporcionan estructura y definen lo q un objeto puede hacer, pero no son el objeto en sí.

## **Herencia**

- Mecanismo q permite q una clase herede atributos y métodos d otra clase, permitiendo reutilización d código y estableciendo una relación de tipo "es un". Facilita la modularidad y la escalabilidad al compartir código común entre clases.

## **Métodos**

- Funciones definidas dentro de una clase que operan en datos encapsulados dentro de esa clase. Permiten a objetos realizar acciones e interactuar con otros objetos.

## **Polimorfismo en tiempo de compilación (Sobrecarga)**

- Capacidad d 1 clase d tener múltiples métodos con \= nombre pero con \!= params. Aumenta la flexibilidad d una clase al permitir diferentes formas de interactuar con ella.

## **Polimorfismo en tiempo de ejecución (Anulación)**

- Capacidad d objeto d subclase d ser tratado como objeto d superclase.  
Se utiliza en herencia y anulación d métodos (donde 1 método en 1 subclase tiene \= nombre y tipo de retorno q 1 método en superclase, pero con implementación diferente).

## **Encapsulación**

- Mecanismo q restringe acceso directo a algunos componentes d 1 objeto y protege la integridad dl mismo. Garantiza q el comportamiento interno d un objeto esté oculto.

## **Características principales de la encapsulación:**

- A. **Agrupación de Datos y Comportamiento:** los atributos y métodos que actúa sobre los atributos se agrupan en un solo bloque llamado clase.  
- B. **Control de Acceso:** Modificadores de acceso (`private`, `protected` y `public`), controlan visibilidad y accesibilidad de atributos y métodos d clase.   
- C. **Protección de Datos:** Se puede evitar el acceso o modificación no deseada de los datos internos de un objeto. Para ello, se proporcionan métodos públicos (**getters** y **setters**). Así, cualquier modificación o acceso a esos datos puede ser controlado y validado a través de esos métodos.  

## **Ventajas**  

- A. **Modularidad:** El código se organiza en bloques (clases) que representan objetos del mundo real. Permite un desarrollo y mantenimiento más sencillos.  
- B. **Reutilización de código (Herencia):** Una clase (hija) puede heredar características de otra clase (padre), lo que evita la repetición de código.  
- C. **Extensibilidad:** Es más fácil agregar nuevas características a un sistema basado en POO debido a la herencia y la sobrecarga de métodos.  
- D. **Mantenibilidad:** Debido a encapsulación, si se necesita cambiar funcionamiento 1 objeto, solo se modifica ese objeto sin afectar a otros.  
- E. **Abstracción:** Permite al programador enfocarse en las interacciones de alto nivel, ocultando los detalles de bajo nivel.  
- F. **Polimorfismo:** Permite que una sola interfaz represente diferentes tipos de datos, lo que facilita la escritura de código genérico.  
- G. **Encapsulación:** Agrupa datos (atributos) y métodos que actúan sobre esos datos en una sola unidad, ocultando la implementación interna y mostrando solo lo necesario al mundo exterior.

## **Inconvenientes**  
- A. **Complejidad:** POO puede introducir complejidad adicional en el diseño.  
- B. **Rendimiento:** creación y gestión d objetos puede consumir \+ memoria y recursos q procedimientos tradicionales. Aunque las diferencias d rendimiento son menores con hardware moderno, en aplicaciones críticas de rendimiento, la sobrecarga de la POO podría ser un problema.  
- C. **Tamaño del código:** POO a menudo puede llevar a un código \+ largo debido a la necesidad de definir clases y métodos.  
- D. **No siempre es la mejor opción:** Aunque la POO es poderosa, no siempre es la mejor elección para todas las aplicaciones o problemas. En algunos casos, un enfoque más funcional o procedimental puede ser más adecuado.