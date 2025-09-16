# Temario TAI Kevin adaptado Bloque II

## TEMA 1 \- REPRESENTACIÓN Y ELEMENTOS DE UN SISTEMA

### 1\. SISTEMAS DE NUMERACIÓN

| Unidad (Decimal, SI) | Equivalencia en bytes (10^n) | Unidad (Binaria, IEC) | Equivalencia en bytes (2^n) | Relación aproximada |
|-----------------------|-----------------------------|------------------------|-----------------------------|---------------------|
| Kilobyte (kB)         | 10^3 = 1 000 B             | Kibibyte (KiB)         | 2^10 = 1 024 B              | 1 KiB ≈ 1.02 kB     |
| Megabyte (MB)         | 10^6 = 1 000 000 B         | Mebibyte (MiB)         | 2^20 = 1 048 576 B          | 1 MiB ≈ 1.05 MB     |
| Gigabyte (GB)         | 10^9 = 1 000 000 000 B     | Gibibyte (GiB)         | 2^30 ≈ 1.07 × 10^9 B        | 1 GiB ≈ 1.07 GB     |
| Terabyte (TB)         | 10^12                      | Tebibyte (TiB)         | 2^40 ≈ 1.10 × 10^12 B       | 1 TiB ≈ 1.10 TB     |
| Petabyte (PB)         | 10^15                      | Pebibyte (PiB)         | 2^50 ≈ 1.13 × 10^15 B       | 1 PiB ≈ 1.13 PB     |
| Exabyte (EB)          | 10^18                      | Exbibyte (EiB)         | 2^60 ≈ 1.15 × 10^18 B       | 1 EiB ≈ 1.15 EB     |
| Zettabyte (ZB)        | 10^21                      | Zebibyte (ZiB)         | 2^70 ≈ 1.18 × 10^21 B       | 1 ZiB ≈ 1.18 ZB     |
| Yottabyte (YB)        | 10^24                      | Yobibyte (YiB)         | 2^80 ≈ 1.21 × 10^24 B       | 1 YiB ≈ 1.21 YB     |
| Brontobyte (BB)       | 10^27                      | Brontobibyte (BibiB)   | 2^90 ≈ 1.23 × 10^27 B       | 1 BibiB ≈ 1.23 BB   |
| Geopbyte (GBB)        | 10^30                      | Geopbibyte (GibiB)     | 2^100 ≈ 1.27 × 10^30 B      | 1 GibiB ≈ 1.27 GBB  |
| Saganbyte (SB)        | 10^33                      | Saganbibyte (SabiB)    | 2^110 ≈ 1.30 × 10^33 B      | 1 SabiB ≈ 1.30 SB   |
| Jotabyte (JB)         | 10^36                      | Jotabibyte (JobiB)     | 2^120 ≈ 1.33 × 10^36 B      | 1 JobiB ≈ 1.33 JB   |

* Bit (binary digit): 0, 1\.
* Nibble (cuarteto): 4 bits.
* Byte (octeto): 8bits \= 23 bits.
* Binario: sólo utilizar 0, 1\. Base(2)
* Octal: 0, 1, 2, 3, 4, 5, 6, 7\. Base (8)
* Hexadecimal: 0-9,A, B, C, D, E, F. Base (16)
* Ca2: Complemento a 2\. Número enteros negativos.
    * Nº 0110
    * Invertir el número 1001
    * Sumarle 1 \+ 1
    * Ca2 del nº original      ``1010``
* Ca1: Complemento a 1\. Igual pero sin sumar 1\.
* Coma flotante: número decimales.

### 2\. ARQUITECTURA DE ORDENADORES

#### 2.1. ARQUITECTURA VON NEUMANN

* Un programa es una secuencia de pasos, en cada uno se realiza una operación aritmético-lógica, para cada paso se
  necesita un conjunto de señales de control, la solución consiste en asociar un código específico a cada posible
  conjunto de señales de control, y además tanto los datos como las instrucciones de este circuito sean guardados en una
  misma memoria, el diseño se basa en tres conceptos clave:
    * Los datos y las instrucciones se almacenan en una sola memoria de lectura-escritura.
    * Los contenidos de esta memoria se direccionan indicando su posición, sin considerar el tipo de dato.
    * La ejecución se produce siguiendo una secuencia de instrucción tras instrucción.

#### 2.2. ARQUITECTURA DE BUS

* La arquitectura Von Newmann utiliza un único canal de comunicación común y conexión material por él se envían todo
  tipo de datos entre las distintas partes del ordenador, son conexiones materiales que permiten a los componentes
  comunicarse entre sí e interaccionar, tres tipos:
    * ``Bus de Control``: transporta ordenes de control.
    * ``Bus de Direcciones``: transporta direcciones de memoria.
    * ``Bus de Datos``: trasporta datos como tales.

* El conjunto de estos tres buses forma el Bus del Sistema, se caracteriza por:
    * ``Ancho de bus``: cantidad de información que puede manipular simultáneamente.
    * ``Rapidez`` con la que puede transferir dichos datos.

#### 2.3. FRECUENCIA DE CICLO

* En todo ordenador existe un reloj maestro que marca en todo momento uno de los dos posibles estados en que puede
  hallarse el voltaje eléctrico en todas las partes de la CPU, la unidad de control que posee la CPU.

#### 2.4. MEMORIA PRINCIPAL

* Es necesario almacenar instrucciones y datos mientras se ejecutan los programas, para este fin existe la memoria
  principal, donde se almacenan los datos y las instrucciones, está dividida en celdas (llamadas palabras de memoria),
  el “mapa de memoria” se corresponde con el espacio de memoria direccionable. Las principales características de la
  memoria principal son:
    * Está formada por circuitos eléctricos denominados biestables.
        * ``Acceso aleatorio``: la memoria principal se divide en celdas que almacenan bits, pero no se puede acceder a
          una celda de manera individual.
        * ``Tiempo de acceso``: tiempo transcurrido desde que se solicita una lectura hasta que el dato está disponible
          en un registro.
        * ``Ciclo de memoria``: tiempo requerido en la ejecución de una operación de memoria y la solicitud inmediata a
          la memoria de otra operación idéntica.

    * Clasificación de la memoria desde el punto de vista de la volatilidad:
        * ``ROM`` (Read Only Memory):
            * ``PROM`` (Programable ROM): una vez grabadas no se pueden borrar.
            * ``EPROM`` (Erasable PROM): se puede borrar con rayos ultravioletas y volver a grabar.
            * ``EEPROM`` (Electrically EPROM): se pueden borrar eléctricamente.

        * ``RAM`` (Random Access Memory):
            * ``SRAM`` (Static Random Access Memory): muy rápida, pero más cara, se usa en los procesadores y en
              pequeñas cantidades.
            * ``NVRAM`` (Non-Volatile Random Access Memory): es una memoria de acceso aleatorio que es capaz de
              almacenar información y no perderla al retirar la alimentación eléctrica del componente (BIOS).
            * ``DRAM`` (Dynamyc Random Access Memory): el termino dinámico indica que para que el chip de memoria pueda
              guardar información cada bit debe ser refrescado en un cierto periodo de tiempo, si se desconecta la
              energía, la información se pierde.
            * ``SDRAM`` (Syncronous DRAM): recibe y emite información sincronizada a un reloj externo, extremada mente
              más rápidas para leer y escribir.
            * ``RAM-CMOS``: es un tipo de memoria que almacena información sobre la configuración del sistema. Debido a
              ello suele confundirse con el propio BIOS, pero es una entidad de memoria diferente, esta solo almacena
              opciones de la BIOS.

#### 2.5. JERARQUÍAS DE MEMORIA

* Aparte de los propios registros de la CPU, que son la memoria más rápida, es necesario tener una memoria pequeña pero
  muy rápida, pero de mayor tamaño que estos, se denomina cache. En una jerarquía donde predomine la proximidad a la
  CPU, podemos distinguir:
    * ``Registros``: memoria local e interna de la propia CPU, es la más rápida.
    * ``Memoria Caché``: intermedia entre CPU y la Memoria Principal, contiene los datos que más se usan, suele usarse
      memoria SRAM para su construcción.
        * Principio de ``localidad temporal``: se ubican en la cache los datos más recientemente utilizados.
        * Principio de ``localidad espacial``: se ubican en la cache los datos adyacentes a los utilizados.
    * ``Memoria Principal`` (RAM): se comunica con la cache por bloques, también se comunica con dispositivos de memoria
      secundaria.

##### 2.5.1. MEMORIA CACHÉ

* Memoria auxiliar de acceso aleatorio de baja capacidad y gran velocidad, se clasifican en:
    * ``Cache interna o integrada``: incluida en el procesador, puede ser de dos tipos:
        * Caché de ``lectura``: cuando la CPU realiza una lectura sobre un dispositivo de memoria principal o
          secundaria, antes comprueba si está en cache.
        * Caché de ``escritura``: las operaciones de escritura no se apuntan directamente sobre memoria principal, sino
          que se escriben en memoria cache.

    * ``Caché externa``.
        * ``Otra distinción``:
            * ``Caché de instrucciones`` (almacena instrucciones).
            * ``Caché de datos`` (almacena datos).
            * ``Se puede organizar de tres formas``:
            * ``Correspondencia directa``: cada bloque tiene un solo lugar donde puede estar dentro de la memoria.
            * ``Asociativa por vías``: cada bloque se puede colocar en un conjunto restringido de dos o más bloques
              dentro de cada cache.
            * ``Completamente asociativa``: cada bloque se puede colocar en cualquier lugar.

##### 2.5.2. POLÍTICAS DE REEMPLAZO POR FALLO DE CACHE

* Cuando se produce un “fallo de cache” hay que ir a buscar el bloque al nivel inmediatamente inferior y liberar
  espacio:
    * ``Aleatorio``: escogemos un bloque de forma pseudoaleatoria.
    * ``Menos recientemente utilizado``: cogemos el que hace más que no se usa.
    * ``El primero en llegar es el primero en salir``: los bloques sustituidos van saliendo en el mismo orden que
      llegaron.

#### 2.6. CPU (Control Processing Unit)

* La unidad funcional que ejecuta las instrucciones de una determinada arquitectura de propósito general (monoprocesador
  o multiprocesador), se encarga de realizar las operaciones de cálculo y de controlar el flujo de datos entre los
  diversos elementos que forma un ordenador, se distinguen básicamente dos partes:
    * ``ALU`` (Aritmethic Logic Unit): agrupa todos los componentes capaces de manipular datos, realiza operaciones de:
        * ``Punto fijo`` (aritmética entera y calculo efectivo de las direcciones).
        * ``Punto flotante`` (aritmética con mantisa y exponente).
        * ``Longitud variable`` (aritmética decimal y operaciones sobre conjuntos de caracteres).

    * ``CU`` (Control Unit): realiza el control del proceso y genera señales para activar los componentes. Trabaja en
      base al reloj maestro que interpreta y coordina la ejecución de todas las operaciones.
    * ``Registros``: unión de varios circuitos lógicos que almacenan un determinado número de bits, tipos básicos:
        * ``Uso general``: puede almacenar el operando para cualquier código de operación.
        * ``Datos``: contienen datos y no participan en el cálculo.
        * ``Direcciones``: dedicados a modos de direccionamiento específicos (Registros índices, Punteros de Pila...).
        * ``Flags`` (Códigos de Condición): son bits fijados mediante hardware, indican si una operación entrega un
          resultado positivo, negativo, nulo, si hay overflow...

#### Registros fundamentales que aparecen en todo ordenador:

* > PC (Program Counter): contiene la dirección de la siguiente instrucción.
* > La CPU actualiza el PC después de cada lectura de instrucción de manera que siempre apunta a la siguiente instrucción a ejecutar.
* > INC (Incrementer): sumando su contenido al registro PC, incrementa el contenido de este.
* > IR (Instruction Register): contiene la instrucción actual, aquí se analiza el código de operación.
* > MAR (Memory Address Register): contiene la dirección de una posición de memoria, el intercambio de datos con la memoria se realiza conectado directamente al bus de direcciones.
* > MBR (Memory Buffer Register): contiene cada palabra de datos para escribir en memoria que ha sido leída más recientemente, el intercambio de datos con la memoria se realiza conectado directamente al bus de datos.
* > Registros E/S: contiene la dirección de memoria cuyo contenido se reserva para almacenar datos provenientes de algún dispositivo de entrada y salida.
    * > E/SAR (E/S Address Register): registro de direcciones, a las posiciones de memoria cuyo contenido se usa para comunicarse con los dispositivos E/S se les denomina “puertos”.
    * > E/SBR (E/S Buffer Register): intercambiar datos entre un módulo E/S y la CPU. Registros D0, D1...
* > Dn (Data Registers): registros genéricos destinados a contener todo tipo de datos.

#### 2.7 CLASIFICACIÓN DE MICROPROCESADORES

* ``CISC`` (Complex Instructions Set Computer): procesa un conjunto de instrucciones complejo. Interpretan y ejecutan un
  gran número de instrucciones pro son relativamente lento.
* ``RISC`` (Reduced Instructions Set Computer): procesan un conjunto de instrucciones reducido. Interpretan y ejecutan
  solo unas pocas instrucciones, pero son mucho mas rápidos que los CISC.

##### 2.7.1 MECANISMOS DE SINCRONIZACION CPU-PERIFÉRICOS:

* ``E/S Programada`` (por sondeo): la CPU realiza por software la sincronización y transferencia, con el control
  absoluto de la operación E/S.
* ``E/S por INTERRUPCIONES``: no existe bucle de espera, sincronización se realiza por hardware. Cuando un periférico
  está listo para transmitir se lo indica a la CPU activando la “Línea de Petición de Interrupción”, la CPU recibe la
  señal de petición de interrupción, abandona la ejecución del programa y salta a la RTI (Rutina de Tratamiento de
  Interrupciones)
  .
* ``E/S por Acceso Directo a Memoria`` (DMA): permite la transferencia de datos entre un periférico y la memoria sin la
  intervención de la CPU. Hay varios tipos:
    * ``Modo ráfaga``: el DMAc (controlador del DMA) solicita el control del bus a la CPU, después este no lo libera
      hasta haber finalizado la transferencia de todo el bloque de datos completo.
    * ``Modo robo de ciclo``: el DMAc solicita el control del bus a la CPU (un ciclo), se realiza la transferencia de
      una única pabla y después el DMAc libera el bus. Por lo que el DMAc solicita el control del bus tantas veces como
      sea necesario.
    * ``Transparente``: el DMAc accede al bus solo cuando la CPU no lo está utilizando.

#### 2.8 PROGRAMACIÓN E/S:

* El procesador de E/S puede observar el estado de la CPU inspeccionando un registro de estado (canal).
* Por medio de interrupciones, hace que la CPU suspenda la ejecución y transfiera el control a una posición determinada
  donde se especifica la dirección de un programa que ha de entrar en proceso como respuesta a la interrupción.
* Hay tres agrupamientos básicos de instrucciones E/S:
    * ``Instrucciones de transferencia``: lectura, escritura o verificación de estado de dispositivo.
    * ``Instrucciones de control de dispositivos``.
    * ``Instrucciones de bifurcación``: transferencia de control dentro del programa de canal.

### 3\. COMPONENTES INTERNOS

#### 3.1. PLACA BASE

* Circuito que conecta diversos elementos que se encuentran sobre ella:
    * ``Microprocesador`` (insertado en un zócalo ZIF “Zero Insertion Forze”).
    * ``Chipset, reloj y memoria RAM``.
    * ``Ranuras de expansión``, donde se conectan las tarjetas controladoras.
    * ``Chips de control y almacenamiento`` (BIOS, ROM, caché externa).
    * ``Conectores externos`` (USB, comunicaciones, sonido, red local, video...).

> Las ``dimensiones`` están ``estandarizadas``: ATX, Micro-ATX, Mini-ITX...

##### 3.1.1. COMPONENTES DE LA PLACA BASE

* ``Socket``: lugar donde se inserta el procesador, tipos:
    * LGA1156, LGA2011 (Intel Core).
    * AM2, AM3, AM4 (Phenom y Ryzen).

* ``Ranuras de memoria``: lugar donde se inserta la RAM, se incorpora un sistema de canal doble (Dual-Channel) en el que
  se utilizan dos buses distintos para la transferencia, tipos de ranuras:
    * ``SIMM`` (Single In-line Memory Module).
    * ``DIMM``: más alargados (168 contactos).
    * ``SO-DIMM``.
    * ``RIMM``.

* ``BIOS`` (Basic Input-Output System):
    * Es un programa incorporado en un chip de la placa base que se encarga de realizar las unciones básicas de control
      y configuración del ordenador, es almacenado en un chip de ROM o flash.
    * Al encender es automáticamente cardado a la memoria principal y es ejecutado por el procesador, realiza una rutina
      de verificación e inicialización de los componentes llamada POST (PowerOn Self Test), se encarga de guardar todas
      las configuraciones del equipo en una memoria volátil llamada CMOS.

* ``Chipset``: elemento formado por un determinado número de circuitos integrados que proporciona compatibilidad PC a
  nivel hardware.

* ``Northbridge`` (Memory Controller Hub): es el circuito integrado más importante del conjunto de chips, controla las
  funciones de acceso desde y hasta el microprocesador, RAM, video integrado... Sirve de conexión entre la placa madre y
  los principales componentes del PC.
* ``Southbridge`` (I/O Controller Hub): circuito integrado que coordina los diferentes dispositivos de entrada y salida.
  Se comunica con la CPU a través del Northbridge, incluye soporte para Ethernet, RAID, USB y codec de audio. Integra
  cada vez mayor número de dispositivos a conectar con tecnologías como HyperTransport o Ultra V-Link para evitar efecto
  botella del PCI.

* ``Memoria caché``: memoria temporal, de existencia oculta para el usuario, proporciona acceso rápido a los datos de
  uso más frecuente, está integrada en el procesador.

* ``Conectores internos``:
    * ``IDE`` (Integrated Drive Electronics)/PATA (Parallel Advanced Technology Attachment): conectar discos duros o
      CD-ROM, transferencia máxima de 166,6 MB/s.
    * ``SATA`` (Serial Advanced Technology Attachment): utilizado en discos duros, sustituye a PATA, mayor velocidad,
      mejor aprovechamiento cuando se tienen varios discos, alcanza los 6 Gbits/s.

* ``Ranuras de expansión``:
    * ``PCI``: trabajan hasta 132 MB/s suficiente para tarjetas de red y sonido.
    * ``AGP``: exclusivo para tarjetas de graficas debido a su auge como aceleradoras 3D en el pasado, puede soportar
      desde 1x a 8x.
    * ``PCIe``: estándar actual para dispositivos de alto rendimiento.

## TEMA 2 \- PERIFÉRICOS

### 1\. PERIFÉRICOS

* Los periféricos son dispositivos E/S conectados al ordenador, pueden ser de entrada, salida, entrada/salida (mixtos) y
  memoria masiva o auxiliar.
* La conexión entre las distintas unidades funcionales del ordenador, ser realiza mediante un conjunto de líneas de
  conexión, denominadas buses, el bus que permite la conexión “a” o “desde” los periféricos se denominan buses de
  entrada y salida paralelos.
* Los dispositivos pueden ser:
    * ``Orientados a bloque``: se pueden direccionar, escribir o leer cualquier bloque del dispositivo realizando
      primero una operación de posicionamiento sobre el mismo (discos duros, memoria, unidades de cinta...)
    * ``Orientados a carácter``: trabajan con secuencias de bytes sin importar su longitud ni ninguna agrupación en
      especial, no son dispositivos direccionables (teclado, pantalla, impresoras...).   
      Los periféricos pueden conectarse directamente al bus de sistema o a través de unos circuitos denominados
      interfaces, que han de proveer gran cantidad de posibilidades de interconexión que cumplan las necesidades de cada
      periférico. Algunos de los puertos más representativos son:
    * ``PATA, SATA y eSATA``: usados en unidades de disco duro.
    * ``Ethernet``: tarjetas de red.
    * ``Firewire`` (IEEE 1394): interfaz de alta velocidad diseñado por Apple para entrada y salida de datos en serie a
      gran velocidad. Suele utilizarse para la interconexión de dispositivos digitales desde ordenadores hasta discos
      duros o cámaras digitales, hasta 32Gbps (400 MB/s).
    * ``HDMI/VGA/DVI``: interfaces con visualizadores.
    * ``SCSI`` (Small Computer System Interface) y SAS (Serial Attached SCSI): usados en discos duros y cintas de
      backup.
    * ``Puertos específicos``: PS/2.
    * ``Puerto paralelo``: habitual para impresoras hasta que llego USB.
    * ``Puerto serie``: RS232 (periféricos que manejan pocos datos).
    * ``Thunderbolt``: hasta 40 Gbit/s.
    * ``USB`` (Universal Serial Bus): permite adjuntar dispositivos periféricos rápidamente, estándar:
        * ``1.0``: alcanza 1.6 Mbps (200 KB/s).
        * ``2.0``: alcanza hasta 480 Mbps (60 MB/s), dispone de 4 conectores, 2 para datos (half-duplex) y dos para
          alimentación.
        * ``3.0``: alcanza hasta 4.8 Gbps (600 MB/s), dispone de 8 conectores, 2 para subida y dos para bajada (
          full-duplex).
        * ``3.1``: alcanza 10 Gbps (1.2 GB/s).
        * ``3.2``: alcanza 20 Gbps (2.5 GB/s).
        * ``4.0``: alcanza 40 Gbps (5 GB/s).

#### 1.1. PERIFÉRICOS DE ENTRADA

* ``Teclado``: clasifican según la disposición de teclas, el mayoritario es QWERTY, pueden ser mecánicos o de membrana.
* ``Ratón``: dispositivo de entrada de datos y de control, tipos:
    * ``Mecánico``: cuenta con una bola de goma y dos ejes dotados de una rueda dentada.
    * ``Óptico``: carece de bola de goma, usa un sensor.
    * ``Inalámbrico``: carece de cable.
    * ``TrackPoint``: protuberancia cilíndrica en el medio del teclado
    * ``Touch Pad``: membrana rectangular sensible al tacto bajo el teclado (portátiles).
    * ``TrackBall``: ratón que presenta su bola al alcance del dedo pulgar.

* ``OMR`` (Optical Mark Reader): aceptan información escrita a mano y la transforman en datos binarios inteligibles para
  el ordenador. Detectores de código de barras: leen el código formado por la codificación de cada digito decimal en
  barras de grosor relativo negras y blancas adyacentes (European Article Numbering)
* ``Escáner``: exploración de imágenes mediante procedimientos opto electrónicos. ``Tipos`` de escáner:
    * De ``mesa o plano``: tiene una fuente de luz y un sensor de luz.
    * De ``tambor``: escáner de gran tamaño que permite escaneo por modelo de color CYMK o RGB con gran resolución
      óptica.
    * De ``microfilm``.
    * Para ``diapositivas``.
    * De ``mano``.
    * ``Digitalizador de video``.
    * De ``transferencia``.

* ``Digitalizador o tarjeta gráfica``: unidades de entrada que permiten transferir directamente al computador gráficas,
  figuras, planos, mapas...

#### 1.2. PERIFÉRICOS DE SALIDA

* ``Monitor``:
    * ``CRT`` (Cathode Ray Tube): metal con potencial negativo y fuertemente calentado por un filamento, de forma que
      libere electrones. Estos chocaran contra el interior de la pantalla, recubierta de fosforo, que se iluminará.
    * ``LCD`` (Liquid Crystal Display): la pantalla está formada por una matriz de puntos, cada uno recibe una señal
      para activarse, dos grandes tipos:
        * Matriz pasiva: cada celda está controlada por un transistor que activa la fila y otro que activa la columna.
    * Matriz activa: cada celda está controlada por su propio transistor, permite una mayor luminosidad, pero también
      consume más energía.
    * ``TFT`` (Thin Film Transistor): cada pixel es excitado de forma directa.
    * ``PDP`` (Plasma): células pequeñas que contienen gases ionizados con carga eléctrica.
    * ``LED`` (Light Emitting Diode): compuesta por diodos emisores de luz, tipos:
        * OLED (Organic Light-Emitting Diode).
        * AMOLED (Active Matrix OLED).
        * Super AMOLED.

* ``Tarjeta de vídeo``: conjunto de circuitos electrónicos que convierten los datos de salida a vídeo, cronológicamente
  aparecieron: Tarjeta de vídeo monocromática, CGA (permitía colores), EGA, VGA, XGA, SVGA, UXGA, WUXGA.

* ``Impresora``: escriben la información de salida sobre papel, cuando el pc se comunica con una impresora utiliza un
  lenguaje especial denominado “lenguaje de descripción de página” o PDL, hay dos PDLs, PCL (Printer Command Language) y
  PostScript, ``tipos`` de impresora:
    * ``De impacto``: utilizan un sistema mecánico de manera que los caracteres se forman al golpear una cinta entintada
      contra el papel:
    * De ``agujas`` (matriciales): cabezal de agujas al golpear forma los caracteres, que son impresos sobre el papel.
    * De ``margarita``: varillas, una por carácter, alrededor de un disco que puede girar.
    * ``Impresoras sin impacto``: más silenciosas, rápidas y mayor calidad, hacen uso de técnicas fotográficas,
      electrónicas, de inyección de tinta y de sublimación de tinta:
    * ``Térmicas``: cabezal de agujas, el papel, al calentarse por la aproximación se oscurece o colorea, dejando
      impreso el carácter.
    * ``Electrostáticas``: usan un cartucho para la proyección de la imagen formada con iones que se depositan sobre un
      tambor dieléctrico. Las partículas del tóner se adhieren al tambor y por presurización en frío la imagen se
      transfiere al papel.
    * ``Láser``: utilizan el haz de un láser para inducir cargas eléctricas sobre un tambor que está girando, la carga
      negativa de las partículas del tóner hace que esta permanezca en el papel.
    * De ``inyección de tinta``: forman los puntos que componen los caracteres y gráficos al pulverizar pequeñas gotas
      de tinta.

* ``Plotter``: dibujos sobre papel (planos, mapas, esquemas...).

#### 1.3. PERIFÉRICOS DE ENTRADA/SALIDA

* ``Módem``: dispositivo que convierte las señales digitales del ordenador ene señales analógicas que pueden
  transmitirse a través del canal telefónico.
* ``NIC`` (Network Interface Card): permite a un ordenador acceder a una red y compartir recursos.
* ``Tarjeta de sonido``: transforma datos digitales en analógicos, DAC (Digital-Analogic  
  Converter).
* ``Pantallas táctiles``: pantallas que pueden detectar coordenadas donde se toca, dos tipos:
    * ``Capacitiva``: manejadas mediante un objeto que tenga capacitancia, no requieren presión sobre el dispositivo (
      móviles).
    * ``Resistiva``: dos capas que al ser pulsadas entran en contacto produciéndose un cambio de corriente y detectando
      la pulsación.

#### 1.4. PERIFÉRICOS DE ALMACENAMIENTO

* ``Disco electromecánico``: contiene un motor que permite la rotación del disco y el posicionamiento de los cabezales
  de lectura/escritura, formado por:
    * ``Discos de soporte``: uno o varios, donde se almacena la información, están recubiertos por ambas partes del
      material ferromagnéticos susceptible de almacenar microcampos magnéticos.
    * ``Motor de rotación``: hace girar los discos a velocidades de 5400, 7200 o 15000 rpm.
    * ``Cabezales de lectura/escritura``: cada cara de los discos del disco duro lleva asociado un pequeño cilindro de
      hierro bobinado que es capaz de detectar variaciones (leer) en el campo magnético de la superficie, o alterarlo (
      escribir).
    * ``Controlador``: circuitería eléctrica que permite controlar tanto los aspectos mecánicos del disco como los
      aspectos lógicos de transferencia de datos.
    * ``Partes`` de cara a almacenar y localizar la información:
        * A. ``Pistas`` o Tracks: pistas concéntricas invisibles a lo largo de las cuales se graban los pulsos
          magnéticos.
        * B. ``Sector geométrico``.
        * C. ``Sector``.
        * D. ``Cluster``: conjunto de sectores en una pista.

* ``SSD`` (Solid State Drive): los datos no se almacenan sobre superficies cilíndricas ni platos, almacenan la
  información en microchips con memorias flash interconectadas entre sí, basadas en NAND, incluyen un procesador
  integrado que se encarga de realizar las operaciones relacionadas con la lectura y escritura de datos, velocidades de
  transferencia entre 200 y 500 MB/s.
* ``Discos ópticos``:
    * ``CD`` (Compact Disk): almacenamiento de 700 MB, velocidad de transferencia 150KBps.
        * CD-ROM (Read Only), CD-R (Write Once, Read Many), CD-RW (Write Many, Read Allways).
    * ``DVD`` (Digital Versatil Disk): almacena entre 4,5 y 15,5 GB, velocidad de 1350 Kbps.
        * DVD-ROM, DVD-R y DVD+R, DVD-RW/DVD+RW, DVD-RAM
    * ``Blu-ray Disc``: sustituye al DVD, almacena alta resolución, contiene 25 GB por capa.

#### 1.5. GESTIÓN DE ALMACENAMIENTO DE DATOS FIABLE Y REDUNDANTE

* ``RAID`` (Redundant Array of Independent Disks): varios discos en un array para formar un volumen de mayor tamaño
  tolerante a fallos y mejor rendimiento.
* Encontramos:
    * ``RAID 0`` (Volumen Stripped (stripping)): datos se distribuyen entre dos o más discos, sin información de
      paridad, redundancia o tolerancia a fallos. El fallo en uno de los discos provoca la paridad de todos los datos,
      la utilidad es que aumenta el rendimiento.
    * ``RAID 1`` (Volumen Espejo (mirroring)): copia exacta de los datos en dos o más discos, aparecen en el sistema
      como una única entidad, en caso de error de una unidad, el otro disco duro se puede desdoblar para que continúe
      proporcionando acceso completo a los datos almacenados en la unidad.
    * ``RAID 3``: divide los datos a nivel de bytes en lugar de a nivel de bloques, necesita un mínimo de tres discos,
      utilizando uno para datos de paridad. En estos se copian los datos en distribución RAID 0 en los 2 primeros, en el
      tercer disco, se crea el byte de paridad.
    * ``RAID 5`` (Volumen Distribuido con Paridad): datos repartidos a nivel de bloque, con paridad distribuida entre
      varios discos, se escribe información de paridad para cada sección dentro de las distintas partes. Si falla un
      disco, los datos pueden reconstruirse con la paridad, requiere al menos tres discos. Proporciona un excelente
      rendimiento en las operaciones de lectura, pero es sustancialmente más lento que las restantes opciones.
    * ``RAID 6`` (Volumen Distribuido con Doble Paridad): es como RAID 5, pero los datos de paridad se escriben en dos
      unidades. Eso significa que requiere al menos 4 unidades y puede soportar 2 unidades que mueren simultáneamente.

