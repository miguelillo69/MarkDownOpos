# Básicos C++

## 1. Estructura Básica de un Programa en C++
> Un programa en C++ normalmente contiene las siguientes partes:

``#include <iostream>``: Incluye la librería estándar para entrada y salida.

``int main()``: Función principal donde comienza la ejecución del programa.

``std::cout``: Se utiliza para imprimir en la consola.

````php
#include <iostream> // Incluye la librería estándar de entrada/salida

int main() {
std::cout << "Hola, Mundo!" << std::endl; // Imprime en consola
return 0; // Termina el programa
}
````
## 2. Variables y Tipos de Datos
> C++ soporta varios tipos de datos básicos como int (enteros), float (decimales), double (decimales de mayor precisión), char (caracteres) y bool (booleanos).

````php
int edad = 25;
float altura = 1.75;
char inicial = 'A';
bool esEstudiante = true;

std::cout << "Edad: " << edad << ", Altura: " << altura << ", Inicial: " << inicial << ", Estudiante: " << esEstudiante << std::endl;
````

## 3. Condicionales y Bucles
> Los condicionales (if, else if, else) y los bucles (for, while, do-while) son fundamentales para el control de flujo.

### Ejemplo de condicional:

````php
int numero = 5;

if (numero > 0) {
std::cout << "El número es positivo." << std::endl;
} else if (numero < 0) {
std::cout << "El número es negativo." << std::endl;
} else {
std::cout << "El número es cero." << std::endl;
}
````

### Ejemplo de bucle for:

````php
for (int i = 1; i <= 5; i++) {
std::cout << "Iteración: " << i << std::endl;
}
````

## 4. Funciones
> Las funciones son bloques de código que realizan tareas específicas y pueden reutilizarse.

````php
int sumar(int a, int b) {
return a + b;
}

int main() {
int resultado = sumar(5, 7);
std::cout << "La suma es: " << resultado << std::endl;
return 0;
}
````

> ``int sumar(int a, int b)``: Define una función que toma dos enteros y devuelve su suma.

## 5. Arreglos y Vectores
> Los arreglos son estructuras de datos que almacenan elementos del mismo tipo. Los vectores son similares pero más flexibles, ya que pueden cambiar de tamaño dinámicamente.

### Ejemplo de arreglo:

````php
int numeros[3] = {1, 2, 3};

for (int i = 0; i < 3; i++) {
std::cout << "Número: " << numeros[i] << std::endl;
}
````

### Ejemplo de vector:

````php
#include <vector> // Librería para usar vectores

std::vector<int> numeros = {1, 2, 3, 4, 5};

numeros.push_back(6); // Añade un número al final

for (int numero : numeros) {
std::cout << "Número: " << numero << std::endl;
}
````

## 6. Clases y Objetos (Programación Orientada a Objetos)
> C++ es un lenguaje orientado a objetos, por lo que es fundamental entender cómo crear y usar clases.

````php
class Persona {
public:
std::string nombre;
int edad;

    void mostrarInfo() {
        std::cout << "Nombre: " << nombre << ", Edad: " << edad << std::endl;
    }
};

int main() {
Persona persona1;
persona1.nombre = "Carlos";
persona1.edad = 30;
persona1.mostrarInfo();

    return 0;
}
````
> ``class Persona``: Define una clase llamada Persona con dos atributos (nombre y edad) y un método (mostrarInfo).
 
## 7. Punteros y Referencias
> Los punteros almacenan direcciones de memoria y las referencias son alias para variables existentes.

### Ejemplo de puntero:

````php
int numero = 10;
int *puntero = &numero; // 'puntero' almacena la dirección de 'numero'

std::cout << "Valor de numero: " << numero << std::endl;
std::cout << "Valor del puntero: " << *puntero << std::endl; // Accede al valor de 'numero' a través del puntero
````

### Ejemplo de referencia:

````php
int a = 10;
int &ref = a; // 'ref' es una referencia a 'a'

ref = 20; // Cambia el valor de 'a' a través de la referencia

std::cout << "Valor de a: " << a << std::endl; // Imprime 20
````

## 8. Manejo de Errores y Excepciones
> C++ permite el manejo de errores mediante excepciones usando try, catch y throw.

