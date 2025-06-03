# C# Cheatsheet

## 1. Tipos de Datos

| Tipo Primitivo | Tamaño      | Ejemplo           |
| -------------- | ------------ | ----------------- |
| string         | 2 bytes/char | s = "referencia"; |
| bool           | N/A          | b = true;         |
| char           | 2 bytes      | ch = 'a';         |
| byte           | 1 byte       | b = 0x78;         |
| short          | 2 bytes      | val = 70;         |
| int            | 4 bytes      | val = 700;        |
| long           | 8 bytes      | val = 70;         |
| float          | 4 bytes      | val = 70.0F;      |
| double         | 8 bytes      | val = 70.0D;      |
| decimal        | 16 bytes     | val = 70.0M;      |

## 2. Arrays (Arreglos)

### 2.1 Declaración

````java
// Inicializado usando una lista definida con llaves
int[] nombreArray = { 100, 101, 102 };

// Definir un array vacío
int[] nombreArray = new int[3];

// Para acceder a un elemento específico del array
int[] nombreArray = new int[10];
int primerNumero = nombreArray[0];
nombreArray[1] = 20;

// Arrays multidimensionales
int[,] matriz = new int[2, 2];
matriz[0, 0] = 1;
matriz[0, 1] = 2;
matriz[1, 0] = 3;
matriz[1, 1] = 4;

int[,] matrizPredefinida = new int[2, 2] { { 1, 2 }, { 3, 4 } };
````

### 2.2 Operaciones con Arrays

````java
// Ordenar en orden ascendente
Array.Sort(nombreArray);

// Ordenar desde el elemento 6 y ordenar 20 elementos
Array.Sort(nombreArray, 6, 20);

// Usar 1 array como clave y ordenar 2 arrays
string[] valores = { "Juan", "Victor", "Elena" };
string[] claves = { "Jimenez", "Martin", "Ortiz" };
Array.Sort(claves, valores);

// Limpiar elementos en el array (array, primer elemento, # elementos)
Array.Clear(nombreArray, 0, nombreArray.Length);

// Copiar elementos de un array a otro
Array.Copy(origen, destino, numElementos);
````

## 3. Operaciones con Cadenas de Texto

````java
// Para concatenar entre cadenas, usa el operador de suma:
string nombre = "Erin";
string apellido = "Roger";
string nombreCompleto = nombre + " " + apellido;

// Para agregar una cadena a otra, usa el operador +=:
string segundoApellido = "Green";
nombreCompleto += segundoApellido;

// Función ToString
Object.ToString();

// Formateo de cadenas
String.Format(String formato, Object arg0);

// Subcadena
String.Substring(comienzo);
String.Substring(comienzo, longitud);

// Reemplazar
string nuevaCadena = viejaCadena.Replace("viejo", "nuevo");

// IndexOf (índice de)
String.IndexOf(valor, inicio, cantidad);
````

## 4. System.Text.StringBuilder

````java
// Constructor
StringBuilder sb = new StringBuilder();
StringBuilder sb = new StringBuilder(miCadena);
StringBuilder sb = new StringBuilder(miCadena, capacidad);
````

## 5. DateTime

````java
// Constructor DateTime
DateTime nuevoAño = DateTime.Parse("1/1/2018");
DateTime fechaActual = DateTime.Now;
DateTime proximoAño = DateTime.Now.AddYears(1);
````

## 6. TimeSpan

````java
// Constructor TimeSpan
TimeSpan intervalo = new TimeSpan(10, 14, 50);
TimeSpan horasIntervalo = TimeSpan.FromDays(3640);
````

## 7. Formateo de Valores

| Formato | Nombre      | Patrón  | Valor  | Resultado |
| ------- | ----------- | -------- | ------ | --------- |
| C       | Moneda      | {0:C2}   | 1000.1 | $ 1000.1  |
| D       | Decimal     | {0:D5}   | 30     | 00030     |
| E       | Exponencial | {0,9:E2} | 120.2  | 1.20+E002 |
| F       | Punto fijo  | {0,9:F2} | 120.2  | 120.2     |
| G       | General     | {0,9:G2} | 120.2  | 120.2     |
| N       | Número     | {0,9:N1} | 1300.5 | 1,300.5   |
| P       | Porcentaje  | {0,9:P3} | 0.0903 | 9.03%     |
| R       | Redondeo    | {0,9:R}  | 3.1416 | 3.1416    |
| X       | Hexadecimal | {0,9:X4} | 31     | 001f      |

## 8. Compilador de C# en la Línea de Comandos

