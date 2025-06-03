# Raids

## 1. **Introducción**

- Proteger y almacenar tus datos es una prioridad para todos, desde los particulares hasta las grandes empresas. Un
  método popular de almacenamiento de datos es el uso de **RAID** or **Matriz redundante de discos independientes**.
- Duplica los datos y los almacena en varios discos duros
  o [unidades de estado sólido (SSD)](https://recoverit.wondershare.es/hard-drive/what-is-a-solid-state-drive.html).
- Esta redundancia te protege si una de las unidades se estropea o falla, ya que seguirás teniendo los mismos datos
  almacenados en otras unidades.
- Hay varios niveles o métodos diferentes de RAID, y no todos están orientados a proporcionar redundancia o duplicar tus
  datos.

## 2. **¿Cómo funciona el RAID?**

- Aunque el RAID almacena los datos en discos diferentes, está espaciado lógicamente para que se superponga
  perfectamente, de modo que el sistema operativo pueda leer los datos de cada uno de los discos simultáneamente.
- Esto no sólo hace que el almacenamiento de tus datos sea más seguro, sino que también mejora el rendimiento, ya que
  cada unidad trabaja conjuntamente y aumenta el tiempo medio entre fallos.
- Desde el punto de vista del sistema operativo, los datos no tienen fisuras y aparecen como una sola unidad.
- Funciona porque el método RAID lógico utiliza la duplicación de discos para duplicar los datos en varias unidades.
- El espacio de almacenamiento de cada unidad se divide en grupos más pequeños, cuyo tamaño oscila entre 512 bytes y
  varios megabytes cada uno.

## 3. **Niveles RAID**

### ``Niveles estándar``

- ## ``RAID 0``
    - [RAID 0](https://recoverit.wondershare.com/windows-tips/what-is-raid-0.html) es el tipo más básico de RAID y
      requiere un mínimo de dos unidades.
    - Se centra en la separación o distribución “stripping” de los datos en cada una de las unidades disponibles.
    - El RAID 0 funciona creando bloques de datos y almacenándolos en todas las unidades.
    - Por ejemplo, si trabajas en un proyecto con muchos datos, como la edición de video, el RAID 0 es la mejor opción.
    - Sin embargo, no es recomendable si trabajas con datos sensibles o críticos, porque basta con que falle una de las
      unidades para que pierdas todos tus datos.
    - ### ``Pros``
        - Alto rendimiento en la lectura y escritura de datos
        - Fácil de configurar y utilizar
    - ### ``Contras``
        - Si falla una unidad, se pierden todos los datos

![](https://www.muycomputer.com/wp-content/uploads/2014/03/461px-Raid0.png)

- ## ``RAID 1``
    - [RAID 1](https://recoverit.wondershare.es/windows-tips/what-is-raid-1.html) se utiliza para reflejar “mirroring”
      los bloques de datos en ambos conjuntos de unidades. Si una de las unidades no funciona correctamente o se
      bloquea, el controlador puede acceder a la versión espejo, y el programa seguirá funcionando sin problemas, y no
      experimentarás ninguna pérdida de datos. Las dos unidades pueden leerse simultáneamente, lo que da lugar a un alto
      rendimiento de lectura. No hay ningún cambio en el rendimiento de escritura porque, aunque las dos unidades se
      lean a la vez, sigue teniendo que escribir los datos varias veces. El RAID 1 es el más adecuado para almacenar
      datos críticos, ya que funciona como una eficaz herramienta de almacenamiento de copias de seguridad.
- ### ``Pros``
    - Alta velocidad de lectura y escritura de datos
    - Funciona como una copia de seguridad de los datos. Si una unidad se estropea, puedes reconstruir rápidamente el
      conjunto
- ### ``Contras``
    - Más costoso, ya que requiere el doble de unidades de disco
    - Diseñado para trabajar con sólo dos unidades, lo que puede limitar la cantidad de almacenamiento a la que puedes
      acceder

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Raid1.png/250px-Raid1.png)

- ## ``RAID 5``

    - [RAID 5](https://recoverit.wondershare.es/windows-tips/what-is-raid-5.html) es el nivel RAID más común. Necesitas
      entre 3 y 16 unidades para que funcione correctamente.
    - El nivel se centra en la separación de datos con paridad, que proporciona la redundancia.
    - En lugar de reflejar los datos de las unidades, utiliza un algoritmo avanzado para crear bloques virtuales basados
      en los datos de la unidad.
    - Para simplificar, si miras la siguiente ecuación "5+x+4=10, sabes que x=1.
    - Del mismo modo, si una de las unidades de disco falla o no se carga correctamente, el RAID 5 puede resolver la X y
      reconstruir los datos que faltan.
    - Funciona con paridad simple, así que mientras no tengas varios fallos en las unidades, deberías estar bien.

    - ### ``Pros``

        - Lee los datos con extrema rapidez
        - No perderás ningún dato si una de las unidades falla

    - ### ``Contras``

        - La escritura de datos es un poco más lenta ya que debe. Más calcular la paridad
        - Es una tecnología muy compleja y sustituir un disco defectuoso puede llevar mucho tiempo.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Raid5.png/1200px-Raid5.png)

- ## ``RAID 6``

    - [RAID 6](https://recoverit.wondershare.es/windows-tips/what-is-raid-6.html) es una versión mejorada del RAID 5\.
    - La principal mejora es que funciona con doble paridad.
    - Necesitarás al menos cuatro unidades disponibles, dos con los datos originales y las otras dos para la paridad.
      Una matriz RAID 6 puede sobrevivir a dos fallos de disco simultáneos sin ninguna pérdida de datos.
    - El RAID 6 es un sistema de almacenamiento eficaz con un alto rendimiento y una seguridad de primer orden. Sin
      embargo, necesitarás espacio para servidores adicionales.

    - ### ``Pros``

        - La lectura de datos es muy rápida
        - Puede soportar dos fallos de disco simultáneos sin perder ningún dato.

    - ### ``Contras``

        - Rendimiento de escritura más lento que el RAID 5 debido a la doble paridad
        - Un mayor número de unidades aumenta las probabilidades de fallo de las mismas

![](https://upload.wikimedia.org/wikipedia/commons/6/68/Raid6.png)

### ``Niveles anidados``

> Los niveles RAID anidados combinan dos de las funcionalidades RAID mencionadas anteriormente (striping, mirroring y paridad) en una única matriz

- ## `` RAID 01 (0+1)``

    - Combina la duplicación de los datos con la división en franjas para obtener una única matriz que pueda replicar y
      compartir los datos entre las unidades.
    - Necesitas al menos cuatro unidades para ejecutar el nivel RAID 01, y la mitad de ellas se utilizan para duplicar
      datos.

    - ### ``Pros``

        - Puedes soportar un fallo de la unidad de disco sin ninguna consecuencia. Los datos se almacenan en otra
          unidad.

    - ### ``Contras``

        - Es una forma costosa de crear redundancia, ya que utilizas la mitad de los servidores para la duplicación

![](https://upload.wikimedia.org/wikipedia/commons/a/ad/RAID_01.svg)

- ## `` RAID 10 (1+0) ``

    - La combinación de RAID 0 y RAID 1 aumenta la seguridad, de la que carece el RAID 0\.
    - Refleja los datos en un conjunto secundario de unidades, a la vez que los separa en cada una de ellas para
      aumentar la velocidad de las transferencias de datos.
    - La principal diferencia entre [RAID 10](https://recoverit.wondershare.es/windows-tips/what-is-raid-10.html)
      y RAID 01 es el orden de funcionamiento.
    - En este nivel, los datos son una franja de espejos en lugar de reflejar las franjas.

    - ### ``Pros``

    - Puedes soportar un fallo de la unidad de disco sin ninguna consecuencia. Los datos se almacenan en otra unidad.

    - ### ``Contras``

    - Es una forma costosa de crear redundancia, ya que utilizas la mitad de los servidores para la duplicación

![](https://upload.wikimedia.org/wikipedia/commons/b/bb/RAID_10.svg)

- ## ``RAID 50 (5+0)``

    - La matriz RAID 50 requiere al menos 6 unidades. Combina la división en bandas del RAID 0 con la paridad de una
      sola unidad del RAID 5\.
    - Con este tipo de matriz, puedes perder hasta una unidad de cada una sin que se pierdan datos. Por ejemplo, si
      tienes cuatro conjuntos de discos, puedes perder hasta 4 discos a la vez, siempre que formen parte de un conjunto
      diferente. La pérdida de un par de unidades coincidentes provocará la pérdida de datos.
    - La configuración RAID 50 mejora el rendimiento del RAID 5 en cuanto a una escritura más rápida y una mayor
      tolerancia a los fallos de las unidades deficientes.

    - ### ``Pros``

        - Rendimiento de lectura más rápido
        - Un mayor nivel de seguridad de los datos sin aumentar los costos
        - Mejora del flujo de datos y de la redundancia

    - ### ``Contras``

        - Si dos de los servidores RAID 5 fallan al mismo tiempo, todo el conjunto dejará de funcionar

![](https://upload.wikimedia.org/wikipedia/commons/9/9d/RAID_50.png)

### ``Otros sistemas RAID menos utilizados``

- ## ``RAID 3``

    - RAID 3 utiliza "striping" para distribuir datos entre varias unidades, pero dedica una unidad específica para
      almacenar la información de paridad.
    - Esta unidad de paridad se utiliza para calcular la información de corrección de errores en caso de fallo de una de
      las unidades de datos.  
      Buena tolerancia a fallos.
    - Puede tolerar la pérdida de una unidad, pero la unidad de paridad se convierte en un cuello de botella de
      rendimiento, ya que todas las operaciones de escritura deben pasar por ella.

    - ### ``Pros`` 
      - Proporciona un alto rendimiento para lecturas secuenciales debido al "striping" de datos, aunque las
        escrituras suelen ser más lentas debido a la necesidad de calcular la paridad.
    - ### ``Contras`` RAID 3 
      - Es menos eficiente en términos de rendimiento de escritura y capacidad de almacenamiento debido a
        la dedicación de una unidad completa para almacenar paridad. 
      - Además, la presencia de la unidad de paridad como un
        único punto de fallo puede limitar la escalabilidad y redundancia del sistema.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/RAID_3.svg/2560px-RAID_3.svg.png)

- ## ``Cantidad mínima de discos por sistema:``

| Nivel de RAID | Cantidad mínima de discos |
| ----- | ----- |
| RAID 0 | 2 |
| RAID 1 | 2 |
| RAID 2 | 3 |
| RAID 3 | 3 |
| RAID 4 | 3 |
| RAID 5 | 3 |
| RAID 6 | 4 |
| RAID 10 | 4 |
| RAID 01 | 4 |
| RAID 50 | 6 |
| RAID 60 | 8 |