````php
#include <iostream>
#include <stdexcept> // Librería para manejo de excepciones

int dividir(int a, int b) {
if (b == 0) {
throw std::invalid_argument("Error: División por cero.");
}
return a / b;
}

int main() {
try {
int resultado = dividir(10, 0);
std::cout << "Resultado: " << resultado << std::endl;
} catch (const std::invalid_argument &e) {
std::cerr << e.what() << std::endl;
}

    return 0;
}
````

## 9. Plantillas (Templates)
> Las plantillas permiten escribir funciones o clases genéricas que pueden trabajar con cualquier tipo de dato.

````php
template <typename T>
T sumar(T a, T b) {
return a + b;
}

int main() {
std::cout << "Suma de enteros: " << sumar(5, 7) << std::endl;
std::cout << "Suma de flotantes: " << sumar(3.5, 2.5) << std::endl;

    return 0;
}
````

## 10. Espacios de Nombres (Namespaces)
> Los espacios de nombres ayudan a evitar conflictos de nombres en programas grandes.

````php
namespace MiEspacio {
int valor = 42;

    void mostrarValor() {
        std::cout << "Valor: " << valor << std::endl;
    }
}

int main() {
MiEspacio::mostrarValor(); // Usa la función dentro del espacio de nombres
return 0;
}
````
# Más C++
> En C++, los operadores básicos se dividen en varias categorías, como operadores aritméticos, de comparación, lógicos, de asignación y bit a bit. A continuación, te muestro cada uno de ellos con ejemplos.

##1. Operadores Aritméticos
> Estos operadores realizan operaciones matemáticas comunes.

``+`` (suma)

``-`` (resta)

``*`` (multiplicación)

``/`` (división)

``%`` (módulo o residuo)

  
#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
int a = 10, b = 3;

    cout << "Suma: " << a + b << endl;           // Suma: 13
    cout << "Resta: " << a - b << endl;          // Resta: 7
    cout << "Multiplicación: " << a * b << endl; // Multiplicación: 30
    cout << "División: " << a / b << endl;       // División: 3 (solo la parte entera)
    cout << "Módulo: " << a % b << endl;         // Módulo: 1

    return 0;
}
````
## 2. Operadores de Comparación
> Estos operadores se utilizan para comparar dos valores.

``==`` (igual a)

``!=`` (diferente de)

``> `` (mayor que)

``< `` (menor que)

``>=`` (mayor o igual que)

``<=`` (menor o igual que)

#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
int x = 5, y = 8;

    cout << "x == y: " << (x == y) << endl;   // x == y: 0 (falso)
    cout << "x != y: " << (x != y) << endl;   // x != y: 1 (verdadero)
    cout << "x > y: " << (x > y) << endl;     // x > y: 0 (falso)
    cout << "x < y: " << (x < y) << endl;     // x < y: 1 (verdadero)
    cout << "x >= y: " << (x >= y) << endl;   // x >= y: 0 (falso)
    cout << "x <= y: " << (x <= y) << endl;   // x <= y: 1 (verdadero)

    return 0;
}
````
## 3. Operadores Lógicos
> Estos operadores se utilizan para combinar expresiones booleanas.

``&&`` (AND lógico)

``||`` (OR lógico)

``!`` (NOT lógico)

## Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
bool a = true, b = false;

    cout << "a && b: " << (a && b) << endl;   // a && b: 0 (falso)
    cout << "a || b: " << (a || b) << endl;   // a || b: 1 (verdadero)
    cout << "!a: " << !a << endl;             // !a: 0 (falso)
    cout << "!b: " << !b << endl;             // !b: 1 (verdadero)

    return 0;
}
````
## 4. Operadores de Asignación
> Se utilizan para asignar valores a las variables.

``=`` (asignación)

``+=`` (suma y asigna)

``-=`` (resta y asigna)

``*=`` (multiplica y asigna)

``/=`` (divide y asigna)

``%=`` (módulo y asigna)

#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    x += 5; // x = x + 5
    cout << "x += 5: " << x << endl; // x += 5: 15

    x -= 3; // x = x - 3
    cout << "x -= 3: " << x << endl; // x -= 3: 12

    x *= 2; // x = x * 2
    cout << "x *= 2: " << x << endl; // x *= 2: 24

    x /= 4; // x = x / 4
    cout << "x /= 4: " << x << endl; // x /= 4: 6

    x %= 2; // x = x % 2
    cout << "x %= 2: " << x << endl; // x %= 2: 0

    return 0;
}
````