````bash
csc Archivo.cs -> Compila Archivo.cs produciendo Archivo.exe
csc -target:library Archivo.cs -> Compila Archivo.cs produciendo Archivo.dll
csc -out:MiPrograma.exe Archivo.cs -> Compila Archivo.cs y crea MiPrograma.exe
csc -define:DEBUG -optimize -out:Archivo2.exe *.cs
csc -target:library -out:Archivo2.dll -warn:0 -nologo -debug *.cs
csc -target:library -out:Algo.xyz *.cs
````

### 8.1 Opciones del Compilador

| Opción             | Propósito                                                    |
| ------------------- | ------------------------------------------------------------- |
| @                   | Lee un archivo de respuesta con más opciones.                |
| -?                  | Muestra un mensaje de uso en la consola.                      |
| -additionalfile     | Nombra archivos adicionales que pueden usar los analizadores. |
| -addmodule          | Vincula los módulos especificados a este ensamblado.         |
| -analyzer           | Ejecuta los analizadores desde este ensamblado.               |
| -appconfig          | Especifica la ubicación de app.config.                       |
| -baseaddress        | Especifica la dirección base.                                |
| -checksumalgorithm  | Especifica el algoritmo de suma de verificación.             |
| -codepage           | Especifica la página de códigos utilizada.                  |
| -define             | Define símbolos de preprocesador.                            |
| -delaysign          | Firmar ensamblado con una clave pública.                     |
| -deterministic      | Hacer que la salida sea determinista.                         |
| -doc                | Generar un archivo de documentación XML.                     |
| -errorlog           | Especifica el archivo de registro de errores.                 |
| -filealign          | Especifica la alineación del archivo.                        |
| -fullpaths          | Especifica rutas completas en mensajes de error.              |
| -langversion        | Define la versión del lenguaje.                              |
| -lib                | Especifica directorios de búsqueda de metadatos.             |
| -link               | Vincula el archivo de ensamblado especificado.                |
| -main               | Especifica la clase con el punto de entrada principal.        |
| -moduleassemblyname | Especifica el nombre del ensamblado del módulo.              |
| -modulename         | Especifica el nombre del módulo del ensamblado.              |
| -nostdlib           | No importar bibliotecas estándar.                            |
| -nowarn             | Suprime las advertencias especificadas.                       |
| -nologo             | No mostrar banner de inicio.                                  |
| -optimize           | Habilitar optimizaciones.                                     |
| -out                | Especifica el nombre del archivo de salida.                   |
| -parallel           | Habilitar compilación en paralelo.                           |
| -pathmap            | Mapea nombres de archivos de origen a rutas.                  |
| -platform           | Especifica la plataforma de destino (x86, x64, etc.).         |
| -preferreduilang    | Especifica el idioma preferido.                               |
| -recurse            | Incluir archivos con el patrón especificado.                 |
| -reference          | Importa metadatos de un archivo especificado.                 |
| -refout             | Especifica el archivo de salida de referencia.                |
| -reportanalyzer     | Informa sobre el rendimiento del analizador.                  |
| -resource           | Incrusta un recurso gestionado.                               |
| -ruleset            | Especifica el archivo de conjunto de reglas.                  |
| -subsystemversion   | Especifica la versión del subsistema.                        |
| -target             | Especifica el tipo de compilación (exe, library, etc.)       |
| -unsafe             | Permite código inseguro.                                     |
| -warn               | Define el nivel de advertencia (0-4).                         |
| -warnaserror        | Tratar advertencias como errores.                             |

## 9. Herencia y Clases

````java
public class ClaseBase {
 public void MetodoBase() {
     Console.WriteLine("Este es un método base.");
 }
}

public class ClaseDerivada : ClaseBase {
  public void MetodoDerivado() {
      Console.WriteLine("Este es un método derivado.");
  }
}
````

## 10. Interfaces

````java
interface IMiInterface {
    void MetodoInterface();
}

public class MiClase : IMiInterface {
    public void MetodoInterface() {
        Console.WriteLine("Implementación de Método de Interface.");
    }
}
````

## 11. Manejo de Excepciones

````java
try {
    // Código que puede lanzar una excepción.
}catch (Exception ex) {
        Console.WriteLine($"Excepción capturada: {ex.Message}");
}finally {
    // Código que siempre se ejecutará.
}
````

## 12. Delegados y Eventos

````java
// Declaración de un delegado
public delegate void MiDelegado(string mensaje);

// Uso de un delegado
MiDelegado delegadoEjemplo = Console.WriteLine;
delegadoEjemplo("Hola, Delegado!");

// Declaración de un evento
public event MiDelegado EventoEjemplo;

// Suscripción a un evento
EventoEjemplo += delegadoEjemplo;
EventoEjemplo("Evento lanzado!");
````
