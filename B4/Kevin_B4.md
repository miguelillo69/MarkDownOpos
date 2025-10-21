# Temario TAI Kevin adaptado Bloque II

## TEMA 1 – ADMINISTRACIÓN, MANTENIMIENTO Y REPARACIÓN DEL SO.

### 1\. TAREAS DEL ADMINISTRADOR

* Instalación y gestión de servidores (después de la instalación, el administrador debe comprobar que funciona
  correctamente, realiza estadísticas sobre el funcionamiento tanto en situaciones normales como en situaciones
  críticas), mantenimiento y configuración de estaciones de trabajo (además de la red y de los servidores, también debe
  instalar y configurar las estaciones de trabajo), instalación y mantenimiento de la red (las redes de datos
  incrementan su tamaño, interconexiones de delegaciones lejanas de una misma empresa, autenticación centralizada,
  VoIP...), gestionar usuarios (responsable de asignar cuentas, gestionar las existentes, asignarle un nombre,
  localización en el sistema de ficheros, determinar el grupo de trabajo, asignar privilegios...
* Cuando un usuario deja de estar activo hay que desactivar su cuenta por razones de seguridad), realizar copias de
  seguridad (también debe verificar su seguridad, identificar los medios utilizados, planificar la estrategia de
  backups, la LOPD puede obligar a mantener un número de copias en un plazo de tiempo determinado), monitorizar el
  sistema (comprobar diariamente que el web, proxy, mail y otros servicios funcionan correctamente, en los ficheros
  “log” se anota el funcionamiento del sistema)\*, mantenimiento de documentación (cuando se modifica el sistema, la
  documentación debe ser actualizada, abarca la configuración de SO, software, cableado, registros, copias de
  respaldo,...)\*\*, enseñar y ayudar a los usuarios,...

### 2\. RESPONSABILIDADES DEL ADMINISTRADOR

* ``Responsabilidad de Hardware``: responsable de la configuración y mantenimiento general del sistema con tareas como
  la creación y manutención de un diagrama o esquema de hardware del sistema, verificar que los periféricos estén
  instalados correctamente y probados, monitorización, reparar el sistema en caso de fallo de hardware, diseñar,
  mantener y monitorizar la red, realizar informes de administración del sistema, control del  
  mantenimiento preventivo,...
* ``Responsabilidad de software``: instalar y configurar el SO, crear los sistemas de archivos y monitorizar el uso de
  recursos, diseñar e implementar rutinas de copia de seguridad y recuperación de información, configurar y mantener el
  software de impresión (spooler), instalar y mantener el software para comunicaciones y redes, actualizar el SO y
  realizar informes de la administración del sistema,...
* ``Responsabilidades con los usuarios``: permitir el acceso a los usuarios de acuerdo a sus necesidades, eliminar a
  usuarios ya no autorizados, evaluar los requerimientos de los usuarios, planear el futuro crecimiento/cambio del
  sistema,...
* ``Responsabilidades de documentación``: “que, quien, cuando y como se ha hecho”, problemas que aparecieran (pitfalls),
  parámetros utilizados, informes de mantenimiento...

### 3\. GESTIÓN DE INCIDENCIAS

* Las incidencias son comportamientos anormales del sistema, pueden deberse a comportamientos anómalos del software, un
  problema en la red, incompatibles entre diferentes arquitecturas y SO, etc. Este comportamiento acaba generando
  incidencias en los servicios que proporciona el sistema como pérdidas de tiempo, decrementos de la funcionalidad,...
* ``Service Level Agreement`` (SLA):
    * Contrato en el que se estipulan los niveles de un servicio en función de una serie de parámetros objetivos,
      establecidos de mutuo acuerdo entre ambas partes y que refleja contractualmente el nivel de operativo de
      funcionamiento, penalizaciones por caída de servicio, limitación de responsabilidad por no servicio...
    * Es decir, es el mantenimiento de la disponibilidad de un determinado servicio basado en un compromiso, medible y
      demostrable, del nivel de cumplimiento en su ejecución.
    * Un SLA debe cubrir como mínimo: soporte a clientes y asistencia, provisiones para seguridad y datos, garantías del
      sistema y tiempos de respuesta como ``MTBF`` (Medium Time Between Fails) y ``MTTR`` (Medium Time To Recover) tras
      una caída.
* ``Service Level Management`` (SLM):
    * Metodología y procedimientos necesarios para la gestión de los SLA y para asegurar que todos los clientes de un
      departamento de TI reciben unos niveles de servicio acordados responsable de asegurar que todos los Acuerdos de
      Nivel Operacional (OLA) y Contratos de Apoyo (UC) sean apropiados.

***

* > RPO (Recovery Point Objective): es la cantidad de datos que una empresa puede permitirse perder y aun así seguir funcionando si sufre un tiempo de inactividad.
* > RTO (Recovery Time Objective): es el tiempo maximo que un negocio necesita para recuperar sus sistemas después de inactividad producida por un incidente

***

### 4\. ACTUALIZACIÓN, REPARACIÓN Y MANTENIMINETO DEL SO

* Los mecanismos de actualización de los sistemas operativos son específicos de cada SO, para Windows la actualización
  se realiza a través de Windows Update (desde Windows 98), además, a partir de Windows XP SP3, se introduce BITS (
  Background Inteligent Transfer Service).
* En 2002, se introduce WSUS (Windows Server Update Services) que en Windows Server 2012 pasa a ser un ROL que se puede
  tener habilitado en el servidor nativamente.
* Por otra parte, dependiendo de la distribución de Linux, las herramientas más conocidas son:
    * ``YUM`` (Yellow dog Update Modified): gestión de paquetes para sistemas Linux basados en RPM “Red Hat Packet
      Manager” (
      RedHat, Fedora, CentOS...), es una herramienta para instalar, actualizar y eliminar paquetes, es una herramienta
      en modo comando (“yum-updatesd”, “yum-updateonboot”), YUM es usado por herramientas como YAST (Yet Another Setup
      Tool) de SUSE y OpenSUSE.
    * ``APT`` (Advanced Packaging Tool): herramienta de gestión de paquetes creada por Debian, implantado también en
      Ubuntu. Se puede usar en comando (“apt-get”), o con interfaz gráfica (SYNAPTIC), ofrecen un mecanismo de gestión
      de paquetes del SO con sintaxis (sudo:apt-get:opciones), siendo las opciones más habituales:
        * ``update``: se encarga de actualizar la lista de paquetes disponibles, pero no instala o actualiza ningún
          paquete.
        * ``upgrade``: se ocupa de actualizar las versiones previamente descargadas.
        * ``install`` (o apt-get install): instala los paquetes.

***

* > “apt-cache”: puede realizar búsquedas de paquete basándose en palabras clave con la sintaxis (apt-cache:search:palabra\_clave). También puede mostrar las cabeceras de las versiones disponibles de un paquete con “apt-cache:show:paquete”.
* > “apt-remove”: borra los archivos binarios de un paquete instalado únicamente.
* > “apt-purge”: borra los archivos binarios de un paquete instalado y además los ficheros de configuración del mismo.

***

#### 4.2. MECANISMOS DE REPARACIÓN

* ``Bootrec``: herramienta utilizada para las reparaciones pertinentes del sector de arranque del sistema (MBR), tiene
  habilitados comandos como:
    * ``/FixMBR``: permite arreglar y/o recuperar el MBR, sector de arranque de un disco duro. No sobrescribe la tabla
      de partición existente.
    * ``/FixBoot``: Esta opción escribe un nuevo sector de arranque en la partición del sistema utilizando un sector de
      arranque compatible, es recomendable utilizar si el sector de arranque está dañado o si el sector de arranque se
      sustituyó.
    * ``/RebuildBCD``: reconstruir por completo el almacén BCD (Boot Configuration Data) que constituye el menú de
      arranque.
    * ``/ScanOS``: escanea todos los discos en busca de instalaciones compatibles con Windows, es útil cuando hay
      instalaciones que no aparecen en el menú.

* ``SFC``: ofrece la posibilidad de examinar todos los archivos protegidos para comprobar sus versiones, descubre un
  archivo protegido se ha sobrescrito, recupera la versión correcta desde la carpeta caché o los archivos origen de la
  instalación de Windows.

#### 4.3. TIPOS DE MANTENIMINETO

* ``En función de donde se encuentra el técnico``:
    * ``In site``: situación en la que se desplaza un técnico a la oficina en la que manifiesta el problema.
    * ``On site``: el técnico no se desplaza, ya está ubicado en dicha oficina.
    * ``Remoto``: problemas Software que se pueden solucionar mediante el uso de aplicaciones de control remoto.
* ``En función del tipo de acciones realizadas``:
    * ``Correctivo``: ciertos cambios que buscan corregir errores precisos.
    * ``Evolutivo``: incorporaciones, modificaciones y eliminaciones para cubrir la expansión o cambio de las
      necesidades.
    * ``Adaptativo``: modificaciones que afectan a los entornos de configuración de hardware, software de base...
    * ``Perfectivo``: revisión constante del software para detectar posibles focos de problemas que puedan surgir.
* ``Periodicidad del mantenimiento``:
    * ``Tiempo de respuesta``: tiempo que transcurre desde el aviso de avería hasta que el equipo técnico se dispone a
      resolver dicha avería.
    * ``Mean Time To Repair`` (MTTR): tiempo que transcurre desde la notificación de la incidencia y la restitución del
      elemento.
    * ``Mean Time Between Failures`` (MTBF): periodo medio comprendido entre dos fallos consecutivos, es usado como
      medida de calidad de los equipos.
    * ``Tiempo mínimo garantizado de disponibilidad``.

***

* > TPM (Third Party Maintenance): empresas de servicios de mantenimiento.
* > Remedy Service Desk: es una aplicación de software para implementar una mesa de ayuda a nivel enterprise compatible con los procesos de ITIL que incluye manejo de indicentes, manejo de problemas, niveles de servicio y muchas facilidades más ya que forman parte de la suite BMC Remedy ITSM.

***

## TEMA 2 – ALMACENAMIENTO, VIRTUALIZACIÓN Y CONTENEDORES

### 1\. SISTEMAS DE ALMACENAMIENTO Y SU VIRTUALIZACIÓN

* El almacenamiento de datos es el proceso por el cual se archiva, organiza y comparten los datos que componen los
  archivos que se utilizan en el día a día como documentos de texto, imágenes, configuraciones, vídeos, sonidos y
  cualquier otra información en formato digital.
* El almacenamiento de datos se realiza en dispositivos de hardware que disponen de unas características que los definen
  y que los hacen más adecuados para guardar copias de seguridad, dar acceso a los datos, transportar la información y
  otras funciones. Los principales dispositivos de almacenamiento de datos, son:
    * ``Cabinas de discos``: entornos de almacenamiento de discos organizados en bandejas, que incluyen los elementos de
      conectividad a los servidores, los controladores (protocolos de acceso, RAID, caché, mecanismos de copia...) y los
      discos individuales. Las partes más importantes, son:
        * ``Front-end``: se encargan de proporcionar conectividad e implementar las distintas interfaces de la cabina (
          FC, SAS, iSCSI, FICON...), es muy importante el número de puertos que presentan para cada uno de los
          protocolos que soportan, así como la velocidad de los mismos.
        * ``Back-end``: se encarga de la conectividad a bajo nivel a los discos y sus componentes (FC, SAS, SATA...). Su
          elemento principal es la controladora, basada en garantizar la redundancia, esta puede ser proporcionada
          mediante varias controladoras activas o mediante una controladora activa y otra de respaldo. La memoria caché
          de las controladoras puede estar dotada de configuraciones en espejo para garantizar la máxima disponibilidad.
      ***
        * > Grupo de almacenamiento (pool): bloque de almacenamiento creado a partir de uno o más discos físicos y que nos permiten agregar la capacidad de una forma flexible, se carga un disco físico a la cabina y se asigna al grupo de almacenamiento para ampliar su capacidad.
      ***

    * ``Cintas``: orientada principalmente a proporcionar gran capacidad de almacenamiento a un coste inferior al de los
      discos, a costa de perder rendimiento en la grabación y el acceso a los datos. Presentan un modo secuencial de
      acceso a los datos renta frente al modo aleatorio de los discos, la tecnología de cintas es más lenta que la del
      disco, dos modelos de trabajo de las cintas:
        * ``Orientadas a trabajo “on-line”``: la cinta se utiliza directamente por el servidor como un dispositivo de
          almacenamiento convencional.
        * ``Orientadas a backups``: la cinta se utiliza solamente para almacenar backups.
    * La principal diferencia entre ambos modos es que en las orientadas a backups funcionan de forma continua, sin
      necesidad de parar, rearrancar la cinta ni rebobinar en una misma sesión de escritura.
    * El uso online impone requisitos mecánicos en las cintas mucho más restrictivos que en el caso de las cintas
      destinadas a backup, es casi exclusivo del entorno mainframe, en sistemas abiertos las cintas se utilizan
      principalmente para backup.
    * Existen dos tipos de cintas: de “``grabación helicoidal``” y las de “``grabación longitudinal``” con menor
      capacidad que las de grabación helicoidal, pero más rápidas.
    * Tecnología de ``cintas más conocidas``:
        * ``Cintas DAT`` (Digital Audio Tape): surgieron como cintas de grabación de audio digital, posteriormente
          pasaron a estándar para grabación de datos. Utilizan cinta de 4mm y grabación helicoidal. Actualmente se
          dispone de cintas DAT de hasta 80GB y velocidades de acceso de hasta 12MBps, las cintas deben renovarse tras
          unas 2000 pasadas.
        * ``Cintas de 8mm``: inicialmente se trataba de un estándar para grabación de video, se transformó para
          grabación de datos, la tecnología es similar a las cintas DAT, pero con mayor capacidad y mayor velocidad de
          acceso. Tienen memoria interna que almacena datos sobre índices en la cinta, estado de la misma... acelera los
          tiempos de búsqueda y el mantenimiento.
        * ``Cintas QIC`` (Quarter-Inch Cartridge): grabación lineal con hasta 4GB de almacenamiento y 1MBps de
          velocidad, deben renovarse tras 5000 pasadas.
        * ``Cintas TRAVAN``: surgen a partir de las QIC, con capacidad para 20GB y 4 MBps.
        * ``Cintas DLT`` (Digital Line Tape): grabación lineal, capacidad para 300GB y 36MBps.
        * ``Cintas LTO`` (Linear Tape-Open): grabación lineal, los cartuchos tienen memoria interna que almacena
          información de estado de la cinta que permite a las unidades detectar un cartucho degradado antes de que se
          produzca el fallo. Presenta una duración superior al millón de pasadas, la generación 6 presenta capacidades
          de 6GB y 400MBps.
    * Las unidades de cinta pueden estar agrupadas en librerías, pueden ser manuales, en las que deben ser operadores
      los que introduzcan cintas en las unidades. Están en desuso, siendo sustituidas por librerías automáticas en las
      que un brazo mecánico selecciona las cintas y las introduce o saca de las unidades de cinta.
    * Existen dos tipos de productos de automatización, los cargadores automáticos que contienen una o dos unidades de
      cinta y un número limitado de cartuchos normalmente no más de 30, y las librerías automáticas, que disponen de
      varias unidades y varios cientos o miles.

### 2\. ARQUITECTURA DE ALMACENAMIENTO DE DATOS

* Las arquitecturas de almacenamiento podemos clasificarlas en dos tipos atendiendo al acceso requerido, ya sea
  directamente a disco o a fichero:
    * Acceso a nivel de disco (dentro de las tramas del protocolo de capa 2 ``SAS, FC, iSCSI...`` se transportan, a
      nivel de bloque, los datos):
    * Con discos internos, por medio de una cabina dedicada (DAS)
    * Mediante una red especifica de almacenamiento (SAN)
    * Acceso a nivel de fichero:
    * Sistema de ficheros creado y gestionado por el sistema operativo del servidor (NAS), tendrá asociado un
      determinado espacio en discos. El cliente o aplicación hará las peticiones de los mismos al NAS de forma
      transparente para el usuario.

#### 2.1. DISCOS INTERNOS

* El modo más básico de conectividad, los discos están conectados a un bus interno del servidor, presenta dos variantes:
  conectividad basada en el bus SCSI (más avanzado y caro) para sistemas empresariales o conectividad basada en el bus
  ATA para sistemas domésticos.
* Ambos buses son de tipo paralelo, lo que conlleva limitaciones que produjeron la aparición de SAS como evolución de
  SCSI y SATA como evolución de ATA, ambas modifican las capas bajas de los protocolos pasando a un protocolo serie en
  lugar de paralelo.

* Los datos de aplicaciones con un mínimo de criticidad no deberían ubicarse en los discos internos del servidor,
  quedando estos relegado a alojar la instalación del SO y de la aplicación (actualmente debido al auge de la
  virtualización de servidores también la instalación reside en una red separada de almacenamiento en forma de máquina
  virtual que puede ubicarse en un servidor y otro de manera rápida).

#### 2.2. DIRECT ATTACHED STORAGE (DAS)

* La conectividad más común entre servidores y almacenamiento está basada en ``SCSI`` o en ``FC``, el protocolo SAS
  sustituye la capa física paralela de SCSI por un protocolo serie y puede ser utilizado para conectar las cabinas de
  almacenamiento directamente a los servidores, el almacenamiento externo es utilizado igual que el interno, sin que las
  capas de ``SO``
  distingan entre ambos, el uso del almacenamiento externo dedicado resuelve los problemas de escalabilidad y seguridad
  del almacenamiento interno, ya que las cabinas de discos son ampliables y tienen una capacidad máxima muy superior,
  además presentan características de alta disponibilidad como redundancia de componentes, niveles de RAID, en espejo o
  con paridad para recuperarse de fallos de disco, software de copia de datos en tiempo real que permite replicar datos
  en tiempo real en otra cabina...

* La interfaz gráfica de usuario con el servidor o con la estación de trabajo está hecha por medio de un ``HBA`` (Host
  Bus Adapter): hardware que conecta un servidor a una red de computadoras y dispositivos o unidades de almacenamiento.
  Normalmente, se refieren a dispositivos a los que se conecta otros dispositivos ``(IDE, SCSI, FC, eSATA)``, pero
  también se suele utilizar el mismo término para los dispositivos que se conectan a sistemas ``Ethernet``, ``FireWire``
  y ``USB``. Recientemente, la llegada del ``iSCSI`` ha dado lugar a los ``HBA`` vía Ethernet, que se diferencian de las
  tarjetas de red en que incluyen hardware dedicado para ``iSCSI``.
* Un típico sistema DAS provee controladores embebidos. El manejo del RAID es off-load, o simplemente sin ``RAID``. Los
  HBA pueden ser usados reduciendo costos. Los controladores ``DAS`` también habilitan acceso compartido al
  almacenamiento, que permite servidores múltiples (no más de cuatro) para acceder a la misma unidad lógica, una
  característica que es simplemente usada para clustering.
* En este punto, los sistemas ``DAS`` de alto rango comparten similitudes con los sistemas SAN de nivel básico.

#### 2.3. STORAGE AREA NETWORK (SAN)

* Red dedicada al almacenamiento, conectada a las redes de comunicación de una organización, los equipos con acceso a
  las SAN tienen una interfaz de red especifica que se conecta a la SAN.
    * Es una arquitectura de acceso a bloques en la que los protocolos de acceso son los mismos que en discos o cabinas
      dedicadas.
    * Los discos no están conectados internamente al servidor.
        * Al tratarse de un acceso por bloques, el sistema de ficheros es creado por el servidor, este tipo de
          almacenamiento no permite el acceso de varios servidores a los mismos datos a no ser que estos formen parte de
          un clúster de servidores y se coordinen para el acceso a los datos.
    * La unidad de almacenamiento que provee una red SAN se denomina LUN (Logical Unit Number) y es un disco virtual
      proporcionado por la SAN, las SAN se componen de tres capas:

        * ``Capa Cliente``: servidores, dispositivos o componentes (interfaz de red, de fibra...) y software (SO).
        * ``Capa Red``: los cables (FO) así como los SAN Hubs y los SAN Switches como punto central de conexión para
          SAN.
        * ``Capa Disco``: agrupaciones de discos (Disk Arrays, Memoria Caché, RAIDs) y cintas, empleados para almacenar
          datos.

* Posibles ``protocolos`` de ``transporte`` de datos en una ``SAN``:
    * ``SAN-FC``: un conjunto de switches que conmutan las tramas FC.  
      iSCSI (Internet SCSI): estándar que permite el uso del protocolo SCSI sobre redes TCP/IP, permiten el intercambio
      de tramas SCSI sobre TCP/IP, en lugar de sobare FC. El objetivo es utilizar la infraestructura LAN existente, a
      igualdad de ancho de banda para el transporte, las redes iSCSI son menos eficientes que las redes FC.
    * ``FCoE`` (Fiber Channel sobre Ethernet): está diseñado sin capa IP, por lo que  
      no es posible enrutar directamente paquetes IP.

##### 2.3.1. VIRTUALIZACIÓN DE SISTEMAS DE ALMACENAMIENTO DE DATOS (VSAN)

* Permite unificar el almacenamiento local de todos los servidores de un clúster y gestionarlo como si se tratase de un
  almacenamiento compartido SAN tradicional. Una red de área de almacenamiento virtual es una colección de puertos de un
  conjunto de conmutadores conectado que forma un tejido virtual, en el acceso a bloques, la relación entre el servidor
  y la cabina física de almacenamiento de forma que sea posible cambiar la cabina o mover los datos de una cabina a
  otra, VSAN se puede implementar de tres formas:
    * ``En el servidor``: se debe instalar un software de virtualización que oculta al resto del SO la cabina física en
      la que residen los datos. El SO se encarga de acceder a los dispositivos virtuales que luego la capa inferior se
      encarga de transformar en los dispositivos reales. El inconveniente de este tipo de virtualización es que requiere
      instalación en los servidores.
    * ``En red``: la propia red SAN, mediante conmutadores inteligentes, proporciona la  
      virtualización, el servidor accede a los discos utilizando direcciones de cabina virtuales, es posible cambiar el
      repositorio físico de los datos sin que los servidores sean conscientes de ello ya que siguen solicitando los
      datos a las cabinas virtuales.
    * ``En cabina``: una cabina con capacidades avanzadas se encarga de reenviar las peticiones de los servidores a las
      cabinas en las que realmente residen los datos. La cabina virtualizadora como destino de sus peticiones, luego el
      dispositivo de virtualización envía los datos a la cabina que corresponda en cada caso.

***

> ``VRRP`` (Virtual Router Redundancy Protocol): protocolo de comunicaciones no propietario definido en el ``RFC 3768`` diseñado para aumentar la disponibilidad de la puerta de enlace por defecto dando servicio a máquinas en la misma subred. El aumento de fiabilidad se consigue mediante el anuncio de un router virtual como una puerta de enlace por defecto en lugar de un router físico. Dos o más routers físicos se configuran representando al router virtual, con sólo uno de ellos realizando realmente el enrutamiento. Si el router físico actual que está realizando el enrutamiento falla, el otro router físico negocia para sustituirlo. Se denomina router maestro al router físico que realiza realmente el enrutamiento y routers de respaldo a los que están en espera de que el maestro falle.

***

#### 2.4. NETWORK ATTACHED STORAGE (NAS)

* Se realiza acceso a ficheros directamente contra el servidor de ficheros o la cabina de almacenamiento con capacidad
  NAS donde se gestiona el sistema de ficheros. El SO del servidor monta un sistema de ficheros externo a través de
  alguno de los protocolos destinados a ese fin (NFS, CIFS...) y delega la transformación de fichero a bloque de bits en
  la red de almacenamiento. La conexión de red que permite el acceso al sistema de ficheros puede ser:
    * ``Conexión a través de LAN``:
        * Solventa el problema del acceso a los datos desde diferentes orígenes, montan los sistemas de ficheros
          exportados que son utilizados por las aplicaciones como si fuesen discos locales.
        * Los sistemas que actúan de servidores de ficheros pueden ser servidores de propósito general o puede tratarse
          de dispositivos especiales, NAS, dedicados en exclusiva a servir fichero y diseñados especialmente para ello,
          tiene como principales funciones la implementación de los protocolos que permiten compartir los ficheros y la
          gestión de la estructura de ficheros.
        * El almacenamiento final de los datos se realiza lógicamente mediante bloques de bits que pueden residir tanto
          internamente en el servidor de ficheros como extremamente en una cabina de la red SAN.
    * ``Conexión a través de WAN``:
        * Donde el ancho de banda es menor y especialmente la latencia mayor presenta problemas pueden hacer inviable la
          compartición de fichero a grades distancias.
        * Para evitar estos problemas está surgiendo el concepto de WAFS (Wide Area File Services) basado en la
          compresión de las tramas de datos de los protocolos CIFS y NFS, para evitar un excesivo número de mensajes y
          el uso de cache local en las oficinas remotas.

### 4\. POLÍTICAS, SISTEMAS Y PROCEDIMIENTOS DE BACKUP Y RECUPERACION

* La conservación de la información se basa en la autenticidad, confidencialidad, integridad y disponibilidad de la
  información, su finalidad es mantener la información para que sea utilizada en el momento preciso.
* La salvaguarda y recuperación de la información en un sistema de información, para ser capaces de mantener la
  disponibilidad de los servicios, no solo es importante replicar las redes, sistema de comunicaciones, servidores,
  estaciones sistemas críticos, sino que además es necesario mantener la capacidad de acceso a los datos puesto que
  estos constituyen la esencia de información.
* Se construyen los dispositivos y sistemas de almacenamiento con la calidad suficiente para garantizar un tiempo de
  fallo mínimo, hace uso de la redundancia en la forma de replicación de la información.
* Los ``métodos de recuperación de datos`` son aquellos procesos llevados a cabo con el objetivo de restablecer el
  acceso a la información que sigue estando almacenada en los dispositivos, pero que no está disponible por alguna
  causa:

    * ``Métodos de recuperación lógica``: cuando todos los componentes del dispositivo funcionan correctamente y por
      tanto se puede acceder a todos los sectores donde se almacena la información.
    * ``Métodos de recuperación física``: algún componente físico del dispositivo se encuentra dañado, se podrá abordar
      una recuperación física reparando o sustituyendo el componente dañado y accediendo nuevamente a la información
      guardada.

#### 4.1. ESTRATEGIAS Y POLÍTICAS DE BACKUP

* Para construir una estrategia asegurando que cualquier caída pueda ser recuperada rápidamente es indispensable contar
  con una plataforma de BackUp regida por un Plan de Contingencia probado y actualizado, los procesos de Copias de
  Resguardo consumen tiempo y recursos del sistema es necesario programar bien su plazo de ejecución para que no
  interfiera con el buen funcionamiento de los sistemas.
* Los ``tres`` ``tipos de copias de seguridad`` que se pueden realizar son:
    * ``Copias Completas``: copia completa de todos los archivos, solo requiere una cinta para recuperar todos los datos
      necesarios, la alternativa más rápida a la hora de realizar la recuperación.
    * ``Copia Incremental``: el BackUp empieza por una copia completa de todos los datos, la siguiente copia se hace
      solo sobre los archivos que se hayan modificado, al día siguiente se realiza el mismo proceso. Raciona y optimiza
      los medios de BackUp por encima de la velocidad de recuperación de los mismos.
    * ``Copia Diferencial``: compra cada copia diaria con la última copia completa disponible, la primera copia
      Incremental el igual a la primera copia diferencial, pero al segundo día, el incrementa solo conserva los datos
      modificados desde la copia anterior, el diferencial lo hace desde la copia completa. Es más exigente en cuanto al
      consumo de medios, pero es mucho más cómodo a la hora de realizar la recuperación de archivos, ya que como máximo
      requiere 2 medios, cada día acumula la copia del día anterior, consume más recursos.

> ``Archive Bit``: marca que llevan todos los archivos del sistema la cual se habilita si el archivo ha sido resguardado mediante un programa de ``BackUp``, de este modo analizan dicho bit y hacen copia solo de los archivos que lo tienen desactivado, lo que significa que han sufrido algún cambio desde el ultimo BackUp.

* ``Estrategias de rotación de soportes``:
    * ``Hijo``: método más simple, consiste en contar con un grupo de soportes (cintas) donde usamos un soporte por día
      durante una semana, es posible recuperar los archivos que tengan por lo menos una semana de antigüedad. Cada
      BackUp diario es completo y las cintas se van rotando. Es un esquema adecuado para ambientes con problemas a la
      hora de acceder a los medio o ambientes con cambios muy dinámicos de sus archivos.
    * ``Padre e Hijo``: funciona como el anterior, pero además de asegurar datos de la última semana incorpora 5 medios
      más para conservar una semana adicional, se realizan BackUp diferenciales o incrementales de lunes a jueves y se
      realiza un acopia completa el viernes que se guarda en una ubicación externa.
    * ``Padre, Hijo y Abuelo``: medio más común de BackUp, se mantienen copias diferenciales e incrementales durante 4
      semanas con una copia completa semanal. De las copias completas semanales la última del mes se conserva como copia
      completa mensual, y es reemplazada por la siguiente de un grupo de 12 que nos permiten conservar la información
      durante un año.

#### 4.2. DIFERENCIA ENTRE BACKUP DE SISTEMAS FÍSICOS Y VIRTUALES

* En el BackUp de sistemas físicos, las máquinas físicas necesitan de un software específico mediante el cual sea
  posible realizar copia, se puede realizar locamente mediante un sistema de arrays de discos o remotamente en un
  entorno ``NAS o SAN``.
* En un entorno tradicional de múltiples servidores físicos, las copias de seguridad se realizan instalando un agente en
  cada servidor y añadiendo una tarea a la programación de copias de manera que u servidor específico de backup se
  conecta a cada uno de los agentes para iniciar la copia de los datos que sean necesarios.

* Los BackUp de sistemas virtuales dan facilidades para el despliegue en otro servidor de VMs en mucho menos tiempo,
  proporcionando soluciones para copias completas como:
    * ``Copias completas en caliente``: de una VM alojada en un host ESXi en un segundo servidor de máquinas virtuales
      sin que las VM alojadas en el primer servidor deje de estar funcionando, se llama replicación de VMs.
    * ``Snapshots``: BackUp de la VM en frio (apagando la VM), pero reduciendo la duración que tarda en hacer la copia,
      puede ser completo o solo de ficheros concretos. Muchos sistemas (VMWare) ofrecen plugins que permiten realizar
      copias en caliente de VMs completas sin pérdida de continuidad de negocio.

### 6\. VIRTUALIZACIÓN DE SISTEMAS Y VIRTUALIZACIÓN DE PUESTOS DE USUARIO

* Es la combinación de hardware y software, permite a un conjunto de recursos físicos funcionar como si fueran múltiples
  recursos lógicos.
* Consiste en añadir una capa de abstracción que separa el hardware físico del software que lo usa permitiendo
  flexibilidad y una mejor utilización de los recursos de los servidores.
* Es necesario multiplexar el acceso físico a los recursos mediante una interfaz que encapsule los detalles de la
  arquitectura subyacente, es posible virtualizar servidores, almacenamiento, redes e incluso puestos de trabajo.
* Las máquinas virtuales se pueden gestionar, actualizar y manipular fácilmente como si fuesen ficheros, por lo que
  proporcionar una máquina virtual es un proceso rápido y simple.

***

* El software que se ocupa de implementar dicha capa de abstracción y de encapsular es el SO anfitrión (host), se
  encarga de gestionar los accesos a los recursos físicos por parte de los SO huésped (guests).
* Un sistema anfitrión suele albergar varios sistemas invitados, dentro de los recursos existentes se puede lograr la
  virtualización de procesador (se logra coordinar el acceso al procesador por parte de las distintas VMs), memoria (
  debe ser gestionada cuidadosamente para posibilitar que múltiples sistemas alojados compartan memoria física
  impidiendo que los sistemas sobrescriban datos de otros), red (garantiza que las VM enviarán y recibirán el tráfico de
  red apropiado) y almacenamiento (se asegura que cada una de las máquinas virtuales tienen su propio almacenamiento de
  datos y que está aislado del resto).

> Un caso particular de virtualización es la Java VM, lo que se virtualiza es un proceso, se ejecuta como proceso en el SO y soporta solo un proceso, cuando se lanza este se ejecuta la VM automáticamente y se le proporciona al proceso un entorno de ejecución independiente de la plataforma hardware y del SO, permitiéndole que se ejecute sobre cualquier plataforma.

#### 6.1 VENTAJAS DE LA VIRTUALIZACIÓN DE SERVIDORES

* El modelo tradicional del uso de un servidor dedicado es extremadamente costoso debido al:
    * ``Coste del hardware``: los servidores crecen en capacidad y en potencia de procesamiento, dedicar un servidor
      para cada aplicación con objeto de garantizar un control total sobre las mismas no es rentable.
    * ``Coste del software``: cada servidor requiere licencias.
    * ``Coste de energía e infraestructura``: la conexión y el suministro de energía para los servidores pueden ser
      extremadamente caros.
    * ``Costes de gestión``: los costes de gestión suponen la mayor parte, el personal de TI tiene que actualizar,
      mantener cuentas, hacer copias...

***

* El modelo de ``virtualización de servidores`` presenta unas ventajas que motivan a una organización a llevar a cabo un
  proceso de consolidación de servidores mediante virtualización:
    * ``Optimización en el uso de hardware``: la mayoría de servidores físicos están trabajando a un 10% o 15% de su
      capacidad total de proceso, se desaprovecha casi la totalidad de su capacidad, aplicando la virtualización las
      organizaciones pueden mejorar la ratio de utilización de sus recursos y obtener grandes ahorros energéticos.
    * ``Aislamiento entre máquinas virtuales``: las VMs se ejecutan en un entorno seguro, aislado e independiente del
      resto de VMs, facilitando la instalación de un único servido por máquina, algo que a nivel de hardware es bastante
      costosos.
    * ``Alta disponibilidad``: en caso de alguna contingencia tiene un coste mucho mayor que en el caso de servidores,
      suele implicar la instalación de tarjetas de memoria y/o procesador además de la instalación del SO y la
      instalación del servicio en cuestión, en el caso de VM se puede tener la maquina duplicada preparada y en caso de
      contingencia poder restaurar el servicio en cuestión de minutos perdiendo el servicio únicamente durante el
      reincido de la VM.
    * ``Evaluación de nuevos sistemas operativos o actualizaciones``: con un entorno virtual se pueden realizar pruebas
      de nuevos SO manteniendo independiente la maquina con el servicio en producción.
    * ``Mejor aprovisionamiento y administración del entorno``: es posible realizar copias de seguridad del sistema al
      completo permitiendo mover maquinas completas entre los servidores físicos, la gestión de la carga de trabajo se
      simplifica, es posible la toma de snapshots (imágenes concretas del sistema en el momento que se toma, de forma
      que se pueda restaurar al momento del snapshot en caso de error del sistema).

#### 6.2. TIPOS DE VIRTUALIZACIÓN DE SERVIDORES

* El objetivo es ofrecer múltiples servidores virtuales mediante un único equipamiento físico.
* El software encargado de realizar la abstracción de los recursos físico y de gestionar el acceso se denomina
  Hypervisor o VMM (Virtual Machine Monitor), existen dos tipos:
    * ``Tipo 1``, Hypervisor nativo (bare-metal): también denominado unhosted, permiten desplegarse directamente sobre
      el hardware y se trata de sistemas que en sí mismos ya son un pequeño SO con un núcleo que ya incorpora un
      hypervisor integrado que permite crear y administrar los accesos de los SO invitados a los recursos hardware, no
      se requiere contar con un SO anfitrión, es el propio Hypervisor el SO (VMWare ESXi, Hyper-V, Citrix, XenServer...)
      . Ofrecen prestaciones como mayor capacidad de procesamiento, posibilidad de migración de VM en caliente, balanceo
      de carga entre servidores,...
    * ``Tipo 2``, Hypervisor alojado (hosted): se necesita de un sistema operativo host en la máquina en la que se
      alojan, no se pueden desplegar directamente sobre el hardware necesitando de un SO en el host (Windows, Linux...)
      y sobre este se ejecuta el Hypervisor (VMWare Workstation, Oracle VirtualBox, QEMU...).

***

> Proxmox VE: entorno de virtualización de servidores de código abierto. Está en distribuciones GNU/Linux basadas en Debian con una versión modificada del Kernel RHEL y permite el despliegue y la gestión de máquinas virtuales y contenedores.

***