## 5. Operadores Bit a Bit (Bitwise)
> Se utilizan para manipular bits individuales en números enteros.

``&`` (AND bit a bit)

``|`` (OR bit a bit)

``^`` (XOR bit a bit)

``~`` (NOT bit a bit)

``<<`` (desplazamiento a la izquierda)

``>>`` (desplazamiento a la derecha)

#### Ejemplo:
````php
#include <iostream>
using namespace std;

int main() {
int a = 5;   // 0101 en binario
int b = 3;   // 0011 en binario

    cout << "a & b: " << (a & b) << endl;  // a & b: 1  (0001 en binario)
    cout << "a | b: " << (a | b) << endl;  // a | b: 7  (0111 en binario)
    cout << "a ^ b: " << (a ^ b) << endl;  // a ^ b: 6  (0110 en binario)
    cout << "~a: " << (~a) << endl;        // ~a: -6 (complemento a uno)
    cout << "a << 1: " << (a << 1) << endl; // a << 1: 10 (desplazamiento a la izquierda)
    cout << "a >> 1: " << (a >> 1) << endl; // a >> 1: 2 (desplazamiento a la derecha)

    return 0;
}
````

## 6. Operadores de Incremento y Decremento
> Se utilizan para aumentar o disminuir el valor de una variable en 1.

``++`` (incremento)

``--`` (decremento)

#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
int a = 5;

    cout << "a++: " << a++ << endl; // a++: 5 (luego de esto, a es 6)
    cout << "++a: " << ++a << endl; // ++a: 7

    cout << "a--: " << a-- << endl; // a--: 7 (luego de esto, a es 6)
    cout << "--a: " << --a << endl; // --a: 5

    return 0;
}
````
# Métodos de String en C++
## 1. length() o size()
> Devuelve el número de caracteres en la cadena.

````php
#include <iostream>
#include <string>
int main() {
std::string texto = "Hola Mundo";
std::cout << "La longitud de la cadena es: " << texto.length() << std::endl;
std::cout << "La longitud de la cadena es: " << texto.size() << std::endl;
// Salida en consola: La longitud de la cadena es: 10
// Salida en consola: La longitud de la cadena es: 10
return 0;
}
````

## 2. empty()
> Verifica si la cadena está vacía.

````php
#include <iostream>
#include <string>

int main() {
std::string texto = "";
if (texto.empty()) {
std::cout << "La cadena está vacía." << std::endl;
} else {
std::cout << "La cadena no está vacía." << std::endl;
}
// Salida en consola: La cadena está vacía.
return 0;
}
````

## 3. append()
> Añade una cadena al final de otra.

````php
#include <iostream>
#include <string>

int main() {
std::string saludo = "Hola";
saludo.append(" Mundo");
std::cout << saludo << std::endl; // Salida: Hola Mundo
return 0;
}
````

## 4. substr()
> Devuelve un sub-string de la cadena a partir de una posición dada y de una longitud específica.

````php
#include <iostream>
#include <string>

int main() {
std::string texto = "Hola Mundo";
std::string subTexto = texto.substr(5, 5); // Desde posición 5, toma 5 caracteres
std::cout << subTexto << std::endl; // Salida: Mundo
return 0;
}
````

## 5. find()
> Busca una subcadena dentro de la cadena y devuelve la posición de la primera ocurrencia. Devuelve std::string::npos si no se encuentra.

````php
#include <iostream>
#include <string>

int main() {
std::string texto = "Hola Mundo";
size_t posicion = texto.find("Mundo");
if (posicion != std::string::npos) {
std::cout << "La palabra 'Mundo' se encuentra en la posición: " << posicion << std::endl;
} else {
std::cout << "La palabra 'Mundo' no se encuentra en la cadena." << std::endl;
}
// Salida consola: La palabra 'Mundo' se encuentra en la posición: 5

return 0;
}
````

## 6. replace()
> Reemplaza parte de la cadena con otra subcadena.
````php
#include <iostream>
#include <string>

