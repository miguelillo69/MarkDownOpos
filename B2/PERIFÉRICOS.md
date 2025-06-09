``BLOQUE II``  
``TEMA 2: PERIFÉRICOS``  
``Periférico``: Dispositivo auxiliar e independiente conectado a un ordenador.  
Categorías:

- Entrada: Teclado, ratón, escáner, lápiz óptico, cámara, sensores, micrófono,…  
- Salida: Monitor, impresora, altavoz, impresora 3D,…  
- Entrada/Salida: Pantalla táctil, casco virtual, impresora multifunción,…  
- Almacenamiento: Cinta, disco duro, CD, memoria Flash, disquete,…  
- Comunicación: Tarjetas de red, módems, hubs, switchs, routers, inalámbricos,…

Métodos de E/S:

- ``Programada (encuesta, pooling, sondeo, espera activa):``  
  * La CPU se encarga de la E/S, preguntando todo el rato si el periférico está listo.  
  * Transfiere a gran velocidad, pero bloquea la CPU no permitiendo que realice otras tareas. Apenas necesita hardware.  
- ``Interrupciones:``  
  * El periférico avisa a la CPU cuando está listo. Enviando una interrupción.  
  * Libera la CPU, pero no permite tener mucha velocidad de E/S.  
  * Dos Tipos:  
    * Hardware  
      * Externas (CPU)  
      * Internas (dispositivo E/S)  
    * Software  
      *  producidas por la ejecución de instrucciones de la CPU.  
- ``DMA`` ``(Acceso Directo a Memoria):``  
  * Un dispositivo capaz de controlar la E/S entre un periférico y memoria, sin la intervención de la CPU. (los periféricos tienen una especie de mini CPU)  
  * Limita al máximo la intervención de la CPU.  
  * Tres tipo:  
    * ``Ráfagas:`` El DMA toma el control del Bus y no lo libera hasta terminar.  
    * ``Robo de ciclo:`` El DMA retiene el Bus sólo un ciclo.  
    * ``Transparente:`` El DMA accede al Bus sólo cuando la CPU no lo está utilizando.

``Bus (canal):``

- Sistema digital que transfiere datos entre componentes de un ordenador.  
- Tipos de Buses:  
  * Paralelo: Los datos se envían por bytes. (en desuso)  
  * Serial: Los datos se envían bit a bit.  
- Puerto Físico: Interfaz hardware. (USB)  
- Puerto Lógico: Número identificativo de una conexión. (8080)  
- ``USB (Universal Serial Bus)``  
  * USB-1: 4 pines (2 datos, 2 potencia) – 12Mbps.  
  * USB-2: 4 pines (2 datos, 2 potencia) – 480Mbps.  
  * USB-3: 9 pines – 5Gbps (a veces llamado superspeed)  
  * USB-3.1: 9 pines – 10Gbps  
  * USB On the Go (``OTG``): permite convertir el puerto en un servidor o dispositivo.  
  * USB (``MSC o UMS``): Sirve para el almacenamiento masivo.  
  * Wireless USB: inalámbrico, por señales de radio. (poco extendido)  
  * Conectores:  
    * Tipo ``A, B``: Los normales, ya sean mini o micro o normales. Compatibles.  
    * Tipo ``C``: Nuevo conector, reversible. 12 pines, permite alimentación a 20v y con OTG integrado. Incompatible con A y B.  
- ``Thunderbolt`` (antiguo LightPeak)  
  * Bus de fibra óptica, con velocidades muy altas, apoyado por Apple.  
  * Thunderbolt – 10Gbps.  
  * Thunderbolt 2 – 20Gbps.  
  * Thunderbolt 3 – 40Gbps.  
  * Puede ir en un USB Type C o un Displayport.  
- ``Firewire (IEEE 1394\)``  
  * Anterior al Thunderbolt (obsoleto) 800 y 1600 Mbps.  
- ``HDMI``  
  * Audio y vídeo. 19 pines. 18Gbps. HDMI 2.0  
- ``DVI (Digital Visual Interface)``  
  * Sólo vídeo. 29 pines. Transmite el brillo como un número binario.  
- ``Displayport``  
  * Audio y vídeo. 20 pines. 10,8Gbps.  
      
- ``SATA (Serial ATA)``  
  * Evolución de los conectores ATA.  
  * Transferencia entre placa base y disco duro.  
  * SATA1 – 150Mbps.  
  * SATA2 – 300Mbps.  
  * SATA3 – 600Mbps  
- ``PCIexpress``  
  * Conexión Full Duplex. Se suele utilizar para tarjetas gráficas.  
  * PCIe (x16)   
    * 1 32Gbps (4)  
    * 2 64Gbps (8)  
    * 3 126Gbps (16)  
    * 4 256Gbps (32)  
- ``Bluetooth``  
  * Transmisión de datos inalámbrica. Por señales de radio.  
  * 24 Mbps – bluetooth 3  
  * 32 Mbps – bluetooth 4  