* Dentro de la ``virtualización de servidores`` destacan las ``técnicas``:
    * ``Virtualización de hardware/servidor``:
        * La técnica más usada permite ejecutar múltiples SO en las distintas máquinas virtuales que sean compatibles
          con la arquitectura hardware subyacente.
        * EL Hypervisor es el que administra los recursos traduciendo las peticiones de los sistemas invitados a
          solicitudes al sistema anfitrión, debe contar con los drivers necesarios para el acceso a los recursos
          físicos.
        * La virtualización de los recursos hardware por separado, creando un driver específico para cada recurso y por
          otro lado la creación de un micro kernel sobre el que funciona igualmente tanto el SO como las VMs.
        * Gracias al encapsulamiento e independencia de la VMs estas son gestionadas como ficheros dentro de la
          estructura de ficheros del SO, es posible mover y copiar una máquina virtual de un lugar a otro o guardarla en
          un USB hasta una SAN de una empresa.

    * ``Virtualización parcial o paravirtualización``:
        * Hypervisor ofrece a los SO invitados una interfaz especial, pueden acceder a los recursos físicos a través de
          llamadas al sistema denominadas hypercalls, lo que hace que tenga mejor rendimiento comparado con la
          virtualización completa.
        * Es necesario realizar una modificación en el SO invitado, permitiendo al sistema invitado realizar llamadas a
          los recursos de manera directa, acelerando el rendimiento de ejecución (esta modificación solo es posible en
          sistemas de software abierto como Solaris, Linux...).
        * A nivel interno, los SO se encuentran estructurados en capas o anillos (rings) donde el ring 0 es el más
          privilegiado y done se ejecuta el núcleo del SO como proceso más importante, dejando el ring 3, el menos
          privilegiado, para la ejecución de las aplicaciones.
        * Al virtualizar un SO, su núcleo no puede ejecutarse en el ring \=, por lo que se utiliza una técnica
          denominada “ring deprivileging” donde el SO es modificado para poder ejecutarse en el ring 1 dejando el ring 0
          para el Hypervisor.
        * Este tiene que recompilar continuamente el SO invitado para obligar a tosa las instrucciones a ejecutarse
          fuera del ring 0, lo que ralentiza la ejecución de las VMs.
        * La alternativa es la emulación del ring 0 completo, pero es  
          una solución muy lenta.
        * Para solucionar esto, Intel (Intel VT-x Vanderpool) y AMD (AMD-V) proporcionan ayuda por hardware, requiere la
          activación en BIOS e incrementa notablemente el rendimiento de la virtualización completa del hardware. (Ej:
          Xen, UML, OpenVZ...).
    * ``Virtualización de puestos de usuario``:
        * Se refiere a la virtualización del escritorio y aplicaciones de cada usuario. Separa el escritorio que utiliza
          un usuario respecto del equipo que manipula físicamente, el equipo del usuario conectará con un servidor
          centralizado de la organización donde se ejecutar su escritorio “VDI (Virtual Desktop Infrastructure)”.
        * Todas las aplicaciones, procesos y datos del usuario se almacenarán de forma centralizada, pudiendo acceder al
          escritorio desde cualquier dispositivo y cualquier lugar siempre que cuente con el cliente adecuado para
          conectar con el servidor, los componentes principales de este tipo de virtualización son:
            * ``Servidor de escritorios y aplicaciones``: ejecutan los distintos escritorios y/o aplicaciones de los
              usuarios, garantizando seguridad y aislamiento, se suele configurar un servidor de aplicaciones adicional
              que se ocupara de la ejecución de las distintas aplicaciones ofrecidas a los usuarios. En ambos casos se
              basan en sistemas operativos multiusuarios.
            * ``Equipo de acceso del usuario``: conecta con el servidor de escritorios y comunica cualquier cambio de
              pantalla que realice el usuario.
            * ``Red de comunicaciones``: garantiza la comunicación correcta entre los equipos de acceso del usuario y
              los servidores del escritorio.
            * ``Protocolos de comunicación``: según el tipo de escritorio a utilizar, protocolo “RDP” (Windows),
              protocolo “X Windows” (Linux), protocolos ICA, NX, VNC...
    * ``Virtualización de software``:
        * El SO anfitrión virtualiza el hardware a nivel del SO, permitiendo que varios sistemas invitados se ejecuten
          de manera autónoma en el mismo servidor físico accediendo por igual a todos los recursos del sistema.
        * Los servidores se virtualizan en la capa del SO (kernel) sin necesidad de un Hypervisor, se crean entornos
          virtuales (EV) asilados en un único servidor físico.
        * Existe una capa que se carga directamente en el servidor base, la siguiente capa superior muestra cada recurso
          hardware que debe virtualizarse.
        * A continuación, se encuentra la capa de virtualización (con un sistema de archivos propietario y una capa de
          abstracción de servidor de kernel) esta capa hace que cada uno de los contenedores aparezca como servidor
          autónomo, estos contenedores utilizan el mismo SO que el sistema anfitrión, mismas librerías, binarios y
          drivers, pero disponen de una estructura de directorios propia. (Ej: Virtuozzo).
*
* En función de la complejidad de la infraestructura puede haber un servidor que actúe de “bróker” siendo el
  intermediario entre el usuario y el servidor de escritorio, ejemplos: VMWare Horizon, XEN Desktop, Quindel...
  *``Dependiendo de donde se lleve a cabo la ejecución del escritorio``:
    * ``Modo centralizado``: los escritorios se ejecutan en un servidor centralizado, dos tipos:
    * ``Persistentes o estáticos``: asignado directamente a un usuario y que mantiene su configuración una vez cierra la
      sesión.
    * ``No persistentes o dinámicos``: una imagen maestra para todos los usuarios a la que se realiza un clon y se le
      asigna al usuario en el momento de iniciar sesión.
    * ``Modo alojado``: proveedor externo es el que ofrece el servicio de escritorio virtualizado con el requisito d
      contar con una conexión de red entre le equipo de usuario y el servidor alojado.
    * ``Modo remoto``: trabajar sin conexión de red al servidor de escritorios, se basa en realizar una copia del
      escritorio al equipo de usuario y este lo ejecuta sin necesidad de conexión a la red (principal inconveniente es
      la seguridad, una pérdida del equipo del usuario implica una pérdida de los datos almacenados).

* > ``Veeam Backup & Replication``: software de gestión de backup, recuperación ante desastres y gestión inteligente de datos para infraestructuras virtuales (VMWare), físicas y multicloud.
* > ``Acronis Cyber Backup``: solución de copia de seguridad para máquinas virtuales y hosts de Oracle VM Server.

#### 6.4. VIRTUALIZACIÓN DE SOFTWARE USANDO CONTENEDORES

* Este método permite la fácil creación de contenedores para la ejecución de aplicaciones, la idea central es crear un
  contenedor (un proceso para el SO) con aquellas librerías, archivos y configuraciones necesarias para la aplicación
  concreta, sin tener que instalar un SO completo de forma subyacente, se diferencia de una máquina virtual en que esta
  necesita contener todo el SO, mientras que un contenedor aprovecha el SO sobre el que se ejecuta. Las tres ventajas
  del uso de contenedores son:
    * ``Portabilidad``: se puede desplegar en cualquier otro sistema que soporte esta tecnología (que tenga instalado el
      software virtualizador).
    * ``Flexibilidad``: arranque de un contenedor supone el mismo tiempo que arrancar un proceso en el sistema, mientras
      que arrancar una máquina virtual implica más tiempo.
    * ``Ligereza``: al contener únicamente las dependencias necesarias para la ejecución de la aplicación ocupa mucho
      menos espacio.

##### 6.4.1. DOCKER

* Proyecto de código abierto que automatiza el despliegue de aplicaciones dentro de contenedores de software,
  proporcionando una capa adicional de abstracción y automatización de virtualización de aplicaciones en múltiples
  sistemas operativos.
* Docker utiliza características de aislamiento de recursos del kernel Linux, tales como cgroups (control groups:
  característica del kernel de Linux que limita, explica y aísla el uso de recursos de una colección de procesos) y
  namespaces (característica del kernel de Linux que divide los recursos del kernel de modo que un conjunto de procesos
  ve un conjunto de recursos mientras que otro conjunto de procesos ve un conjunto diferente de recursos), para permitir
  que "contenedores" independientes se ejecuten dentro de una sola instancia de Linux, evitando la sobrecarga de iniciar
  y mantener máquinas virtuales.
* El soporte del kernel Linux para los namespaces aísla la vista que tiene una aplicación de su entorno operativo,
  incluyendo árboles de proceso, red, ID de usuario y sistemas de archivos montados, mientras que los cgroups del kernel
  proporcionan aislamiento de recursos, incluyendo la CPU, la memoria, el bloque de E/S y de la red.
* Docker incluye la biblioteca “libcontainer” como su propia manera de utilizar directamente las facilidades de
  virtualización que ofrece el kernel Linux, además de utilizar las interfaces abstraídas de virtualización mediante
  libvirt, LXC (Linux Containers) y systemd-nspawn.
* Docker implementa una API de alto nivel para proporcionar contenedores livianos que ejecutan procesos de manera
  aislada.
* Usar Docker para crear y gestionar contenedores puede simplificar la creación de sistemas altamente distribuidos,
  permitiendo que múltiples aplicaciones, las tareas de los trabajadores y otros procesos funcionen de forma autónoma en
  una única máquina física o en varias máquinas virtuales.
* Esto permite que el despliegue de nodos se realice a medida que se dispone de recursos o cuando se necesiten más
  nodos, lo que permite una plataforma como servicio (PaaS) de estilo de despliegue y ampliación de los sistemas como
  Apache Cassandra, MongoDB o Riak.
* Docker también simplifica la creación y el funcionamiento de las tareas de carga de trabajo o las colas y otros
  sistemas distribuidos.
* Docker puede integrarse con Amazon Web Services, Microsoft Azure, Ansible, Jenkins...
* ``Comandos`` útiles en ``Docker``:
    * ``ps``: lista todos los contenedores en ejecución.
    * ``stop``: detiene la ejecucion de un contenedor.
    * ``search``: busca una imagen contenda en Docker.
    * ``builder``: gestiona builds.
    * ``config``: gestiona Docker configs.
    * ``container``: gestiona containers.
    * ``context``: gestiona contexts.
    * ``images``: lista y gestiona imagenes de sistema.
    * ``network``: gestiona networks.
    * ``swarm``: gestiona Swarm (permite agrupar una serie de hosts de Docker en un clúster y gestionar los clústeresde
      forma centralizada).
    * ``node``: gestiona Swarm nodes.
    * ``plugin``: gestiona plugins.
    * ``secret``: gestiona Docker secrets.
    * ``service``: gestiona services.
    * ``stack``: gestiona Docker stacks.
    * ``system``: gestiona Docker.
    * ``trust``: gestiona trust on Docker images.
    * ``volume``: gestiona volumenes.

##### 6.4.2. KUBERNETES

* Sistema de código libre para la automatización del despliegue, ajuste de escala y manejo de aplicaciones en
  contenedores, define un conjunto de bloques de construcción (primitivas) que conjuntamente proveen los mecanismos para
  el despliegue, mantenimiento y escalado de aplicaciones.
* Los componentes que forman Kubernetes están diseñados para estar débilmente acoplados pero a la vez ser extensibles
  para que puedan soportar una gran variedad de flujos de trabajo.
* La extensibilidad es provista en gran parte por la API de Kubernetes, que es utilizada por componentes internos así
  como extensiones y contenedores ejecutados sobre el mismo.
    * ``Cápsulas`` (Pods): la unidad básica de planificación, esta agrega un nivel de abstracción más elevado a los
      componentes en contenedores. Consta de uno o más contenedores en los que se garantiza su ubicación en el mismo
      equipo anfitrión y pueden compartir recursos. Cada pod en Kubernetes es asignado a una única dirección.
    * ``Etiquetas y selectores``: permite a los clientes (usuarios o componentes internos) vincular pares clave-valor (
      label)
      a cualquier objeto API en el sistema, como pods o nodos. Las etiquetas y los selectores son el mecanismo principal
      de agrupamiento en Kubernetes, y son utilizados para determinar los componentes sobre los cuales aplica una
      operación.
    * ``Controladores``: un controlador es un bucle de reconciliación que lleva al estado real del clúster hacia el
      estado deseado.
        * ``Replication Controller``: se encarga de la replicación y escala mediante la ejecución de un número
          especificado de copias de un pod a través de un clúster. También se encarga de crear pods de reemplazo si un
          nodo subyacente falla.
        * ``DaemonSet Controller``: se encarga de asegurar la ejecución de exactamente un pod en cada máquina (o algún
          subconjunto de máquinas).

    * ``Servicios``: conjunto de pods definidos por el selector de etiquetas. Kubernetes provee de un servicio de
      descubrimiento y enrutamiento de pedidos mediante la asignación de una dirección IP estable y un nombre DNS al
      servicio, y balancea la carga de tráfico en un estilo round-robin hacia las conexiones de red de las direcciones
      IP entre los pods que verifican el selector (incluso cuando fallas causan que los pods se muevan de máquina en
      máquina).  
      Por defecto un servicio es expuesto dentro de un cluster (por ejemplo, pods de un back end pueden ser agrupados en
      un servicio, con las peticiones de los pods de front end siendo balanceadas entre ellos), un servicio también
      puede ser expuesto hacia afuera del clúster.

##### 6.4.2.1. ARQUITECTURA Y MÓDULOS

* ``Kubernetes`` sigue una arquitectura maestro-esclavo. Los componentes de Kubernetes pueden ser divididos en aquellos
  que administran un nodo individual y aquellos que son partes de un panel de control:
    * ``etcd``: almacén de datos persistente, liviano, distribuido de clave-valor desarrollado por CoreOS que almacena
      de manera confiable los datos de configuración del clúster, representando el estado general del cluster en un
      punto del tiempo dado.
    * ``Servidor de API``: componente central que sirve a la API de Kubernetes, utiliza JSON sobre HTTP, que provee la
      interfaz interna y externa de Kubernetes. El servidor API procesa y valida las peticiones REST y actualiza el
      estado de los objetos API en etcd, permitiendo a los clientes configurar flujos de trabajos y contenedores a
      través de los nodos esclavos.
    * ``Planificador``: selecciona sobre qué nodo deberá correr un pod sin planificar (la unidad básica de manejo del
      planificador) basado en la disponibilidad de recursos; lleva la cuenta de la utilización de recursos en cada nodo
      para asegurar que un flujo de trabajo no es planificado en exceso de la disponibilidad de los recursos. En
      esencia, el rol del planificador es el de emparejar la oferta de un recurso con la demanda de un flujo de
      trabajos.
    * ``Administrador del controlador``: proceso sobre el cual el núcleo de los controladores Kubernetes como DaemonSet
      y Replication se ejecuta. Los controladores se comunican con el servidor API para crear, actualizar y eliminar
      recursos que ellos manejan (pods, servicios...).
    * ``Nodo Kubernetes``: el nodo, también conocido como esclavo o worker, es la máquina física o virtual donde los
      contenedores (flujos de trabajos) son desplegados. Cada nodo en el clúster debe ejecutar la rutina de tiempo de
      ejecución (como Docker), para comunicarse con el maestro para la configuración en red de estos contenedores.
    * ``Kubelet``: es responsable del estado de ejecución de cada nodo (es decir, asegurarse que todos los contenedores
      en el nodo se encuentran saludables). Se encarga del inicio, la detención y el mantenimiento de los contenedores
      de aplicaciones (organizados como pods) como es indicado por el panel de control. Monitorea el estado de un pod y,
      si no se encuentra en el estado deseado, el pod será desplegado nuevamente al mismo nodo. El estado del nodo es
      comunicado al maestro cada pocos segundos mediante una señal periódica (heartbeat). Una vez que el nodo detecta la
      falla de un nodo, el Replication Controller observa este cambio de estado y lanza pods en otros nodos sanos.
    * ``Kube-Proxy``: implementación de un proxy de red y balanceador de carga soportando la abstracción del servicio
      junto con otras operaciones de red. Responsable del enrutamiento de tráfico hacia el contenedor correcto basado en
      la dirección IP y el número de puerto.
    * ``cAdvisor``: es un agente que monitorea y recoge métricas de utilización de recursos y rendimiento como CPU,
      memoria, uso de archivos y red de los contenedores en cada nodo.
    * ``Módulos básicos de Kubernetes``: en forma práctica y general se describe a continuación lacreación y
      administración de cápsulas (Pods).
    * ``Clúster de Kubernetes``: coordina un grupo de computadoras de alta disponibilidad que están conectadas para
      funcionar como una sola unidad. Las abstracciones en Kubernetes le permiten implementar aplicaciones en
      contenedores en un clúster sin vincularlas específicamente a máquinas individuales.
    * ``Despliegue de una aplicación``: se puede crear y administrar una implementación utilizando la interfaz de línea
      de comandos “Kubectl”, que utiliza la API de Kubernetes para interactuar con el clúster. Cuando se crea una
      implementación, se deberá especificar la imagen del contenedor para su aplicación y el número de réplicas que se
      desean ejecutar. Se puede cambiar esa información más adelante actualizando su implementación.
    * ``Exploración de aplicaciones``: al crear una implementación, Kubernetes crea un Pod para alojar su instancia de
      aplicación. Un Pod es una abstracción de Kubernetes que representa un grupo de uno o más contenedores de
      aplicaciones (
      como Docker o rkt), y algunos recursos compartidos para esos contenedores.
    * ``Mantenimiento de los Pods``: los pods tienen un ciclo de vida. Cuando un nodo trabajador "muere", los pods que
      se ejecutan en el nodo también se pierden. Luego, un controlador de replicación puede hacer que el clúster regrese
      dinámicamente al estado deseado mediante la creación de nuevos pods para mantener su aplicación en ejecución.
    * ``Ampliación de aplicaciones``: al crear un despliegue se expone públicamente a través de un servicio. La
      implementación creó solo un pod para ejecutar nuestra aplicación. Cuando el tráfico aumenta, se debe escalar (
      aumentar en recursos y número) la aplicación para satisfacer la demanda de los usuarios.
    * ``Actualización de aplicaciones``: las actualizaciones continuas permiten que la actualización de implementaciones
      tenga lugar sin tiempo de inactividad al actualizar incrementalmente las instancias de pods con otras nuevas. Los
      nuevos Pods serán programados en Nodos con recursos disponibles.

## TEMA 3 – MODELOS OSI/TCP-IP, PROTOCOLOS Y ACCESIBILIDAD

### 1\. ARQUITECTURA DE INTERNET

* Organizaciones y comités que supervisan el funcionamiento de internet:
    * ``Internet Engineeiring Task Force`` (IETF): comunidad de diseñadores de red, operadores, vendedores e
      investigadores interesados en la evolución de la arquitectura de internet, así como en su adecuado funcionamiento,
      es quien crea grupos de trabajo para desarrollar nuevas especificaciones.
    * ``Internet Engineering Steering Group`` (IESG): encargado de hacer avanzar una propuesta por las diferentes fases
      de aprobación, hasta llegar al estado de “estándar de internet”.
    * ``Internet Architecture Board`` (IAB): grupo de supervisión técnica de la ISOC, se encarga de la publicación de
      documentos RFCs entre otros.
    * ``Internet Society`` (ISOC): organización no gubernamental internacional que promociona la cooperación global y la
      coordinación para Internet de las tecnologías de red y las aplicaciones.
    * ``Internet Research Task Force`` (IRTF): grupos que se centran en la realización de investigación en protocolos,
      aplicaciones, arquitectura y tecnologías de Internet.
    * ``Asignación de direcciones IP y servicios de registro de dominios``:
    * ``Assigned Numbers Authority`` (IANA): fue autorizada por la ISOC para coordinar la asignación de los
      identificadores en Internet, como nombres de domino, números de sistema autónomo, direcciones IP, números de
      protocolo y de puerto. Coordino la creación del ``Internet Network Information Center`` (InterNIC) responsable de
      gestionar los nombres de dominio de Internet de máximo nivel (“.com”, “.org”, “.net”).
    * ``Internet Corporation for Assigned Names and Numbers`` (ICANN): tomo la responsabilidad de las funciones que
      previamente tenía IANA, también coordina el sistema de servidores rais de Internet y mantiene la estabilidad
      operativa en Internet.
* Tomar responsabilidad global de la asignación del espacio de direcciones IP, de los parámetros de protocolo, la
  administración de los DNS y la gestión de los sistemas servidores raíz.
* Distribuye espacio de direccionamiento de forma jerárquica y delega la responsabilidad de la asignación local en
  organizaciones regionales denominadas ``Regional Internet Registries`` (RIR): ARIN, RIPE, APNIC (AFRINIC, LACNIC) (
  “Red.es” es una entidad pública empresarial adscrita al ministerio de Industria, Energía y Turismo encargada de
  impulsar el desarrollo de la sociedad de la información en España).

### 2\. MODELO OSI (Open Systems Interconnection)

* En lugar de implementar toda la lógica necesaria para llevar a cabo la comunicación entre dos dispositivos en un único
  modulo, el problema se divide en funciones, cada una de las cuales se realiza por separado.
* En una arquitectura de protocolos, los distintos módulos se disponen en forma de “pila”. Cada capa de la pila realiza
  un conjunto de tareas relacionadas entre sí, cada capa proporciona un conjunto de servicios a la capa inmediatamente
  superior y utiliza los servicios de la inmediatamente inferior.

* Es un modelo de referencia para los protocolos de la red que tiene por objetivo conseguir interconectar sistemas de
  procedencia distinta para que estos pudieran intercambiar información sin ningún tipo de impedimentos debido a los
  protocolos con los que estos operaban de forma propia según su fabricante. El modelo OSI está conformado por 7 capas o
  niveles de abstracción.
* Cada uno de estos niveles tendrá sus propias funciones para que en conjunto sean capaces de poder alcanzar su objetivo
  final.
* Precisamente esta separación en niveles hace posible la intercomunicación de protocolos distintos al concentrar
  funciones específicas en cada nivel de operación.
* Lo que realmente hace OSI es definir la funcionalidad de ellos para conseguir un estándar.
* Entre cada par de capas adyacentes dentro de la misma entidad, existe una interfaz que define cuales son las
  operaciones y servicios que la capa ofrece a la capa superior, dichas capas se comunican intercambiando bloques de
  datos, denominados ``PDU`` (Protocol Data Unit).
* Deben ser fragmentadas y envidas en varias PDU de nivel N-1 en el origen, dichos fragmentos recibidos por la capa N-1
  en el destino deben ser reensamblados antes de pasarlos a la capa N.
* El modelo se basa en la distribución de la funcionalidad de las comunicaciones en capas, cada capa realiza un
  subconjunto de tareas, relacionadas entre sí, cada capa hace uso de las funciones “primitivas” proporcionadas por su
  capa inmediatamente inferior y proporciona servicios a su capa inmediatamente superior.