int main() {
std::string texto = "Hola Mundo";
texto.replace(5, 5, "Amigo"); // Desde posición 5, reemplaza 5 caracteres por "Amigo"
std::cout << texto << std::endl; // Salida: Hola Amigo
return 0;
}
````

## 7. erase()
> Elimina parte de la cadena.

````php
#include <iostream>
#include <string>

int main() {
std::string texto = "Hola Mundo";
texto.erase(5, 5); // Elimina 5 caracteres desde la posición 5
std::cout << texto << std::endl; // Salida: Hola
return 0;
}
````

## 8. insert()
> Inserta una cadena en una posición específica.

````php
#include <iostream>
#include <string>

int main() {
std::string texto = "Hola Mundo";
texto.insert(5, "querido "); // Inserta "querido " en la posición 5
std::cout << texto << std::endl; // Salida: Hola querido Mundo
return 0;
}
````

## 9. at()
> Devuelve una referencia al carácter en una posición específica.

````php
#include <iostream>
#include <string>

int main() {
std::string texto = "Hola Mundo";
char letra = texto.at(5); // Obtiene el carácter en la posición 5
std::cout << "El carácter en la posición 5 es: " << letra << std::endl; // Salida: El carácter en la posición 5 es: M
// Salida en consola: El carácter en la posición 5 es: M

return 0;
}
````

## 10. c_str()
> Devuelve un puntero const char* al contenido de la cadena.
````php
#include <iostream>
#include <string>

int main() {
std::string texto = "Hola Mundo";
const char* cstr = texto.c_str();
std::cout << "La cadena como c-string es: " << cstr << std::endl;
// Salida en consola: La cadena como c-string es: Hola Mundo

return 0;
}
````

## 11. compare()
> Compara dos cadenas lexicográficamente.

````php
#include <iostream>
#include <string>

int main() {
std::string texto1 = "Hola";
std::string texto2 = "Mundo";

    int resultado = texto1.compare(texto2);

    if (resultado == 0) {
        std::cout << "Las cadenas son iguales." << std::endl;
    } else if (resultado < 0) {
        std::cout << "La primera cadena es menor que la segunda." << std::endl;
    } else {
        std::cout << "La primera cadena es mayor que la segunda." << std::endl;
    }
    
   // Salida en consola: La primera cadena es menor que la segunda.

    return 0;
}
````
> En C++, además de las funciones de manipulación de cadenas de texto (std::string), hay muchos otros métodos y funciones estándar que se utilizan frecuentemente.

## 1. Métodos de la Biblioteca <vector>
> La clase std::vector es parte de la Biblioteca Estándar de C++ y se usa para almacenar colecciones de elementos de manera dinámica.

``push_back``: Añade un elemento al final del vector.

``pop_back``: Elimina el último elemento del vector.

``size``: Devuelve el número de elementos en el vector.

``clear``: Elimina todos los elementos del vector.

``empty``: Verifica si el vector está vacío.

``at``: Accede al elemento en la posición indicada, con verificación de límites.

````php
#include <iostream>
#include <vector>

int main() {
std::vector<int> numeros;

    // Agregar elementos al vector
    numeros.push_back(10);
    numeros.push_back(20);
    numeros.push_back(30);

    // Mostrar tamaño del vector
    std::cout << "Tamaño del vector: " << numeros.size() << std::endl;
    //Salida en consola: Tamaño del vector: 3
    
    // Acceder a un elemento usando at
    std::cout << "Elemento en la posición 1: " << numeros.at(1) << std::endl;
    //Salida en consola: Elemento en la posición 1: 20
    
    // Eliminar el último elemento
    numeros.pop_back();
    std::cout << "Tamaño del vector después de pop_back: " << numeros.size() << std::endl;
    //Salida en consola: Tamaño del vector después de pop_back: 2
    
    // Limpiar el vector
    numeros.clear();
    std::cout << "¿El vector está vacío? " << (numeros.empty() ? "Sí" : "No") << std::endl;
    //Salida en consola: ¿El vector está vacío? Sí
    
    return 0;
}
````

## 2. Métodos de la Biblioteca <algorithm>
> La biblioteca <algorithm> proporciona una variedad de algoritmos estándar que pueden aplicarse a contenedores, como ordenación, búsqueda, manipulación de secuencias, entre otros.