- ``WIFI (IEEE 802.11)``  
  * Tecnología de transmisión inalámbrica.  
  * Varios tipos:  
    * 802.11b – 11Mbps.  
    * 802.11g – 54Mbps.  
    * 802.11n – 300Mbps.  
    * 802.11ac – Wifi 5 5GHz – 1,3Gbps.

``Elementos de visualización y Digitalización:``

- ``Pixel``: unidad mínima representable.  
- ``Dot Pitch`` (tamaño de punto): Espacio entre pixeles, cuanto más pequeño más calidad.  
- ``RAMDAC:`` Convierte la señal digitar en analógica en las tarjetas gráficas.  
- Resoluciones:  
  * 720p – 720 líneas.  
  * 1080p – 1080 líneas HD  
  * 4k – 4000pixeles.  
- Clasificación:  
  * ``CRT`` \- tubo de rayos catódico.  
  * ``LCD`` – pantalla de cristal líquido. (Game Gear)  
  * ``PDP`` – plasma.  
  * ``TFT`` – Monitores planos. Transistores.  
  * ``LED`` – Leds de colores.  
    * OLED (Organic)  
    * AMOLED (matriz activa)  
    * Super AMOLED

``Escáner:``

- Periféricos que mediante el uso de la luz, forman una imagen digitalizada.  
- ``CCD:`` elemento que recoge la imagen y permite digitalizarla.  
- ``OCR`` (Optical Carácter Recognition): Permite escanear a texto.  
- Calidad en pixel por pulgada. ppp  
- Tipos:  
  * ``De mano``: Un escáner que se agarra con la mano y este lo escanea.  
  * ``Cama plana:`` El típico.  
  * ``Tambor (rotativo):`` Un escáner rotativo, permite escanear por colores.  
  * ``Cenital:`` Un pie elevado, útil para digitalizar documentos delicados.  
  * Para microfilms.  
  * Para transparencias.

Dispositivos de Impresión:

- Periféricos de salida.  
- ``PDL (Lenguaje de descripción de página):`` Codificar el documento en un lenguaje que interprete la impresora (Postscript, PCL, HPGL, TrueType).  
- ``Buffer:`` Una memoria interna de la impresora que permite compensar la diferencia de velocidad.  
- Tipos de impresoras:  
  * ``Inyección de tinta:`` Expulsan tinta por el cabezal de los cartuchos. Las más comunes. La calidad se mide en puntos por pulgada. 600dpi.  
  * ``Laser:`` Utilizan cartuchos de tóner. Un láser ioniza la página a la que se adhieren las partículas del tóner. OPC (Cartucho fotoconductor orgánico). Mejor calidad.  
  * ``Matricial:`` Son impresoras de impacto. Útiles para imprimir muchos documentos de poca calidad. Muy ruidosas.  
  * ``Térmicas:`` Utilizan un papel especial termosensible, unas agujas tocan el papel y este se pone de un color. Máquinas de tickets. Duran poco el color, no necesitan ni cartuchos, ni tinta.  
  * ``Sublimación:`` Utilizan una cinta con 4 colores (Cian, Magenta, Amarillo y Negro). Se aplica calor a dicha cinta. No usar para texto. Impresora de camisetas.  
  * ``Tinta sólida:`` Utilizan barras sólidas de tinta, parecidas a velas. Se derrite el material y se pasa al papel.  
  * ``Impacto:`` Golpean una cinta y luego al papel. (máquina de escribir)  
    * Margarita: Letras en una margarita.  
    * Rueda: Las letras están en una rueda.  
  * ``Plotter:`` Son impresoras de inyección más pensadas para publicidad. Se utilizan mucho para gráficos.

``Elementos de almacenamiento:``

- Conjunto de componentes que permiten leer y grabar datos.  
- Discos magnéticos:   
  * Utilizan medios magnéticos para guardar la información.  
  * ``Cintas:`` Muy utilizadas para copias de seguridad. LTO, DLT, DDS, DAT – hasta 200GB.  
  * ``Disketes:`` Hasta 1,44MB  
  * ``Disco Duro (HDD):`` Se dividen en discos, pistas y sectores. Tienen velocidad angular constante.  
  * ``Dispositivos ópticos (por láser):``  
    * CD-ROM 700MB – CD-RW (permite varias escrituras)  
    * DVD-ROM (+, \-) 4,7GB Si es de doble cara 17GB.  
    * Blue-Ray 25GB-54GB  
    * HD-DVD 15Gb (simple) 30GB (doble cara) 45GB (triple cara)  
  * ``Dispositivos magneto-ópticos:``  
    * Poco usados. Unidad Zip, Unidad Jaz, SuperDisk.  
  * ``Unidades de Estado Sólido (SSD)``  
    * Flash.  
    * Trabajan con puertas Nand.  
    * Tienen su propia controladora, sólo permiten una serie limitada de lecturas y escrituras.