# Chuleta de Comandos del Editor de Texto ``VI`` en Linux
## Modos de vi
+ Modo de Comando (Normal Mode): Es el modo por defecto al abrir vi. Permite navegar y realizar operaciones de edición.
+ Modo de Inserción (Insert Mode): Permite insertar texto.
+ Modo de Línea de Comandos (Command-Line Mode): Se accede presionando : para ejecutar comandos como guardar, salir, etc.

## Navegación Básica
|Comando|	Descripción|
|:-----:|:------------:|
|h	|Mueve el cursor a la izquierda.|
|j	|Mueve el cursor hacia abajo.|
|k	|Mueve el cursor hacia arriba.|
|l	|Mueve el cursor a la derecha.|
|w	|Mueve el cursor al inicio de la siguiente palabra.|
|b	|Mueve el cursor al inicio de la palabra anterior.|
|e	|Mueve el cursor al final de la palabra actual.|
|0 (cero)	|Mueve el cursor al inicio de la línea actual.|
|$	|Mueve el cursor al final de la línea actual.|
|G	|Mueve el cursor al final del documento.|
|gg	|Mueve el cursor al inicio del documento.|
|Ctrl + f	|Avanza una página.|
|Ctrl + b	|Retrocede una página.|

## Modo de Inserción
> Para entrar en el modo de inserción, usa uno de los siguientes comandos:

|Comando|	Descripción|
|:-----:|:------------:|
|i	|Inserta texto antes del cursor.|
|I	|Inserta texto al inicio de la línea actual.|
|a	|Añade texto después del cursor.|
|A	|Añade texto al final de la línea actual.|
|o	|Inserta una nueva línea debajo de la línea actual.|
|O	|Inserta una nueva línea encima de la línea actual.|

> Para salir del modo de inserción y volver al modo de comando, presiona Esc.

## Guardado y Salida
|Comando|	Descripción|
|:-----:|:------------:|
|:w	|Guarda el archivo.|
|:q	|Sale de vi.|
|:wq	|Guarda y sale del editor.|
|:q!	|Fuerza la salida sin guardar cambios.|
|:w nombre_archivo	|Guarda el archivo con un nuevo nombre.|

## Edición de Texto
|Comando|	Descripción|
|:-----:|:------------:|
|x	|Elimina el carácter en la posición del cursor.|
|X	|Elimina el carácter antes del cursor.|
|dw	|Elimina desde el cursor hasta el final de la palabra.|
|dd	|Elimina la línea actual.|
|d$	|Elimina desde el cursor hasta el final de la línea.|
|d0	|Elimina desde el cursor hasta el inicio de la línea.|
|u	|Deshace la última acción.|
|Ctrl + r	|Rehace la última acción deshecha.|
|yy	|Copia (yank) la línea actual.|
|p	|Pega el texto copiado después del cursor.|
|P	|Pega el texto copiado antes del cursor.|
|cw	|Cambia la palabra desde el cursor.|
|r	|Reemplaza un solo carácter.|

## Buscar y Reemplazar
|Comando|	Descripción|
|:-----:|:------------:|
|/texto	|Busca texto hacia adelante en el documento.|
|?texto	|Busca texto hacia atrás en el documento.|
|n	|Repite la búsqueda en la misma dirección.|
|N	|Repite la búsqueda en la dirección opuesta.|
|:%s/viejo/nuevo/g	|Reemplaza todas las ocurrencias de viejo por nuevo.|
|:%s/viejo/nuevo/gc	|Reemplaza con confirmación todas las ocurrencias de viejo por nuevo.|

## Otras Funciones Útiles
|Comando|	Descripción|
|:-----:|:------------:|
|.	|Repite la última acción realizada.|
|J	|Une la línea actual con la siguiente.|
|Ctrl + g	|Muestra el número de la línea actual y el estado del archivo.|
|:set nu	|Muestra los números de línea.|
|:set nonu	|Oculta los números de línea.|
|:!comando	|Ejecuta un comando de shell (por ejemplo, :!ls para listar archivos).|