* Muchas controladoras permiten anidar niveles RAID, es decir, que un RAID pueda usarse como elemento básico de otro en
  lugar de discos físicos. Los niveles RAID anidados más comúnmente usados son:
    * [``RAID 0+1``](https://es.wikipedia.org/wiki/RAID#RAID_0+1): Un espejo de divisiones.
    * [``RAID 1+0``](https://es.wikipedia.org/wiki/RAID#RAID_1+0): Una división de espejos.
    * [``RAID 30``](https://es.wikipedia.org/wiki/RAID#RAID_30): Una división de niveles RAID con paridad dedicada.
    * [``RAID 100``](https://es.wikipedia.org/wiki/RAID#RAID_100): Una división de una división de espejos.
    * [``RAID 10+1``](https://es.wikipedia.org/wiki/RAID#RAID_10+1): Un Espejo de espejos.

##

* > Bit de Paridad: dígito binario que indica si el número de bits con un valor de 1 en un conjunto de bits es par o impar.
* > En el caso de la paridad PAR, se cuentan el número de unos.
* > Si el total es impar, el bit de paridad se establece en uno y por tanto la suma del total anterior con este bit de paridad, daría par.
* > Si el conteo de bits uno es par, entonces el bit de paridad (par) se deja en 0, pues ya es par.
* > En el caso de la paridad IMPAR, la situación es la contraria.
* > Se suman los bits cuyo valor es uno, si da un número impar de bits, entonces el bit de paridad (impar) es cero.
* > Y si la suma de los bits cuyo valor es uno es par, entonces el bit de paridad (impar) se establece en uno, haciendo impar la cuenta total de bits uno.

##

* ``JBOD`` (Just a Bunch Of Disks):
* Es una arquitectura que utiliza múltiples discos duros expuestos como dispositivos individuales.
* Los discos duros pueden tratarse de forma independiente o combinarse en uno o más volúmenes lógicos mediante un gestor
  de volúmenes como ``LVM`` o ``mdadm``, o un sistema de archivos que abarque varios dispositivos como btrfs; estos
  volúmenes suelen denominarse "spanned" (abarcados) o "linear | SPAN | BIG".
* Un volumen "spanned" no ofrece redundancia, por lo que la falla de un solo disco duro equivale a la falla de todo el
  volumen lógico.
* A diferencia de un volumen RAID 0 (stripped), la capacidad de un volumen lineal no está limitada por el disco más
  pequeño multiplicado por el número total de discos, sino que simplemente se suma su capacidad.
* Sin embargo, la velocidad no se multiplica.

> ``mdadm``: utilidad de Linux utilizada para administrar y monitorear dispositivos RAID por software.

## TEMA 3 \- SISTEMAS OPERATIVOS

### 1\. SISTEMAS OPERATIVOS

* Es el software básico de un ordenador, conjunto de programas y funciones que gestionan el funcionamiento del hardware
  y del software, es el primer programa que se carga en memoria al encender y el principal administrador de recursos.
* Pueden ser según el modo en el que este se comunica con el usuario:
    * ``Línea de comandos``: las operaciones del sistema se introducen tecleándolas directamente o bien ejecutando una
      colección de estas almacenadas en forma de guion “script”.
    * ``Interfaz gráfica``: manipulación de elementos gráficos en la pantalla.

* Se organizan por capas en torno a un núcleo principal:
    * ``Nivel kernel``: controla todo lo que sucede en el ordenador, gestiona los procesos que llegan para ser
      ejecutados.
    * ``Nivel ejecutivo``: administración de la memoria.
    * ``Nivel supervisor``: realiza la comunicación de cada proceso entre el sistema y el usuario, controla y coordina
      la gestión de entrada/salida de los diferentes procesos con destino a los periféricos.
    * ``Nivel usuario``: controla los procesos que está utilizando el usuario, simplemente muestra al usuario el proceso
      que este quiere ejecutar.

### 2\. COMPONENTES DE UN SISTEMA OPERATIVO

* ``Núcleo`` o “kernel”: componente principal del sistema, responsable de tareas como trasladar el control de un
  programa a otro, control y programación de entrada y salida, de manejo de interrupciones, gestión de memoria,
  comunicación entre procesos...
* ``Programas de control``: parte del sistema dedicado a controlar el funcionamiento de todos los recursos y elementos
  de un ordenador: procesador, memoria, periféricos...
* ``Programas de proceso``: diseñados para ayudar al programador en la puesta a punto de las aplicaciones, dos tipos:
    * ``Traductores``: toman como entrada un programa fuente y proporcionan con salida un programa objeto, este necesita
      cierta preparación que realiza el enlazador, tres tipos de traductores:
        * ``Ensambladores``: transforma programas fuente escritos en leguajes simbólicos de bajo nivel denominados
          ensambladores en programas objetos escritos en código máquina y directamente ejecutables.
        * ``Compiladores``: transforman programas fuente escritos en lenguajes de alto nivel en programas objetos
          escritos en leguaje máquina, realiza la traducción completa y crea el programa objeto cuando no existan
          errores en la traducción.
        * ``Intérpretes``: transforman programas fuente escritos en lenguajes de alto nivel en programas objetos
          escritos en lenguaje máquina, ejecuta las instrucciones según se va realizando la traducción sin esperar a
          traducir el programa fuente completo.
* ``Programas de servicio``: programas que realizan funciones apara el sistema usuario denominadas utilidades:
    * Programas de manipulación de datos: liberan al programador de trabajos rutinarios como la trasferencia de archivos
      entre soportes, reorganización de archivos, ordenación de datos.
* Programas de servicio del sistema: generación del sistema operativo completo sobre el ordenador, preparación de los
  programa y creación y mantenimiento de las bibliotecas de programas.

> `modprobe`: programa de Linux para gestionar módulos del kernel de UNIX.

### 3\. PROCESOS

* En un sistema multiprogramado la CPU alterna entre programas, ejecutando cada uno de ellos unos cuantos milisegundos,
  todo software ejecutable en el ordenador se organiza en procesos, inclusive el sistema operativo, cada proceso dispone
  de una CPU virtual, aunque la CPU física lo que hace es una alternancia muy rápida.
* Se puede definir un proceso como un programa en ejecución, puede estar constituido por el programa y los valores de
  las variables que intervienen en la ejecución, por lo tanto, es una entidad dinámica, contiene una parte fija (el
  programa) y una parte variable (estado del proceso), cuatro conceptos asociados a la gestión de procesos:
    * Necesidad de que cada proceso tenga asignada una prioridad, se encarga el planificador.
    * El distribuidor se encarga de activar procesos en función de sus prioridades.
    * Estado de proceso, situación con respecto al procesador (activo, esperando el bloqueado...).
    * Si no hay espacio suficiente en la memoria principal los programas en espera se llevan a la memoria secundaria.
    * Los estados de un proceso pueden ser:
        * ``Activo/ejecución``: proceso que se está ejecutando.
        * ``Bloqueado/en espera``: se espera la conclusión de un suceso.
        * ``Preparado``: proceso que se puede ejecutar pero que está esperando por otro de mayor prioridad.
        * ``Muerto/terminado``: se termina la ejecución del proceso.

> ``PCB`` (Process Control Block): registro especial donde el sistema operativo agrupa toda la información que necesita conocer respecto a un proceso particular. Cada vez que se crea un proceso el sistema operativo crea el BCP correspondiente para que sirva como descripción en tiempo de ejecución durante toda la vida del proceso.

* Las operaciones de E/S son mucho más lentas que los procesos de cómputo, por lo tanto, el procesador estaría libre la
  mayor parte del tiempo, porque los procesos en memoria estarían en espera de esas operaciones.
* Para solucionar esto, la memoria principal puede expandirse para almacenar más procesos, a coste de mover parte o todo
  el proceso de memoria principal al disco secundario o una partición (swapping).
* Al hacer uso del swapping, se crea un nuevo estado llamado “suspendido”: el proceso esta en disco secundario listo
  para ser cargado a memoria principal cuando se le llame.

#### 3.1. PLANIFICACIÓN DE PROCESOS

* Tiene como objetivo obtener la mayor cantidad de trabajos realizados en una unidad de tiempo, la planificación es el
  conjunto de políticas y mecanismo incorporados al sistema operativo por el que se rige el orden en el que se completa
  el trabajo, se pretende: justicia en el reparto de la CPU, evitar la demora indefinida de los procesos, lograr la
  máxima capacidad de ejecución y el equilibrio en el uso de los recursos. Se puede planificar en función de los 3
  siguientes conceptos:
    * ``Alto nivel``: a que trabajos se les va a permitir competir activamente por los recursos del sistema.
    * ``Nivel intermedio``: que procesos se les puede permitir por la CPU, intentando siempre conseguir el mejor
      rendimiento.
    * ``Bajo nivel``: determinar qué proceso de los que están listos se les va a asignar la CPU.

##### 3.1.1. ALGORITMOS DE PLANIFICACIÓN

> ``Apropiativa`` (preemtive): interrupciones periódicas en las que el planificador toma el control y decide si el proceso sigue ejecutándose. No apropiativa: un proceso acapara la CPU y no la libera hasta que no finaliza.

* Su función consiste en repartir el tiempo disponible de un microprocesador entre todos los procesos que están
  disponibles para su ejecución.
* En principio, cualquier proceso monopoliza el microprocesador impidiendo que otros procesos se ejecuten, por ello, la
  primera misión de un algoritmo de planificación es expulsar el programa en ejecución cuando decida que es pertinente.
* El control del microprocesador pasa a manos del planificador gracias a que el hardware genera una interrupción.
* En este proceso de expulsión, se guarda el estado de ejecución del programa (programa y su estado se denomina
  contexto).
    * ``FIFO`` (First In First Out): algoritmo NO apropiativo, cuando un proceso llega a la cola de preparado se agrega
      su PCB al final de la lista, la CPU se otorga al primero de la lista y una vez que un proceso empieza a ejecutar
      no deja de hacerlo hasta que termina, el tiempo de espera será bastante alto.
    * ``SJF`` (Shortest Job First): algoritmo NO apropiativo, asocia a cada proceso el tiempo de CPU que necesitara en
      el siguiente ciclo y se decide por el más pequeño, el mayor problema radica en el cálculo del tiempo de CPU, el
      tiempo de espera para procesos largos puede ser excesivo.
    * ``Priority Scheduling``: asocia a cada proceso una prioridad para a continuación seleccionar el proceso con mayor
      valor de esta, hay dos tipos de prioridades, externa (definida a través del SO) e interna (definida por el tiempo
      de uso de la CPU). Se implementa un proceso de aumento de la prioridad con el envejecimiento de cola debido a que
      existe la posibilidad de la “muerte por inanición”.
    * ``Round Robin``: se basa en el uso del “quantum temporal” (pequeña unidad de tiempo o franja temporal que mide el
      tiempo máximo que un proceso puede hacer uso del procesador, al ocurrir una interrupción del reloj se llama al
      quantum y este le cede el control de la CPU al planificador).

#### 3.2. PROBLEMAS DE CONCURRENCIA

* Ocurren cuando dos o más procesos acceden a un recurso compartido sin control, de manera que el resultado combinado de
  este acceso depende del orden de llegada, hay varios tipos:
    * ``Inanición o aplazamiento indefinido``: ocurre cuando un proceso tiene una prioridad tan baja que nunca llega a
      ser trasladado a memoria principal
    * ``Condición de no apropiación``: si un proceso tiene asignado un recurso, dicho recurso no puede arrebatársele por
      ningún motivo, y n estará disponible hasta que le proceso lo suelte por su voluntad.
    * ``Condición de espera ocupada``: un proceso pide un recurso que ya este asignado a otro proceso y la condición de
      no apropiación se debe cumplir, entonces el proceso estará gastando el resto de su “time slice” comprobando si el
      recurso fue liberado.
    * ``Condición de exclusión mutua``: un proceso realiza operaciones sobre el recurso, después lo deja de usar. La
      sección de código que usa ese recurso se le llama región critica, la condición de exclusión mutua establece que
      solamente se permite a un único proceso estar dentro de la misma “región critica”. (se puede lograr entrar en la
      región critica con el algoritmo de Dekker y Peterson: algoritmo de programación concurrente para exclusión mutua
      que permite a 2 o más procesos compartir un recurso sin conflictos, utilizando tan solo memoria compartida para la
      comunicación).
    * ``Condición de espera circular`` (deadlock): se produce cuando en un conjunto de procesos, cada uno de ellos
      espera a un evento que solo puede generar otro del conjunto. Existen técnicas para prevenir el deadlock, como
      mecanismos para evitar que se presente alguna de las cuatro condiciones necesarias para el deadlock:
        * ``Asignar recursos en orden lineal``: si un proceso tiene el recurso con etiqueta menor que otro, este no
          puede pedir recursos a uno con etiqueta mayor. Con esto se evita la condición de espera ocupada.
        * ``Asignar todo o nada``: el proceso debe pedir todos los recursos que va a necesitar de golpe, y se le
          asignaran solamente si se le pueden dar todos.
        * ``Algoritmo del banquero``: se elabora una tabla de recursos existente e información del máximo de recurso de
          cada tipo que usa cada proceso y cuando un proceso pide un recurso se verifica si, asignándoselo, todavía
          quedan otros del mismo tipo de reserva.

### 4\. GESTIÓN DE MEMORIA

Los programas residen en el disco como ejecutables binarios, el conjunto de programas residentes en el disco esperando a
ser cargados en memoria forman la cola de entrada, los programas pueden direccionar memoria:  
``Direccionamiento en el momento de compilación``: generan código absoluto (siempre se ejecuta en una dirección de
memoria de inicio fija).  
``Direccionamiento en el momento de la carga``: maneja direcciones relativas, genera código localizable.  
``Enlace dinámico``: se retarda la edición del enlace hasta el momento de ejecución.  
``Overlays``: permite ejecutar un programa en un espacio de memoria menor que su tamaño.

#### 4.1. ADMINISTRACIÓN DE MEMORIA REAL

* ``Asignación contigua de almacenamiento``: cada archivo ocupa un conjunto de bloques contiguos en el disco a los que
  se les asigna ese espacio fijo en el momento de su creación (por lo que los archivos no pueden crecer).
* ``Multiprogramación de partición fija``: la memoria se divide en particiones de tamaño fijo, los compiladores y
  editores de enlaces generaban código localizable para que un programa pudiera ejecutarse en cualquier partición de
  memoria (
  suficientemente grande).
* ``Multiprogramación de partición variable``: cada programa el usuario emplea tanta memoria como sea necesaria siempre
  que quepa en el almacenamiento real, se van generando huecos en la memoria, estos huecos se pueden solucionar de
  varias formas:
    * ``Combinación``: cuando un programa termina su ejecución, el sistema operativo verifica si hay algún bloque de
      memoria contigua libre y los combina para generar un único bloque de memoria libre.
    * ``Compactación``: agrupa toda la memoria disponible en un único bloque al final. Como desventajas genera un alto
      consumo de CPU y obliga a detener la actividad del sistema.
* ``Colocación para el almacenamiento``: cuando a una petición se le asigna una nueva partición y sobra memoria el
  sistema operativo se da cuenta y deja este espacio sobrante como una nueva partición:
    * ``Best Fit``: los bloques de memoria son asignados según las necesidades del programa que se está ejecutando.
    * ``First Fit``: se asigna en la primera partición disponible en la que pueda entrar el programa, más rápida, pero
      se desperdicia mucho espacio de memoria.
    * ``Worst Fit``: se asigna en la partición en la que sobra más espacio.

#### 4.2. ALMACENAMIENTO EN MEMORIA VIRTUAL

* Las ``direcciones de memoria`` no están necesariamente contenidas en el almacenamiento real, el SO se apoya en el
  almacenamiento secundario para extender la capacidad de la memoria con direcciones virtuales, estas deben poder
  transformarse en direcciones reales mientras el proceso está en ejecución.
* La ``memoria virtual`` es la separación de la memoria lógica y de la memoria física, esta separación permite
  proporcionar a los programadores una gran memoria virtual cuando solo se dispone de una memoria física más pequeña. La
  memoria virtual facilita las tareas de programación, ya que el programador no se tiene que preocupar por la cantidad
  de memoria física disponible.

##### 4.2.1. ESTRATEGIAS DE REEMPLAZO DE MEMORIA VIRTUAL (PAGINACIÓN)

* Se denominan páginas a los bloques de memoria de igual tamaño y paginación a la administración del almacenamiento
  virtual asociado, si los bloques son de distinto tamaño hablamos de segmentos.
* Las páginas se transfieren del almacenamiento primario al secundario en bloques llamados “page frames”.
* La tabla de páginas de cada proceso puede llegar a ser demasiado grande, se buscan mecanismos que permitan acelerar el
  tiempo de repuesta como la utilización de un conjunto de registros dedicado, el “CPU Dispatcher” encargado de cargar y
  actualizar la información de estos registros en cada contexto.
* La solución más común es apoyarse en una cache de acceso muy rápida llamada TLB (Translation Location Buffer), puede
  contener algunas entradas de la tabla de páginas.
* Si en el momento de generarse un fallo no hubiera ningún frame disponible se procede a sustituir una página en
  memoria, algoritmos de sustitución de página:
    * ``Política óptima``: selecciona para reemplazar la página que tiene que esperar una mayor cantidad de tiempo hasta
      que se produzca la referencia siguiente. Este algoritmo es imposible de implementar, ya que requiere que el
      sistema operativo tenga un conocimiento exacto de los sucesos futuros. Sin embargo sirve como un estándar para
      comparar otros algoritmos.
    * ``FIFO`` (First In First Out): asocia a cada página el momento en que fue cargada en memoria, se selección ala que
      hace más tiempo que está en memoria.
    * ``LRU`` (Least Recently Used): se selecciona la página que hace más tiempo que no se emplea. Se necesita almacenar
      el momento temporal de la última actualización de cada página:
        * ``Contadores``: se asocia a cada entrada en la tabla de páginas el momento de la última vez que se usó, cada
          vez que se accede a una página se actualiza el contador.
        * ``Stack``: lleva una pila con los numero de cada página, cada vez que se accede a una página se coloca en el
          tope, en la cima de la pila estará la página que fue utilizada por última vez y en el fondo la que hace más
          tiempo que no se accede.
    * ``Paginación por demanda``: “Swapping”, cuando un proceso va a ser ejecutado, el mismo es paginado a la memoria,
      empleando la técnica lazy swapping, se necesita determinar si una página está en memoria o en disco, se emplea el
      bit “valido/invalido”.
    * ``Segunda oportunidad``: variante de FIFO, cada vez que se selecciona una página se inspecciona un bit de
      referencia, si el valor es cero se procede a sustituir la página, si el valor es uno, se da una segunda
      oportunidad a la página y se selecciona el siguiente candidato por criterio FIFO, cada vez que una página recibe
      una segunda oportunidad se cargar un cero en el bit de referencia.
    * ``LFU`` (Least Frequently Used): la página con menos cantidad de referencias debe ser sustituida.
    * ``MFU`` (Most Frequently Used): la página con mayor cantidad de referencias es la sustituida.
    * ``Page Buffering``: se mantiene una cola de “frames”, cuando ocurre un fallo de página se elige una víctima
      empleando alguno de los mecanismos ya vistos, en lugar de hacer el cambio de frame en una sola operación se carga
      la página en memoria y el SO descarga la página y la agrega a la cola de “frames”.

> ``Hiperpaginación`` (thrashing): situación en la que se utiliza una creciente cantidad de recursos para hacer una cantidad de trabajo cada vez menor cuando se cargan y descargan sucesiva y constantemente partes de la imagen de un proceso desde y hacia la memoria principal y la memoria virtual. Cuando se produce hiperpaginación, los ciclos del procesador se utilizan en llevar y traer páginas (o segmentos, según sea el caso) y el rendimiento general del sistema se degrada notablemente.

## SISTEMAS OPERATIVOS EN RED

### 1\. TIPOS DE REDES DE ÁREA LOCAL

* Las redes se dividen en dos categorías dependiendo del tamaño de la organización, nivel de seguridad requerido, nivel
  de soporte administrativo, tráfico de la red...
    * ``Redes Workgroup``: no hay servidores dedicados ya que implica un pequeño grupo de personas, máximo diez equipos
      y no existe una jerarquía entre ellos. Todos los equipos son iguales (peers), cada equipo actúa como cliente y
      servidor no hay necesidad de un potente servidor central ni de software adicional, el usuario de cada equipo
      determina los datos de dicho equipo que van a ser compartidos en la red. Los equipos están en las mesas de los
      usuarios, estos actúan como sus propios administradores y planifican su propia seguridad, están conectados por un
      sistema de cableado simple. La seguridad no es fundamental.
    * ``Redes basadas en Servidor``: la mayoría de las redes tienen servidores dedicados, es aquel que funciona solo
      como servidor y no se utiliza como cliente o estación, están optimizados para dar servicio con rapidez a
      peticiones de los clientes, garantizar la seguridad de los archivos y directorios, la división de tareas de la red
      entre varios servidores asegura que cada tarea será realizada de la forma más eficiente posible. Servidores
      especializados:
        * De ``archivos e impresión``: gestionan el acceso de los usuarios y el uso de recursos de archivos e impresión,
          al ejecutar una aplicación de tratamientos de textos, dicha aplicación se ejecuta en su equipo. El documento
          de tratamiento de textos almacenado en el servidor de archivos e impresión se cargar en la memoria de su
          equipo de forma local, los servidores de archivos e impresión se utilizan para el almacenamiento de archivos y
          datos.
        * De ``aplicaciones``: en un servidor de aplicaciones la base de datos permanece en el servidor y solo se envían
          los resultados de la petición al equipo que realiza la misma, una aplicación cliente que se ejecuta de forma
          local accede a los datos del servidor de aplicaciones, solo se pasara el resultado de la consulta desde el
          servidor a su equipo local.
        * De ``correo``: funcionan como servidores de aplicaciones, datos encargados de forma selectiva del servidor al
          cliente.
        * De ``fax``: gestionan el tráfico de fax hacia el exterior y el interior de la red, compartiendo una o más
          tarjetas modem fax.
        * De ``comunicaciones``: gestionan el flujo de datos y mensajes de corro entre las propias redes de los
          servidores o usuarios remotos que se conectan a los servidores utilizando módems y líneas telefónicas.
        * De ``servicios de directorio``: permiten a los usuarios localizar, almacenar y proteger información en la red.

#### 1.1. PARTES DE UNA RED BASADA EN SERVIDOR

* Al igual que un equipo no puede trabajar sin un SO, una red de equipos no puede funcionar sin un SO de red.
* Este es el ejemplo más familiar y famoso donde el software de red del equipo cliente se incorpora en el SO del equipo.
* El equipo personal necesita ambos SO para gestionar conjuntamente las funciones de red y las funciones individuales.
* El SO de un equipo coordina la interacción entre el equipo y los programas que está ejecutando.
* Controla la asignación y utilización de los recursos hardware (memoria, CPU, espacio de disco, periféricos...).
* En un entorno de red, los servidores proporcionan recursos a los clientes de la red y el software de red del cliente
  permite que estos recursos estén disponibles para los equipos clientes.
* Elementos principales:
    * ``Software de cliente``: en un sistema autónomo, en un entorno de red, cuando un usuario inicia una petición para
      utilizar un recurso que está en un servidor, la petición se tiene que enviar o redirigir desde el bus local a la
      red y desde allí al servidor que tiene el recurso solicitado, este envío es realizado por el “redirector” (se
      inicia en un equipo cliente cuando el usuario genera la petición de un recurso o servicio de red). El equipo del
      usuario se identifica como cliente, puesto que está realizando una apetición a un servidor, este procesa la
      conexión solicitada por los redirectores del cliente y les proporciona acceso a los recursos solicitados.
    * ``Software de servidor``: permite a los usuarios en otras máquinas y a los equipos clientes, poder compartir los
      datos y periféricos del servidor incluyendo impresoras, trazadores y directorios. Si un usuario solicita un
      listado de directorios de un disco duro remoto compartido. El redirector envía la petición al servidor de archivos
      que contiene el directorio compartido. Se concede la petición y se proporciona el listado de directorios.
    * ``Periféricos``: los redirectores pueden enviar peticiones a los periféricos, con el redirector podemos
      referenciar como LPT1, COM1 o USB1 impresoras de red en lugar de impresoras locales. El redirector intercepta
      cualquier trabajo de impresión y lo envía a la impresión de red especifica. La utilización del redirector permite
      a los usuarios no preocuparse ni de la ubicación actual de los datos o periféricos. Para acceder a los datos de un
      ordenador de red el usuario solo necesita escribir el designador de la unidad asignado a la localización del
      recurso y el redirector determina el encaminamiento actual.
    * ``Gestión de usuarios``: los SO permiten al administrador de la red determinar las personas o grupos de personas
      que tendrán la posibilidad de acceder a os recursos de la red así como crear permisos de usuario controlados por
      el SO de red, asignar o denegar permisos de usuario de red, eliminar usuarios de la lista de usuario que controla
      el SO de red... Para simplificar la tarea de gestión de usuarios el SO permite la creación de grupos de usuarios.
      Clasificando los individuos en grupos todos los miembros de un grupo tendrán los mismos  
      permisos asignados al grupo como una unidad.
    * ``Compartir recursos``: termino para describir los recursos que públicamente están disponibles para cualquier
      usuario de la red, la mayoría de los SO también pueden determinar el grado de compartición permitiendo diferentes
      usuarios con diferentes niveles de acceso a los recursos y coordinación en el acceso a los recursos asegurando que
      dos usuarios no utilizan el mismo recurso en el mismo instante.
    * ``Gestión de la red``: algunos SO de red avanzados incluyen herramientas de gestión ayudan a controlar el
      comportamiento de la red, estas herramientas de gestión permiten detectar síntomas del problema y presentar estos
      síntomas en un gráfico, el administrador de la red puede tomar la decisión correcta antes de que el problema
      suponga la caída de la red.

> ``Script de inicio de sesión``: especifica el nombre de la secuencia de comandos de inicio de sesión que va a utilizar esta cuenta de usuario. Están almacenadas en el recurso compartido NETLOGON. Variables de secuencias de comando de inicio de sesión: %homedrive%: unidad de disco que contiene el directorio principal del usuario en la estación de trabajo local. %homepath%: directorio principal del usuario. %os%: SO del usuario. %processor\_architecture%: tipo de procesador de la estación de trabajo. %processor\_level%: nivel de procesador de la estación de trabajo. %userdomain%: domino donde está definida la cuenta. %username%: nombre del usuario de la cuenta.

## UNIX

### 1\. CONCEPTOS BÁSICOS

* La última versión soporta cuatro intérpretes de ordenes (shells):
    * ``Shell Bash``: se escribió como proyecto para GNU, para proveerlo de un superconjunto de funcionalidad con la
      Shell Bourne.
    * ``Shell Job``: incorpora características de control de trabajos al shell estándar.
    * ``Shell Korn``: ofrece un superconjunto de las características dl Shell del sistema, incluyendo historial de
      órdenes, edición de línea de orden y características ampliadas de programación.
    * ``Shell C``: procedente del sistema BSD, comparte capacidad de control de trabajos, historia de órdenes, capacidad
      de edición...

> ``LTS`` (Long Term Support): termino usado para nombrar ediciones diseñadas para tener soporte durante un período más largo que el normal, unos 5 años. Se aplica particularmente a los proyectos de software de código abierto, como Linux. En el ámbito de los sistemas basados en este núcleo, el término se usa en algunas versiones de distribuciones como Debian o Ubuntu, entre otras.

* Niveles de ``directorios`` más importantes:
    * ``/``: raíz, donde empieza el árbol de directorios.
    * ``/bin``: residen los comandos ejecutables.
    * ``/sbin``: residen los comandos ejecutables reservados para el (root).
    * ``/lib``: librerías compartidas por los distintos compiladores e intérpretes.
    * ``/usr``: residen los programas de usuario y aplicaciones instaladas, con los subdirectorios siguientes:
        * ``/usr/lib``: librerías utilizadas por dichas aplicaciones, enlaces simbólicos a las de /lib.
        * ``/usr/bin``: ejecutables de las aplicaciones.
        * ``/usr/sbin``: ejecutables reservados para la administración del software.
    * ``/dev``: directorio en el que se alojan los distintos dispositivos (devices), estos ficheros actúan como
      interfaces de comunicación entre la shell y el dispositivo físico.
    * ``/etc``: mayor parte de los programas y fichero de configuración del sistema.
    * ``/var``: ficheros que varían de tamaño dinámicamente a lo largo de la ejecución de procesos del sistema, dos
      subdirectorios importantes:
        * ``/var/spool``: colas de procesos
        * ``/var/log``: registros de actividad. (auth.log)
    * ``/proc``: el file system virtual, aloja información como los procesos activos en el sistema.
    * ``/home``: donde se sitúan los directorios de trabajo e los distintos usuarios.
    * ``/root``: directorio de trabajo del administrador (root).
    * ``/mnt``: punto de montaje de dispositivos extraíbles.
    * ``/tmp``: donde se sitúan los ficheros temporales generados por el sistema.

> ``Saltstack``: es un software de código abierto basado en Python para la automatización de IT impulsada por eventos, la ejecución de tareas remotas y la gestión de la configuración, usa por defecto el puerto 4505\.

* ``Tipos de archivos:``
    * ``\-``: fichero ordinario (fichero de texto, binario ejecutable, fichero de datos...).
    * ``d``: directorio (equivalente en Windows a una carpeta).
    * ``l``: enlace simbólico (equivalente en Windows a un enlace directo).
    * ``b``: dispositivo de bloques (interface de conexión de disco duro, unidad de CD...).
    * ``c``: dispositivo de caracteres (puerto, modem...).
    * ``s``: dispositivo especial de caracteres.
    * ``.``(punto): carpeta actual.

#### 1.1. SISTEMAS DE FICHEROS

* Es la parte más visible del sistema operativo: almacenamiento de la información en el sistema, define una unidad
  lógica de almacenamiento: el archivo.
* Podemos definir un sistema de ficheros en cada unidad de almacenamiento física o incluso varios sistemas de ficheros
  creando particiones con la orden fdisk, dividimos la unidad física en unidades lógicas (
  particiones), para así poder administrar el espacio disponible con más precisión, “fdisk” no crea sistemas de
  ficheros, para esta tarea utilizaremos la orden “mkfs”.
* UNIX se suele dividir en cuatro partes diferenciadas entre sí:
    * ``Bloque boot``: contiene el programa para iniciar el sistema operativo.
    * ``Superbloque``: contiene información relativa al sistema de ficheros (un indice) como el espacio disponible, es
      espacio total, el tipo de sistema...
    * ``Lista de inodos``: referencia de los inodos del sistema, información administrativa relativa a ficheros. El
      inodo sirve como interface entre el núcleo del SO y la información almacenada en el dispositivo. Los campos que
      conforman la estructura del inodo son:
        * Dueño del fichero.
        * Tipo de fichero.
        * Permisos.
        * Enlaces del archivo.
        * Fecha de la última modificación.
    * ``Área de datos``: parte del dispositivo lógico donde vamos a poder almacenar información.

#### 1.2. CREACIÓN E INCORPORACIÓN DE SISTEMAS DE FICHEROS

* Una vez creado un sistema de ficheros mediante la orden “mkfs” necesitamos incorporar ese sistema de ficheros a la
  estructura jerárquica de nuestro sistema UNIX (llamado montar un sistema), para ello se usa la orden mount (mount:
  opciones:dispositivo:punto\_montaje).
* Para especificar el tipo de File System “-t tipo\_fs” (en Linux), “F tipo\_fs” (en Solaris) ... Otro tipo de opción es
  “-o” y especificar “ro” (read only), rw (lectura-escritura), suid (si acepta suid), ...
* El dispositivo es la entrada de /dev que utilizaremos como interface del dispositivo físico y el punto\_montaje es el
  directorio del árbol en el que se hará accesible, si no especificamos el tipo de file system, el comando mount
  asignará por orden secuencial de aparición en /proc/filesystems el tipo más adecuado.
* Si montamos un dispositivo sobre un punto de montaje ocupado por otro, el sistema oculta automáticamente el directorio
  antiguo, mostrando el nuevo.
* Proceso para desmontar un dispositivo, ejecutar la orden unmount (unmount:punto\_montaje) y para desmontar un file
  system ninguno de los procesos del sistema puede estar utilizando sus recursos.

    * Cuando arranca el sistema debe tener por lo menos un sistema de ficheros: el directorio raíz, ya montado.
    * Los sistemas de ficheros que se montan de modo automático la arrancar el sistema, se especifican en ficheros del
      estilo /etc/fstab (en Linux). La organización de estos ficheros son entradas con la sintaxis (device:
      punto\_montaje:tipo\_fs:opciones:freq:passno), device es el dispositivo que enlaza al sistema de ficheros,
      punto\_montaje es el directorio en el que se hará accesible, tipo\_fs es el tipo de fs que vamos a usar,
      opciones (la opción “auto” provoca que la ejecución de los scripts de arranque monte el dispositivo en cuestión
      durante el proceso de arranque.
    * Si no está especificada la opción auto solo se preparará al FS para un montaje más automatizado en ejecución),
      freq es la frecuencia de volcado y passno orden en que se chequean los sistemas de archivos con “fsck” al arrancar
      la máquina. Puede haber dos entradas especiales:
        * ``swap``: no necesita punto de montaje.
        * ``/proc``: no está asociado a ningún dispositivo físico de la máquina ya que es un FS virtual que actúa como
          interface entre las estructuras de datos del kernel y las aplicaciones.

##

* > ``BitLocker``: provee de cifrado del disco completo, está diseñado para proteger los datos al proporcionar cifrado para volúmenes enteros. Por defecto se utiliza el algoritmo de cifrado estándar AES en modo CBC con una clave de 128 bits. Tres mecanismos de autenticación:
    * > Modo de funcionamiento transparente:
        * > Este modo aprovecha las capacidades del módulo de plataforma de confianza (en inglés, Trusted Platform Module, TPM).
        * > La clave utilizada para el cifrado de disco está cifrada y solo se dará a conocer el código al sistema operativo si los archivos de inicio a principio del arranque no han sido modificados.
        * > Este modo es vulnerable a un ataque de arranque en frío, ya que permite el apagado de la máquina por un atacante.
    * > Modo de autenticación de usuario:
        * > Este modo requiere que el usuario proporcione alguna de autenticación al prearranque.
        * > Este modo es vulnerable a un ataque rootkit (conjunto de software que permite un acceso de privilegio continuo “root” a un ordenador pero que mantiene su presencia activamente oculta al control de los administradores al corromper el funcionamiento normal del sistema operativo o de otras aplicaciones).
    * > Modo en dispositivos USB:
        * > El usuario debe insertar un dispositivo USB que contenga una clave de inicio en el equipo para poder arrancar el sistema operativo protegido.
        * > Tenga en cuenta que esta modalidad requiere que la BIOS de la máquina protegida acepte el arranque desde dispositivos USB.
        * > Este modo también es vulnerable a un ataque rootkit.

##

#### 1.3. TIPOS DE SISTEMAS DE FICHEROS

* ``ReFS`` (Resilient File System): se introdujo con Windows Server 2012, es transaccional, sus metadatos y archivos se
  organizan en tablas, de manera similar a una base de datos relacional.
    * Mejora la fiabilidad de las estructuras en disco.
    * Capacidad de resiliencia incorporada.
    * Compatibilidad con APIs y tecnologías existentes (Bitlocker\*, ACLs...)

* ``EXT4`` (Extended Filesystem 4): sistema de archivos transaccional (con jounaling), menor uso del CPU, mejoras en la
  velocidad de lectura y escritura,...
    * Extents: conjunto de bloques físicos contiguos, mejora el rendimiento de ficheros de gran tamaño y reduce
      fragmentación.
    * Compatibilidad con EXT3 sin necesidad de cambios de disco.
    * Asignación persistente de espacio en el disco: permite la reserva de espacio en disco para un fichero.
    * Asignación multibloque: permite asignar los bloques para un fichero en una sola operación, lo que reduce la
      fragmentación.

> ``e2fsck``: comprueba la integridad de un sistema de ficheros ext3.

* ``ReiserFS`` (Reiser File System): sistema de propósito general, soportado por Linux y Windows, soporta journaling y
  reparticionamiento.
    * Tail packing, un esquema para reducir la fragmentación interna.

> ``rsync``: herramienta de copia y sincronización de archivos en Unix.

#### 1.4. LOGIC VOLUME MANAGER (LVM)

* ``PV``: puede ser cualquier tipo de dispositivo de almacén, pasa a llamarse Physical Volume.
    * pvcreate dev “disco, partición...”
    * pvdisplay (permite ver información del PV)
    * pvresice (redimensiona el tamaño del LV)
* ``VG``: agrupa varios PV, funciona como una agrupación de discos que puede expandirse “en caliente”.
    * vgcreate “nombre del vg” disco, partición...
    * vgextend “disco a incorporar”
    * vgreduce “disco a retirar”

* ``LV``: partición del VG, entendido ya como almacenamiento lógico. o lvcreate \-L “tamaño” “vg al que pertenece”

### 2\. ENLACES DIRECTOS EN UNIX

* Un inodo es un bloque especial de disco de 64 bytes que almacena las propiedades de un fichero (tamaño del fichero, id
  del usuario, permisos...), existen tantos inodos como ficheros existen en el sistema.
* Tipos de enlaces:
    * ``Enlace simbólico``: entradas del sistema de ficheros que apuntan a otra entrada (accesos directo), no conservan
      el inodo, pero si conserva los permisos del fichero original.

        * > Para crear un enlace simbólico a un ``inodo`` se usa “ln \-s origen destino” (siendo “origen” el fichero existente y “destino” el nombre del nuevo enlace).

    * ``Enlaces fuertes``: es otra entrada de directorio que referencia al mismo inodo. Solo se pueden hacer enlaces
      fuertes entre ficheros del mismo dispositivo de almacenamiento (no se pueden saltar puntos de montaje).
        * \-i: averigua el número de inodo de un fichero.
        * \-l: número de enlaces fuertes a un inodo.

        * > Un enlace fuerte “ln origen destino” (siendo “origen” el fichero existente y “destino” el nombre del nuevo enlace). Si borramos el fichero original, el enlace simbólico permanece en el sistema de ficheros, no referenciado (entrada inútil).

### 3\. PERMISOS

* Solo el propietario y el administrador tienen permiso para modificar el mapa de permisos de un fichero, para ellos se
  usa la orden “chmod”:
    * ``r``: permiso de lectura.
    * ``w``: permiso de escritura o modificación, así como añadir o borrar ficheros de un directorio.
    * ``x``: permiso de ejecución.

* ``Se organizan en tres bloques``:
    * ``Tres primeros``: afectan al propietario (u) del fichero.
    * ``Tres segundos``: afectan al grupo (g) principal al que pertenece el usuario.
    * ``Tres últimos``: afecta al resto de usuarios (o).

* En el momento de su creación los ficheros y los directorios obtienen una serie de ``permisos por defecto``:
    * ``666`` (rw-rw-rw-): mapa total que afecta a los ficheros por defecto del sistema.
    * ``777`` (rwxrwxrwx): mapa total que afecta a los directorios por defecto del sistema.

#### 3.1. PERMISOS ESPECIALES

* Para cambiar la contraseña de usuario ejecutamos la instrucción “passwd” esta actualiza el fichero /etc/passwd o en el
  /etc/shadow, pero por defecto el usuario no tiene permiso de escritura en ese fichero, esta situación se resuelve con
  el uso del bit ``SUID`` (peso 4\) y ``GUID`` (peso 2), su función es asociar al proceso lanzado por el usuario (o el
  grupo)
  los permisos y privilegios del propietario del programa ejecutable, así el sistema entiende que quien está intentando
  modificar los fichero sea root, y se le permite realizar la modificación.
* Sticky bit (bit de permanencia): es un bloqueador del fichero, protegiéndolo contra agresiones involuntarias,
  cualquier usuario puede crear ficheros dentro del directorio con sticky bit, pero solamente el propietario puede
  eliminarlos (peso 1).
    * Estos permisos valen tanto para aumentar como para disminuir privilegios.
    * Para poner o quitar los bits SUID, SGID y Sticky, se usa la formula “chmod u (user) /g (group) /o (other) ± s
      (SUID) /t (Sticky)”.

### 4\. PROCESO DE ARRANQUE DE UNIX

* 1\. Chequeo inicial del sistema por las rutinas ROM almacenadas en la máquina.
* 2\. Carga de una boot-prompt (gestor de arranque) que permita localizar el núcleo de un sistema operativo UNIX (LILO
  en caso de Linux).
* 3\. Carga del núcleo del sistema.
* 4\. Carga del proceso “init” padre de todos los procesos, establece el runlevel (conjunto de servicios referenciados
  por una letra o número) por defecto, y pone disponibles los servicios en el sistema.

##

* > ``GNU GRUB`` (GNU GRand Unified Bootloader): es un gestor de arranque multiple usado en GNU/Linux y Solaris.
* > Alrededor de 2002 investigadores japoneses empezaron a trabajar en PUPA (siglas de Preliminary Universal Programming Architecture), cuyo objetivo era reescribir el cuerpo de GRUB para hacerlo más claro, seguro, robusto y poderoso.
* > ``PUPA`` fue posteriormente renombrado a GRUB 2, y la versión original de GRUB fue renombrada a GRUB Legacy.

##

* ``Sistemas de inicio``:
    * ``upstart``: desarrollado por Ubuntu, mejora la gestión de los disipativos que se conectan en caliente.
    * ``systemd``: utilizado en Fedora y Mandriva, arranque más rápido al iniciar los servicios en paralelo.

##

* > ``Xfce``: entorno de escritorio libre para sistemas tipo Unix como GNU/Linux, BSD, Solaris y derivados.
* > Es rápido y ligero, sin dejar de ser visualmente atractivo y fácil de usar.

##

* ``Runlevels estándar`` (En cada uno de estos niveles init lanza servicios que se indican en el fichero
  “/etc/inittab”):
    * 0: Maquina apagada o boot-prompt.
    * 1 o “S”: Single-user.
    * 2: Multiuser sin NFS (sin red).
    * 3: Multiuser con NFS y con entorno gráfico).
    * 4: sin uso especifico.
    * 5: apagar la máquina.
    * 6: reinicio del sistema.

* ``Sintaxis``: son un conjunto de registros con la estructura (ID:runlevels:acción:comando), uno de los comandos que se
  ejecutan durante el establecimiento del runlevel es rc, invoca al directorio del runlevel indicado, se localizan
  enlaces simbólicos a los scripts de inicialización de los servicios que se sitúan en /etc/init.d, para cambiar de un
  runlevel a otro se usa “init n” (siendo “n” el runlevel al que queremos acceder). Estos enlaces simbólicos tienen la
  sintaxis: “KXXfile” o “SXXfile” donde “K” indica para el servicio, “S” indica levantar el servicio y “XX” un numero de
  prioridad.

* Una vez finalizado el proceso de arranque se nos presentara una login-prompt donde podemos lanzar una sesión de
  usuario.

> ``who \-r``: indica el runlevel actual.

### 5\. USUARIOS Y GRUPOS

* ``Cuentas de usuario``: cada usuario tiene una cuenta home asociada, con acceso completo a este directorio, lo que
  implica que podrá crear, borrar y almacenar ficheros en este directorio.
* El usuario está en por lo menos un grupo (grupo principal), puede estar en más grupos (secundarios), el listado de
  usuarios y sus asignaciones a grupos se almacenan en /etc/passwd (listado de usuarios, un registro para cada usuario
  del sistema con la estructura de campos):\[alias:pw\_encript:UDI:GID:datos descriptivos:home\_directory:
  default\_shell\]
* La modificación de cuentas de usuario se efectúa con el comando usermod, este modifica las características de una
  cuenta de usuario ya existente, modifica por ejemplo:
    * ``/etc/shadow``: fichero adicional donde se almacenan los passwords encriptados y los datos para la expiración de
      contraseñas. (también se usa el comando “chage” SIN “N” para cambiar la fecha de expiración de contraseñas ``-e``,
      ver el último cambio de contraseña ``-l (ele)``...).
    * ``/etc/groups``: contiene toda la información de pertenencia a grupos.
    * ``/etc/gshadow``: similar al fichero shadow de contraseñas, contiene los grupos, contraseñas y miembros.
    * ``/etc/login.defs``: definir valores por defecto para diferentes programas como useradd.
    * ``/etc/shells``: contienen un alista de shells válidos.

* ``Cuentas de grupo``: proporcionan un método para vincular a usuarios similares, agrupándolos para agrupar un conjunto
  de cuentas de usuario de características similares con el propósito de aplicar directivas de seguridad parecidas a
  ellas, las cuentas de grupo son similares a las cuantas de usuario y se definen en un único fichero /etc/groups que
  contiene una lista con todos los grupos y sus correspondientes miembros, los grupos también poseen un nombre y un GID.
* Cuando un usuario se conecta al sistema Linux lo hace dentro de su grupo primario, este es el grupo al que el usuario
  pertenece por defecto, si un usuario quiere acceder a fichero so ejecutar programas que no están en su grupo primario,
  debe conmutar de grupo aquel que este asociado con los ficheros a los que quiere acceder o con los programas que
  quiere ejecutar. Solamente el root puede crear y administrar grupos, para crear un nuevo grupo en Linux se utiliza el
  comando groupadd, para crear nuevos usuarios el comando useradd y para modificar grupos ya existentes se usa el
  comando gpasswd:
    * \-M: para asignar miembros a un determinado grupo.
    * \-a nombreUsuario: añadir un usuario al grupo.
    * \-d nombreUsuario: eliminar un usuario del grupo especificado.
    * \-r: elimina la contraseña del grupo.
    * \-R: indica que no se puedan añadir usuarios nuevos el grupo especificado con el comando newgrp.
    * \-A nombreUsuario: el usuario root pueda especificar que usuarios tienen privilegios para añadir o eliminar
      usuarios de los grupos, especificar las contraseñas de grupo, este sobrescribe cualquier lista previa. Implica que
      todos los nombres de usuario se deben introducir con esta opción.

> ``groups``: se utiliza para mostrar los grupos a los que pertenece el usuario en un determinado momento, “root” es miembro de todos los grupos por defecto.

* ``Cuenta de root``: se crea por defecto durante la instalación del SO, es la cuenta que utiliza el administrador del
  sistema para realizar cualquier tarea administrativa en el sistema Linux, se puede usar:
    * ``Accediendo al sistema con la cuenta “root”``: se puede utilizar para acceder al equipo directamente a través de
      consola, solamente se puede realizar a través de la consola principal, una vez logueado, cualquier acción que se
      realice en el sistema es llevada a cabo como “root”.
    * ``Comando SU``: se puede utilizar para adquirir temporalmente los privilegios de superusuario para realizar tareas
      administrativas o para ejecutar programas que requieran privilegios de superusuario, se solicitara la contraseña
      de roo y si es correcta se obtendrán lo privilegios, el comando SU puede utilizarse también para conmutar a otras
      cuentas de usuario.
    * ``Comando SUDO``: permite a un administrador seleccionar ciertos comandos que pueden ser tecleados sin ser “root”
      que de otra forma requerirían los privilegios de superusuario, esto se hace editando el fichero ``/etc/sudoers`` y
      especificando que usuario y que comandos podrán ejecutar dichos usuarios sin convertirse en root.
    * ``Ficheros SUID root``: es posible seleccionar un fichero que se ejecute como si fuese lanzado por el ``“root”``
      pese a que haya sido ejecutado por cualquier otro usuario del sistema.

### 6\. MANEJO DE LA SHELL

* Cuando iniciamos sesión en UNIX, se ejecutan una serie de instrucciones contenidas normalmente en los ficheros
  ``.profile`` (en estos ficheros se personaliza el entorno de usuario, configurando variables de ambiente y alias.
* La shell ofrece una prompt, puede ser:
    * ``\#``: prompt de root.
    * ``$``: prompt de usuario en las principales Shell de UNIX (Bourne, Bash, Korn).
    * ``%``: prompt de usuario en la C-Shell.

* Las órdenes del Shell pueden ser internas o externas, el tratamiento que recibe una orden es el de una subshell, el
  proceso padre es la shell.
    * ``Orden interna`` es aquella cuyo código está integrado en el shell:
        * bg, fg, cd, exec, exit, echo…
    * ``Orden es externa`` si su código reside en un archivo:
        * more, cat, mkdir, ls, grep...

#### 6.1. ÓRDENES DE USUARIO EN UNIX

* ``Control``:
    * ``CTRL+c``: termina un comando.
    * ``CTRL+d``: End Of File (fin de fichero).
    * ``CTRL+u``: borra la línea de comandos.

* ``Páginas Man:``
    * ``intro``: desplaza una línea.
    * ``space``: siguieinte pantalla.
    * ``f``: avanza una pantalla.
    * ``q``: sale de las páginas MAN.

### 7\. COMANDOS UNIX

* ``pwd`` (print working directory): directorio de trabajo actual.
* ``who``: listado de usuarios conectados a nuestro sistema.
* ``id user``: muestra el UID y el GID del usuario especificado, sin parámetros muestra información de uno mismo.
* ``passwd user``: permite cambiar la password de usuario user.
* ``uname``: muestra información sobre el sistema actual:
    * \-a: información en formato largo.
    * \-s: nombre del sistema operativo.
    * \-n: nombre de la estación de trabajo
* ``su user``: abre una sesión de user en una subshell de la shell de usuario. Utilizado sin parámetros abre una sesión
  de root (pidiendo la password).
* ``sudo`` comando: ejecuta un comando con los permisos de root.
* ``mkdir`` directorio: crea un directorio.
* ``rmdir``: borra un directorio.
* ``rm`` file o ``rm \-r`` dir: borra un fichero.
* ``cd``: directorio\_destino: se desplaza al directorio de destino.
* ``ls`` directorio: muestra el contenido de un directorio.
    * \-a: muestra todos los ficheros.
    * \-l: listado completo (muestra las propiedades de cada archivo).
    * \-i: muestra el número de inodo.
* ``free``: muestra datos sobre la memoria del sistema
* ``df`` (disk free): detalla el espacio total, ocupado y libre del sistema
* ``du`` (disk usage): muestra el uso en disco que realiza un conjunto de archivos en los directorios existentes.
* ``dd``: permite copiar y convertir datos de archivos a bajo nivel
    * if (input file): lee desde el archivo indicado como origen
    * of (output file): escribe al archivo indicado como destino
    * bs: indica el tamaño de bloque en bytes (por defecto)
    * count: copia el número indicado de bloques del archivo
* ``watch``: ejecutar cualquier comando arbitrario a intervalos regulares.
* ``ss``: se utiliza para volcar estadísticas de sockets (permite mostrar información similar a netstat).
* ``whereis``: localiza el archivo binario, el código fuente y la página de manual de un determinado comando.
    - Ejemplo: `whereis ls`
* ``which``: comando de búsqueda que lista la ruta completa de un comando.
    - Ejemplo: `which python3` → `/usr/bin/python3`
* ``touch``: crea un fichero vacío desde el terminal de linux, si el fichero existe le cambia la fecha y hora de
  modificación.
* ``nmap``: herramienta de exploración de red y escáner de seguridad/puertos.
    - Ejemplo: `nmap 192.168.1.1`
* ``top`` (comando linux): monitoreo de procesos y tareas, varias herramientas dedicadas:
    * ``htop``: monitoreo de CPU
    * ``iotop``: monitoreo de la información de E/S del disco
    * ``iftop``: monitoreo de red
        - Ejemplo: `top`
        - ``htop`` → interfaz mejorada.
        - ``iotop`` → uso de disco.
        - ``iftop`` → uso de red.

#### 7.1. Comandos de manejo de ficheros:

* ``cat`` file1 file2: concatena los ficheros mostrándolos por pantalla.
* ``pg`` file: muestra el contenido del fichero file y a continuación la prompt.
* ``head / tail`` ± n file: muestra las n (primeras o últimas líneas) del fichero.
* ``wc`` file: muestra el número de caracteres (-m), líneas (-l), palabras (-w) o bytes (-c) del fichero.
* ``cmp`` file1 file2: localiza la primera diferencia entre los ficheros.
* ``file`` file: informa sobre el tipo de fichero (ASCII, binario, ejecutable...).
* ``cp / mv`` fichero\_origen fichero\_destino: copia / mueve el fichero origen con el nombre y posición del fichero
  destino.
* ``sort`` file: ordena alfabéticamente las líneas (registros) del fichero.

#### 7.2. Comandos de búsqueda de información:

* ``find`` ruta patrón acción: busca los archivos que coincidan con el patrón en la ruta especificado y ejecuta la
  acción indicada.
    * ``ruta``: lugar donde empieza la búsqueda
    * ``patrón``: criterio de búsqueda (-name, \-size, \-type, \-mtime (mide el tiempo transcurrido desde hoy hasta el
      parámetro...)).
    * ``acción``: acción a realizar (-print, \-exec, \-copy, \-delete...).
        - Ejemplo: `find /home -name "*.txt"`
        - Ejemplo: `find . -type f -size +10M`

* ``grep / fgrep`` (no reconoce metacaracteres) / egrep patrón fichero: busca patrón en ficheros.
    * ^: seguido de una letra indica las líneas que empiezan por esa letra.
    * $: precedido de una letra indica todas las líneas que acaba por esa letra.
    * \*: a\* equivale a “aa”, a\*\*\* equivale a “aaaa”.
        - Ejemplo: `grep "ERROR" log.txt`
        - Ejemplo: `egrep "^(a|b)" palabras.txt` (líneas que empiezan por a o b)

#### 7.4. Comandos VI: editor de texto en consola.

* ``w``: guardar los cambios pero no sale del editor.
* ``wq``: guarda los cambios y sale del editor.
* ``q!``: sale del editor sin guardar los datos.

> ``less``: visualizador de archivos de texto, funciona en intérpretes de comandos UNIX.

### 8. METACARACTERES (caracteres especiales que cumplen funciones dentro de la Shell)

* ``*``: sustituye cualquier cadena de caracteres.
    - Ejemplo: `ls *.txt` → lista todos los ficheros terminados en `.txt`.

* ``[rango]``: sustituye cualquier carácter descrito en el rango.
    - Ejemplo: `ls archivo[1-3].txt` → busca `archivo1.txt`, `archivo2.txt`, `archivo3.txt`.
    - Ejemplo: `ls [abc]*.sh` → busca scripts que comiencen por `a`, `b` o `c`.

* ``$``: obtiene el valor de una variable.
    - Ejemplo: `echo $HOME` → muestra la ruta del directorio personal.

* ``?``: comodín que sustituye **un solo carácter**.
    - Ejemplo: `ls fichero?.doc` → encuentra `fichero1.doc`, `ficheroA.doc`, etc.

* ``|``: enlaza órdenes (convierte la salida de la primera en la entrada de la segunda).
    - Ejemplo: `ls -l | grep ".txt"`

* ``>``: redirecciona la salida.
    - Ejemplo: `echo "hola" > salida.txt`

* ``<``: redirecciona la entrada.
    - Ejemplo: `wc -l < archivo.txt`

* ``;``: enlaza la ejecución de dos órdenes.
    - Ejemplo: `echo hola ; echo adiós`

* ``&&``: ejecuta la segunda orden **solo si la primera tiene éxito**.
    - Ejemplo: `mkdir test && cd test`

* ``||``: ejecuta la segunda orden **solo si la primera falla**.
    - Ejemplo: `cd carpeta_inexistente || echo "Error: no existe la carpeta"`

### 9\. ÓRDENES DE IMPRESIÓN

* ``/etc/printcap``: base de datos de la configuración de las impresoras (spool).
* ``lp`` y ``lpr``: encola ficheros de texto para imprimir:
    * \-d: especifica impresora.
    * \-n: imprime un número de copias específicas.

* ``lprm``: borra los documentos pendientes de la cola de impresion
* ``lpstat``: monitoriza el estado de la cola de impresión:
    * \-p: visualiza el estado de las impresoras.
    * \-d: visualiza la impresora por defecto.
    * \-s: resumen de información de estado para todas las impresoras.

* ``cancel`` id\_peticion: cancela una petición de impresión.
* ``pr``: formatea para imprimir.

### 10\. COPIAS DE SEGURIDAD Y ALMACENAMIENTO

* ``tar``: agrupa ficheros pero sin “-z” no comprime. Archiva y extrae ficheros desde y hacia un fichero de destino u
  origen.
    * c: crea un nuevo fichero tar.
    * t: lista los contenidos de un fichero tar.
    * x: extrae los contenidos de un fichero tar / z: comprime los ficheros agrupados.
    * f: especifica el fichero de destino.
    * v: visualiza la extracción o empaquetado de ficheros.

* ``compress``: reducir el tamaño de un fichero: (el fichero resultante tiene la extensión “.Z”)
    * \-v: indica la progresión de la compresión.

* ``uncompress``: descomprimir ficheros:
    * \-c: muestra el contenido del fichero sin descomprimirlo.

* ``cpio`` (copy in/out): archiva o extrae información de una cita o de un fichero. Realiza un empaquetamiento más
  eficiente que tar, permite la recuperación de soportes defectuosos y posibilita escribir ficheros con distinto formato
  de cabecera.
    * o: crea un nuevo fichero.
    * i: extrae el fichero del archivo.
    * c: lee la información de cabecera en ASCII (muestra los ficheros comprimidos pero sin extraerlos).
    * t: lista la tabla del contenido de la cinta / v: imprime la lista de los nombres del fichero.

* ``.jar``: comprime y empaqueta en un entorno jvm (java virtual machine).

### 11\. GESTIÓN DE PROCESOS

* Cada programa que se ejecuta en un entorno UNIX es un proceso, cuando se entra en la shell y comienza a ejecutarse la
  sesión, eso es un proceso, a cada proceso se le asigna un PID, usado por el kernel.
* El sistema también comienza algunos procesos llamados demonios, son programas arrancados en tiempo de arranque y son
  críticos para la funcionalidad del sistema. Para comenzar un proceso se crea un duplicado del proceso actual al que le
  llamaremos hijo, la referencia de este proceso es PPID, dos modos de ejecución:
    * ``Foreground`` (primer plano): suspende la interactividad de la shell hasta el fin de su ejecución.
    * ``Background`` (segundo plano): se lanza añadiendo “&” al final del comando, devuelve la prompt del sistema, el
      usuario es informado mediante un mensaje de la finalización del proceso.

> ``fg``: trae a primer plano un proceso / bg: envía a background un proceso.

* ``Herramientas para gestionar procesos``:
    * ``ps``: la salida de la orden “ps” es el PID (identificador del proceso), TTY (identificador de terminal), TIME (
      tiempo de ejecución acumulado) y CMD (línea de comando):
        * \-e: muestra información sobre todos los procesos del sistema.
        * \-f: genera un listado completo que añade los campos UID (usuario propietario del proceso), PPID (padre del
          proceso) y STIME (hora de inicio del proceso).
        * \-a: lista los procesos que no pertenecen al usuario.
        * \-x: lista de procesos que no tienen asociada una terminal.
        * \-u: lista extendida.

    * ``pidof``: muestra el ID de un proceso activo.

#### 11.1. SEÑALES

* Se usan para controlar los procesos en ejecución en el sistema, se envían a procesos para indicar que ha corrido un
  evento y el proceso debe reaccionar (CTRL+c por ejemplo).
* Cada señal está asociada a un único número, un nombre y una acción esperada. Su sintaxis es (kill:señal:PID\_proceso),
  donde la opcion :señal: realiza:
    * ``SIGHUP`` (1): Hangup (reinicia teniendo en cuenta cambios de configuracion al reiniciar).
    * ``SIGINT`` (2): Interrupt.
    * ``SIGKILL`` (9): Kill (finaliza de golpe un proceso, no libera las instancias ocupadas).
    * ``SIGTERM`` (15): Terminate (finaliza ordenadamente el proceso dando tiempo a cerrar los buffers accedidos).

### 12\. ADMINISTRACIÓN DE DISPOSITIVOS

* ``UNIX`` controla los dispositivos, escalando las capas de interacción desde el hardware hasta el nivel de usuario,
  Driver es un programa que gestión la interacción entre un hardware determinado interpretándolo comandos propios del
  dispositivo a la interface propia del núcleo, pueden ser tanto parte del kernel como módulos independientes (LKM,
  Loadable Kernel Modules).
* El acceso a nivel de usuario es provisto a través de archivos de dispositivo especiales que encontraremos en el
  directorio /dev. El núcleo transforma las operaciones sobre estos archivos especiales en las llamadas al código del
  controlador. Los dispositivos son tratados por UNIX como entradas en el File System.
* Los archivos de dispositivo se mapean en los correspondientes dispositivos a través del Número menor / mayor de
  dispositivo.
    * ``Número mayor``: identifica el tipo de driver al que está asociado el archivo.
    * ``Número menor``: indica el número de instancia o número d unidad que ocupa el driver en cuestión, es usado por el
      controlador para seleccionar características particulares del dispositivo. Debemos diferenciar entre dos grandes
      tipos de archivos de dispositivo:
        * ``Dispositivos de bloques``: escribe o lee bloque a bloque (grupos de bytes de tamaño múltiplo de 512 o 1024
          bytes).
        * ``Dispositivos de caracteres``: escriben carácter a carácter.
* Los drivers de dispositivos presentan una interface estándar del kernel, cada driver tiene rutinas (open, close, read,
  reset...). Dentro del núcleo, las funciones para cada controlador se mantienen en una tabla de saltos (man mkmod),
  indexadas por el número mayor de dispositivo.
* Hay dos tablas para dispositivos una en modo bloque y otra en modo carácter.
* Cuando un programa realiza una operación sobre un archivo de dispositivo, el kernel intercepta la referencia
  automáticamente, busca la función adecuada en la tabla de saltos y le transfiere el control.
* Todos los sistemas proporcionan algún sistema de agregar nuevos drivers de dispositivo al kernel, ya se modificando
  tablas y recompilando, o en forma de módulos cargables en tiempo de ejecución.

#### 12.1 ARCHIVOS DE DISPOSITIVO

* Se encuentran en el directorio /dev, en este directorio puede haber cientos de dispositivos, se crean con el comando
  “mkmod” (el SO crea y monta al conectar por primera vez), usa la sintaxis (mkmod:nombre:tipo:major:minor), tipo es “c”
  para los archivos de caracteres y “b” para los dispositivos de bloques.
* Muchos sistemas proporcionan un script llamado MAKEDEV para aplicar de forma automatizada los argumentos a “mkmod”
  para los dispositivos más comunes.
* En Linux, utilizamos la abreviatura de disco o dispositivo, seguido del etiquetado del elemento y el número de
  partición hda1 para la primera partición del primer disco duro).

### 13\. SCRIPTS DEL SHELL

* Una serie de estructuras de control del propio shell que también actúa como intérprete de un potente lenguaje de
  programación, se crean scripts para automatizar tareas o ejecutar lotes largos de órdenes. La almohadilla (\#), tiene
  doble función:
    * ``Marcar como comentario``: cualquier línea de código del script, estas serán ignoradas por el shell en el momento
      de la ejecución.
    * ``Como excepción``, la primera línea de un script suele ser: \#\!/bin/\*shell indicada\*. Mediante esta secuencia
      indicamos al intérprete de comandos que lo que vienen a continuación es un script, debe ser interpretado mediante
      la \*shell indicada\*.

#### 13.1 CRON Y CRONTAB

* ``CRON`` es un demonio que se ejecuta desde el arranque del sistema. Comprueba si existe alguna tarea para ser
  ejecutada de acuerdo a la hora configurada en el sistema.
* En función de la distribución, se inicia utilizando las carpetas /etc/rc.d/ o /etc/init.d y cada minuto comprueba los
  ficheros /etc/crontab o /var/spool/cron es busca de posibles ejecuciones.
* ``CRONTAB`` es un archivo de texto que posee una lista con todos los scripts a ejecutar, generalmente cada usuario del
  sistema posee su propio fichero Crontab. Se considera que el ubicado en la carpeta /etc pertenece al usuario “root” (
  para generar el archivo propio, cada usuario deberá hacer uso del comando crontab).
* Para editar el archivo se usa la opción “-e” con la notación: (\* \* \* \* \*:comando a ejecutar). Cada asterisco (\*)
  significa, de izquierda a derecha:
    * ``minutos``: (0-59).
    * ``horas``: (0-23).
    * ``día del mes``: (1-31).
    * ``mes``: (1-12).
    * ``día de la semana``: (0-6), siendo 0=domingo 1=lunes, 2=martes,... 6=sábado.

> Se puede usar el ``metacaracter`` “/” antes del número para indicar que la acción se haga un número determinado de veces.

#### 13.2. VARIABLES (almacenamiento temporal en un área de la memoria)

* ``Variables locales``: privadas de la shell donde se han creado.
* ``Variables de entorno``: pasadas del proceso padre al hijo, algunas heredadas por la entrada en la Shell, otras son
  creadas en los ficheros de inicialización de la Shell del usuario, en scripts de la shell o en líneas de comando.
  Variables más frecuentes establecidas por el shell:
    * ``EDITOR``: define el editor por defecto de la shell.
    * ``HOME``: directorio al que lleva el comando cd sin argumentos.
    * ``LOGNAME``: establece el nombre de entrada del usuario.
    * ``PATH``: lista de rutas en las cuales el intérprete de comandos debe buscar los programas a ejecutar.
    * ``PS1``: indicador primario del shell (“$” para usuario y “\#” para root).
    * ``PS2``: indicador secundario del shell, suele ser “\>”.
    * ``SHELL``: el nombre del shell por defecto.

* ``Variables especiales``: pasan argumentos desde la línea de comandos, cada palabra separada por un espacio que sigue
  al nombre del script es llamada argumento.  
  Cuando ejecutamos (nombre\_script:argumento1:argumento2:argumento3:...), el shell almacena el “argumento 1” en $1, el
  “argumento 2” en $2 y así sucesivamente. ``Posiciones especiales``:
    * ``$0``: el propio nombre del script.
    * ``$\#``: el número total de argumentos de script.
    * ``$@``: visualizar cada uno de los argumentos.
    * ``$?``: retoma el valor del ultimo comando ejecutado.

> Se puede usar el ``metacaracter`` “/” antes del número para indicar que la acción se haga un número determinado de veces.

#### 13.3. ORDEN TEST Y EXPR

* Se usa para realizar comparación de expresiones, evalúa la expresión y se esta es verdad devuelve como salida cero, si
  es falso, devuelve un valor distinto, permite comprar cadenas, operadores lógicos, valores numéricos...
    * ``Comparación de cadenas``:
        * \=: iguales.
        * \!=: distintos.
        * \-n: evaluar la longitud de la cadena.

    * ``Comparación de expresiones lógicas``:
        * \!: negar una expresión lógica.
        * \-a: AND.
        * \-o: OR.

    * ``Comparación y valoración de archivos``:
        * \-d: comprueba si es un directorio.
        * \-f: “” si es un archivo.
        * \-r: “” el permiso de lectura.

    * ``Comparación numérica``:
        * \-eq: iguales.
        * \-ge: mayor.
        * \-le: menor.

> ``read``: para el script y pide un dato al usuario.

* ``EXPR``: Realiza operaciones, es una utilidad de cálculo aritmético que admite las siguientes operaciones básicas (+,
  \-, /\*, /, %), solo se admiten valores enteros y deben ir entre acentos.

#### 13.4. SENTENCIAS REPETITIVAS, CONDICIONALES Y BUCLES

* ``for``: implementa un bucle, es decir, que es capaz de repetir un grupo de sentencias un número determinado de
  veces. (
  for contador in valor / do / sentencias / done).
* ``while``: ejecutara las sentencias mientras se cumpla la condición especifica en las siguientes sintaxis. (while
  expesion / do / sentencias / done).
* ``if``: evalúa una expresión para tomar una decisión según el resultado de ella.  
  (if expresión / then sentencias / else / sentencias / fi).
* ``case``: ejecuta diferentes sentencias dependiendo de un valor o rango de valores que coincida con la variable
  especificada. (case cadena in / lista de patrones 1 sentencia / ... / ;;).
* ``func``: aparte del programa que realiza un proceso concreto. (func() / { / sentencias / }).

### 14\. UNIX EN RED

* Los comandos “ifconfig” o “ip” se utilizan para la configuración de los drivers y de los interfaces de red, se ejecuta
  en los scripts de arranque del sistema para poner en marcha los interfaces de red, sin argumentos ``ifconfig`` muestra
  el estado actual de los interfaces, sus opciones son:
    * ``\-a``: muestra todas las interfaces disponibles.
    * ``interface``: muestra el nombre de la interfaz, suele ser eth0 para la primera y así sucesivamente, se puede
      también habilitar o deshabilitar dicha interface, asociar una dirección ip (adress), una máscara de red (netmask
      addr), un alias, una dirección de broadcast,...
    * ``up/down``: activa o desactiva la interfaz.
    * ``\-promisc``: activa o desactiva el modo promiscuo en esa interfaz.
    * Para ``ip``, algunas de sus opciones son:
        * ``\-h (-human)``: muestra las estadísticas de un modo más legible (equivalente a “-v”).
        * ``\-s (-stats)``: muestra más información (equivalente a “-a”).
        * ``\-f (-family)``: especifica la familia de protocolos (inet [-4], inet6 [-6], bridge [-B], mpls [-M] o
          link [-0])
          .
        * ``\-r (-resolve)``: muestra los nombres DNS en lugar de las direcciones ip.
        * ``\-br (-brief)``: muestra solo información básica en formato de tabla.

* El programa “``route``” se utiliza para definir tablas de enrutamiento, cuando nuestro host necesita acceder a
  recursos de más de una red lógica. (opciones: add, del, target, netmask, gw,...).

* > ``IP Masquerade``:
    * > Es una capacidad de red de Linux en desarrollo.
    * > Si un servidor Linux está conectado a Internet con IP Masquerade habilitado, los ordenadores conectados a él (bien en la misma red local, bien por módem) también pueden conectarse a Internet, incluso aunque no tengan una dirección IP oficial asignada.

* Resolución de nombres en UNIX, serie de ficheros encargados de definir y acceder a los nombres: /etc/hosts.conf y
  /etc/resolve.conf. \[Nombres de las interfaces de red: /dev/eth0 (en Linux)\]

#### 14.1. CONFIGURACIÓN DE LOS SERVICIOS DE RED

* Servicios basados en red, en sistemas UNIX, se habilitan mediante demonios que corren en los servidores, un demonio no
  es más que un programa que se activa en tiempo de arranque del sistema y permanece a la escucha de recibir una
  solicitud para ofrecer un servicio, dos modos:
    * ``standalone``: un proceso escuchando un único puerto, para responder a las solicitudes.
    * ``inetd`` (metademonio de red): escucha distintos puertos y reclama el servicio apropiado.
    * Ficheros implicados en este tipo de servicios:
        * ``/etc/services``: se reserva un puerto para cada servicio, hay una serie de puertos reservados y los no
          reservados por encima del 1024 son determinados arbitrariamente.
        * ``/etc/inetd.conf``: se configuran las llamadas de inetd.

#### 14.2 X WINDOW SYSTEM

* Protocolo que permite la interacción grafica en red entre un usuario y una o más computadoras haciendo transparente la
  red para este de forma totalmente independiente del SO.
* Distribuye el procesamiento de aplicaciones especificando enlaces cliente-servidor\*.
* El servidor provee servicios para acceder a la pantalla, teclado y ratón, mientras que los clientes son las
  aplicaciones que utilizan estos recursos para interacción con el usuario.
* Debido a este esquema cliente-servidor, se puede decir que X se comporta como un terminal gráfico virtual.

#### 14.3. SMB vs SAMBA

* ``Server Message Block`` (SMB): es un protocolo que permite compartir recursos en una red. Fue modificado y
  renombrado, por Microsoft, como CIFS (Common Internet File system).
* ``Samba``: es una implementación libre del protocolo SMB/CIFS que se usa en sistemas GNU/Linux y Unix en general.

### 15\. IPTABLES

* Programa de utilidad de espacio de usuario que permite a un administrador de sistemas configurar las tablas
  proporcionadas por el cortafuegos del núcleo Linux (implementado como diferentes módulos Netfilter) y las cadenas y
  reglas que almacena.
* Se utilizan diferentes módulos del kernel y programas para protocolos diferentes:
    * ``iptables`` se aplica a IPv4
    * ``ip6tables`` a IPv6
    * ``arptables`` a ARP
    * ``ebtables`` a marcos de Ethernet.
* Las reglas se guardan en el fichero “iptables.sh”:
    * ``Cadenas`` (por donde van a circular los paquetes dentro del sistema):
        * ``PREROUTING``: contiene los paquetes que acaban de entrar al sistema, independientemente de que estén
          generados por el mismo equipo o un equipo remoto.
        * ``INPUT``: contiene los paquetes destinados al equipo local con cualquier origen.
        * ``OUTPUT``: contiene los paquetes generados en el equipo local y que van a salir del mismo.
        * ``FORWARD``: contiene los paquetes que pasan por el equipo pero que son generados en equipos remotos y se
          dirigen a otros equipos diferentes.
        * ``POSTROUTING``: contiene los paquetes que van a abandonar el sistema, independientemente de estén generados
          en el mismo equipo o en un equipo remoto.

    * ``Acciones`` (especifican qué se va a realizar con el paquete cuando satisface la regla en la que se encuentra):
        * ``ACCEPT``: el paquete se acepta y no continúa atravesando ni la cadena actual ni cualquier otra cadena de la
          misma tabla.
        * ``DROP``: el paquete se elimina completamente dentro de la cadena actual, y no será procesado en ninguna de
          las cadenas principales de ninguna tabla. Tampoco se enviará ninguna información en ninguna dirección para
          informar de ello.
        * ``REJECT``: el paquete se elimina completamente dentro de la cadena actual, aunque en este caso sí que se
          devuelve información al equipo que envió el paquete. Sólo es válido en las cadenas INPUT, OUTPUT y FORWARD.
        * ``RETURN``: el paquete dejará la cadena en la que se encuentre, pero continuará por la cadena superior a esa,
          si es que existe.
        * ``REDIRECT``: redirige el paquete hacia el mismo equipo local donde se ejecuta Iptables. Necesita un parámetro
          opcional para indicar hacia dónde se redirige (--to-ports puertos).

    * ``Operaciones``:
        * \-L (--list): lista todas las reglas de la cadena.
        * \-A (–append): añade la regla al final de la cadena.
        * \-I (–insert): inserta la regla en la posición que indiquemos de la cadena.
        * \-D (–delete): elimina la regla de la cadena.
        * \-R (--replace): sustituye la regla en la cadena por la nueva.
        * \-F (–flush): elimina todas las reglas de la cadena.
        * \-P (--policy): crea una política por defecto en la cadena.

    * ``Coincidencias`` (patrones de los paquetes, podremos aplicarles acciones):
        * \-j accion: realiza la acción (ACCEPT, DROP, QUEUE y RETURN) cuando un paquete coincide con una regla
          particular.
        * \-p protocolo (--protocol): indica el protocolo de conexión que debe poseer el paquete.
        * \-s ip/máscara (--source): indica la dirección o red de origen del paquete.
        * \-d ip/máscara (--destination): indica la dirección o red de destino del paquete.
        * \-i interfaz (--in-interface): indica la interfaz de red del sistema por la que se recibe el paquete (sólo
          permitido en las cadenas PREROUTING, INPUT y FORWARD).
        * \-o interfaz (--out-interface): indica la interfaz de red del sistema por la que se envía el paquete (sólo
          permitido en las cadenas OUTPUT, FORWARD y POSTROUTING).
        * \--sport puerto (--source-port): indica el puerto de origen del paquete (sólo para los protocolos TCP y UDP).
        * \--dport puerto (--destination-port): indica el puerto de destino del paquete (sólo para los protocolos TCP y
          UDP).

* La ``Arquitectura cliente servidor`` es un modelo de diseño de software en el que las tareas se reparten entre los
  proveedores de recursos o servicios, llamados servidores, y los demandantes, llamados clientes.
* Un cliente realiza peticiones a otro programa, el servidor, quien le da respuesta.
* Esta idea también se puede aplicar a programas que se ejecutan sobre una sola computadora, aunque es más ventajosa en
  un sistema operativo multiusuario distribuido a través de una red de computadoras.
* En la arquitectura C/S sus características generales son:
    * El Cliente y el Servidor pueden actuar como una sola entidad y también pueden actuar como entidades separadas,
      realizando actividades o tareas independientes.
    * Las funciones de Cliente y Servidor pueden estar en plataformas separadas, o en la misma plataforma.
    * Cada plataforma puede ser escalable independientemente. Los cambios realizados en las plataformas de los Clientes
      o de los Servidores, ya sean por actualización o por reemplazo tecnológico, se realizan de una manera transparente
      para el usuario final.
    * La interrelación entre el hardware y el software están basados en una infraestructura poderosa, de tal forma que
      el acceso a los recursos de la red no muestra la complejidad de los diferentes tipos de formatos de datos y de los
      protocolos.
    * Su representación típica es un centro de trabajo (PC), en donde el usuario dispone de sus propias aplicaciones de
      oficina y sus propias bases de datos, sin dependencia directa del sistema central de información de la
      organización.

* Los servidores pueden ser apátridas o stateful.
* Un servidor apátrida no guarda ninguna información entre las peticiones.
* Un servidor stateful puede recordar la información entre las peticiones.
* El alcance de esta información puede ser global o sesión-específico.
* Un servidor del HTTP para las páginas estáticas del HTML es un ejemplo de un servidor, apátrida mientras
  que ``Apache Tomcat`` es un ejemplo de un servidor stateful.
* La interacción entre el cliente y el servidor se describe a menudo usando diagramas de secuencia.
* Los diagramas de secuencia se estandarizan en el UML.
* Es importante que los clientes no interactúen entre sí ni que lo hagan clientes de capas bajas hacia otros de capas
  más altas, por eso todo tiene que pasar por el servidor.
* Para la arquitectura C/S el remitente de una solicitud es conocido como cliente (front-end). Sus características son:
    * Es quien inicia solicitudes o peticiones, tienen por tanto un papel activo en la comunicación (dispositivo maestro
      o amo).
    * Espera y recibe las respuestas del servidor.
    * Por lo general, puede conectarse a varios servidores a la vez.
    * Normalmente interactúa directamente con los usuarios finales mediante una interfaz gráfica de usuario.

* Al receptor de la solicitud enviada por el cliente se conoce como servidor (back-end).
* Sus características son:
    * Al iniciarse esperan a que lleguen las solicitudes de los clientes, desempeñan entonces un papel pasivo en la
      comunicación (dispositivo esclavo).
    * Tras la recepción de una solicitud, la procesan y luego envían la respuesta al cliente.

* Por lo general, acepta las conexiones de un gran número de clientes (en ciertos casos el número máximo de peticiones
  puede estar limitado).

## WINDOWS

* Microsoft produce dos líneas separadas de sistemas operativos, una para ordenadores personales y otra para servidores.
* Versiones más importantes:
    * ``Windows NT``: primera versión, orientada a computadoras personales, necesitaba gran cantidad de recursos
    * ``Windows 95 y 98``: Versiones basadas en MS-DOS.
    * ``Windows 2000``: muy útil para los administradores de sistemas y con una gran cantidad de servicios de red,
      implementaba la posibilidad del “plug and play”, alguna de las características más destacables:
        * Soporte para FAT32 y NTFS.
        * Cifrado de ficheros (EFS).
        * Sistema RAID.
        * Servicios de acceso remoto (RAS, VPN, RADIUS...).
        * Active Directory.
        * Windows XP: nueva interfaz, mayores capacidades multimedia, multitarea mejorada, soporte para redes
          inalámbricas...

    * ``Windows Server``: basada en el núcleo de XP con servicios añadidos.
    * ``Windows 7``: mayor compatibilidad con aplicaciones y hardware, mejor interfaz, sistema de redes domesticas
      simplificado y fácil de usar denominado “Grupo en el hogar”, mejoras de rendimiento...
    * ``Windows 10``: introdujo una arquitectura de aplicaciones universales, desarrolladas con la interfaz “modern UI”,
      orientado al uso con ratón y al uso con pantalla táctil, introduce la vista de tareas, un sistema de escritorio
      virtual y el asistente Cortana.

### 1\. WINDOWS XP (Windows XP Home, Windows XP Profesional)

* Construido con el código de Windows 2000 con un nuevo interfaz gráfico, introduce mejoras importantes como “entorno
  mejorado orientado a tareas”, “asistentes y herramientas”, “restaurar el sistema”, “nuevas tecnologías (conexión de
  varios monitores, DVD, dispositivos inalámbricos, bus USB...)”, “mejoras multimedia (controladores de tarjetas de
  video y sonido)”...
    * ``Instalación``: el proceso de instalación está dirigido por un asistente que se ocupa de todo, solicitado en cada
      paso la información que necesita.
        * ``RIS`` (Remote Installation Services): servicio de los servidores de Microsoft que permite a ordenadores con
          BIOS PXE ejecutar parámetros de arranque de forma remota.

    * ``Administración de discos``: admite trabajar con “discos básicos” que se dividen en particiones y “discos
      dinámicos” que se dividen en volúmenes, facilita dos herramientas, el administrador de discos y la línea de
      comandos “diskpart”.

        * Los ``discos básicos`` pueden dividirse en porciones de almacenamiento más pequeñas denominadas particiones,
          dos tipos de particiones en un disco básico: primaria y extendida y esta a su vez se puede dividir en
          particiones lógicas.
        * Los ``discos dinámicos`` dan la posibilidad de administrarlo sin la necesidad de reiniciar, ampliar un volumen
          de disco, extender un volumen entre múltiples discos duros, realizar secciones de un volumen para mejorar su
          rendimiento, hacer un espejo o añadirlo a un array RAID 5, todo desde MMC y sin tener que reiniciar, la
          creación inicial o conversión de un disco básico a disco dinámico si necesitara reinicio.
        * ``Se organizan en``:
            * ``Volúmenes simples``: contienen el espacio en un único disco.
        * ``Volúmenes seccionados`` (striped): combina espacio libre de dos o más discos físicos en un único volumen,
          este proceso de división de los datos entre varios discos mejora el rendimiento del disco.
        * ``Volúmenes distribuidos`` (spanned): usa dos o más discos físicos de forma que se rellena el primer disco y
          después el segundo y así sucesivamente.

> ``Windows`` proporciona dos métodos para la desfragmentación del disco y mejorar el rendimiento: la herramienta gráfica “desfragmentador de disco” y la línea de comandos “defrag”.

#### 1.1. SISTEMA DE ARCHIVOS

* Es la estructura en la que se asigna nombres a los archivos, se almacena y se tiene acceso a ellos, tres tipos de
  archivos en los discos duros FAT, FAT32 y NTFS, donde el utilizado actualmente es NTFS (New Technology File System)
  sistema de archivos implementado en Windows NT, aunque son posibles tamaños mayores, el máximo recomendado en la
  práctica para cada volumen es de 2 TB (Terabytes).
* El tamaño máximo de fichero viene limitado por el tamaño del volumen.
* A partir de la versión 3.0, soporta cuotas de disco, cifrado de archivos, archivos dispersos, puntos de análisis,
  número de secuencia de actualización (USN) diario, la carpeta $ Extender y sus archivos.
* Se reorganizó los descriptores de seguridad de forma que varios archivos utilizando la misma configuración de
  seguridad pueden compartir el mismo descriptor.
* La versión 3.1 amplió la tabla maestra de archivos (MFT) entradas con número de registro MFT redundante (
  útil para la recuperación de archivos dañados MFT).

> ``chkdsk`` (windows): comprueba la integridad del disco.

##### 1.1.1. PERMISOS NTFS

* Los permisos sobre carpetas y archivos en NTFS son:
    * ``escribir`` (crear archivos y carpetas y modificar los atributos),
    * ``leer`` (leer los archivos y carpetas, también los atributos),
    * ``mostrar`` el contenido de la carpeta (permite movernos por la carpeta),
    * ``lectura y ejecución`` (lectura y listado), modificar (lectura y ejecución más suprimir la carpeta) y control
      total (permite cambiar los permisos y tomar posesión).
* En un volumen NTFS se pueden establecer permisos a nivel de archivo, cualquier archivo puede otorgar a los usuarios
  diferentes tipos de acceso.
* Se deben asignar permisos a grupos, no a usuarios individualmente.
* No hay que establecer permisos archivo a archivo a menos que sea inevitable.
* Estos permisos siguen unas reglas:
    * El usuario que crea un archivo o carpeta es el propietario de ese objeto.
    * Los permisos que le demos a una carpeta se heredan en los niveles inferiores (Herencia).
    * Los permisos son acumulativos cuando un usuario está en más de un grupo salvo que alguno tenga marcado “DENEGAR” (
      Aditivos).
* Si copiamos un archivo a una partición distinta se heredan los permisos de la partición destino, si movemos un archivo
  o una carpeta NTFS hacia otra partición esta pierde sus propiedades de seguridad, se eliminan los permisos y se
  heredan de la carpeta destino.
* Para determinar los permisos reales de acceso a un recurso, el permiso global efectivo será el más restrictivo entre
  el permiso efectivo de compartición (FAT) y el permiso efectivo de NTFS.

#### 1.2. CARPETAS Y RECURSOS COMPARTIDOS

* El sistema crea varios recursos compartidos especiales como ADMIN$ (aparece como C$, D$, E$...), permiten a los
  administradores conectarse a unidades que en otro caso no estarían compartidas. Existen como parte de la instalación
  del SO:
    * ``ADMIN$``: se utiliza durante la administración remota de un equipo, solo los administradores, operadores de
      copia y operadores de servidores se pueden conectar a este recurso compartido.
    * ``C$``: carpeta raíz de la unidad específica.
    * ``IPC$``: utilizado durante la administración remota y cuando se revisan los recursos compartidos, es esencial en
      la comunicación y no se debe cambiar, modificar o eliminar.
    * ``NETLOGON``: servicio Inicio de sesión de red de un servidor que ejecuta Windows NT Server cuando procesa los
      únicos de sesión en el dominio.
    * ``PRINT$``: soporta impresoras compartidas.
    * ``REPL$``: se crea en un servidor cuando un cliente de fax está enviando el fax.

* El objeto principal en una red es compartir archivos entre los distintos equipos, en sistemas Microsoft vamos a
  compartir siempre carpetas nunca archivos.
* La forma más sencilla de crear carpetas compartidas es utilizar la consola MMC con el complemento de carpetas
  compartidas, le asigna un nombre identificativo y se asignan los permisos correspondientes.
* Se pueden definir recursos compartidos y una única carpeta puede ser compartida más de una vez, un recurso compartido
  podría incluir control total para administradores y otro recurso compartido para  
  usuarios podría ser más restrictivo.
* Los permisos de recursos compartidos se pueden asignar a usuarios individuales, a grupos y a las entidades especiales
  “Todos”, SYSTEM, INTERACTIVE, NETWORK y Usuarios autentificados. ``Carpetas que comparte`` el sistema ``por defecto``:
    * ``C$``
    * ``IPC$``: comunicación entre procesos.
    * ``ADMIN$``: ruta %systemroot%.
    * ``Print$``: administración de impresoras.

#### 1.3. CONFIGURACIÓN DE RED EN WINDOWS XP

* Dos métodos para asignar direcciones IP a un dispositivo de red TCP/IP:
    * ``Direccionamiento estático``: se especifica físicamente la dirección IP.
    * ``Direccionamiento dinámico``: protocolo DHCP, configurado de forma predeterminada para obtener una dirección IP
      automáticamente de un servidor DHCP. Utilidades que permiten diagnosticar problemas de red:
        * ``arp``: muestra y permite modificar las tablas de protocolo arp, convertir direcciones IP de cada ordenador
          en direcciones MAC.
        * ``ftp``: conectarse a otra maquina a través del protocolo FTP para transferir archivos.
        * ``ipconfig``: configuración de todos las interfaces.
        * ``/flushdns``: purga la cache de resolución de DNS.
        * ``net``: administrar usuarios, carpetas compartidas, servicios...
        * ``netstat``: listado de todas las conexiones de red que nuestra maquina está realizando.
        * ``nslookup``: obtener la dirección IP conociendo el nombre, y viceversa; permite que el usuario consulte de
          forma manual los servidores de nombres para resolver un nombre de host dado.
        * ``ping``: paquetes IP, comprobar la conexión, informa del tiempo que tarda en contestar la máquina destino.
        * ``pathping``: la ruta que sigue cada paquete para llegar a una IP determinada, tiempo de respuesta de cada uno
          de los nodos por los que pasa y las estadísticas de cada uno de ellos.
        * ``route``: ver o modificar las tablas de enrutamiento de red.

* Un equipo puede estar configurado en modo:
    * ``Grupo de trabajo``: cada máquina se administra de forma independiente, es una agrupación de equipos en una red
      que comparte recursos, todos los equipos pueden compartir recursos como elementos iguales sin servidor dedicado.
    * ``Dominio``: todas las maquinas son controladas por un equipo llamado controlador de dominio.

#### 1.4. USUARIOS Y GRUPOS

* El fichero “NTUSER.DAT” se encarga de guardar las configuraciones y preferencias de cada usuario de Windows.
* Cada usuario tendrá su propio fichero dentro de su carpeta personal, y cuando inicia sesión se carga este fichero en
  el registro para dar forma al perfil de usuario.
    * ``Administradores``: pueden acceder a todos los componentes, configuración, instalar programas, crear nuevos
      usuarios...
    * ``Usuarios``: usar el equipo y almacenar sus archivos en las carpetas del equipo.
    * ``Usuario Avanzado``: similar a usuario con más derechos administrativos.
    * ``Cuentas de usuario en red``:
        * Registradas en el equipo servidor, pueden iniciar sesión en cualquier equipo de la red, las cuentas de usuario
          local son el único tipo de cuenta en un grupo de trabajo que se crea en el equipo que se va a utilizar, pero
          reside en una base de datos de cuentas denominada administrador de seguridad SAM.
        * Los usuarios y contraseñas se almacenan en system32/config y cada usuario tiene un SID (security identifier)
          único.
        * La configuración específica de un usuario queda guardada en su perfil, en la carpeta %HOMEPATH% (
          Documents and settings/User), los perfiles existentes son:
            * ``Usuario permanente``: base de todos los perfiles de usuario.
            * ``Usuario local``: perfiles creados en un equipo cuando un usuario inicia sesión, el perfil es especifico
              a un usuario y local al equipo. Se crean en los equipos cuando los usuarios individuales inician sesión y
              la primera vez que un usuario inicia sesión en un equipo, se genera una carpeta de perfil para el usuario
              y los contenidos de la carpeta Default User se copian a ella. Si un usuario tiene una cuenta local en el
              equipo además de una cuenta de dominio, tendrá dos carpetas de perfil en el equipo local, una para cuando
              inicie sesión localmente y otra para cuando inicie sesión en el dominio.
            * ``Usuario móvil``: perfiles creados por un administrador y almacenados en un servidor, después del inicio
              de sesión del usuario sea autentificado en el servicio de directorio se copia al equipo local. Se crea una
              carpeta compartida con los usuarios que tengan perfiles móviles. Se introduce una ruta de acceso a esa
              carpeta en la ventana propiedades del perfil de los usuarios, cuando el usuario cierra la sesión, el
              perfil se almacena tanto localmente como en la ubicación de la ruta de acceso al perfil del usuario.
            * ``Usuario obligatorio``: lo crea el administrador del sistema con determinada configuración para uno o
              varios usuarios, puede convertir perfiles móviles en obligatorio si se cambia el nombre del archivo de
              perfil de Ntuser.dat en Ntuser.man

##### 1.4.2. ACCESO REMOTO

* ``Remote Desktop Protocol`` (RDP): es un protocolo que permite la comunicación en la ejecución de una aplicación entre
  una terminal (mostrando la información procesada que recibe del servidor) y un servidor Windows (recibiendo la
  información dada por el usuario en el terminal mediante el ratón o el teclado), bajo el puerto TCP 3389\.
* La información gráfica que genera el servidor es convertida a un formato propio RDP y enviada a través de la red al
  terminal, que interpretará la información contenida en el paquete del protocolo para reconstruir la imagen a mostrar
  en la pantalla del terminal.
* Para acceder al cliente del protocolo se ejecuta mstsc (Microsoft Remote Desktop Connection), en ese momento se tiene
  acceso a todas las aplicaciones, archivos y recursos, mientras se utiliza el equipo de forma remota, nadie podrá
  usarlo de forma local, provocaría el cierre de la sesión remota.

#### 1.5. SERVICIOS

* Son aplicaciones que se ejecutan en segundo plano y que el sistema ejecuta de forma predeterminada al iniciar o cuando
  es necesario (como los demonios de UNIX).
    * ``Estado``: modo de funcionamiento actual del servicio (Detenido, pausado, iniciado).
    * ``Tipo de inicio``:
        * ``Manual``: mediante intervención del usuario.
        * ``Automático``: cada vez que arranca el SO, arranca el servicio.
        * ``Deshabilitar``: no se puede iniciar.

* Se puede parar o arrancar servicios desde la línea de comandos con el comando “net”:
    * net ``start``: inicializa un servicio / net stop: detiene un servicio que se encuentra en ejecución.
    * net ``continue``: inicia de nuevo un servicio interrumpido.
    * net ``user``: para la gestión de usuarios
    * net ``name``: agrega o elimina un alias.
    * net ``session``: muestra y gestiona una lista con las sesiones conectadas a un equipo local.
    * net ``accounts``: actualiza la base de datos y modifica las directivas de seguridad.
    * net ``computer``: agrega o quita equipos en una base de datos de dominios.
    * net ``group``: agrega o elimina grupos globales
    * net ``localgroup``: agrega elimina grupos locales.
    * net ``share``: comparte carpetas o impresoras (recurso compartido) para ser utilizadas en red.
    * net ``config``: muestra o modifica los servicios configurables que están en ejecución.
    * net ``file``: muestra los nombres de todos los archivos compartidos abiertos en un servidor.
    * net ``help``: muestra la ayuda de un comando
    * net ``helpmsg``: muestra la ayuda de un error.
    * net ``print``: muestra la cola de impresión
    * net ``statistics``: muestra estadísticas del servicio local.
    * net ``view``: muestra un listado de los recursos compartidos de un equipo.

### 1.6. IMPRESORAS

* ``Servidor de impresión``: ordenador al que se mandan los documentos para imprimir.
* ``Impresora``: interfaz entre aplicación e impresión.
* ``Dispositivo de impresión``.
* ``Cola de impresión``: lista de documentos que se están imprimiendo.
* ``Spool de impresión``: software que se encarga de administrar la cola de impresión.
* ``Pool de impresoras``: dirigir desde una única impresora los documentos hacia varios dispositivos de impresión.
* Puertos:
    * ``Impresoras locales``: USB, COM, LPR (compatible con UNIX).
    * ``Impresoras de red``: para compartir una impresora local, se comparten los drivers de dicha impresora con TCP/IP,
      quedan incluidos en la carpeta PRINT$ con la ruta %systemroot%/system32/spool/drivers.

### 2\. WINDOWS 7 (Windows Home / Windows 7 Professional / Windows 7 Ultimate)

* ``Windows 7`` crea una partición automática utilizando la totalidad del disco duro, automáticamente crea una partición
  de 200MB, se denomina partición de sistema y contienen los archivos para que Windows 7 arranque correctamente, la otra
  partición se denomina arranque y contiene el resto de archivos del sistema operativo. Modos de instalación:
    * ``Instalación manual``:
        * ``Actualizaciones``: conserva los archivos, la configuración y los programas en su ubicación en el equipo. Es
          posible realizar un proceso de migración de los perfiles de usuario:
        * ``Windows Easy Transfer`` (WET): migración de un único ordenador.
        * ``Personalizada``: no conserva los archivos, la configuración ni los programas, se la denomina instalación
          limpia.

    * ``Mediante imagen estándar`` (clonación de equipo), pasos:
        * Analizar la compatibilidad de las aplicaciones: con ACT (Kit de herramientas de compatibilidad de
          aplicaciones).
        * Prepara un dispositivo de arranque para capturar imágenes: AIK de Windows, prepara una imagen del entorno de
          preinstalación de Windows (Windows PE).
        * Instalar Windows 7 en el equipo de referencia las aplicaciones, controladores y actualizaciones que queramos
          incluir en la imagen.
        * Prepara la imagen en el equipo de referencia con sysprep.
        * Capturar la imagen del equipo de referencia: se inicia el equipo de referencia con Windows PE y se captura una
          imagen con ImageX, se puede almacenar la imagen en un recurso compartido de red o disco duro USB local.
        * Se crea un archivo de respuestas Unattend.xml que apunte a la imagen anterior.
        * Instalar la imagen en el quipo cliente con el archivo de respuesta.

    * ``Implementación con MDT`` (Microsoft Deployment Toolkit):
        * Instalación: debe crearse un servidor de archivos (Windows Server).
        * Se instala el MDT 2010, en ese servidor de archivos junto con el resto de componentes.
        * Se crea un recurso compartido de distribución que debe contener el sistema operativo, las aplicaciones, los
          drivers y la configuración del Windows.
        * En MDT 2010 indican las instrucciones para la instalación y configuraron de Windows, se crea también en el MDT
          punto de implementación, establecer una conexión a archivos en el resto de recurso compartido de distribución
        * Podemos almacenar las imágenes que ha creado el MDT en dispositivo de almacenamiento extraíble.

    * ``User State Migration Tool`` (USMT): automatización de la migración.
    * ``Herramientas externas`` como “Clonezilla”.

#### 2.1. PROCESO DE ARRANQUE

* 1\. La BIOS accede al MBR indicando cual es la partición activa.
* 2\. Se accede al sector de arranque de dicha partición (creando al instalar el SO).
* 3\. Este sector de arranque direcciona al fichero BOOTMGR (en Windows NT, XP y Server 2003 se usa NTLDR “NT Loader”).
* 4\. BOOTMGR accede al fichero BOOTBCD, es un archivo binario, no editable mediante procesador de textos, se encuentra
  en la partición de 200MB.
* 5\. Inicio del sistema ejecutamos el kernel y ubicado en el fichero NTOSKRNL.exe

#### 2.2. NOVEDADES

* Se añaden a los tipos de usuarios ya vistos en Windows XP:
    * ``Operadores de copia de seguridad``: pueden hacer copias de seguridad y restaurar archivos de un equipo.
    * ``Replicador``: cuenta de usuario de dominio que se usa para iniciar sesión en servicios de replicador de un
      controlador de domino.
    * ``Compartición de carpetas``: permite compartir archivos de las carpetas públicas con otras personas con el mismo
      equipo y con personas que usen otros equipos en la misma red.
    * ``Servicios``: se añade un nuevo modo de inicio, Automático (inicio retrasado), retrasa el inicio del servicio
      hasta después de completarse el proceso de arranque de Windows.
    * ``Impresoras``: se añaden el formato XPS (XML Paper Specification) y Location-Aware Printing, la impresora por
      defecto se modifica automáticamente cuando se detecta el cambio de conexión a una nueva red.
    * Además de trabajar con los tipos de discos ya vistos en Windows XP, también soporta el trabajo
      con ``dos nuevos tipos de discos``:
        * ``MBR`` (Master Boot Record): discos tradicionales, en los que se crea una tabla de particiones con un máximo
          de cuatro, en el primer sector del disco duro.
        * ``GPT`` (GUID Partition Table): contiene un array de entradas de particiones que indican la dirección del
          bloque inicial y final de cada partición en el disco.

#### 2.6. MEJORAS DE SEGURIDAD EN WINDOWS 7

* ``User Access Control``: permite controlar los privilegios de los usuarios que hacen uso del sistema cuando se
  ejecutan tareas administrativas que acceden o modifican archivos críticos del sistema, se activara cuando identifique
  la necesidad de tareas administrativas por parte de procesos o actualizaciones.
* ``Supresión de Autoplay``: solo los dispositivos ópticos (CD, DVD...) utilizaran la opción de ejecutar automáticamente
  archivos al ser insertados (USB deja de utilizarla, pregunta primero).
* ``Windows Biometric Framework`` (WBF): utilización de dispositivos biométricos de lectura de huellas dactilares.

### 3\. WINDOWS 10 (Windows 10 Home / Windows 10 Pro / Windows 10 Enterprise-Education)

* Introduce una arquitectura de aplicaciones universales (Modern UI), diseñadas para ejecutarse en todas las familias de
  productos Microsoft.
* Se introduce la vista de tareas, sistema de escritorio virtual, soporte para huella digital o reconocimiento facial,
  DirectX 12, WDDM 2.0.
* La edición Pro añade características adicionales de seguridad y red como BitLocker, Device Guard, Windows Update para
  empresas y la habilidad de unirse a un dominio.

#### 3.1. SISTEMA Y SEGURIDAD

* Incorpora ``FIDO`` (Fast Identity Online) una tecnología de autenticación en factores múltiples, incluye soporte
  mejorado para la ``autenticación biométrica`` (Windows Hello), las credenciales se almacenan localmente y están
  protegidas mediante cifrado asimétrico.
* La plataforma “Passport” permitirá a las redes, software y sitios web verificar la identidad del usuario mediante un
  PIN o un inicio de sesión biométrico, los administradores establecen normativas para el cifrado de datos automático y
  bloquear selectivamente las solicitudes de acceso a datos cifrados.
* ``Device Guard``, permite a los administradores reforzar la seguridad de un espacio digital, mediante el bloqueo de la
  ejecución de software que no está firmado digitalmente por un proveedor de confianza o Microsoft, también incluye
  Sensor de almacenamiento, permite al usuario ver de qué forma la capacidad de almacenamiento de su dispositivo está
  siendo utilizado por diferentes tipos de archivos.

* > ``SCCM`` (Microsoft System Center Configuration Manager):
    * > Solución de software de administración que permite gestionar de forma centralizada la configuración de todos los sistemas físicos y virtuales de una organización o grupo de organizaciones permitiendo, entre otras características, control remoto, gestión de actualizaciones y parches, distribución de software, despliegue de sistemas operativos, protección, cumplimiento e inventariado de software y de hardware.
    * > Desde la versión 1910, se llama ECM (Microsoft Endpoint Configuration Manager).

### 4\. WINDOWS SERVER 2008

* ``Active Directory`` es el nombre utilizado por Microsoft (desde Windows 2000\) como almacén centralizado de
  información de uno de sus dominios de administración.
* Un Servicio de Directorio es un depósito estructurado de la información de los diversos objetos que contiene el Active
  Directory, en este caso podrían ser impresoras, usuarios, equipos...
* Bajo este nombre se encuentra realmente un esquema (definición de los campos que pueden ser consultados) LDAP versión
  3, lo cual permite integrar otros sistemas que soporten el protocolo.
* En este LDAP se almacena información de usuarios, recursos de la red, políticas de seguridad, configuración,
  asignación de permisos, etc.

* > ``LDAP`` (Lightweight Directory Access Protocol):
    * > Protocolo a nivel de aplicación que permite el acceso a un servicio de directorio ordenado y distribuido para buscar diversa información en un entorno de red.
    * > Los despliegues actuales de LDAP tienden a usar DNS para estructurar los niveles más altos de la jerarquía.
    * > Conforme se desciende en el directorio pueden aparecer entradas que representan personas, unidades organizacionales, impresoras, documentos, grupos de personas o cualquier cosa que representa una entrada dada en el árbol (o múltiples entradas).
    * > Habitualmente, almacena la información de autenticación (usuario y contraseña) y es utilizado para autenticarse aunque es posible almacenar otra información (datos de contacto del usuario, ubicación de diversos recursos de la red, permisos, certificados, etc).
    * > A manera de síntesis, LDAP es un protocolo de acceso unificado a un conjunto de información sobre una red.

* Combina el SO del equipo y de red en un mismo sistema, configura un equipo para proporcionar funciones y recursos de
  servidor a una red y las funciones de cliente de red. Trabaja sobre una modelo de dominio, es una colección de equipos
  y usuarios que comparten unas políticas de seguridad y una base de datos común (catalogo global).

* Se debe designar un servidor como controlador principal de domino (PDC, Primary Domain Controller).
* Este servidor mantiene los servicios de directorios y autentifica cualquier usuario que quiera entrar en el sistema.
* Los servicios de directorios de Windows Server se pueden implementar de varias formas, existen cuatro modelos de
  domino:
    * ``Dominio único``: un único servidor mantiene la base de datos de seguridad y de las cuentas.
    * ``Maestro único``: una red con maestro único puede tener diferentes dominios, pero se designa uno como el maestro
      y mantiene la base de datos de las cuentas de usuario. Incluye varios roles y la capacidad de transferir roles a
      cualquier controlador de dominio de la empresa. Dado que un rol de Active Directory no está enlazado a un solo
      controlador de dominio, se conoce como un rol ``FSMO`` (Flexible Single Master Operations).
    * Actualmente en Windows hay ``cinco roles`` FSMO:
        * ``Maestro de esquema``: se encarga de procesar actualizaciones del esquema de directorio. Una vez completada
          la actualización de esquema, se replica desde el patrón de esquema a todos los demás DCs del directorio.
        * ``Patrón de nomenclatura de dominio``: se encarga de agregar o quitar un dominio del directorio. También puede
          agregar o quitar referencias cruzadas a dominios en directorios externos.
        * ``Patrón de RID``: responsable de quitar un objeto de su dominio y colocarlo en otro dominio durante un
          movimiento de objeto. Cuando un controlador de dominio crea un objeto de entidad de seguridad, como un usuario
          o grupo, adjunta un identificador de seguridad (SID, security identifier) único al objeto. Consta de un SID de
          dominio que es el mismo para todos los SID creados en un dominio y de un RID (relative identifier) que es
          único para cada SID de entidad de seguridad creado en un dominio.
        * ``Emulador PDC``: el emulador PDC es necesario para sincronizar el tiempo en una empresa. Windows incluye el
          servicio de tiempo W32Time, que requiere el protocolo de autenticación Kerberos\*. Se encarga de los cambios
          de contraseña realizados por otros controladores de dominio en el mismo, se replican de forma preferente en el
          emulador de PDC, cuando se producen errores de autenticación en un controlador de dominio determinado debido a
          una contraseña incorrecta, los errores se reenvían al emulador de PDC antes de que se informe al usuario de un
          mensaje de error de contraseña incorrecto, el bloqueo de cuentas se procesa en el emulador PDC y este realiza
          todas las funciones.

* > ``Kerberos``:
    * > Protocolo de autenticación de redes de ordenador, permite a dos ordenadores en una red insegura demostrar su identidad mutuamente de manera segura mediante autenticación mutua:
        * > tanto cliente como servidor verifican la identidad uno del otro.
    * > Kerberos se basa en criptografía de clave simétrica y requiere un tercero de confianza.
    * > Además, existen extensiones del protocolo para poder utilizar criptografía de clave asimétrica.

    * ``Maestro de infraestructura``: cuando otro objeto de otro dominio hace referencia a un objeto de un dominio,
      representa la referencia mediante el GUID, el SID y el DN del objeto al que se hace referencia. El titular de la
      función FSMO de infraestructura es el controlador de dominio responsable de actualizar el SID y el nombre
      distintivo de un objeto en una referencia de objeto entre dominios.

    * ``Maestro múltiple``: incluye diferentes dominios y la base de datos de la cuenta se mantiene en más de un
      servidor.
    * ``Confianza completa``: existen varios dominios, ninguno esta designado como maestro, sino que todos confían
      completamente en el resto.
    * Sus características principales son:
        * Gestión mediante la consola de administración MMC.
        * Servicios de distribución de Windows (WDS), evolución de RIS, para la implementación de los sistemas
          operativos en múltiples equipos.
        * Nuevo entorno de Windows PowerShell que permite programar scripts de administración y tener acceso a los
          recursos de las aplicaciones desde la propia interfaz, es un intérprete de comandos orientado a objetos. La
          información de entrada y de salida en cada etapa del proceso (cmdlet, "comándulo") es un conjunto de
          instancias de objeto, a diferencia de lo que ocurre con los intérpretes de comandos tradicionales, que
          devuelven y reciben texto.
            * ``get-item``: lista archivos o carpetas
            * ``get-childitem``: lista los archivos o carpetas de un sistema de archivos
            * ``get-command``: lista todos los comandos
            * ``get-process``: lista los procesos activos del equipo local
            * ``remove-item``: borra archivos o carpetas
            * ``copy-item``: copia archivos o carpetas
            * ``set-location``: sitúa el directorio de trabajo en un directorio concreto
            * ``clear-content``: borra el contenido de un objeto pero no el propio objeto.
            * ``clear-item``: limpia el contenido de un objeto pero no el propio objeto
            * ``remove-item``: borra un objeto especifico
            * ``get-WmiObject``: muestra el listado de software instalado por Windows Installer
            * ``get-history``: obtiene el historial de comandos introducidos
            * ``get-service``: lista los servicios en el puesto de usuario
        * Motor de visualización llamado ``Hyper-V``, utiliza la virtualización por hardware.
        * Nuevos servicios de terminal server como el ``RemoteApp``, que permite la ejecución remota de aplicaciones
          desde los equipos cliente sin tener que abrir una sesión.
        * ``IPAM`` (Internet Protocol Address Management): software que puede planificar, hacer seguimiento y
          administrar las direcciones IP usadas en una red de computadoras.
    * ``Versiones``:
        * ``Web Edition``: servidores WEB fundamentalmente y servidores de aplicaciones, incluye .NET Framework, IIS con
          ASP.NET, servidor de aplicaciones, carece de servicios como Active Directory y es posible instalar una versión
          core del mismo. Soportar un máximo de 2 GB de RAM y dos CPU.
        * ``Standar Edition``: proporcionar servicios básicos y recursos a otros sistemas a través de una red. Soporta
          hasta 32 GB de memoria en sistemas de 64 bits.
        * ``Enterprise Edition``: mayor escalabilidad y disponibilidad, dispone de servicios de clustering y Active
          Directory, soporte para el intercambio de RAM en caliente, soporta un máximo de 2 TB de RAM en sistemas de 64
          bit.
        * ``Datacenter Edition``.

#### 4.1. CARACTERÍSTICAS

* Windows Server trabaja con Active Directory, este se centra en la administración de los recursos de la red
  organizativa, independientemente de la ubicación física de dichos recursos, y de la topología de las redes
  subyacentes.
* Los objetos de Active Directory representan usuarios y recursos, como por ejemplo, los ordenadores y las impresoras.
* La estructura lógica de Active Directory se compone de objetos, clases de objetos, unidades organizativas, dominios,
  árboles de dominios y bosques:
    * ``Objetos``: componentes básicos de la estructura lógica. Algunos objetos representan entidades individuales de la
      red, como un usuario o equipo (hojas) y no pueden contener otros objetos. Sin embargo, para facilitar la
      administración y simplificar la organización del directorio, se pueden colocar objetos “hoja” dentro de otros
      objetos denominados objetos contenedor. Los objetos contenedores también pueden contener otros contenedores de
      forma anidada, o jerárquica. Cada objeto puede definirse mediante unas plantillas o modelos definidos por unos
      atributos y valores (
      clases de objetos).
    * ``Unidades organizativas``: tipo más común de objeto contenedor y se pueden utilizar para organizar otros objetos
      con propósitos administrativos, por ejemplo dividir una empresa en departamentos. Organizando éstos es más fácil
      localizar y administrar objetos. También es posible delegar la autoridad para administrar estas unidades
      organizativas de manera que haya administradores de cada una de ellas.
    * ``Dominios``: se usan para agrupar objetos relacionados con el fin de reflejar la red de una organización, son
      colecciones de los objetos administrativos definidos, que comparten en una base de datos común del directorio,
      políticas de la seguridad y relaciones de confianza con otros dominios. Cada dominio que se crea almacena
      información acerca de los objetos que contiene. Los dominios proporcionan un límite administrativo para los
      objetos, medios de administrar la seguridad para los recursos compartidos y una réplica para los objetos.
    * ``Árbol de dominios``: dominios agrupados en estructuras jerárquicas que permiten el uso compartido de recursos
      globales. Cuando se agrega un segundo dominio a un árbol, se convierte en hijo del dominio raíz y este a su vez
      puede tener sus propios hijos, combinándose con el nombre de su padre para formar su propio y único.
    * ``Bosque``: nivel más alto, pueden agruparse árboles dispares para formar un bosque. Un bosque permite combinar
      divisiones diferentes en una organización o, incluso, pueden agruparse organizaciones distintas. El primer dominio
      en el bosque se llama Dominio raíz del bosque y el nombre de ese dominio se refiere al bosque, por ejemplo
      miempresa.com. Por defecto, la información en Active Directory se comparte solamente dentro del bosque. De esta
      manera, la seguridad del bosque estará contenida en una sola instancia de Active Directory. Así que la mayoría de
      las veces nuestra organización será de un sólo dominio (miempresa.com) dentro de un solo bosque.

##

> Importación de usuarios con la herramienta de comando ``CSVDE``: permite la importación/exportación de objetos de AD desde o hacia un archivo de texto (Formato CSV).

##

* Los ``grupos de usuario`` facilitan al administrador las tareas de mantenimiento y gestión de los usuarios, pueden ser
  organizados en grupos y aplicar sobre ellos actualizaciones de forma simultánea, tres tipos de grupos:
    * ``Globales``: pueden contener cuentas de usuario y otros grupos globales del mismo dominio, se usan para las
      tareas más cotidianas de gestión dentro del mismo domino, no se propagan a otros dominios del mismo bosque.
    * ``Locales``: a los miembros de los grupos locales solo se les pueden asignar permisos dentro de un mismo dominio,
      los grupos locales pueden contener dentro de ellos cuentas de cualquier domino, grupos globales de cualquier
      domino, grupos universales de cualquier dominio y grupos locales del mismo dominio.
    * ``Universales``: contienen cuentas de cualquier dominio del bosque, grupos globales de cualquier dominio del
      bosque y grupos universales de cualquier dominio del bosque, a estos grupos se le s pueden asignar permisos en
      cualquier dominio del bosque, son útiles para consolidar grupos que abarquen varios dominios, debe limitarse su
      uso a casos indispensables.

##### 4.1.1. SERVICIOS

* Con el tiempo, Microsoft ha agregado servicios adicionales bajo el estandarte de Active Directory que proporciona un
  framework para otros servicios similares.
    * ``Certificate Server Active Directory`` (AD CS): servicios y funcionalidades que permite que un servidor emita
      certificados digitales para asegurar los sistemas y las comunicaciones en red.
    * ``Servicios de Domino de Active Directory`` (AD DS): proporcionar los servicios de directorio en un dominio, emite
      certificados digitales para asegurar los sistemas y las comunicaciones en red.
    * ``Servicios de Federación de Active Directory`` (AD FS): complementan las características de autenticación y
      gestión de acceso que proporciona AD DS, extendiéndolas a la WEB, la gestión de los accesos a los sistemas y
      recursos desde el exterior, internet.
    * ``Servicios de directorio activo ligero de Active Directory`` (AD LDS): almacén de datos a las aplicaciones de
      datos a las aplicaciones basadas en la utilización del directorio, puede ser empleado en grupos de trabajo.
    * ``Active Directory Rights Management Services`` (AD RMS): capa de seguridad en la protección de la información de
      la organización, proteger los accesos no autorizados, establecimiento de relaciones de confianza.

> Las impresoras se publican en el almacén de AD como objetos printQueu, estos contienen un subconjunto de la información almacenada en el servidor de impresión. Cualquier impresora compartida se publica en los servicios de AD.

* Herramientas de comandos de AD: permiten gestionar los objetos de AD, son:
    * ``dsadd``: crea un objeto en el directorio.
    * ``dsget``: obtiene atributos de un objeto del directorio.
    * ``dsmod``: modifica atributos.
    * ``dsmove``: mueve un objeto entre contenedores o OU del directorio.
    * ``dsrm``: elimina un objeto o todos los objetos de un subárbol bajo un contexto.
    * ``dsquery``: realiza una consulta y devuelve una lista con los objetos que coinciden con los parámetros de la
      búsqueda. (“dsquerry:computer”: busca ordenadores en el directorio).

#### 4.2. GESTIÓN DE POLÍTICAS DE GRUPO

* Ofrecen infraestructura, centralizan las configuraciones que se implementan en los usuarios y/o equipos.
* En un entorno administrativo mediante directivas de grupo todas las configuraciones se realizan a través de objetos de
  política de grupo (GPO) ejecutando “gpedit.msc”, pueden afectar a una OU, a un sitio o a un domino.
* Mediante directivas de grupo se puede configurar prácticamente todo desde la configuración de seguridad, la
  implementación de software, las directivas de contraseñas y auditoría.
* El método más habitual de delimitar el ámbito de un GPO es vincularlo a un sitio, dominio o OU a través de GPMC. Las
  GPO se gestionan a través de la Group Policy Management Console (GPMC), puede tener tres estados:
    * ``No configurada``: el GPO no modificara la configuración existente de esa configuración particular para el
      usuario o grupo.
    * ``Habilitada o deshabilitada``: se producirá un cambio en la configuración de usuario so equipos a los que se
      aplique dicha directiva.

* Las configuraciones de directivas se aplican cuando se inicia una sesión de usuario y después requieren el cierre de
  sesión, pero es posible forzar la actualización de directivas con comando “gupdate/target:equipo” o “gupdate/target:
  usuario”.
* Las Directivas de Grupo se procesan:
    * ``Sitio``: el ordenador procesa todas las políticas de grupo que se aplican al sitio en el que se encuentra
      actualmente el equipo.
    * ``Dominio``: cualesquiera políticas aplicadas en el nivel de dominio (ámbito de la política por defecto) se
      procesan a continuación.
    * ``Unidad organizativa``: último grupo de políticas asignado a la unidad organizativa que contiene la computadora o
      el usuario que se procesan.

* > ``gpresult``: muestra información del conjunto de directivas para un usuario y equipo remotos.
* > ``gpupdate``: actualiza la configuración de directiva de grupo.

#### 4.3. CARPETAS COMPARTIDAS (ofrece dos modos de compartición de archivos):

* ``Modo estándar``: acceso a recursos de red como archivos, carpetas y unidades, la compartición de una unidad o
  carpeta se aplica a todas las subcarpetas y archivos contenidos en dicha carpeta y/o unidad, se puede aplicar a discos
  con formato FAT32, NTFS... Para gestionar se usa la herramienta “administración de almacenamiento y recursos
  compartidos”, y también con el comando net (net share, net sessions).
* ``Modelo público``: consiste en copiar o trasladar los archivos a una carpeta pública, estarán accesibles para
  cualquier usuario que inicie una sesión local en dicha máquina. Si dicha carpeta pública se comparte, existe la
  posibilidad de establecer permisos de acceso a esta carpeta a través de la red. La carpeta pública está ubicada en
  %SystemDrive%/Users/Public.

#### 4.3. GESTIÓN DE DISPOSITIVOS

* El almacenamiento local y de red se ha simplificado para el usuario, proporciona soporte tanto para almacenamiento
  remoto como para almacenamiento local y en medios extraíbles, todo de forma completamente transparente al usuario, el
  usuario no tiene que preocuparse de sí un programa o archivo se almacena en disco, en cinta o en cualquier parte de
  internet, solo de que esté disponible cuando sea necesario. La interfaz está basada en la consola de administración  
  (MMC), permite administrar discos locales y discos remotos en otras computadoras.

#### 4.4. GESTIÓN DE DISCOS

* Windows Server utiliza particiones MBR (Master Boot Record) y GPT (GUID Partition Table) al igual que Windows 7, la
  herramienta fundamental para la gestión de discos es “diskpart”, se pueden configurar tres tipos de discos:
    * ``Básico``: pueden dividirse en porciones de almacenamiento más pequeñas denominadas particiones, dos tipos de
      particiones en un disco básico: primaria y extendida y esta a su vez se puede dividir en particiones lógicas.
    * ``Dinámico``: da la posibilidad de administrarlo sin la necesidad de reiniciar en la  
      mayoría de las ocasiones, ampliar un volumen de disco, extender un volumen entre múltiples discos duros, realizar
      secciones de un volumen para mejorar su  
      rendimiento, hacer un espejo o añadirlo a un array RAID 5, todo desde MMC y sin tener que reiniciar, la creación
      inicial o conversión de un disco básico a disco dinámico si necesitara reinicio. Se pueden organizar en simples,
      stripped y spanned.
    * ``Extraíble``: propio de unidades de disco extraíble. Se dispone de una herramienta grafica “Administrador de
      cuotas del administrador de recursos del servidor de archivos”, dos tipos de cuotas:
        * ``Cuotas de disco NTFS``: se emplean para administrar la utilización del espacio de disco que hacen los
          usuarios. Se configuran por volumen, es posible configurar mensajes de advertencia, para definir los límites
          de uso de disco:
            * denegar espacio de disco a usuarios que excedan el límite de cuota,
            * limitar espacio de disco,
            * establecer el nivel de advertencia.
        * ``Cuotas de disco del administrador de recursos``: permiten gestionar el espacio ocupado por carpetas y
          volúmenes cuando un usuario se aproxima o exceda la cuota recibirá un aviso.

#### 4.4. GESTIÓN DE IMPRESIÓN EN WINDOWS SERVER

* Está diseñado para la impresión en red, las aplicaciones envían los trabajos de impresión a las impresoras conectadas
  a un servidor de impresión de Windows Server.
* Varias configuraciones básicas de clientes, servidores y dispositivos de impresión, dependiendo de si es remoto o no:
    * ``Dispositivo de impresión local no remoto``: está enchufada a un puerto del ordenador, el controlador de la
      impresora y la cola de trabajos están en esa computadora que envía los datos a directamente al dispositivo de
      impresión.
    * ``Pequeño grupo de equipos que comparten un dispositivo de impresión en red``: una red donde cada ordenador tienen
      igual acceso al dispositivo de impresión y no hay un control central de impresión o de seguridad, cada equipo
      tiene su propia cola de trabajos y no puede ver los documentos en la cola en el dispositivo de impresión por otras
      computadoras.
    * ``Servidor central de impresión``: el acceso al dispositivo de impresión es a través del servidor que está
      conectado localmente al dispositivo de impresión, la cola de trabajos se encuentra en el servidor y es visible
      para cada cliente.
    * ``Varios clientes que comparten un dispositivo de impresión en un dominio``: el dispositivo de impresión se
      conecta al servidor a través de la red, permitiendo que un servidor de impresión que administre varios
      dispositivos de impresión.

* Una página de separación es un archivo que contiene órdenes del dispositivo de impresión, identifica y separar los
  documentos impresos y cambia entre los modos de impresión (se pueden utilizar páginas de separación para determinar el
  lenguaje de descripción de página, PostScript o PCL).

* Windows incluye cuatro archivos de páginas de separación de forma predeterminada, pero se pueden crear páginas de
  separación personalizadas creando un archivo “.sep”:
    * ``Pcl.sep``: cambia el modo de impresión a PCL.
    * ``Pscript.sep``: cambia el modo de impresión a PostScript
    * ``Sysprint.sep``: imprime una página antes de cada documento, compatible con PostScript.
    * ``Sysprtj.sep``: una versión de “Sysprint.sep” que utiliza caracteres japoneses.

> Para que un servidor de impresión de Windows server soporte páginas web es necesario instalar en el servidor de impresión los servicios de información de internet (IIS Internet Information Services). Se crea un directorio virtual Printers debajo del sitio web predeterminado, este directorio apunta a la carpeta %systemroot%\\web\\printers.

* Un ``grupo de impresoras`` es una impresora que está conectada a múltiples dispositivos de impresión a través de
  múltiples puertos de un servidor de impresión, pueden ser dispositivos de impresión locales o de red.
* Cuando se crea un grupo de impresoras, los usuarios pueden imprimir documentos sin tener que averiguar qué dispositivo
  de impresión está disponible, la impresora busca un puerto disponible; disminuye el tiempo que esperan los documentos
  en el servidor de impresión y simplifica la administración porque se pueden administrar múltiples dispositivos de
  impresión desde una sola impresora.
* Esto hace posible establecer prioridades entre grupos de documentos que se imprimen en el mismo dispositivo de
  impresión, los críticos siempre se imprimen primero.

#### 4.5. GESTIÓN DE LAS ACTUALIZACIONES DE WINDOWS

* ``WSUS`` (Windows Server Update Services) versión privada del servicio Microsoft Update, desde el que los equipos
  pueden desplegar actualizaciones automáticamente, se puede emplear para distribuir actualizaciones además es posible
  mantener un control total sobre las actualizaciones instaladas, supone una conexión del servidor en que está instalado
  al sitio de Microsoft Update, se descargar la información de las actualizaciones disponibles y se agrega a una lista
  que posteriormente tiene que aceptar el administrador.
* El servidor WSUS establece conexión HTTP o HTTPS (80/443) con el sitio web de Windows Update.

#### 4.6. MICROSOFT EXCHANGE SERVER

* Microsoft Exchange Server es un software propietario de colaboración entre usuarios, desarrollado por Microsoft. Es
  parte de la familia Microsoft Server ya que es una de las aplicaciones destinadas para el uso de servidores.
    * ``Exchange ActiveSync``: protocolo de sincronización de Exchange, basado en HTTP y XML, permite a los teléfonos
      móviles acceder a la información (correo electrónico, calendario...) de la organización en un servidor que está
      ejecutando Microsoft Exchange. Se puede configurar ActiveSync para utilizar cifrado SSL. Puede establecer
      directivas, iniciar una limpieza remota, ejecutar informes, controlar los tipos de dispositivos móviles mediante
      reglas de acceso...
    * Algunos comandos para su administración son:
        * ``GetBulkRequest``: cuando es requerida una larga transmisión de datos, tal como la recuperación de largas
          tablas.
        * ``InformRequest``: transmite un mensaje de este tipo a otro con las mismas características, para notificar
          información sobre objetos administrados.
        * ``Trap``: mensajes no solicitados enviados por los agentes al administrador SNMP si ocurre algún evento
          inesperado.

* > ``DAG`` (Database Availability Group): contiene servidores de buzones de correo que se convierten en miembros del DAG.
* > Una vez que un servidor de buzones de correo es miembro de un DAG, las bases de datos de buzones de ese servidor se pueden copiar a otros miembros del DAG.
* > Asumiendo que no haya problemas de replicación y que las bases se encuentren disponibles, dentro de un DAG de Exchange estas pueden encontrarse “Mounted (Activa)” o “Healthy (Pasiva)”.
* > En ningún caso una misma base de datos puede estar activa en más de un servidor a la vez.

### 5\. NOVEDADES EN WINDOWS SERVER 2012 Y 2016

* ``2012``:
    * Powershell incluye mayor cantidad de comandos.
    * PAM (IP Address Management): función de administración de direcciones IP para la búsqueda, monitoreo, auditoria y
      administración del espacio de direcciones IP usados en la red corporativa.
    * Mejoras en AD, como un interfaz gráfico.
    * Hyper-V: incluye soporte para virtualización de redes y copias de seguridad en la nube.
    * ReFS (Resilient File System): mejora NTFS.
    * Nueva versión de IIS (IIS 80).
    * LAPS (Local Administrator Password Solution)

* ``2016``:
    * Windows Defender.
    * Soporte para librerías OpenGL y OpenCL.
    * Failover Clustering: clúster de actualización gradual del sistema operativo con soporte para réplicas de
      almacenamiento.
    * Web Aplication Proxy.
    * ISS 10: soporte para HTTP/2.
    * Powershell 5.0
    * “Reinicio Suave”: reinicia solo el software sin tener que inicializar el hardware.

### 6\. SISTEMAS OPERATIVOS PARA DISPOSITIVOS MÓVILES

* Fabricantes de hardware que son los fabricantes de sus propios SO: Apple.
* Fabricantes de dispositivos que utilizan SO de otras compañías: Android, Windows Mobile.

#### 6.1. ANDROID (construido a partir de la versión 2.6 del kernel de Linux en 2008 (v. 1.0)):

* 1.0 Apple Pie (Alpha).
* 1.1 Banana Bread (Beta).
* 1.5 Cupcake.
* 1.6 Donut.
* 2.0 Eclair.
* 2.2 Froyo.
* 2.3 Gingerbread.
* 3.0 Honeycomb (sólo para tablets).
* 4.0 Ice Cream Sandwich / 4.1-4.3 Jelly Bean / 4.4 KitKat.
* 5.0 Lollipop. (ART).
* 6.0 Marshmallow. (Adoptable Storage).
* 7.0 Nougat.
* 8.0 Oreo.
* 9.0 Pie.
* 10 Quince Tart.
* 11 Red Velvet Cake.
* 12 Snow Cone.
* 13 Tiramisú.
* 14 Upside Down Cake.
* 15 Vanilla Ice Cream.
* 16 Baklava.

* Basa el funcionamiento de sus aplicaciones en una máquina virtual Java que ejecuta cada aplicación en un proceso
  propio, donde se lanza una nueva máquina virtual llamada Dalvik, sustituida por ART (Android Runtime) en Android 5.0.
* Las aplicaciones se distribuyen en ficheros empaquetados “.apk”, posee un navegador integrado basado en WebKit, los
  gráficos están optimizados por una librería grafica 2D propia y OpenGL para gráficos 3D, para el almacenamiento de
  datos utiliza como gestor de bases de datos SQLite.

#### 6.2. IOS

* Esta limitado a la instalación en hardware propietario, la versión más actual es IOS 13.2. Deriva del sistema
  operativo de ordenadores Mac (OS X), es un sistema UNIX, la pantalla principal (SpringBoard).

* > ``Swift``: lenguaje de programación multiparadigma creado por Apple enfocado en el desarrollo de aplicaciones para iOS y macOS.
* > ``FileVault``: tecnología que proporciona capacidades de cifrado para todo el sistema de almacenamiento principal de un equipo macOS, usando el método de encriptación AES.
* > ``Gatekeeper``: es una función de seguridad de macOS. Hace cumplir la firma de código y verifica las aplicaciones descargadas antes de permitir que se ejecuten.

#### 6.3 TIPOS DE APP MÓVILES

* ``Nativas``: se diseñan y desarrollan específicamente para un sistema operativo en particular, empleando un lenguaje
  de programación específico, son fluidas, estables y permiten obtener el máximo provecho de las funcionalidades del
  dispositivo.
* ``Web``: se desarrollan con lenguajes como es el caso de HTML, CSS o Javascrip. Se accede a ellas mediante un
  navegador web por lo que cualquier dispositivo puede entrar en ellas. PWA “Progressive Web App” páginas web, pero
  mediante el uso de Service Workers y otras tecnologías se comportan más como aplicaciones normales que como
  aplicaciones web, es decir, pueden seguir ejecutándose en segundo plano.
* ``Híbridas``: combinación de los dos tipos de apps descritos con anterioridad, serán desarrolladas con lenguajes de
  programación típicos de una web, pero su estructura externa estará basada en lenguajes de programación propios del
  dispositivo móvil.

#### 6.4 TENDENCIAS EN SO

* Uso de sistemas operativos en la nube, ahorro de costes en licencias. Plataformas de virtualización de sistemas
  operativos y del software de aplicación en las máquinas virtuales.
* Tipos de servicios Cloud:
    * ``IaaS`` (Infraestructure as a Service): el consumidor alquila recursos IT, no controla la infraestructura cloud,
      pero tiene control directo sobre el SO, computación, almacenamiento, deploy de aplicaciones y red. Se realiza a
      través de virtualización, externalizando todos estos recursos y lo delegan al proveedor de servicios externo (
      Amazon Web Services, Windows Azure, Rackspace, Openstack).
    * ``PaaS`` (Platform as a Service): ofrece todo lo necesario para soportar el ciclo de vida completo de
      desarrollo/construcción y puesta en marcha (deploy) de aplicaciones y servicio web mediante lenguajes o
      herramientas soportadas por el proveedor (java, phyton...). Proporciona control completo sobre las aplicaciones
      desplegadas y sobre los ajustes de configuración de estas, es usado principalmente por desarrolladores. (Servicios
      de Azure, Google App Engine, OpenShift...).
    * ``SaaS`` (Software as a Service): las aplicaciones del proveedor son accesibles como servicios, el consumidor no
      controla la infraestructura ni las capacidades de las aplicaciones. (Office 365, Suit de Google...).

    * ``Git`` es un software de control de versiones, eficiencia, confiabilidad y compatibilidad del mantenimiento de
      versiones de aplicaciones cuando estas tienen un gran número de archivos de código fuente. Comandos GIT:
        * ``init``: creará un nuevo repositorio local GIT.
        * ``clone``: se usa para copiar un repositorio
        * ``add``: agregar archivos al área de preparación.
        * ``commit``: creará una instantánea de los cambios y la guardará en el directorio git.
        * ``config``: establecer una configuración específica de usuario, como el email, user...
        * ``status``: muestra la lista de los archivos que se han cambiado junto con los archivos que están por ser
          preparados o confirmados.
        * ``push``: se usa para enviar confirmaciones locales a la rama maestra del repositorio remoto.
        * ``checkout``: crea ramas y te ayuda a navegar entre ellas.
        * ``remote``: lista los repositorios remotos.
        * ``branch``: listar, crear o borrar ramas.
        * ``pull``: fusiona todos los cambios que se han hecho en el repositorio local con el directorio de trabajo
          local.
        * ``merge``: fusionar una rama con otra rama activa.
        * ``diff``: hacer una lista de conflictos.
        * ``tag``: marca commits específicos.
        * ``log``: se usa para ver el historial del repositorio listando ciertos detalles de la confirmación.
        * ``reset``: sirve para resetear el index y el directorio de trabajo al último estado de confirmación.
        * ``rm``: remover archivos del index y del directorio de trabajo.
        * ``stash``: guardará momentáneamente los cambios que no están listos para ser confirmados
        * ``fetch``: buscar todos los objetos de un repositorio remoto que actualmente no se encuentran en el directorio
          de trabajo local.
        * ``show``: mostrar información sobre cualquier objeto git.
        * ``grep``: permite al usuario buscar frases y palabras específicas en los árboles de confirmación, el
          directorio de trabajo y en el área de preparación.

##

> ``ownCloud``: aplicación de software libre del tipo Servicio de alojamiento de archivos, que permite el almacenamiento en línea y aplicaciones en línea (cloud computing). ownCloud puede ser instalado dentro de un servidor que disponga de una versión reciente de PHP (mayor o igual a 5.6) y soporte de SQLite (base de datos por defecto), MySQL o PostgreSQL.

##

> ``OpenShift``: producto de computación en la nube de plataforma como servicio de Red Hat. Los desarrolladores pueden usar Git para desplegar sus aplicaciones Web en los diferentes lenguajes de la plataforma. OpenShift se encarga de mantener los servicios subyacentes a la aplicación y la escalabilidad de la aplicación como se necesite. Origin: la versión de código abierto de Open Shift, utiliza Docker para la gestión de contenedores y Kubernetes para la gestión de grupos de contenedores. Todo el código del proyecto está disponible sobre la licencia Apache en GitHub. Azure DevOps: anteriormente Team Foundation Server (TFS), es un producto de Microsoft que proporciona control de versiones, informes, gestión de requisitos, gestión de proyectos, building automatizado y testing.

##

> ``Bitbucket``: servicio de alojamiento basado en web, para los proyectos que utilizan el sistema de control de versiones Mercurial y Git, similar a GitHub.

##

> ``Software MDM`` (mobile device management): es un tipo de software que permite asegurar, monitorizar y administrar dispositivos móviles sin importar el operador de telefonía o proveedor de servicios. La mayoría de las MDM permiten instalar aplicaciones, localizar y rastrear equipos, sincronizar archivos, reportar datos y acceder a dispositivos, todo esto de manera remota. MobileIron: un MDM que permite la seguridad y la gestión de dispositivos móviles como teléfonos inteligentes y tabletas en un entorno empresarial, así como el acceso móvil seguro a los datos empresariales.

##

* ``TIPOS DE SOFTWARE``, en función de su proximidad al hardware:
    * ``Software de base``: compuesto por programas que interactúan directamente con el hardware del SO.
    * ``Software de utilidad``: utilizado como herramienta básica en tareas de mantenimiento, soporte y ejecución.
    * ``Software de aplicación``: realización de tareas específicas, aplicaciones ofimáticas, software educativo,
      editores de música...

7\. SERVICE-ORIENTED ARCHITECTURES (SOA)  
Es un estilo de arquitectura de TI que se apoya en la orientación a servicios. Un servicio es una representación lógica
de una actividad de negocio que tiene un resultado de negocio específico. SOA se caracteriza por los principios:  
``Contrato de servicios estandarizados``: los servicios adhieren a un acuerdo de comunicación, según se define en
conjunto con uno o más documentos de descripción de servicios.  
``Acoplamiento débil de sistemas``: los servicios mantienen una relación que minimiza las dependencias y sólo requiere
que mantengan un conocimiento de uno al otro.  
``Abstracción de servicios``: más allá de las descripciones del contrato de servicios, los servicios ocultan la lógica a
los demás.  
``Reutilización de servicios``: lógica se divide en servicios para promover la reutilización.  
``Autonomía de servicios``: los servicios tienen control sobre la lógica que encapsulan, desde una perspectiva de diseño
y ejecución.  
``Servicios sin-estado``: los servicios minimizan el consumo de recursos aplazando la gestión de la información de
estado cuando sea necesario.  
``Descubrimiento de servicios``: los servicios se complementan con los metadatos mediante los cuales se pueden descubrir
e interpretar la eficacia.  
``Composición de servicios``: servicios están compuestos por partes eficazmente,  
independientemente del tamaño y la complejidad de la composición.  
``Granularidad de servicios``: una consideración de diseño para proporcionar un ámbito óptimo y un correcto nivel
granular de la funcionalidad del negocio en una operación de servicio.  
``La normalización de servicios``: los servicios se descomponen a un nivel de forma normal para minimizar la
redundancia. En algunos casos, los servicios se desnormalizan para fines específicos, como la optimización del
rendimiento, el acceso y agregación.  
``Optimización de servicios``: los servicios de alta calidad son preferibles a los de baja calidad.  
``Relevancia de servicios``: la funcionalidad se presenta en un nivel de granularidad reconocido por el usuario como un
servicio significativo.  
``Encapsulación de servicios``: muchos servicios están consolidados para el uso de SOA. A menudo, estos servicios no
fueron planificados para estar en un SOA.  
``Transparencia de ubicación de servicios``: se refiere a la capacidad de un consumidor de servicios para invocar a un
servicio independientemente de su ubicación en la red. Esto también reconoce la propiedad de descubrimiento (uno de los
principios fundamentales de SOA) y el derecho de un consumidor para acceder al servicio. A menudo, la idea de la
virtualización de servicios también se refiere a la transparencia de ubicación. Aquí es donde el consumidor simplemente
llama a un servicio lógico, mientras que un SOA habilita la ejecución del componente de la infraestructura, normalmente
un bus de servicios, que mapea este servicio lógico y llama al servicio físico.

8\. MICRO SERVICES ARCHITECTURE (MSA):  
Desarrollo de software que consiste en construir una aplicación como un conjunto de pequeños servicios, que se ejecutan
en su propio proceso y se comunican normalmente con una API de recursos HTTP. Cada servicio se encarga de implementar
una funcionalidad, es desplegado de forma independiente y puede estar programado en distintos lenguajes y usar
diferentes tecnologías. ``Características``:  
``Cada microservicio tiene un nombre único`` (URL): se usa para resolver su ubicación y debe ser direccionable en
cualquier lugar donde se ejecute (de la misma manera que DNS resuelve una URL para un equipo en particular, su
microservicio debe tener un nombre único para que su ubicación actual sea reconocible).  
``Los servicios son componentes``: están separados y se comunican mediante mecanismos como los servicios web o los RPC
en lugar de usar llamadas a funciones en memoria.   
``Organizada en torno a las funcionalidades del negocio``: el sistema se divide en distintos servicios donde cada uno
está organizado en torno a una capacidad del negocio. Es muy importante limitar la responsabilidad de cada servicio.
Cada servicio implementa toda la funcionalidad del negocio que agrupa desde la interfaz de usuario, la persistencia en
el almacenamiento y cualquiera de las colaboraciones externas.  
``Productos, no proyectos``: se sigue la idea de que un equipo debe estar a cargo de un componente (servicio) durante
todo el ciclo de vida del mismo, desde la etapa de diseño y construcción, la fase de producción y hasta la de
mantenimiento. Esta mentalidad se acopla bien con la vinculación a una capacidad del negocio. En lugar de ver el
software como un conjunto de funcionalidades terminadas se ve como una relación continua, esto es facilitado por el bajo
nivel de granularidad que ofrecen los microservicios.  
``Extremos inteligentes, tuberías bobas``: las aplicaciones creadas desde microservicios pretenden ser tan disociadas y
cohesivas como sea posible, ellas poseen su propia lógica de dominio y actúan como filtros en el clásico sentido UNIX:
recibe una solicitud, aplica la lógica apropiada y produce una respuesta. Estos pasos son coreografiados usando
protocolos simples (típicamente HTTP con REST o mensajería liviana como RabbitMQ o ZeroMQ).  
``Tener gobierno descentralizado`` permite usar tecnologías que se adapten mejor a cada funcionalidad. En un sistema con
múltiples servicios colaborativos, podemos decidir utilizar diferentes lenguajes de programación y tecnologías dentro de
cada servicio. De esta forma podemos elegir la herramienta adecuada para cada tipo de trabajo en lugar de tener una
estandarizada.  
``Gestión de datos descentralizada``: los microservicios prefieren dejar a cada servicio que gestione su propia base de
datos, sean estas diferentes instancias de la misma tecnología de base de datos o sistemas de base de datos
completamente diferentes.

El estilo de microservicios tiene implicaciones en el manejo de las actualizaciones las cuales tradicionalmente han
usado transacciones para garantizar la consistencia. Las transacciones imponen un acoplamiento temporal lo que se vuelve
problemático cuando hay varios servicios. Como las transacciones distribuidas son mucho más difíciles de implementar,
las arquitecturas de microservicios promueven la coordinación no transaccional entre servicios, con el reconocimiento
explícito que la consistencia puede ser una consistencia eventual y los problemas son compensados operativamente. El
sistema merece la pena siempre y cuando el costo de solucionar los errores sea menor que el costo de perder negocios por
una mayor consistencia. Los microservicios no obligan a tener distintas tecnologías de almacenamiento, sólo lo
permiten.  
``Diseño tolerante a fallos``: las aplicaciones necesitan ser diseñadas de modo que puedan tolerar las fallas de los
distintos servicios. Cualquier llamada de servicio puede fallar y el cliente tiene que ser capaz de responder a esto con
la mayor facilidad y eficacia posible, evitando los muy habituales fallos en cascada de las arquitecturas
distribuidas.  
``Automatización de la infraestructura``: la mayoría de los productos y sistemas desarrollados con el enfoque de
microservicios han sido construidos por equipo que usan entrega continua y su precursor la integración continua.  
``Diseño evolutivo``: cuando se divide el sistema en servicios hay que tener en cuenta que cada uno tiene que poder ser
reemplazado o actualizado de forma independiente. Es decir, tiene que permitir una fácil evolución. El diseño del
servicio tiene que ser de tal forma que evite en lo posible que la evolución de los servicios afecte a sus consumidores.

| AMQ de Red Hat: es una plataforma de mensajería flexible que permite la integración en tiempo real y la conexión a Internet de las cosas (IoT). |
| :---- |

TEMA 4 – ESTRUCTURAS, ALGORITMOS Y FORMATOS DE INFORMACIÓN  
1\. ESTRUCTURAS DE DATOS (tipos de datos más habituales):  
``Estáticos`` (tamaño de memoria fijo definido en compilación):

* ``Valores lógicos`` (boolean): Almacenan “true” o “false”.
* ``Números enteros``: valores numéricos enteros en formato de punto fijo.
* ``Números reales``: valores numéricos reales (que pueden tener parte decimal) en formato de punto flotante.
* ``Caracteres``: letras, símbolos ASCII.
* ``Punteros o referencias``: números enteros que hacen referencia a direcciones de memoria, donde se supone que se
  almacenan otras estructuras.
* ``Vectores`` (arrays): conjuntos formados por datos del mismo tipo, estructuras de datos contiguas, cada dato
  individual se denomina celda y se identifica mediante un índice. Destacan los vectores de caracteres llamados “String”
  se utilizan para representar textos.
* ``Registros``: conjuntos formados por datos que pueden ser de distintos tipos, cada dato individual se denominan campo
  y se identifica mediante un nombre.

``Dinámicos``:

* ``Lista``: tipo de datos compuesto que permite almacenar elementos simples o compuestos todos del mismo tipo, cada
  elemento va seguido de otro del mismo tipo o de ninguno y sus componentes.
* ``Pila`` (LIFO: Last In First Out): almacena datos y recuperarlos de forma invertida.
* ``Cola`` (FIFO: First In First Out): almacena datos de forma ordenada, se recupera la información guardada en el orden
  en que se almacenó.
* ``Árbol``: organiza datos jerárquicamente, cada dato (llamado nodo) padre tiene asociados un conjunto de datos (nodos)
  hijos.
* ``Grafos``: parecidos a los árboles, pero cada nodo puede estar asociado con cualquier otro nodo o nodos y consigo
  mismo.

Todas estas estructuras se utilizan para almacenar información en la memoria principal, para guardar la información en
los discos se utilizan unas estructuras llamadas ficheros y tienen la misma estructura que la memoria principal.

2\. TIPOS ABSTRACTOS DE DATOS  
Los tipos de datos abstractos (TDA) son una arquitectura de información compuesta por la abstracción de datos y
procesos (llamado implementación de los mismos). Son una colección de operaciones definidas sobre un conjunto de datos
para el modelo de datos, creadas a partir de arrays. Estas estructuras se dividen en:  
``Lista``: estructura de datos secuencial, sus datos se ordenan de forma consecutiva. Se clasifican, por la manera de
acceder al siguiente elemento en:

* ``Densa``: la propia estructura determina cual es el siguiente elemento de la lista.
* ``Enlazada``: la posición del siguiente elemento de la estructura la determina el elemento actual, es dinámica, su
  tamaño cambia durante la ejecución del programa. Es, a su vez, un elemento de información y un enlace hacia una
  lista (un nodo).

``Pila`` (LIFO: Last In First Out): estructura de datos secuencial de acceso restrictivo a sus elementos, la recesividad
de simula en un ordenador con la ayuda de una pila.  
``Cola`` (FIFO: First In First Out): estructura de datos secuencia l de acceso restrictivo, el primero que llegue será
el primeo en entrar.  
``Árbol``: estructura de datos no secuencial, un elemento o clave de información con (nodo) más un numero finito de
estructuras tipo árbol llamadas subárboles, si cada nodo tiene un número de hijos igual o inferior a 2, será un árbol
binario y si las alturas de los dos subárboles de todo nodo difieren a lo sumo en 1 será
un ``árbol binario balanceado`` (AVL). Por el contrario si no tienen ningún nodo se llama ``árbol vacío o nulo``
. ``Conceptos``:

* ``Raíz``: nodo superior de un árbol (no tiene antecesor).
* ``Hijo``: nodo conectado directamente con otro superior a través de una rama.
* ``Padre``: nodo conectado directamente con otro inferior a través de una rama.
* ``Hoja``: nodo que no tiene hijos.
* ``Nodo interno``: aquel que tiene al menos un hijo.
* ``Grado de un nodo``: número de hijos directos que tiene.
* ``Altura de un nodo``: número de ramas en el camino más largo entre ese nodo y una hoja.
* ``Grado de un árbol``: igual al grado del nodo con más hijos.
* ``Altura de un árbol``: igual a la altura de su raíz.
* ``Nivel``: 1 \+ (el número de ramas entre el nodo y la raíz).
* ``Anchura``: el mayor valor del número de nodos que hay en un nivel.

``Recorridos`` en árboles binarios:

* ``Preorden``: procesar primero la raiz, después procesar el subárbol izquierdo y por último el subárbol derecho.
* ``Inorden``: procesa el subárbol izquierdo hacia arriba, con su raiz, y después el subárbol derecho hacia abajo con su
  raíz.
* ``Postorden``: primero el subárbol izquierdo, después el subárbol derecho, y por último el nodo actual. Permite borrar
  el árbol de forma consistente.

``Grafo``: conjunto de elementos llamados vértices o nodos que se encuentran unidos entre si mediante enlaces llamadas
aristas. Terminología:

* ``Camino``: lista de vértices en la que dos elementos sucesivos están conectados por una arista del grafo.
* ``Grafo conexo``: existe un camino desde cualquier nodo del grafo hasta cualquier otro.
* ``Camino simple``: camino entre dos nodos en el que ningún nodo ser repite, si tiene como primer y último nodo el
  mismo se denomina ciclo.
* ``Grafo completo``: Grafo que cuenta con todas las aristas posibles, si le falta poco para ser completo será un grafo
  denso mientras que si tiene pocas aristas será disperso.
* ``Grafo dirigido``: las aristas llevan asociado un sentido de desplazamiento, cuando la arista se puede recorrer en
  cualquier sentido, hablamos de grafos no dirigidos.
* ``Grafo ponderado``: las aristas tienen un coste asociado denominado peso.

| Árbol recubridor (o árbol de expansión): dado un grafo conexo y no dirigido, es un subgrafo que tiene que ser un árbol y contener todos los nodos (vertices) del grafo inicial. Kruskal: algoritmo de la teoría de grafos para encontrar un árbol recubridor mínimo en un grafo conexo y ponderado. |
| :---- |

3\. ORGANIZACIONES DE FICHEROS  
3.1. CONCEPTOS Y DEFINICIONES  
``Memoria principal``: poca capacidad de almacenamiento, volátil y de acceso rápido.  
``Memoria secundaria``: capacidad de almacenamiento ilimitada, la información esta almacenada permanentemente y el
acceso es lento, ya que la información tiene que ser transportada desde el dispositivo externo hasta la memoria
principal, el área de memoria principal destinada a recibir esta información se llama “Buffer”.  
``Registro lógico``: colección de información relativa a una entidad particular va a contener a todos aquellos campos
lógicamente relacionados referentes a una determinada entidad.  
``Archivo o fichero``: colección de registro relacionad entre si con aspectos en común y organizados. Los datos en los
archivos deben estar organizado de tal forma que puedan ser recuperado fácilmente actualizaos o borrados.  
``Base de datos``: colección de archivos a los que puede accederse por un conjunto de programas y contiene todos ellos
datos relacionados.  
``Clave``: campo o conjunto de campos de dato que identifica al registro y lo diferencia del resto de registros del
fichero.  
``Registro activo``: registro lógico que va a procesarse en la siguiente operación del fichero.  
``Apuntador``: marca interna que siempre apunta al registro activo.  
``Registro físico o bloque``: la cantidad más pequeña de datos que puede transferirse en una operación de
entrada/salida. La adaptación consiste en empaquetar en cada bloque tantos registros lógicos como se pueda, el
empaquetamiento puede ser de tipo fuerte o débil, según se permita o no aprovechar el sobrante de un bloque, situando
registros a caballo entre dos bloques contiguos.  
``Factor de bloqueo``: el número de registros lógicos que puede contener un registro físico.

3.2. CLASIFICACIÓN DE FICHEROS  
``Ficheros permanentes``: contiene datos relevantes para una aplicación.

* ``Ficheros maestros``: estado actual de los datos (fichero de clientes actuales de un banco).
* ``Ficheros constantes``: datos fijos para la aplicación (el fichero de códigos postales).
* ``Ficheros históricos``: datos que fueron actuales en el pasado (fichero de clientes que se han dado de baja).

``Ficheros temporales``: datos relevantes para un proceso so programa, se utilizan para actualizar los ficheros
permanentes.

* ``Ficheros de movimiento``: almacenan resultados de un programa que han de ser utilizados por otro, dentro de una
  misma tarea.
* ``Ficheros de maniobras``: almacenar datos propios de un programa que este no puede conservar en memoria principal,
  por falta de espacio en esta (programas de cálculo, editores...).
* ``Ficheros de resultados``: almacenar datos elaborados que van a ser transferidos a un dispositivo de salida.

3.3. ORGANIZACIÓN Y ACCESO  
La manera en que los datos son estructurados y almacenados internamente en el fichero se establece durante la fase de
creación del mismo, muy dependiente del soporte físico. Hay dos tipos de soportes:  
``Soportes secuenciales``: los registros están dispuestos físicamente uno a continuación de otro, se necesita pasar por
todos los anteriores a él.  
``Soportes direccionables``: localizan a un registro directamente por su información (clave) sin tener que pasar por
todos los anteriores.

El ``acceso`` es el procedimiento necesario que debemos seguir para situarnos sobre un registro, ``dos tipos`` de
acceso:  
``Acceso secuencial``: acceso a un archivo según el orden de almacenamiento.  
``Acceso directo``: acceso a un registro determinado sin que ello implique la consulta de los registros precedentes.

3.3.1. TIPOS DE ORGANIZACIONES FUNDAMENTALES  
``Organización secuencial``: ficheros caracterizados porque los registros que lo forman se escriben o graban sobre el
soporte de almacenamiento en posiciones de memoria físicamente contiguas, sin dejar huecos o espacio libres entre ellos,
el acceso a los datos en este tipo de ficheros es siempre secuencial. Variantes:

* ``Organización secuencial encadenada``: junto a cada registro se almacena un puntero a la dirección del registro
  siguiente. Desventajas:
    * Los ficheros se almacenan secuencialmente según el orden de llegada, sin ninguna secuencia lógica.
* Eliminaciones de registros se efectúan marcando el registro de manera que sea ignorando, aunque siga existiendo, lo
  que deteriora progresivamente el fichero.
* ``Organización secuencial indexada``: la información se gestiona mediante tablas, que contienen las direcciones de los
  datos a los que se puede acceder secuencialmente, formado por tres zonas, denominadas áreas primaria, de índices y de
  excedentes:
    * En el área primaria se encuentran los registros ordenados según el valor de su clave. El acceso a cada registro se
      realiza en una doble operación que consiste en:

1\. Acceder directamente al segmento donde se ubica el registro buscado.  
2\. Una vez localizado, accedemos secuencialmente a los registros contenidos en él.

* El área de índices tiene la misma estructura que un fichero secuencial puto done cada registro contiene dos campos, el
  primer campo contiene la clave del último registro de cada segmento y el segundo campo contiene la dirección de
  entrada a cada uno de los segmentos.
* El área de excedentes alberga todos aquellos registros que no han tenido cabida en el área primaria.

El proceso a seguir para realizar una consulta por clave sin necesidad de leer los registros que le anteceden es:  
1\. Leer secuencialmente las claves en la zona de índices hasta encontrar una mayor o igual a la del registro a
buscar.  
2\. Leer secuencialmente el área primaria a partir de la dirección obtenida hasta encontrar el registro buscado.  
``Ventajas``:  
Especialmente útil cuando se debe combinar consultas a registros concretos y el procesamiento secuencial de todo el
archivo.  
``Desventajas``:  
Imposibilidad de realizar actualizaciones, no permite la inserción de nuevos registros en el área primaria después de la
creación del fichero.

* ``Organización directa o aleatoria``: los registros se sitúan en el fichero y se accede a ellos a través de un
  identificativo o clave que indica la posición del registro dentro del fichero y la posición de memoria donde está
  ubicado. No necesita área de desbordamiento.

Ventajas:

* Cada posición solamente puede ser ocupada por un registro.
* Es muy rápido el acceso a los registros individuales.

Desventajas:

* Gran cantidad de huecos dentro del fichero (desaprovechamiento).
* Para la consulta total de un fichero hay que analizar todas las posiciones de memoria, aunque algunas estén vacías.

3.4. ÍNDICES  
Un índice para un archivo funciona como el catálogo de libros de una biblioteca. Donde si se quiere buscar algún libro
se busca por el índice deseado. De este modo, podremos mirar directamente en ese índice sin necesidad de recorrer
completamente todos los libros de la biblioteca. Tipos básicos de índices:  
``Índices ordenados``: Estos índices están basados en una disposición ordenada de los valores.

* ``Índices primarios``: todos los archivos están ordenados secuencialmente según el campo clave (se denominan archivos
  secuenciales indexados). Estos los empleamos en aquellas aplicaciones que demandan un procesamiento secuencial del
  archivo completo, así como un acceso directo a sus registros.
* ``Índice denso``: en el cual aparece un registro índice para cada valor de la clave búsqueda en el archivo. El
  registro índice contiene el valor de la clave y un puntero al primer registro con ese valor de la clave de búsqueda.
* ``Índice disperso``: solo se crea un registro índice para algunos de los valores. Al igual que en los índices densos,
  cada registro índice contiene un valor de la clave de búsqueda yun puntero al primer registro con ese valor de la
  clave. Para localizar un registro se busca la entrada del índice con el valor más grande que sea menor o igual que el
  valor que se está buscando.

A pesar de ser más rápido localizar un registro si se usa un índice denso, a veces es mejor utilizar el esquema de
índice disperso para utilizar un espacio más reducido y un mantenimiento adicional menor para las inserciones y
borrados.

* ``Índices multinivel``: incluso si se usan índices dispersos, el propio índice podría ser demasiado grande para un
  procesamiento eficiente.

``Índices secundarios``: un índice secundario sobre una clave candidata es como un indice denso primario, excepto que
los registros apuntados apuntados por los sucesivos valores del indice no estan almacenados secuencialmente. En este
esquema, debemos usar un nivel adicional de indireccion para implementar los indices secundarios sobre claves de
busqueda que no sean claves candidatas. Los punteros a estos indices no apuntan directamente al archivo. En vez de eso,
cada puntero apunta a un cajon que contiene punteros al archivo.  
``Índices asociativos`` (hash): Estos índices están basados en una distribución uniforme de los valores a través de una
serie de cajones. El valor asignado a cada cajón está determinado por una función de hashing.

4\. ALGORITMOS

| Complejidad algorítmica: cantidad de recursos que necesita un algoritmo para resolver un problema. |
| :---- |

``Algoritmos de búsqueda``: se emplean para la localización de los datos, existe un conjunto de datos sobre donde nos
interesara realizar una consulta o modificación y debemos obtener la posición. Principales algoritmos de búsqueda:

* ``Secuencial``: recorrer y examinar cada uno de los elementos del array hasta encontrar el elemento buscado.
* ``Binaria o dicotómica``: para utilizar este algoritmo el array debe estar ordenado, la búsqueda consiste en dividir
  el array por su elemento medio en dos subarrays más pequeños y comprar el elemento con el del centro, si coinciden la
  búsqueda termina, si el elemento es menor debe estar en la mitad izquierda, si es mayor en la derecha.
* ``Indirecta``: búsqueda de otro objeto intermedio que mantenga una relación espacial con el objeto buscado,
  demostrando una mayor eficiencia.
* ``Mediante transformación de claves`` (hashing): aumenta la velocidad de búsqueda, no requiere que los elemento estén
  ordenaos, consiste en asignar a cada elemento un índice mediante una transformación del elemento, ser realiza mediante
  una función de conversión llamada hash.

``Algoritmos de ordenación``: Organizar ciertos datos (normalmente arrays o ficheros) mediante una regla prefijada,
puede ser:

* ``Selección``: consiste en buscar el elemento más pequeño del array y ponerlo en primera posición; luego, entre los
  restantes, sed busca el elemento más pequeño y se coloca en segundo lugar y así sucesivamente.
* ``Inserción directa``: sublista ordenada de elementos del array, insertando el resto en el lugar adecuado para que la
  sublista no pierda el orden.
* ``Inserción binaria``: mismo método que la inserción directa, excepto la búsqueda del orden de un elemento en la
  sublista ordenad se realiza mediante una búsqueda binaria.
* ``Shell``: mejora del método de inserción directa, utilizando cuando el array tiene un gran número de elementos. No se
  compra a cada elemento con el de su izquierda, como en el de inserción, sino con el que está un cierto número de
  lugares (llamado salto). Se van dando pasadas hasta que el salto vale 1\.
* ``Burbuja`` (Bubblesort): revisando cada elemento de la lista que va a ser ordenada con el siguiente,
  intercambiándolos de posición si están en el orden equivocado. Es necesario revisar varias veces toda la lista hasta
  que no se necesiten más intercambios. También conocido como método del intercambio directo dado que solo usa
  comparaciones para operar elementos, se lo considera un algoritmo de comparación.
* ``Ordenamiento rápido`` (Quicksort): el algoritmo elije un elemento del conjunto a ordenar al que llama pivote, a
  partir de él resitúa los demás elementos a cada lado del mismo, de manera que a un lado queden lo menores que él y al
  otro los mayores, se repite este proceso de forma recursiva para cada sublista mientras éstas contengan más de un
  elemento. Una vez terminado este proceso todos los elementos estarán ordenados.
* ``Ordenamiento Radix`` (Radix sort): se basa en la clasificación de los datos que queremos ordenar por una clave.
  Dicha clave ha de ser una característica de cada dato que pueda ser descompuesta en elementos más pequeños que
  permitan clasificar los elementos poco a poco (unidades, decenas, centenas...). Para ordenar los elementos tenemos que
  crear un número finito de urnas, de forma que en cada urna los elementos estén relacionados por la clave y que así
  podamos separarlos.

``Algoritmos de compresión``: pueden ser “sin perdida” (procedimiento de codificación que tenga como objetivo
representar cierta cantidad de información utilizando u ocupando un espacio menor, siendo posible una reconstrucción
exacta de los datos originales) o “con perdida” (procedimiento de codificación que tenga como objetivo representar
cierta cantidad de información utilizando una menor cantidad de la misma, siendo imposible una reconstrucción exacta de
los datos originales).

* ``TDC`` (Codificación por transformación): es un tipo de compresión de datos con pérdida para datos "naturales" como
  señales de audio o imágenes fotográficas.
* ``Codificación Huffman``: es un algoritmo usado para compresión de datos sin pérdida. El término se refiere al uso de
  una tabla de códigos de longitud variable para codificar un determinado símbolo (como puede ser un carácter en un
  archivo), donde la tabla ha sido rellenada de una manera específica basándose en la probabilidad estimada de aparición
  de cada posible valor de dicho símbolo.
* ``LZW`` (Lempel-Ziv-Welch): un algoritmo de compresión sin pérdida, se basa en crear sobre la marcha, de manera
  automática y en una única pasada un diccionario de cadenas que se encuentren dentro del texto a comprimir mientras al
  mismo tiempo se procede a su codificación.
* ``RLE`` (Run-length encoding): es una forma muy simple de compresión de datos en la que secuencias de datos con el
  mismo valor consecutivas son almacenadas como un único valor más su recuento.

5\. FORMATOS DE INFORMACIÓN  
``Ficheros con información de texto``: solo contienen ASCII estándar, no presentan problemas de presentación, los más
notables son los ficheros readme, léame... se incluyen los formatos de la web (HTML) que son también texto ASCII.

* ``.pfx`` (Personal Information Exchange): se utiliza en los servidores de Windows para los archivos que contienen
  tanto los archivos de clave pública (sus archivos de certificados SSL) y su clave privada que corresponde a sus
  certificados (generado por el servidor).
* ``.csv`` (comma-separated values): tipo de documento en formato abierto sencillo para representar datos en forma de
  tabla, en las que las columnas se separan por comas y las filas por saltos de línea.

``Texto formateado``: el contenido es principalmente ASCII, pero acompañado de múltiples caracteres específicos de
control de formato y presentación (docx, pdf, xls,...).   
``Ficheros con información de imagen``: ficheros con imágenes estáticas o animadas y formatos para diseño gráfico, dos
formas básicas para almacenar imágenes: ráster y vectorial.

* ``Ráster``: consiste en descomponer la imagen en una serie de puntos y almacenar el color y brillo de cada uno de
  estos puntos, más definición cuanto mayor sea el número de puntos (JPG, PNG, ICO, JNG, MNG...).
    * ``JPEG``: algoritmo de compresión con perdida, flexibilidad a la hora de ajustar el grado de compresión. Convierte
      la imagen desde su modelo de color RGB a otro llamado YCbCr. Puede reducirse la información cromática a la mitad,
      4:2:2 (reducir en un factor de 2 en dirección horizontal), con lo que el color tiene la mitad de resolución (en
      horizontal) y el brillo sigue intacto. Otro método, muy usado, es reducir el color a la cuarta parte, 4:2:0, en el
      que el color se reduce en un factor de 2 en ambas direcciones, horizontal y vertical. Si la imagen de partida
      estaba en escala de grises (blanco y negro), puede eliminarse por completo la información de color, quedando como
      4:0:0.
* ``HSB`` (Hue, Saturation, Brightness – Matiz, Saturación, Brillo).
* ``Resolución``: La resolución de una imagen es el número de píxeles por pulgada que contiene. Ésta se expresa en PPP (
  puntos por pulgada en español) o DPI (dots per inch en inglés).
* ``Profundidad de color``: o bits por píxel (bpp) es un concepto de la computación gráfica que se refiere a la cantidad
  de bits de información necesarios para representar el color de un píxel en una imagen digital.
    * ``PNG``: nivel de compresión que casi no presenta perdidas (predicción del valor de pixel), permite el uso de
      transparencias.
    * ``TIFF``: manejar imágenes y datos en un solo archivo, sin pérdidas.
    * ``GIF``: baja calidad y ofrece una escasa profundidad de colores, permite unir varios cuadros para formar una
      animación.
    * ``EXIF`` (Exchangeable Image File Format): es una especificación para formatos de archivos de imagen usado por las
      cámaras digitales.
    * ``HEIF`` (High Efficiency Image File Format): es un formato de archivo informático para almacenar imágenes y
      secuencias de estas. Realmente es un contenedor flexible de imágenes con compresión, considerado actualmente uno
      de los posibles sustitutos de JPG.
* ``Vectorial``: cada elemento es definido por sus propiedades matemáticas, una línea entre dos puntos puede ser
  definida como una recta, usadas para dibujo de tipo técnico, mapas geográficos (DWG, DWF,...).
    * .swf (Small Web Format): es un formato de archivo de gráficos vectoriales, pueden ser creados por Flash o por
      aplicaciones de software libre. Son ejecutados sobre el navegador mediante el plugin de Flash player.
* SVG (Scalable Vector Graphics): es un lenguaje usado para dibujar y representar gráficos vectoriales escalables,
  imágenes y logotipos, o sea que son gráficos que pueden manipularse con CSS y JavaScript.

``Ficheros con información compuesta``: documentos que integran texto con imágenes o gráficos (PostScript, PDF,...).  
``Ficheros con información comprimida``: se desarrollaron distintos algoritmos de compresión (ZIP, RAR,...).  
``Ficheros de audio``: multitud de “códecs” (MP3, MIDI,...).  
``Ficheros ejecutables``: pueden ser ejecutados directamente en el ordenador, alguno tiene la sola finalidad de
desempaquetar un cierto contenido que vienen incluido en el propio fichero (EXE, COM,...).

| “.ods” extensión del equivalente a Excel en Oracle. |
| :---- |

TEMA 5 – MODELO CONCEPTUAL, REGLAS DE MODELIZACIÓN Y DFD  
1\. DIAGRAMAS DE FLUJO DE DATOS Y LENGUAJES DE BASES DE DATOS  
1.1 DIAGRAMAS DE FLUJO DE DATOS  
Representan gráficamente los límites del sistema y la lógica de los procesos, estableciendo qué funciones hay que
desarrollar. Además, muestra el flujo o movimiento de los datos a través del sistema y sus transformaciones como
resultado de la ejecución de los procesos. El diagrama de flujo de datos se compone de los siguientes elementos:  
``Proceso``: representa una funcionalidad que tiene que llevar a cabo el sistema  
para transformar o manipular datos. El proceso debe ser capaz de generar los  
flujos de datos de salida a partir de los de entrada, más una información  
constante o variable al proceso.  
El proceso nunca es el origen ni el final de los datos, puede transformar un flujo de datos de entrada en varios de
salida y siempre es necesario como intermediario entre una entidad externa y un almacén de datos. Un proceso actualiza o
consulta un almacen, pero nunca controla un almacén.

| Proceso primitivo: es un proceso que no necesita descomposición, solo se detalla su entrada y su salida. |
| :---- |

``Almacén de datos``: representa la información en reposo utilizada por el  
sistema, independientemente del sistema de gestión de datos (un fichero,  
base de datos, archivador...). Contiene la información necesaria para la  
ejecución del proceso.  
El almacén no puede crear, transformar o destruir datos, no puede estar comunicado con otro almacén o entidad externa y
aparecerá por primera vez en aquel nivel en que dos o más procesos accedan a él.  
``Entidad externa``: representa un ente ajeno al sistema que proporciona o  
recibe información del mismo. Puede hacer referencia a departamentos,  
personas, máquinas, recursos u otros sistemas. Puede aparecer varias veces  
en un mismo diagrama, así ́ como en los distintos niveles del DFD para  
mejorar la claridad del diagrama.  
``Flujo de datos``: representa el movimiento de los datos, y establece la comunicación entre los procesos y los
almacenes de datos o las entidades externas. Un flujo de datos entre dos procesos solo es posible cuando la información
es síncrona, es decir, el proceso destino comienza cuando el proceso origen finaliza su función. Los flujos de datos que
comunican procesos con almacenes pueden ser de los tipos:

* ``De consulta``: representan la utilización de los valores de uno o más campos de un almacén o la comprobación de que
  los valores de los campos seleccionados cumplen unos criterios determinados.
* ``De actualización``: representan la alteración de los datos de un almacén como consecuencia de la creación de un
  nuevo elemento, por eliminación o modificación de otros ya existentes.
* ``De diálogo``: es un flujo entre un proceso y un almacén que representa una consulta y una actualización.

Existen sistemas que precisan de información orientada al control de datos y requieren flujos y procesos de control, así
́ como los mecanismos que desencadenan su ejecución. Para que resulte adecuado el análisis de estos sistemas, se ha
ampliado la notación de los diagramas de flujo de datos incorporando los siguientes elementos:  
``Proceso de control``: representa procesos que coordinan y sincronizan las actividades de otros procesos del diagrama
de flujo de datos.  
``Flujo de control``: representa el flujo entre un proceso de control y otro proceso. El flujo de control que sale de un
proceso de control activa al proceso que lo recibe y el que entra le informa de la situación de un proceso. A diferencia
de los flujos tradicionales, que pueden considerarse como procesadores de datos porque reflejan el movimiento y
transformación de los mismos, los flujos de control no representan datos con valores, sino que en cierto modo, se trata
de eventos que activan los procesos (señales o interrupciones).

La descomposición por niveles se realiza de arriba abajo (top-down), es decir, se comienza en el nivel más general y se
termina en el más detallado, pasando por los niveles intermedios necesarios. De este modo se dispondrá́ de un conjunto
de particiones del sistema que facilitaran su estudio y su desarrollo.

La explosión de un proceso de un DFD origina otro DFD y es necesario comprobar que se mantiene la consistencia de
información entre ellos, es decir, que la información de entrada y de salida de un proceso cualquiera se corresponde con
la información de entrada y de salida del diagrama de flujo de datos en el que se descompone, para ello se debe
comprobar:

* No falten flujos de datos de entrada o salida que acompañaban al proceso del nivel superior.
* No aparezca algún flujo que no estuviese ya asociado al proceso de nivel superior.
* Todos los elementos del DFD resultante deben estar conectados directa o indirectamente con los flujos del proceso
  origen.

1.2. NIVELES DE UN DFD  
``Nivel 0`` “diagrama de contexto”: se caracterizan todas las interacciones que realiza un sistema con su entorno (
entidades externas), estas pueden ser otros sistemas, sectores internos a la organización, o factores externos a la
misma. Se dibuja un solo proceso que representa al sistema en cuestión y se escribe su nombre en dicha burbuja como un
sustantivo común más adjetivos. De él solamente parten los flujos de datos que denotan las interrelaciones entre el
sistema y sus agentes externos, no admitiéndose otros procesos ni almacenamientos en el dibujo, ya que estos son
procesos estructurados y ordenados,además posee una cardinalidad que varía según la función que desempeñe cada
diagrama.  
``Nivel 1`` “diagrama de nivel superior”: se plasman todos los procesos que describen al proceso principal. En este
nivel los procesos no suelen interrelacionarse directamente, sino que entre ellos debe existir algún almacenamiento o
entidad externa que los una. Esta regla de construcción sirve como ayuda al analista para contemplar que en un nivel tan
elevado de abstracción es altamente probable que la información que se maneja requiera ser almacenada en el sistema.  
``Nivel 2`` “diagrama de detalle o expansión”: comienzan a explotarse las excepciones a los caminos principales de la
información dado que aumenta progresivamente el nivel de detalle. De aquí en adelante se permiten los flujos entre
procesos. Puede considerarse el máximo para ser validado en forma conjunta con el usuario dado que en los niveles
posteriores el alto grado de complejidad del diagrama.

1.2. DISEÑO DE UNA BASE DE DATOS / DISEÑO DE UN SGBD  
``Diseño de una base de datos``:  
``Conceptual``: se confecciona a partir de la especificación de requerimientos y su resultado es el esquema conceptual
de la base de datos (una descripción de alto nivel de la estructura de la base de datos, independiente del software que
se use para manipularla).  
``Lógico``: se confecciona a partir del diseño conceptual y da como resultado una descripción de la estructura de la
base de datos que puede procesar el software DBMS.  
``Físico``: se confecciona a partir del esquema lógico y da como resultado una descripción de la implementación de una
base de datos en la memoria secundaria, describe la estructura de almacenamiento y los métodos usados para tener un
acceso efectivo a los datos.

``Diseño de un Sistema Gestor de Bases de Datos`` (el objetivo de la arquitectura de tres niveles es separar la vista de
los usuarios, y así ocultar la complejidad de la base en tres niveles):  
``Nivel interno`` (Almacenamiento Físico): implica la forma en que la base de datos se representa físicamente en el
sistema informático. En él se describe cómo los datos se almacenan en la base de datos y en el hardware del equipo.  
``Nivel conceptual``: forma de describir los datos que se almacenan dentro de la base de datos y cómo los datos están
relacionados entre sí. Describe la estructura de todos los usuarios y es independiente de hardware y software.  
``Nivel externo`` (Vistas de usuario): describe una parte de la base de datos que es relevante para un usuario en
particular. Excluye datos irrelevantes, así como los datos que el usuario no está autorizado a acceder.

2\. MODELO ENTIDAD/RELACIÓN  
Es una herramienta para el modelo de datos, la cual facilita la representación de entidades de una base de datos y las
relaciones entre ellas. Se suele desarrollar en dos fases:  
1\. Se elabora el diagrama entidad/relación.  
2\. Se completa el modelo con listas de atributos y una descripción de otras restricciones que no se pueden reflejar en
el diagrama.

El modelo está basado en una colección de objetos básicos (llamados entidades), de relaciones entre esos objetos y de
atributos los mismos.  
``Entidad``: representa un “objeto” del mundo real con existencia independiente, es decir, se diferencia únicamente de
otro objeto o cosa, incluso siendo del mismo tipo o una misma entidad (Ejemplo: una persona se diferencia de cualquier
otra persona, incluso siendo gemelos). Todos los valores que toman los atributos de la entidad deben tener las mismas
propiedades. Existen dos clases de entidades:

* ``Fuertes``: tienen existencia por sí mismos.
* ``Débiles``: su existencia depende de otro tipo de entidad, si desaparece la entidad de la que dependen, también
  desaparece la entidad débil.

``Relación``: asociación entre entidades de la misma naturaleza (Ejemplo: dados los conjuntos de entidades "Habitación"
y "Huésped", todas las relaciones de la forma habitación-huésped, permiten obtener la información de los huéspedes y sus
respectivas habitaciones, es decir, participan en el conjunto). Las relaciones se caracterizan por tres propiedades:

* ``Grado``: número de entidades participantes en la relación. (Si relacionan una entidad consigo misma se llaman
  reflexivas).
* ``Cardinalidad``: número de entidades con la cual otra entidad puede asociar mediante una relación binaria, pueden ser
  de tres tipos: 1-1, 1-N y N-N.
* Se dice que una ``relación`` es ``exclusiva`` cuando la existencia de una relación entre dos tipos de entidades
  implica la no existencia de las otras relaciones.

``Atributos``: unidad básica de información, características que definen o identifican a una entidad, cada entidad tiene
valores específicos asignados para cada uno de sus atributos, de esta forma, es posible su identificación unívoca. (
Ejemplo: a la colección de entidades “alumnos”, con el siguiente conjunto de atributos en común, (id, nombre, edad,
semestre), pertenecen las entidades:

* (1, Ana, 15 años, 2), (2, María, 19 años, 5), ...

Los atributos identificativos permiten diferenciar a una instancia de la entidad de otra distinta (en el ejemplo, el ID
de cada alumno). Para cada atributo, existe un dominio del mismo, este hace referencia al tipo de datos que será
almacenado a restricciones en los valores que el atributo puede tomar. ``Tipos`` de atributos:

* ``Univaluados``: distingue de manera única una ocurrencia de entidad del resto de ocurrencias de entidad (su nombre
  aparece subrayado).
* ``Multivaluados``: pueden tomar más de un valor.
* ``Compuestos``: su valor se puede calcular a partir de valores de atributos relacionados y a su vez puede
  descomponerse en varios atributos.

3\. MODELO RELACIONAL  
Un SBDRelacional se caracteriza por presentar sus datos siguiendo las Reglas de Codd:  
``Regla 0`` (fundación): Cualquier sistema que se proclame como relacional, debe ser capaz de gestionar sus bases de
datos enteramente mediante sus capacidades relacionales.  
``Regla 1`` (información): la información en la base de datos es representada  
unidireccionalmente por valores en posiciones de las columnas dentro de filas de tablas. Toda la información en una base
de datos relacional se representa explícitamente en el nivel lógico exactamente de una manera: con valores en tablas.  
``Regla 2`` (acceso garantizado): Todos los datos deben ser accesibles sin ambigüedad. Cada valor escalar individual en
la base de datos debe ser lógicamente direccionable  
especificando el nombre de la tabla, la columna que lo contiene y la clave primaria.  
``Regla 3`` (tratamiento sistematico de valores nulos): el SGBD debe permitir que haya campos nulos. Debe tener una
representación de la «información que falta y de la información inaplicable» que sea sistemática y distinta de todos los
valores regulares.  
``Regla 4`` (catálogo dinámico): El sistema debe soportar un catálogo en línea, el catálogo relacional, que da acceso a
la estructura de la base de datos y que debe ser accesible a los usuarios autorizados. El catálogo de sistema es una
colección de tablas especiales en una base de datos que son propiedad, están creadas y son mantenidas por el propio
DBMS. Estas tablas del sistema contienen datos que describen la estructura de la base de datos.  
``Regla 5`` (sublenguaje global de datos): El sistema debe soportar por lo menos un lenguaje relacional que tenga una
sintaxis lineal, pueda ser utilizado de manera interactiva y tenga soporte de operaciones de definición de datos,
operaciones de manipulación de datos (actualización así como la recuperación), de control de la seguridad e integridad y
operaciones de administración de transacciones.  
``Regla 6`` (actualización de vistas): Todas las vistas que son teóricamente actualizables deben poder ser actualizadas
por el sistema.  
``Regla 7`` (alto nivel de inserción, actualización y borrado): los datos no solo se pueden recuperar de una base de
datos relacional a partir de filas múltiples y/o de tablas múltiples,sino que también pueden realizarse inserciones,
actualizaciones y borrados sobre varias tuplas y/o tablas al mismo tiempo y no solo sobre registros individuales.  
``Regla 8`` (independencia física de los datos): Los programas de aplicación y actividades del terminal permanecen
inalterados a nivel lógico aunque se realicen cambios en las representaciones de almacenamiento o métodos de acceso.  
``Regla 9`` (independencia lógica de los datos): Los programas de aplicación, actividades del terminal y vistas,
permanecen inalterados a nivel lógico aunque se realicen cambios a las tablas base que preserven la información.  
``Regla 10`` (independencia de la integridad): Las reglas de integridad\* se deben especificar por separado de los
programas de aplicación y almacenarse en la base de datos. Debe ser posible cambiar esas restricciones sin afectar
innecesariamente a las aplicaciones existentes.  
``Regla 11`` (independencia de la distribución): La distribución de porciones de base de datos en distintas
localizaciones debe ser transparente para los usuarios de la base de datos.  
``Regla 12`` (no subversión): Si el sistema proporciona una interfaz de bajo nivel de registro, aparte de una interfaz
relacional, esa interfaz de bajo nivel no debe permitir su utilización para subvertir el sistema. Por ejemplo para
sortear las reglas de seguridad relacional o las restricciones de integridad (no puede tener backdoors).

3.1 CONCEPTOS DEL MODELO RELACIONAL  
``Relación``: en una BDR, todos los datos se almacenan y se accede a ellos por medio de relaciones previamente
establecidas, las relaciones que almacenan datos son llamadas relaciones base y su implementación es llamada "tabla",
para que una tabla sea considerada como una relación tiene que cumplir con algunas restricciones:

* Cada tabla debe tener un solo tipo de filas.
* Todos los datos en una columna deben ser del mismo tipo (dominio).
* Nunca habrá valores multivaluados (el valor individual de la intersección de una fila y una columna será único).

``Dominio``: describe un conjunto de posibles valores para cierto atributo.  
``Atributo``: es una etiqueta de una relación (tabla), deben estar explícitamente relacionados con un nombre en todas
las operaciones.  
``Grado``: número de atributos de una relación.  
``Cardinalidad``: número de tuplas (filas) de la relación.

3.2. REGLAS DE INTEGRIDAD  
La extensión de las relaciones (es decir, las tuplas que contienen las relaciones) deben tener valores que reflejen la
realidad correctamente (en la relación de esquema EMPLEADOS(DNI, nombre, apellido, sueldo), una tupla que tiene un valor
de –1.000 para el sueldo probablemente no tiene sentido, porque los sueldos no pueden ser negativos). En general, las
condiciones que garantizan la integridad de los datos pueden ser de dos tipos:  
``Restricciones de integridad de usuario``: condiciones específicas de una base de datos concreta; es decir, son las que
se deben cumplir en una base de datos particular con unos usuarios concretos, pero que no son necesariamente relevantes
en otra base de datos.  
``Reglas de integridad de modelo``: son condiciones más generales, propias de un modelo de datos, y se deben cumplir en
toda base de datos que siga dicho modelo.

* ``Regla de integridad de unicidad de la clave primaria``: establece que toda clave primaria que se elija para una
  relación no debe tener valores repetidos.
* ``Regla de integridad de entidad de la clave primaria``: dispone que los atributos de la clave primaria de una
  relación no pueden tener valores nulos.
* ``Regla de integridad referencial``: está relacionada con el concepto de clave foránea. Concretamente, determina que
  todos los valores que toma una clave foránea deben ser valores nulos o valores que existen en la clave primaria que
  referencia.
* ``Regla de integridad de dominio``: implica que todos los valores no nulos que contiene la base de datos para un
  determinado atributo deben ser del dominio declarado para dicho atributo (enteros, string,...).

Asociado al concepto de integridad, se define el concepto de clave:  
Clasificación de Claves: cada relación puede tener uno o más campos cuyos valores identifican de forma única cada
registro de dicha tabla, es decir, no pueden existir dos o más registros diferentes cuyos valores en dichos campos sean
idénticos. Este conjunto de campos se llama clave única. Pueden existir varias claves únicas en una determinada tabla, y
a cada una de estas suele llamársele candidata a clave primaria.

* ``Clave primaria``: una clave primaria es una clave única (puede estar conformada por uno o más campos de la tabla)
  elegida entre todas las candidatas que define unívocamente a todos los demás atributos de la tabla para especificar
  los datos que serán relacionados con las demás tablas. La forma de hacer esto (relación entre tablas) es por medio de
  claves foráneas.
* ``Clave externa o foránea``: una clave foránea es una referencia a una clave en otra tabla, determina la relación
  existente en dos tablas. Las claves foráneas no necesitan ser claves únicas en la tabla donde están (por lo que una de
  ellas puede ser nula) y sí a donde están referenciadas. Por ejemplo, el código de departamento puede ser una clave
  foránea en la tabla de empleados. Se permite que haya varios empleados en un mismo departamento, pero habrá uno y solo
  un departamento por cada clave distinta de departamento en la tabla de departamentos.
* ``Clave índice``: las claves índice surgen con la necesidad de tener un acceso más rápido a los datos. Los índices
  pueden ser creados con cualquier combinación de campos de una tabla. Las consultas que filtran registros por medio de
  estos campos, pueden encontrar los registros de forma no secuencial usando la clave índice. Las bases de datos
  relacionales incluyen múltiples técnicas de ordenamiento, cada una de ellas es óptima para cierta distribución de
  datos y tamaño de la relación.

Los índices generalmente no se consideran parte de la base de datos, pues son un detalle agregado. Sin embargo, las
claves índices son desarrolladas por el mismo grupo de programadores que las otras partes de la base de datos.

4\. MODELO ORIENTADO A OBJETOS  
``Características del modelo de programación orientado a objetos``:  
``Abstracción``: consiste en aislar un elemento en su contexto de sus elementos que lo acompañan.  
``Encapsulamiento``: poder separar la interfaz de una clase de su implementación o dicho en otras palabras no es
necesario conocer los detalles de cómo están implementados las propiedades para poder utilizarlas.  
``Herencia``: es una propiedad que permite que los objetos sean creados a partir de otros ya existentes, obteniendo
características (métodos y atributos) similares a los ya existentes.  
``Polimorfismo``: hace referencia a un conjunto de métodos con el mismo nombre e igual número de parámetros y tipos,
pero que se encuentran definidos en diferentes clases.  
``Sobrecarga``: capacidad de un lenguaje de programación, que permite definir dos o más métodos con el mismo nombre pero
parámetros diferentes en cantidad y/o tipo.  
``Modularidad``: una opción importante para la escalabilidad y comprensión de programas, además de ahorrar trabajo y
tiempo en el desarrollo.  
``Relación``: una relación o vínculo entre dos o más entidades describe alguna interacción entre las mismas.

4\. NORMALIZACIÓN  
La ``normalización`` de bases de datos es un proceso que consiste en aplicar una serie de reglas a las relaciones (
tablas) obtenidas tras el paso del modelo entidad-relación al modelo relacional. Con objeto de minimizar la redundancia
de datos, facilitando su gestión posterior para:

* Minimizar la redundancia de los datos.
* Disminuir problemas de actualización de los datos en las tablas.
* Proteger la integridad de datos.

El proceso de normalización se basa en relaciones de dependencia entre los datos:  
``Dependencia funcional reflexiva``: a partir de cualquier atributo o conjunto de atributos siempre puede deducirse él
mismo (A-\>B). Si la dirección o el nombre de una persona están incluidos en el DNI, entonces con el DNI podemos
determinar la dirección o su nombre.  
``Dependencia funcional aumentativa/completa``: si A-\>B, entonces AC-\>BC (si con el DNI se determina el nombre de una
persona, entonces con el DNI más la dirección también se determina el nombre y su dirección).  
``Dependencia funcional transitiva``: si A-\>B-\>C, entonces A-\>C (entonces entendemos que FechaDeNacimiento determina
a Edad y la Edad determina a Conducir, indirectamente podemos saber a través de FechaDeNacimiento a Conducir).

4.1. FORMAS NORMALES  
``1FN``: una entidad está en 1FN si no tiene grupos repetitivos, es decir, un atributo solo puede tomar un único valor
de un domino simple. Debe cumplir:

* No hay orden de arriba a abajo en las filas.
* No hay orden de izquierda a derecha en las columnas.
* No hay filas duplicadas.
* Cada intersección de fila y columna contiene exactamente un valor del dominio aplicable (y nada más).
* Todas las columnas son regulares, es decir, las filas no tienen componentes como IDs de fila, IDs de objeto, o
  timestamps ocultos.

``2FN``: una entidad está en 2FN si está en 1FN y todos los atributos que no forman parte de las claves candidatas
tienen dependencia funcional completa respecto de estas, es decir, una tabla 1NF está en 2NF si y solo si, dada una
clave primaria y cualquier atributo que no sea un constituyente de la clave primaria, el atributo no clave depende de
toda la clave.  
``3FN``: una entidad está en 3FN si está en 2FN y todos sus atributos no principales depende directamente de la clave
primaria, es decir, no hay dependencias funcionales transitivas de atributos no principales respecto de las claves.

* ``FN Boyce-Codd``: es una versión de la 3FN, está en FNBC si solo existen dependencias funcionales elementales que
  dependan de la clave primaria o de cualquier alternativa, es decir, si la clave primaria está formada por un atributo
  y ya está en 3FN, también estará en FNBC.

``4FN``: una entidad está en 4FN, si está en 3FN y no tiene dependencias funcionales  
multivaluadas no triviales.  
``5FN``: una entidad está en 5FN, si está en 4NF y cada dependencia de unión (join) en ella es implicada por las claves
candidatas.

5\. TRANSFORMACION DEL MODELO E/R A RELACIONAL

| ELEMENTO DEL MODELO E/R | TRANSFORMACIÓN AL MODELO RELACIONAL |
| :---- | :---- |
| Entidad | Relación (Tabla). |
| Entidad débil | Relación (Tabla) que tiene todos los atributos de la entidad débil y los de la clave primaria de la entidad propietaria en el modelo E/R. La clave primaria está formada por los atributos de la cave primara de la entidad propietaria en el modelo E/R más los atributos de la clave parcial de la entidad débil. |
| Relación 1:1 | Clave foránea. |
| Relación 1:N | Clave foránea en el lado de N |
| Relación N:M | Relación (Tabla), los atributos de la relación serán las claves primarias de las entidades más los atributos del propio vinculo. La clave primaria de la relación será el conjunto de los atributos que sean claves primarias de las entidades relacionadas. |
| Relación recursiva | Si es binaria (1:1 o 1:N) será una clave foránea. Si es n-aria se crea una relación (tabla). |
| Clave candidata | Una clave principal más el resto de claves candidatas. |
| Atributos simples | Atributos. |
| Atributos compuestos | Se divide en varios atributos simples, uno por cada atributo que lo forma. |
| Atributos derivados | No se representan. |
| Atributos multivaluados | Para cada atributo multivaluado se crea una relación (tabla). Los atributos de la relación serán la clave primaria de la entidad a la que pertenece el atributo multivaluado más los atributos correspondientes al atributo multivaluado. La clave primaria de la relación será la clave primaria de la entidad más los atributos correspondientes al atributo multivaluado. |

TEMA 6 \- DFD, MODELO E/R Y SGBD (RELACIONALES, OBJETOS Y NOSQL)  
1\. GESTIÓN DE BASES DE DATOS  
Una base de datos es una colección de datos relacionados que pueden registrarse y que tienen un significado implícito (
nombres, números de teléfono, direcciones...). Tiene una fuente de la cual provienen los datos, grado de interacción con
los sucesos del mundo real, y audiencia que esta activamente interesada en el contenido, puede tener cualquier tamaño y
complejidad, puede crearse y mantenerse bien mediante un conjunto de programas de aplicación diseñados específicamente
para dicha tarea o bien mediante un sistema de gestión de base de datos.

1.1 DBMS (DataBase Management System)  
Es una colección de programas que permiten a los usuarios crear y mantener una base de datos, es un software de
propósito general que facilita los procesos de definición, construcción y manipulación de bases de datos. El enfoque de
bases de datos, la estructura y organización detallada de cada fichero se almacena en el catálogo, y el DMBS extrae del
catálogo los detalles de la organización cuando estos son requeridos por el software DBMS.

La característica que permite la independencia de programas-datos y de programas-operaciones se llama abstracción de
datos, un DBMS ofrece a los usuario una representación conceptual de los datos, un modelo de datos es un tipo de
abstracción de datos que se utiliza para proporcionar esta representación conceptual, el modelo de datos utiliza
conceptos lógicos como las propiedades e interrelaciones de objetos, el modelo de datos oculta los detalles de
almacenamiento e implementación que no interesan a la mayoría de usuario de la base de datos. El objetivo de esta
abstracción es separar las aplicaciones del usuario y la base de datos física:  
``Nivel interno``: esquema interno que describe la estructura física de almacenamiento de la base de datos, emplea un
modelo de datos físico y describe todos los detalles para su almacenamiento, así como los camios de acceso para la base
de datos.  
``Nivel conceptual``: esquema conceptual que describe la estructura de datos completa para una comunidad de usuarios,
oculta los detalles de las estructuras físicas de almacenamiento y se concentra en describir detalles entidades, tipos
de datos, vínculos, operaciones de los usuarios y restricciones.  
``Nivel externo``: “de visitas”, varios esquemas externos o vistas de usuario. Cada esquema externo describe la parte de
la base de datos que interesa a un grupo de usuarios y oculta a ese grupo el resto de la base de datos, modelo de datos
de alto nivel o uno de implementación.

Los tres esquemas no son más que descripciones de los datos, que existen realmente y están en el nivel físico, el DBMS
debe transformar una solicitud expresada en términos de un esquema externo en una solicitud expresada en términos del
esquema conceptual y luego en una solicitud en el esquema interno. El proceso de trasformar solicitudes y resultados de
un nivel a otros denomina correspondencia o transformación (mapping).

1.2. COMPARTIMIENTO DE DATOS Y PROCESAMIENTO DE TRANSACCIONES MULTIUSUARIOS   
Todo DBMS debe permitir a varios usuarios tener acceso simultaneo a la base de datos, el DBMS debe incluir software de
control de concurrencia para asegurar que cuando varios usuarios intenten actualizar los mismos datos lo hagan de manera
controlada, los DBMS deben asegurar que todas las transacciones que se hagan sobre los datos, una vez finalizadas,
tengan (ACID):  
``Atomicity``: asegurar que la transacción realizada este completa sin que exista la posibilidad de que haya quedado a
media debido al algún fallo.  
``Consistency``: si la base de datos estaba en un estado correcto antes del inicio de la transacción debe acabar la
transacción en un estado correcto.  
``Isolation``: si se están ejecutando varias transacciones simultáneamente, el sistema debe asegurar que se realizan de
manera independiente unas de otras.  
``Durability``: terminada la transacción, se debe asegurar que los resultados quedan registrados en la base de datos.

1.3. CARACTERÍSTICAS Y COMPONENTES  
Los actuales paquetes de DBMS tienen un diseño modular, arquitectura cliente-servidor, en una arquitectura
cliente-servidor básica la funcionalidad del sistema se distribuye entre dos tipos de módulos, el módulo cliente se
suele ejecutar sobre una estación de trabajo del usuario, el módulo servidor maneja el almacenamiento, acceso, búsqueda
de datos y otras funciones. La capacidad para modificar el esquema en un nivel del sistema de base de datos sin tener
que modificar el esquema del nivel inmediato superior se denomina:  
``Independencia lógica``: capacidad de modificar el esquema conceptual sin tener que alterar los esquemas externos ni
los programas de aplicación. Podemos modificar el esquema conceptual para ampliar la base de datos o para reducir la
base de datos, la modificación no deberá afectar a los esquemas externos que solo se refiera a los datos restantes. Si
el DBMS se cuenta con independencia lógica de datos, solo será preciso modificar la definición de la vista y las
correspondencias.  
``Independencia física``: es la capacidad de modificar el esquema interno sin tener que alterar el esquema conceptual (o
los externos). Si la base de datos aun contiene los mismos datos, no será necesario modificar el esquema conceptual.  
Todo DBMS incluye información sobre como establecer la correspondencia entre las solicitudes y los datos entre los
diversos niveles, el DBMS utiliza software adiciónales para realizar correspondencias haciendo referencia a la
información de correspondencia que se encuentra en el catálogo.

1.4. LENGUAJES E INTERFACES DE BASES DE DATOS  
Una vez que se ha completado el diseño de una base de datos y se ha elegido un DBMS para su implementación, el primer
paso será especificar los esquemas conceptual e interno de la base de datos y cualquier correspondencia existente entre
ambos:  
``Leguaje de definición de datos`` (LDD): El DBMS contará con un compilador de LDD cuya función será procesar las
sentencias para identificar las descripciones de los elementos de los esquemas y almacenar la descripción del esquema en
el catálogo del DMBS, también sirve para definir ambos esquemas en DBMS donde no se separen claramente los niveles.  
``Lenguaje de definición de almacenamiento`` (LDA): En sistemas que separan claramente los niveles para especificar el
esquema interno se utiliza este lenguaje.  
``Lenguaje de definición de vistas`` (LDV): sirve para especificar las vistas del usuario y sus correspondencias con el
esquema conceptual.  
``Lenguaje de manipulación de datos`` (LMD): los usuarios requerirán algún mecanismo para manipularla, las operaciones
de manipulación más comunes son la recuperación, la inserción, la eliminación y la modificación de los datos.

* ``LMD de alto nivel``: se pueden utilizar de manera independiente para especificar operaciones complejas de base de
  datos en forma concisa, como SQL, pueden especificar y recuperar muchos registros con una sola instrucción de LMD,
  suelen especificar qué datos hay que obtener y no como obtenerlos, se denominan también declarativos.
* ``LMD de bajo nivel``: deben estar embebidos en un lenguaje de programación de propósito general, recupera registros u
  objetos individuales de la base de datos y los procesa por separado, necesita utilizar elementos de lenguajes de
  programación, como los bucles, para recuperar y procesar cada registro individual de un conjunto de registros.

``Lenguaje de datos relacionales SQL``: en los actuales DBMS se utiliza un amplio lenguaje integrado que cuenta con
elementos para definir esquemas conceptuales, definir vistas, manipular datos y definir su almacenamiento, representa
una combinación de LDD, LDV y LMD, así como sentencias para especificación de restricciones y evolución del esquema.

1.5 HERRAMIENTAS  
``CASE`` (Computer Aided Software Engineering): aplicaciones informáticas o programas informáticos destinadas a aumentar
el balance en el desarrollo de software reduciendo el costo de las mismas en términos de tiempo y de dinero.  
``Powerbuilder``: entorno para desarrollar aplicaciones de gestión de bases de datos. Puede trabajar con las bases de
datos más utilizadas (Oracle, MySQL, MS SQL Server...). Además, dispone de un lenguaje propio que permite programar en
la propia BD llamado Powerscript.

2\. CLASIFICACIÓN DE LOS SISTEMAS DE GESTION DE BASE DE DATOS  
Toda base de datos soportada por un SGBD debe tener unos esquemas modelados adecuadamente. Coincidiendo con la evolución
histórica de las bases de datos, estas han utilizado distintos modelos. Los SGBD esperan un modelo determinado para
poder acceder de forma simple a la base de datos. Estos modelos son:  
``Jerárquicos``: usada en los SGBD de los primeros mainframes. Las relaciones entre registros forman una estructura en
árbol. Esta estructura es simple e inflexible, permite representar relaciones “padre/hijo” donde cada padre puede tener
varios hijos, pero cada hijo ha de venir de solo un padre (las conocidas como relaciones 1:N).  
``En red``: contiene relaciones más complejas que las jerárquicas. Admite relaciones de cada registro con varios que se
pueden seguir por distintos caminos. En otras palabras, el modelo permite relaciones N:N. Está concebido como un modo
flexible de representar objetos y sus relaciones.  
``Relacionales``: cumple con el modelo relacional, es la más extendida hoy en día. Se usa en mainframes, computadoras
medias y microcomputadoras. Almacena los datos en filas (tuplas) y columnas (atributos). Estas tablas pueden estar
conectadas entre sí por claves comunes. Todos los sistemas de bases de datos relacionales utilizan SQL (Structured Query
Language) para consultar y mantener la base de datos. Características comunes:

* Se compone de varias tablas, denominadas relaciones.
* La relación entre una tabla padre y un hijo se lleva a cabo por medio de las llaves primarias y llaves foráneas (o
  ajenas).
* Las llaves primarias son la clave principal de un registro dentro de una tabla y estas deben cumplir con la integridad
  de datos.
* Las llaves ajenas se colocan en la tabla hija, contienen el mismo valor que la llaveprimaria del registro padre; por
  medio de estas se hacen las formas relacionales.

Ejemplos de bases de datos relacionales: SQL Server, Oracle, Ingres, MySQL, MariaDB (evolución de MySQL), PostgreSQL,
DB2, Heidi, SQLite, Firebird...  
``Orientado a Objetos``: diseñada siguiendo el paradigma de los lenguajes orientados a objetos. De este modo soporta los
tipos de datos gráficos, imágenes, voz y texto de manera natural. Un Sistema de Gestión de Bases de Datos Orientado a
Objetos debe cumplir las siguientes características:

* ``Persistencia``: los datos deben mantenerse después de que la aplicación que los creo haya finalizado el proceso que
  los creó.
* ``Concurrencia``: debe controlar la interacción entre las transacciones concurrentes para evitar que se destruya la
  consistencia.
* ``Recuperación``: proveer mecanismos de recuperación de la información como mínimo al nivel de los SGBD relacionales.
* ``Independencia lógica y física``: debe evitar que los programadores tengan que escribir programa para mantener
  índices y asignar almacenamiento en disco.
* ``Identidad del objeto``: los objetos deben tener un identificador independiente de los valores de sus atributos.
* ``Soporta objetos complejos``: debe ser posible construir objetos complejos aplicando constructores a objetos básicos.
* ``Encapsulamiento``: los programadores solo tienen acceso a la especificación de interfaz de los métodos, los datos de
  implementación de estos métodos están ocultos en los objetos.
* ``Tipos o clases``: esquema de una BDOO contiene un conjunto de clases o tipos y deben ser capaz de heredar de sus
  supertipos o superclases los atributos y métodos (estos soportan sobrecarga ,es decir, deben poder aplicarse a
  diferentes tipos).
    * ``Clase``: es una plantilla para la creación de objetos de datos según un modelo predefinido. Las clases se
      utilizan para representar entidades o conceptos, como los sustantivos en el lenguaje. Cada clase es un modelo que
      define un conjunto de variables y métodos apropiados para operar con dichos datos. Cada objeto creado a partir de
      la clase se denomina instancia de la clase.
* ``Superclases y subclases``: las clases pueden derivar desde otras clases. La clase derivada (la clase que proviene de
  otra clase) se llama subclase. La clase de la que está derivada se denomina superclase.
* ``Clase abstracta``: funcionan como una clase que declara la existencia de métodos pero no su implementación. No puede
  tener métodos privados, y uno de sus métodos debe ser abstracto, pero no todos.
* ``Métodos``: procedimientos y funciones que se invocan para actuar sobre los objetos y especifican cómo se ejecuta un
  mensaje. Los campos y métodos de una clase pueden definirse de tipo public, protected y private, por defecto son
  públicos.
* ``Interfaces``: definen un comportamiento, son clases completamente abstractas que contiene sólo una colección de
  métodos abstractos y propiedades constantes. Si se desea utilizar un método que no ha implementado el usuario se
  utiliza una interfaz.

``Lenguajes de datos``:  
``ODL`` (Object Description Language): es empleado para facilitar la portabilidad de los esquemas de las bases de datos,
no es un lenguaje de programación completo, define las propiedades y lo prototipo de las operaciones de los tipos, pero
no los métodos que implementan esas operaciones, intentan definir tipos que puedan implementarse en diversos lenguajes,
no está ligado a la sintaxis concreta de un lenguaje de programación particular, es una extensión de IDL (Interface
Definition Languaje).  
``OML`` (Object Manipulation Language): es empleado para la elaboración de  
programas que permitan crear, modificar y borrar datos que constituyen la base de datos.  
``OQL`` (Object Query Language): es el equivalente a SQL, presenta las siguientes  
características:

* Las consultas pueden invocar métodos: los métodos escritos en cualquier lenguaje de programación pueden incluir
  consultas.
* Sintaxis abstracta.
* Semántica formal puede definirse fácilmente.
* Acceso declarativo a los objetos.
* Sintaxis concreta al estilo SQL.
* No proporciona operadores explícitos para la modificación.
* Proporciona primitivas de alto nivel para tratar con conjuntos de objetos

| Ventajas de las BDOO: Flexibilidad y soporte para el manejo de tipos de datos complejos. Puede ajustarse a userbase siempre el espacio sea los campos son necesarios: eliminando espacio desperdiciado en registros con campos que nunca se usan. Rendimiento: permiten que los objetos hagan referencia directamente a otro mediante apuntadores, colocando cerca las estructuras relacionadas entre sí en el espacio de almacenamiento en disco, lo que hace que pasen más rápido del objeto A al objeto B que las Bases de Datos Relacionales, las cuales deben usar comandos “JOIN” para logar esto. Desventajas: No están tan avanzadas como la relacionales: no tienen la abundancia de herramientas, fiabilidad de administración y rendimiento de estas últimas. Son incompatibles entre sí mismas: esto hace imposible migrar una aplicación desde una base de datos orientada a objetos a otra (obliga a depender de un único proveedor). Falta de estándares en la industria orientada a objetos. |
| :---- |

Ejemplos de bases de datos orientadas a objetos: ObjectDB, Zope, DB40, Gemstone...

``NoSQL``: surgen por problemas debidos a la cantidad masiva de información (Big Data) que supone la generalización de
internet, que experimentan los DBMS tradicionales: lentitud de accesos, problemas de bloqueos, dificultad para mantener
bases de datos distribuidas geográficamente. Los datos almacenados no requieren estructuras fijas como tablas,
normalmente no soportan operaciones JOIN, ni garantizan completamente ACID y habitualmente escalan bien
horizontalmente.   
A menudo, las bases de datos NoSQL se clasifican según su forma de almacenar los datos:

* ``Clave-valor``: funcionan con una clave indexada asociada a un valor, que desde el punto de vista de la base de datos
  es información opaca (asociada a la clave) que simplemente almacena y recupera. Están diseñadas para escalar
  masivamente manteniendo un tiempo de respuesta muy rápido y disponibilidad total. Se suelen usar para almacenar
  información de sesión, preferencias o perfiles de usuario, carritos de la compra y en general como cachés de cualquier
  conjunto de información que se pueda recuperar por una clave. Ejemplos: Cassandra, DynamoDB, Redis, Riak o Aerospike
* ``Orientadas a documentos``: el concepto principal es el de documento, mayoritariamente en formato JSON para almacenar
  y consultar información, cada base de datos puede utilizar distintas codificaciones para los documentos, el
  direccionamiento de los documentos se realizará a través de una clave que identificará de forma única al mismo.
  Permiten gestionar información con complejas estructuras jerárquicas, y ofrecen índices secundarios y completos
  lenguajes de consulta y agregación de datos. Ejemplos: MongoDB (puerto 27017), CouchDB o CouchBase
* ``Orientadas a grafos``: la información se almacena en los nodos de un grafo (entidades), representando las relaciones
  mediante las aristas. Tanto las entidades (nodos del grado), como las relaciones (aristas) pueden además tener
  atributos. Recorrer las uniones entre entidades a través de estas relaciones es el fuerte de las bases de datos
  orientadas a grafos, y permiten hacerlo con gran velocidad, independientemente del volumen de datos (caso de uso más
  conocido de este tipo de bases de datos son las redes sociales). Ejemplos: Neo4j (cypher: lenguaje de consulta para BD
  Neo4j), OrientDB o Titan
* ``Orientadas a columnas``: similares a una tabla en las bases de datos relacionales, se definen familias de columnas
  antes de cargar los datos, la estructura de estos datos debe ser conocida con anterioridad. Organizan los datos de una
  forma distinta al modelo relacional, los datos están organizados penando en operaciones de columna para ejecutar
  operaciones de agregación o realizar búsquedas de registro a través de múltiples columnas, cada registro no requiere
  un único valor por columna, en su lugar, se pueden modelar familias de columnas. No requiere que los campos siempre
  estén presentes, aunque almacene valores nulos, si es información que no existe, no se incluye. Ejemplos: Hbase.

| Las bases de datos NoSQL no cumplen el modelo ACID, en su caso, se cumple el modelo BASE, un enfoque similar pero perdiendo la consistencia y el aislamiento a favor de la disponibilidad la degradación y el rendimiento: Basic Availability: sistema funciona incluso cuando alguna parte falla debido a que el almacenamiento sigue los principios de distribución y replicación. Soft State: los nodos no tienen por qué ser consistentes. Eventual Consistency: la consistencia se produce de forma eventual. |
| :---- |

2.1. TEOREMA DE CAP (BREWER)  
En un sistema distribuido no se puede garantizar de forma simultánea la consistencia, la disponibilidad y la tolerancia
al particionado, solo una combinación de dos de ellas:  
``Consistency``: garantizar que la información almacenada en los nodos sea la misma.  
``Availability``: garantizar que la información almacenada en los nodos este siempre disponible.  
``Partition tolerance``: garantizar que el sistema distribuido sigue funcionando, aunque algún nodo falle.

3\. SGBD (SISTEMA GESTOR DE BASE DE DATOS)  
El sistema gestor de base de datos actúa de interfaz entre el usuario y la información almacenada, el usuario nunca
accede a los datos directamente, siempre lo hace a través del gestor. La mayoría de operaciones sobre una base de dato
se puede realizar mediante consultas. El usuario podrá realizar determinadas consultas en función de la autorización que
el administrador de bases de datos le proporcione. Se pueden definir las consultas como operaciones que se efectúan
sobre los datos de una base de datos.

3.1. SQL   
Las consultas se hacen en un lenguaje definido para el acceso a la base de datos llamado SQL (Standard Query Language):
es un lenguaje de dominio específico utilizado en programación, diseñado para administrar, y recuperar información de
sistemas de gestión de bases de datos relacionales. Efectúa consultas con el fin de recuperar, de forma sencilla,
información de bases de datos, así como realizar cambios en ellas. SQL usa los siguientes “dialectos”:  
``DDL`` (Data Definition Language): además, proporciona comandos para la definición de esquemas de relación, borrado de
relaciones, modificaciones de los esquemas de relación, comandos para especificar las restricciones de integridad que
deben cumplir los datos almacenados y comandos para la definición de vistas, también incluye comandos para especificar
los derechos de acceso a las relaciones y a las vistas.

* ``CREATE``: crear una base de datos, tabla, vistas...
* ``ALTER``: modificar la estructura, añadir o borrar columnas.
* ``DROP``: eliminar objetos de la estructura. (CASCADE: borra el usuario y todos los objetos que tenga creados).

``DML`` (Data Manipulation Language): permite a los usuarios introducir datos para posteriormente realizar tareas de
consultas o modificación de los datos.

* ``SELECT``: realizar consultas sobre tuplas / DISTINCT: devuelve solo valores distintos.
* ``INSERT``: insertar los valores / UPDATE: modificar valores.
* ``DELETE``: eliminar filas de una tabla.
* ``GROUP BY``: agrupa las filas de mismos valores en filas de resumen.
* ``WHERE``: condición que debe cumplirse para que los datos sean devueltos.
* ``LIKE``: se usa junto a un WHERE para buscar un patrón específico en una columna.
* ``HAVING``: condición que debe cumplirse para que los datos sean devueltos. Su funcionamiento es similar al de “WHERE”
  pero aplicado al conjunto de resultados devueltos por la consulta. Debe aplicarse siempre junto a “GROUP BY” y la
  condición debe estar referida a los campos contenidos en ella.
* ``COUNT``(): cuenta el número de filas que coincide con un criterio específico.
* ``AVG``() / ``SUM``(): devuelve el valor promedio / suma total de una columna numérica.

``DCL`` (Data Control Language): controlar el acceso a usuarios mediante la asignación de permisos o roles para realizar
determinadas tareas.

* ``GRANT``: otorga permisos.
* ``REVOKE``: eliminar permisos.

``TCL`` (Transaction Control Language): una transacción es una unidad en la ejecución de un programa, un conjunto de
sentencias de acceso a la BD. En la práctica suele consistir en la agrupación de consultas SQL y su ejecución como parte
de una transacción. Los pasos para realizar una transacción en MySQL son:

* Indicar que vamos a realizar una transacción con la sentencia START TRANSACTION, BEGIN o BEGIN WORK.
* Realizar operaciones de manipulación de datos sobre la base datos (insertar, borrar...).
* Si las operaciones se han realizado correctamente y queremos que los cambios se apliquen de forma permanente sobre la
  base de datos usaremos la sentencia COMMIT. Sin embargo, si durante las operaciones ocurre algún error y no queremos
  aplicar los cambios realizados podemos deshacerlos con la sentencia ROLLBACK.

El proceso de definición de tablas implica indicarlas columnas y el tipo de datos de cada una, algunos de los tipos de
datos básicos de SQL son:

* “``varchar``”: cadena de palabras compuestas de letras, números y caracteres especiales.
* “``int``”: principal tipo de datos de valores enteros de SQL Server. Números enteros con o sin signo.
* “``date``”: una fecha de calendario que contiene el año (de cuatro cifras), el mes y el día.
* “``time``”: La hora del día en horas minutos segundos (el valor predeterminado es 0).

3.1.1. CONSTRAINTS (Restricciones)  
Se utilizan para especificar reglas para los datos en una tabla como limitar el tipo de datos que pueden incluirse en
una tabla. Si hay alguna violación entre la restricción y la acción de datos, la acción se cancela, son:  
``NOT NULL``: asegura que una columna no pueda tener un valor NULL.  
``UNIQUE``: asegura que todos los valores en una columna sean diferentes.  
``PRIMARY KEY``: una combinación de una NOT NULL y UNIQUE. Identifica de forma única cada fila en una tabla.  
``FOREIGN KEY``: evita acciones que destruirían enlaces entre tablas.  
``CHECK``: asegura que los valores en una columna satisfagan una condición específica.  
``DEFAULT``: establece un valor predeterminado para una columna si no se especifica ninguno.  
``CREATE INDEX``: se utiliza para crear y recuperar datos de la base de datos muy rápidamente.

3.1.2. Wildcards (Carácter Comodín)  
``\``* : representa un conjunto de caracteres (se usa para seleccionar “todos los valores de”).  
``?`` : representa un único carácter. (m?no busca mano, mono,...)  
``\[\]`` : representa cualquier valor dentro de los Brackets.  
``\! / ^``: representa cualquier valor que no sea el que va después de la exclamación.  
``\-`` : representa el rango de valores entre los dos extremos del guión.  
``\#`` : representa un valor numérico.  
``%`` : completa la palabra (a% busca a, alba, antonio,...)  
``\_`` : representa un carácter.

3.2. JOIN  
Uno de los operadores más usados en SQL es la cláusula JOIN: sirve para combinar filas de dos o más tablas basándose en
un campo común entre ellas, devolviendo por tanto datos de diferentes tablas. Los tipos más importantes son:  
``INNER JOIN``: devuelve todas las filas cuando hay al menos una coincidencia  
en ambas tablas.  
``LEFT JOIN``: devuelve todas las filas de la tabla de la izquierda, y las filas  
coincidentes de la tabla de la derecha.  
``RIGHT JOIN``: devuelve todas las filas de la tabla de la derecha, y las filas  
coincidentes de la tabla de la izquierda.  
``FULL OUTER JOIN``: devuelve todas las filas de las dos tablas, la izquierda y la  
derecha.  
``CROSS JOIN``: devuelve el producto cartesiano de los registros de las dos tablas.

| Mediante el uso de “WHERE” se puede excluir el campo común en un JOIN pidiendo que la sentencia devuelva solo los valores nulos comunes, resultando: LEFT JOIN \+ WHERE B.Key IS NULL RIGHT JOIN \+ WHERE B.Key IS NULL OUTER JOIN \+ WHERE B.Key IS NULL |
| :---- |

3.3. INTEGRIDAD EN UN SGBD  
Una vez definidas las tablas se procederá a definir las relaciones entre ellas y las restricciones de integridad
derivadas de estas relaciones (“integridad” significa que la clave externa de una tabla de referencia siempre debe
aludir a una fila válida de la tabla a la que se haga referencia. La integridad referencial garantiza que la relación
entre dos tablas permanezca sincronizada durante las operaciones de actualización y eliminación), se puede indicar como
se desea que actúe el gestor ante una violación de la integridad:  
``Exigir integridad referencial``: el SGBD impedirá que se introduzcan datos que violen la regla de integridad. (
Ejemplo: no permitirá la introducción de una compra si no existe un DNI de cliente en las tablas de cliente).  
``Actualizar en salto o en caída``: si se modifica un atributo referenciado en otra tabla, también cambia en todas las
tablas relacionadas.  
``Borrado en salto o en caída``: en caso de que se borre una fila de una tabla, elimina también todas la relacionadas
con ella.

3.3.2. ANOMALÍAS EN UNA BASE DE DATOS  
Son resultados generados que parecen incorrectos cuando se observan desde el ámbito de una sola transacción, pero que
son correctos cuando se observan desde el ámbito de todas las transacciones. A continuación se describen los diversos
tipos de anomalías de base de datos:  
``Lecturas erróneas`` (dirtyreads): transacción lee datos que han sido escritos por otra transacción que aún no ha sido
confirmada (con COMMIT).  
``Doble lectura`` (non-repeattablereads): transacción lee datos que ya había leído, pero entre lecturas, los datos han
sido modificados o borrados por una transacción ya confirmada.   
``Lectura fantasma`` (phantomread): transacción reejecuta una consulta encontrando que el conjunto de filas resultantes
ha sido ampliado por otra transacción que inserto nuevas filas y que ya ha realizado su COMMIT.

Para dar una solución a estos problemas, los SGBD proporcionan 4 niveles de aislamiento que controlan el grado de
bloqueo durante el acceso a los datos. Para la mayor parte de aplicaciones, el acceso a los datos se puede realizar de
modo que se eviten altos niveles de aislamiento reduciendo así la sobrecarga debida a la necesidad de bloqueos por el
sistema. Si se usan altos niveles de aislamiento la posibilidad de bloqueo aumenta. Los niveles de aislamiento son:  
``Serializable``: es el que más se acomoda a lo que significa la definición de ACID, pero no permite una alta
escalabilidad, queda garantizado es que dos instrucciones “select” en la misma transacción con nivel serializable van a
devolver el mismo conjunto de datos. Implica bloquear registros que incluso no existen todavía evitando el problema de
los registros fantasma.  
``Repeatable Reads``: evita el problema de las lecturas no repetibles, no soluciona el problema de los datos fantasmas (
registros que aparecen y desaparecen dentro de nuestra transacción).  
``Read Commited``: proporciona un nivel de concurrencia muy bueno y previene del problema de las lecturas sucias, pero
no previene lecturas no repetibles y datos fantasma. Las lecturas no repetibles implican que varias instrucciones
“select” dentro de la misma transacción devuelve datos diferentes.  
``Read Uncommited``: nivel más bajo de aislamiento, protege de lecturas de datos físicamente dañados, mayor nivel de
concurrencia (nunca hay un bloqueo), no garantiza la coherencia de los datos.

3.3.3. BLOQUEOS  
Para garantizar que no haya problemas entre transacciones el scheduler emplea una tabla debloqueo de manera que sea
seguro ejecutar toda transacción. La consistencia de transacciones se basa en que una transacción solo puede leer y
escribir un elemento si se solicito un bloqueo y este no se ha liberado, y que si una transacción bloquea un elemento
debe liberarlo posteriormente. Si un scheduler cumple las condiciones anteriores se dice que es “legal”.   
Se trabaja con el llamado bloqueo de dos fases (2PL) cuando en la transacción todos los bloqueos preceden a desbloqueos
pero este sistema tiene el problema de caer en un “deadlock” (una transacción B no puede continuar hasta que otra
transacción A libere un recurso, pero a su vez, la transacción A también está esperando a que B libere el recurso). Por
lo general el DBMS detecta aquellas transacciones que caen en un abrazo mortal y lo soluciona haciendo ROLLBACK
considerando primero aquellas transacciones en las que tenga que “deshacer menos”.

3.4. BACKUP DE UNA BD  
Los BackUp se pueden clasificar en físicos y lógicos. Los físicos se realizan cuando se copian los ficheros que soportan
la base de datos, estos se dividen en:  
``BackUP del SO``: es el más sencillo de ejecutar, consume mucho tiempo y hace inaccesible al sistema mientras se lleva
a cabo, aprovecha el backup del SO para almacenar también todos los ficheros de la base de datos.  
``BackUP de la BD en frío``: implican parar la BD en modo normal y copiar todos los ficheros sobre los que se asienta.  
BackUP de la BD en caliente: se realiza mientras la BD está abierta y funcionando en modo “archivelog”, se realiza
cuando la carga es pequeña. Consiste en copiar todos los ficheros correspondientes a un tablespace, los ficheros redo
log archivados y los ficheros de control.

Los ``BackUp lógicos`` solo extraen los datos de las tablas utilizando comandos SQL: solo extraen los datos de las
tablas utilizando comandos SQL, las utilidades Export/Import permiten hacer copias de determinados objetos de la BD,
restaurarlos o moverlos de una BD a otra.

3.4.1. ARCHIVELOG  
El administrador debe decidir si arrancar la base de datos en modo “archivelog” (mecanismo de protección ante fallos de
disco. Protegerá la base de datos ante posibles fallos físicos de disco y también ante eliminaciones o modificaciones no
deseadas de los datos).  
Presenta las siguientes ``ventajas``:

* Se puede recuperar la BD con una copia antigua de los ficheros de datos y los ficheros de “redo log” (archivo que
  guarda todas las transacciones que se van realizando).
* Es posible realizar BackUPs en caliente.

``Desventajas``:

* Necesitará más espacio en disco.
* El trabajo del administrador se incrementa al tener que determinar el destino del archivado de los “redo log”.

3.5. RECUPERACIÓN DE UNA BD  
El administrador debe estar preparado ante la posibilidad de que se produzca un fallo, recuperar la BD en el menor
tiempo posible, los procesos de recuperación dependen del tipo de error y de las estructuras afectadas. Existen
diferentes modos de recuperar un fallo en la BD:  
``Recuperación de Bloques``: mecanismo de recuperación más simple, cuando un proceso muere justo cuando está cambiando
un bloque, se utilizan los registros redo log en línea para reconstruir el bloque y escribirlo en disco.  
``Recuperación de threads``: cuando se descubre que una instancia muere dejando abierto un thread, se restauran los
bloques de datos modificados que estaban en el caché de la instancia muerta y cerrando el thread que estaba abierto.  
``Recuperación física``: respuesta a un comando “recover”, convertir los ficheros backup en actuales, restaurar los
cambios que fueron perdidos cuando un fichero de datos fue puesto offline sin un checkpoint aplicando los ficheros “redo
log” archivados en línea.

| RMAN (Recovery Manager): gestor de copia de seguridad y recuperación suministrado para bases de datos Oracle. |
| :---- |

4\. MySQL  
SGBD Relacional de código abierto comercializado bajo licencia dual: Licencia pública general/Licencia comercial por
Oracle, usa el puerto 3306\. Es muy rápida en la lectura cuando utiliza el motor no transaccional MyISAM (el mecanismo
de almacenamiento de datos usado por defecto por el sistema administrador de bases de datos relacionales MySQL), pero
puede provocar problemas de integridad en entornos de alta concurrencia en la modificación. En aplicaciones web hay baja
concurrencia en la modificación de datos y en cambio el entorno es intensivo en lectura de datos, lo que hace a MySQL
ideal para este tipo de aplicaciones.  
Existen varias interfaces de programación de aplicaciones que permiten, a aplicaciones escritas en diversos lenguajes de
programación, acceder a las bases de datos MySQL. También existe una interfaz ODBC (Open DataBase Connectivity), llamado
MyODBC que permite a cualquier lenguaje de programación que soporte ODBC comunicarse con las bases de datos MySQL.  
Las ``Interfaces Graficas de Usuario`` (GUI) son un tipo de interfaz que permite a los usuarios interactuar con
dispositivos o programas electrónicos mediante iconos gráficos e indicadores visuales. Se dispone de aplicaciones de
administración gráfica de propiedad de terceros y gratuitas que se integran con MySQL y permiten a los usuarios trabajar
con la estructura y los datos de la base de datos de forma visual:  
``MySQL Workbench``: entorno integrado oficial de MySQL, permite a los usuarios administrar gráficamente las bases de
datos MySQL y diseñar visualmente las estructuras de las bases de datos. Es considerado como el front-end autorizado de
MySQL, permite a los usuarios administrar el diseño y modelado de bases de datos, el desarrollo de SQL (reemplazando al
MySQL Query Browser) y la administración de bases de datos (reemplazando al MySQL Administrator).  
``Adminer`` (antes conocido como phpMinAdmin): front-end gratuito de MySQL para gestionar el contenido de las bases de
datos MySQL. El administrador se distribuye bajo la licencia Apache (o GPL v2) en forma de un único archivo PHP y es
capaz de gestionar múltiples bases de datos, con muchas capas CSS disponibles.  
``ClusterControl``: sistema de administración de MySQL de extremo a extremo que provee la habilidad de desplegar,
monitorear, administrar y escalar instancias de MySQL desde una sola interfaz.  
``Database Workbench``: aplicación de software para el desarrollo y la administración de múltiples bases de datos
relacionales utilizando SQL, con interoperatividad entre diferentes sistemas de bases de datos, proporciona la misma
interfaz e incluye también herramientas de bases de datos cruzadas.  
``DBeaver``: cliente SQL y una herramienta de administración de base de datos.  
``DBEdit``: editor de base de datos, que puede conectarse a cualquier base de datos que proporcione un controlador
JDBC (Java Database Connectivity, es la especificación JavaSoft de una API (interfaz de programación de aplicaciones)
estándar que permite que los programas Java accedan a sistemas de gestión de bases de datos), es un software libre y de
código abierto y se distribuye bajo la Licencia Pública General GNU.  
``HeidiSQL``: anteriormente conocido como MySQL-Front, es un cliente libre y de código abierto, actúa como front-end
para MySQL (y para sus bifurcaciones como MariaDB y Percona Server). Su conjunto de características es suficiente para
las operaciones más comunes y avanzadas de bases de datos, tablas y registros de datos.  
``LibreOffice Base``: creación y gestión de bases de datos, la preparación de formularios e informes que proporcionan a
los usuarios finales un fácil acceso a los datos, también puede utilizarse como interfaz para diversos SGBD.  
``Navicat``: software multiplataforma de gestión y desarrollo de bases de datos, concretamente es una interfaz gráfica
de usuario y admite múltiples conexiones de bases de datos locales y remotas.  
``OpenOffice.org``: es de libre acceso y puede manejar bases de datos MySQL.  
``phpMyAdmin``: herramienta gratuita y de código abierto escrita en PHP destinada a manejar la administración de MySQL
con el uso de un navegador web. Puede importar datos de CSV y SQL, y transformar los datos almacenados en cualquier
formato utilizando un conjunto de funciones predefinidas.  
``SequelPro``: aplicación MacOS gratuita y de código abierto para trabajar con bases de datos MySQL de forma local o
remota.  
``SQLBuddy``: aplicación de código abierto basada en la web y escrita en PHP, destinada a manejar la administración de
MySQL y SQLite con el uso de un navegador web.  
``SQLyog``: herramienta GUI para la manipulación de datos, pueden realizarse desde una interfaz similar a una hoja de
cálculo.  
``Toad for MySQL``: aplicación de software para la administración de bases de datos relacionales y no relacionales
utilizando SQL.  
``Webmin``: herramienta de configuración de sistemas basada en la web para sistemas de tipo Unix. Está construido
alrededor de módulos, esto hace que sea fácil añadir nuevas funcionalidades.

``Interfaz de línea de comandos``: MySQL se envía con muchas herramientas de línea de comandos, de las cuales la
interfaz principal es el cliente mysql. Las utilidades de MySQL son un conjunto de utilidades diseñadas para realizar
tareas comunes de mantenimiento y administración. Incluidas originalmente como parte del Banco de Trabajo de MySQL, las
utilidades son una descarga independiente disponible en Oracle.  
Percona Toolkit es un kit de herramientas multiplataforma para MySQL, puede ser usado para probar que la replicación
funciona correctamente, arreglar datos corruptos, automatizar tareas repetitivas y acelerar los servidores.  
El shell de MySQL es una herramienta para el uso interactivo y la administración de la base de datos MySQL. Soporta los
modos JavaScript, Python o SQL y puede ser utilizado para la administración y el acceso. Los clientes en línea de
comandos de MySQL son:

* ``mysql``: shell SQL simple con capacidades de edición de línea de entrada.
* ``mysqladmin``: permite realizar las operaciones más comunes que un administrador de este motor de base de datos
  necesita realizar con comandos más cortos.
* ``mysqlcheck``: realiza el mantenimiento de las tablas: comprueba, repara, optimiza o analiza las tablas.
* ``mysqldump``: puede ser utilizado para generar respaldos de bases de datos y ser usados o incluso para ser
  transferidos a otro servidor de base datos SQL (No estrictamente tiene que ser un servidor MySQL.
* ``mysqlimport``: El cliente mysqlimport proporciona una interfaz de línea de comandos para el comando LOAD DATA
  INFILE (carga tablas de archivos de texto en varios formatos).
* ``mysqlpump``: realiza copias de seguridad lógicas , produciendo un conjunto de declaraciones SQL que se pueden
  ejecutar para reproducir las definiciones de objetos de la base de datos original y los datos de la tabla.
* ``mysqlshow``: se puede utilizar para ver rápidamente qué bases de datos existen, sus tablas o las columnas o índices
  de una tabla.
* ``mysqlslap``: programa de diagnóstico diseñado para emular la carga del cliente para un servidor MySQL y para
  informar el tiempo de cada etapa.

``Interfaces de programación de aplicaciones``: muchos lenguajes de programación con APIs de lenguaje específico
incluyen bibliotecas para acceder a bases de datos MySQL. Una interfaz ODBC llamada MySQL Connector/ODBC permite que los
lenguajes de programación adicionales que soportan la interfaz ODBC se comuniquen con una base de datos MySQL. El método
de consulta basado en ``HTSQL`` (Hyperthreaded Structured Query Language Database, sistema gestor de bases de datos
libre escrito en Java) también se envía con un adaptador MySQL, permitiendo la interacción directa entre una base de
datos MySQL y cualquier cliente web a través de URLs estructuradas.  
En ingeniería de software se considera un ``fork`` (bifurcación) al desarrollo de un proyecto informático tomando como
base un código fuente que ya existe o a la ramificación de un proyecto madre en varios proyectos que son independientes
entre sí y que cuentan con objetivos o desarrolladores diferentes. Actualmente existen dos fork de MySQL:  
``MariaDB``: fork desarrollado por la comunidad del sistema de gestión de bases de datos relacionales MySQL, notable por
estar liderado por los desarrolladores originales de MySQL, que lo bifurcaron debido a las preocupaciones sobre su
adquisición por Oracle. MariaDB pretende mantener una alta compatibilidad con MySQL, asegurando una capacidad de
sustitución "drop-in" con equivalencia binaria de la biblioteca y una coincidencia exacta con las API's y comandos de
MySQL. Incluye el motor de almacenamiento XtraDB para reemplazar a InnoDB.  
``Percona Server for MySQL``: fork que mantiene compatibilidad con las versiones oficiales de MySQL, se centra en el
rendimiento y el aumento de la visibilidad de las operaciones del servidor. Percona incluye características de
escalabilidad, disponibilidad, seguridad y respaldo que solo están disponibles en la edición comercial Enterprise de
MySQL.  
``Drizzle y WebScaleSQL`` (actualmente abandonados).

5\. PostgreSQL  
DBMS relacional orientado a objetos y de código abierto, es un descendiente de Berkeley y compatible con una gran parte
del estándar SQL, usa por defecto el puerto 5432\. Ofrece las siguientes características:  
``Consultas complejas``: hay ocasiones en las que tipos específicos de datos, como datos de diferentes tablas, deben
obtenerse de la base de datos mediante una consulta más larga o compleja.  
``Claves foráneas``: una de las alternativas que PostgreSQL ofrece para asegurar la integridad de datos es el uso de
restricciones (constraints), que se establecen en tablas y campos asegurando que los datos sean válidos y que las
relaciones entre las tablas se mantengan.  
``Vistas e Integridad transaccional``: Soporta cualquier tipo de transacciones como establece el estándar ACID.  
``Triggers``: cualquier evento que establece un curso de acción en un movimiento. En PostgreSQL, si desea tomar medidas
sobre eventos específicos de la base de datos, como INSERT, UPDATE, DELETE o TRUNCATE, la funcionalidad de activación
puede ser útil ya que invocará la función requerida en eventos definidos.  
El disparador se asociará con la tabla, vista o tabla externa especificada y ejecutará la función especificada cuando se
realicen ciertas operaciones en esa tabla. Dependiendo del requerimiento podemos crear un disparador ANTES, DESPUÉS o EN
LUGAR de los eventos / operación.  
``Alta concurrencia``: mediante MVCC (MultiVersion Concurrency Control), permite que mientras un proceso escribe en una
tabla, otros accedan a la misma sin necesidad de bloqueos y de manera consistente.  
``Amplia variedad de tipos nativos``: números de precisión arbitraria, texto de largo ilimitado, figuras geométricas (
con una variedad de funciones asociadas), direcciones IP (IPv4 e IPv6), bloques de direcciones estilo CIDR, direcciones
MAC, arrays,...

5.1. Aplicaciones cliente de PostgreSQL  
Son interfaces gráficas o de comandos para gestión, implementación, respaldo,... de PostgreSQL. La característica común
de estas aplicaciones es que se pueden ejecutar en cualquier host, independientemente de dónde resida el servidor de la
base de datos, algunas de ellas son:

* ``clusterdb``: agrupa una base de datos PostgreSQL.
* ``createdb``: crea una nueva base de datos PostgreSQL.
* ``createlang``: instala un lenguaje de procedimiento PostgreSQL.
* ``createuser``: define una nuevacuenta de usuario de PostgreSQL.
* ``dropdb``: eliminar una base de datos PostgreSQL.
* ``droplang``: elimina un lenguaje de procedimiento PostgreSQL.
* ``dropuser``: eliminar una cuenta de usuario de PostgreSQL.
* ``ecpg``: preprocesador SQL con C incorporado.
* ``pgadmin``: plataforma de desarrollo y administración de código abierto para PostgreSQL.
* ``pg\_basebackup``: realiza una copia de seguridad básica de un clúster de PostgreSQL.
* ``pg\_config``: recupera información sobre la versión instalada de PostgreSQL.
* ``pg\_dump``: extrae una base de datos PostgreSQL en un archivo de secuencia de comandos u otro archivo de
  almacenamiento, (pg\_dumpall: extrae un clúster de base de datos PostgreSQL en un archivo de secuencia de comandos).
* ``pg\_receivexlog``: transmite registros de transacciones desde un clúster de PostgreSQL.
* ``pg\_restore``: restaure una base de datos PostgreSQL a partir de un archivo de almacenamiento creado por pg\_dump (
  utilizando la opción “-d:nombrebasededatos”).
* ``psql``: Terminal interactivo de PostgreSQL, front-end basado en terminales, le permite escribir consultas de forma
  interactiva, enviarlas a PostgreSQL y ver los resultados de la consulta. Alternativamente, la entrada puede ser de un
  archivo. Además, proporciona una serie de metacomandos y varias funciones similares a shell para facilitar la
  escritura de scripts y automatizar una amplia variedad de tareas. Por ejemplo:
    * \\l (\\list): lista todas las bases de datos disponibles, luego sale. Se ignoran otras opciones sin conexión.
      Similar al metacomando \\list
    * \\?: muestra información de ayuda sobre los meta-comandos, opciones y variables.
    * \\h (\\help): muestra la ayuda de la sintaxis del comando SQL especificado.
    * \\H (\\html): activa o desactiva el formato de salida de consulta HTML.
    * \\c (\\connect): establece una nueva conexión con el servidor PostgreSQL.
    * \\i: lee un archivo, lo toma como input y ejecuta su contenido.
    * \\x: activa o desactiva el formato de tabla expandido en el resultado de cada instrucción SQL.
    * \\q (\\quit): cierra psql
    * \\o (\\out): guarda los resultados de futuras consultas en un archivo.
    * \\d “pattern”: describe la relación cuyo nombre coincida con el patron asignado.
    * \\d t/i/s/u/n/: muestra una lista de tablas/índices/secuencias/roles/esquemas.
    * \\dv: muestra una lista de vistas (\\dm: muestra una lista de vistas materializadas).
    * \\df: muestra una lista de las funciones con el tipo de datos de resultado y los tipos de datos de los argumentos.
* ``reindexdb``: reindexar una base de datos PostgreSQL.
* ``vacuumdb``: recolecta basura y analiza una base de datos PostgreSQL.

6\. SQLite  
SGBD relacional compatible con ACID, contenida en una pequeña biblioteca escrita en C, es un proyecto de dominio
público. El motor de SQLite no es un proceso independiente con el que el programa principal se comunica. En lugar de
eso, la biblioteca SQLite se enlaza con el programa pasando a ser parte integral del mismo. El programa utiliza la
funcionalidad de SQLite a través de llamadas simples a subrutinas y funciones. Esto reduce la latencia en el acceso a la
base de datos, debido a que las llamadas a funciones son más eficientes que la comunicación entre procesos. El conjunto
de la base de datos (definiciones, tablas, índices, y los propios datos), son guardados como un solo fichero estándar en
la máquina host. Este diseño simple se logra bloqueando todo el fichero de base de datos al principio de cada
transacción.  
La biblioteca implementa la mayor parte del estándar SQL-92, incluyendo transacciones de base de datos atómicas,
consistencia de base de datos, aislamiento, y durabilidad (ACID), triggers y la mayor parte de las consultas complejas.

Existe un programa independiente de nombre “sqlite3” que puede ser utilizado para consultar y gestionar los ficheros de
base de datos SQLite. La mayoría de las veces, sqlite3 solo lee líneas de entrada y las pasa a la biblioteca SQLite para
su ejecución. Pero las líneas de entrada que comienzan con un punto (".") Son interceptadas e interpretadas por el
propio programa sqlite3. Estos "comandos de puntos" se utilizan normalmente para cambiar el formato de salida de las
consultas o para ejecutar determinadas declaraciones de consulta preempaquetadas:

* ``.backup``: realiza una copia de seguridad.
* ``.clone``: clona los datos de una base de datos en una nueva base de datos.
* ``.databases``: lista los nombres y archivos adjuntos de las bases de datos existentes.
* ``.dump``: vuelca la base de datos en un fichero de datos externo.
* ``.exit``: sale del cliente y muestra un código de retorno.
* ``.explain``: obtiene una descripción de alto nivel de una implementación de una consulta SQL.
* ``.headers``: muestra la cabecera de la consulta SQL.
* ``.import``: importa información de un archivo a una tabla.
* ``.indices``: muestra los índices de una tabla.
* ``.load``: carga una extensión de una librería.
* ``.log``: activa o desactiva el inicio de sesión.
* ``.once``: redirige la salida del siguiente comando a un archivo.
* ``.open``: cierra la base de datos actual y abre la base de datos indicada.
* ``.print``: imprime un string.
* ``.quit``: sale del cliente.
* ``.read``: toma un archivo como input.
* ``.restore``: recupera contenido desde un archivo.
* ``.save``: guarda la base de datos en el archivo indicado.
* ``.schema``: muestra las sentencias CREATE que coincidan con el patrón indicado (PATTERN).
* ``.separator``: cambiar los separadores de filas y columnas.
* ``.show``: muestra valores de las opciones indicadas.
* ``.tables``: lista el nombre de las tablas especificadas.
* ``.trace``: muestra cada declaración SQL a medida que se ejecuta.

7\. SQL Server  
SGBD relacional desarrollado por Microsoft, soporta transacciones (conjunto de órdenes que se ejecutan formando una
unidad de trabajo, es decir, en forma indivisible o atómica), procedimientos almacenados (procesos almacenados
físicamente en el propio servidor, por lo cual al ser ejecutado, en respuesta a una petición de usuario, es ejecutado
directamente en el motor de bases de datos), incluye entorno gráfico, permite trabajar en modo cliente-servidor (la
información y datos se alojan en el servidor y los terminales o clientes de la red solo acceden a la información).

El lenguaje de desarrollo utilizado (por línea de comandos o mediante la interfaz gráfica de Management Studio) es
Transact-SQL (TSQL), una implementación del estándar ANSI del lenguaje SQL (usa las mismas sentencias y comandos:
CREATE, ALTER, DROP,...), utilizado para manipular y recuperar datos (DML), crear tablas y definir relaciones entre
ellas (DDL). Incluye características que permiten definir la lógica necesaria para el tratamiento de la información:

* Tipos de datos.
* Definición de variables.
* Estructuras de control de flujo.
* Gestión de excepciones.
* Funciones predefinidas.