* Las capas permiten que un cambio en un protocolo de una capa no afecte a los protocolos del resto,
* ``OSI`` consta de ``7 capas``:
    * ``CAPA FÍSICA``: La capa física define las especificaciones eléctricas, mecánicas, de  
      procedimiento y funcionales para activar, mantener y desactivar el enlace físico entre sistemas finales. Son
      estándares de capa física:

        * ``EIA/TIA-232`` (norma para el intercambio de datos binarios serie entre un DTE \[Data Terminal Equipment\]
          como por ejemplo un equipo de usuario, y un DCE \[Data Communication Equipment\], por ejemplo un módem).
        * ``V.35`` (estándar de ITU-T para comunicaciones síncronas entre un dispositivo de acceso a la red y una red de
          paquetes).
        * ``Ethernet`` (opera en las dos capas inferiores del modelo OSI, la capa de enlace de datos y la capa física.
          En la Capa 1 implica señales, streams de bits que se transportan en los medios, que transmiten las señales a
          los medios y distintas topologías).
        * ``Bluetooth`` (especificación industrial para redes inalámbricas de área personal “WPAN”)...

        * ``Medios de transmisión``: componen el canal por el cual enviamos datos, puede ser medio guiado, la señal
          puede ser eléctrica (cable coaxial y par trenzado) u óptica (fibra óptica), o medio no guiado, se utilizan
          señales radioeléctricas, se propagan por el espacio. Cuando se transmite una señal sobre un medio de
          transmisión, se observan distintos efectos negativos sobre la señal:
            * ``Atenuación``: cualquier señal al propagarse por un medio de transmisión pierde potencia y se atenúa con
              la distancia (en el caso del cable de cobre se debe fundamentalmente a la resistencia del cable que
              provoca perdida en forma de calor; en el caso de la fibra óptica se debe a la absorción de luz por parte
              del medio físico).
            * ``Interferencia``: algunos medios son susceptibles de recibir interferencias electromagnéticas, la
              diafonía es un tipo particular de interferencia, se produce entre señales que discurren por medios
              paralelos, los pares trenzados, por ejemplo, entre las señales de ida y vuelta o entre las señales de
              distintos abonados.
            * ``Ruido``: es una perturbación en la señal analógica o digital que puede distorsionar la información
            * ``Desfase``: una onda electromagnética se propaga a una velocidad, si no es exactamente la misma en todas
              las frecuencias se da el desfase.
            * ``Dispersión``: la señal tiende a descomponerse.
        * Dentro de los medios guiados hay ``cuatro tipos`` principales de ``medios de transmisión``: par trenzado no
          blindado (UTP), par trenzado blindado/apantallado (STP), cable coaxial y fibra óptica.
            * ``Cable coaxial``: presentan unas características comunes, núcleo de cobre, aislamiento plástico, blindaje
              de malla de cobre (evita que los datos generen interferencias en el exterior), revestimiento exterior.
            * ``RG-58`` (thinnet): cable coaxial de 50 ohmios utilizado en redes 10-BASE-2.
            * ``RG-59``: cable coaxial de 75 ohmios utilizado en sistemas de TV por cable.
            * ``RG-6U``: cable coaxial de 75 ohmios instalado en viviendas, capaz de transmitir frecuencias de satélite,
              HD TV o cable-modem.
            * ``Cable de par trenzado``: más ampliamente utilizado debido al menor coste del cable y la facilidad de
              instalación.
                * ``UTP``: presenta la mejor relación calidad/precio, la instalación es muy sencilla y su rendimiento se
                  incrementa continuamente, tiene habitualmente una cubierta externa de material aislante, contiene
                  cuatro pares de hilos de cobre, recubiertos (cada hilo) de material aislante.

                * ``STP``: son sustancialmente más caros que UTP, su principal ventaja es su menor susceptibilidad a
                  interferencias electromagnéticas

                  | Cat. 5 | 100Mbps | 100MHz |
                  | :---- | :---- | :---- |
                  | Cat. 5e | 1Gbps | 100MHz |
                  | Cat. 6 | 1Gbps | 250MHz |
                  | Cat. 6a | 10Gbps | 500MHz |
                  | Cat. 7 | 10Gbps | 600MHz |
                  | Cat. 7a | 10Gbps | 1000MHz |
                  | Cat. 8 | 40Gbps | 2000MHz |

            * ``Fibra óptica``: 2 hebras de vidrio o plástico (una de transmisión y otra de recepción), existen dos
              variantes:
                * ``Monomodo``: utilizada por los proveedores de servicios de comunicaciones en sus enlaces
                  intercontinentales y en redes de campus o área local. El haz de luz no rebota en el “cladding”, las
                  longitudes de onda típicas son 1.310 y 1.550 nanómetros.
                * ``Multimodo``: es utilizada en tecnologías como FDDI, Gigabit y 10 Gigabit Ethernet, 10-BASE-FL Y
                  100-BASE-F (
                  habitualmente dentro de un edificio) permite la transmisión de más de un nodo de luz a través del
                  cable. Las longitudes de onda típicas van de 850 a los 1.300 nanómetros.

        * ``Medidas reflectométricas``: permiten detectar causas de problemas de comunicación posteriores debidas a un
          mal diseño o instalación. Pruebas en el cableado de cobre:

            * ``Reflectometría en el Dominio del Tiempo``: se basa en transmitir una señal por un cable y analizar su
              reflejo.
            * ``Longitud del cable``: permite detectar pares abiertos, cortocircuitos o roturas en el cable.
            * ``Mapeo de hilos`` (Wire Mapping): consiste en verificar que cada hilo individual del cable está conectado
              al pin del conector adecuado. (problemas típicos: cortocircuito de par, par invertido, par cruzado...).

        * Rendimiento (las pruebas relatadas en los apartados anteriores son las pruebas básicas mínimas que permiten
          garantizar que la red funciones, para categorizar y certificar, se llevan a cabo las siguientes):
            * ``Impedancia``:
                * Pérdida de retorno estructural (Structural Return los, SRL).
                * Pérdida de retorno (Return Loss, RL).
            * ``Atenuación``: mide la degradación de la señal que atraviesa el cable, se mide en dB.
            * ``Diafonía próxima`` (Near-End Crosstalk, NEXT): se mide emitiendo una señal sobre un par del cable y
              midiendo la señal generada (señal de crosstalk) en el resto de pares del cable, en dB.
            * ``Atenuación/NEXT`` (Attenuation to near Crosstalk Ratio, ACR): mide la relación señal/ruido en dB.
            * ``Diafonía lejana`` (Far-End Crosstalk, FEXT): se mide emitiendo una señal sobre un par del cable y
              midiendo la señal generada (señal de crosstalk o diafonía) en el resto de pares del cable en el extremo
              del cable alejado del transmisor.
            * ``Ruido``: interferencias electromagnéticas (EMI).

        * ``Pruebas en Fibra Óptica``: en inmune a las interferencias generadas por el “crosstalk”, EMI y RFI. Suelen
          llevarse a cabo dos pruebas, utilizando un ``Reflectómetro en el Dominio del Tiempo Óptico`` (
          OTDR):
            * ``Potencia Óptica``: prueba fundamental, determina la fortaleza de la señal que atraviesa el cable, base
              para medir la pérdida o atenuación de la señal. En fibra multimodo se realizan con longitud de onda de 850
              y 1300 nm, mientras que en monomodo habitualmente solo se utiliza la de 1300 nm.
            * ``Pérdida o atenuación``: es el decremento de fortaleza de la luz que atraviesa una fibra óptica. La
              atenuación esta mas relaz8ionado con empalmes y conexiones que con la longitud del cable, verifica que los
              cables y los conectores se han instalado correctamente. Consiste en medir la potencia óptica de una fuente
              de luz calibrada que genera un pulso y medir cuata señal (potencia óptica también) llega al otro extremo
              del cable. La combinación del generador de luz y el medidor de potencia se denomina
              “``Optical Loss Test Set`` (
              OLTS)”.
            * ``Reflectómetros en el Dominio del Tiempo Ópticos``: dispositivo que transmite un pulso calibrado sobre el
              cable que va a ser probado y monitoriza la señal que retorna, mide la señal retornada por el efeto de
              “dispersión de retorno” (
              blackscatter).

        * ``Medios de transmisión no guiados``:

            * ``Radiofrecuencia`` (RF): se consideran las ondas electromagnéticas con frecuencias en el rango de 3KHz
              hasta 300 GHz, utilizadas para las comunicaciones en televisión, radio, telefónico móvil... Una antena se
              coloca en una zona en la que se percibe un cierto campo electromagnético genera como respuesta a esta una
              corriente eléctrica, los parámetros de una antena que más influyen son: la longitud de onda, potencia de
              la antena en transmisión, calidad de receptor, tamaño y altura de la antena, modo de transmisión, ruido y
              señales de interferencia. Algunas de las tecnologías inalámbricas más utilizadas son:
                * ``Microondas``: están constituidas por radiación electromagnética con longitudes de onda que varían de
                  un metro a un milímetro, sus frecuencias oscilan entre 300 MHz y 300 GHz, una banda inmensa en la que
                  se incluyen entre otras tecnologías y bandas de UHF a EHF:
                  WiFI, WIMAX, Bluetooth... En telefonía móvil en España se emplean las bandas de microondas:
                    * 900 MHz y 1800 MHz para 2G.
                    * 900 MHz y 2100 MHz para 3G.
                    * 800 MHz y 1800 MHz para 4G.
                    * 700 MHz, 1500-3600 MHz y 2600 MHz para 5G.
            * ``Infrarrojos``: la radiación IR es una forma de radiación electromagnética, su banda de frecuencias va
              desde 430 THz hasta los 300 GHz, se utiliza fundamentalmente en telecomunicaciones para transmisiones de
              corto alcance entre periféricos, se utiliza el estándar IrDA (Infrared Data Association), utiliza diodos
              emisores de luz infrarroja (LED)
              para emitir radiación infrarroja, el haz se modula para evitar la interferencia de otras fuentes de
              infrarrojos como la luz solar o la iluminación artificial. Son útiles para uso en interiores en áreas de
              alta densidad de población, IR no penetra las paredes. También se utiliza para proporcionar la luz para
              sistema de comulaciones de fibra óptica. La luz infrarroja con una longitud de onda de alrededor de 1330
              nm o 1550 nm son las mejores opciones para fibra óptica.

    * ``CAPA ENLACE DE DATOS``:
        * La tarea principal de la capa de enlace de datos es tomar una transmisión de datos y transformarla en una
          extracción libre de errores de transmisión para la capa de red.
        * Logra esta función dividiendo los datos de entrada en marcos de datos (de unos cuantos cientos de bytes),
          transmite los marcos en forma secuencial y procesa los marcos de estado que envía el nodo destino.
        * Proporciona un servicio de transmisión de datos fiable a través del enlace físico, envía los datos en forma de
          bloques de bits (tramas), se ocupa del direccionamiento físico, la topología de red, el acceso a la red, la
          notificación de errores, entrega ordenada de tramas y control de flujo.
        * El dispositivo que usa la capa de enlace es el Switch que se encarga de recibir los datos del enrutador y
          enviar cada uno de estos a sus respectivos destinatarios.
        * Esta capa se divide en ``dos subcapas``:
            * ``MAC``: constituye la subcapa inferior de la capa de enlace de datos. La MAC se  
              implementa mediante hardware, por lo general, en la NIC de la PC.
            * ``LLC``: se ocupa de la comunicación entre las capas superiores y las capas inferiores. Generalmente, esta
              comunicación se produce entre el software de red y el hardware del dispositivo.
                * La subcapa LLC toma los datos del protocolo de la red, que generalmente son un paquete IPv4, y agrega
                  información de control para ayudar a entregar el paquete al nodo de destino.
                * En un PC, el LLC se puede considerar el controlador de la NIC.
                * El controlador de la NIC es un programa que interactúa directamente con el hardware de la NIC para
                  transmitir los datos entre la subcapa MAC y los medios físicos.

        * > La ``CAPA DE ENLACE DE DATOS`` proporciona control de errores en el envío de tramas entre computadoras, y provee el control de la capa física, se realiza mediante diversos tipos de códigos como:
            * > CRC (Cyclic Redundancy Check): código de detección de errores usado frecuentemente en redes digitales y en dispositivos de almacenamiento para detectar cambios accidentales en los datos. Los bloques de datos ingresados en estos sistemas contienen un valor de verificación adjunto, basado en el residuo de una división de polinomios; el cálculo es repetido, y la acción de corrección puede tomarse en contra de los datos presuntamente corruptos en caso de que el valor de verificación no concuerde.
            * > Checksum: función de redundancia que tiene como propósito principal detectar cambios accidentales en una secuencia de datos para proteger la integridad de estos, verificando que no haya discrepancias entre los valores obtenidos al hacer una comprobación inicial y otra final tras la transmisión.
            * > Paridad: comprueba que el dato ha llegado correctamente mediante el uso de un “bit de paridad”.

        * ``Son estándares de capa de enlace de datos``:
            * ``HDLC`` (High-Level Data Link Control): protocolo de comunicaciones de propósito general punto a punto.
              Proporciona recuperación de errores en caso de pérdida de paquetes de datos, fallos de secuencia y otros,
              por lo que ofrece una comunicación confiable entre el transmisor y el receptor.
            * ``PPP`` (Point-to-Point Protocol): establecer una conexión directa entre dos nodos de una red. Conecta dos
              enrutadores directamente sin ningún equipo u otro dispositivo de red entre medias de ambos. Puede
              proporcionar autenticación, cifrado de la transmisión1 y compresión.
            * ``Frame Relay``: técnica de comunicación mediante retransmisión de tramas para redes de circuito virtual,
              consiste en una forma simplificada de tecnología de conmutación de paquetes que transmite una variedad de
              tamaños de tramas o frames para datos, perfecto para la transmisión de grandes cantidades de datos.
              Permite la interconexión de redes de área local separadas geográficamente a un coste menor.
            * ``Token Ring`` (IEEE 802.5): arquitectura de red con topología lógica en anillo y técnica de acceso de
              paso de testigo.
                * Define una red de área local LAN en configuración de anillo (Ring), con método de paso de testigo como
                  control de acceso al medio.
                * El testigo es una trama que circula por el anillo en su único sentido de circulación.
                * Cuando una estación desea transmitir y el testigo pasa por ella, lo toma. Este sólo puede permanecer
                  en su poder un tiempo determinado (10 ms).
                * Tienen una longitud de 3 bytes y consiste en un delimitador de inicio, un byte de control de acceso y
                  un delimitador de fin.
                * En cuanto a las tramas de comandos y de datos pueden variar en tamaño, dependiendo del tamaño del
                  campo de información.
                * Las tramas de datos tienen información para protocolos mayores, mientras que las tramas de comandos
                  contienen información de control.
            * ``FDDI`` (Fiber Distributed Data Interface): conjunto de estándares ISO y ANSI para la transmisión de
              datos en redes de computadoras de área extendida (WAN) o de área local (LAN), mediante cables de fibra
              óptica. Se basa en la arquitectura Token Ring y permite una comunicación tipo dúplex (
              completo).
            * ``Ethernet`` (IEEE 802.3): estándar de redes de área local para computadoras, define las características
              de cableado y señalización; de nivel físico y los formatos de tramas de datos del nivel de enlace de datos
              del modelo OSI. Permite alimentación mediante ``PoE`` (Power over Ethernet):
                * ``af``: 15.4W (POE)
                * ``at``: 25.5W (POE+)
                * ``bt``: 60W (tipo3) 100W (tipo 4\) (POE++)

            * La diferencia entre PoE pasivo y activo es que el pasivo no se adhiere a los estándares IEEE. Negocian y
              suministran la energía de forma diferente.
            * A continuación se especifican los anteriores conceptos en las tecnologías más importantes:

              | Tecnología  | Velocidad     | Distancia / Medio                      |
              | :----------- | :------------ | :------------------------------------ |
              | 10BaseT      | 10 Mbit/s     | 100 m / Par trenzado                  |
              | 10Base2      | 10 Mbit/s     | 185 m / Coaxial delgado              |
              | 10Base5      | 10 Mbit/s     | 500 m / Coaxial grueso               |
              | 10BaseF      | 10 Mbit/s     | 2000 m / Fibra óptica                |
              | 100BaseT4    | 100 Mbit/s    | 100 m / Par trenzado (Cat 3)         |
              | 100BaseTX    | 100 Mbit/s    | 100 m / Par trenzado (Cat 5)         |
              | 100BaseFX    | 100 Mbit/s    | 2000 m / Fibra óptica                |
              | 1000BaseT    | 1000 Mbit/s   | 100 m / Par trenzado (Cat 5e o 6)    |
              | 1000BaseTX   | 1000 Mbit/s   | 100 m / Par trenzado (Cat 6)         |
              | 1000BaseSX   | 1000 Mbit/s   | 550 m / Fibra óptica (multimodo)     |
              | 1000BaseLX   | 1000 Mbit/s   | 5000 m / Fibra óptica (monomodo)     |
              | 10000BaseT   | 10000 Mbit/s  | 100 m / Par trenzado (Cat 6a o 7)    |
              | 10000BaseSR  | 10000 Mbit/s  | 300 m / Fibra óptica (multimodo)     |
              | 10000BaseLR  | 10000 Mbit/s  | 10000 m / Fibra óptica (monomodo)    |

            * ``ATM`` (Asynchronous Transfer Mode): protocolo para el transporte de una gama completa de tráfico de
              usuarios, incluidas las señales de voz, datos y video. Proporciona una funcionalidad similar tanto a la
              conmutación de circuitos como a las redes de conmutación de paquetes: ATM utiliza multiplexación por
              división de tiempo asincrónica y codifica datos en paquetes pequeños de tamaño fijo llamados celdas.
            * ``ARP`` (Address Resolution Protocol): responsable de encontrar la dirección de hardware (
              Ethernet MAC) que corresponde a una determinada dirección IP. Para ello se envía un paquete (
              ARP request) a la dirección de difusión de la red que contiene la dirección IP por la que se pregunta, y
              se espera a que esa máquina (u otra) responda (ARP reply) con la dirección Ethernet que le corresponde. En
              Ethernet, la capa de enlace trabaja con direcciones físicas. El protocolo ARP se encarga de traducir las
              direcciones IP a direcciones MAC (direcciones físicas). Para realizar esta conversión, el nivel de enlace
              utiliza las tablas ARP, cada interfaz tiene tanto una dirección IP como una dirección física MAC.

            * > RARP es un protocolo para obtener la dirección IP perteneciente a un determinado hardware electrónico que se encuentra en la mayoría de las veces en una red Ethernet. RARP utiliza el mismo mecanismo que ARP. La respuesta que se devuelve de una solicitud es la dirección de protocolo de la estación origen, no la dirección de la estación destino de la solicitud. Para poder usar RARP, todas las direcciones MAC deben estar configuradas en un servidor central para que transfiera una dirección IP. El RARP además de encontrarlo en las redes Ethernet, está disponible en otras redes de área local como lo son la Interfaz de Fibra de Distribución de Datos y las redes LAN Token Ring.

            * ``STP`` (Spanning Tree Protocol): en algunos puentes pueden realizarse mapeos estáticos “Dirección MAC \-
              Puerto”, el mecanismo habitual para crear la tabla de conmutaciones el aprendizaje dinámico. En una red
              con caminos físico redundante se producen fenómenos como las tormentas de difusión, inestabilidad en las
              tablas de conmutación y la generación de tráfico únicas residual que degradan el rendimiento de la misma
              hasta bloquearla completamente. Con el objetivo de definir la arquitectura de protocolos para puentes
              basados en MAC, se desarrolla el estándar IEEE 802.1D, en él se define el uso del algoritmo de árbol de
              expansión (
              Spanning-tree protocol, STP) como mecanismo necesario para la selección de caminos lógicos únicos. Y
              evitar así los efectos negativos de la redundancia. El algoritmo transforma una red física con forma de
              malla, en la que existen bucles, por una red lógica en forma de árbol (
              libre de bucles). Los puentes se comunican mediante mensajes de configuración llamados Bridge Protocol
              Data Units (BPDU).
            * ``LACP`` (Link Aggregation Control Protocol): La agregación virtual de enlaces, también llamada trunking,
              es una característica de nivel 2, que une puertos físicos de la red en un único enlace de datos de gran
              ancho de banda; de este modo se aumenta la capacidad de ancho de banda y se crean enlaces redundantes y de
              alta disponibilidad. Si falla un enlace, la carga se redistribuye entre los enlaces restantes, con lo que
              el funcionamiento es continuo. Gracias a la capacidad de “Distributed Multilink Trunking”, el fallo o la
              eliminación de una unidad de la pila no causará la caída de todo un trunk.

    * ``CAPA DE RED``:
        * Proporciona conectividad y selección de ruta entre dos sistemas de hosts que pueden estar ubicados en redes
          geográficamente distintas, su misión es conseguir que los datos lleguen desde el origen al destino y para la
          consecución de su tarea, puede asignar direcciones de red únicas, interconectar subredes distintas, encaminar
          paquetes, utilizar un control de congestión y control de errores. Su PDU son los “paquetes” Hay dos formas en
          las que el nivel de red puede funcionar internamente:
            * ``Datagramas``: cada paquete se encamina independientemente, sin que el origen y el destino tengan que
              pasar por un establecimiento de comunicación previo.
            * ``Circuitos virtuales``: dos equipos que quieran comunicarse tienen que empezar por establecer una
              conexión. Durante este establecimiento de conexión, todos los routers que haya por el camino elegido
              reservarán recursos para ese circuito virtual específico.

        * Los dispositivos que facilitan tal tarea se denominan routers, trabajan en esta capa, aunque pueden actuar
          como switch de nivel 2 en determinados casos, dependiendo de la función que se le asigne. Los firewalls actúan
          sobre esta capa principalmente, para descartar direcciones de determinadas máquinas o limitar el acceso a
          ciertas de ellas.  
          En este nivel se realiza el direccionamiento lógico y la determinación de la ruta de los datos hasta su
          receptor final mediante los protocolos de capa de red, que se pueden clasificar en:
        * ``Protocolos de enrutamiento`` (permiten la selección de rutas):
            * Pueden ser orientados a vector-distancia (calculan las rutas utilizando el algoritmo de Bellman-Ford. En
              los protocolos de este tipo, ningún enrutador tiene información completa sobre la topología de red. En
              lugar de ello, se comunica con los demás routers, enviando y recibiendo información sobre las distancias
              entre ellos):
                * ``RIP`` (Routing Information Protocol): protocolo de puerta de IGP (Interior Gateway Protocol)
                  , utilizado por los routers o encaminadores para intercambiar información acerca de redes del Internet
                  Protocol (IP) a las que se encuentran conectados. Está basado en el vector de distancia, ya que
                  calcula la métrica o ruta más corta posible hasta el destino a partir del número de "
                  saltos" o equipos intermedios que los paquetes IP deben atravesar. El límite máximo de saltos en RIP
                  es de 15, de forma que al llegar a 16 se considera una ruta como inalcanzable o no deseable. RIP es un
                  protocolo libre, fácil de configurar y simple.

                * > ``RIPng``: para el enrutamiento IPv6, use RIPng (next gen). El RIPng usa el puerto ``UDP 521`` para enviar actualizaciones a las tablas de enrutamiento.

                * ``IGRP`` (Interior Gateway Routing Protocol): protocolo propietario de Cisco, basado en la tecnología
                  vector-distancia. Utiliza una métrica compuesta para determinar la mejor ruta basándose en el ancho de
                  banda, el retardo, la confiabilidad y la carga del enlace. El concepto es que cada router no necesita
                  saber todas las relaciones de ruta/enlace para la red entera, este publica destinos con una distancia
                  correspondiente y el router que recibe la información, ajusta la distancia y la propaga a los routers
                  vecinos. La información de la distancia en IGRP se manifiesta de acuerdo a la métrica. Esto permite
                  configurar adecuadamente el equipo para alcanzar las trayectorias óptimas. IGRP es un protocolo con
                  clase, lo que significa que no pueden manipularse las máscaras de red (utiliza las máscaras por
                  defecto de cada clase). Actualmente se usa EIGRP.
                * ``EIGRP`` (Enhanced Interior Gateway Routing Protocol): protocolo de encaminamiento de vector
                  distancia, propiedad de Cisco. Se considera un protocolo avanzado que se basa en las características
                  normalmente asociadas con los protocolos del estado de enlace. Algunas de las mejores funciones de
                  OSPF, como las actualizaciones parciales y la detección de vecinos, se usan de forma similar con
                  EIGRP. Aunque no garantiza el uso de la mejor ruta, es bastante usado porque mejora las propiedades de
                  convergencia y opera con mayor eficiencia que IGRP. Esto permite que una red tenga una arquitectura
                  mejorada y pueda mantener las inversiones actuales en IGRP.
                * ``BGP`` (Border Gateway Protocol): protocolo mediante el cual se intercambia  
                  información de encaminamiento entre sistemas autónomos. Entre los sistemas  
                  autónomos de los ISP se intercambian sus tablas de rutas a través del protocolo BGP. Este intercambio
                  de información de encaminamiento se hace entre los routers externos de cada sistema autónomo, los
                  cuales deben ser compatibles con BGP. Se trata del protocolo más utilizado para redes con intención de
                  configurar un EGP (Exterior Gateway Protocol). Pueden ser orientados a enlace-estado (cada nodo posee
                  información acerca de la totalidad de la topología de red. De esta manera, cada uno puede calcular el
                  siguiente salto a cada posible nodo destino de acuerdo a su conocimiento sobre cómo está compuesta la
                  red):

                    * ``OSPF`` (Open Shortest Path First): protocolo de red para encaminamiento jerárquico de IGP que
                      usa el algoritmo Dijkstra, para calcular la ruta más corta entre dos nodos. Construye una base de
                      datos enlace-estado idéntica en todos los routers de la zona, puede operar con seguridad usando
                      MD5 para autenticar sus puntos antes de realizar nuevas rutas y antes de aceptar avisos de
                      enlace-estado. OSPF puede usar tanto multidifusiones (multicast) como unidifusiones (unicast) para
                      enviar paquetes de bienvenida y actualizaciones de enlace-estado. Las direcciones de multidifusión
                      usadas son 224.0.0.5 y 224.0.0.6. Al contrario que RIP o BGP, OSPF no usa ni TCP ni UDP, sino que
                      se encapsula directamente sobre el protocolo IP. Una red OSPF se puede descomponer en regiones (
                      áreas) más pequeñas. Hay un área especial llamada área backbone que forma la parte central de la
                      red a la que se encuentran conectadas el resto de áreas de la misma. Las rutas entre las
                      diferentes áreas circulan siempre por el backbone, por lo tanto todas las áreas deben conectar con
                      el backbone. Si no es posible hacer una conexión directa con el backbone, se puede hacer un enlace
                      virtual entre redes.
                    * ``IS-IS`` (Intermediate System to intermediate System): protocolo de estado de enlace que maneja
                      un mapa para enrutar paquetes mediante la convergencia de la red. Permite a sistemas intermedios (
                      IS’s)dentro de un mismo dominio cambiar su configuración e información de ruteo para facilitar la
                      información de encaminamiento y funciones de transmisión de la capa de red. El protocolo de
                      encaminamiento IS-IS está pensado para soportar encaminamiento en grandes dominios consistentes en
                      combinaciones de muchos tipos de subredes. Esto incluye enlaces punto a punto, enlaces multipunto,
                      subredes X.25, subredes broadcast...

                * > ``X.25`` es un estándar ITU-T para redes WAN de conmutación de paquetes. Su protocolo de enlace es LAPB (Link Access Procedure, Balanced), establece mecanismos de direccionamiento entre usuarios, negociación de características de comunicación, técnicas de recuperación de errores. X.25 está orientado a conexión y trabaja con circuitos virtuales tanto conmutados como permanentes. En la actualidad se trata de una norma obsoleta.

        * ``Protocolos para el control e intercambio de información entre router``:

            * ``IGMP`` (Internet Group Management Protocol): se utiliza para intercambiar información acerca del estado
              de pertenencia entre enrutadores IP que admiten la multidifusión y miembros de grupos de multidifusión.
              Los hosts miembros individuales informan acerca de la pertenencia de hosts al grupo de multidifusión y los
              enrutadores de multidifusión sondean periódicamente el estado de la pertenencia. Su objetivo que tiene es
              describir las principales funcionalidades de gestión de grupos en Internet, así como el formato de sus
              mensajes. Es usado principalmente para optimizar el rendimiento de la red y en los que sea necesaria las
              transmisiones de multidifusión en redes IPv4.
            * ``ICMP`` (Internet Control Message Protocol): utilizado para enviar mensajes de error e información
              operativa indicando, por ejemplo, que un host no puede ser localizado o que un servicio que se ha
              solicitado no está disponible. Estos mensajes del protocolo ICMP se envían a la dirección IP de origen del
              paquete. Siendo un protocolo de la "Capa de Red" ICMP difiere de los protocolos de la "Capa de
              Transporte" (tales como TCP y UDP), en que no es generalmente usado para intercambiar información entre
              sistemas, ni tampoco por las aplicaciones de usuario (con excepción de algunas herramientas como ping y
              traceroute, que emplean mensajes ICMP con fines de diagnóstico). Muchas de las utilidades de red comunes
              están basadas en los mensajes ICMP. El comando traceroute puede implementarse transmitiendo datagramas con
              valores especiales de TTL en la cabecera, y analizando luego los mensajes de "Destino inalcanzable"
              y "
              Tiempo excedido" (tipos 3 y 11\) generados como respuesta. La herramienta ping está implementada
              utilizando los mensajes "Echo request" y "Echo reply" de ICMP. Mensajes de control:
                * ``Echo Request``: mensaje de control que se envía a un host con la expectativa de recibir de él un
                  Echo Reply (
                  Respuesta eco). Esto es conocido como Ping y es una utilidad del protocolo ICMP, subprotocolo de IP.
                  Todo host debe responder a un Echo Request con un Echo Reply que contenga exactamente los mismos datos
                  que el primero.
                * ``Echo Reply``: mensaje generado como respuesta a un mensaje Echo Request (petición de Eco).
                * ``Destination Unreachable``: transportar un mensaje que es generado por un enrutador, y se envía al
                  host de origen, que recibe el mensaje emitido por el enrutador. El mensaje en sí significa que este
                  router considera inalcanzable el destino al que quiere llegar el host. Si se recibe de parte del host
                  de destino, significa que el protocolo que se intentó acceder no está activo en aquel momento.
                * ``Time Exceded``: se crea por una puerta de enlace para informar a la fuente de un datagrama debido al
                  tiempo de vida de campo al llegar a cero. Un mensaje sobrepasando el tiempo también puede ser enviado
                  por un host si no logra volver a montar una fragmentación de datagramas dentro de su límite de tiempo.
                  Los mensajes del tiempo excedido son utilizados por la Ruta de Seguimiento de utilidad para
                  identificar las puertas de enlace en el cambio de los anfitriones.
                * ``Mask Request``: se envía normalmente por un host a un router con el fin de obtener una adecuada
                  Máscara de Subred. Los remitentes deben responder este mensaje con una Solicitud de Dirección de
                  Máscara.

            * ``Protocolo IP`` (Internet Protocol):  
              Protocolo de comunicación de datos digitales clasificado funcionalmente en la capa de red según el modelo
              internacional OSI, su función principal es el uso bidireccional en origen o destino de comunicación para
              transmitir datos mediante un protocolo no orientado a conexión que transfiere paquetes conmutados a través
              de distintas redes físicas previamente enlazadas según la norma OSI de enlace de datos.  
              El diseño del protocolo IP se realizó presuponiendo que la entrega de los paquetes de datos sería no
              confiable. Por ello, IP tratará de realizarla del mejor modo posible, mediante técnicas de enrutamiento,
              sin garantías de alcanzar el destino final pero tratando de buscar la mejor ruta entre las conocidas por
              la máquina que esté usando IP. Los datos en una red basada en IP son enviados en bloques conocidos como
              paquetes o datagramas (en el protocolo IP estos términos se suelen usar indistintamente). En particular,
              en IP no se necesita ningún intercambio de información de control previa a la carga útil (datos), como sí
              que ocurre, por ejemplo, con TCP y únicamente proporciona seguridad (mediante checksums o sumas de
              comprobación) de sus cabeceras y no de los datos transmitidos.

                * ``Direccionamiento IP``: es el identificador de cada equipo dentro de su red de redes. Cada equipo
                  conectado a una red tiene una dirección IP asignada, la cual debe ser distinta a todas las demás
                  direcciones que estén vigentes en ese momento en el conjunto de redes visibles por el equipo. Una
                  dirección IP es un número binario de 32 bits. La dirección IP de un dispositivo está estructurada en
                  dos partes, el identificador de red a la que está conectado el dispositivo, host u ordenador y el
                  identificador del dispositivo, host u ordenador dentro de la red. Para definir el prefijo de la
                  dirección IP, es decir, lo que se conoce como identificador de red, se utiliza la denominada máscara
                  de red que es un número binario de 32 bits que define en las posiciones a “1” el prefijo o
                  identificador de red y en las posiciones a “0” el sufijo o identificador de host. Es muy importante
                  tener en cuenta que dentro de una LAN un host únicamente se puede comunicar con aquellos otros que
                  tengan su mismo prefijo de red, por lo que utilizando las direcciones IP y sus correspondientes
                  máscaras de red podemos crear redes virtuales.
                * ``Máscara, clases y subredes``: para poder realizar el correspondiente encaminamiento en Internet a
                  través de las diferentes redes, y subredes creadas por las distintas organizaciones; se introduce el
                  concepto de máscara, es un número de 32 bits que contiene unos en los bits que identifican tanto a una
                  red (máscara de red), como a una subred (
                  máscara de subred) y al host. Mediante la máscara un ordenador sabe si otro ordenador se encuentra en
                  su misma subred o en otra distinta. Si pertenece a su misma subred, el mensaje se entregará
                  directamente, si se encuentra en otra red diferente, el mensaje se enviará a la puerta de salida o
                  router de la red.

            * ``ARIN`` (American Register Internet Number) es quien a través de los ISP (Internet Service Provider)
              se encarga de gestionar, asignar y en su momento crear las direcciones IP. Para facilitar la
              administración, los diseñadores del esquema de direccionamiento IP determinaron la existencia de cinco
              únicas clases:

                * ``Clase A`` (0): utilizan solamente los 8 primeros bits para identificar la parte de red de la
                  dirección, el resto (
                  tres octetos) se utilizan para especificar la parte de host de la dirección, es decir, 24 bits se
                  reservan para identificar cada una de las conexiones dentro de la red.
                * ``Clase B`` (10): sus dos primeros bits (los que se encuentran más a la izquierda) tomarán siempre el
                  valor binario 10, es decir, el primer octeto tendrá un valor decimal entre 128 y 191, además las
                  direcciones clase B utilizan los dos primeros octetos para el identificador de red, por lo que restan
                  los dos últimos octetos para el identificador de host.
                * ``Clase C`` (110): sus tres primeros bits (los que se encuentran más a la izquierda)
                  tomarán siempre el valor binario 110, es decir, el primer octeto tendrá un valor decimal entre 192 y
                  223, además las direcciones clase C utilizan los tres primeros octetos para el identificador de red,
                  por lo que únicamente queda el último octeto para el identificador de host.
                * ``Clase D`` (1110): direcciones de multicast, consisten en que un datagrama sea entregado a varios
                  hosts dentro de la red en lugar de todos (broadcast) o uno sólo (unicast).Se puede decir que una
                  dirección de clase D o multicast identifica un grupo de host dentro de la red. Lo que caracteriza a
                  las direcciones clase D es que sus cuatro primeros bits (los que se encuentran más a la izquierda)
                  tomarán siempre el valor binario 1110, es decir, el primer octeto tendrá un valor decimal entre 224 y
                  239, además las direcciones clase D utilizan únicamente el primer octeto como identificativo de red y
                  los tres octetos restantes se utilizan como identificativo de grupo de host.
                * ``Clase E`` (1111): reservadas para uso experimental en proyectos de investigación en la red.

            * ``Direcciones Públicas y Privadas``: una dirección IP pública es aquella que identifica de forma única una
              conexión a Internet. De todas las direcciones posibles existentes en Internet han sido excluidas algunas
              para ser utilizadas como direcciones IP privadas, es decir, direcciones IP para utilizar única y
              exclusivamente en redes de área local que no pueden salir a navegar por Internet. Cuando desde una red
              local se sale a navegar por Internet deberemos utilizar un router con tecnología NAT (Network Address
              Translation), hará que sea el router el encargado de almacenar la dirección privada en una tabla,
              asignarle un identificador y sustituir la dirección de origen por la pública del router, de tal manera,
              que se podrá navegar por Internet con la dirección del router y cuando se le conteste, al llegar
              nuevamente al router, no tendrá más que consultar en su tabla el valor de la dirección privada
              correspondiente al identificador y mandarle a ella el datagrama de respuesta. Las direcciones IP
              reservadas como privadas son:

              | Clase | Desde | Hasta |
              | :---: | :---: | :---: |
              | A | 10.0.0.0 | 10.255.255.255 |
              | B | 172.16.0.0 | 172.31.255.255 |
              | C | 192.168.0.0 | 192.168.255.255 |

            * Las direcciones IP también se pueden clasificar en:
                * ``Estáticas``: un host que se conecte a la red con una dirección IP estática, siempre lo hará con la
                  misma IP. Las direcciones IP públicas estáticas son las que utilizan los servidores de internet con
                  objeto de que estén siempre localizables por los usuarios de internet. Estas direcciones hay que
                  contratarlas.
                * ``Dinámicas``: un equipo que se conecte a la red mediante una dirección IP dinámica, cada vez lo hará
                  con una dirección IP distinta. Las direcciones IP públicas dinámicas, son las que se utilizan en las
                  conexiones de internet mediante un módem. Los provedores de internet (ISP)
                  utilizan direcciones IP dinámicas porque tienen más clientes que direcciones IP (es muy improbable que
                  todos se conecten a la vez).

            * ``Otras direcciones IPv4 de Propósito Especial``: bloques de direcciones IPv4 globales y de propósito
              especial que han sido asignados por IANA, no se asignan a los operadores y usuarios y tampoco para uso
              interno de los Regional Internet Registries (RIR):

                * ``0.0.0.0/8``: hace referencia a los equipos origen al concepto “esta red” o “este dispositivo”
                * ``0.0.0.0/32``: hace referencia a la dirección IP de origen de “este host” en “esta red”.
                * ``127.0.0.1/8``: se ha asignado para el uso como dirección de “loopback”. Un datagrama enviado por un
                  protocolo de capa superior a cualquier dirección de este bloque regresa al propio host.
                * ``169.254.0.0/16``: bloque de direcciones de enlace local (local link), se reserva para la
                  comunicación entre hosts en un solo enlace de datos, equipos que están conectado en el mismo “domino
                  de difusión”.
                * ``192.0.2.0/24``: uso en documentación y código de ejemplo “TEST-NET-1”
                * ``224.0.0.0/4``: conocido formalmente con direcciones de clase D, se reserva para el tráfico multicast
                  en IPv4
                * ``240.0.0.0/4``: denominado formalmente como direcciones de clase E, reservada para usos futuros por
                  la IANA, la única excepción existente es 255.255.255.255 usada para “broadcast inundado” los paquetes
                  dirigidos a esta dirección no se enrutan.

            * > ``CIDR (Classless Inter-Domain Routing)``: reemplaza la sintaxis previa para nombrar direcciones IP, las clases de redes. En vez de asignar bloques de direcciones en los límites de los octetos, que implicaban prefijos «naturales» de 8, 16 y 24 bits, CIDR usa la técnica VLSM (variable length subnet mask, en español «máscara de subred de longitud variable»), para hacer posible la asignación de prefijos de longitud arbitraria.

            * ``Subneting``: a medida que las redes de datos iban aumentando su tamaño, se planteaban dos problemas
              relacionados con la escalabilidad, el control del tráfico de broadcast (en las redes IP se utiliza en
              situaciones muy habituales el tráfico de broadcast, dirigido a todos los equipos de la red y que es
              procesado por todos ellos. Cuando el tamaño de la red crece en número de equipos, el porcentaje de tráfico
              de broadcast se va incremento, hasta que provoca que le ancho de banda quede prácticamente consumido por
              este tipo de paquetes) y la creación de redes lógicas diferentes dentro de una sola organización (cuando
              las redes de comunicaciones dan servicio a diferentes departamentos es recomendable separar el tráfico de
              cada departamento en redes lógicas diferentes, dentro de una organización pueden utilizarse diferentes
              tipos de tecnologías de red, lo que genera la necesidad de identificar de forma individual cada una de
              ellas.  
              Se define una subred como un subconjunto de una red, dividiendo la parte local o dirección del equipo en 2
              partes, la dirección de subred y la dirección de host. Existen dos métodos:

                * ``FLSM`` (Fixed Length Subnet Mask): para solucionar los problemas descritos se realiza la división en
                  subredes de la siguiente forma:

                    * 1\. Se toman prestados los bits que necesitemos de la parte de host: (2^número de bits robados \=
                      número de subredes posibles)

                      | Original | 192.168.1.0000.0000 |
                      | :---- | :---- |
                      | Máscara | 255.255.255.``0``000.0000 |

                    * En negrita: Si se toma prestado 1 bit de la porción de host, se crean 2 subredes con la misma
                      máscara de subred.  
                      \* Se divide 256 entre el numero de subredes elegidas (256/2 \= 128\) para saber dónde hacer el
                      corte al crear las subredes.

                      | Subred 0 | Subred 1 |
                      | :---: | :---: |
                      | Red 192.168.1.0-127/25 | Red 192.168.1.0-127/25 |
                      | Máscara: 255.255.255.128 | Máscara: 255.255.255.128 |

                    * 2\. Calcular el rango de direcciones de cada subred:

                      | Rango de direcciones para 192.168.1.0/25 |
                      | :---- |
                      | ``Dirección de red``: 192.168.1.0 000 0000 \= 192.168.1.0  |
                      | ``Primera dirección de host``: 192.168.1.0 000 0001 \= 192.168.1.1 |
                      | ``Última dirección de host``: 192.168.1.0 111 1110 \= 192.168.1.126 |
                      | ``Dirección de broadcast``: 192.168.1.0 111 1111= 192.168.1.127 |

                      | Rango de direcciones para 192.168.1.1/25 |
                      | :---- |
                      | ``Dirección de red``: 192.168.1.1 000 0000 \= 192.168.1.128 |
                      | ``Primera dirección de host``: 192.168.1.1 000 0001 \= 192.168.1.129 |
                      | ``Última dirección de host``: 192.168.1.1 111 1110 \= 192.168.1.254 |
                      | ``Dirección de broadcast``: 192.168.1.1 111 1111= 192.168.1.255 |

                    * 3\. Cálculo de hosts: (2^número de bits no robados – 2 \= número de hosts posibles)

                * ``VLSM`` (Variable Length Subnet Mask): da soporte a subredes con máscaras de diferente longitud. Este
                  estándar permite un direccionamiento IP más flexible. Se toma una red y se divide en subredes fijas,
                  luego se toma una de esas subredes y se vuelve a dividir en otras subredes tomando más bits del
                  identificador de máquina, ajustándose a la cantidad de equipos requeridos por cada segmento de la red.

                    * 1\. Se toman prestados los bits que necesitemos de la parte de host: (2^número de bits robados \=
                      número de subredes posibles), que debe ser el siguiente mayor al numero de hosts que se
                      necesitan. (Si se piden 80 hosts, se necesitan 7 bits para la parte de host “128-2 \= 126”)
                    * 2\. Calcular el rango de direcciones de las subredes:

                      | Rango de direcciones para 192.168.1.0/25 |
                      | :---- |
                      | ``Dirección de red``: 192.168.1.0 000 0000 \= 192.168.1.0  |
                      | ``Primera dirección de host``: 192.168.1.0 000 0001 \= 192.168.1.1 |
                      | ``Última dirección de host``: 192.168.1.0 111 1110 \= 192.168.1.126 |
                      | ``Dirección de broadcast``: 192.168.1.0 111 1111= 192.168.1.127 |

                      | Rango de direcciones para 192.168.1.1/25 |
                      | :---- |
                      | ``Dirección de red``: 192.168.1.1 000 0000 \= 192.168.1.128 |
                      | ``Primera dirección de host``: 192.168.1.1 000 0001 \= 192.168.1.129 |
                      | ``Última dirección de host``: 192.168.1.1 111 1110 \= 192.168.1.254 |
                      | ``Dirección de broadcast``: 192.168.1.1 111 1111= 192.168.1.255 |

                    * 3\. Calcular el resto de redes VLSM:
                        * (Si se piden 30 hosts, se necesitan 5 bits para la parte de host “32-2 \= 30”).
                        * ``Dirección de red``: 192.168.1.128
                        * ``Primera dirección de host``: 192.168.1.129
                        * ``Útima dirección de host``: 192.168.1.159
                        * ``Dirección de broadcast``: 192.168.1.160
                        * ``Cabecera IP``:

                      | Bits | 0-3 | 4-7 | 8-15 | 16-18 | 19-31 |
                      | :---: | :---: | :---: | :---: | :---: | :---: |
                      | 20  Bytes Mínimo | Versión | IHL | Tipo de servicio | Longitud total |  |
                      |  | Identificador |  |  | Flags | Offset fragmento |
                      |  | TTL |  | Protocolo | Checksum de cabecera |  |
                      |  | IP de origen |  |  |  |  |
                      |  | IP de destino |  |  |  |  |
                      |  | Opciones |  |  |  | Relleno |
                      | Datos |  |  |  |  |  |

                        * ``Versión`` (4 bits): versión de protocolo.
                        * ``Longitud de cabecera``: longitud de la cabecera IP en palabras de 32 bits
                        * ``Tipo de servicio``: característica de calidad de servicio dentro del esquema de calidad de
                          servicio diferenciados.
                        * ``Longitud total del paquete`` (16 bits): longitud total del datagrama en bytes,  
                          implica que un paquete o datagramas IP puede tener una longitud de entre 20 y 65535 bytes.
                        * ``Identificación``: número de secuencia que, junto con la dirección de origen,  
                          dirección de destino y protocolo, se utiliza para identificar de forma única el datagrama.
                        * ``Indicadores`` (3 bits):

                            * ``Más fragmentos``: el paquete ha sido fragmentado y restan más fragmentos.
                            * ``No fragmentación``: el paquete no puede ser fragmentado.

                        * ``Desplazamiento del fragmento``: el lugar en que se sitúa el fragmento dentro del datagrama.
                        * ``Tiempo de vida``: tiempo de vida que le queda al paquete en su tránsito.
                        * ``Protocolo``: protocolo de comunicaciones de la capa inmediatamente superior  
                          que va encapsulad en el propio paquete. Permite determinar cuál es la siguiente cabecera que
                          va a ser procesada.
                        * ``Suma de comprobación de la cabecera``: código de detección de errores.
                        * ``Dirección de origen``: identificador de 32 bits del dispositivo origen.
                        * ``Dirección de destino``: identificador de 32 bits del dispositivo destino.  
                          Opciones.
                        * ``Relleno``: la longitud de la cabecera debe ser múltiplo de 32, es necesario utilizar bytes
                          de relleno.

            * ``IPv6``: especifica un nuevo formato de paquete, diseñado para minimizar el procesamiento del encabezado
              de paquetes. Debido a que las cabeceras de los paquetes IPv4 e IPv6 son significativamente distintas, los
              dos protocolos no son interoperables. Las direcciones IPv6 tienen un tamaño de 128 bits que se escriben en
              ocho grupos de cuatro dígitos hexadecimales, se puede comprimir un grupo de cuatro dígitos si este es
              nulo (es decir, toma el valor "0000")
              , si la dirección tiene más de una serie de grupos nulos consecutivos la compresión permite en solo uno:  
              ``2001:0DB8:0000:0000:0000:0000:1428:57ab \= 2001:0DB8::1428:57ab``

            * > La dirección IPv6 del tipo IPv4-mapeada ::ffff:c000:280 se puede representar como ::ffff:192.0.2.128, mostrando claramente la dirección IPv4 mapeada dentro de la IPv6.
            * ``Se clasifican en tres``:
                * ``Unicast``: identifica un único interfaz de red. El protocolo de Internet entrega los paquetes
                  enviados a una dirección unicast al interfaz específico.
                * ``Anycast``: es asignada a un grupo de interfaces, normalmente de nodos  
                  diferentes. Un paquete enviado a una dirección anycast se entrega únicamente  
                  a uno de los miembros, típicamente el host con “menos coste”.

                * > Tanto los Unicast como los Anycast, los primeros 64bits identifican el prefijo de red, y son usados para encaminamiento; los últimos 64 bits identifican lainterface de red del host. BITS 48 (o más) 16 (o menos) 64 CAMPO Prefijo de red Prefijo de subred Identificador de Interfaz de Host Los 64 bits de identificador de la interface (interface identifier) son generados automáticamente con la dirección MAC de la interface y el algoritmo EUI-64 modificado, obtenidos de un servidor DHCPv6, establecidos aleatoriamente o asignados manualmente.

                * ``Multicast``: es usada por múltiples interfaces, que consiguen la dirección multicast participando en
                  el protocolo de multidifusión (multicast) entre los routers de red. Un paquete enviado a una dirección
                  multicast es entregado a todos los interfaces que se hayan unido al grupo multicast correspondiente. (
                  IPv6 no implementa direcciones broadcast. El mismo efecto puede lograrse enviando un paquete al grupo
                  de multicast de enlace-local “todos los nodos” ff02::1). los primeros dos dígitos hexadecimales son
                  FF, esto es lo que caracteriza a las direcciones multidifusión en IPv6.

              | BITS | 8 | 4 | 4 | 112 |
              | :---- | :---- | :---- | :---- | :---- |
              | CAMPO | Prefijo (11111111) | Flags (0RPT) | Scope (XXXX) | GROUP ID |

                * ``Identificación de los tipos de direcciones``: pueden identificarse tomando en cuenta los rangos
                  definidos por los primeros bits de cada dirección.
                * ``::/128`` Se usa para indicar ausencia de dirección
                * ``::1/128`` La dirección de loopback es una dirección que puede usar un nodo para enviarse paquetes a
                  sí mismo (
                  corresponde con 127.0.0.1 de IPv4). No puede asignarse a ninguna interfaz física.
                * ``fe80::/10`` El prefijo local link, específica que la dirección solamente es válida en el enlace
                  físico local.
                * ``ff00::/8`` El prefijo de multicast.
                * ``2002::/16`` Esquema de direccionamiento 6to4 (permite enviar paquetes IPv6 sobre redes IPv4 obviando
                  la necesidad de configurar túneles manualmente).

                * Un paquete en IPv6 está compuesto principalmente de dos partes: header (que tiene una parte fija y
                  otra con las opciones) y payload (los datos).
                * ``Cabecera fija``: Los primeros 40 bytes (320 bits) son la cabecera del paquete y contiene los
                  siguientes campos

                  | Bits | 0-7 | 8-15 | 16-23 | 24-31 |
                  | :---: | :---: | :---: | :---: | :---: |
                  | Primeros 40 Bytes | Versión | Etiqueta de flujo |  |  |
                  |  | Longitud de datos Clase de tráfico |  | Cabecera siguiente | Límite de saltos |
                  |  | IP de origen |  |  |  |
                  |  | IP de destino |  |  |  |

                  | Datos |
                  | :---: |

                  | Variable | Cabecera de extensión I |
                  | :---: | :---: |
                  | Variable | Cabecera de extensión II |
                  | Hasta 8 | ... |

                * ``Version`` (4 bits): representa la versión del Protocolo IPv6 (0110)
                * ``Traffic Class`` (6+2 bits): 6 bits se utilizan para señalar el tipo de campo “DS field” (
                  arquitectura que especifica un mecanismo escalable y simple para clasificar y gestionar el tráfico de
                  red, paquetes de datos y proporcionar QoS). Los 2 bits menos significativos se utilizan para
                  Notificación de Congestión Explícita (ECN).
                * ``Flow Label`` (20 bits): esta etiqueta se usa para mantener el flujo secuencial de los paquetes
                  pertenecientes a la comunicación ayudar al router a identificar que un paquete en particular que
                  pertenece a un determinado flujo de información.
                * ``Payload Length`` (16 bits): indica el tamaño del payload en octetos, incluyendo las cabeceras de
                  extensión (extension headers)
                * ``Next Header`` (8 bits): especifica el tipo de cabecera siguiente y especifica el tipo de cabecera de
                  extensión si está presente en el paquete.
                * ``Hop Limit`` (8 bits): reemplaza el TTL de IPv4.
                * ``Source Address`` (128 bits).
                * ``Destination Address`` (128 bits).

            * En IPv6 las opciones se manejan por medio de las llamadas Cabeceras de Extensión (Extension Headers).
              Estas cabeceras se insertan en el paquete solo si las opciones son necesarias:
                * ``Hop-by-Hop Options``: la información de esta cabecera debe ser examinada Salto-a-Salto, es decir, en
                  cada uno de los nodos de la ruta que ha de seguir el paquete.
                * ``Routing Header``: se utiliza para dar una lista de uno o más nodos que deben estar en la ruta
                  seguida por un paquete.
                * ``Fragment Header``: un host IPv6 que quiere enviar un paquete a un destino IPv6 utiliza el llamado
                  “Path MTU discovery” para determinar el tamaño máximo de paquete que se puede utilizar en el path
                  hasta ese destino. Si el paquete que hay que enviar es más grande que el MTU soportado, el host origen
                  fragmenta el paquete. Gracias a esta forma de actuar, la fragmentación se gestiona de extremo a
                  extremo, liberando a los routers del path de este trabajo.
                * ``Destination Options``: estas cabeceras llevan información que será procesada,  
                  exclusivamente, por el nodo de destino.
                * ``Authentication Header``: proporciona integridad y autenticación (que no  
                  confidencialidad) para todos los paquetes de datos IP.
                * ``Encapsulation Security Payload Header``: proporciona integridad, confidencialidad, autenticación de
                  datos y otras funciones para todos los paquetes de datos IP.

        * ``Protocolo NAT``: U
            * Una posible solución al problema de la escasez de direcciones IP públicas es la utilización de direcciones
              privadas en la red de área local de la organización y hacer uso de una única dirección IP pública para el
              acceso de Internet de todos los equipos de la red local.
            * Debido a que en Internet sólo son válidas las direcciones públicas, para que un dispositivo con una
              dirección privada pueda acceder a Internet se debe enmascarar su dirección privada con una dirección
              pública.
            * Este enmascaramiento de direcciones IP privadas se realiza utilizando el protocolo NAT, su trabajo
              consiste en sustituir la dirección IP local de la cabecera por la IP global cuando el paquete se dirige de
              la red interna a la externa, y en sustituir la dirección IP global por la IP local cuando el paquete va
              desde la red global a la local, este mecanismo solamente era válido cuando un conjunto muy reducido de
              estaciones de las redes locales necesitaba acceder a Internet, puesto que si todos los equipos de la red
              interna pretendían acceder de forma simultánea a internet, se precisaban tantas direcciones globales (IP
              públicas) como dispositivo locales (IP privadas).
            * Para abordar este problema nace: PAT (Port Address Translation) incluyendo un nuevo tipo de traducciones
              que se basaba en la sustitución tanto de direcciones IP como de puertos TCP/UDP.

    * ``CAPA DE TRANSPORTE``: encargada de efectuar el transporte de los datos (que se encuentran dentro del paquete) de
      la máquina origen a la de destino de forma confiable, independientemente del tipo de red física que esté
      utilizando, así como de mantener el flujo de la red. La PDU se llama Segmento o Datagrama, dependiendo de si
      corresponde a TCP o UDP, el primero orientado a conexión (transmisión verificada, eventualmente retransmitida) y
      el otro sin conexión (pueden perderse algunos datos por el camino). Internet tiene dos protocolos principales en
      la capa de transporte, uno no orientado a la conexión, UDP, y otro orientado a la conexión, el TCP:
        * ``UDP`` (User Datagram Protocol): protocolo del nivel de transporte basado en el intercambio de datagramas (
          Encapsulado de capa 4 o de Transporte del Modelo OSI). Permite el envío de datagramas a través de la red sin
          que se haya establecido previamente una conexión, ya que el propio datagrama incorpora suficiente información
          de direccionamiento en su cabecera. Tampoco tiene confirmación ni control de flujo, por lo que los paquetes
          pueden adelantarse unos a otros; y tampoco se sabe si ha llegado correctamente, ya que no hay confirmación de
          entrega o recepción. Su uso principal es para protocolos como DHCP, BOOTP, DNS.
        * ``TCP`` (Transmission Control Protocol): garantiza que los datos serán entregados en su destino sin errores y
          en el mismo orden en que se transmitieron. También proporciona un mecanismo para distinguir distintas
          aplicaciones dentro de una misma máquina, a través del concepto de puerto. Las aplicaciones pueden comunicarse
          en forma segura (gracias al acuse de recibo “ACK” del protocolo TCP) independientemente de las capas
          inferiores. Permite colocar los segmentos nuevamente en orden cuando vienen del protocolo IP, monitoreo del
          flujo de los datos para evitar la saturación de la red, permite que los datos se formen en segmentos de
          longitud variada para "
          entregarlos" al protocolo IP y permite multiplexar los datos, es decir, que la información que viene de
          diferentes fuentes (por ejemplo, aplicaciones) en la misma línea pueda circular simultáneamente. Las
          conexiones TCP se componen de tres etapas:
            * 1\. ``Establecimiento de conexión`` (3-way handshake): una entidad abre un socket en un determinado puerto
              TCP, enviando un paquete SYN inicial al servidor, en el lado del servidor se comprueba si el puerto está
              abierto, es decir, si existe algún proceso escuchando en ese puerto. En caso de no estarlo, se envía al
              cliente un paquete de respuesta con el bit RST activado, lo que significa el rechazo del intento de
              conexión. En caso de que sí se encuentre abierto el puerto, el lado servidor respondería con un paquete
              SYN/ACK. Finalmente, el cliente debería responderle al servidor con un ACK, completando así la negociación
              en tres pasos (SYN, SYN/ACK y ACK) y la fase de establecimiento de conexión.
            * 2\. ``Transferencia de datos``: una serie de mecanismos claves determinan la fiabilidad y robustez del
              protocolo. Entre ellos están incluidos el uso del número de secuencia para ordenar los segmentos TCP
              recibidos y detectar paquetes duplicados, checksums para detectar errores, asentimientos y temporizadores
              para detectar pérdidas o retrasos y ventanas deslizantes para el control de flujo de datos.

                * ``Números iniciales de secuencia``: son usados para identificar los datos dentro del flujo de bytes, y
                  poder identificar (y contar) los bytes de los datos de la aplicación. Siempre hay un par de números de
                  secuencia incluidos en todo segmento TCP, referidos al número de secuencia y al número de
                  asentimiento. Para mantener la fiabilidad, un receptor asiente los segmentos TCP indicando que ha
                  recibido una parte del flujo continuo de bytes. Una mejora de TCP, llamada asentimiento selectivo (
                  Selective Acknowledgement, SACK) permite a un receptor TCP asentir los datos que se han recibido de
                  tal forma que el remitente solo retransmita los segmentos de datos que faltan.
                * ``Checksum``: consistente en el complemento a uno de la suma en complementoa uno del contenido de la
                  cabecera y datos del segmento TCP, agrupados en intervalos de 16 bits, es calculado por el emisor, e
                  incluido en la transmisión del segmento.
                * ``Ventanas deslizantes``: TCP usa control de flujo para evitar que un emisor envíe datos de forma más
                  rápida de la que el receptor puede recibirlos y procesarlos.

              | bit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
              | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
              | 0 | Puerto de origen |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Puerto de destino |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
              | 32 | Número de secuencia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
              | 64 | Número de acuse de recibo (si ACK es establecido) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
              | 96 | Long. cabecera |  |  |  | Reservado |  |  | NS | CWR | ECE | URG | ACK | PSH | RST | SYN | FIN | Tamaño de ventana |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
              | 128 | Suma de verificación |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Puntero urgente (si URG es establecido) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
              | 160 | Opciones (si la longitud de cabecera \> 5, relleno al final con “0” bytes si es necesario). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

                * En cada segmento TCP, el receptor especifica en el campo receive window la cantidad de bytes que puede
                  almacenar en el búfer para esa conexión. El emisor puede enviar datos hasta esa cantidad. Para poder
                  enviar más datos debe esperar que el receptor le envíe un ACK con un nuevo valor de ventana.
            * 3\. ``Fin de la conexión``: utiliza una negociación en cuatro pasos (four-way handshake), tipo FIN-ACK /
              FIN-ACK, terminando la conexión desde cada lado independientemente.
            * ``Puertos``: cada lado de la conexión TCP o UDP tiene asociado un número de puerto asignado por la
              aplicación emisora o receptora. Los puertos son clasificados en tres categorías:

                * ``Well Known``: son asignados por la Internet Assigned Numbers Authority (IANA), van del 0 al 1023 y
                  son usados normalmente por el sistema o por procesos con privilegios. Las aplicaciones que usan este
                  tipo de puertos son ejecutadas como servidores y se quedan a la escucha de conexiones. Algunos
                  ejemplos son:

              | FTP / TFTP / SFTP | 20-21 / 69 / 989-990 | TCP / UDP / TCP |
              | :---- | :---- | :---- |
              | SSH | 22 | TCP |
              | Telnet | 23 | TCP |
              | SMTP | 25 | TCP |
              | DNS | 53 | UDP |
              | DHCP | 67-68 | UDP |
              | HTTP / HTTPS | 80 / 443 | TCP |
              | POP3 / POP3oTLS-SSL | 110 / 995 | TCP |
              | NTP | 123 | UDP |
              | NetBIOS | 137 / 138 / 139 | TCP |
              | IMAP4 / IMAP4oTLS-SSL | 143 /993 | TCP |
              | SNMP | 161 / 162 | TCP |
              | BGP | 179 | TCP |
              | LDAP / LDAPS | 389 / 989 \- 990 | TCP |
              | syslog | 514 | UDP |

                * ``Registered``: normalmente empleados por las aplicaciones de usuario de forma temporal cuando
                  conectan con los servidores, pero también pueden representar servicios que hayan sido registrados por
                  un tercero (rango de puertos registrados: 1024 al 49151).
                * ``Dinámicos/Privados``: también pueden ser usados por las aplicaciones de usuario, pero este caso es
                  menos común. Los puertos dinámicos/privados no tienen significado fuera de la conexión TCP en la que
                  fueron usados (rango de puertos dinámicos/privados: 49152 al 65535).

        * > Keep alive (mecanismos de mantenimiento de conexiones TCP) se refiere generalmente a las conexiones de comunicación en una red que no están terminadas pero que se mantienen hasta que el cliente o servidor interrumpe la conexión. La característica clave de mantener las keep alive es el envío de un mensaje sin contenido entre un servidor y un cliente. Con este mensaje, uno de los usuarios de la red (cliente o servidor) puede comprobar si la conexión está activa.

    * ``CAPA DE SESIÓN``: se encarga de mantener y controlar el enlace establecido entre dos computadores que están
      transmitiendo datos, proporciona control del diálogo, agrupamiento y recuperación. Algunos protocolos que operan
      en la capa de sesión:
        * ``RPC`` (Remote Procedure Call): protocolo que utiliza una computadora para ejecutar código en otra máquina
          remota sin tener que preocuparse por las comunicaciones entre ambas, de forma que parezca que se ejecuta en
          local, es una herramienta básica para establecer estructuras colaborativas y operativas en redes y
          arquitecturas cliente- servidor. El proceso de comunicación con RPC consta del envío de parámetros y el
          retorno de un valor de función, las llamadas a procedimiento remoto siempre se ejecutan siguiendo un patrón
          determinado, por ejemplo, un cliente contacta con un servidor de base de datos central para buscar una pieza
          de repuesto. El servidor remoto revisa entonces la base de datos y envía el resultado al cliente. Este último
          procesa los datos recibidos y muestra, por ejemplo, una lista con los datos del inventario en un software de
          gestión. En la implementación de una Remote Procedure Call, en el lado del emisor y del receptor participan
          unas instancias especiales llamadas “stub”. El “stub” del cliente actúa como sustituto del procedimiento del
          servidor remoto en el lado del cliente, mientras que el “stub” del servidor sustituye al código del cliente
          que realiza la llamada en el lado del servidor. Disfrazando el “alejamiento” del código en el otro lado, los
          “stubs” simulan operar como una unidad local funcional. Al mismo tiempo, actúan como interfaces de
          procedimiento.
        * ``SCP`` (Simple Communication Protocol): medio de transferencia segura de archivos informáticos entre un host
          local y otro remoto o entre dos hosts remotos, usando el protocolo Secure Shell (SSH). Los datos son cifrados
          durante su transferencia, para evitar que potenciales packet sniffers extraigan información útil de los
          paquetes de datos. Sin embargo, el protocolo mismo no provee autenticación y seguridad; sino que espera que el
          protocolo subyacente, SSH, lo asegure.
        * ``ASP`` (AppleTalk Session Protocol): establecimiento de la sesión, mantenimiento y desmontaje, así como la
          secuencia petición. Proporciona servicios básicos para solicitar respuestas a las arbitrarias órdenes y llevar
          a cabo fuera de la banda de consultas de estado. También permite al servidor enviar mensajes asíncronos de
          atención al cliente.
        * ``ONC RPC`` (Open Network Computing Remote Procedure Call): protocolo de llamada a procedimiento remoto (RPC)
          desarrollado como parte del proyecto de su sistema de archivos de Red NFS.
        * ``NetBIOS`` (Network Basic Input/Output System): permite a las aplicaciones 'hablar' con la red. Su intención
          es conseguir aislar los programas de aplicación de cualquier tipo de dependencia del hardware. También evita
          que los desarrolladores de software tengan que desarrollar rutinas de recuperación ante errores o de
          enrutamiento o direccionamiento de mensajes a bajo nivel. En una red local con soporte NetBIOS, las
          computadoras son conocidas e identificadas con un nombre. Cada computador de la red tiene un único nombre.
          Cada PC de una red local NetBIOS se comunica con los otros bien sea estableciendo una conexión (sesión),
          usando datagramas NetBIOS o mediante broadcast. Las sesiones permiten, como en el protocolo TCP, mandar
          mensajes más largos y gestionar el control y recuperación de errores. La comunicación será punto a punto. Por
          otro lado, los métodos de datagramas y broadcast permiten a un ordenador comunicarse con otros cuantos al
          mismo tiempo, pero estando limitados en el tamaño del mensaje. Además, no hay control ni recuperación de
          errores (al igual que ocurre en UDP). A cambio, se consigue una mayor eficiencia con mensajes cortos, al no
          tener que establecer una conexión.

    * ``CAPA DE PRESENTACIÓN``: se encarga de la representación de la información, de manera que aunque distintos
      equipos puedan tener diferentes representaciones internas de caracteres, números, sonido, imagen... Podemos
      resumir definiendo a esta capa como la encargada de manejar las estructuras de datos abstractas y realizar las
      conversiones de representación de datos necesarias para la correcta interpretación de los mismos. Esta capa actúa
      como traductor y cumple 3 funciones principales: formateo de datos, cifrado de datos y compresión de datos.
    * ``SSL`` (Secure Sockets Layer): protocolo criptográfico, que proporciona comunicaciones seguras por una red. Se
      usan certificados X.509 y por lo tanto criptografía asimétrica para autentificar a la contraparte con quien se
      están comunicando,2 y para intercambiar una llave simétrica. Esta sesión es luego usada para cifrar el flujo de
      datos entre las partes. Esto permite la confidencialidad del dato/mensaje, códigos de autenticación de mensajes
      para integridad y como un producto lateral, autenticación del mensaje. SSL proporciona autenticación y privacidad
      de la información entre extremos sobre Internet mediante el uso de criptografía e implica 3 fases básicas:
      negociación entre las partes, intercambio de claves publicas y autenticación basada en certificados y por ultimo
      el cifrado del trafico basado en cifrado simétrico. Durante el proceso de comunicación segura SSL existen dos
      estados fundamentales, el estado de sesión y el estado de conexión. A cada sesión se le asigna un número de
      identificación elegido por el servidor, un método de compresión de datos, una serie de algoritmos de encriptación
      y funciones hash, una clave secreta maestra de 48 bytes y una etiqueta de conexiones.

    * > Certificado digital X.509: propuesta por el ITU-T, fue la primera propuesta a nivel internacional para una infraestructura de clave publica, Public Key Infraestructure (PKI). Es un estándar importante debido a que la estructura del certificado y los protocolos de autenticación que en él se definen son utilizados en muchos contextos como SSL, TLS o S/MIME. OCSP (Online Certificate Status Protocol): método para determinar el estado de vigencia de un certificado digital X.509 usando otros medios que no sean el uso de CRL (Listas de Revocación de Certificados).

    * ``TLS``: el protocolo intercambia registros que encapsulan los datos que se intercambian, cada registro puede ser
      comprimido, cifrado y empaquetado con un código de MAC (Código de Autenticación del Mensaje), todo dependiendo del
      estado de la conexión. Cada registro tiene un “campo de tipo de contenido” que designa el tipo de datos
      encapsulados, “campo de longitud” y un “campo de versión TLS”. Funciona mediante los protocolos TLS Record
      Protocol y el protocolo de la capa de mutuo acuerdo que consiste en un conjunto de tres subprotocolos que permiten
      a las entidades participantes en la comunicación TLS intercambiar los parámetros de seguridad necesarios en la
      capa de registro, autenticarse entre ellas, instanciar los parámetros de seguridad e informar de las condiciones
      de error producidas:

        * ``El protocolo Change Chiper Spec (CCSP)``: consiste en indicar los cambios de estrategias de cifrado.
        * ``Alert Protocolo (AP)``: utilizado para que una entidad emita a la entidad para cualquier tipo de error que
          se produzca en el ámbito de TLS.
        * ``Handshake Protocol (HP)``: cuando se inicia la conexión, el registro encapsula un protocolo de "control" (el
          protocolo de mensajería de handshake). Este protocolo se utiliza para el intercambio de toda la información
          requerida por las dos partes para el intercambio de los datos de las aplicaciones reales por TLS. En él se
          definen los mensajes de formato o que contengan esta información y el orden de su intercambio. Este
          intercambio inicial resulta en una conexión exitosa TLS (ambas partes listas para transferir datos de la
          aplicación con TLS) o un mensaje de alerta. A continuación, un ejemplo simple de conexión, que ilustra un
          handshake en el que el servidor (pero no el cliente) es autenticado por su certificado:

            * 1\. ``Fase de negociación``:
                * 1\. Un cliente envía un mensaje ClientHello especificando la versión más alta de protocolo TLS que
                  soporta, un número al azar, una lista de conjuntos de cifrado sugeridas y métodos de compresión
                  sugeridos.
                * 2\. El servidor responde con un mensaje ServerHello, que contiene la versión del protocolo elegido, un
                  número aleatorio, CipherSuite y método de compresión de las opciones ofrecidas por el cliente.
                * 3\. El servidor envía su mensaje de certificado y a continuación el ServerKeyExchange y por ultimo el
                  servidor envía un mensaje ServerHelloDone, lo que indica que terminó con la negociación del handshake.
                * 4\. El cliente responde con un mensaje ClientKeyExchange, que puede contener una PreMasterSecret (se
                  cifra utilizando la clave pública del certificado del servidor), la clave pública, o nada.
                * 5\. El cliente y el servidor a continuación utilizan los números aleatorios y PreMasterSecret para
                  calcular un secreto común, llamado el "secreto principal" (master secret). Todos los demás datos clave
                  para esta conexión se deriva de este secreto principal (y los valores aleatorios generados tanto por
                  cliente y por servidor), que se pasan a través de una función pseudoaleatoria cuidadosamente diseñado.
            * 2\. ``El cliente envía un registro ChangeCipherSpec``, informando de que todo será autenticado (y cifrado
              si los parámetros de cifrado estaban presentes en el certificado del servidor) desde este momento, por
              último, el cliente envía un mensaje autenticado y cifrado de Finished (terminado), que contiene un hash y
              MAC sobre los mensajes de handshake anteriores. El servidor intentará descifrar el mensaje Finished del
              cliente y verificar el hash y MAC. Si el descifrado o verificación falla, el handshake se considera que ha
              fracasado y la conexión debe ser derribada.
            * 3\. ``El servidor responde con otro ChangeCipherSpec``, diciéndole al cliente, "Todo lo que yo te diga de
              ahora en adelante será autenticado (y cifrado, si el cifrado se negoció)." El servidor envía su mensaje
              Finished autenticado y cifrado. El cliente realiza el mismo descifrado y verificación.
            * 4\. ``Fase de aplicación``: en este punto, el "handshake" está completado y el protocolo de aplicación
              está activada. Los mensajes de aplicación intercambiados entre el cliente y el servidor también serán
              autenticados y opcionalmente cifrados exactamente igual que en su mensaje final.

        * > ``TLS 1.3``: proporciona autenticación y privacidad de la información entre extremos sobre Internet mediante el uso de criptografía.
        * > Para poder iniciar una sesión de conexión, el protocolo handshake o de negociación inicia una fase de negociación siguen el siguiente orden:
            * > El cliente envía un mensaje ClientHello, especificando la información de cifrado y la versión del protocolo, la lista de algoritmos y los métodos de compresión que soporta.
            * > El servidor responde al cliente con un mensaje ServerHello indicando el cifrado, método de compresión y protocolo TLS elegidos y una cadena de 32 bytes aleatorios.
            * > El servidor ofrece su mensaje de certificado para ser verificado por el cliente, de esta manera el cliente puede verificar la integridad del servidor.
            * > El servidor envía su mensaje ServerKeyExchange, el cual incluye la calve publica y la clave del certificado y posteriormente solicita mediante el mensaje Certificate Request el certificado del cliente para que la conexión pueda ser mutuamente autenticada.
            * > El servidor envía un mensaje ServerHelloDone dando por concluida la fase de negociación asimétrica. El cliente responde con un mensaje con su certificado.
            * > El cliente una vez ha comprobado y validad el certificad responde con un mensaje ClientKeyExchange que contienen la PreMasterSecret cifrada con la clave pública del servidor.
            * > Cliente y servidor usan las cadenas de números aleatoria y la PreMasterSecret para generar la clave de sesión secreta con la ambos cifraran y descifraran la informa enviada.

        * ``Códecs de audio y video``: H.323 es uno de los estándares más antiguos que generalmente se utilizan para la
          telefonía VoIP y videoconferencia. Es un sistema de varios protocolos y elementos que permite la transferencia
          de datos de medios sobre redes de paquetes. Esta estructura de recomendación estándar abre diferentes opciones
          de comunicación multimedia, incluyendo telefonía, videoconferencia y transferencia de medios. Por defecto,
          H.323 utiliza el código G.711 con una alta velocidad de ancho de banda. Sin embargo, se considera que G.711
          está desactualizado. Los códecs de baja frecuencia como G.723 y G.729 se usaron inicialmente para las
          conexiones a Internet. En cuanto a los códecs de video, todos los puntos finales modernos H.323 deben ser
          compatibles con H.264, que se convierten en un estándar.
        * ``XDR`` (eXternal Data Representation): permite la transferencia de datos entre máquinas de diferentes
          arquitecturas y sistemas operativos. Trabaja al nivel de ordenamiento de byte, códigos de caracteres y
          sintaxis de estructura de datos.

    * ``CAPA DE APLICACIÓN``: Ofrece a las aplicaciones (de usuario o no) la posibilidad de acceder a los servicios de
      las demás capas y define los protocolos que utilizan las aplicaciones para intercambiar datos, como correo
      electrónico (POP y SMTP), gestores de bases de datos y protocolos de transferencia de archivos (FTP). En esta capa
      aparecen diferentes protocolos y servicios:
        * ``NFS`` (Network File System): posibilita que distintos sistemas conectados a una misma red accedan a ficheros
          remotos como si se tratara de locales y está implementado sobre los protocolos XDR (presentación) y ONC RPC (
          sesión). El protocolo NFS está incluido por defecto en los Sistemas Operativos UNIX y la mayoría de
          distribuciones Linux. Un servidor y uno o más clientes. Los clientes acceden de forma remota a los datos que
          se encuentran almacenados en el servidor, Las estaciones de trabajo locales utilizan menos espacio de disco
          debido a que los datos se encuentran centralizados en un único lugar, pero pueden ser accedidos y modificados
          por varios usuarios, de tal forma que no es necesario replicar la información. Los usuarios no necesitan
          disponer de un directorio “home” en cada una de las máquinas de la organización. Los directorios “home” pueden
          crearse en el servidor de NFS para posteriormente poder acceder a ellos desde cualquier máquina a través de la
          infraestructura de red. También se pueden compartir a través de la red, dispositivos de almacenamiento.  
          El servidor también ofrece servicios de montaje, de control de autenticación y acceso y una caché a través del
          uso del comando “rpc”:

            * ``rpc.mountd``: demonio que se encarga del montaje remoto. Recibe la petición desde el cliente NFS y
              comprueba que el sistema de archivos este exportado y si está disponible permite las solicitudes de acceso
              de NFS y proporciona información sobre ello (showmount).
            * ``rpc.nfsd``: demonio para servir archivos. Se pueden arrancar varias copias de este demonio. Utiliza el
              puerto TCP/UDP 2049\.
            * ``rpc.portmap``: se encarga de indicar a los clientes donde se encuentra el servicio real en el servidor.
              Los servicios basados en RPC usan portmap para atender las peticiones de los clientes por lo cual este
              servicio debe estar disponible el primero.
            * ``rpc.lockd``: encargado de proporcionar el servicio de bloqueo de archivos para asegurar su consistencia
              ya que pueden ser accedidos de forma concurrente. Se ejecuta tanto en el servidor como en el cliente.
            * ``rpc.statd``: demonio que trabaja conjuntamente con lockd para recuperar en caída de sistemas. Mantiene
              información sobre los procesos en los clientes que poseen locks de archivos de determinado servidor.
              Cuando el servidor NFS se recupera statd informa a los otros de los clientes, que el servidor se ha
              recuperado y así ellos resuelven los locks que tenían.

        * ``FTP`` (File Transfer Protocol): protocolo utilizado para la transferencia de archivos entre dos equipos que
          estén conectados a una red TCP/IP. El modelo usado en FTP es el de una aplicación cliente-servidor, envía
          comandos oportunos para iniciar sesión, una vez iniciada, puede efectuar algunos comandos de manipulación o
          envío/recepción de ficheros y después desconecta la sesión. El servidor se limita a recibir conexiones de los
          clientes, interpretar los comandos y comprobar si las operaciones se pueden efectuar sobre los ficheros.
          Dependiendo de factores como los cortafuegos que existan entre el cliente y el servidor, si se usa NAT o no...
          Se puede usar:

            * ``Modo activo``: el cliente se conecta al puerto 21 del servidor, y pone un puerto TCP aleatorio por
              envían del 1023 en escucha, envía ese número de puerto al servidor mediante la conexión establecida, y el
              servidor se conecta al cliente para enviar los datos.
            * ``Modo pasivo``: el cliente se conecta al puerto 21 del servidor, el servidor entonces pone un puerto
              aleatorio por encima del 1023 en escucha, y envía ese número de puerto al cliente, para que inicie otra
              conexión al servidor e intercambiar los datos por ella.

        * Estos dos modos consiguen que la comunicación se pueda realizar, aunque uno de los extremos tena un firewall
          que le impida recibir conexiones.
        * Dependiendo del tipo de datos que se envían:

            * ``Type ASCII``: solo se utilizará el juego de caracteres ASCII para enviar los datos, es decir, que
              transmitiremos únicamente texto.
            * ``Type Binary``: podemos enviar el tipo de archivos que queramos, sin importar la codificación.

        * ``Comandos FTP``:

            * ``open “dirección”``: inicia una conexión con un servidor FTP.
            * ``close o disconnect``: finaliza una conexión FTP.
            * ``bye``: finaliza una conexión FTP y la sesión de trabajo con el programa cliente.
            * ``cd``: cambia el directorio de trabajo en el servidor.
            * ``delete “archivo”``: borra un archivo en el servidor.
            * ``dir``: muestra el contenido del directorio de trabajo en el que estamos en el servidor.
            * ``\!dir``: muestra el contenido del directorio de trabajo en el que estamos en la maquina local.
            * ``get “archivo”``: solicita el envío de un archivo del servidor.
            * ``put “archivo”``: envía un archivo al servidor.
            * ``pwd``: muestra el directorio activo en el servidor.
            * ``bin``: activa el modo de transferencia binario.
            * ``ascii``: activa el modo de transferencia en modo texto ASCII.

        * ``DHCP`` (Dynamic Host Configuration Protocol): protocolo de red de tipo cliente/servidor mediante el cual un
          servidor DHCP asigna dinámicamente una dirección IP y otros parámetros de configuración de red a cada
          dispositivo en una red para que puedan comunicarse con otras redes IP. Este servidor posee una lista de
          direcciones IP dinámicas y las va asignando a los clientes conforme estas van quedando libres, sabiendo en
          todo momento quién ha estado en posesión de esa IP, cuánto tiempo la ha tenido y a quién se la ha asignado
          después. El DHCP le permite al administrador supervisar y distribuir de forma centralizada las direcciones IP
          necesarias y, automáticamente, asignar y enviar una nueva IP si fuera el caso en que el dispositivo es
          conectado en un lugar diferente de la red. El protocolo DHCP incluye ``tres métodos de asignación`` de
          direcciones ``IP``:

            * ``Manual o estática``: asigna una dirección IP a una máquina determinada. Se suele utilizar cuando se
              quiere controlar la asignación de dirección IP a cada cliente, y evitar, también, que se conecten clientes
              no identificados.
            * ``Automática``: asigna una dirección IP a una máquina cliente la primera vez que hace la solicitud al
              servidor DHCP y hasta que el cliente la libera. Se suele utilizar cuando el número de clientes no varía
              demasiado.
            * ``Dinámica``: el único método que permite la reutilización dinámica de las direcciones IP. El
              administrador de la red determina un rango de direcciones IP y cada dispositivo conectado a la red está
              configurado para solicitar su dirección IP al servidor cuando la tarjeta de interfaz de red se inicializa.
              El procedimiento usa un concepto muy simple en un intervalo de tiempo controlable. Esto facilita la
              instalación de nuevas máquinas clientes.

        * ``HTTP`` (HyperText Transfer Protocol): protocolo de comunicaciones de aplicación que permite la transmisión
          de datos en forma de texto, hipertexto, audio, imágenes o cualquier tipo de información multimedia. Es un
          protocolo cliente/servidor orientado a transacciones, un protocolo sin estados donde cada “transacción” de
          información requiere el establecimiento, mantenimiento y cierre de la conexión entre el cliente y el servidor.
          El funcionamiento de HTTP es: un cliente HTTP (
          navegador web) establece una conexión directa con el servidor, donde se ubica el recurso. El cliente establece
          una conexión TCP con el servidor y emite una solicitud HTTP. Esta solicitud consta de una sentencia concreta (
          método), una URL y un mensaje MIME que contiene los parámetros de la solicitud. Cuando el servidor recibe la
          solicitud, intenta llevar a cabo la acción solicitada y después devuelve una respuesta HTTP. La respuesta
          incluye información de estado, un código de éxito/error y un mensaje MIME que contiene información sobre el
          servidor sobre la propia respuesta y finalmente el cuerpo de la propia respuesta.
        * ``Métodos HTTP``:
            * ``GET``: El método GET se emplea para leer una representación de un resource. En caso de respuesta
              positiva (200 OK), GET devuelve la representación en un formato concreto: HTML, XML, JSON o imágenes,
              JavaScript, CSS, etc.
            * ``HEAD``: Es idéntido a GET, pero el servidor no devuelve el contenido en el HTTP response. Cuando se
              envía un HEAD request, significa que sólo se está interesado en el código de respuesta y los headers HTTP,
              no en el propio documento
            * ``POST``: se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el
              estado o efectos secundarios en el servidor, aunque se envía en el mismo formato que con el método GET. Si
              se quiere enviar texto largo o cualquier tipo de archivo este es el método apropiado.
            * ``PUT``: Utilizado normalmente para actualizar contenidos, pero también pueden crearlos.
            * ``DELETE``: elimina un recurso especifico identificado en la URI.
            * ``CONNECT``: establece un túnel hacia el servidor identificado por el recurso.
            * ``OPTIONS``: es utilizado para describir las opciones de comunicación para el recurso de destino.
            * ``TRACE``: realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino.
            * ``PATCH``: es utilizado para aplicar modificaciones parciales a un recurso.

        * ``Mensajes de respuesta``:

            * ``Respuestas informativas 1xx``:
                * 100: Continue
                * 101: Switching Protocol
                * 102: Processing
                * 103: Early Hints
            * ``Respuestas satisfactorias 2xx:``
                * 200: OK
                * 201: Created
                * 202: Accepted
                * 203: Non-authoritative Information
                * 204: No Content
                * 205: Reset Content
                * 206: Partial Content
                * 207: Multi-Status
            * ``Redirecciones 3xx``:
                * 300: Multiple Choice
                * 301: Moved Permanently
                * 302: Found
                * 303: See Other
                * 304: Not Modified
                * 305: Use Proxy
                * 306: Unused
                * 307: Temporary Redirect
                * 308: Permanent Redirect
            * ``Errores de los clientes 4xx``:
                * 400: Bad Request
                * 401: Unauthorized
                * 402: Payment Required
                * 403: Forbidden
                * 404: Not Found
                * 405: Method Not Allowed
                * 406: Not Acceptable
                * 407: Proxy Authentication Required
                * 408: Request Timeout
                * 429: Too Many Requests
            * ``Errores de los servidores 5xx``:
                * 500: Internal Server Error
                * 501: Not Implemented
                * 502: Bad Gateway
                * 503: Service Unavailable
                * 504: Gateway Timeout
                * 505: HTTP Version Not Supported
                * 506: VAriant Also Negotiates
                * 507: Insufficient Storage
                * 508: Loop Detected
                * 511: Network Authentication Required
      ***
        * > HTTP/2 no modifica la semántica de aplicación de HTTP.
        * > Todos los conceptos básicos, tales como los métodos HTTP, códigos de estado, URI, y campos de cabecera, se mantienen sin cambios; sin embargo, HTTP 2.0 introduce innumerables mejoras como el uso de una única conexión, la compresión de cabeceras o el servicio ‘server push’.
        * > Características:
            * > Una única conexión para descargar todos los elementos de la web.
            * > Multiplexación: permite enviar y recibir varios mensajes al mismo tiempo optimizando la comunicación.
            * > HTTP 2.0 es un protocolo binario: tiene el uso de un protocolo binario es la facilidad para encontrar el comienzo y el final de cada frame.
            * > Servicio “server push”: estimaciones para que el servidor sea capaz de enviar información al usuario antes de que éste la solicite para que la información esté disponible de forma inmediata.
            * > Comprensión de cabeceras para transmitir menos información: las cabeceras experimentan compresiones, con lo que se obtienen mejores tiempos de respuesta y también se mejora la eficiencia.
            * > Priorización de flujos: Para poder ‘controlar’ la prioridad que tienen las tramas, HTTP 2.0 permite asignar a cada flujo un peso (entre 1 y 256\) y una dependencia.
            * > No requiere TLS: el uso de cifrado TLS (Transport Layer Security) es opcional pero los principales navegadores hacen uso de este.
      ***
        * ``HTTP Strict Transport Security`` (HSTS): es una política de seguridad web establecida para evitar ataques
          que puedan interceptar comunicaciones, cookies, etc. Según este mecanismo un servidor web declara que los
          agentes de usuario compatibles (es decir, los navegadores), solamente pueden interactuar con ellos mediante
          conexiones HTTP seguras (es decir, en HTTP sobre TLS/SSL1). HSTS es un estándar del IETF y se especifica en el
          RFC 6797\.

        * ``HTTPS`` (HyperText Transfer Protocol Secure): existe una variante de HTTP utilizada para comunicaciones
          seguras llamada HTTPS, es una conexión HTTP que se realiza con la ayuda del protocolo SSL (Secure Socket
          Layer) o TLS (Transport Layer Security) y que usa el puerto por defecto TCP 443 en vez del 80\. Lo que
          proporciona una medida efectiva de cifrado y autenticación tanto del servidor como del cliente, para las
          transacciones de comercio o banca electrónica. Un servidor HTTP espera recibir del cliente como primeros datos
          una “Request-Line”. Sin embargo, los primeros datos que espera recibir un servidor TLS es un mensaje del tipo
          “ClientHelp”.

            * ``Identidad del servidor``: si el nombre del servidor es conocido por el cliente, dicho cliente debe
              comprobar la identidad del servidor cuando se muestre el mensaje del certificado del servidor, si el
              nombre del servidor no coincide con la identidad indicada en el certificado, el cliente debe notificárselo
              al usuario o terminal la conexión con un mensaje de “error de certificado”.
            * ``Identidad del cliente``: el servidor no tiene conocimiento sobre la identidad del cliente.

        * ``SSH`` (Secure Shell): nombre de un protocolo y del programa que lo implementa cuya principal función es el
          acceso remoto a un servidor por medio de un canal seguro en el que toda la información está cifrada. Además de
          la conexión a otros dispositivos, SSH permite copiar datos de forma segura (tanto archivos sueltos como
          simular sesiones FTP cifradas), gestionar claves RSA para no escribir contraseñas al conectar a los
          dispositivos y pasar los datos de cualquier otra aplicación por un canal seguro tunelizado mediante SSH y
          también puede redirigir el tráfico del (Sistema de Ventanas X) para poder ejecutar programas gráficos
          remotamente. El puerto TCP asignado es el 22\. SSH trabaja de forma similar a como se hace con telnet. La
          diferencia principal es que SSH usa técnicas de cifrado que hacen que la información que viaja por el medio de
          comunicación vaya de manera no legible, evitando que terceras personas puedan descubrir el usuario y
          contraseña de la conexión ni lo que se escribe durante toda la sesión; aunque es posible atacar este tipo de
          sistemas por medio de ataques de reinyección/reproducción y manipular así la información entre destinos.
        * ``TELNET``: protocolo de comunicaciones de capa de aplicación, permite la ejecución de sesiones de terminal
          remoto, utilizando para ello conexiones TCP. Tienen una arquitectura cliente/servidor (puerto 23). No
          proporciona ningún mecanismo de seguridad, la recomendación actual es utilizarlo solamente en redes privadas
          seguras o sino utilizar en su lugar el protocolo Secure Shell (SSH). Estos servidores escuchan las solicitudes
          de conexión en el puerto TCP 22\.
        * ``DNS`` (Domain Name System): sistema de nomenclatura jerárquica par ordenadores, servicio o cualquier recurso
          conectado a TCP/IP. Permite asociar información de diferente tipo con el nombre de domino asignado, su función
          más importante es traducir (resolver) nombres de sistemas, a direcciones IP. Los servidores DNS utilizan una
          base de datos distribuida y jerárquica que almacena información asociada a nombres de dominio. Los usos más
          comunes son la asignación de nombres de domino a direcciones IP y la localización de los servidores de correo
          electrónico de cada dominio.
        * ``La red de DNS se conforma de``:
            * ``Clientes DNS``: genera peticiones DNS de resolución de nombres a un servidor DNS.
            * ``Servidores DNS``: contestan a las peticiones de los clientes.
            * ``Zonas de autoridad``: parte del espacio de nombres de domino que almacena los datos.
            * ``Servidor autoritativo de Zona``: cada dominio DNS tienen al menos uno, es aquel legitimado para
              almacenar los registros d host o de servicios asociados a este dominio. Cada servidor de zona tiene
              información explicita sobre que servidor es el autoritativo para cada uno de sus subdominios. Cualquier
              nombre de domino pueda ser rastreado a partir de una consulta de un cliente por cualquier servidor DNS
              conociendo la dirección de los servidores Raiz (aquellos que conocen las direcciones IP de los servidores
              autoritativos de los dominios del primer nivel).

        * ``Nombres de dominio``: usualmente consiste en dos o más cadenas de texto (etiquetas) separadas por puntos, a
          la etiqueta ubicada más a la derecha se le llama dominio de nivel superior (Top Level Domain, TLD). Cada
          etiqueta a la izquierda especifica una subdivisión o subdominio. Finalmente, a la izquierda del dominio se
          coloca el nombre de la maquina a la que se hace referencia.  
          Estructura: DNS conjunto jerárquico de servidores, cada dominio o sub dominio tienen una o más zonas de
          autoridad. Al inicio de esa jerarquía se encuentran los servidores raíz, que responden cuando se busca
          resolver un dominio de primer y segundo nivel.  
          El espacio de nombres de dominio tiene una estructura arborescente. Un nombre de dominio completo de un objeto
          consiste en la concatenación de todas las etiquetas de un camino. Las etiquetas individuales están separadas
          por puntos. Los objetos de un dominio DNS se registran en un archivo de zona, ubicado en uno o más servidores
          de nombres, los DNS pueden ser del tipo:
            * ``Preferidos o primarios``: servidores autoritativos de al menos un domino que guardan los datos de un
              espacio de nombres en sus ficheros. Permiten lectura y escritura.
            * ``Alternativos o secundarios``: servidores autoritativos de dominio, son de solo lectura y obtienen y
              actualizan los datos de los servidores primarios a través de una transferencia de zona.
            * ``Locales o caché``: no son autoritativos de ningún dominio, no contienen la base de datos para la
              resolución de nombres. Cuando se les realiza una consulta, obtienen la información requerida de los
              servidores autoritativos, almacenando la respuesta en su base de datos (caché) para agilizar la repetición
              de estas peticiones.

        * ``Consultas que un servicio cliente DNS puede hacer a un servidor DNS``:
            * ``Recursiva``: realiza un cliente en las que solicita al servidor una respuesta final autoritativa ante
              una consulta. El servidor consultado debe enviar cuantas consultas intermedias (no autoritativas) se
              requieran hasta localizar al servidor autoritativo del FQDN (Fully Qualified Domain Name) de la consulta
              inicial y obtener la respuesta autoritativa, es el tipo de consulta que realizan los equipos cliente.
            * ``Iterativa``: consulta enviada a un servidor DNS permite a este responder con una respuesta no
              autoritativa, permite al servidor responder a su solicitante con la dirección de otro servidor DNS. Suelen
              enviar unos servidores a otros para localizar al autoritativo de dominio al que pertenece el FQDN.

        * ``Respuestas que puede proporcionar un servidor DNS``:
            * ``Autoritativa``: proviene del servidor que posee autoridad sobre el dominio que está solicitando la
              resolución. Siempre es una respuesta final, ya sea satisfactoria o no.
            * ``No autoritativa``: un servidor es preguntado por un FQDN para cuyo dominio no es autoritativo y responde
              con la dirección de otro servidor DNS distinto.

        * ``Tipos de registros DNS``:
            * ``A`` (Address): este registro se usa para traducir nombres de hosts a direcciones IPv4.
            * ``AAAA`` (Address): se usa en IPv6 para traducir nombres.
            * ``CNAME`` (Canonical Name): crear nombres de servidores de alojamiento adicionales, cuando se están
              ejecutando múltiples servicios (como ftp y web) en un servidor con una sola dirección IP cada servicio
              tiene su propia entrada de DNS.
            * ``NS`` (Name Server): asociación que existe entre un nombre de dominio y los servidores de nombres
              autoritativos que almacenan la información del dominio.
            * ``MX`` (Mail Exchange): asocia un nombre de dominio a un servidor de intercambio de correo para ese
              dominio.
            * ``PTR`` (Pointer): “registro inverso” traduce IPs en nombres de host o de dominio.
            * ``SOA`` (Start of Authtority): proporciona información sobre el servidor DNS primario de zona.
            * ``HINFO`` (Host Information): permite que la gente conozca el tipo de maquina y SO al que corresponde un
              dominio.
            * ``TXT`` (Text): permite a los dominios identificarse de modos arbitrarios.
            * ``LOC`` (Localization): permite indicar las coordenadas del dominio.
            * ``SRV`` (Services): ofrece el dominio asociándolos a un nombre.
            * ``SPF`` (Sender Policy Framework): protección contra la falsificación de direcciones en el envío de correo
              electrónico. Identifica, a través de los registros de nombres de dominio (DNS), a los servidores de correo
              SMTP autorizados para el transporte de los mensajes.

### 3\. MODELO TCP/IP

* El modelo TCP/IP es usado para comunicaciones en redes y, como todo protocolo, describe un conjunto de guías generales
  de operación para permitir que un equipo pueda comunicarse en una red. TCP/IP provee conectividad de extremo a extremo
  especificando cómo los datos deberían ser formateados, direccionados, transmitidos, enrutados y recibidos por el
  destinatario. TCP/IP es un conjunto de protocolos que permiten la comunicación entre los ordenadores pertenecientes a
  una red. La sigla TCP/IP significa Protocolo de control de transmisión/Protocolo de Internet. Proviene de los nombres
  de dos protocolos importantes incluidos en el conjunto TCP/IP, es decir, del protocolo TCP y del protocolo IP.

| Modelo OSI | Modelo TCP/IP |
| :---: | :---: |
| 1\. Física | 1\. Acceso a la red |
| 2\. Enlace de datos |  |
| 3\. Red | 2\. Internet |
| 4\. Transporte | 3\. Transporte |
| 5\. Sesión | 4\. Aplicación |
| 6\. Presentación |  |
| 7\. Aplicación |  |

* El modelo incluye ``cuatro capas``:
    * ``Capa de acceso al medio``: maneja las partes físicas del envío y recepción de datos mediante el cable Ethernet,
      la red inalámbrica, la tarjeta de interfaz de red, el controlador del dispositivo en el equipo, etcétera.
    * ``Capa de internet``: controla el movimiento de los paquetes alrededor de la red.
    * ``Capa de transporte``: proporciona una conexión de datos fiable entre dos dispositivos. Divide los datos en
      paquetes, hace acuse de recibo de los paquetes que recibe del otro dispositivo y se asegura de que el otro
      dispositivo haga acuse de recibo de los paquetes que recibe a su vez.
    * ``Capa de aplicación``: grupo de aplicaciones que requiere comunicación de red. Es con lo que el usuario suele
      interactuar, como el correo electrónico y la mensajería. Como la capa inferior gestiona los detalles de la
      comunicación, las aplicaciones no tienen que preocuparse por ello.

### 4\. W3C, ATAG, WCAG

* ``WCAG`` (Web Content Accessibility Guidelines): son una parte de las directrices de accesibilidad web publicadas por
  la WAI (Web Accessibility Initiative ) parte del World Wide Web Consortium (W3C), la principal organización de
  estándares de internet. Consiste en 12 directrices organizados en cuatro principios.
* Los sitios web deben ser perceptibles, operables, entendibles y robustos:
    * ``Perceptible``: a información y los componentes de la interfaz de usuario deben ser presentados al usuario de tal
      forma que sean perceptibles.
        * ``Alternativas textuales``: provea textos alternativos para contenido no textual
        * ``Medios tempodependientes``: provea alternativas para Time Based Media.
        * ``Adaptable``: contenido que pueda ser presentado de diferentes formas
        * ``Distinguible``: más fácil para los usuarios el ver y escuchar el contenido
    * ``Operable``: los componentes de la interfaz y navegación deben ser operables.
        * ``Accesible por teclado``: Proporcionar acceso a toda la funcionalidad mediante el teclado
        * ``Tiempo suficiente``: Proporcionar a los usuarios el tiempo suficiente para leer y usar el contenido.
        * ``Convulsiones``: No diseñar contenido de un modo que se sepa podría provocar ataques, espasmos o
          convulsiones.
        * ``Navegable``: Proporcionar medios para ayudar a los usuarios a navegar, encontrar contenido y determinar
          dónde se encuentran.
        * ``Formas de entrada de datos`` (Input Modalities): Facilitar a los usuarios operar la funcionalidad mediante
          varias formas de entrada de datos, más allá del teclado.
    * ``Comprensible``: la información y la operación de la interfaz de usuarios deben ser entendibles.
        * ``Legible``: Hacer que los contenidos textuales resulten legibles y comprensibles.
        * ``Predecible``: Hacer que las páginas web aparezcan y operen de manera predecible.
        * ``Entrada de datos asistida``: Ayudar a los usuarios a evitar y corregir los errores.
    * ``Robusto``: el contenido debe ser suficientemente robusto de tal forma que pueda ser interpretado de forma
      confiable.
    * ``Compatible``: Maximizar la compatibilidad con las aplicaciones de usuario actuales y futuras, incluyendo las
      ayudas técnicas

* ``ATAG`` (Authoring Tool Accessibility Guidelines): parte de una serie de pautas de accesibilidad, incluidas las
  Pautas de accesibilidad al contenido web (WCAG) y las Pautas de accesibilidad del agente de usuario (UAAG). Las
  herramientas de autor son software y servicios que los “autores” (desarrolladores web, diseñadores, escritores, etc.)
  utilizan para producir contenido web (páginas web estáticas, aplicaciones web dinámicas, etc.). Los documentos de las
  ATAG explican cómo:
    * Hacer que las herramientas de creación sean accesibles, de modo que las personas con discapacidad puedan crear
      contenido web.
    * Ayudar a los autores a crear contenido web más accesible, específicamente: habilitar, respaldar y promover la
      producción de contenido que se ajuste a las Pautas de accesibilidad al contenido web (WCAG).

* > ``RDF`` (Resource Description Framework):
    * > Es una familia de especificaciones de la World Wide Web Consortium (W3C) originalmente diseñado como un modelo de datos para metadatos.
* > ``SPARQL``:
    * > Un lenguaje estandarizado para la consulta de grafos RDF, normalizado por el RDF Data Access Working Group (DAWG) del World Wide Web Consortium (W3C).
    * > Es una tecnología clave en el desarrollo de la web semántica.
    * > Al igual que sucede con SQL, es necesario distinguir entre el lenguaje de consulta y el motor para el almacenamiento y recuperación de los datos.
    * > Por este motivo, existen múltiples implementaciones de SPARQL, generalmente ligados a entornos de desarrollo y plataforma tecnológicas.
* > ``NVDA`` (Non-Visual Desktop Access):
    * > Lector de pantalla portátil gratuito, de código abierto para Microsoft Windows.
* > ``JAWS`` (Job Access With Speech):
    * > Es un software lector de pantalla para ciegos o personas con visión reducida.

## TEMA 4 – SERVIDORES DE MENSAJERÍA

### 1\. ADMINISTRACIÓN DE SERVIDORES DE CORREO ELECTRÓNICO

* Inicialmente el correo se sustentaba sobre un conjunto pequeño de recomendaciones y especificaciones para el
  intercambio de mensajes entre “hosts” TCP/IP llamado X.400 (estándar conforme al modelo OSI, para el intercambio de
  correo electrónico), como le pasó a la mayor parte de los estándares OSI del nivel de aplicación no soportó la
  competencia con el protocolo similar de Internet, en este caso el SMTP.
* La tendencia actual es la de proveer una solución unificada de mensajería para una organización que integre también
  mensajería móvil, mensajería instantánea, groupware... la frontera entre servidores puros de correo y servidores
  generales de mensajería o entrono colaborativo se diluye. Un servidor más estándar resulta interesante, con
  alternativas como sendmail (Linux).
* Es más habitual contar con dispositivos de almacenamiento dedicados como soluciones NAS o SAN con conexiones rápidas
  de fibra óptica y que además facilitan el uso de clústeres al permitir que un servidor asuma los buzones gestionados
  por otro en caso de caída. Los modelos de acceso más habituales, son:
    * ``Sin conexión``: el cliente se conecta periódicamente al servidor y descarga los mensajes nuevos del mismo
      procediendo a continuación a su borrado, el correo se procesa y almacena localmente en el cliente (POP3).
    * ``Conectado``: los clientes realizan cambios en el servidor, es decir, el correo se almacena en el servidor, pero
      es procesado por software en el cliente, los cambios suelen realizarse por medio de algún protocolo de acceso
      remoto (
      NFS).
    * ``Desconectado``: mezcla de los anteriores, el cliente en primer lugar recupera los datos del servidor, trabaja
      con ellos localmente y posteriormente se envían al servidor.
    * ``Tipos de clientes``:
        * ``Cliente tradicional``: presente en los primeros sistemas Unix. Accesible desde la interfaz de comandos
          mediante una cuenta en la misma máquina del servidor de correo, actualmente obsoleto.
        * ``Clientes pesados``: se instalan en el PC del usuario y gestionan todo el ciclo de vida de creación, envió y
          recepción de mensajes, se conectan a los servidores correspondientes con POP3 o IMAP4 para la recuperación de
          los mensajes y el envío se centraliza también en los servidores con SMTP.
        * ``Clientes ligeros o web``: el usuario accede al sistema de correo a través de una interfaz web con un
          navegador.
        * ``Clientes en dispositivos móviles``: clientes nativos para móviles que utilizan IMAP4 como protocolo de
          recuperación para permitir que posteriormente, los mensajes procesados sean visibles también desde el PC u
          otros clientes.

* > ``Postfix``: servidor de correo de software libre / código abierto, un programa informático para el enrutamiento y envío de correo electrónico, creado con la intención de que sea una alternativa más rápida, fácil de administrar y segura al ampliamente utilizado Sendmail.
* > ``Exim``: agente de transporte de correo desarrollado por la Universidad de Cambridge y puede ser utilizado en la mayoría de los sistemas Unix.

### 2\. ARQUITECTURA DEL PROTOCOLO DE CORREO ELECTRÓNICO EN INTERNET

* Actualmente, el correo electrónico proporciona funciones para el envío y recepción de mensaje de forma asíncrona con
  la posibilidad de adjuntar todo tipo de ficheros y múltiples opciones de formato.
* Admite diversas extensiones de funcionalidad como notificación de entrega, firma electrónica de los mensajes,
  establecimiento de prioridad, listas de correo, envío y reenvío de copias...
* El correo constituye una aplicación en si misma que proporciona conectividad asíncrona extremo a extremo, pero también
  puede considerarse una herramienta o canal de comunicación.
* Actualmente puede establecerse una arquitectura genérica para los sistemas de correo basados en Internet:
    * ``MUA`` (Mail User Agent): sistema que se encarga de recibir y enviar emails usando los protocolos STMP (para el
      envío)
      y POP3 o IMAP (para la recepción). (Ejemplos: evolution, kmail, sylpheed, squirrelmail, Mozilla Thunderbird,
      Microsoft Outlook, webmails como Gmail o outlook...).
    * ``MSA`` (Mail Submission Agent): programa del servidor que recibe correo de un MUA, comprueba si hay errores y lo
      transfiere (con SMTP) al MTA alojado en el mismo servidor.
    * ``MTA`` (Mail Transfer Agent): sistema que se encarga de tomar el email de un MUA o de otro MTA y entregarlo a
      otro MTA o a un MDA, en caso de que el email pertenezca al dominio propio del MTA. (Ejemplos: postfix, qmail,
      exim, Cyrus, courier...).
    * ``MDA`` (Mail Delivery Agent): sistema que se encarga de la recepción del email por parte de un MTA, y lo almacena
      de la forma que tenga configurada. Los MDA pueden almacenar en disco, base de datos o llamar a otro programa para
      hacer el procesado de emails (listas de correo, sistemas de control de incidencias...). (Ejemplos: procmail,
      maildrop...).
    * ``MAA``: (Mail Access Agent, Agente de Acceso de Correo), es el sistema que se encarga del acceso al correo
      almacenado. Sería como la oficina de correos, y por ello su protocolo más usado es POP3 (Post-Office Protocol
      version 3). Se encarga de hacer accesible lo buzones a equipos remotos. (Ejemplos: dovecot, uw, qpopper...).

* > ``ZCS`` (Zimbra Collaboration Suite): programa informático colaborativo o Groupware que consta de un servicio de correo electrónico, posee tanto el componente de servidor como su respectivo cliente.

#### 2.1 PROTOCOLOS DE CORREO ELECTRÓNICO

* La arquitectura de correo en Internet se fundamenta en un conjunto combinado de protocolos básicos en redes TCP/IP, el
  conjunto de protocolos básico que han adquirido el carácter de estándares esta descrito en tres RFC publicados por la
  IETF:
    * ``SMTP``: protocolo de comunicación estándar de Internet para la transmisión de correo electrónico bajo redes
      TCP/IP.
    * ``MAIL``: estándar que versa sobre el formato de los mensajes de correo y que describe la sintaxis de cabeceras de
      un mensaje y los posibles campos a utilizar en la misma, y como deben interpretarse.
    * ``DNS-MX``: estándar para describir el procedimiento de enrutado de los mensajes que se basa en el Sistema de
      Nombres de Dominio (DNS). Cuando un usuario especifica una dirección de correo (un buzón) al que se desea enviar
      un mensaje, tras el símbolo “@” se encuentra el nombre de domino del “host” destino. Para establecer una conexión
      TCP con el mismo, el emisor SMTP deberá en primer lugar realizar una consulta al servidor de nombres
      correspondiente para determinar la dirección IP del equipo remoto, el nombre que figura tras la “@” en la
      dirección de correo no es un nombre de domino completo, los servidores DNS almacenan entradas mensajes MX RR\*
      específicas para la entrega de. Estas entradas mapean el nombre de domino a un valor de preferencia ya que pueden
      existir múltiples entradas MX RR para un nombre y se asigna prioridad a cada una de ellas, y al nombre de dominio
      completo del “host”, deberá utilizarse para establecer la conexión TCP/IP y deberá resolverse nuevamente en el
      DNS.

* > ``Un registro MX`` (Mail eXchange record)
    * > Es un tipo de registro, un recurso DNS que especifica cómo debe ser encaminado un correo electrónico en internet.
    * > Los registros MX apuntan a los servidores a los cuales envían un correo electrónico, y a cuál de ellos debería ser enviado en primer lugar, por prioridad.
    * > Cuando un mensaje de correo electrónico es enviado a través de internet, el remitente (MTA) hace una petición al DNS solicitando el registro MX para los nombres de dominio de destino.
    * > El nombre de dominio es la parte de la dirección de correo que va a continuación de la "@".
    * > Esta consulta devuelve una lista de nombres de dominios de servidores de intercambio de correo que aceptan correo entrante para dicho dominio, junto con un número de preferencia.
    * > Entonces el agente emisor (o remitente) intenta establecer una conexión SMTP (Simple Mail Transfer Protocol) hacia uno de estos servidores, comenzando con el que tiene el número de preferencia más pequeño, y enviando el mensaje al primer servidor con el cual puede establecer una conexión.
    * > Si no hay registros MX disponibles, una segunda petición es solicitada al registro A (A Record) del dominio en su lugar.

##### 2.1.1. SMTP (SIMPLE MAIL TRANSFER PROTOCOL)

* El RFC 5321 define SMTP como un protocolo cliente/servidor, el cliente SMTP es el equipo que inicia una sesión (el que
  envía el mensaje) y el servidor es el equipo que responde a la petición de sesión (y recibe el mensaje).
* Se fundamenta sobre el principio de una entrega extremo a extremo, un cliente SMTP que desee enviar un mensaje a otro
  equipo o servidor en una red TCP/IP se conectara directamente a dicha máquina para transmitir el mensaje sin el empleo
  de nodos intermedios (una clara diferencia con respecto a X.400).
* Se contempla la posibilidad de envíar correo a través de una puerta de enlace de correo con otro tipo de redes, pero
  en tal caso SMTP solo garantiza el envío hasta la puerta de enlace, el envío no corresponde al usuario, sino que se
  centraliza en un equipo que recibe el nombre de servidor de correo.
* La estructura del mensaje transmitido sigue:
    * ``SMTP ENVELOPE``:
        * ``HELLO``: el cliente envía este comando al servidor SMTP para identificarse e iniciar la conversación SMTP y
          el nombre de dominio o la dirección IP del cliente SMTP generalmente se envía como un argumento junto con el
          comando.
        * ``MAIL TO``: especifica la dirección de correo electrónico del remitente. Este comando también le dice al
          servidor SMTP que se está iniciando una nueva transacción de correo y hace que el servidor restablezca todas
          sus tablas de estado y búferes, etc.
        * ``RCPT TO``: Especifica la dirección de correo electrónico del destinatario. Este comando se puede repetir
          varias veces para un mensaje de correo electrónico determinado con el fin de entregar un solo mensaje de
          correo electrónico a varios destinatarios.
    * ``MESSAGE HEADER``: portador de una gran cantidad de información interesante relativa al mensaje y el remitente,
      incluyendo las direcciones y los servidores de email por los que ha pasado. La importancia de la cabecera radica
      en los metadatos que aporta sobre el propio mensaje que permiten tanto su entrega correcta como su interpretación
      por parte del servidor. Delimitada por una línea nula (en blanco) generalmente seguido de un carácter de retorno
      de carro \<CRLF\>. Los campos que contiene son:
        * ``FROM``: emisor del mensaje.
        * ``SUBJECT``: asunto del mensaje.
        * ``DATE``: fecha y hora en la que el mensaje fue enviado.
        * ``TO``: destinatarios principales del mensaje.
        * ``CC``: destinatarios secundarios del mensaje (copia).
        * ``CCO``: destinatarios ocultos del mensaje.
        * ``RETURN-PATH``: dirección y ruta del destino.
        * ``ENVELOPE-TO``: muestra que el correo fue enviado al buzón de correo del destinatario.
        * ``RECIVED``: muestra una lista de todos los equipos por los que el correo ha viajado para llegar al
          destinatario. La primera linea RECIVED el equipo del destinatario.

    * ``MESSAGE BODY``: datos que siguen a la cabecera, secuencias de líneas con caracteres codificados en ASCII.

* > Para hacer frente a las limitaciones impuestas por SMTP en la codificación se han empleado dos mecanismos de extensión al protocolo:
    * > MIME (Multipourpose Internet Mail Extensions): especifica un mecanismo para la codificación de texto y datos binarios sobre una codificación base en ASCII de 7 bits.
    * > Extensiones de servicio SMTP: mecanismo para extender las posibilidades de SMTP, estas extensiones permiten que dos “hosts” TCP/IP negocien un tipo de codificación distinta antes del envío de los mensajes, el equipo receptor indique que puede utilizar codificación ASCII en 8 bits, también permite al receptor especificar el tamaño máximo de mensaje que puede recibir, sobrepasando la limitación de 1000 caracteres.

* SMTP se fundamenta sobre un modelo de comunicación actuando a partir de una petición de usuario, el emisor de SMTP (
  componente lógico) establece una conexión TCP/IP bidireccional con el SMTP receptor, que puede ser o bien el
  destinatario final o un nodo intermedio que implemente una puerta de enlace de correo (esto no debe confundirse con la
  existencia de elementos de encaminamiento de nivel 3 en la red IP). El emisor genera comandos según el protocolo SMTP
  junto con el envío del mensaje, mientras que el receptor responde a su vez con los comandos pertinentes. El flujo
  básico de un envío de mensaje se resume en:
    * 1\. El emisor SMTP establece una conexión TCP con el servidor destino y espera a recibir un mensaje “220
      Serviceready”, junto con el nombre de domino del servidor o bien un mensaje “421 Servicenotaviable”, la conexión
      TCP ha de establecerse en el puerto asignado para SMTP (puerto 25), el servidor destinatario está esperando
      recibir conexiones SMTP para intercambio de mensajes.
    * 2\. Se envía el comando HELO y el receptor se identifica con su nombre de dominio, así el emisor puede comprobar
      si esta efectivamente contactando con el servidor correcto. Si el emisor soporta extensiones de servicio SMTP y
      quiere comprobar si el servidor acepta, sustituye el comando HELO por EHLO.
    * 3\. El emisor inicia la transacción de un mensaje enviando un comando MAIL al receptor, contendrá el camino
      inverso por el que se informará de errores (puede ser un buzón, generalmente el del emisor del mensaje, o una
      dirección IP) si se acepta el servidor responde con un 250 OK.
    * 4\. Envío de los buzones de correo destino del mensaje, se envían tantos comandos RCPT TO como sea necesario con
      la indicación de los nombres de los buzones, para cada uno se recibirá un comando 250 OK si el servidor conoce
      dicho buzón o un “550 Notsuchuser” si el buzón no existe en el servidor.
    * 5\. Cuando se han enviado todos los comandos RCPT el emisor está listo para enviar el propio mensaje y para ello
      envía el comando DATA para notificarlo. El servidor responde “354 Start mail input, endwith \<CRLF\>-\<CRLF\>”. La
      secuencia \<CRLF\>-\<CRLF\> es la que tiene que enviar el emisor para indicar el final del mensaje.
    * 6\. El cliente envía los datos a continuación, línea por línea, incluyendo las cabeceras del mensaje. Se indica el
      final con la secuencia \<CRLF\>-\<CRLF\> y el servidor responde con 250 OK o con un mensaje de error.
    * 7\. Finalmente, si:
        * No hay más mensajes: el emisor termina la conexión con un QUIT y el código 221\.
        * Hay más mensajes de otra parte: se envía el comando TURN y ambos equipos intercambian sus papeles.
        * Hay más mensajes y el emisor es el mismo: el emisor envía un nuevo comando MAIL.

##### 2.1.2. LMTP (Local Mail Transfer Protocol)

* Es un derivado de SMTP para situaciones donde el lado receptor no dispone de cola de correo (el verbo EHLO es
  reemplazado por LHLO), requiere una respuesta por cada comando RCPT previamente aceptado. La mayor diferencia es que
  LMTP rechazara un mensaje si no es derivado de inmediato a su destino final. Elimina la necesidad de una cola de
  correo y evita tener habilitado el puerto 25 (TCP).

##### 2.1.3. POP3 (Post Office Protocol)

* En la arquitectura SMTP el usuario de correo electrónico debe poder interactuar directamente con el equipo físico que
  alberga el repositorio de mensajes y actúa como emisor/receptor SMTP.
* Con la evolución pareja de internet y los PC resultaba inviable este modelo para la recepción de mensajes puesto que
  carecía de lógica implementar un buzón junto con el emisor/receptor SMTP en cada PC de usuario.
* Como solución SMTP adopto en cierto modo la arquitectura definida por X.400, mediante el uso de los agentes de
  transferencia de mensajes (MTA) y los agentes de usuario (UA) separándolos en máquinas físicamente distintas, así nace
  POP.
    * ``POP`` es un protocolo usado en clientes locales de correo para obtener los mensajes de correo electrónico
      almacenados en un servidor remoto, denominado Servidor POP.
    * Es un protocolo de nivel de aplicación en el Modelo OSI.
    * Cuenta con funcionalidades tanto de cliente (para la recepción de mensajes) como servidor (para el almacenamiento
      de los mismos)
      soporta funciones básicas para la consulta y obtención de mensajes de un servidor desde un cliente.
    * Un cliente POP3 establece una conexión TCP con un servidor de correo SMTP (donde se almacena el buzón y se
      ejecutan las funciones de emisor/receptor SMTP) a través del puerto 110\.
    * El servidor POP3 envía un mensaje de bienvenida al cliente y la sesión entra en un modo autenticación.
    * El cliente debe enviar al servidor sus credenciales de autenticación.
    * La sesión entra en modo de transacción, el cliente tiene acceso a su buzón de correo en el servidor y puede
      recuperar todos los mensajes allí almacenados, estos mensajes se almacenarán a su vez en el sistema de ficheros
      local del usuario que utilice el cliente.
    * Lo que se está logrando con OPO3 es implementar de forma eficiente la asincronía en la recepción de mensajes para
      un usuario y la posibilidad de recuperar los mensajes de un buzón a posteriori sin necesidad de mantener una
      conexión permanente con la red.
    * ``POP3`` funciona mediante un modelo de comandos en modo carácter, consisten en una pablara clave y uno o más
      argumentos que la siguen. El servidor envía una respuesta al comando emitido por el cliente, y debe comenzar con
      un indicador de estado que puede ser (+OK) o (-ERR) para indicar el éxito o no de la operación.
    * El protocolo distingue tres estados:
        * ``Estado de autenticación``: el cliente envía información de autenticación al usuario mediante los comandos
          USER y PASS o bien con el comando APOP.
        * ``Estado de transacción``: el cliente es capaz de enviar comandos para listar, recuperar y borrar mensajes en
          su buzón de correo (STAT, LIST, RETR y DELE). Las opciones de edición requieren entrar en el siguiente estado
          mediante el comando QUIT.
        * ``Estado de actualización``: el servidor actualiza el contenido del buzón.

#### 2.4. IMAP4

* Protocolo de aplicación que permite el acceso a mensajes almacenados en un servidor de Internet que funciona bajo TCP
  en los puertos 143 (modo seguro bajo 993).
* Presenta mejoras y funciones avanzadas respecto a POP3, al igual que este funciona bajo el paradigma cliente/servidor,
  el servidor IMAP4 es capaz de almacenar mensajes para múltiples usuarios de forma que estos pueden recuperarlos a
  posteriori.
* La diferencia fundamental con POP3 es que IMAP4 presenta un modelo de sincronización de mensajes entre el cliente y el
  servidor frente al modelo de recuperación de mensajes de POP3, IMAP4 siempre almacena los mensajes de un usuario en el
  servidor y replica la copia de los mismos al usuario, este puede a su vez trabajar sobre la réplica del buzón en modo
  desconectado y al volver a conectarse scon el servidor se sincronizaran los cambios, IMAP4 es capaz de
  trabajar: ``sin conexión, conectado o desconectado.``
* Otra ventaja de IMAP4 es su capacidad de interpretar el contenido MIME.
* Cuando un cliente IMAP4 establece una conexión TCP con el servidor, este envía también un mensaje de bienvenida y a
  partir de entonces, cliente y servidor intercambian datos de forma interactiva.
* Para cada comando enviado por el cliente, el servidor responde con el resultado de la operación.
* Todos los comandos se formatean como líneas terminadas en \<CRLF\>.
    * → Quiere decir que cada comando se escribe como una línea de texto que termina con los caracteres
    * <CRLF>, que son el estándar de fin de línea en los protocolos de Internet:
        * \<CR> = Carriage Return (retorno de carro, \r).
        * \<LF> = Line Feed (salto de línea, \n).
* Cada respuesta del servidor incluye la marca identificativa, seguida de un código de estado que puede
  ser ``OK, NO o BAD.``

## TEMA 5 – MONITORIZACIÓN, ADMINISTRACIÓN DE REDES Y HARDWARE

### 1\. MONITORIZACIÓN Y CONTROL DE TRÁFICO

* El método de inventario cada vez más frecuente consiste en recoger información empleando la propia red a la que están
  conectados los dispositivos, los inventarios basados en red reducen significativamente el tiempo y el coste de las
  auditorias, permiten realizar inventario programados de forma regular y con ellos se dispone de información más
  actualizada.
* Hay aplicaciones que permiten la distribución de software en ambientes multiplataforma a todo tipo de clientes como
  Microsoft Systems Management Server, herramientas de cliente de acceso remoto para conectarse a servidores que
  ejecuten servicios o programas como ``VNC``, ``Team Viewer``, ``Citrix``...
    * ``Nagios``: sistema de monitorización de código abierto, vigila los equipos (hardware) y servicios (software) que
      se especifiquen, alertando cuando el comportamiento de los mismos no sea el deseado. Entre sus características
      principales figuran la monitorización de servicios de red (SMTP, POP3, HTTP, SNMP...), la monitorización de
      recursos de sistemas hardware (carga del procesador, uso de los discos, memoria, estado de los puertos...),
      independencia de sistemas operativos, monitorización remota mediante túneles SSL cifrados o SSH, y posibilidad de
      programar plugins específicos para nuevos sistemas.
    * ``RADIUS`` (Remote Authentication Dial-In User Service): protocolo de autenticación y autorización para
      aplicaciones de acceso a la red o movilidad IP. Utiliza el puerto 1812 UDP. Una de las características más
      importantes del protocolo RADIUS es su capacidad de manejar sesiones, notificando cuándo comienza y termina una
      conexión, así que al usuario se le podrá determinar su consumo y facturar en consecuencia; los datos se pueden
      utilizar con propósitos estadísticos. Las prestaciones pueden variar, pero la mayoría pueden gestionar los
      usuarios en archivos de texto, servidores LDAP, bases de datos varias, etc. A menudo se utiliza SNMP para
      monitorear remotamente el servicio. Los servidores Proxy RADIUS se utilizan para una administración
      centralizada.  
      Surge la necesidad de una gestión de integridad y monitorización desde un solo sistema que presenta sus
      interconexiones en un mapa de la red a través de plataformas como:
        * ``Apache Chukwa`` es un sistema de recopilación de datos de código abierto para monitorear grandes sistemas
          distribuidos.
        * ``HCL AppScan`` (IBM Appscan): familia de herramientas de monitoreo y prueba de seguridad web y de escritorio,
          diseñado para probar aplicaciones web y locales en busca de vulnerabilidades de seguridad durante el proceso
          de desarrollo, cuando es menos costoso solucionar dichos problemas.
        * ``OpenView``: gestión de redes y sistemas a gran escala de la infraestructura de TI de una organización. El
          producto fundamental de OpenView fue Network Node Manager (NNM), software de monitoreo de red basado en SNMP.
          NNM se usó para administrar redes y podría usarse junto con otro software de administración, como CiscoWorks (
          familia de herramientas integrales para la gestión de redes que permiten y facilitan el acceso de los
          administradores de red a las capacidades avanzadas de voz, video y datos), entre ellas se encuentra CiscoView,
          un software de gestión de dispositivos de red, configuración y monitorización de dispositivos, aplicación
          basada en web.
        * ``SunNet Manager``: sistema de gestión de red principal de Sun Microsystems. Se utiliza para monitorear y
          mejorar el desempeño en redes multiprotocolo. ``BayNetworks Optivity``: sistema escalable para configurar
          redes complejas. Introduce NETarchitect, el paquete de administración a nivel del sistema de la compañía que
          automatiza la configuración de redes ATM sofisticadas. 3Com’s ``Transcend``: gestionar toda la red como un
          único sistema integrado más que como una serie de unidades independientes, incluye soluciones de hardware y
          software para aumentar las prestaciones de las redes corporativas, ampliar su alcance y gestionar su
          crecimiento.

***

* > La metodología de análisis y gestión más utilizado en la administración española es ``Magerit`` (Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información):
    * > Está elaborada por el ``Consejo Superior de Administración Electrónica del Gobierno de España`` para minimizar los riesgos de la implantación y uso de las Tecnologías de la Información.
    * > Ofrece una aplicación para el análisis y gestión de riesgos de un Sistema de la Información.
    * > Herramientas comerciales de ``Magerit``:
        * > ``GxSGSI``: Herramienta de Análisis y Gestión de Riesgo basada en ``Magerit`` y homologada por la Agencia Europea de Seguridad de la Información.
        * > ``R-Box``: Herramienta de Análisis y Gestión de Riesgo basada en ``Magerit``.
        * > ``SECITOR``: Herramienta de Análisis y Gestión de Riesgos de alto nivel que permite la gestión integral de la Seguridad de la Información siendo un sistema multimarco (ISO 27001, Protección de datos, ENS, ISO 19001, etc), además de una monitorización en tiempo real de la seguridad de la organización.
        * > ``EAR / PILAR``: Entorno de análisis de riesgos.

***

#### 1.1. ADMINISTRACIÓN DE RED

* Son estándares y protocolos de gestión de red que siguen modelos de gestión integrada, permiten la interconexión
  abierta entre los recursos de telecomunicación y las aplicaciones de gestión de red:
  ***
    * ``SNMP``: protocolo de la capa de aplicación que facilita el intercambio de información de administración entre
      dispositivos de red usando pocos recursos y de forma simple, emplea como protocolo de capa de transporte tanto TCP
      como UDP en los puertos 161 y 162 (cuando se usa con TLS funciona en los puertos 10161 y 10162).
    * Los dispositivos que normalmente soportan SNMP incluyen routers, switches, servidores, estaciones de trabajo,
      impresoras...
    * Una red administrada a través de SNMP está organizada en jerarquías, las cuales junto con otros metadatos (tales
      como el tipo y la descripción de la variable), se describen por Bases de Información de Gestión (MIB). El
      protocolo SNMP consta de tres componentes clave:
        * ``Sistemas administradores de red`` (Network Management Systems, NMS): ejecuta aplicaciones que supervisan y
          controlan a los dispositivos administrados, proporcionan el volumen de recursos de procesamiento y memoria
          requeridos para la administración de la red.
        * ``Dispositivos administrados``: recogen y almacenan información de administración a través de un agente, la
          cual es puesta a disposición de los NMS’s.
        * ``Agentes``: módulo de software de administración de red que reside en un dispositivo administrado. Un agente
          posee un conocimiento local de información de administración (memoria libre, número de paquetes IP recibidos,
          rutas...), la cual es traducida a un formato compatible con SNMP y organizada en jerarquías.

    * > MIB (Management Information Base): colección de información que está organizada jerárquicamente.
    * > Las MIB son accedidas usando un protocolo de administración de red, como por ejemplo, SNMP.
    * > Un objeto administrado (algunas veces llamado objeto MIB, objeto, o MIB) es uno de cualquier número de características específicas de un dispositivo administrado.
    * > Los objetos administrados están compuestos de una o más instancias de objeto, que son esencialmente variables.

    * Para realizar las operaciones básicas de administración el protocolo SNMP utiliza un servicio no orientado a la
      conexión (UDP) para enviar un pequeño grupo de mensajes (PDUs) entre los administradores y agentes, se utilizan
      varios tipos de mensajes SNMP:
        * ``GetRequest``: solicita al agente retornar el valor de un objeto de interés mediante su nombre. En respuesta
          el agente envía una respuesta indicando el éxito o fracaso de la petición. Este mensaje puede ser usado para
          recoger un valor de un objeto, o varios valores de varios objetos, a través del uso de listas.
        * ``GetNextRequest``: usado para repetir la operación con el siguiente objeto de la tabla, es decir, es usado
          para recorrer una tabla de objetos.
        * ``SetRequest``: solicitar a un agente modificar valores de objetos.
        * ``GetResponse``: usado por el agente para responder un mensaje GetRequest, GetNextRequest, o SetRequest.
      ***
    * ``CMIP`` (Common Management Information Protocol): protocolo de gestión de red que se implementa sobre el modelo
      de interconexión de redes abiertas OSI.
    * Provee un modo de que la información de control y de mantenimiento pueda ser intercambiada entre un gestor (
      manager) y un elemento remoto de red, pero requiere 10 veces más recursos que SNMP.
    * Los managers residen en las estaciones de gestión mientras que los procesos agentes residen en los elementos de
      red.
    * CMIP define una relación igual a igual entre el gestor y el agente en lo referido al establecimiento y cierre de
      conexión y a la dirección de la información de gestión, las operaciones CMIS (Common Management Information
      Services) y CMISE (Common Management Information Service Element), se pueden originar tanto en gestores como en
      agentes.
    * Para comunicarse entre sí dos entidades de aplicación pares del gestor y del agente se utilizan APDUs (Application
      Protocol Data Units). CMIP se implementa en asociación con los protocolos ACSE y ROSE.
        * ``ACSE`` (Association Control Service Element): establece y libera asociaciones entre entidades de aplicación,
          el establecimiento lo puede realizar el agente o el gestor.
        * ``ROSE`` (Remote Operation Service Element): equivalente OSI a una llamada de un procedimiento remoto, permite
          la invocación de una operación en un sistema remoto. CMIP usa los servicios orientados a conexión para todas
          las peticiones, respuestas y respuestas de error.
      ***
    * > CMOT (CMIP over TCP/IP): arquitectura de gestión de red usando los protocolos CMIS/CMIP del modelo OSI sobre la familia de protocolos de internet (TCP/IP).
      ***
    * ``DMI`` (Desktop Management Interface): framework estándar para gestión y seguimiento de componentes en un
      ordenador de sobremesa, portátil o servidor, creando una abstracción de esos componentes desde el software que los
      gestiona.
    * DMI puede coexistir con SNMP y otros protocolos de gestión. Una estación de trabajo aislada o un servidor pueden
      actuar como agente proxy y contener el módulo SNMP de un segmento de la red local (LAN) con equipos dotados de
      DMI.
      ***
    * ``RMON`` (Remote Network Monitoring): especificación de monitoreo estándar que permite que varios monitores de red
      y sistemas de consola intercambien datos de monitoreo de red.
    * RMON brinda a los administradores de red más libertad para seleccionar sondas de monitoreo de red y consolas con
      características que satisfacen sus necesidades particulares de red.
    * Los dispositivos de monitoreo (comúnmente llamados "sondas" en este contexto), contienen agentes de software RMON
      que recopilan información y analizan paquetes.
    * Estas sondas actúan como servidores y las aplicaciones de administración de red que se comunican con ellas actúan
      como clientes.
    * Si bien tanto la configuración del agente como la recopilación de datos utilizan SNMP.
    * En resumen, RMON está diseñado para la supervisión "basada en el flujo", mientras que SNMP se utiliza a menudo
      para la gestión "basada en el dispositivo"
      .
      ***

### 1\. EQUIPOS TERMINALES Y EQUIPOS DE INTERCONEXIÓN Y CONMUTACIÓN

* ``Dispositivos finales`` (hosts): su función principal es permitir que determinadas aplicaciones y/o usuarios
  intercambien información entre sí, utilizando para ello servicios proporcionados por la red, son generadores y/o
  consumidores de información, implementan las siete capas del modelo OSI, utilizan los servicios de las capas
  inferiores para acceder finalmente a la capa física de la red (estaciones de trabajo, servidores, impresoras...)
* ``Dispositivos intermedios`` (elementos de interconexión de redes): su función principal es servir de intermediarios
  entre los dispositivos finales, su objetivo fundamental es hacer llegar la información desde el origen hasta el
  destino.
* Los activos de red se clasifican según la capa del modelo OSI en el que desempeñan sus funciones:
    * ``Capa 1 o capa física``: repetidores y concentradores (o hubs).
      ***
        * ``Repetidores``: es un dispositivo intermedio de capa física cuyo objetivo es regenerar y resincronizar los
          bits de las señales de transmisión de datos, surge de la necesidad de llevar la información las allá de los
          limites físico impuestos por los medios de transmisión pasivos (cables de cobre, fibra óptica...) por el
          efecto de la atenuación. Un repetidor clásico tiene dos interfaces, recibe la señar por una y la regenera,
          resincroniza y transmite por la otras, no utiliza ningún tipo de lógica a la hora de retransmitir la señal.
      ---   
    * > Se define como dominio de colisión el conjunto de dispositivos que compite por utilizar un mismo medio físico para transmitir datos, este concepto se utiliza habitualmente en las tecnologías basadas en acceso al medio múltiple por detección de portadora (Carrier Sense Multiple Access).
    * > La adición de repetidores hace que el dominio de colisión sea mayor, permite que más dispositivos compartan el mismo medio físico, se puede afirmar que los repetidores amplían el domino de colisión, al existir un mismo medio físico con un ancho de banda constante, el ancho de banda disponible para cada uno de los elementos finales de la red será menor.
      ___
        * Los repetidores eran típicos en las redes Ethernet antiguas, utilizaban topologías físicas y lógicas en bus,
          como 10-BASE-2 o 10-BASE-5. En la actualidad se utilizan en las grandes redes WAN de transporte basadas en
          fibra óptica y en las redes inalámbricas.
      ***
        * ``Concentradores`` (hub): dispositivo activo de red que, además de actuar como repetidor, permite concentrar
          la conectividad de la red, facilitando la transición de una topología física en bus a una topología física en
          estrella o en estrella extendida, recibe una señal por una interfaz o puerto, la regenera, resincroniza y
          transmite por las demás interfaces. Esto provoca que, a pesar de que la topología física de la red sea una
          estrella, su funcionamiento lógico sea el de un bus. Al igual que los repetidores, un hub amplia el domino de
          colisión de una red, es decir, cuando se añade un concentrador a la red existe la posibilidad de incorporar
          más dispositivos que compiten por el mismo medio físico, obliga a compartir el ancho de banda disponible entre
          todos los equipos conectados.
      ***
    * ``Capa 2 o capa de enlace de datos``: puentes (bridges) y conmutadores (switches).
      ***
        * ``Puentes`` (bridge): dispositivo de interconexión de redes que funciona en la capa 2\.
        * Surgieron de la necesidad de reducir el tamaño de los dominios de colisión y del hecho de que la mayor parte
          de las comunicaciones en una red de área local se realizaba con equipo próximos dentro de la misma red física.
        * Un puente dispone de una tabla de conmutación en la que a cada dirección MAC conocidas se le asigna el puerto
          o interfaz que permiten alcanzar el dispositivo en cuestión, cuando un puente recibe una trama, examina la
          dirección de capa 2 de destino de dicha trama, la dirección MAC de destino y la envía por el puerto que tiene
          asociado.
        * SI la MAC de destino no se encuentra en la tabla de conmutación, la rama es enviada por todos los puertos del
          puente, excepto el que tiene asociado.
        * El puente antes de retransmitir la trama comprueba si el medio físico esta libre, en caso de que este ocupado,
          el puente almacena temporalmente hasta que el medio físico se libere, un puente puede almacenar temporalmente
          múltiples tramas.
        * Se puede decir que un puente rompe un domino de colisión único en dos dominios de colisión, en este caso los
          dispositivos finales del segmento A y el puerto del puente competirán por le medio físico correspondiente a la
          LAN A y los dispositivos del segmento B junto con el puerto 2 del puente competirán por le medio físico de la
          LAN B.
      ***
        * ``Conmutadores`` (switch): es un dispositivo de interconexión de red de capa dos que además de actuar como un
          puente, permite concentrar la conectividad de la red.
        * La diferencia fundamental entre un conmutador y puente multipuerto es que el conmutador realiza todas las
          funciones de aprendizaje de direcciones, determinación de puerto y conmutación de trama por hardware. Además,
          los switches suelen presentar una densidad de puertos mucho mayor que los puentes.
        * Los conmutadores presentan diferentes modos de envío de tramas, permiten optimizar su rendimiento, los dos
          modos de envió principales son:
            * ``Modo de almacenamiento y envío`` (store and forward): el conmutador recibe la trama completa, la
              almacena en un búfer de memoria RAM, calcula el “checksum” de capa 2, y si el cálculo es correcto, la
              trama se reenvía por el puerto o puertos indicados. En caso contrario, la trama no se envía y simplemente
              ese elimina de la memoria del switch (se descarta), presenta como ventaja que las tramas erróneas no se
              propagan de un segmento a otro. Tiene como principal inconveniente una alta latencia.
            * ``Modo de conmutación rápida``: la trama comienza a enviarse hacia el destino una vez que se ha leído la
              dirección MAC destino de la misma (la trama Ethernet comienza con una cabecera de 8 bytes de preámbulo, 6
              bytes de MAC origen y 6 bytes de MAC destino). Este método presenta como ventaja una latencia baja y
              constante, pero adolece de mecanismos para evitar la retrajimos de tramas erróneas.
      ***
        * Un ``switch`` es un dispositivo de naturaleza ``“full-duplex”``, gestiona de forma independiente las tramas
          entrante y las salientes, y puede almacenarlas de forma temporal en caso de congestión, algunos incorporan un
          software que facilita la creación de grupos de puertos que se comportan como LANs separadas, se las denomina
          VLAN, con el fin de extender esta funcionalidad a través de múltiples switches, es necesario utilizar enlaces
          que puedan transportar tramas de múltiples VLANs, se les denomina “enlaces troncales”, es necesario
          identificar a que VLAN pertenece cada una de las tramas, antes de transmitir la trama por dicho troncal, para
          ello se desarrolló el IEEE 802.1Q que permite etiquetar las tramas Ethernet, añadiendo un campo de 4 bytes a
          dicha cabecera que identifica la VLAN.
  *** 
    * ``Capa 3 o capa de red``: encaminadores (routers)
  ***
    * ``Encaminadores`` (router): dispositivo de interconexión de redes de capa 3, cuyo objetivo es conectar redes
      lógicas diferentes, determinado la ruta (enrutamiento) y trasmitiendo el paquete por la interfaz adecuada.
    * Un router determina la interfaz de salida o ruta en función de la dirección IP de destino, para ello el router
      construye una tabla en memoria denominada tabla de enrutamiento donde se almacena información de todas las redes
      conocidas, indicando que interfaces se deben utilizar para alcanzarlas.
    * Se puede generar de forma estáticas (rutas configuradas manualmente por un administrador), los encaminadores
      utilizan protocolos de enrutamiento, como pueden ser RIP, OSPF, EIGRP, IS-IS, o BGP, la necesidad de enrutadores
      se debe a dos causas fundamentales:
        * Interconectar redes con diferentes tecnologías y distantes fiscalmente.
        * Acotar los tamaños de los dominios de difusión (broadcast): en Ethernet se utilizan un tipo de tramas/paquetes
          especiales denominados de difusión (broadcast) inundado, dichos paquetes se caracterizan por tener como
          dirección IP de destino 255.255.255.255 y las tramas tienen la dirección FF-FF-FF-FF-FF-FF.
        * Estas tramas y paquetes son recibido y procesado por todos los dispositivos de la red en cuestión, además este
          tráfico es necesario para el funcionamiento de la propia red, y por tanto no puede ser eliminado (el protocolo
          ARP que permite obtener una MAC asociada a una determinada IP se basa en transmisión de tráfico broadcast).
        * Es necesario mantener el tamaño de los dominios de broadcast restringido (si la dirección IP de destino del
          paquete pertenece a la misma red lógica que el propio equipo, se busca la dirección MAC del destino mediante
          una petición ARP, si la dirección destino del paquete pertenece a una red lógica diferente se utiliza la
          dirección MAC del encaminador de salida preferido del equipo para dicha red), se entiende que cuando dos
          equipos se ubican en dominios de broadcast diferentes, será necesario un router para pasar el paquete de un
          domino de difusión a otro.

***

* > Los “hubs” y “switches” hacen crecer el domino de difusión o de broadcast mientras que un router cera tantos dominios de difusión como interfaces tiene operativas. GLBP (Gateway Load Balancing Protocol): protocolo propietario de Cisco que intenta superar las limitaciones de los protocolos de router redundantes existentes añadiendo la funcionalidad de balanceo de carga.

***

* ``Capa 7 o capa de aplicación``: pasarelas de aplicación (ALG) y proxies.
    * ``Pasarelas`` (gateway): es cualquier tipo de dispositivo que sea capaz de enrutar paquetes IP, en ellas se debe
      definir una dirección IP para cada equipo, una macara y la dirección IP de la “pasarela” que es el router, se
      encarga de enviar hacia el destino los paquetes dirigidos a direcciones de red remota, también existen nuevos
      términos que se asocian con el concepto pasarela:
        * ``Application Level Gateway`` (ALG): agentes de traducción de la capa de aplicación que permiten a una
          aplicación específica, comunicarse con su “peer” ubicado en otro dominio de direccionamiento transparente para
          ambas aplicaciones.
        * Los ``ALG`` son los encargados de que dos aplicaciones de este tipo puedan comunicarse entre sí de forma
          transparente sin tener que considerar las traducciones de dirección IP y puertos que haya que realizar en la
          capa de aplicación.
        * Los ALG pueden interactuar con NAT para configurar el estado de la conexión, son similares a los “proxies”,
          ambos facilitan la comunicación de aplicaciones específicas entre cliente y servidor.
        * A diferencia de los “proxies”, los ALG no necesitan cambiar ningún tipo de configuración en los clientes de
          aplicación.
        * Esta se realiza de forma transparente para dichos clientes.
  ---
    * Un “``proxy``” es un servidor que escucha las peticiones de un determinado servicio o conjunto de servicios de sus
      clientes y reenvía dichas peticiones a otros servidores, recoge también las respuestas de los servidores y las
      reenvía a los clientes originales, puede modificar la petición del cliente o la respuesta del servidor, e incluso
      proporcionar el recurso al cliente sin contactar con el poseedor del recurso original lo cual acelera el proceso
      de respuesta.
    * A los “proxy servers” que reenvían todas sus peticiones y respuestas sin ningún tipo de modificación se les
      denomina “túneles proxy o pasarelas”.
  ---

## 2\. REDES DE COMUNICACIONES, DIFUSIÓN Y CONMUTACIÓN

* En los inicios de las comunicaciones los dispositivos electrónicos transmitían información entre si directamente
  mediante conexiones punto a punto, este planteamiento dejo de ser válido debido tanto a las grandes distancias como la
  naturaleza multipunto de las comunicaciones.
* La solución fueron las redes de comunicaciones, es un conjunto de dispositivos, finales e intermedios conectados entre
  sí de formal que pueden intercambiar información.
* Las redes de comunicaciones se pueden clasificar en base a diferentes criterios:
* En cuanto a la tecnología de transmisión:

***

* ``Redes de difusión``: utilizan un solo canal de comunicación compartido por todas las máquinas de la red, el
  dispositivo origen envía mensajes cortos (denominados datagramas), recibidos por todos los dispositivos de la red, las
  maquinas comprueban si la dirección de destino de dicho paquete es la suya propia, en ese caso, procesan el paquete en
  caso contrario lo ignoran (tráfico unicast).

***

* ``Redes punto a punto``: se construyen a partir del establecimiento de múltiples  
  interconexiones entre pares individuales de dispositivos, para ir desde el origen al destino puede que un paquete
  tenga que atravesar diferentes dispositivos intermedio. Es posible que existan múltiples rutas o caminos con
  diferentes distancias hacia el destino. El enrutamiento determina cual es el mejor camino para alcanzar el destino
  desde un determinado punto.

  ***

* ``En cuanto al ámbito geográfico o escala``:
  ***
    * ``Red de área local`` (LAN): redes privadas cuyo ámbito está restringido habitualmente a un edificio o conjunto de
      edificios próximos.
    * La privacidad es una característica calve de este tipo de redes, no es necesario contar con los servicios de una
      empresa y organización externa para implementar este tipo de redes, se utilizan habitualmente para conectar
      dispositivos que pertenecen a una misma organización.
    * Las LAN utilizan tecnologías que permiten velocidades de transmisión entre los 10 Mbps y los 100 Gbps siendo las
      variantes derivadas de la tecnología Ethernet.
    * Su topología puede ser tanto bus (Ethernet o IEEE 802.3) como anillo (Token Ring o IEEE 802.5), la incorporación
      de las comunicaciones “full-duplex” en la tecnología Ethernet (802.3x) ha permitido que las LAN pasen a ser punto
      a punto, utilizando las topologías de estrella y estrella extendida.
  ***
    * ``Redes de Área Metropolitana`` (MAN): es una red que abarca el área geográfica de una ciudad, puede ser publica (
      acceso proporcionado por un proveedor de servicios), como privada. La definición, desarrollo e implantación de la
      tecnología WIMAX, basada en el estándar IEEE 802.16 ha provocado que las redes MAN sea una buena solución para
      proporcionar fundamentalmente acceso a internet en área de baja densidad de población.
  ***
    * ``Redes de Área Extensa`` (WAN): áreas geográficas extensas, la infraestructura proporcionada habitualmente por
      empresas u organizaciones denominadas Proveedores de Servicios de Comunicaciones. La interconexión entre los
      diferentes dispositivos intermedios de una WAN se realiza fundamentalmente utilizado tecnologías de red punto a
      punto con lo que las topologías son: estrella extendida, anillo, árbol, malla parcial y malla completa. Se
      clasifican por el modo de conmutar los datos entre los dispositivos origen y destino:
        * ``Conmutación de circuitos``: intercambiar datos entre dos equipos finales es necesario que se establezca
          previamente un camino dedicado a través de los nodos intermedios una secuencia de enlaces físicos entre los
          nodos origen y destino, donde existe un canal lógico dedicado para la conexión. Ejemplo: redes basadas en Red
          Telefonía Básica (RTB)
          y Red Digital de Servicios Integrados (RDSI).
        * ``Conmutación de paquetes``: no es necesario asignar recursos “a priori” para construir un camino para los
          datos, se envían en unidades de datos pequeñas denominadas datagramas, se pasa de un nodo al siguiente
          tomándose las decisiones de envío en cada dispositivo en el momento previo a la transmisión Ejemplo: X.25
        * ``Conmutación de tramas``: mientras en la conmutación de paquetes las decisiones de envió se realizan en
          función de cabeceras y direcciones de capa 3, en la conmutación de tramas estas decisiones se toman en función
          de direcciones y cabeceras de capa 2\. Ejemplo: Frame Relay.
        * ``Conmutación de celdas``: evolución de la conmutación de tramas, la mayor diferencia que este tipo de redes
          presenta es que se utilizan tramas de tamaño fijo y pequeño denominadas celdas. Ejemplo: Asynchronous Transfer
          Mode (ATM).

***

* ``En cuanto a topologías``: disposición de los dispositivos que forman parte de una red de comunicaciones en relación
  con el medio de transmisión utilizado.
  ***
    * ``Redes de difusión``:
        * ``Bus``: estaciones de trabajo se distribuyen linealmente a lo largo del medio de transmisión abierto. El
          mensaje enviado se envía en ambos sentidos del medio físico por lo que dicho mensaje será recibido por todos
          los dispositivos. Ejemplo: 10-BASE-5, 10-BASE-2, ...
        * ``Anillo``: estaciones de trabajo se distribuyen a lo largo de un medio de transmisión cerrado, el mensaje
          enviado es enviado en un único sentido por lo que termina llegando de nuevo a la estación origen que lo retira
          del medio físico.
  ***
    * ``Redes punto a punto``:
        * ``Estrella``: todas las estaciones se conectan a un dispositivo central, se encarga de enviar los mensajes
          recibidos al destino adecuado. Se establecen tantas conexiones punto a punto como dispositivos están
          conectados al dispositivo de interconexión.
        * ``Estrella extendida``: un dispositivo de interconexión para comunicar diferentes redes en topología de
          estrella.
        * ``Anillo``: las estaciones de trabajo se distribuyen a lo largo de un medio de transmisión cerrado. El mensaje
          enviado por una estación es enviado en un único sentido por lo que termina llegado de nuevo a la estación
          origen que lo retira del medio físico.
        * ``Árbol``: cuando la estrella extendida tiene un único punto central o raíz, se dice que tiene estructura de
          árbol.
        * ``Malla parcial``: se conectan entre sí, sin seguir un patrón, pero ningún nodo puede permanecer aislado.
        * ``Mall completa``: todos los dispositivos de la red se conectan directamente con todos los demás dispositivos
          de dicha red.

***

### 3\. REDES INALÁMBRICAS

* Son aquellas que posibilitan la interconexión de dos o más equipos entre si sin que intervengan cables. Se basan en un
  enlace que utiliza ondas electromagnéticas. Dependiendo del tamaño:
    * ``WPAN``: redes de corto alcance generalmente para conectar dispositivos periféricos. Ejemplos: Bluetooth (
      802.15.1), Zigbee (802.15.4), HomeRF
    * ``WLAN``: redes de área local basadas en tecnologías como HiperLAN o Wi-Fi (IEEE 802.11).
    * ``WMAN``: redes de área metropolitana basadas en IEEE 802.16 o WIMAX, así como en LMDS (Local Multipoint
      Distribution Service).
    * ``WWAN``: redes inalámbricas de área extensa (LTE, UMTS, GPRS)

***

#### 3.1. REDES WIFI

* Redes inalámbricas que se rigen por los estándares IEEE 802.11, siguen en líneas generales lo dispuesto en el 802.3
  genérico. Así, se emplean un mecanismo de acceso al medio basado en CSMA (Carrier Sense Medium Access) pero necesitan
  una capa física (PHY) y de acceso al medio (MAC) específicas para poder utilizar el espectro radioeléctrico.

##### 3.1.1. CAPA FÍSICA

* Utilizan dos banas, 2.4GHz (en este rango actúan también tecnologías como Bluetooth, HomeRF...) y 5GHz.
* Hay ``tres aspectos`` fundamentales relacionados con la ``capa física``:
    * ``Velocidad de transmisión``: la tasa de transmisión dependerá del estándar del dispositivo para 801.11b el límite
      superior estará en los 11 Mbps, para 802.11a y 802.11b en 54 Mbps; 802.11n en los 600 Mbps y 802.11ac en 1,3 Gbps.
    * ``Potencia de transmisión``: a mayor potencia el punto de acceso tendrá un mayor rango de cobertura, en España el
      máximo límite legal es 100nW en el rango de 2,4 GHz y 200nW en 5 GHz.
    * ``Número de canales``: identifica el subrango de frecuencias de trabajo específicos, en la banda de 2,4 GHz
      canales del 1 a 13, se trata de canales separados 5 MHz pero que tienen un ancho de banda analógico de 22 MHz de
      modo que los canales contiguos se solapan creando interferencias. Las técnicas de modulación usadas (OFDM) en el
      caso de 802.11g y DSSS en el caso de 802.11b hacen que la señal sea muy robusta frente a tales interferencias, por
      tanto, los canales óptimos a usar en punto de acceso adyacentes para eliminar el solapamiento son 1, 7 y 13\.
      *** 
    * Respecto a las técnicas empleadas por IEEE 802.11 para realizar la trasmisión por radiofrecuencia destaca la
      utilización de técnicas de modulación por espectro ensanchado (spread spectrum) se basan en la transmisión de una
      señal con un ancho de banda mucho mayor del ancho de banda del mensaje original mediante la aplicación al mismo de
      una señal adicional conocida como código mensaje original mediante la aplicación al mismo de una señal adiciona
      conocida como código ensanchado (spreading code).
  ***
    * ``Los sistemas de espectro ensanchado presentan dos grandes etapas``:
        * ``Empleo de baja densidad de potencia``: la energía transmitida por un ancho de banda mucho mayor, la cantidad
          de energía aplicada a cada frecuencia es muy baja, la señal no interferirá con otros receptores.
        * ``Incorporación de redundancia``: el mensaje está presente sobre diferentes frecuencias de las que se puede
          recuperar en caso de error, alta resistencia a interferencias y ruido.
      ***
    * Las ``técnicas de espectro ensanchado`` se componen de dos procesos de modulación consecutivos a ejecutar sobre la
      señal portadora: un primer proceso ejecutado por el código ensanchado y un segundo proceso ejecutado sobre el
      mensaje, podemos distinguir entre ``dos técnicas`` fundamentales:
  ***
    * ``FHSS`` (Frecuency Hopping Spread Spectrum): la frecuencia portadora a utilizar se modifica periódicamente, el
      mensaje se modula sobre la portadora utilizando FSK, genera una señal de banda estrecha durante el periodo de
      salto, pero de banda ancha si se observa el canal en intervalos de tiempo de varios segundos.
  *** 
    * ``DSSS`` (Direct Sequence Spread Spectrum): la señal a transmitir utiliza todo el ancho de banda del canal
      asignado, modula mediante PSK siguiendo una secuencia de bits específica.
    * El número de códigos ortogonales existentes para un sistema CDMA depende de la longitud en bits del chip.
    * Las técnicas de espectro ensanchado tienen como inconveniente principal la complejidad añadida en los emisores y
      receptores para el ensanchado y desenganchado del espectro, incide en la velocidad de transmisión que se puede
      conseguir.
  ***
    * ``OFDM`` (Ortogonal Frequency Division Multiplexing): el ancho de banda asignado se divide en canales y la señal a
      enviar se divide en tramas, cada una de ellas es modulada por la frecuencia subportadora de cada canal. Esta
      técnica busca optimizar el canal de comunicaciones.
  ***

##### 6.1.2. SUBCAPA DE ACCESO AL MEDIO

* En las redes cableadas basadas en 802.3, los terminales utilizan un método de acceso al medio compartido conocido
  como:
    * ``CSMA/CD`` (Carrier Sense Medium Access/Collision Detection) en el que el emisor, durante el tiempo de
      transmisión de una trama, está escuchando el medio para comprobar si se ha producido una colisión con otro emisor
      que hubiese comenzado a transmitir al mismo tiempo, de detectarse esta circunstancia, el emisor detiene la
      transmisión en curso y espera un tiempo aleatorio para volver a retransmitir la trama dañada.
    * Este mecanismo tiene unas buenas prestaciones en medios guiados como el par trenzado, sin embargo, para medios no
      guiados como el aire, no es posible aplicar el mecanismo de detección de colisiones al no poder el terminal
      realizar escuchas simultaneas durante la transmisión, IEEE 802.11 ha adoptado en su capa MAC el protocolo DCF (
      Distributed Control Function) una variante de CSMA conocida como CSMA/CA (
      Carrier Sense Medium Access/Collision Avoidance) con ACK.
      ***
    * ``CSMA/CA`` define ``dos modos de operación:``
      ***
        * ``Detección de canal físico``: al utilizar CSMA/CA un emisor que desee transmitir una trama realiza una
          verificación previa del estado del radio canal, si detecta que dicho canal se encuentra inactivo, transmitirá
          inmediatamente, en caso contrario quedara a la espera y transmitirá cuando detecte que el medio queda
          liberado, requiere confirmación expresa (
          ACK) del receptor de que la trama le ha llegado correctamente.
        * Si se produce colisión, ambas esperan un breve tiempo aleatorio para volver a transmitir. Este mecanismo
          presenta problemas cuando se presenta la situación conocida como el “nodo oculto”: no todas las estaciones se
          encuentran dentro del alcance del resto, las transmisiones pueden no ser detectadas por el resto de los
          equipos conectados a dicha red, para evitar dicho problema, CSMA implementa el mecanismo de detección de canal
          virtual conocido como RTS/CTS.
      ***
        * ``Detección de canal virtual``: cuando una estación quiere transmitir a otra, A envía previamente una trama
          RTS con información sobre la identidad del emisor y la longitud de datos que pretende enviar, B, si está
          preparada para recibir dichos datos, responde con una trama CTS en la que especifica el emisor al que se le
          concede el canal y la longitud de datos que espera recibir. Esto se conoce como Network Allocation Vector (
          NAV).
        * La estación A comienza entonces la transmisión y queda a la espera del ACK de B confirmación la recepción de
          los datos transmitidos.
        * El mayor inconveniente del esquema CTS/RTS es la cantidad de información de control que se tiene que
          intercambiar.
        * DFC otorga un control distribuido de la red a todos los nodos que la componen, el estándar 802.11 permite
          también efectuar control centralizado a través del protocolo PCF (Point Coordinator Function) en el modo PCF,
          una estación base consulta a las demás si tienen tramas que emitir mediante un sistema de sondeo o polling.
        * El mecanismo para establecer el sondeo se basa en la transmisión de una trama baliza (beacon frame) de manera
          periódica entre 10 y 100 veces por segundo, se indican las características del servicio de polling e invita a
          nuevas estaciones a conectarse al mismo, se le garantiza una fracción del ancho de banda total de la estación
          base.
        * DCF y PCF pueden convivir dentro de una misma red con lo que algunas estaciones recibirían calidad de servicio
          mientras que el resto competiría por le medio compartido.

#### 3.2. ARQUITECTURA DE RED

Se pueden establecer redes de área local inalámbricas de dos modos:  
``Red Ad-Hoc`` (Peer-to-peer): grupo de ordenadores que se comunican cada uno directamente con los otros a través de las
señales de radio sin usar un punto de acceso, pueden ser útiles para establecer una red inalámbrica cuyo objetivo no es
permanecer invariable en el tiempo, se crean y deshacen para cubrir necesidades puntuales de comunicación.  
``Red Modo Infraestructura``: las redes inalámbricas se configuran como una extensión de las redes LAN cableadas ya
existentes, la red inalámbrica se configura mediante la utilización de:

* ``Terminales de usuario`` (clientes): disponer de una tarjeta interfaz de red (NIC) y un transceptor radio.
* ``Punto de acceso`` (AP, Access Point): controlador central de la red inalámbrica. Coordina la transmisión y recepción
  de múltiples dispositivos inalámbricos dentro de una extensión especifica. La forma habitual pasa por conectar los
  puntos de acceso de la red inalámbrica a un switch ethernet y este a un encaminador router IP.
* ``Controlador de acceso`` (AC, Access Controller): se proporciona servicio mediante un AP, conectar los AP a un
  controlador de acceso, el AC es un dispositivo IP que se encarga de asignar direcciones IP a los terminales de la
  WLAN. Para aumentar la capacidad de la red inalámbrica, se puede disponer más de un AP iluminado la misma zona con
  distintos canales de frecuencia, todo esto provoca que para redes que trabajen en la bandera de 2,4 GHz solo puedan
  operar sin interferencias 3 AP concurrentes, mientras que en la banda de 5 GHz se puede disponer de 8 AP.

### 7\. COMUNICACIONES MÓVILES INALÁMBRICAS

* Cualquier enlace de radiocomunicación entre dos terminales, al menos uno está en movimiento o detenido, pero en
  localizaciones indeterminadas.
* El servicio de ``Telefonía Móvil Automática`` (TMA) permite a sus abonados móviles establecer comunicación de voz y
  datos con otros móviles o con abonados a las redes fijas, el móvil debe encontrarse dentro del área de cobertura
  radioeléctrica de la red, los sistemas TMA se denominan sistemas celulares, su cobertura radioeléctrica total la
  consiguen mediante células o celdas proporcionadas por estaciones base de radio.
* Se denomina célula a cada una de las unidades básicas de cobertura que contiene un equipo transceptor (
  transmisor-receptor) un conjunto de frecuencias limitado se lleva a cabo la reutilización de frecuencias mediante la
  división del terreno en celdas continuas.
* La reutilización de frecuencias no es posible en células contiguas, ya que se producirían interferencias, pero si
  entre otras alejadas entre sí. “Clúster” designa un conjunto de células adyacentes de manera que, entre todas, agrupan
  la práctica totalidad de las frecuencias disponibles por la red celular.
* La cobertura final del sistema se alcanza sumando tantos clústeres como sea necesario reutilizándose las mismas
  frecuencias en todos ellos.
    * ``Conmutación de llamadas en curso`` (Hand-over): procedimiento mediante el cual se consigue que una conexión se
      mantenga cuando el móvil cambia de celda dependiente de la misma central de conmutación.
    * ``Seguimiento automático de abonados`` (Roaming): permite el mantenimiento  
      automático de una comunicación, cuando el móvil pasa a una celda dependiente de otra central de conmutación. La
      cobertura total de una red está dividida en áreas geográficas, cada área tiene asociada una central de conmutación
      que le da servicio y esta a su vez una base de datos asociada que contiene información de los móviles registrados
      en dicha área mediante el “Roaming”, la red puede dar servicio a un abonado que se encuentre desplazado en un área
      distinta a la que se ha registrado.
    * ``Telefonía móvil analógica y digital``:
        * ``Sistemas analógicos``: el servicio de voz se presta utilizando técnicas de transmisión analógica de señales.
        * ``Sistemas digitales``: se realiza una digitalización previa de la voz que luego es transmitida utilizando
          diversos mecanismos de transmisión digital de la señal.

* Las distintas familias de sistemas TMA se agrupan bajo la denominación de ``generaciones``, cada una marcada por un
  salto fundamental:
    * ``1G`` (Telefonía móvil analógica): utilización de señales analógicas para la transmisión de voz, modulación en
      frecuencia (FM), era imposible la comunicación entre países. Estándares englobados en esta generación:
        * ``AMPS``: primer sistema celular, americano de la banda 800 MHz
        * ``NMT-450``: europeo, banda 450 MHz
        * ``NMT-900``: evolución del NMT-450 sobre la banda de 900 MHz
        * ``TACS``: versión europea del AMPS en la banda de 900 MHz
  ***
    * ``2G`` (Telefonía móvil digital): alternativa para incrementar la cantidad de usuario simultáneos en los sistemas,
      surgió ``TDMA`` (Time Division Multiple Access) y ``CDMA`` (Code Division Multiple Access) como tecnologías
      predominantes de esta segunda generación. En CDMA se usa un espectro de 1.25 MHz donde cada usuario tenía con un
      código para diferenciarse del resto de los usuarios, ofrecía capacidades de seguridad y privacidad al incorporar
      un sistema criptográfico de autenticación. Esta generación se caracteriza por ser digital, en lugar de analógica,
      esto facilito el despliegue de nuevo servicios como el identificador de llamada, envío de mensaje cortos (SMS),
      mensajes de voz y llamada a tres. Los estándares europeos son GSM y DCS-1800.
  ***
    * ``2.5G``: Telefonía móvil multimedia (Banda Estrecha): despliegue de la tercera generación que ofrecía servicios
      multimedia avanzados sobre las redes móvil, para tratar de minimizar el efecto de dicha interrupción e ir
      preparando a los usuarios para la utilización de este tiempo de servicios se definió esta generación, con la
      evolución de GPRS a EDGE.
  ***
    * ``3G``: Telefonía móvil multimedia (Banda Ancha): estándar internacional de la ITU (IMT-2000), en Europa es
      estándar es UMTS, proporciona servicios de voz y dato avanzados, así como acceso a los nuevos servicios.
  ***
    * ``3.5G`` (Enlace descendente de alta velocidad):
        * ``HSDPA`` eleva la capacidad del enlace descendente hasta los 14,4 Mbps. En esta generación nace ``LTE`` (Long
          Term Evolution), se define un nuevo interfaz aire basado en la aplicación de OFDM (Orthogonal Frequiency
          Division Multiplexing) y antenas ``MIMO`` (Multiple Input Multiple Output) para conseguir hasta 42 Mbps en el
          enlace descendente.
        * ``UTRAN LTE`` (Universal Terrestrial Radio Access Network – LTE): se pretende conseguir una cobertura a nivel
          mundial mediante la modificación de las redes 3G actuales para permitir picos de transmisión de hasta 100 Mbps
          de bajada y 50 Mbps de subida.
  ***  
    * ``4G`` (LTE de cuarta generación): capacidad para proporcionar velocidades de acceso mayores de 100 Mbps en
      movimiento y 1Gbps en reposo, manteniendo QoS y alta seguirá. Es una fusión de tecnologías y protocolos, no un
      solo único estándar, WiMax y LTE pueden ser consideradas 4G, pero LTE Advanced y WiMax2 son auténticamente 4G. Uso
      de ``SDR`` (Software Defined Radios) para optimizar el acceso radio. Red completa prevista es todo IP. Tasas de
      pico máximas previstas son de 100 Mbps en enlace descendente y 50 Mbps en enlace ascendente.
  ***

### 3.3. GRUPOS DE TRABAJO IEEE 802:

* Su misión se centra en desarrollar estándares de redes de área local (LAN) y redes de área metropolitana (MAN),
  principalmente en las dos capas inferiores del modelo OSI.

| 802.1  Normalización de la interfaz. |
| :---- |
| ``802.1d``
STP`` (Spanning Tree Protocol): protocolo de red de capa 2 del modelo OSI (capa de enlace de datos). Su función es la de gestionar la presencia de bucles en topologías de red debido a la existencia de enlaces redundantes (necesarios en muchos casos para garantizar la disponibilidad de las conexiones). El protocolo permite a los dispositivos de interconexión activar o desactivar automáticamente los enlaces de conexión, de forma que se garantice la eliminación de bucles. STP es transparente a las estaciones de usuario.|
| ``802.1q``
VLAN`` (Virtual Local Area Networks): mecanismo que permita a múltiples redes compartir de forma transparente el mismo medio físico, sin problemas de interferencia entre ellas (Trunking). Varias VLAN pueden coexistir en un único conmutador físico o en una única red física. Son útiles para reducir el dominio de difusión y ayudan en la administración de la red, separando segmentos lógicos de una red de área local. Una VLAN consiste en dos o más redes de computadoras que se comportan como si estuviesen conectados al mismo computador, aunque se encuentren físicamente conectados a diferentes segmentos de una red de área local (Local). |
| ``802.1x Autenticación en redes``
LAN``: norma para el control de acceso a red basada en puertos. Permite la autenticación de dispositivos conectados a un puerto LAN, estableciendo una conexión punto a punto o previniendo el acceso por ese puerto si la autenticación falla. |
| ``802.1aq``
SPB`` (Shortest Path Bridging): tecnología de red que posibilita el Multipath routing, surgió como reemplazo de los antiguos protocolos spanning tree, que sirvieron para evitar caminos redundantes que pudiesen tener swtiching loop y evitar así tormentas de tramas. Mientras que SPB permite tener activas todas las rutas con caminos de igual coste, lo que conlleva una mayor escalabilidad a nivel 2 aportando una mayor velocidad de convergencia y mejorando la eficiencia gracias a un incremento del ancho de banda y permitiendo al tráfico un reparto de carga a través de todos los caminos de una topología en malla. Está diseñado para eliminar el error humano durante la configuración, preservando así la naturaleza plug-and-play que estableció Ethernet como protocolo por defecto de nivel 2\. |
| ``802.2``
LLC`` (Control de enlace lógico): se ocupa de la comunicación entre las capas superiores y las capas inferiores. Generalmente, esta comunicación se produce entre el software de red y el hardware del dispositivo. La subcapa LLC toma los datos del protocolo de la red, que generalmente son un paquete IPv4, y agrega información de control para ayudar a entregar el paquete al nodo de destino. En un PC, el LLC se puede considerar el controlador de la NIC. El controlador de la NIC es un programa que interactúa directamente con el hardware de la NIC para transmitir los datos entre la subcapa MAC y los medios físicos. |
| ``802.3 CSMA / CD``
(Carrier Sense Medium Access/Collision Detection): el que el emisor, durante el tiempo de transmisión de una trama, está escuchando el medio para comprobar si se ha producido una colisión con otro emisor que hubiese comenzado a transmitir al mismo tiempo, de detectarse esta circunstancia, el emisor detiene la transmisión en curso y espera un tiempo aleatorio para volver a retransmitir la trama dañada. Este mecanismo tiene unas buenas prestaciones en medios guiados como el par trenzado, sin embargo, para medios no guiados como el aire, no es posible aplicar el mecanismo de detección de colisiones al no poder el terminal realizar escuchas simultaneas durante la transmisión. |
| ``802.4 Token``
Bus``: protocolo de la subcapa MAC de Enlace de Datos que implementa una red lógica en anillo con paso de testigo sobre una red física de cable coaxial. |
| ``802.5 Token``
Ring``: arquitectura de red con topología lógica en anillo y técnica de acceso de paso de testigo, usando una trama de 3 bytes llamado testigo (en inglés token), que viaja alrededor del anillo. |
| ``802.11-B``
Utilizan DSSS para alcanzar velocidades máximas de 11 Mbps compartidos por todos los usuarios del canal por la utilización del mecanismo RTC/CTS el alcance de estas redes se encuentra en torno a los 100 metros. |
| ``802.11-A``
(no llego a implantarse en España) velocidad máxima de 54 Mbps por canal usa OFDM, frecuencias más altas en la banda de 5 GHz, con espacio para más canales y menos propensa a interferencias que la banda de 2,4 GHz pero reduce el alcance comparándolo con IEEE 802.11b. |
| ``802.11-G``
Misma velocidad máxima que IEEE 802.11a usando la banda de 2,4 GHz con dos opciones: OFDM o DSSS mejorado para garantizar la interoperabilidad con equipos IEEE 802.11b. El alcance es mayor debido a combinar las ventajas de OFDM en cuanto a multitrayecto con la menor absorción de la banda de 2.4 GHz. (IEEE 802.11a, b y g tienen como principal inconveniente la débil seguridad y carencia de calidad de servicio). |
| ``802.11-N``
Ha definido una especificación WLAN que, sobre las bandas de los 2,4 GHz y 5 GHz, ofrece una velocidad m |
| ``802.11-AC(wifi5)``
Permite alcanzar tasas de 1,3 Gbps y opera en la banda de 5 GHz, dispone de hasta 8 canales con un ancho de banda de 80-160 MHz cada uno. Incorpora cifrado de información con AES (Advanced Encryption Standard) conocido como WPA2. |
| ``802.11-AX(wifi6)``
Diseñado para operar en los espectros ya existentes de 2.4 GHz y 5 GHz. Introduce OFDMA para mejorar la eficiencia espectral global, con velocidad máxima de 11 Gbps. |
| ``802.15 WPAN``
(Bluetooth): redes inalámbricas de área personal, define la capa física (PHY) y de control de acceso al medio (MAC) para la conectividad inalámbrica tanto de dispositivos estacionarios como móviles dentro de un área personal. |
| ``802.16 WIMAX``
(Worldwide Interoperability for Microwave Access): tecnología dentro de las conocidas como tecnologías de última milla, también conocidas como bucle local que permite la recepción de datos por microondas y retransmisión por ondas de radio. Una de sus ventajas es dar servicios de banda ancha en zonas donde el despliegue de cable o fibra por la baja densidad de población presenta unos costos por usuario muy elevados (zonas rurales). |

## TEMA 6 – SEGURIDAD INFORMATICA: VIRUS, FIREWALL, VPN

### 1\. DEFINICIÓNES DE SEGURIDAD INFORMÁTICA

* Protección física del ordenador como componentes hardware, de su entorno, hasta la protección de la información que
  contiene o de las redes que lo comunican con el exterior, es un conjunto de reglas, planes y acciones que permiten
  asegurar la información contenida en un sistema computacional, un conjunto de soluciones técnicas a problemas no
  técnicos. Debe cubrir las características de confidencialidad, integridad y disponibilidad.
    * ``Confidencialidad``: asegura que la información no pueda estar disponible o ser descubierta por o para personas,
      entidades o procesos no autorizados, se refiere a la capacidad del sistema para evitar que personas no autorizadas
      puedan acceder a la información almacenada en él.
    * ``Integridad``: el servicio de seguridad que garantiza que la información es modificada, incluyendo su creación y
      borrado solo por el personal autorizado, el concepto de integridad significa que el sistema no debe modificar o
      corromper la información o permitir que alguien no autorizado lo haga, permite asegurar que no se ha falseado la
      información.
    * ``Disponibilidad``: el grado en que un dato está en el lugar, momento y forma en que es requerido por el usuario
      autorizado, el sistema, tanto hardware como software se mantiene funcionando eficientemente y es capaz de
      recuperarse en caso de fallo.
    * ``Autenticidad``: permite asegurar el origen de la información, la identidad del emisor puede ser validada, se
      evita que un usuario se haga pasar por otro.
    * ``No-Repudio``: permite asegura que cualquier entidad que envía o recibe información, no puede alegar ante
      terceros que no la envió o la recibió.
    * ``Consistencia``: asegurar que el sistema se comporta como se supone que debe hacerlo.
    * ``Prevención``: conocer los registros de actividad de los usuarios.
    * ``Vulnerabilidad``: potencialidad o posibilidad de ocurrencia de la materialización de una amenaza sobre el
      activo, o defecto o debilidad en el diseño, implementación, operación y mantenimiento de un sistema que podía ser
      explotado para violar la directiva o política de seguridad de dicho sistema.
    * ``Amenaza``: eventos que pueden desencadenar un incidente en la organización, produciendo daños materiales o
      perdidas inmateriales en sus activos, o una posibilidad de violación de la seguridad, que existe cuando se da una
      circunstancia, capacidad, acción o evento que pudiera romper la seguridad y causar prejuicio, es decir, una
      amenaza es un peligro posible que podría explotar una vulnerabilidad.
    * ``Impacto``: consecuencia sobre el activo de la materialización de una amenaza.
    * ``Riesgo``: posibilidad de que se produzca un impacto determinado en un activo, en un domino o en la organización,
      o probabilidad de que ocurra una amenaza, ponderándola con la magnitud del daño que pueda ocasionar, actos
      naturales, errores u omisiones humanas o actos intencionados.
    * ``Activos``: recursos del sistema de información o relacionados con este, necesarios para que la organización
      funcione correctamente.
    * ``Política de seguridad``: conjunto de reglas que dirige como un sistema proporciona servicios de seguridad para
      proteger recursos del sistema sensible y críticos.
    * ``Vulnerabilidades que afectan a todos los sistemas``: instalaciones por defecto de sistemas y aplicaciones,
      cuentas sin contraseña o débiles, BackUps incompletos o inexistentes, gran número de puertos abiertos,
      insuficiente filtrado de los paquetes con direcciones de inicio y destino inadecuadas, registro de eventos (
      logging) incompleto o inexistente, programas CGI (Common Gateway Interface) vulnerables,...
    * ``Vulnerabilidades que afectan a sistemas Windows``: vulnerabilidad Unicode, desbordamiento de buffer en
      extensiones ISAPI (Internet Server Application Programming Interface), exploit para RDS del IIS (Servicios de
      información remota Microsoft), recursos compartidos en red no protegidos, fuga de información a través de
      conexiones de tipo “null sesión”, hashing débil en SAM (Security Account Manager).
    * ``Vulnerabilidades que afectan a sistemas UNIX``: desbordamiento de Buffer en los servicios RPC (Remote Procedure
      Call, vulnerabilidades en sendmail, debilidades en BIND (Berkeley Internet Name Domain), comandos “r.”,
      desbordamiento de buffer en LPD (Line Printer Daemon), “sadmind” y “mountd”, bajo control de cifrado en SNMP,...
    * ``Vulnerabilidades que afectan a servidores web``: parámetros no validos en peticiones HTTP, control de acceso
      violado, ruptura en el manejo de control de cuentas y sesiones, desbordamiento de buffer, errores por inyección de
      código y comandos, problemas con el manejo de errores, uso inseguro de la criptografía, errores de
      implementaciones de administración remota, fallos en sistemas con scripts, falta de configuración correcta en los
      servidores,...

### 2\. ATAQUES Y AMENAZAS

* Tipos de ataques y amenazas: todas aquellas acciones que supongan una violación de la seguridad de nuestro sistema (
  autentificación, confidencialidad, integridad o disponibilidad), se pueden clasificar en:
    * ``Interrupción``: un recurso del sistema es destruido o se vuelve no disponible, es un ataque contra la
      disponibilidad (
      Nukes: causan que los equipos queden fuera de servicio).
    * ``Intercepción``: una entidad no autorizada consigue acceso a un recurso, ataque contra la confidencialidad (
      Troyanos:
      copia ilícita de archivos o programas o bien la lectura de las cabeceras de paquetes de datos para desvelar la
      identidad, Spoofing...)
    * ``Modificación``: una entidad no autorizada no solo consigue acceder a un recurso, sino que es capaz de
      manipularlo. Virus y troyanos poseen esa capacidad, es un ataca contra la integridad. Modificación de cualquier
      tipo en archivos de datos, alterar un programa, modificar el contenido de información que este siendo trasferida
      por la red...
    * ``Fabricación``: una entidad no autorizada inserta objetos falsificados en el sistema, es un ataque contra la
      autenticidad (Inserción de mensajes falsos en una red o añadir datos a un archivo), pueden clasificarse en:
        * ``Ataques activos``: algún tipo de modificación de los datos o la creación de falsos datos (suplantación de
          identidad, modificación de mensajes, web spoofing...)
        * ``Ataques pasivos``: el atacante no altera la comunicación si no que únicamente la escucha o monitoriza para
          obtener la información que está siendo transmitida, son muy difíciles de detectar ya que no provocan ninguna
          alteración de los datos, es posible evitar su éxito mediante el cifrado de la información.

#### 2.1. CLASIFICACIÓN DE LOS ATAQUES POR SU “MODUS OPERANDI”

* ``Escaneo de puertos``: buscar puertos abiertos y fijarse en los que puedan ser receptivos o de utilidad para el
  ataque.
* ``Ataques de autenticación``: suplantación de una persona con autorización por parte del atacante mediante la
  obtención del nombre y contraseña del atacado o suplantando a la víctima una vez está ya ha iniciado una sesión en su
  sistema. Se utilizan varias técnicas:
    * ``Simulación de identidad``: el atacante instala un programa que recrea la pantalla de entrada al sistema para
      capturar su login y clave.
    * ``Spoofing``: ataques (sobre protocolos) que consisten en sustituir la fuente de origen de una serie de datos
      adoptando una identidad falsa para engaña a un firewall o filtro de red, los más conocidos son:
        * ``IP Spoofing``: sustituye una IP, el atacante logra identificarse con una IP que no es la suya, con lo que a
          ojos del atacado el agresor es una tercera persona en vez del atacante real (a través de nmap, por ejemplo).
        * ``DNS Spoofing``: aprovecha de la capacidad de un servidor DNS de resolver una petición de dirección IP a
          partir de un nombre que no figura en su base de datos (sustituye un servidor DNS).
        * ``Web Spoofing``: el atacante crea un sitio web (falso) similar al que la víctima desea entrar, los accesos a
          este sitio están dirigidos por el atacante permitiéndole monitorizar todas las acciones de la víctima.
    * ``Fake-mail``: envío de emails con remitente falso, el atacante envía email en nombre de otra persona.
    * ``Eavesdropping``: ataque de capa de red, captura pequeños paquetes de la red y lee el contenido de datos.
    * ``Looping``: el intruso utiliza algún sistema para obtener información e ingresar en otro, que luego utiliza para
      entrar en otro y así sucesivamente, tiene como finalidad hacer imposible localizar la identificación y la
      ubicación del atacante.
    * ``IP Splicing-Hijacking``: el atacante espera a que la víctima entre en una red usando su nombre, contraseña y
      demás y una vez que la víctima ha superado los controles de identificación y ha sido autorizada, la expulsa del
      sistema y se hace pasar por ella.
    * ``Sinkholing``: técnica para manipular el flujo de datos en una red; redirige el tráfico desde su destino previsto
      al servidor de su elección. Se puede utilizar de forma maliciosa para desviar el tráfico legítimo de su
      destinatario previsto.
    * ``Backdoors`` (puertas traseras): trozos de código en un programa que permite a quien los conocen saltarse los
      métodos usuales de autentificación para realizar ciertas tareas, son insertados por los programadores para
      agilizar la tarea de probar código durante la fase de desarrollo, son fallos de seguridad que se mantienen
      voluntariamente o no una vez terminado el producto.
    * ``Exploit``: ingresar a un sistema aprovechándose de agujeros en los algoritmos de encriptación utilizados.
    * ``Obtención de contraseñas``: obtención por “fuerza bruta” de nombres de usuarios y claves de acceso. Suele
      realizar este tipo de ataques usando una clase de programas llamados diccionarios (programas que en su base de
      datos contienen millones de palabras, van probando con millones de combinaciones de letras y números encriptados,
      hasta descubrir la combinación correcta).
    * ``Man in the middle``: el atacante se ubica en el medio de una comunicación entre dos entidades legítimas para
      leer o modificar los datos que pasan entre las dos partes. Se basa en capturar todo el tráfico de red de un
      usuario objetivo.

* ``Denial of Service`` (DoS): ataque de negación de servicio, produce la imposibilidad por parte de la víctima de
  acceder y/o permitir el acceso a un recurso determinado, la imposibilidad de un servidor de prestar sus servicios. Es
  más fácil corromper un sistema que acceder clandestinamente al mismo, estos ataques intentan corromper o saturar los
  recursos de la víctima por medio de peticiones de conexión para lograr desactivarla por medio de saturación, ataques
  más usuales:
    * ``Jamming o Flooding``: ataques que saturan los recursos del sistema de la víctima dejándola sin memoria, sin
      espacio libre en su disco duro o saturando sus recursos en red.
    * ``Syn Flood``: inundación con paquetes SYN, cuando se establece una comunicación a través de TCP, el servidor
      envía un paquete que si el cliente no contesta entra en un estado denominado semiabierto, no se ha atendido el
      saludo inicial. El servidor permanecerá a la escucha un determinado tiempo hasta cancelar la llamada, si se envían
      muchos saludos incompletos se consigue que el servidor se paralice.
    * ``Land Attack``: consiste en un bug en la implementación de la pila TCP/IP en Windows, el ataque envía a algún
      puerto abierto de un servidor un paquete, maliciosamente construido con la IP y puerto origen igual que la IP y
      puerto destino termine por colapsarse.
    * ``Supernuke o Winnuke``: “Nuke” es el ataque más común de los equipos Windows, hace que los equipos que escuchan
      por el puerto UDP 137/138/139 (utilizando NetBios), queden fuera de servicio o disminuyan su rendimiento al
      enviarle paquetes UDP manipulados, se envían fragmentos de paquetes que la maquina victima detecta como erróneos
      pasando a un estado inestable.
    * ``Teardrop``: afectan a fragmentos de paquetes, algunas implementaciones de colas IP no vuelve a recomponer
      correctamente los fragmentos ya que se superponen haciendo que el sistema se cuelgue.
    * ``Mail bombing / Mail Spamming``: envío indiscriminado y masivo de un mensaje idéntico a una misma dirección,
      saturando así buzón el de correo del destinatario.

* ``Ataques de modificación / daño``:
    * ``Tampering o Data Diddling``: modificación no autorizada de datos o software instalado en el sistema víctima.
    * ``Ataques usando Java Applets``: son ejecutados desde otra aplicación, como un navegador de internet, los
      navegadores actuales implementan JVM para poder ejecutarlos, no son más que código ejecutable y como tal puede ser
      manipulado por intrusos.
    * ``Ataques usando JavaScript y VBScript``: son dos lenguajes usados por los diseñadores de sitios web evitando el
      uso de java, los programas son interpretados por el navegador.
    * ``Ataques usando ACTIVEX``: tecnología de Microsoft cuya seguridad se basa en certificados y firmas digitales, el
      problema es que los usuarios aceptan los certificados sin pararse a leerlos, y estos se basan en que el
      programador del control ActiveX asegura que su control no es nocivo, lo cual es falso en bastantes ocasiones.
    * ``Cookies``: solo representan una amenaza para la privacidad, ya que pueden cumplir la función de espiar. No son
      capaces de causar daño al sistema, se utilizan para reconocer al usuario al entrar en determinados sitios web.
    * ``Ataques usando vulnerabilidades de los navegadores``: fallos del navegador, los más comunes son los “buffer
      overflow” debido a una debilidad de los buffers de algunos navegadores para el procesamiento de las entradas de
      usuario, se puede llegar a manipular datos como URL almacenadas.

* ``Explotación de errores``:
    * ``Errores de diseño, implementación y operación``: sistemas están expuestos a agujeros de seguridad que son
      explotados para acceder a archivos, obtener privilegios o realizar sabotaje. Ocurren por varias razones como
      puertas traseras, bugs...

### 3 CONCEPTOS BÁSICOS SOBRE VIRUS

* Es un programa que tiene la capacidad de causar daño y puede replicarse a sí mismo y propagarse a otras computadoras.
  Infecta “entidades ejecutables”, archivos o sectores de las unidades de almacenamiento, se programa en lenguaje de
  bajo nivel, requiere conocimientos del funcionamiento interno del pc, tienen tres características principales:
    * ``Dañino``: siempre causa daños en el sistema que infecta, se busca destruir o alterar la información o pueden ser
      situaciones con efectos negativos para la computadora, consumo de memoria principal, tiempo de procesador,
      disminución de rendimiento...
    * ``Autorreproductor``: crear copias de sí mismo, cosa que ningún otro programa convencional.
    * ``Subrepticio``: utilizara técnicas para evitar que el usuario se dé cuenta de su presencia (se oculta). Tener un
      tamaño reducido para poder disimularse a primera vista, la peligrosidad de un virus está dada por lo critico del
      sistema que este infectando, no pueden causar daño directo sobre el hardware, pero si pueden hacer ejecutar
      operaciones que reduzcan la vida útil de estos. Por lo general prefieren atacar los archivos y no meterse con la
      parte física.

* Este tipo de programas se pega a alguna entidad ejecutable que le facilitara la subida a memoria principal y la
  posterior ejecución, como entidades ejecutables reconocen los sectores de arranque de los discos de almacenamiento (
  MBR), los archivos ejecutables (.exe), librerías, módulos de programas (.dll, .lib,...). El virus puede tener control
  total de la máquina al igual que el SO si logra cargarse antes que nadie, es decir, si cada vez que se inicie el
  sistema el virus lograr cargarse antes que el SO y luego, respetando su dese por permanecer oculto hacer ejecutar las
  intrusiones del MBR. Un virus puede contener tres módulos principales:
    * ``Módulo de reproducción``: encargado de manejar las rutinas para infectar entidades ejecutables que aseguraran la
      subsistencia del virus. Cuando toma el control del sistema puede infectar otras entidades ejecutables.
    * ``Módulo de ataque``: contiene las rutinas de daño adicional o implícito. Puede ser disparado por distintos
      eventos del sistema: fecha, hora, encontrar un archivo o sector especifico, una determinada cantidad de arranques
      desde que ingreso al sistema...
    * ``Módulo de defensa``: principal objetivo es proteger el cuerpo del virus, incluye rutinas que disminuyen los
      síntomas que delatan su presencia para que permanezca invisible, muy sofisticadas logrando dar información falsa
      al SO y localizándose en lugares poco comunes para el registro de los antivirus, como la memoria flash/ROM.

* ``Métodos de infección``:
    * ``Añadidura o empalme``: el código del virus se agrega al final del archivo ejecutable a infectar, modificando las
      estructuras de arranque del archivo anfitrión. La principal desventaja es el tamaño del archivo infectado es mayor
      al original, lo que permite una fácil detección.
    * ``Inserción``: se aloja en zonas de código no utilizadas o en segmentos de datos dentro de los archivos que
      contagian, la longitud total del archivo infectado no varía.
    * ``Reorientación``: se introducen centrales virósicas en zonas físicas del disco rígido marcadas como defectuosas o
      en archivos ocultos del sistema. El cuerpo del virus, al no estar insertado en el archivo infectado, sino en otro
      sitio oculto, puede tener un tamaño bastante grande, aumentando así su funcionalidad.
    * ``Polimorfismo``: método más avanzado de contagio logrado por los programadores, la técnica básica usada es la de
      inserción de código viral en un archivo ejecutable, pero para evitar el aumento de tamaño del arco infectado, el
      virus compacta parte de su código y del código del archivo anfitrión de manera que la suma de ambos sea igual al
      tamaño original del archivo.
    * ``Sustitución``: sustituye el código completo del archivo original por el código del virus, al ejecutar el
      programa infectado el único que actúa es el virus, que cumple con sus tareas de contagiar otros archivos y luego
      termina la ejecución del programa reportando algún tipo de error.
    * ``Tunneling``: los virus utilizan el tunneling para protegerse de los módulos residentes de los antivirus que
      monitorean todo lo que sucede en la máquina para interceptar todas las actividades “típicas” de los virus.

* ``Clasificación de los virus``:
    * ``Según su comportamiento``:
        * ``Caballos de Troya``: no tienen la capacidad de autorreproducirse. Se esconden dentro del código de archivos
          ejecutables y no ejecutables. Su objetivo es robar las contraseñas que el usuario tenga en sus archivos o las
          contraseñas para el acceso a redes y enviarlas por correo a la dirección registrada como la de la persona que
          lo envió a realizar la tarea.
        * ``Troyanos``: programas Remote adminstration Tool, deben estar instalados en ambos pc y su comunicación se
          produce vía internet o vía red. Tiene un carácter malicioso como el aprovechamiento de bugs y backdoors, el
          desconocimiento de la victima de que el troyano esta instalado en su PC, se oculta intentando pasar
          desapercibido,...
            * ``Camaleones``: variedad de los troyanos, actúan como otros programas comerciales, en los que el usuario
              confía pero en realidad están haciendo algún tipo de daño.
        * ``Virus polimorfos o mutantes``: poseen la capacidad de cifrar el cuerpo del virus para que no pueda ser
          detectado fácilmente, deja disponibles unas cuantas rutinas que se encargaran de descifrar el virus para poder
          propagarse, una vez descifrado el virus intentara alojarse en algún archivo de la computadora. Para esto
          incluye un generador de códigos al que se conoce como motor de mutación.
        * ``Virus sigilosos``: posee un módulo de defensa bastante sofisticado, intentara permanecer oculto tapando
          todas las modificaciones que haga. Subvirtiendo algunas líneas de código el virus logra apuntar el flujo de
          ejecución hacia donde se encuentra la zona infectada. La técnica stealth de ocultamiento de tamaño captura las
          interrupciones del SO que solicitan ver los atributos del archivo y, el virus le devuelve la información que
          poseía el archivo antes de ser infectado.
        * ``Virus lentos``: infectan solamente los archivos que el usuario hace ejecutar por el SO, simplemente siguen
          la corriente y aprovechan cada una de las cosas que se ejecutan.
        * ``Retro-virus``: intenta como método de defensa atacar directamente al programa antivirus, lo programadores de
          virus esta no es una información difícil de obtener ya que pueden conseguir cualquier copia de antivirus que
          hay en el mercado, descubrir cuales son los puntos débiles del programa y buscar una buena forma de
          aprovecharse de ellos. Virus voraces: alteran el contenido de los archivos de forma indiscriminada, sustituirá
          el programa ejecutable por su propio código, se dedican a destruir completamente los datos que puedan
          encontrar.
        * ``Bombas de tiempo``: virus convencionales con la diferencia de que el trigger de su módulo de ataque se
          disparara en una fecha determinada, muestran mensajes en la pantalla en alguna fecha.
        * ``Macro-virus``: son completamente independientes del SO o de la plataforma, ni siquiera son programas
          ejecutables, son pequeños programas escritos en el lenguaje propio de un programa (editores de texto, hojas de
          cálculo, utilidades especializadas...), se pueden propagar a otros ordenadores siempre que los usuarios
          intercambien documentos del tipo del virus. Alteran de tal forma la información de los documentos infectados
          que su recuperación resulta imposible, solo se ejecutan en aquellas plataformas que tengan la aplicación para
          la que fueron creados.
        * ``Gusanos``: un conjunto de programas, que tiene la capacidad de desparramar un segmento de él o su propio
          cuerpo a otras computadoras conectadas a una red, hay dos tipos de gusanos:
        * ``Host Computer Worm``: contenidos totalmente en una computadora, se ejecutan y se copian a si mismo vía
          conexión de una red, originalmente terminan cuando hicieron una copia de ellos mismo en otro host, también
          existen los que hacen la copia e infectan otras redes, es decir que cada máquina guarda una copia de ese
          gusano.
            * ``Network Worm``: conjunto de partes (segmentos), cada una corre en una máquina distinta y usando la red
              para distintos propósitos de comunicación propagan un segmento de una maquina a otra, tienen un segmento
              principal que coordina el trabajo de los otros segmentos.

### 4\. SEGURIDAD PERIMETRAL Y PROTECCIÓN EN REDES DE COMUNICACIONES  
* Cuando surgieron los primeros virus y comenzaron a producirse los primeros ataques de DoS (Denial of Service). Para
satisfacer las necesidades de comunicación segura de los usuarios, fue necesario desarrollar estándares, protocolos y
técnicas para implementar mecanismos de seguridad en las redes.

#### 4.1. TIPOS DE MEDIDAS DE SEGURIDAD

* Diseñar sistemas mediante criterios de seguridad es más complejo, pues las amenazas con poco cuantificables y muy
  variadas, las medidas de seguridad llevan un costo aparejado, a mayores y más restrictivas medidas de seguridad, menos
  amigable es el sistema, las medidas de seguridad que pueden establecerse en un sistema informático son:
    * ``Medidas físicas``: mecanismos para impedir el acceso directo o físico no autorizado, también protege de
      desastres naturales y se encarga de establecer un perímetro de seguridad.
    * ``Medidas lógicas``: incluye las medidas de acceso a los recursos, el uso correcto de los mismos, distribución de
      las responsabilidades entre los usuarios, protección de la información almacenada.
    * ``Medidas humanas``: definir las funciones, relaciones y responsabilidades de distintos usuarios potenciales del
      sistema.
    * ``Medidas administrativas``: aquellas que deben ser tomadas por las personas encargadas de definir la política de
      seguridad como la documentación y publicación de la política de seguridad y el establecimiento de un plan de
      formación del personal
    * ``Medidas legales``: aplicación de medidas legales para disuadir al posible atacante o para aplicarle algún tipo
      de castigo a posteriori. Normalmente son fijadas por instituciones gubernamentales e incluso instituciones
      internacionales como LOPD (Ley Orgánica de Protección de Datos)

### 5\. IDENTIFICACIÓN Y AUTENTIFICACIÓN

* Las herramientas y aplicaciones forman la base técnica de la política de seguridad, pero la política de uso aceptable
  debe considerar otros aspectos (quien tiene permisos, acceso, responsabilidades...).
* Para poder entrar en un recinto será necesario saber de quien se trata y si el sujeto está autorizado, será preciso
  identificar al sujeto (
  identificación) de forma totalmente fiable (autenticación o verificación) y consultar un archivo, base de datos y/o
  algoritmo que nos diga si el sujeto tiene o no autorización para realizar la acción demandada (autorización).
* Esto implica que antes se haya establecido un sistema para identificar a los sujetos (gestión de la identificación),
  se haya definido un sistema para autentificar al usuario (Autentificador), y que para cada usuario se haya definido
  una tabla de permisos.
* Cuando el usuario intente entrar en el sistema, deberá dar su identificación, que el sistema verificará (
  Comprobación del identificador), realizar la operación pertinente para demostrar que es quien dice ser (contraseña) y
  el sistema lo comprobará (Autentificación).

### 5.1. CONTROL DE ACCESO

* Seleccionar o filtrar los usuarios que pueden acceder a recursos informáticos, en redes telemáticas se puede hacer la
  selección del acceso según:
* ``En el servidor``: el ordenador que almacena la información instala los filtros en el SO, esto permite realizar la
  selección también para los usuarios que acceden físicamente al ordenador, el problema es gestionar el acceso de una
  lista en muchos servidores, para solucionar esto hay sistema que centralizan la gestión como Kerberos (protocolo de
  autenticación de redes de ordenador creado por el MIT que permite a dos ordenadores en una red insegura demostrar su
  identidad mutuamente de manera segura. Se basa en criptografía de clave simétrica y requiere un tercero de confianza)
  o Radius (Remote Authentication Dial-In User Service): protocolo de autenticación y autorización para aplicaciones de
  acceso a la red o movilidad IP. Utiliza el puerto 1812 UDP para establecer sus conexiones.).
* ``En la red``: se instalan filtros en la red que controlan los accesos desde maquinas remotas, estos se pueden
  implementar en Switchs LAN, Routers o Firewalls. Permite controlar zonas y grupos. Podemos definir seguridad
  perimetral como el conjunto de técnicas, elementos y sistema tanto hardware como software que permiten la protección
  del perímetro delimitante entre las redes LAN de una organización y el conjunto de las redes externas a dicha
  organización. Los ataques a través de las redes de comunicaciones potencialmente pueden ocasionar perdidas de
  información. El empleo de sistemas de protección perimetral que permitan realizar un robusto control de accesos y
  protección los servicios informáticos garantizan un correcto aprovechamiento de la infraestructura y garantiza la
  integridad y confidencialidad de la información. Los diferentes segmentos de red se organizan en base a zonas de
  seguridad:
    * ``Zona interna``: se sitúan los usuarios de la propia organización.
    * ``Zona externa``: se encuentran los dispositivos cuya gestión esta fuera del alcance de la organización.
    * ``DMZ`` (De-Militarized Zone): se suelen situar a los servidores corporativos que proporcionan servicios a los
      puestos de la red interna y a clientes situados en la red externa, quedando protegidos por las diferentes reglas
      de seguridad configuradas en el firewall. La DMZ está separada de la red interna y la red externa a través de un
      dispositivo de control y filtrado del tráfico. El Firewall podría ser también un router que ejerciese, además de
      las funciones propias, funciones específicas de un firewall.

#### 5.2. FIREWALLS  

* Es un sistema o grupo de sistemas que hace cumplir una política de control de acceso entre varias redes, se puede
  definir como cualquier sistema (desde un simple router hasta varias redes en serie) utilizado para separar en cuanto a
  seguridad se refiere, una maquina o subred del resto, protegiendo así servicios y protocolos que desde el exterior
  puedan suponer una amenaza a la seguridad.
* Son dispositivos hardware o sistemas software que controlan el flujo de tráfico entre dos o más redes empleando
  ciertas políticas de seguridad, son dispositivos cuya funcionalidad se limita a permitir o bloquear el tráfico entre
  dos redes basándose en una serie de reglas.
* Su complejidad reside en las reglas que admiten y en como realizan la toma de decisiones basándose en dichas reglas.

***

* El nivel de protección depende de las necesidades de la organización, los firewalls se configuran para proteger la red
  contra cualquier intento de acceso desautorizado desde el exterior hacia el interior de la red o viceversa,
  adicionalmente, es un punto único e ineludible de acceso a la red donde se pueden centralizar las medidas de seguridad
  y auditoría sobre esta.
* Un firewall no puede proteger la red contra amenazas que no pasan a través de él.
* Los firewalls no pueden proteger contra clientes o servicios que se admiten como validos pero que son vulnerables.
* Tampoco pueden proteger contra mecanismos de “tunneling” criptográfico para HTTP, SMTP u otros protocolos (
  comunicaciones cifradas sobre SSL para los protocolos citados).
* Algunos proporcionan mecanismos de detección y eliminación básicos.
* Los cortafuegos no pueden ni deben sustituir otros mecanismos de seguridad que reconozcan la naturaleza y efectos de
  los datos y aplicaciones que se estén manejando y actúen en consecuencia.
* Se dividen en:
    * ``Firewall a nivel de red o de filtrado de paquetes`` (capas 2, 3 y/o 4 del modelo OSI):
        * Cuanto más bajas sean las capas en las que el firewall trabaja, su evaluación será más rápida y transparente
          pero su capacidad de acción ante ataques complejos es menor.
        * Los firewalls de filtrado de paquetes utilizan información de las cabeceras de capa 2, 3 y 4 para tomar
          decisiones de bloque o envió.
        * Existen dos clases principales dentro de esta categoría, los firewalls de filtrado de paquetes estático y
          filtrado de paquetes dinámico, la diferencia fundamental entre ellos es que los segundos tienen en cuenta
          información sobre el estado de la conexión a la hora de evaluar las reglas.
        * Los firewalls de filtrado estático de paquetes analizan cada paquete individualmente, los firewalls de
          filtrado dinámico analizan cada paquete en el contexto de su contexto.
        * Aparte de Aceptar o Rechazar, los firewalls de este tipo poseen un tercer tipo de acción:
            * ``Descartar``.
                * Cuando un paquete es procesado por una regla que define esta acción, este se elimina “silenciosamente”
                  sin devolverse error ninguno a lo originario de este creando un efecto de “agujero negro” y evitando
                  así que el firewall revele su presencia.
                * Las principales ventajas de este tipo de firewalls son su rapidez, transparencia y flexibilidad.
                * Proporcionan un alto rendimiento, escalabilidad y bajo coste y son muy útiles para bloquear la mayoría
                  de los ataques de DoS, se siguen implementando como servicios integrados en algunos routers y
                  dispositivo hardware de balanceo de carga.
                * Los firewalls con inspección de estado o filtrado dinámico de paquetes (Stateful Inspection Firewalls)
                  son firewalls de filtrado de paquetes en los que, además, se valida a la hora de aceptar o rechazar el
                  paquete, el hecho de que este sea una petición de nueva conexión o pertenencia a una sesión ya
                  establecen entre un host externo y otro interno.
                * Los firewalls de este tipo examinan de forma estricta el establecimiento de cada conexión (en capa 4
                  del modelo OSI), mantiene una tabla de conexiones válidas y deja pasar los paquetes que contienen
                  información correspondiente a una entrada válida en dicha tabla de circuitos virtuales.
                * También proporcionan los mecanismos efectivos de seguridad sobre el tráfico UDP, creando información
                  de sesión a partir d los puertos origen y destino utilizados.
    * ``Firewall a nivel de aplicación`` (capas 5, 6, y/o 7 del modelo OSI): mantienen información del contexto de cada
      conexión, teniendo en cuenta información de capa de aplicación antes de permitir una conexión, manteniendo un
      riguroso control del estado de todas las conexiones y el número de secuencia de los paquetes. Suelen ser servicios
      de filtrado para los protocolos de capa 7 más habituales (HTTP, FTP, DNS, HTTPS, SMTP) proporcionando un control
      de acceso adicional y un detallado registro de sucesos respecto a este.

***

* > ``Proxys``: aplicación o dispositivo hardware que hace de intermediario entre los usuarios, normalmente de una red local e internet.
* > Lo que hace realmente es recibir peticiones de usuario y redirigirlas a internet, la ventaja que presenta es que con una única conexión a internet podemos conectar varios usuarios.
* > Un proxy es a su vez un servidor de caché, almacena las páginas web a las que se accede más asiduamente en una memoria, un usuario quiere acceder a internet, accede a través del proxy.
* > Se aceleran en gran medida los accesos a internet. El proxy el transparente al usuario, porque tendrá que configurar su navegador diciéndole que accede a internet a través de este.
* > Los últimos proxies que han aparecido en el mercado realizan además funciones de filtrado, dejar que un usuario determinado acceda a unas determinadas páginas de internet o que no acceda a ninguna, podemos configurar una red local en la que haya usuario a los que se les permita salir a internet, otros a los que les permita enviar correo, pero no salir a Internet...

*** 

#### 2.3. ARQUITECTURAS DE SEGUIRDAD PERIMETRAL

* ``Dual-Homed Host``: basada en el uso de “proxy” (sin firewall), habitualmente en máquinas Linux/Unix con “Squid (
  servidor proxy para web con caché para entornos Linux)” equipadas con dos o más tarjetas de red y denominadas
  anfitriones de dos bases (Dual-Homed Host) o multibase (Multi-Homed Host). Una de las tarjetas se suele conectar a la
  red interna a proteger y la otra a la red externa a la organización. Esta configuración se basa en el uso de un host
  bastión.

* > ``Host bastión`` (gate): un sistema especialmente asegurado, expuesto a todo tipo de ataques por estar accesible desde Internet, función principal es ser el punto de contacto de los usuarios de la red interna o de algún servicio de la DMZ de una organización con otro tipo de redes.
* > El host bastión filtra tráfico de entrada y salida, y también oculta la configuración de la red hacia fuera.

* El sistema ha de ejecutar al menos un servidor “proxy” para cada uno de los servicios que se desee permitir y es
  necesario que le servicio “IP Forwarding” este deshabilitado, para que la maquina con varias tarjetas de red no pueda
  actuar como router, aislando el tráfico entre la red interna y la externa.
* Los sistemas externos verán al host a través de una de las tarjetas y lo internos a través de la otra.
* Entre las dos partes no puede existir ningún tipo de tráfico que no pase por el proxy: todo el intercambio de datos
  entre las redes se ha de realizar a través de servidores “proxy” situados en el host bastión.
* La utilización de proxies es muy recomendable, pero puede ser problemática al configurar cierto tipo de servicios o
  protocolos que no se diseñaron tenido en cuenta la existencia de un proxy entre los dos extremos de una conexión.

***

* ``Screened Host``: un paso en términos de seguridad perimetral es la arquitectura “screened host” o “choke gate”, que
  combina un router (configurado como firewall de filtrado de paquetes estático), con un host bastión.
* El principal nivel de seguridad proviene del filtrado de paquetes (el router es la primera y más importante línea de
  defensa).
* En la máquina bastión, único sistema accesible desde el exterior, se ejecutan los proxies de las aplicaciones,
  mientras que el choke o router de filtrado de paquetes, se encarga de filtrar los paquetes que se puedan considerar
  peligrosos para la seguridad de la red interna, permitiendo únicamente la comunicación con un reducido número de
  servicios.
* La recomendación es situar el router entre la red exterior y el host bastión, pero situar el bastión en la red
  exterior no provoca aparentemente degradación de la seguridad.
* La “no degradación” de la seguridad mediante esta aproximación es más que discutible, ya que habitualmente es más
  fácil de proteger un router que una maquina con un operativo de propósito general.
* Así cuando una máquina de la red interna desea comunicarse con el exterior existen dos posibilidades:
    * El “choke” permite la salida de algunos servicios a todas o parte de las maquinas internas a través de un simple
      filtrado de paquetes.
  * El “choke” prohíbe todo el tráfico entre máquinas de la red interna y el exterior, permitiendo solo la salida de
    ciertos servicios que provienen de la maquina bastión que han sido autorizados por la política de seguridad de la
    organización. Así, se obliga a los usuarios a que las conexiones con el exterior se realicen a través de los
    servidores proxy situados en el bastión.

***

* ``Screened subnet`` (DMZ): es con diferencia la más utilizada, añade un nivel de seguridad en las arquitecturas de
  firewall situando una subred (DMZ) entre las redes externa e interna, de forma que, si la seguridad del mismo se veía
  comprometida, la amenaza se extendía automáticamente al resto de la red.
* Como la maquina bastión es un objetivo interesante para muchos atacantes, la arquitectura DMZ intenta aislarla en una
  red perimétrica de forma que un intruso que accede a esta máquina no consiga un acceso total a la subred protegida.
* Es una arquitectura más segura, pero también más compleja.
* Se utilizan dos firewalls, denominados exterior e interior, conectados ambos a la DMZ, donde se puede ubicar el host
  bastión y también se podrían incluir sistemas que requieran un acceso controlado como el servidor de correo.
* El firewall exterior tiene como misión bloquear el tráfico no deseado en ambos sentidos, mientras que el interior hace
  lo mismo, pero con el tráfico entre la red interna y la perimétrica.
* De este modo un atacante había de romper la seguridad de ambos routers para acceder a la red protegida.
* Incluso es posible implementa una zona desmilitarizada con único router que posea tres o más interfaces de red, pero
  en este caso si se compromete este único elemento se rompe toda nuestra seguridad.

#### 2.4. SISTEMAS DETECTORES Y PREVENTORES DE INTRUSIONES (IDS)

* ``IDS`` (Intrusion Detection Systems) es un sistema de seguridad complementario al firewall y proxy.
* Los IDS no garantizan la seguridad, pero proporciona información adicional sobre los eventos que se están produciendo
  en un sistema o en un segmento de red.
* Una buena estrategia de seguridad debe incluir, además, autenticación de usuarios, control de acceso, cifrado de datos
  y análisis de vulnerabilidades.
* Los sistemas de detección de intrusos proporcionan monitorización (recibe y analiza el tráfico en busca de cualquier
  actividad que pueda ser potencialmente peligrosa o que no cumpla la política de seguridad de la organización),
  detección (usan políticas para definir los actos sospechosos de todo ese tráfico) y respuesta (pueden proporcionar un
  conjunto de respuestas limitados, finalización de sesiones TCP sospechosas o la interacción con firewalls mediante
  comandos SNMP).
* Los sistemas de detección son un elemento integral y necesario en una infraestructura de información seguirá,
  representando el complemento ideal a los firewalls en las redes.
* Permiten una completa supervisión de las redes, independientemente de la acción tomada, esa información siempre estará
  ahí y será necesaria para determinar la naturaleza del incidente y su fuente. Existen dos grandes enfoques a la hora
  de clasificar a los sistemas de detección de intrusos en función de que sistemas vigilan:
    * ``IDS basados en máquina``: sistemas que analizan actividades de una única máquina en busca de posibles ataques.
      Realizan su función protegiendo un único sistema, es un proceso que trabaja en background buscando patrones de
      eventos y alertando o tomando las medidas oportunas en caso de que uno de estos intentos sea detectado.
    * ``IDS basados en red``: sistemas que analizan una subred (generalmente en un mismo dominio de difusión), en busca
      de posibles ataques. Monitoriza los paquetes que circulan por un segmento de red, puede situarse en cualquier de
      los hosts o en un elemento que analice todo el tráfico (como un switch o un router). Monitorizara todo el tráfico
      del segmento, es necesario que le puerto del switch al que se conecta el IDS sea configurado con la funcionalidad
      de “port mirroring”.

* > ``Sistemas de decepción (honeypots)``: mecanismos encargados de simular servicios con problemas de seguridad de forma que un atacante piense que realmente es problema se puede aprovechar para acceder a un sistema cuando realmente se está aprovechado para registrar todas sus actividades, es un mecanismo útil para conseguir entretener al atacante mientras se localiza su conexión.
* > El objetivo fundamental es obtener información del atacante.

#### 2.2 VIRTUAL PRIVATE NETWORK

* Técnica que permite crear una red privada sobre una infraestructura de red pública, manteniendo sus características de
  seguridad. Se utilizan protocolos de “tunneling” criptográfico para proporcionar los servicios de autenticación de
  origen, integridad del mensaje y confidencialidad, La clave de la tecnología VPN es la seguridad, que se consigue
  mediante el encapsulamiento (tunneling) cifrado y mecanismos de autenticación. Se pueden clasificar en overlay VPNs y
  peer-to-peer VPN:
    * ``Overlay VPN``: los proveedores de servicios proporcionan comunicaciones seguras a través de su backbone. Dichos
      circuitos son establecidos antes de que se puedan enviar datos. Este tipo de VPN puede presentar una serie de
      inconvenientes como su diseño complejo desde el punto de vista del cliente o la problemática al incrementar el
      número de clientes. Se pueden crear VPN de este tipo a nivel de capa 2, 3 o 5 de la pila TCP/IP:
        * ``L2`` Overlay VPN (capa enlace de datos): circuitos virtuales de ATM y Frame Relay
        * ``L3`` Overlay VPN (capa de red): encapsulamiento de paquetes IP en paquetes IP
        * ``L5`` Overlay VPN (capa de aplicacion): WebVPN o VPN over SSL

    * ``Peer-to-peer VPN``: utiliza MPLS que permite combinar las ventajas de Overlay VPN con las de enrutamiento
      simplificado entre los peers de la VPN, enrutamiento sencillo para el cliente, variedad de tipologías...

* > ``MPLS (Multiprotocol Label Switching)``: opera entre la capa de enlace de datos y la capa de red del modelo OSI.
* > Fue diseñado para unificar el servicio de transporte de datos para las redes basadas en circuitos y las basadas en paquetes.
* > Puede ser utilizado para transportar diferentes tipos de tráfico, incluyendo tráfico de voz y de paquetes IP.
* > Reemplazó a Frame Relay y ATM como la tecnología preferida para llevar datos de alta velocidad y voz digital en una sola conexión.

#### 3.2. IPSEC

* Es un “framework” de seguridad que define como crear VPN sobre redes IP, se basa en la utilización de protocolos de
  encapsulamiento (ESP, AH), algoritmos de cifrado (DES, 3DES, AES), algoritmos de autenticación (MD-5, SHA-1),
  mecanismos de gestión de claves y dominios de interpretación.
* Proporciona servicios de seguridad en la capa IP, permitiendo que los sistemas elijan los protocolos necesarios,
  determinen que algoritmos se van a utilizar en cada servicio y facilite la gestión de las claves criptografía
  asociadas con cada servicio proporcionado.
* IPSec puede funcionar en dos modos:
    * ``Modo de transporte``: proporción protección de los protocolos de capa superior, protege la carga útil (payload),
      se utiliza este modo cuando la VPN se establece de extremo a extremo entre dos dispositivos finales.
    * ``Modo túnel``: proporciona protección al paquete IP completo, después de haber añadido la cabecera AH o ESP al
      paquete IP original, se le añade una nueva cabecera IP dando lugar a un nuevo paquete IP cuyo payload es el
      paquete IP original encapsulado en ESP o AH. La cabecera del paquete original queda por lo tanto también
      protegida. El modo túnel suele utilizarse cuando al menos uno de los extremos de la VPN es una pasarela VPN (
      router, cortafuegos, concentrador).

* > GRE (Generic Routing Encapsulation): protocolo para el establecimiento de túneles a través de Internet

#### 3.3. PROTOCOLOS DE VPN

* ``Authentication Header`` (AH): proporciona soporte para la integridad y la autenticación de paquetes IP.
* La autenticación puede estar relacionada tanto con el control de acceso de un usuario o aplicación como con la
  verificación del origen de los paquetes, para evitar ataques basados en “IP Spoofing”.
* También proporciona protección frente a ataques de repetición de mensajes.
* La autenticación se basa en la utilización MAC lo que implica que los dos extremos de la VPN deben compartir una clave
  secreta para utilizar esta técnica.
* La cabecera AH se compone de:
    * ``Next Header``: identifica el tipo de cabecera que encapsula AH.
    * ``Payload Length``: longitud de la carga útil.
    * ``Reservado``.
    * ``SPI``: índice de parámetros de seguridad, identifica la SA con la que está vinculando el mensaje.
    * ``Sequence Number``: permite implementar servicios de defensa frente a ataques de repetición.
    * ``Authentication Data``: campo de longitud variable que contiene el valor de comprobación de integridad (Integrity
      Check Value, ICV) o el Message Autheticacion Code (MAC).

* Encapsulamiento de seguridad de la carga útil (Encapsulation Payload Security): es un protocolo que encapsula la carga
  útil (payload) del paquete original, pudiendo proporcionar servicios de confidencialidad y autenticación (
  opcionalmente)
  .
* La cabecera ESP consta de:
    * ``Índice de Parámetros de Seguridad`` (SPI): identifica la SA.
    * ``Número de secuencia`` (Sequence Number): este campo permite implementar servicios de defensa frente a ataques de
      repetición.
    * Carga útil: es la PDU de capa de transporte (modo transporte) o el paquete IP (modo túnel) protegido mediante
      cifrado.
    * Relleno.
    * Longitud de relleno.
    * Siguiente cabecera (Next Header): identifica el tipo de cabecera que encapsula ESP.
    * Datos de Autenticacion (Authentication Data): longitud variable que contiene el valor de comprobación de
      integridad.

* El protocolo de gestión de claves automático predeterminado para IPSec se conoce como ISAKMP/Oalkey y está formado
  por:
    * ``Protocolo de Determinación de Claves Oakley``: es un protocolo de intercambio de claves basado en el algoritmo
      Diffie-Hellman.
    * ``ISAKMP`` (Intertet Security Asociation Key Management Protocol): es un “framework” de gestión de claves y el
      soporte de un protocolo especifico, incluyendo formatos para la negociación de los atributos de seguridad. ISAKMP
      define los procedimientos y los formatos de los paquetes para establecer, negociar, modificar y eliminar las
      asociaciones de seguridad. Como parte del establecimiento de la SA, ISAKMP define las cargas útiles para
      intercambiar durante la generación de calves, así como los datos de autenticación.

* > ``OpenVPN``:
    * > Es un “framework” para el establecimiento de VPN basado en software libre.
    * > Ofrece conectividad punto a punto con validación jerárquica de usuarios y host conectados remotamente.
    * > Es una solución multiplataforma que pretende simplificar la configuración de VPN frente a otras soluciones más difíciles de configurar como IPSec.
    * > OpenVPN tiene dos modos seguros, uno basado en calves estáticas precompartidas y otro en SSL/TLS usando certificados y claves RSA.

## TEMA 7 – CIFRADO, FIRMA DIGITAL Y CERTIFICADOS DIGITALES

### 1\. TÉCNICAS CRIPTOGRAFICAS Y PROTOCLOS SEGUROS. MECANISMO DE FIRMA DIGITAL

* ``Criptografía``: se define como el arte de escribir con clave secreta o de un modo enigmático.
* ``Criptología``: ciencia que estudia la ocultación, disimulación o cifrado de la información. Abarca por tanto a la
  criptografía, la criptofonía y el criptoanálisis, ciencia que estudia los pasos y operaciones orientados a transformar
  un criptograma en el texto claro original pro sin conocer inicialmente el sistema de cifrado utilizado y/o la clave.
  La finalidad de esta técnica ha sido siempre enviar menajes confidenciales con la garantía de que solo el destinatario
  de los mismo pudiera acceder a la información contenida en el mensaje.
* ``Criptografía``: desarrolla métodos que consisten en la aplicación de una transformación al mensaje conocida como
  cifrado, con el objetivo de que las personas que desconozcan la transformación realizada sean incapaces de acceder a
  la información contenida en el mensaje.
* ``Criptoanálisis``: su finalidad es descubrir la clave de cifrado, un algoritmo de cifrado es más o menos vulnerable
  en función de la dificultad de la tarea de descubrimiento de la clave.
* ``Esteganografía``: lo que busca es ocultar un mensaje ante un posible atacante, pero la diferencia estaba en como
  oculta la información ambas técnicas: mientras que la criptografía pretende que la información no sea descifrada, la
  esteganografía lo que pretende es que la información pase desapercibida.

#### 1.1. TÉCNICAS CRIPTOGRÁFICAS

* ``Técnicas criptográficas clásicas``: realizan el cifrado en base a la sustitución y transposición de los caracteres
  del mensaje, es crucial ocultar el algoritmo a los atacantes, ya que si un atacante lo descubre será capaz de
  interpretar todos los mensajes cifrados que capture, como el algoritmo Cesar, cifrado Vigenere...
* ``Técnicas criptográficas modernas``: utilizan claves de cifrado, la seguridad del método debe depender únicamente de
  la clave de cifrado, esta premisa hace que estas técnicas resulten mucho más segura y efectivas, ya que resulta más
  sencillo mantener el secreto de la clave y además cambiar la clave de cifrado siempre será menos costoso que idear un
  nuevo algoritmo resultando frecuente que la clave de cifrado se genere de forma automática, se pueden clasificar
  atendiendo a las claves que utilizan o al modo en que procesan la información.
* Tipo de claves que utilizan.
    * ``Cifrado simétrico o de clave privada``: utiliza una clave secreta para cifrar y descifrar un mensaje, deben
      cumplirse dos requisitos fundamentales, que el algoritmo que se utiliza debe ser robusto, si una tercera persona
      no autorizada está en posesión del mensaje, no debería ser capaz de descifrar el texto ni de obtener la clave con
      la que fue cifrado. Además, la selección, envío, almacenamiento y utilización de las claves debe ser totalmente
      segura, de forma que las entidades no autorizadas no puedan acceder a ellas. Los cifradores de bloques son los
      algoritmos de cifrado simétrico más utilizados, dividen el mensaje original en bloque de igual tamaño que después
      serán cifrado con la misma clave. Los algoritmos de este tipo más importantes en la actualidad son:
        * ``DES`` (Data Encryption Standard): diseñado para cifrar y descifrar bloques de datos de 64 bits con una clave
          secreta de 56 bits. Un bloque que va a ser cifrado debe someterse primero a una permutación inicial,
          posteriormente a un computación compleja y dependiente de la clave y finalmente, a una permutación inversa a
          la permutación inicial.
        * ``3DES`` (Triple DES): utiliza tres claves y tres ejecuciones del algoritmo, de esta forma el tamaño efectivo
          de la clave pasa a ser 168 bits, con tres veces más etapas que DES utiliza un tamaño de bloque de 64 bits.
        * ``AES`` (Advanced Encryption Standard): capaz de soportar longitudes de clave de 128, 192 y 256 bits y
          longitud de bloque 128 bits.
        * ``IDEA`` (International Data Encryption Algorithm): algoritmo propuesto como reemplazo del DES (Data
          Encryption Standard). Opera con bloques de 64 bits usando una clave de 128 bits y consiste de ocho
          transformaciones idénticas (
          cada una llamada una ronda) y una transformación de salida (llamada media ronda).
        * ``RC5`` (Cifrado de Rivest v.5): unidad de cifrado por bloques notable por su simplicidad. A diferencia de
          muchos esquemas, RC5 tiene tamaño variable de bloques (32, 64 o 128 bits), con tamaño de clave (entre 0 y 2040
          bits) y número de vueltas (entre 0 y 255). La combinación sugerida originalmente era: bloques de 64 bits,
          claves de 128 bits y 12 vueltas.
        * ``Sistemas de cifrado asimétrico o de clave pública``: basada en el uso de dos claves, una clave privada y
          otra publica, una de ellas sirve para descifrar los mensajes que han sido cifrado únicamente con la otras. Los
          algoritmos utilizados para cifrar y descifrar no utilizan operaciones sobre los patrones de bits, sino que se
          apoyan en problemas matemáticos difíciles de resolver. Este tipo de criptosistemas puede ser utilizado, para
          cifrar y descifrar mensajes, intercambiar claves de sesión y para firmar digitalmente los mensajes. Ejemplos
          de sistemas de criptografía pública:
            * ``Diffie-Hellman``: mecanismo que permite que dos partes se pongan de acuerdo de forma segura sobre una
              clave secreta utilizando un canal inseguro, el algoritmo se basa en la dificultad de calcular logaritmos
              discretos y se usa generalmente como medio para acordar calves simétricas que será empleadas para el
              cifrado de una sesión.
        * ``RSA``: es el algoritmo más utilizado en la historia de la criptografía de clave pública. La clave publica
          está formada por un numero n, calculando como producto de dos factores primos muy grandes y un exponente. La
          clave privada es otro exponente de tal forma que el cifrado y el descifrado se puede realizar inversamente, la
          clave pública y la privada son intercambiables: si se usa cualquier de ellas para cifrar se deberá utilizar la
          otra para descifrar.
        * ``DSA`` (Digital Signature Algorithm): este algoritmo como su nombre lo indica, sirve para firmar (autenticar)
          , pero no para cifrar información.

* > Para asegurar que la clave pública del destinatario es realmente de quien dice ser, surgen las autoridades de certificación. 
* > “Trusted Third Parties”, entidades que merecen la confianza de otros actores en un escenario de seguridad donde no existe confianza directa entre las partes involucradas en una cierta transacción. 
* > Es necesaria aun infraestructura de clave publica para cerrar el círculo de confianza. 
* > Esta infraestructura de clave publica consta de una serie de autoridades que se especializan en papeles concretos: 
  * > Autoridades de certificación (CA o certificación authorities): vinculan la clave publica a la entidad registrada proporcionado un servicio de identificación. 
  * > Autoridades de registro (RA o registration authorities): ligan entes registrados a figuras jurídicas, extendiendo la accesibilidad de las CA. 
  * > Autoridades de fechado digital (TSA o time stamping authorities): vinculan un instante de tiempo a un documento electrónico avalando con su firma la existencia del documento en el instante referenciado (exactitud temporal de los documentos electrónicos).

  * ``Funciones HASH``: operación que se aplica sobre un conjunto de datos de cualquier tamaño para obtener una “huella”
    o “resumen” del mismo. Una función hash debe producir una salida de tamaño fijo, independiente del tamaño del
    conjunto de datos de entrada relativamente fácil de computar para cualquier conjunto de datos, asociada unívocamente
    a los datos de la entrada, haciendo prácticamente imposible encontrardos mensajes distintos que tengan igual
    resumen (
    resistencia fuerte a las colisiones) y unidireccional en el sentido de que es imposible obtener le conjunto de dato
    inicial a partir del valor de resumen.
      * ``MD5``: este algoritmo de resumen de mensaje procesa los mensajes de entidad en bloques de 512 bits y produce
        un resumen de 128 bits. Comienza rellenando el mensaje original hasta una longitud 64 bits inferior a un
        múltiplo de 512\. Antes de procesar el primer bloque del mensaje se inicializa con un valor fijo un buffer de
        128 bits. Durante varias rondas de procesamiento el algoritmo toma bloques de 512 bits de la entrada y los
        mezcla con los 128 bits del buffer. Este proceso es repetido hasta que todos los bloques de entrada han sido
        consumidos. El valor resultante en el buffer es el resumen del mensaje.
      * ``SHA-1``: el procesamiento del algoritmo es similar al de MD5. Se toma como entradaun mensaje con longitud
        máxima menor que 2^64 bits y produce en la salida un resumen de 160 bits. La entrada se procesa en bloques de
        512 bits. SHA-2 lo sustituye debido a debilidades matemáticas que fueron solucionadas usando una función hash
        más fuerte. Mas tarde se libera SHA-3.

### 2\. FIRMA DIGITAL Y CERTIFICADOS DIGITALES

#### 2.1 FIRMA DIGITAL

* Es una de las aplicaciones más importantes que posibilita la utilización de la criptografía de clave pública, es un
  bloque de caracteres que acompaña a un documento (o fichero) acreditando quien es su autor (autenticación) y que no ha
  existido ninguna manipulación posterior de los datos (integridad) para firmar un documento digital, su autoría queda
  vinculado al documento de la firma, dicha firma podrá ser comprobada por cualquier persona que disponga de la clave
  pública del autor.
* La firma se realiza de modo que el software del firmante aplica un algoritmo hash sobre el texto a firmar (
  unidireccional, lo cifrado no se puede descifrar), extracto de longitud ficha y absolutamente específico para ese
  mensaje.
* Los algoritmos has más utilizados para esta función son el MD5 o SHA-1.
* El extracto conseguido cuya longitud oscila entre 128 y 1690 bits, se somete a continuación al cifrado mediante la
  clave secreta del autor.
* El algoritmo más utilizado en el procedimiento de encriptación asimétrica es el RSA, obtenemos un extracto final
  cifrado con la clave privada del autor el cual se añadirá al final del texto o mensaje para que se pueda verificar la
  autoría e integridad del documento por aquella persona interesada que disponga de la calve pública del autor.
* La firma digital aporta la identificación del firmante, integridad del contenido firmado y no repudio del firmante.

#### 2.2 CERTIFICADOS DIGITALES

* Es un documento que permite vincular una clave pública a una entidad ya sea un usuario, una organización...
* Dos entidades que no se conocen previamente pueden intercambiar sus claves públicas.
* Al comienzo de una comunicación, el emisor envía su clave publica dentro de un certificado digital al receptor, que al
  recibir el certificado debería verificar su validez, que la clave publica pertenece realmente a la entidad con la que
  está vinculada.
* Public Key Infrastructure (PKI): conjunto de componentes y políticas necearías para crear, gestionar y revocar
  certificados digitales que pueden ser utilizados para autenticar cualquier aplicación, persona, proceso u organización
  de una red de empresa, extranet o Internet. Está formada por cinco actores principales:
    * ``Autoridades de Certificación`` (CA): responsables de emitir y revocar certificados digitales.
    * ``Autoridades de Registro`` (RA): verifican la unión entre las claves públicas y la identidad de los propietarios
      mediante un “proceso de registro”.
    * ``Usuarios certificados`` o “suscriptores”: personas, organización o cualquier entidad que utilice el certificado
      proporcionado por un CA
    * ``Clientes``: poseen un documento firmado de un usuario certificado y desean comprobar su validez.
    * ``Repositorio``: directorio central donde se almacenan los certificados.

## TEMA 8 – CPD, CERES Y CCN-CERT  
### 1\. CPD (Centro de Proceso de Datos):  
* Ubicación donde se concentran todos los recursos necesarios para el almacenamiento, procesado y transmisión de la
información de una organización, buscando garantiza la continuidad y disponibilidad de los servicios basados en dicha
información; realiza funciones de servicios para las toras operaciones de la organización, el objetivo principal es
concentrar el procesado de los datos y la información de formal sistematizada y automática de formal que fluyan y
organice sin importar el volumen. 
* Sigue el estándar TIA-942 que define directrices de planificación y construcción d
CPD, la norma trabaja con cobre y fibra óptica como medios de transmisión, especifica las necesidades para aplicaciones
y procedimientos como la arquitectura de red, diseño eléctrico, almacenamiento de archivos, backup y archivo... 
* La norma
TIA-942 recomienda las siguientes áreas funcionales clave:  
  * ``Uno o más cuartos de entrada``: alberga el equipo de los operadores de telefonía y el punto de demarcación.  
  * ``Un Área de Distribución Principal`` (MDA): alberga el punto de conexión cruzada central para el sistema de cableado
  estructurado dl centro de datos. Ubicada en una zona central, racks separados para los cables de fibra, UTP y coaxial.  
  * ``Una o más Áreas de Distribución Horizontal`` (HDA): ubicación de las interconexiones horizontales, el punto de
  distribución para el cableado hacia las áreas de distribución de los equipos, máximo 2000 cables UTP de 4 pares.  
  * ``Un Área de Distribución de Zona`` (ZDA): cableado estructurado para los equipos que van en el suelo y no pueden
  aceptar paneles de parcheo, computadoras centrales y servidores.  
  * ``Un Área de Distribución de Equipos``: ubicación de los gabinetes y racks de equipos, colocar en una configuración “hot
  aisle/cold aisle” (pasillos) que disipen de manera eficaz el calor de los equipos. El sistema de cableado de un CPD debe
  deseñarse teniendo en mente que tiene que ser permanente y genérico, debe seguir las normas EIA/TIA-568, que garantizan
  que los sistemas que se ejecuten de acuerdo a ella soportaran todas las aplicaciones de telecomunicaciones presentes y
  futuras por un lapso de al menos diez años.

* Para refrigeración se emplean unidades ``CRAC`` (Computer Room Air Conditioner) con ciclo de refrigeración autónomo para
extraer el calor de la sala y alejarlo del CPD, intercambiadores de calor basados en el principio de equilibrio térmico
y expansión directa de un fluido refrigerante.  
  * ``CRAH`` (Computer Room Air Handling): que utilizan agua fría en circulación para extraer el calor. Para favorecer la
  circulación de aire se usan diferentes arquitecturas de refrigeración en salas (método tradicional utilizado para
  refrigerar un CPD donde uno o más equipos de aire acondicionado que suministran aire frio sin ningún tipo de
  restricción), filas (las unidades de CRAC están asociadas y dedicada a una fila, las vías de circulación de aire son más
  cortas y están definida scon mayor claridad que en la refrigeración por salas), pasillos (eliminan los puntos calientes
  típicos de los centros de datos tradicionales gracias a la disposición de pasillos fríos (CACS, Cold Aisle Containment
  System) / pasillos calientes (HACS, Hot Aisle Containment System)) o racks (las unidades de CRAC están asociadas y
  dedicadas a un único rack, se montan directamente al lado o dentro de los racks).

* Las medidas a tomar dependerán del nivel de fiabilidad requerido y de los costos, mantener un equilibrio sopesando el
coste que tendría para la empresa un “apagón”. Para ayudar a estimar el nivel de fiabilidad de un CPD, la norma TIA-492
desarrolla cuatro niveles denominados Tier: el nivel I brinda la menor fiabilidad y el IV, la mayor. Se crearon para
describir consistentemente la infraestructura requerida para mantener las operaciones de los centros de datos, no las
características de sistemas individuales o subsistemas. El grado de la topología Tier para un sitio está limitado por el
grado del subsistema más débil que afectara a las operaciones del sitio.  
  * ``Tier I`` (CPD Básico): un CPD Tier I puede admitir interrupciones tanto planeadas como no planeadas. Cuenta con
  sistemas de aire acondicionado y distribución de energía, pero puede no tener piso técnico, UPS o generador eléctrico.
  La carga máxima de los sistemas en situaciones críticas puede llegar al 100%, el CPD deberá estar fuera de servicio al
  menos una vez al año por razones de mantenimiento y o reparaciones. Errores de operación fo fallas en los componentes de
  su infraestructura causaran la interrupción del CPD.  
  * ``Tier II`` (Componentes Redundantes): un CPD con componentes redundantes son ligeramentemenos susceptibles a
  interrupciones, tanto planeadas como las no planeadas. Cuentan con suelo técnico, UPS y generadores eléctricos,
  conectado a una sola línea de distribución eléctrica, existe al menos un duplicado de cada componente de la
  infraestructura. La carga máxima de los sistemas en situaciones críticas es del 100%. El mantenimiento en la línea de
  distribución eléctrica o en otros componentes, pueden causar una interrupción del servicio.  
  * ``Tier III`` (Mantenimiento Concurrente): permiten realizar cualquier actividad planeada sobre cualquier componente de
  la infraestructura sin interrupciones en la operación, incluyen mantenimiento preventivo, reparaciones o reemplazo de
  componentes, agregar o eliminar componentes, realizar pruebas de sistemas o subsistemas, entre otros. Suficiente
  capacidad y doble línea de distribución de los componentes, actividades no planeadas como errores de operación o fallos
  espontaneas den la infraestructura pueden todavía causar una interrupción del CPD. La carga máxima en los sistemas en
  situaciones críticas es de 90%.  
  * ``Tier IV`` (Tolerante a Fallos): provee capacidad para realizar cualquier actividad planeada sin interrupciones en el
  servicio, la funcionalidad tolerante a fallos le permite a la infraestructura continúa operando aun ante un evento
  critico no planeado. Esto requiere dos líneas de distribución simultáneamente activas (UPS independientes). La carga
  máxima de los sistemas de situaciones críticas des de 90%. Persiste un nivel de exposición a fallos, por el inicio una
  alarma de incendio o porque una persona inicie un procedimiento de apagado de emergencia (EPO).

* > CSIRT (Computer Security Incident Response Team): está formado por las personas que cuentan con la experiencia y la formación para actuar y gestionar las incidencia y desastres que pudieran afectar a la seguridad informática de una organización. 
* > Definen una guía de actuación con los procedimientos y acciones necesarios para restauración rápida, eficiente y segura de la capacidad de procesamiento informático y de comunicaciones de la organización, así como para la recuperación de los datos dañados o destruidos. 
* > Debe proporcionar una respuesta sistemática ante los incidentes de seguridad, permitirá minimizar los daos ocasionados y facilitar la recuperación del sistema afectado. 
* > El “Plan de Respuesta a Incidentes” debe definir cómo se ha producido el incidente (el tipo de ataque, que métodos ha empleado...), utilizando una matriz de diagnóstico, realiza una valoración inicio de los daños y de sus posibles consecuencias, establecer un orden de prioridades en las actividades que lleva a cabo el equipo de respuesta.

### 2\. SISTEMAS ALIMENTACIÓN ININTERRUMPIDA  
* Es un dispositivo que puede proporcionar energía eléctrica a todos los dispositivos que tenga conectados, tras un corte
en la red de alimentación. Se basa en el uso de baterías recargables, el tiempo de interrupción es limitado,
proporcional a la capacidad de las baterías, permiten un apagado “ordenado” de los dispositivos para evitar daños en
discos os sistemas de ficheros, tienen filtro de subidas y picos de tensión y pueden eliminar problemas de frecuencia.
* Existirán SAIs centralizadas en el CPD para dar alimentación eléctrica durante un periodo corto de tiempo, equipos
siguen funcionando más allá de este tiempo de paradas, será necesario utilizar “grupos electrógenos”, existen 3 tipos de
SAI:  
  * ``SAI Offline``: son económicos (equipos no críticos), no disponen de estabilizador de corriente, solamente generan
  tensión en caso de corte en el suministro eléctrico...  
  * ``SAI Inline``: incorporan un estabilizador de corriente, solamente generan tensión en caso de corte...  
  * ``SAI Online``: diseñado para proteger sistemas críticos, siempre generan tensión eléctrica, independientemente de la
  entrada...

#### 7.5. CCN-CERT  
* Dentro de las funciones del Centro Criptológico Nacional se encuentra la coordinación, promoción y desarrollo de
soluciones que garanticen la seguridad de los sistemas y contribuyan a una mejor gestión de la ciberseguridad en
cualquier organización y permitan una mejor defensa frente a los ciberataques. Entre estas soluciones se encuentran las
siguientes:  
  * ``ADA``: Plataforma avanz``ada`` de análisis de malware.  
  * ``AMPARO``: Implantación de ``seguridad`` y conformidad con el ENS.  
  * ``CARMEN``: Defensa de ataques avanzados/APT.  
  * ``microCLAUDIA``: ``C``entro de ``vacunación``.  
  * ``CLAUDIA``: Herramienta para la ``d``etecc``i``ón de ``a``menazas ``c``omplejas en el puesto de usuario.  
  * ``CLARA``: ``A``uditoría de ``c``umplimiento ENS/STIC en sistemas windows.  
  * ``ANA``: ``A``utomatización y ``n``ormalización de ``a``uditorías.  
  * ``ELENA``: Simulador d``e`` técnicas de vigilanci``a``.  
  * ``ELSA``: ``E``xposición ``l``ocal y ``s``uperficie de ``a``taque.  
  * ``IRIS``: Estado de la c``i``be``r``segur``i``dad.  
  * ``GLORIA``: ``G``estor de ``lo``gs.  
  * ``LUCÍA``: Sistemas de gestión federada de tickets.  
  * ``MARTA``: ``A``nálisis ``a``vanzados de ficheros.  
  * ``LORETO``: Almacenamiento en la nube.  
  * ``OLVIDO``: Borrado seguro de datos.  
  * ``MÓNICA``: Gesti``ó``n de eve``n``tos e ``i``nforma``c``ión de segurid``a``d.  
  * ``INÉS``: ``In``forme del ``E``stado de ``S``eguridad en el ENS.  
  * ``REYES``: Intercambio de información de ciberamenazas.  
  * ``PILAR``: ``A``nálisis y gestión de ``r``iesgos.  
  * ``metaOLVIDO``: Gestión de ``meta``datos.  
  * ``ATENEA``: Pl``at``aforma d``e`` desafíos de s``e``gurid``a``d.  
  * ``VANESA``: Gra``ba``cio``n``es y ``e``misiones de vídeo en ``s``tre``a``ming.  
  * ``ROCÍO``: Inspección de operación. Audito``r``ía de c``o``nfigura``cio``nes de dispositivos de red.

- > ``CERES``: iniciativa puesta en marcha por la Administración, consiste en establecer una entidad pública de certificación que permita autentificar y garantizar la confidencialidad de las comunicaciones entre ciudadanos, empresas u otras instituciones ya administración públicas a través de las redes abiertas de comunicación.

