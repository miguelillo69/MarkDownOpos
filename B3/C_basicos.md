# Chuleta de Lenguaje C
## 1. Estructura Básica de un Programa en C
````php
#include <stdio.h>  // Biblioteca estándar de entrada/salida

int main() {
printf("Hola, mundo!\n");  // Imprime en consola
return 0;  // Indica que el programa terminó correctamente
}
````

### Salida de Consola:
````yaml
Hola, mundo!
````
## 2. Tipos de Datos Básicos

| Tipo  | Descripción  | Ejemplo de Declaración |
|:-----:|:------------:|:----------------------:|
| int   | Enteros      | int edad = 25;         |
|   float    |      Números de punto flotante        |            float altura = 1.75;            |
|   char    |     Caracteres         |        char letra = 'A';                |
|  double     |       Números de doble precisión       |         double pi = 3.1416;               |
 
## 3. Entrada y Salida de Datos
   Salida: ``printf``

   Entrada: ``scanf``
````php
#include <stdio.h>

int main() {
int numero;
printf("Introduce un número: ");
scanf("%d", &numero);  // Lee un número entero
printf("El número introducido es: %d\n", numero);
return 0;
}
````

### Salida de Consola:
````yaml
Introduce un número: 5
El número introducido es: 5
````

## 4. Operadores Básicos
````yaml
   Aritméticos: +, -, *, /, %
   Relacionales: ==, !=, >, <, >=, <=
   Lógicos: && (AND), || (OR), ! (NOT)
````

## 5. Estructuras de Control
### Condicionales:
````php
#include <stdio.h>

int main() {
int edad = 18;
if (edad >= 18) {
printf("Eres mayor de edad.\n");
} else {
printf("Eres menor de edad.\n");
}
return 0;
}
````

### Salida de Consola:

````yaml
Eres mayor de edad.
````

## Bucles:
### while Loop:
````php
#include <stdio.h>

int main() {
int i = 1;
while (i <= 5) {
printf("%d\n", i);
i++;
}
return 0;
}
````
### Salida de Consola:

````yaml
1
2
3
4
5
````

### for Loop:

````php
#include <stdio.h>

int main() {
for (int i = 1; i <= 5; i++) {
printf("%d\n", i);
}
return 0;
}
````

### Salida de Consola:

````yaml
1
2
3
4
5
````

## 6. Funciones
`````php
#include <stdio.h>

// Declaración de la función
int suma(int a, int b) {
return a + b;
}

int main() {
int resultado = suma(5, 3);
printf("La suma es: %d\n", resultado);
return 0;
}
`````

### Salida de Consola:
````yaml
La suma es: 8
````

## 7. Arreglos
````php
#include <stdio.h>

int main() {
int numeros[3] = {1, 2, 3};
printf("El primer número es: %d\n", numeros[0]);  // Accede al primer elemento
return 0;
}
````

### Salida de Consola:
````yaml
El primer número es: 1
````
## 8. Punteros
````php
#include <stdio.h>

int main() {
int x = 10;
int *ptr = &x;  // Puntero que almacena la dirección de `x`
printf("El valor de x es: %d\n", *ptr);  // Desreferenciación del puntero
return 0;
}
````

### Salida de Consola:
````yaml
El valor de x es: 10
````
## 9. Estructuras
````php
#include <stdio.h>

struct Persona {
char nombre[50];
int edad;
};

int main() {
struct Persona persona1 = {"Juan", 30};
printf("Nombre: %s, Edad: %d\n", persona1.nombre, persona1.edad);
return 0;
}
````

### Salida de Consola:
````yaml
Nombre: Juan, Edad: 30
````