``std::sort:`` Ordena los elementos en un rango.

``std::find:`` Busca un elemento en un rango.

``std::reverse:`` Invierte el orden de los elementos en un rango.

``std::max_element:`` Encuentra el elemento máximo en un rango.

``std::min_element:`` Encuentra el elemento mínimo en un rango.

````php
#include <iostream>
#include <vector>
#include <algorithm> // Incluye los algoritmos

int main() {
std::vector<int> numeros = {3, 1, 4, 1, 5, 9, 2};

    // Ordenar el vector
    std::sort(numeros.begin(), numeros.end());
    std::cout << "Vector ordenado: ";
    for (int n : numeros) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    // salida en consola: Vector ordenado: 1 1 2 3 4 5 9 

    // Buscar un elemento
    auto it = std::find(numeros.begin(), numeros.end(), 5);
    if (it != numeros.end()) {
        std::cout << "Elemento 5 encontrado en la posición: " << std::distance(numeros.begin(), it) << std::endl;
    } else {
        std::cout << "Elemento 5 no encontrado." << std::endl;
    }
   
    // salida en consola: Elemento 5 encontrado en la posición: 5


    // Invertir el vector
    std::reverse(numeros.begin(), numeros.end());
    std::cout << "Vector invertido: ";
    for (int n : numeros) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
   
    // salida en consola: Vector invertido: 9 5 4 3 2 1 1 


    // Encontrar el máximo y mínimo
    auto max_it = std::max_element(numeros.begin(), numeros.end());
    auto min_it = std::min_element(numeros.begin(), numeros.end());
    std::cout << "Elemento máximo: " << *max_it << ", Elemento mínimo: " << *min_it << std::endl;
    // salida en consola: Elemento máximo: 9, Elemento mínimo: 1

    return 0;
}
````

## 3. Métodos de la Biblioteca <map>
> La clase std::map es un contenedor de pares clave-valor, donde cada clave es única.

``insert``: Inserta un par clave-valor en el mapa.

``erase``: Elimina un elemento por clave o por iterador.

``find``: Busca un elemento por clave.

``size``: Devuelve el número de elementos en el mapa.

``clear``: Elimina todos los elementos del mapa.

````php
#include <iostream>
#include <map>
#include <string>

int main() {
std::map<std::string, int> edad;

    // Insertar elementos
    edad.insert({"Juan", 25});
    edad["Ana"] = 30;
    edad["Luis"] = 20;

    // Mostrar el tamaño del mapa
    std::cout << "Tamaño del mapa: " << edad.size() << std::endl;
    // Salida en consola: Tamaño del mapa: 3
     
    // Buscar un elemento
    auto it = edad.find("Ana");
    if (it != edad.end()) {
        std::cout << "Edad de Ana: " << it->second << std::endl;
    } else {
        std::cout << "Ana no está en el mapa." << std::endl;
    }
    // Salida en consola: Edad de Ana: 30

    // Eliminar un elemento
    edad.erase("Luis");
    std::cout << "Tamaño del mapa después de eliminar a Luis: " << edad.size() << std::endl;
    // Salida en consola: Tamaño del mapa después de eliminar a Luis: 2

    // Limpiar el mapa
    edad.clear();
    std::cout << "¿El mapa está vacío? " << (edad.empty() ? "Sí" : "No") << std::endl;
    // Salida en consola: ¿El mapa está vacío? Sí

    return 0;
}
````
## 4. Métodos de la Biblioteca <queue>
> La clase std::queue es un contenedor que implementa una cola (FIFO).

``push``: Inserta un elemento al final de la cola.

``pop``: Elimina el primer elemento de la cola.

``front``: Devuelve una referencia al primer elemento de la cola.

``back``: Devuelve una referencia al último elemento de la cola.

``empty``: Verifica si la cola está vacía.

``size``: Devuelve el número de elementos en la cola.

````php
#include <iostream>
#include <queue>

