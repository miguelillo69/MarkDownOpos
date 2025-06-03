# REDES LOCALES
## Concepto
- Una red de ordenadores es un conjunto de equipos o PC's conectados entre sí, cuya finalidad principal es compartir recursos.
- Las redes se pueden clasificar por el alcance, es decir por él área de actuación.
## Red Área Local (LAN)
### DEFINICIÓN. 
- LAN (Local Area Network) conjunto de elementos físicos y lógicos que proporcionan interconexión entre dispositivos en un área privada y restringida.
   - Restricción Geográfica: Depende de la tecnología con que esté construida (el ámbito de una oficina, una planta de un edificio, un edificio entero,…)
   - Velocidad de transmisión: Es relativamente elevada
   - Privacidad:Toda la red pertenece a la misma organización
   - Fiabilidad de transmisión: La tasa de error debe ser muy baja
### FUNCIÓN PRINCIPAL
- Que los ordenadores de la red puedan compartir recursos entre todos los usuarios autorizados del sistema, mediante el intercambio de tramas de datos entre los distintos equipos conectados a la línea de transmisión.

![](https://github.com/miguelillo69/Imagenes/blob/main/lan.png?raw=true)
   
## Red de Área Extensa (WAN)
### DEFINICIÓN.
- WAN (Wide Area Network). Red que intercomunica equipos en un área geográfica muy amplia.
  - Las líneas de comunicación que utiliza son líneas públicas
  propiedad de las compañías telefónicas.
  - Estas líneas son compartidas simultáneamente por muchos usuarios mediante técnicas de multiplexación.
  La multiplexación es una técnica utilizada en comunicaciones. Se hace convivir en un canal señales procedentes de emisores distintos y con destino en un conjunto de receptores también distintos. Se comparte un canal físico estableciendo sobre él varios canales lógicos.
  - Su capacidad de transmisión suele ser menor que las utilizadas en las redes LAN.
- Son compartidas por muchos usuarios a la vez, lo que exige un acuerdo en los modos de transmisión y en las normas de interconexión a la red.
  - La tasa de error en las transmisiones son mayores (unas mil veces) que su equivalente en las redes LAN.

![](https://github.com/miguelillo69/Imagenes/blob/main/red-WAN.jpg?raw=true)
## Otras Redes
- Existen otras redes que no son propiamente locales o extensas, pero se relacionan con ellas de forma directa.
  - Redes Metropolitanas (MAN)
  - Redes de área personal (PAN)
  - Redes inalámbricas.

## REDES METROPOLITANAS (MAN)
- Red de distribución de datos para un área geográfica en el entorno de una ciudad.
- Su tasa de error (proporción entre los bits erróneos y los bits
  transmitidos) no llega a tener las limitaciones de las redes WAN,
  aunque están por encima de la tasa de una red LAN.
- Un máximo de 50km de diámetro.
## REDES PERSONALES (PAN)
- Configuración de acceso a la red muy sencilla o automática.
- Radio de acción geográficamente limitado.
- Medio de transmisión preferentemente inalámbrico.
- Costes de instalación y de explotación de la red pequeños.
## REDES INALÁMBRICAS
- Comodidad de una instalación sin cables junto con el descenso significativo de los costes de fabricación.
- Exponen una mayor superficie de ataque por ser su medio de transmisión aéreo y, por lo tanto, abierto a cualquier dispositivo que se encuentre en las cercanías.
- Puesto que el canal de transmisión es compartido por todas la estaciones de trabajo, se tiene que multiplexar la señal repartiendo el ancho de banda.
## TECNOLOGÍAS INALÁMBRICAS.
- **Bluetooth** e infrarrojos para bajas tasas de transferencia.
- **Wi-Fi** para redes de área local.
- **WiMAX** para redes metropolitanas.
## Estándares y Asociaciones
- Los estándares son necesarios para acordar el modo en que se llevará a cabo la comunicación, tanto en el nivel físico como en el lógico.
- Existen unas normas para los fabricantes que indican qué requisitos deben cumplir sus equipos.
- Los estándares pueden ser de dos tipos:
  - Estándar de facto o de hecho:
    - Estándar aceptado en el mercado por su uso generalizado.
  - Estándar de iure o de derecho:
    - Estándar creado por una asociación de estándares que se propone a los fabricantes para que diseñen sus equipos de acuerdo con la norma recomendada.
## Organización de una LAN
- La organización de una red de área local consiste en un conjunto ordenado de protocolos de comunicación.
- Los protocolos operan sobre una topología bien definida.
- La topología les indica cómo se conectan los ordenadores de la red.
  - **Host o nodo**: cada equipo con capacidad de interactuar en red.
  - Los ordenadores que pertenecen a la red pueden tener las funciones-  siguientes:
    - **Ser cliente**: Ordenador de la red que se aprovecha de los servicios que le brinda un servidor.
    - **Ser servidor**: Ordenador encargado de ofrecer unos servicios al resto de la red.
  - Por el **tipo de brindar servicios**, la red puede ser:
  
## RED CLIENTE-SERVIDOR
- Los servidores suelen estar dedicados.
- Cumplen sólo la función prevista para ellos: la de proporcionar uno o varios servicios.

![](https://github.com/miguelillo69/Imagenes/blob/main/diagrama-cliente-servidor.png?raw=true)
  
## REDES ENTRE IGUALES (Peer to Peer)
- El Sistema Operativo de red puede actuar como cliente y como servidor simultáneamente.
- Cada nodo de la red puede ser cliente con respecto de un servicio que le provee otro nodo.
  Y puede ser servidor con respecto de otros clientes de la red que se benefician de sus servicios.
- Los servidores suelen ser no dedicados.
- El servidor es un puesto más de la red con posibilidad de ejecutar aplicaciones de usuario desde su consola. Aunque esto disminuye su rendimiento como servidor.

![](https://github.com/miguelillo69/Imagenes/blob/main/p2p.png?raw=true)

## Topologías
- La topología de la red es la propiedad que indica la forma física de la red, es decir, el modo en que se disponen los equipos y el sistema de cableado que los interconecta para cumplir su función.

![](https://github.com/miguelillo69/Imagenes/blob/main/topologias-de-red-1.jpg?raw=true)

### TOPOLOGÍA EN ESTRELLA
- Las estaciones se conectan entre sí a través de un nodo especialmente privilegiado que ocupa la posición central de la red, formando con el resto de las estaciones una estrella.
- Al nodo central se le denomina estación concentradora de la estrella.

![](https://github.com/miguelillo69/Imagenes/blob/main/estrella.png?raw=true) 

#### VENTAJA:
- La seguridad, el concentrador tiene las funciones de intercomunicar y aislar los problemas. Si un segmento se deteriora, sólo él se queda sin el servicio de red.
#### INCONVENIENTE:
- Todos los segmentos terminan en el concentrador, lo que conlleva

### TOPOLOGÍA EN ANILLO
- Todos los equipos de la red se conectan en torno a un anillo físico.
 
![](https://github.com/miguelillo69/Imagenes/blob/main/anillo.png?raw=true)

#### VENTAJA:
- No presenta problemas de congestión de tráfico.
#### INCONVENIENTE:
- Una rotura del anillo produce el fallo general de la red.
  
### TOPOLOGÍA EN BUS
- Los equipos se conectan a una única línea de transmisión (bus). 
- El bus recorre la ubicación física de todos los ordenadores. 
- La ruptura del bus impide totalmente la comunicación.
- Es muy sensible a las averías en los cables o problemas en las
  conexiones de los nodos.

![](https://github.com/miguelillo69/Imagenes/blob/main/bus-topology.png?raw=true)

#### VENTAJA:
- Funcionamiento muy simple.
#### INCONVENIENTES:
- Sensible a problemas de tráfico.
- Sensible a las roturas de los cables.

## Modelo OSI
- El modelo OSI es un modelo teórico que se utiliza para el estudio de las redes. 
- Es un modelo de referencia que recoge una estructuración de los servicios de red en siete capas o niveles.

![](https://github.com/miguelillo69/Imagenes/blob/main/OSI.png?raw=true)
- Los siete niveles OSI reciben los siguientes nombres de mayor a menor:
  - 7- Aplicación
  - 6- Presentación
  - 5- Sesión
  - 4- Transporte
  - 3- Red
  - 2- Enlace
  - 1- Físico
   
### La definición de OSI es la siguiente:
- “OSI es el nombre del modelo de referencia de una arquitectura de capas para redes de ordenadores y sistemas distribuidos, propuesta por la ISO como estándar de interconexión de sistemas abiertos”

![](https://github.com/miguelillo69/Imagenes/blob/main/osi.png?raw=true)

### Capa o Nivel
- Para simplificar la complejidad de cualquier red, las diferentes funciones que realizan y los servicios que proveen se estructuran en una serie de niveles o capas. Las capas están jerarquizadas. 
- Cada capa o nivel se ocupa exclusivamente de su nivel inmediatamente inferior, a quien solicita servicios del nivel inmediatamente superior, a quien devuelve resultados.
   
### Interfaz entre capas
- Es el modo en que cada capa negocia los servicios y se comunica con las capas adyacentes. Son las normas de intercomunicación entre capas. 

### Arquitectura de una red.
- Conjunto organizado de capas y protocolos que la red utiliza para producir sus comunicaciones entre nodos.
- Cada capa de la pila añade a los datos a enviar a la capa inferior, información de control para que el envío sea correcto. 
- Esta información de control se denomina cabecera, pues se coloca precediendo a los datos. 
- A la adición de esta información en cada capa se le denomina encapsulación.

### Sistemas distribuidos
- Un sistema distribuido se define como una colección de ordenadores separados físicamente y conectados entre sí por una red de comunicaciones; cada máquina posee sus componentes de hardware y software que el programador percibe como un solo sistema (no necesita saber qué cosas están en qué máquinas). 
- El programador accede a los componentes de software (objetos) remotos, de la misma manera en que accedería a componentes locales.
   
### Sistemas abiertos
- Sistema compuesto por uno o más ordenadores, el software asociado, los periféricos, los procesos físicos, los medios de transmisión de la información,… que constituyen un todo autónomo capaz de realizar un tratamiento de la información y que es capaz de intercomunicarse con otros de acuerdo con unas normas establecidas.

## Niveles OSI orientados a la red
- Los niveles **orientados a la red** son los niveles inferiores que están más próximos a la red
- Se dice que las capas física, de enlace y de red están orientadas a la red.
- Al subconjunto de estas tres capas inferiores se le llama subred .

### NIVEL 1 o NIVEL FÍSICO
- Es la capa de más bajo nivel.
- Se ocupa de las transmisiones de los bits.
- Se ocupa de definir las características mecánicas, eléctricas, funcionales de procedimiento para poder establecer y liberar conexiones entre dos equipos de la red.
  
![](https://github.com/miguelillo69/Imagenes/blob/main/fisico.png?raw=true)

### NIVEL 2 o NIVEL DE ENLACE DE DATOS
- Su misión es establecer una línea de comunicación libre de errores que pueda ser utilizada por la capa inmediatamente superior, la capa de red.
  
![](https://github.com/miguelillo69/Imagenes/blob/main/enlace_datos.png?raw=true)

### NIVEL 3 o NIVEL DE RED
- Se ocupa del control de la subred.
- Su principal función es el encaminamiento, el tratamiento de cómo elegir la ruta más adecuada para que el bloque de datos del nivel de red o paquete llegue a su destino.
- Cada destino está identificado unívocamente en la subred por una dirección.

![](https://github.com/miguelillo69/Imagenes/blob/main/red.png?raw=true)

### NIVEL 4 o NIVEL DE TRANSPORTE
- Es la capa de transición entre los niveles orientados a la red (subred) y los niveles orientados a las aplicaciones. 
- Su misión es
   aceptar los datos de la capa de sesión, fraccionarlos adecuadamente para que sean aceptados por la subred y asegurar que lleguen correctamente al nivel de transporte de destinatario, esté o no en la misma red.

![](https://github.com/miguelillo69/Imagenes/blob/main/transporte.png?raw=true)

## Niveles OSI orientados a la aplicación
- Los tres niveles superiores (sesión, presentación y aplicación) son niveles orientados a la aplicación y realizan funciones directamente vinculadas con los procesos de aplicación que desea comunicarse. 

### NIVEL 5 o NIVEL DE SESIÓN
- La capa de sesión controla y mantiene el enlace entre dos ordenadores durante la transmisión de datos, asegurando que una sesión establecida se complete de principio a fin y pueda reanudarse en caso de interrupción. En muchos casos, sus servicios pueden ser parcialmente o totalmente prescindibles.
 
![](https://github.com/miguelillo69/Imagenes/blob/main/sesion.png?raw=true)
  
### NIVEL 6 O NIVEL DE PRESENTACIÓN
- Esta capa se encarga de la representación de la información, asegurando que los datos sean reconocibles, incluso si los equipos tienen diferentes representaciones internas de caracteres. Se enfoca en el contenido de la comunicación, gestionando la semántica y la sintaxis de los datos transmitidos. También permite cifrar y comprimir los datos, actuando como un traductor entre diferentes sistemas.
   
![](https://github.com/miguelillo69/Imagenes/blob/main/presentacion.png?raw=true)

### NIVEL 7 O NIVEL DE APLICACIÓN
- Proporciona a las aplicaciones acceso a los servicios de otras capas y define los protocolos que utilizan para intercambiar datos (como correo electrónico, bases de datos y servidores de ficheros). Existen numerosos protocolos y su número sigue creciendo debido al desarrollo constante de nuevas aplicaciones.

![](https://github.com/miguelillo69/Imagenes/blob/main/aplicacion.png?raw=true)

# Acceso seguro a redes inalámbricas en dispositivos Apple

- Las plataformas de Apple son compatibles con los protocolos estándar de autenticación y encriptación de redes Wi-Fi, proporcionando acceso autenticado y confidencialidad al conectarse a redes seguras.

## Protocolos de seguridad compatibles

- Apple soporta los siguientes protocolos de seguridad Wi-Fi:

| Protocolo                       | Descripción                                                                           |
|---------------------------------|---------------------------------------------------------------------------------------|
| **WPA2 Personal**               | Proporciona encriptación AES de 128 bits para seguridad personal.                      |
| **WPA2 Enterprise**             | Ofrece encriptación AES de 128 bits para entornos empresariales.                       |
| **WPA2/WPA3 transicional**      | Compatibilidad mixta entre WPA2 y WPA3.                                                |
| **WPA3 Personal**               | Proporciona mayor seguridad personal con encriptación AES de 128 bits.                 |
| **WPA3 Enterprise**             | Mayor seguridad empresarial con encriptación AES de 128 bits.                          |
| **WPA3 Enterprise 192 bits**    | Seguridad reforzada con encriptación AES de 256 bits para entornos empresariales.      |

## Compatibilidad de dispositivos con WPA3

| Dispositivo                      | Compatibilidad con WPA3                      | Compatibilidad con WPA3 Enterprise (192 bits)      |
|----------------------------------|---------------------------------------------|---------------------------------------------------|
| iPhone                           | iPhone 7 o posterior                        | iPhone 11 o posterior                              |
| iPad                             | iPad 5.ª generación o posterior             | iPad 7.ª generación o posterior                    |
| Apple TV                         | Apple TV 4K o posterior                     | No aplicable                                       |
| Apple Watch                      | Apple Watch Series 3 o posterior            | No aplicable                                       |
| Ordenadores Mac                  | Finales de 2013 o posterior (802.11ac)      | Mac con chip de Apple                              |

## Compatibilidad con PMF

- Apple amplía las protecciones WPA2 y WPA3 a tramas de gestión de unidifusión y multidifusión mediante el **servicio de trama de gestión protegida (PMF)**, según el estándar 802.11w.

| Dispositivo                      | Compatibilidad con PMF                       |
|----------------------------------|---------------------------------------------|
| iPhone                           | iPhone 6 o posterior                        |
| iPad                             | iPad Air 2 o posterior                      |
| Apple TV                         | Apple TV HD o posterior                     |
| Apple Watch                      | Apple Watch Series 3 o posterior            |
| Ordenadores Mac                  | Finales de 2013 o posterior (802.11ac)      |

## Métodos de autenticación compatibles

- Los dispositivos Apple compatibles con 802.1X se pueden integrar con servidores RADIUS y soportan los siguientes métodos de autenticación inalámbrica:

  - EAP-TLS
  - EAP-TTLS
  - EAP-FAST
  - EAP-SIM
  - PEAPv0
  - PEAPv1

## Protecciones de la plataforma

- Los sistemas operativos de Apple implementan protecciones avanzadas para evitar vulnerabilidades en el firmware del procesador de red, limitando el acceso a la memoria y utilizando unidades de gestión de memoria de entrada/salida (IOMMU) para aislar los procesadores de red.

## Protocolos en desuso

- Apple también es compatible con varios protocolos antiguos de autenticación y encriptación, que ya no se consideran seguros:

  - WEP (abierta y compartida, con claves de 40 y 104 bits)
  - WEP dinámica
  - TKIP
  - WPA
  - WPA/WPA2 transicional

- Se desaconseja el uso de estos protocolos y se recomienda migrar a WPA3 para garantizar la máxima seguridad y compatibilidad.

## Recomendación

- Se recomienda migrar todas las implementaciones de redes Wi-Fi a **WPA3 Personal** o **WPA3 Enterprise** para ofrecer conexiones más seguras y robustas.

# Arquitectura de Servidores: Cliente-Servidor y Multicapa

## ¿Qué es la arquitectura de servidores?
La arquitectura de servidores se refiere a un diseño en el que procesadores remotos, llamados "clientes", solicitan y reciben servicios de una computadora central, conocida como "servidor". Este modelo es fundamental en las redes informáticas, donde los servidores gestionan y distribuyen recursos o servicios a los clientes conectados.

## Modelo Cliente-Servidor
Este modelo describe la relación en la que un cliente solicita un recurso y un servidor lo proporciona. Inicialmente, se usó para diferenciar la computación distribuida en PCs del modelo centralizado de mainframes. Hoy es uno de los enfoques más comunes en las transacciones informáticas.

### Funcionamiento
- El cliente establece una conexión con el servidor a través de una LAN o WAN.
- El servidor procesa la solicitud y, una vez cumplida, se cierra la conexión.
- Un daemon especial puede esperar solicitudes de clientes en el servidor.

### Tipos de Tráfico
- **Tráfico Norte-Sur:** Comunicación entre clientes remotos y servidores.
- **Tráfico Este-Oeste:** Comunicación entre servidores, más común con la computación en la nube.

### Ventajas del Modelo Cliente-Servidor
- **Centralización:** Facilita la seguridad y el control de acceso a los datos mediante políticas.
- **Independencia de plataforma:** Clientes y servidores pueden utilizar diferentes sistemas operativos.

### Desventajas del Modelo Cliente-Servidor
- **Sobrecarga:** Demasiadas solicitudes pueden saturar el servidor, causando una denegación de servicio y congestión en la red.

### Protocolos Cliente-Servidor
- **TCP/IP:** TCP gestiona la transmisión confiable de datos, mientras que IP se encarga del direccionamiento y envío de paquetes. TCP opera en la capa de transporte (capa 4 del modelo OSI), mientras que IP opera en la capa de red (capa 3 del modelo OSI).

## Modelo Multicapa (OSI)
El modelo OSI, desarrollado por ISO en 1974, describe una arquitectura en 7 capas, cada una con responsabilidades específicas, que colaboran para transmitir datos a través de una red.

### Capa 1: Física
Define la conexión física entre dispositivos y la forma en que los datos se representan como bits. Establece la sincronización y control de velocidad de los datos.

- **Topologías:** Define cómo los dispositivos están organizados en la red (bus, estrella, malla).
- **Modos de transmisión:** Define cómo fluyen los datos entre dispositivos (simplex, half-duplex, full-duplex).

### Capa 2: Enlace de Datos
Responsable de la entrega de datos libres de errores entre nodos. Se encarga del enmarcado, control de acceso y detección de errores.

- **Subcapas:**
  - **LLC (Control de Enlace Lógico):** Maneja la comunicación con las capas superiores.
  - **MAC (Control de Acceso a Medios):** Gestiona el acceso al canal de comunicación.

### Capa 3: Red
Gestiona la transmisión de paquetes entre redes diferentes. Encapsula las direcciones IP y se encarga del enrutamiento, es decir, seleccionar la mejor ruta para los datos.

### Capa 4: Transporte
Asegura la entrega de extremo a extremo de los datos. Implementa control de flujo, gestión de errores y segmentación de datos en unidades más pequeñas llamadas segmentos.

- **Funciones:** Reensamblaje de los datos, dirección de puertos y retransmisión en caso de error.

### Capa 5: Sesión
Controla el establecimiento, gestión y finalización de las sesiones de comunicación. Implementa sincronización y control de diálogo entre aplicaciones.

### Capa 6: Presentación
Se encarga de la traducción de los datos, cifrado/descifrado y compresión de la información para su correcta transmisión a través de la red.

### Capa 7: Aplicación
Proporciona los servicios necesarios para que las aplicaciones accedan a la red. Aquí se implementan las aplicaciones de red que interactúan directamente con el usuario.

- **Funciones:** Servicios de correo, gestión de archivos y directorios.
