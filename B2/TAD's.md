# Tipos Abstractos de Datos (TADs)

## Concepto

Un ``Tipo Abstracto de Datos (TAD)`` es una agrupación de datos (simples o compuestos) junto con las operaciones
asociadas, que permite modelar el comportamiento de una entidad real. Es clave en la Programación Orientada a Objetos y
se basa en la ``abstracción de datos``.

### Características principales:

- ``Ocultamiento``: El usuario sabe qué puede hacer el TAD, pero no cómo está implementado.
- ``Encapsulamiento``: Protege las características internas del TAD.
- ``Compilación separada``: Permite usar TADs como si fueran elementos predefinidos en el lenguaje de programación.

---

# TAD Pila de Números Enteros

## Concepto

Una ``pila`` es una estructura de datos de tipo ``LIFO`` (*Last Input First Output*). El último elemento en entrar es el
primero en salir.

## Modelo gráfico

![](img/pilas.png)

## Especificaciones

| Operación            | Especificación semántica                                         | Especificación sintáctica                               |
|-----------------------|-------------------------------------------------------------------|---------------------------------------------------------|
| inicializarPila      | Deja lista la pila para operar sobre ella                         | `void inicializarPila()`                                 |
| apilar               | Incorpora un elemento en la cima                                  | `void apilar(int x)`                                     |
| desapilar            | Elimina y devuelve el elemento de la cima                         | `int desapilar()`                                        |
| pilaVacia            | Devuelve `true` si la pila está vacía, `false` en caso contrario  | `boolean pilaVacia()`                                    |
| leerPila             | Carga inicial de elementos                                        | `void leerPila() throws NumberFormatException, IOException` |
| imprimirPila         | Muestra el contenido de la pila                                   | `void imprimirPila()`                                    |
| numElemPila          | Devuelve el número de elementos en la pila                        | `int numElemPila()`                                      |
| cima                 | Devuelve el elemento de la cima sin eliminarlo                    | `int cima()`                                             |
| decapitar            | Elimina el elemento de la cima sin devolverlo                     | `void decapitar()`                                       |
| eliminarPila         | Devuelve la pila vacía                                            | `void eliminarPila()`                                    |

---

## Ejemplo básico: uso de la pila

````java
package tadPila;

import java.io.*;

public class PruebaPila1 {
    public static void main(String[] args) {
        Pila p = new TadPila();
        int x;

        p.inicializarPila();
        p.apilar(1);
        p.apilar(2);
        p.apilar(3);
        p.apilar(11);
        p.apilar(15);
        x = p.desapilar();
        System.out.println("x = " + x);
        x = p.desapilar();
        System.out.println("x = " + x);
        p.eliminarPila();
    }
}
````

# TAD Cola de Números Enteros

## Concepto

Una ``cola`` es una estructura de datos de tipo ``FIFO`` (*First Input First Output*). El primer elemento en entrar es
el primero en salir.

## Modelo gráfico

![](img/colas.png)

## Especificaciones

| Operación            | Especificación semántica                                         | Especificación sintáctica                               |
|-----------------------|-------------------------------------------------------------------|---------------------------------------------------------|
| inicializarCola      | Prepara la cola para su uso                                       | `void inicializarCola()`                                 |
| encolar              | Agrega un elemento al final de la cola                            | `void encolar(int x)`                                    |
| desencolar           | Elimina y devuelve el primer elemento                             | `int desencolar()`                                       |
| colaVacia            | Devuelve `true` si la cola está vacía, `false` en caso contrario  | `boolean colaVacia()`                                    |
| leerCola             | Carga inicial de la cola                                          | `void leerCola() throws NumberFormatException, IOException` |
| imprimirCola         | Muestra el contenido de la cola                                   | `void imprimirCola()`                                    |
| invertirCola         | Devuelve la cola con sus elementos invertidos                     | `void invertirCola()`                                    |
| numElemCola          | Devuelve el número de elementos en la cola                        | `int numElemCola()`                                      |
| primero              | Devuelve el primer elemento sin eliminarlo                        | `int primero()`                                          |
| quitarPrimero        | Elimina el primer elemento sin devolverlo                         | `void quitarPrimero()`                                   |
| eliminarCola         | Deja la cola vacía                                                | `void eliminarCola()`                                    |

---

## Ejemplo básico: uso de la cola

````java
package tadCola;

public class PruebaCola1 {
    public static void main(String[] args) {
        Cola cola1 = new TadCola();
        int elem;

        cola1.inicializarCola();
        cola1.encolar(8);
        cola1.encolar(7);
        cola1.encolar(9);
        cola1.encolar(11);
        elem = cola1.desencolar();
        elem = cola1.desencolar();
        System.out.println("Acaba de salir el número " + elem);
        cola1.eliminarCola();
    }
}

````

> Estos conceptos forman la base para entender cómo implementar y usar las estructuras de datos fundamentales en programación, como pilas y colas, a través de los TADs.

## Ejemplos de algoritmos básicos

### Invertir los elementos de una pila

````java
static void invertir(Pila pila){
        int elem;
        if(!pila.pilaVacia()){
        elem=pila.desapilar();
        invertir(pila);
        sumergir(pila,elem);
        }
        }

````

### Invertir los elementos de una cola

````java
static void invertir(Cola cola){
        int elem;
        if(!cola.colaVacia()){
        elem=cola.desencolar();
        invertir(cola);
        cola.encolar(elem);
        }
        }

````

## Escribir el contenido de una pila en pantalla

El método `escribirPila` consiste en vaciar la pila (``desapilar``) durante la fase de "ida" de la recursividad. Una vez
que se alcanza la base de la recursión (pila vacía), durante la fase de "vuelta" se restauran los elementos en su orden
original.

### Algoritmo

````java
static void escribirPila (Pila pila) {
    int elem;
    if (!pila.pilaVacia()) {
        elem = pila.desapilar();
        System.out.println(elem);
        escribirPila(pila);
        pila.apilar(elem);
    }
}
````

### Paso a paso del algoritmo
- Verificar si la pila está vacía.
  - Si la pila está vacía, no se hace nada y se retorna.

- Desapilar el elemento superior.
  - Se guarda en la variable elem.

- Imprimir el elemento desapilado.
  - Muestra en pantalla el elemento actual.

- Llamada recursiva.
  - Llama a escribirPila para procesar el resto de la pila.

- Apilar nuevamente el elemento.
  - Una vez que se regresa de la recursión, se apila el elemento guardado para restaurar la pila en su estado original.

### Ejemplo de ejecución
#### Supongamos que la pila tiene los siguientes elementos (de arriba hacia abajo):

````java
Cima
5
3
7
2
Fondo
````

### Ejecución del método:
````yaml
Salida por pantalla:
5
3
7
2
````

### Después de la ejecución del método, la pila queda restaurada a su estado inicial:

````java
Cima
5
3
7
2
Fondo
````