int main() {
std::queue<int> cola;

    // Agregar elementos a la cola
    cola.push(1);
    cola.push(2);
    cola.push(3);

    // Mostrar el primer y último elemento
    std::cout << "Primer elemento: " << cola.front() << std::endl;
    std::cout << "Último elemento: " << cola.back() << std::endl;
    // Salida en consola: Primer elemento: 1
                          Último elemento: 3

    // Eliminar el primer elemento
    cola.pop();
    std::cout << "Primer elemento después de pop: " << cola.front() << std::endl;
    // Salida en consola: Primer elemento después de pop: 2

    // Verificar si la cola está vacía
    std::cout << "¿La cola está vacía? " << (cola.empty() ? "Sí" : "No") << std::endl;
    // Salida en consola: ¿La cola está vacía? No

    return 0;
}
````
# Condicionales en C++
> Los condicionales permiten que el programa tome decisiones basadas en ciertas condiciones. En C++, las estructuras condicionales principales son if, else if, else y switch.
### if, else if, else

``if``: Evalúa una condición y ejecuta el bloque de código correspondiente si la condición es verdadera.

``else if``: Se utiliza para verificar múltiples condiciones.

``else``: Se ejecuta si ninguna de las condiciones anteriores es verdadera.

#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
int edad = 18;

    if (edad < 13) {
        cout << "Eres un niño." << endl;
    } else if (edad >= 13 && edad < 18) {
        cout << "Eres un adolescente." << endl;
    } else {
        cout << "Eres un adulto." << endl;
    }
    // Salida en consola: Eres un adulto.

    return 0;
}
````

> En este ejemplo, si la variable edad es menor que 13, se imprime "Eres un niño". Si está entre 13 y 17, se imprime "Eres un adolescente". De lo contrario, se imprime "Eres un adulto".

### switch
``switch``: Evalúa el valor de una expresión y ejecuta el bloque de código correspondiente al valor coincidente.

#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
int dia = 3;

    switch (dia) {
        case 1:
            cout << "Lunes" << endl;
            break;
        case 2:
            cout << "Martes" << endl;
            break;
        case 3:
            cout << "Miércoles" << endl;
            break;
        default:
            cout << "Día no válido" << endl;
            break;
    }
    // Salida en consola: Miércoles

    return 0;
}
````

> En este ejemplo, el valor de dia es 3, por lo que se imprimirá "Miércoles". El bloque default se ejecuta si ningún caso coincide.

# Bucles en C++
> Los bucles permiten ejecutar repetidamente un bloque de código mientras se cumpla una condición.

## for
``for``: Se utiliza cuando se sabe de antemano cuántas veces se debe ejecutar el bloque de código.

#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
for (int i = 1; i <= 5; i++) {
cout << "Iteración " << i << endl;
}
// Salida en consola:  Iteración 1
                       Iteración 2
                       Iteración 3
                       Iteración 4
                       Iteración 5

    return 0;
}
````

> En este ejemplo, el bucle for imprime "Iteración" seguido del número de iteración, cinco veces.

## while
``while``: Se utiliza cuando no se sabe cuántas veces se debe ejecutar el bloque de código, pero se necesita iterar mientras se cumpla una condición.

#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
int contador = 1;

    while (contador <= 5) {
        cout << "Contador: " << contador << endl;
        contador++;
    }
    // Salida en consola: Contador: 1
                          Contador: 2
                          Contador: 3
                          Contador: 4
                          Contador: 5

    return 0;
}
````

> En este ejemplo, el bucle while continúa ejecutándose mientras la variable contador sea menor o igual a 5.

## do-while
``do-while``: Es similar al while, pero siempre ejecuta el bloque de código al menos una vez, ya que la condición se evalúa al final del bucle.

#### Ejemplo:

````php
#include <iostream>
using namespace std;

int main() {
int numero = 1;

    do {
        cout << "Número: " << numero << endl;
        numero++;
    } while (numero <= 5);
    
    // Salida en consola: Número: 1
                          Número: 2
                          Número: 3
                          Número: 4
                          Número: 5

    return 0;
}
````

> En este ejemplo, el bucle do-while ejecuta el bloque de código al menos una vez, incluso si la condición es falsa desde el principio.

#### Resumen de Uso

> Condicionales (if, else if, else, switch): Utilizados para tomar decisiones basadas en condiciones.

> Bucles (for, while, do-while): Utilizados para ejecutar repetidamente un bloque de código hasta que se cumpla una condición específica.