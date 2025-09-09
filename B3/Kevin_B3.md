# Temario TAI Kevin adaptado

## Bloque III

### PROGRAMACIÓN POR CAPAS

* Modelo de desarrollo software en el que el objetivo primordial es la separación (desacoplamiento) de las partes que
  componen un sistema de software o también una arquitectura cliente-servidor. Se divide en: ``lógica de negocios``
  , ``capa de presentación`` y ``capa de datos``. La ventaja principal de este estilo es que el desarrollo se puede
  llevar a cabo en varios niveles y, en caso de que sobrevenga algún cambio, solo afectará al nivel requerido sin tener
  que revisar entre el código fuente de otros módulos.
* ``Capa de presentación``: la que ve el usuario (también se la denomina ``capa de usuario``), presenta el sistema al
  usuario, le comunica la información y captura la información del usuario en un mínimo de proceso (realiza un filtrado
  previo para comprobar que no hay errores de formato). También es conocida como interfaz gráfica y debe tener la
  característica de ser «amigable» (entendible y fácil de usar) para el usuario. Esta capa se comunica únicamente con la
  capa de negocio.
* ``Capa de negocio``: es donde residen los programas que se ejecutan, se reciben las peticiones del usuario y se envían
  las respuestas tras el proceso. Se denomina capa de negocio (e incluso de lógica del negocio) porque es aquí donde se
  establecen todas las reglas que deben cumplirse. Esta capa se comunica con la capa de presentación, para recibir las
  solicitudes y presentar los resultados, y con la capa de datos, para solicitar al gestor de base de datos almacenar o
  recuperar datos de él. También se consideran aquí los programas de aplicación.
* ``Capa de datos``: es donde residen los datos y es la encargada de acceder a los mismos. Está formada por uno o más
  gestores de bases de datos que realizan todo el almacenamiento de datos, reciben solicitudes de almacenamiento o
  recuperación de información desde la capa de negocio.

> ``IDE`` (Integrated Development Environment): aplicación informática que proporciona servicios integrales para facilitarle al desarrollador o programador el desarrollo de software. webStorm: un IDE multiplataforma principalmente para desarrollo web, JavaScript y TypeScript.

### 1\. PATRONES DE DISEÑO

* Son técnicas para resolver problemas comunes en el desarrollo de software y otros ámbitos referentes al diseño de
  interacción o interfaces, sirven para crear objetos comunes con pequeñas diferencias entre ellos (de ahí el nombre de
  patrón), según la escala o nivel de abstracción, pueden ser:
    * ``Patrones creacionales``: patrones de diseño de software que solucionan problemas de creación de instancias. Nos
      ayudan a encapsular y abstraer dicha creación, los tipos son:
        * ``Singleton``: garantiza la existencia de una única instancia para una clase y la creación de un mecanismo de
          acceso global a dicha instancia. Restringe la instanciación de una clase o valor de un tipo a un solo objeto.
        * ``Abstract Factory``: permite trabajar con objetos de distintas familias de manera que las familias no se
          mezclen entre sí y haciendo transparente el tipo de familia concreta que se esté usando. El problema a
          solucionar por este patrón es el de crear diferentes familias de objetos, como por ejemplo, la creación de
          interfaces gráficas de distintos tipos (ventana, menú, botón...).
        * ``Builder``: permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y
          representaciones de un objeto empleando el mismo código de construcción.
        * ``Factory Method``: centraliza en una clase constructora la creación de objetos de un subtipo de un tipo
          determinado, ocultando al usuario la casuística, es decir, la diversidad de casos particulares que se pueden
          prever, para elegir el subtipo que crear. Parte del principio de que las subclases determinan la clase a
          implementar.
        * ``Prototype``: permite copiar objetos existentes sin que el código dependa de sus clases.

    * ``Patrones estructurales``: patrones de diseño software que solucionan problema de composición (agregación) de
      clases y objetos:
        * ``Adapter/Wraper``: adapta una interfaz para que pueda ser utilizada por una clase que de otro modo no podría
          utilizarla.
        * ``Bridge``: desvincula una abstracción de su implementación. Permite dividir una clase grande, o un grupo de
          clases estrechamente relacionadas, en dos jerarquías separadas (abstracción e implementación) que pueden
          desarrollarse independientemente la una de la otra.
        * ``Composite``: permite componer objetos en estructuras de árbol y trabajar con esas estructuras como si fueran
          objetos individuales.
        * ``Decorator``: permite añadir funcionalidades a objetos colocando estos objetos dentro de objetos
          encapsuladores especiales que contienen estas funcionalidades.
        * ``Facade``: provee de una interfaz unificada simple para acceder a una interfaz o grupo de interfaces de un
          subsistema.
        * ``Flyweight``: reduce la redundancia cuando gran cantidad de objetos poseen idéntica información.
        * ``Proxy``: proporciona un sustituto o marcador de posición para otro objeto. Un proxy controla el acceso al
          objeto original, permitiéndote hacer algo antes o después de que la solicitud llegue al objeto original.

    * ``Patrones de comportamiento``: patrones de diseño software que ofrecen soluciones respecto a la interacción y
      responsabilidades entre clases y objetos, así como los algoritmos que encapsulan:
        * ``Chain of Responsability``: permite pasar solicitudes a lo largo de una cadena de manejadores. Al recibir una
          solicitud, cada manejador decide si la procesa o si la pasa al siguiente manejador de la cadena.
        * ``Command``: encapsula una operación en un objeto, permitiendo ejecutar dicha operación sin necesidad de
          conocer el contenido de la misma.
        * ``Interpreter``: dado un lenguaje, define una representación para su gramática junto con un intérprete del
          lenguaje.
        * ``Iterator``: permite realizar recorridos sobre objetos compuestos independientemente de la implementación de
          estos.
        * ``Mediator``: define un objeto que coordine la comunicación entre objetos de distintas clases, para que
          funcionen como un conjunto.
        * ``Memento``: permite guardar y restaurar el estado previo de un objeto sin revelar los detalles de su
          implementación.
        * ``Observer``: define una dependencia de uno-a-muchos entre objetos, de forma que cuando un objeto cambie de
          estado se notifique y actualicen automáticamente todos los objetos que dependen de él.
        * ``State``: permite que un objeto modifique su comportamiento cada vez que cambie su estado interno, es decir,
          parece como si el objeto cambiara su clase.
        * ``Strategy``: permite disponer de varios métodos para resolver un problema y elegir cuál utilizar en tiempo de
          ejecución.
        * ``Template Method``: define en una operación el esqueleto de un algoritmo en la superclase, delegando en las
          subclases algunos de sus pasos, esto permite que las subclases redefinan ciertos pasos de un algoritmo sin
          cambiar su estructura.
        * ``Visitor``: permite definir nuevas operaciones sobre una jerarquía de clases sin modificar las clases sobre
          las que opera, es decir, separar algoritmos de los objetos sobre los que operan.

### 2\. JAVA EE (JAKARTA EE)

* Plataforma de programación para desarrollar y ejecutar software de aplicaciones en el lenguaje de programación Java.
  Utiliza arquitecturas de N capas distribuidas y se apoya ampliamente en componentes de software modulares ejecutándose
  sobre un servidor de aplicaciones. La arquitectura Java EE está basada en tres conceptos clave:
    * ``Servicios``: Permiten que el programador se concentre en su lógica de negocio y usar estos servicios para su
      aplicación. Estos servicios pueden tener funcionalidades de seguridad, comunicaciones de red, logging, integridad
      de datos, etc. Estos servicios son proporcionados por un contenedor.
    * ``Contenedores``: Son entornos en tiempo de ejecución, es decir un programa que se está ejecutando y tu aplicación
      la montas sobre este como si fuera un plugin o el casete para una consola de juegos. Hay varios tipos de
      contenedores y la agrupación de ellos forman un servidor de aplicaciones.
    * ``Componentes``: Son objetos Java que contienen la lógica de negocio de la aplicación y usan los servicios
      proporcionados por el contenedor. Hay varios tipos de componentes y según ese tipo son desplegados en un
      contenedor u otro.  
      Estos tres conceptos permiten a Java EE definir una arquitectura de capas:
    * ``Capa cliente``: Con componentes que corren en la máquina del cliente (como un navegador, un smartphone o un
      ordenador de escritorio)
    * ``Capa web``: Corre en el servidor Java EE o servidor de aplicaciones y se comunica con la capa web y la de capa
      de negocio de tal manera que transforma la información al formato adecuado (por ejemplo HTML).
    * ``Capa de servidor/negocio``: Proporciona los datos y persiste la información de la capa cliente y contiene la
      capa de negocio. También se ejecuta en el servidor de aplicaciones.
    * ``Capa de datos``: Donde se persisten los datos, por ejemplo una bbdd.

#### 2.1. API

* Tiene varias especificaciones de API, como JDBC, RMI, e-mail, JMS, Servicios Web, XML, etc y define cómo coordinarlos.
  Java EE también configura algunas especificaciones únicas para Java EE para componentes.
* Estas incluyen Enterprise JavaBeans, servlets, portlets (siguiendo la especificación de Portlets Java), JavaServer
  Pages y varias tecnologías de servicios web.
* Ello permite al desarrollador crear una aplicación de empresa portable entre plataformas y  
  escalable, a la vez que integrable con tecnologías anteriores.
* Otros beneficios añadidos son, que el servidor de aplicaciones puede manejar transacciones, la seguridad,
  escalabilidad, concurrencia y gestión de los componentes desplegados, significando que los desarrolladores pueden
  concentrarse más en la lógica de negocio de los componentes en lugar de tareas de mantenimiento del bajo nivel.
* Las API de Java EE incluyen varias tecnologías que extienden la funcionalidad de las API base de Java SE:
    * ``Javax.ejb`` (Enterprise JavaBeans): define un conjunto de API que un contenedor de objetos distribuidos
      soportará para suministrar persistencia, RPCs (usando RMI o RMI-IIOP), control de concurrencia, transacciones y
      control de acceso para objetos distribuidos.
    * ``Javax.naming``: forma parte de JNDI (Java Naming and Directory Interface), que es usada por Java RMI para buscar
      objetos en una red.
    * ``Java.sql:`` forma parte de JDBC (Java DataBase Conectivity), que es una API que permite la ejecución de
      operaciones sobre bases de datos desde Java, independientemente del sistema operativo donde se ejecute o de la
      base de datos a la cual se accede, utilizando el dialecto SQL del modelo de base de datos que se utilice.
    * ``Java.transaction``: forma parte de JTA, que establece una serie de Interfaces java entre el manejador de
      transacciones y las partes involucradas en el sistema de transacciones distribuidas: el servidor de aplicaciones,
      el manejador de recursos y las aplicaciones transaccionales.
    * ``Java.xml``: forma parte de JAXP (Java API for XML).
    * ``Java.jms``: forma parte de JMS (Java Message Service), solución para el uso de colas de mensajes.
    * ``Java.persistence``: provee las clases e interfaces para gestionar la interacción entre los proveedores de
      persistencia, las clases administradas y los clientes de la JPA (Java Persistence API).

2.2. TIPOS DE MODIFICADORES DE ACCESO JAVA  
Uno de los principios básicos de los lenguajes orientados a objetos es la encapsulación, mediante la cual se garantiza
que los datos de una clase solo son modificados por las operaciones apropiadas implementadas en los métodos de sus
clases para preservar su invariante, las reglas que define la clase y el estado consistente de su estado. El acceso a
las propiedades y métodos se determina mediante las palabras reservadas de los modificadores de acceso, en Java hay
cuatro modificadores de acceso que definen ámbitos de visibilidad de más a menos restrictivos:

* ``private``: únicamente la clase puede acceder a la propiedad o método.
* ``package private`` (valor por defecto si no se indica ninguno): solo las clases en el mismo paquete pueden acceder a
  la propiedad o método.
* ``protected``: las clases del mismo paquete y que heredan de la clase pueden acceder a la propiedad o método.
* ``public``: la propiedad o método es accesible desde cualquier método de otra clase.

#### 2.3. DATOS PRIMITIVOS

* Manipulan directamente el procesador y permiten almacenar datos simples numéricos, lógicos y de carácter. No
  representan objetos pero soportan “boxing” (ser tratadas como objetos):
    * Tipos de datos primitivos numéricos enteros:

        * ``byte`` (8 bits)
        * ``short`` (16 bits)
        * ``int`` (32 bits)
        * ``long`` (64 bits)

* Tipos de datos primitivos numéricos decimales (coma flotante):

    * ``float`` (32 bits)
    * ``double`` (64 bits)

* Tipos de datos primitivos de caracteres:
    * ``char`` (16 bits)
* Tipos de datos lógicos:
    * ``boolean`` (True / False)

* ``Swing`` es una biblioteca gráfica para Java. Incluye widgets para interfaz gráfica de usuario tales como cajas de
  texto, botones, listas desplegables y tablas.
* ``Junit`` es un conjunto de bibliotecas creadas por que son utilizadas en programación para hacer pruebas unitarias de
  aplicaciones Java.
* ``Apache Lucene`` es una API de código abierto para recuperación de información, originalmente implementada en Java.
  Es útil para cualquier aplicación que requiera indexado y búsqueda a texto completo. Lucene ha sido ampliamente usado
  por su utilidad en la implementación de motores de búsquedas.
* ``Jenkins`` es un servidor de automatización open source escrito en Java. Ayuda en la automatización de parte del
  proceso de desarrollo de software mediante integración continua y facilita ciertos aspectos de la entrega continua.
  Admite herramientas de control de versiones como CVS, Subversion, Git, Mercurial, Perforce y Clearcase y puede
  ejecutar proyectos basados en Apache Ant y Apache Maven, así como secuencias de comandos de consola y programas por
  lotes de Windows.

#### 2.4. SERVLETS Y JAVASERVER PAGES

* ``Java Servlet``:
    * Es una clase en el lenguaje de programación Java, utilizada para ampliar las capacidades de un servidor.
    * Aunque los servlets pueden responder a cualquier tipo de solicitudes, estos son utilizados comúnmente para
      extender las aplicaciones alojadas por servidores web, de tal manera que pueden ser vistos como applets de Java
      que se ejecutan en servidores en vez de navegadores web.
    * La palabra servlet deriva de otra anterior, applet, que se refiere a pequeños programas que se ejecutan en el
      contexto de un navegador web.
* ``JavaServer Pages`` (JSP):
    * Tecnología que ayuda a los desarrolladores de software a crear páginas web dinámicas basadas en HTML y XML, entre
      otros tipos de documentos.
    * JSP es similar a PHP, pero usa el lenguaje de programación Java. Para desplegar y correr JavaServer Pages, se
      requiere un servidor web compatible con contenedores servlet como Apache Tomcat o Jetty.
    * La principal ventaja de JSP frente a otros lenguajes es que el lenguaje Java es un lenguaje de propósito general
      que excede el mundo web y que es apto para crear clases que manejen lógica de negocio y acceso a datos de una
      manera prolija.
    * Esto permite separar en niveles las aplicaciones web, dejando la parte encargada de generar el documento HTML en
      el archivo JSP.
* Los servlets y Java Server Pages (JSPs) son dos métodos de creación de páginas web dinámicas en servidor usando el
  lenguaje Java. En ese sentido son similares a otros métodos o lenguajes tales como el PHP, ASP o los CGIs, programas
  que generan páginas web en el servidor. JSP puede ser visto como una abstracción de alto nivel de los servlets Java.
  Las JavaServer Pages son traducidas a servlets en tiempo real; cada servlet es guardado en caché y reutilizado hasta
  que la JSP original es modificada. Dicho en otras palabras las JSP son páginas java para un ambiente web.

#### 2.5. JDOM (Java Document Object Model)

* Especificación definida por el W3C muy similar a Java EE, genera un árbol jerárquico en memoria del documento o
  información en XML, esto permite que a través de un analizador (Xerces,...) sea manipulada la información:
    * Puede ser agregado o eliminado un nodo (Información) en cualquier punto del árbol.
    * Lo anterior se ejecuta sin incurrir en las penalidades o limitaciones de manipular un archivo de alguna otra
      manera.
    * Está enfocado a la edición o cambios en documentos XML.

> Xerces es un analizador (parser), colección de bibliotecas para el análisis sintáctico, validación, serialización y manipulación de documentos XML de Apache.

#### 2.6. SPRING FRAMEWORK

* Framework open source que facilita la creación de aplicaciones en Java, por lo que es más conocido es por la inyección
  de dependencias, Spring está dividido en diversos módulos:
    * ``Core container``: proporciona inyección de dependencias.
    * ``Web``: nos permite crear controladores web, tanto de vistas MVC como aplicaciones REST.
    * ``Acceso a datos``: abstraccioens sobre JDBC (Java DataBase Conectivity), ORM (Object-Relational Mapping), OXM (
      Object-XML Mappers), JSM (Java Message Service) y transacciones.
    * ``Programación Orientada a Aspectos`` (AOP): soporte para aspectos.
    * ``Instrumentación``: proporciona soporte para instrumentación de clases.
    * ``Pruebas de código``: contiene un framework de testing, con soporte para Junit y TestNG y todo lo necesario para
      probar los mecanismos. Si bien es cierto que Spring es muy potente, la configuración inicial y la preparación de
      las aplicaciones para producción son tareas bastante tediosas. Spring Boot simplifica el proceso al máximo gracias
      a sus dos principales mecanismos:
    * ``Contenedor de aplicaciones integrado``: Spring Boot permite compilar nuestras aplicaciones web como un archivo
      .jar que podemos ejecutar como una aplicación Java normal, esto lo consigue integrando el servidor de aplicaciones
      en el propio .jar y levantándolo cuando arrancamos la aplicación. De esta forma, podemos distribuir nuestras
      aplicaciones de una forma mucho más sencilla, al poder configurar el servidor junto con la aplicación.
    * ``Starters``: dependencias que podemos añadir a nuestro proyecto dependiendo de lo que necesitemos. Una vez
      añadimos un starter, éste nos proporciona todas las dependencias que necesitamos, tanto de Spring como de
      terceros. Además, los starters vienen configurados con valores por defecto, que pretenden minimizar la necesidad
      de configuración a la hora de desarrollar.

> ``Apache Tomcat`` funciona como un contenedor de servlets. Incluye el compilador Jasper, que compila JSPs convirtiéndolas en servlets. El motor de servlets de Tomcat a menudo se presenta en combinación con el servidor web Apache. Apache Hadoop: entorno de trabajo para software, bajo licencia libre, para programar aplicaciones distribuidas que manejen grandes volúmenes de datos. Permite a las aplicaciones trabajar con miles de nodos en red y petabytes de datos. Apache Avro es un marco de serialización de datos y llamadas de procedimiento remoto orientado a filas. Utiliza JSON para definir tipos de datos y protocolos, y serializa datos en un formato binario compacto. Su uso principal es en Apache Hadoop, donde puede proporcionar un formato de serialización para datos persistentes
> y un formato de cable para la comunicación entre los nodos de Hadoop y desde los programas cliente a los servicios de Hadoop.

### 3\. XML (eXtensible Markup Language)

* Metalenguaje que permite definir lenguajes de marcas desarrollado por W3C utilizado para almacenar datos en forma
  legible. Permite definir la gramática de lenguajes específicos para estructurar documentos grandes.
* El tratamiento del fichero XML comienza por la localización del mismo a lo largo del conjunto de documentos existentes
  en el mundo. Para llevar a cabo esta localización de forma unívoca, se utilizan los URI (Uniform Resource Identifiers)
  , de los cuales los URL (Uniform Resource Locators) son sin duda los más conocidos.
* A diferencia de otros lenguajes, XML da soporte a bases de datos, siendo útil cuando varias aplicaciones deben
  comunicarse entre sí o integrar información.

> ``XSLT`` (Extensible Stylesheet Language Transformations): estándar de la organización W3C que presenta una forma de transformar documentos XML en otros e incluso a formatos que no son XML. Xalan es una biblioteca de software de código abierto de Apache Software Foundation, que implementa el lenguaje de transformación XSLT 1.0 y el lenguaje XPath.

* ``XML`` es una tecnología sencilla que tiene a su alrededor otras que la complementan y la hacen mucho más grande, con
  unas posibilidades mucho mayores. Tiene un papel muy importante en la actualidad ya que permite la compatibilidad
  entre sistemas para compartir la información de una manera segura, fiable y fácil:
    * ``Apache Axis``: framework de código abierto, basado en XML para servicios web. Consiste en una implementación en
      Java y otra en C++ del servidor SOAP, así como diversos utilitarios y APIs para generar y desplegar aplicaciones
      de servicios web.
    * ``SAX`` (Simple API for XML): procesa (analiza) el documento o información en XML de una manera muy diferente a
      DOM, SAX procesa la información por eventos. A diferencia de DOM que genera un árbol jerárquico en memoria , SAX
      procesa la información en XML conforme esta sea presentada (evento por evento), efectivamente manipulando cada
      elemento a un determinado tiempo , sin incurrir en uso excesivo de memoria.

* Está enfocado a la lectura de documentos XML.
* Es un "parser (analizador)" ideal para manipular archivos de gran tamaño, ya que no ocupa generar un árbol en memoria
  como es requerido en DOM.
* Es más rápido y sencillo que utilizar DOM.
* La sencillez antes mencionada tiene su precio, debido a que SAX funciona por eventos.
* No es posible manipular información una vez procesada, en DOM no existe esta limitación ya que se genera el árbol
  jerárquico en memoria y es posible regresar a modificar nodos.
* ``OWL`` (Web Ontology Language): un lenguaje de marcado para publicar y compartir datos usando ontologías en la WWW.
  OWL tiene como objetivo facilitar un modelo de marcado construido sobre RDF y codificado en XML.

#### 3.1. WSDL (Services Description Language)

* Es un formato del Extensible Markup Language (XML) que se utiliza para describir servicios web, describe la forma de
  comunicación, es decir, en él, se declaran los servicios Web ofertados, los parámetros que requieren y devuelven, el
  tipo de conexión y los tipos utilizados. Las operaciones y mensajes que soporta se describen en abstracto y se ligan
  después al protocolo concreto de red y al formato del mensaje. La estructura del WSDL tiene los siguientes elementos:
    * ``Tipos de datos``: define los tipos de datos usados en los mensajes, se utilizan tipos definidos en la
      especificación de esquemas XML.
    * ``Mensajes``: se definen los elementos de mensaje. Cada mensaje puede consistir en una serie de partes lógica. Las
      partes pueden ser de cualquiera de los tipos definidos.
    * ``Tipos de puerto``: define las operaciones permitidas y los mensajes intercambiado en el servicio.
    * ``Bindings``: especifica protocolos de comunicación usados.
    * ``Servicios``: conjunto de puertos y dirección de los mismos.

* A la hora de definir un servicio Web, WSDL separa los que es la propia definición de aspectos dependientes de la red
  sobre la que se trabaje, de manera que se puedan reutilizar estas definiciones. En concreto cuando se habla de las
  operaciones que se quieren definir se está aludiendo al concepto de puerto WSDL. Un puerto WSDL no es más que un
  determinado conjunto de operaciones que se pueden realizar. Se pueden definir distintos tipos de puertos, dependiendo
  del tratamiento que hacen de los parámetros de entrada y de salida, estas operaciones son:
    * ``Puertos “one-way”`` (unidireccional): estos puertos reciben parámetros, pero no devuelven ningún dato.
    * ``Puertos “request-response”`` (petición-respuesta): el servicio recibe parámetros y devuelve datos.
    * ``Puertos “solicit-response”`` (solicitud-respuesta): el servicio envía una solicitud y recibe una respuesta.
    * ``Puertos “Notification”`` (notificación): el servicio puede enviar un mensaje, pero no espera por una respuesta.

> SAML (Security Assertion Markup Language): estándar abierto que define un esquema XML para el intercambio de datos de autenticación y autorización.

#### 3.2. JSON (JavaScript Object Notation)

* Formato de texto sencillo para el intercambio de datos.
* Se trata de un subconjunto de la notación literal de objetos de JavaScript, aunque, debido a su amplia adopción como
  alternativa a XML, se considera un formato independiente del lenguaje.
* Una de las ventajas de JSON sobre XML como formato de intercambio de datos es que resulta mucho más sencillo escribir
  un analizador sintáctico (parser) para él.
* En JavaScript, un texto JSON se puede analizar fácilmente usando la función eval(), algo que (debido a la ubicuidad de
  JavaScript en casi cualquier navegador web) ha sido fundamental para que haya sido aceptado por parte de la comunidad
  de desarrolladores AJAX.

> Jaql es un procesamiento de datos funcional y lenguaje de consulta más comúnmente utilizado para el procesamiento de consultas JSON en Big Data.

### 4\. UML (Unified Modeling Language)

* Lenguaje de modelado de sistemas de software para especificar o para describir métodos o procesos, es un lenguaje
  gráfico para visualizar, especificar, construir y documentar un sistema.
* ``UML`` ofrece un estándar para describir un "plano" del sistema (modelo), incluyendo aspectos conceptuales tales como
  procesos, funciones del sistema, y aspectos concretos como expresiones de lenguajes de programación, esquemas de bases
  de datos y compuestos reciclados. Tipos de diagrama en UML:
    * ``Diagramas Estructurales``: muestran la estructura estática del sistema y sus partes en diferentes niveles de
      abstracción, son:

        * ``De clases``: es el bloque de construcción principal de cualquier solución orientada a objectos, muestra las
          clases de un sistema, atributos y operaciones de cada clase y la relación entre cada clase.
        * ``De componentes``: muestra la relación estructural de los componentes de un sistema de software.
        * ``De despliegue``: muestra el hardware de su sistema y el software de ese hardware, incluyendo nodos y
          conexiones.
        * ``De objetos``: muy similares a los diagramas de clases. Al igual que los diagramas de clases, también
          muestran la relación entre los objetos, pero usan ejemplos del mundo real. Se utilizan para mostrar cómo se
          verá un sistema en un momento dado.
        * ``De paquetes``: representa las dependencias entre los paquetes que componen un modelo, es decir, muestra cómo
          un sistema está dividido en agrupaciones lógicas y las dependencias entre esas agrupaciones.
        * ``De perfiles``.

    * ``Diagramas de Comportamiento``: Muestran el comportamiento dinámico de los objetos en el sistema, son:

        * ``De casos de uso``: ofrecen una visión general de los actores involucrados en un sistema, las diferentes
          funciones que necesitan esos actores y cómo interactúan estas diferentes funciones.
        * ``De actividades``: representan los flujos de trabajo de forma gráfica.
        * ``De transición de estados``: similares a los diagramas de actividad, describir el comportamiento de los
          objetos que actúan de manera diferente de acuerdo con el estado en que se encuentran en el momento.
        * ``De interacción``: modelos que describen como grupos de objetos colaboran para conseguir algún fin.
            * ``De tiempos``.
        * ``De secuencia``.
        * ``De comunicación``.
        * ``Diagrama Global de interacciones``.

#### 4.1. MECANISMOS COMUNES DE UML

* La construcción de los bloques del UML resulta más sencilla y más armoniosa, si se realiza de acuerdo a un patrón de
  características comunes.
    * ``Especificaciones``: detrás de cada parte de la notación gráfica del UML hay una especificación que proporciona
      una declaración textual de la sintaxis y semánticas de dicho bloque de construcción.
    * ``Adornos``: la mayoría de los elementos en el UML tienen una notación gráfica y directa que proporciona una
      representación visual de los aspectos más importantes del elemento.
    * ``Divisiones comunes``: a la hora de modelar sistemas orientados a objetos, el mundo aparece dividido como mínimo
      en un par de formas. Por ejemplo, está la división de clase y de objeto. Una clase es una abstracción, mientras
      que un objeto es una manifestación concreta de dicha abstracción en el UML
    * ``Mecanismos de extensión``: UML proporciona un lenguaje estándar para escribir modelos de software, pero no es
      posible para un lenguaje cerrado expresar todos los detalles de todos los modelos en todos los dominios a lo largo
      de todo el tiempo. Los mecanismos de extensión del UML incluyen:
        * ``Estereotipos``: extiende el vocabulario del UML, permitiendo que podamos crear nuevos tipos de bloques de
          construcción que son derivados a partir de los ya existentes y que son específicos a nuestro problema.
        * ``Valores añadidos``: extiende las propiedades de un bloque de construcción del UML, permitiendo que podamos
          crear nueva información en la especificación de dicho elemento.
        * ``Restricciones``: extiende las semánticas de un bloque de construcción del UML, permitiendo que podamos
          añadir nuevas reglas o modificar las ya existentes.

### 5\. .NET

#### 5.1. ADO.NET

* Conjunto de componentes del software que pueden ser usados por los programadores para acceder a datos y a servicios de
  datos. Es parte de la biblioteca de clases base que están incluidas en el Microsoft .NET Framework.
* Es comúnmente usado por los programadores para acceder y para modificar los datos almacenados en un Sistema Gestor de
  Bases de Datos Relacionales, aunque también puede ser usado para acceder a datos en fuentes no relacionales, consiste
  en dos partes primarias:
    * ``Data provider``: clases que proporcionan el acceso a una fuente de datos, como Microsoft SQL Server (puerto
      1433\) y Oracle (puerto 1521). Cada fuente de datos tiene su propio conjunto de objetos del proveedor, pero cada
      uno tienen un conjunto común de clases de utilidad:
        * ``Connection``: proporciona una conexión usada para comunicarse con la fuente de datos.
        * ``Command``: usado para realizar alguna acción en la fuente de datos, como lectura, actualización o borrado de
          datos relacionales.
        * ``Parameter``: describe un simple parámetro para un command.
        * ``DataAdapter``: "puente" utilizado para transferir data entre una fuente de datos y un objeto DataSet.
        * ``DataReader``: es una clase usada para procesar eficientemente una lista grande de resultados, un registro a
          la vez.

    * ``DataSets``: grupo de clases que describen una simple base de datos relacional en memoria y representa un
      esquema (o una base de datos entera o un subconjunto de una), contiene las tablas y las relaciones entre esas
      tablas.

        * DataTable representa una sola tabla en la base de datos. Tiene un nombre, filas, y columnas.
        * DataView "se sienta sobre" un DataTable y ordena los datos, todas las DataTables tienen un filtro por defecto,
          mientras que pueden ser definidos cualquier número de DataViews adicionales, reduciendo la interacción con la
          base de datos subyacente y mejorando así el desempeño.

> ``NUnit`` es un framework open source de Pruebas de unidad para Microsoft .NET y Mono.
> Sirve al mismo propósito que JUnit realiza en el mundo Java, y es uno de muchos en la familia xUnit.

#### 5.2. ASP.NET

* Entorno para aplicaciones web desarrollado y comercializado por Microsoft.
* Es usado por programadores y diseñadores para construir sitios web dinámicos, aplicaciones web y servicios web XML.
* Funciona sobre el servidor de Microsoft IIS, y sobre Apache.
* Las páginas de ASP.NET, conocidas oficialmente como "web forms" (formularios web), son el principal medio de
  construcción para el desarrollo de aplicaciones web.
* Los formularios web están contenidos en archivos con una extensión ASPX; estos archivos típicamente contienen
  etiquetas HTML o XHTML estático, y también etiquetas definiendo Controles Web que se procesan del lado del servidor y
  Controles de Usuario donde los desarrolladores colocan todo el código estático y dinámico requerido por la página web.
* Las aplicaciones ASP.NET son alojadas en un servidor web y se tiene acceso a ellas mediante el protocolo sin estado
  HTTP, que no guarda ninguna información sobre conexiones anteriores.
* Por lo tanto, si la aplicación requiere interacción entre conexiones, tiene que implementar su propia administración
  del estado. ASP.NET proporciona varias maneras de administrar el estado de las aplicaciones ASP.NET:
    * ``Estado de la aplicación``: el estado de la aplicación (Application state) es una colección de variables
      definidas por el usuario que son compartidas por todas las invocaciones de una aplicación ASP.NET.
    * ``Estado de la sesión``: colección de variables definidas por el usuario, las cuales persisten durante la sesión
      de un usuario. Estas variables son únicas para diferentes instancias de una sesión de usuario, Las variables de
      sesión pueden ser preparadas para ser automáticamente destruidas después de un determinado tiempo de inactividad,
      incluso si la sesión no ha terminado. Del lado del cliente, una sesión de usuario es identificada por una cookie o
      codificando el ID de la sesión en la misma URL. ASP.NET proporciona tres modos de  
      persistencia para variables de sesión:
    * ``InProc``: Las variables de sesión son mantenidas dentro del proceso. Sin embargo, en este modo, las variables
      son destruidas cuando el proceso ASP.NET es reciclado o terminado.
    * ``StateServer``: En este modo, ASP.NET ejecuta un servicio de Windows separado que mantiene las variables de
      estado. Como esta administración de estado ocurre fuera del proceso ASP.NET, tiene un impacto negativo en el
      rendimiento, pero permite a múltiples instancias de ASP.NET compartir el mismo estado del servidor, permitiendo
      que una aplicación ASP.NET pueda tener su carga balanceada y escalada en múltiples servidores
    * ``SqlServer``: en este modo, las variables de estado son almacenadas en un servidor de base de datos, accesible
      usando SQL. Las variables de sesión pueden persistir a través de finalizaciones de procesos también en este modo.

> ``DevExpress`` es una suite de componente de interfaz de usuario en plataformas .NET, incluye distintos componentes tales como tablas, calendarios, editor de HTML, Hojas de cálculo, editores de datos o gráficas.

### 6\. HTML (HyperText Markup Language)

* Lenguaje de marcado para la elaboración de páginas web.
* Es un estándar que sirve de referencia del software que conecta con la elaboración de páginas web en sus diferentes
  versiones, define una estructura básica y un código (denominado código HTML) para la definición de contenido de una
  página web.
* La página web contiene solamente texto mientras que recae en el navegador web (interpretador del código) la tarea de
  unir todos los elementos y visualizar la página final.
* HTML se escribe en forma de «etiquetas», rodeadas por corchetes angulares (\<,\>,/).
* El HTML también puede incluir scripts. HTML también sirve para referirse al contenido del tipo de MIME text/html o
  todavía más ampliamente como un término genérico para el HTML, ya sea en forma descendida del XML (como XHTML 1.0 y
  posteriores) o en forma descendida directamente de SGML (como HTML 4.01 y anteriores).
    * ``Etiquetas``:

        * ``\<a\>``: define los enlaces.
        * ``\<body\>``: es el cuerpo de la página, donde va lo que se ve en el navegador al cargar una web. En el body
          van los textos, las imágenes y todos los contenidos de la web.
        * ``\<\!DOCTYPE\>``: define el tipo de documento.
        * ``\<html\>``: indica el comienzo del documento HTML.
        * ``\<head\>``: indica que empieza la cabecera de la página. En ella se suele poner el título (\<title\>) de la
          web, una descripción y otras informaciones relacionadas con el contenido de la página.
        * ``\<h1\>``, ``\<h2\>``, etc.: son los títulos o encabezados. Se utilizan para establecer determinados textos
          de la página como titulares, suelen tener un tamaño de fuente mayor para diferenciarlos del resto del texto.
          Son importantes en el posicionamiento en buscadores.
        * ``\<table\>``: es una tabla, y dentro de esta tenemos filas \<tr\> y celdas \<td\>.
        * ``\<p\>``: el texto dentro de esta etiqueta forma un párrafo.
        * ``\<img\>``: imágenes.
        * ``\<ul\>``: los textos dentro de esta etiqueta se estructuran en listas. Mediante el uso de ``\<li\>``
          definimos cada guión dentro de la lista, y usando ``\<ol\>`` en lugar de ``\<ul\>`` tendremos listas
          ordenadas.
        * ``\<b\>`` y ``\<strong\>``: texto en negrita (bold).
        * ``\<u\>``: texto subrayado.
        * ``\<i\>`` y ``\<em\>``: texto en cursiva (italic).

    * ``Etiquetas introducidas en HTML5``:

        * ``\<article\>``: representa un artículo de revista, documento…
        * ``\<aside\>``: contenidos aparte de la página principal.
        * ``\<audio\>``: contenido embebido en la web.
        * ``\<canvas\>``: dibujar graficas via scripts (javascript).
        * ``\<datalist\>``: lista de opciones.
        * ``\<details\>``: contenidos adicionales que el usuario puede elegir si esconder o mostrar.
        * ``\<dialog\>``: ventana de dialogo.
        * ``\<embed\>``: define un contenedor para una aplicación externa.
        * ``\<figure\>``: representa contenido independiente (imagen, diagrama o fragmento de código al que se hace
          referencia en el texto principal, pero que se puede mover a otra sin que afecte al flujo principal.)
        * ``\<footer\>``: pie de pagina para el contenido de sección más cercano.
        * ``\<header\>``: grupo de ayudas introductorias o de navegación.
        * ``\<mark\>``: texto marcado o resaltado (highlight) como referencia o anotación.
        * ``\<nav\>``: proporcionar enlaces de navegación.
        * ``\<output\>``: realiza una cuenta y muestra el resultado.
        * ``\<ruby\>``: texto adicional que indica la pronunciación de algún carácter.
        * ``\<section\>``: representa una sección genérica de un documento. Sirve para determinar qué contenido
          corresponde a qué parte de un esquema y estructurar semánticamente un documento a la hora de ser representado
          por parte de un agente usuario.
        * ``\<source\>``: especifica recursos de medios múltiples para los elementos picture, audio, o video.
        * ``\<time\>``: periodo específico en el tiempo.
        * ``\<video\>``: incrustar vídeos.

> WebM: es un formato multimedia abierto y libre desarrollado por Google y orientado para usarsecon HTML5. Es un proyecto de software libre pensado para ser utilizado con códec de vídeo VP8 y el códec de audio Vorbis dentro de un contenedor multimedia Matroska.

#### 6.1. XHTML (eXtensible HyperText Markup Language)

* ``HTML`` expresado como XML válido donde la información, y la forma de presentarla estén claramente separadas. Las
  principales ``ventajas del XHTML`` ``sobre el HTML`` son:

    * La incorporación de elementos de distintos espacios de nombres XML (como MathML y Scalable Vector Graphics).
    * Un navegador no necesita implementar heurísticas para detectar qué quiso poner el autor, por lo que el parser
      puede ser mucho más sencillo.
    * Como es XML se pueden utilizar fácilmente herramientas creadas para procesamiento de documentos XML genéricos (
      editores, XSLT, etc.).

* ``Reglas básicas``:

    * Los elementos vacíos o no vacíos deben cerrarse siempre.
    * Los elementos anidados deben tener un correcto orden de apertura/cierre (el que se abre último, debe cerrarse
      primero).
    * Los valores de los atributos deben siempre ir encerrados entre comillas.
    * Los nombres de elementos y atributos deben ir en minúsculas.
    * No está permitida la minimización de atributos (se usa el nombre del atributo como valor).
    * El texto no debe ser insertado directamente en el cuerpo (dentro de la etiqueta body).
    * No se deben insertar elementos de bloque dentro de elementos de línea.

### 7\. CSS (Cascading Style Sheets)

* Lenguaje de diseño gráfico para definir y crear la presentación de un documento estructurado escrito en un lenguaje de
  marcado. Es muy usado para establecer el diseño visual de los documentos web, e interfaces de usuario escritas
  en ``HTML`` o
  ``XHTML``. Una hoja de estilos consiste en una serie de reglas. Cada regla, o conjunto de reglas consisten en uno o
  más selectores, y un bloque de declaración.
    * ``Selectores``: declaran qué etiquetas se les aplican a los estilos que coincidan con la etiqueta o atributo
      señalados en la regla. Los selectores pueden aplicarse a:
        * Todos los elementos de un tipo, como los párrafos \<p\>.
        * Elementos seguidos de un atributo, en particular:
            * ``id(\#)``: identificador, un identificador único para la etiqueta.
            * ``class(.)``: clase, un identificador para anotar múltiples elementos.

    * ``Herencia``: mecanismo por el cual las propiedades no solo se aplican a un solo elemento, sino también a sus
      descendientes. Se basa en el anidamiento. Los elementos descendientes pueden heredar los valores de las
      propiedades CSS de un elemento ancestro. Las propiedades que pueden ser heredadas son el color, fuente, espaciado,
      el peso de la línea, propiedades de lista, alineación del texto, visibilidad, espaciado de espacios and y
      espaciado entre palabras.
    * ``Preprocesador CSS``: podemos extender las funcionalidades de CSS, mediante un lenguaje de script escribimos
      código parecido al que usamos en CSS (esto dependerá del preprocesador que estemos usando), luego este código será
      compilado y como resultado de esta compilación tendremos un archivo CSS. Estos son algunos de los preprocesadores
      CSS más populares:
      SASS, LESS, Stylus y PostCSS.

> ``Flexbox`` es un modelo de diseño CSS3 que permite que los elementos adaptables dentro de un contenedor se organicen automáticamente dependiendo del tamaño de la pantalla o del dispositivo.

### 8\. PHP (Hypertext Preprocessor)

* Es un lenguaje de programación de uso general que se adapta especialmente al desarrollo web, suele ser procesado en un
  servidor web por un intérprete PHP implementado como un módulo, un daemon o como un ejecutable.
* El intérprete de PHP solo ejecuta el código que se encuentra entre sus delimitadores.
* Los delimitadores más comunes son ``“\<?php”`` para abrir una sección PHP y ``“?\>”`` para cerrarla.
* Las variables se prefijan con el símbolo del dólar ``($)`` y no es necesario indicar su tipo.
* Las variables, a diferencia de las funciones, distinguen entre mayúsculas y minúsculas.
* En cuanto a las palabras clave, PHP comparte con la mayoría de otros lenguajes con sintaxis ``C`` las condiciones
  con ``if``, los bucles con ``for`` y ``while`` y los retornos de funciones.
* Como es habitual en este tipo de lenguajes, las sentencias deben acabar con punto y coma ``(;)``.
* Características:
    * Orientado al desarrollo de aplicaciones web dinámicas con acceso a información almacenada en una base de datos.
    * El código fuente escrito en PHP es invisible al navegador web y al cliente, ya que es el servidor el que se
      encarga de ejecutar el código y enviar su resultado HTML al navegador.
    * Capacidad de conexión con la mayoría de los motores de base de datos que se utilizan en la actualidad, destaca su
      conectividad con ``MySQL`` y ``PostgreSQL``.
    * Permite aplicar técnicas de programación orientada a objetos.
    * No requiere definición de tipos de variables aunque sus variables se pueden evaluar también por el tipo que estén
      manejando en tiempo de ejecución.

### 9\. REST vs SOAP

* ``REST`` (Representational State Transfer):
    * Es una interfaz para conectar varios sistemas basados en el protocolo ``HTTP``, sirve para obtener y generar datos
      y operaciones, devolviendo esos datos en formatos muy específicos, como ``XML`` y ``JSON``. ``REST`` se apoya en
      HTTP, los verbos que utiliza son exactamente los mismos, con ellos se puede hacer ``GET``, ``POST``, ``PUT``
      y ``DELETE``.
    * Crea una petición ``HTTP`` que contiene toda la información necesaria, es decir, un ``REQUEST`` a un servidor
      tiene toda la información necesaria y solo espera una ``RESPONSE``, ósea una respuesta en concreto. Hace mucho más
      fácil el desarrollo de una ``API REST``, en este caso de un servicio en el cual nosotros vamos a almacenar nuestra
      lógica de negocio y vamos a servir los datos con una serie de recursos URL y una serie de datos que nosotros los
      limitaremos, es decir, será nuestro ``BACKEND`` nuestra lógica pura de negocios que nosotros vamos a utilizar.
    * Todos los objetos se manipulan mediante ``URI``(Universal Resource Identifier).

* ``SOAP`` (Simple Object Access Protocol):
    * Protocolo estándar que define cómo dos objetos en diferentes procesos pueden comunicarse por medio de intercambio
      de datos ``XML``, es un paradigma de mensajería de una dirección sin estado, que puede ser utilizado para formar
      protocolos más completos y complejos según las necesidades de las aplicaciones que lo implementan.
    * Puede formar y construir la capa base de una "pila de protocolos de web service", ofreciendo un framework de
      mensajería básica en el cual los “web services” se pueden construir.
    * ``SOAP`` tiene tres características principales:
        * ``Extensibilidad``: seguridad y ``WS-routing`` son extensiones aplicadas en el desarrollo.
        * ``Neutralidad``: bajo TCP puede ser utilizado sobre cualquier protocolo de aplicación como ``HTTP``, ``SMTP``
          , ``JMS…``
        * ``Independencia``: permite cualquier modelo de programación.

    * Un mensaje ``SOAP`` es un documento ``XML`` ordinario con una estructura definida en la especificación del
      protocolo. Dicha estructura la conforman las siguientes partes:
        * ``Envelope``: parte que identifica al mensaje ``SOAP`` como tal.
        * ``Header``: permite enviar información relativa a cómo debe ser procesado el mensaje. Es una herramienta para
          que los mensajes puedan ser enviados de la forma más conveniente para las aplicaciones.
        * ``Body``: información relativa a la llamada y la respuesta.
        * ``Fault``: información relativa a errores que se hayan producido durante el procesado del mensaje y el envío.

> ``Apache Flume`` es un servicio distribuido, fiable, y altamente disponible para recopilar, agregar, y mover eficientemente grandes cantidades de datos.

### 10 SOFTWARE ESPECÍFICO

* ``SonarQube``:
    * Plataforma para evaluar código fuente de software libre, cuenta con herramientas de análisis estático de código
      fuente (``Checkstyle``, ``PDM``, ``FindBugs``), para obtener métricas que pueden ayudar a mejorar la calidad del
      código de un programa.
    * ``Funciones``:
        * Informa sobre código duplicado, estándares de codificación, pruebas unitarias, errores potenciales, diseño de
          software...
        * Está pensado para ``Java`` pero acepta otros lenguajes mediante extensiones.
        * Se integra con ``Maven``, ``Ant`` y herramientas de integración continua (``Atlassian Bamboo``
          , ``Jenkinsy Hudson``).

* ``Mercurial``:
    * Sistema de control de versiones multiplataforma, para desarrolladores de software.
    * Está implementado principalmente haciendo uso del lenguaje de programación Python.
    * Ha sido adaptado para ``Windows``, ``Mac OS X`` y la mayoría de otros sistemas tipo ``Unix``.
    * Las principales metas de desarrollo de ``Mercurial`` incluyen un gran rendimiento y escalabilidad;
    * Desarrollo completamente distribuido, sin necesidad de un servidor;
    * Gestión robusta de archivos tanto de texto como binarios; y capacidades avanzadas de ramificación e integración,
      todo ello manteniendo sencillez conceptual.
    * Incluye una interfaz web integrada.

* ``Apache Subversion`` (SVN):
    * Herramienta de control de versiones open source basada en un repositorio cuyo funcionamiento se asemeja
      enormemente al de un sistema de ficheros.
    * Utiliza el concepto de revisión para guardar los cambios producidos en el repositorio.
    * Entre dos revisiones solo guarda el conjunto de modificaciones (delta), optimizando así al máximo el uso de
      espacio en disco.
    * SVN permite al usuario crear, copiar y borrar carpetas con la misma flexibilidad con la que lo haría si estuviese
      en su disco duro local.
    * Dada su flexibilidad, es necesaria la aplicación de buenas prácticas para llevar a cabo una correcta gestión de
      las versiones del software generado.
    * Subversion puede acceder al repositorio a través de redes, lo que le permite ser usado por personas que se
      encuentran en distintas computadoras.

* ``Drupal``:
    * Sistema de gestión de contenidos o CMS libre, modular, multipropósito y muy configurable que permite publicar
      artículos, imágenes, archivos...

> ``Bamboo``: es un servidor de automatización par la gestión de integración continua de software, con entrega desde el código hasta el despliegue.

> ``Atom``: es un editor de código fuente de código abierto para macOS, Linux, y Windows con soporte para múltiples plug-in escritos en Node.js y control de versiones Git integrado.

### 11\. MODELO VISTA CONTROLADOR

* Patrón de arquitectura de software, que separa los datos y la lógica de negocio de una aplicación, de la interfaz de
  usuario y del módulo encargado de gestionar los eventos y las comunicaciones.
* Se basa en las ideas de reutilización de código y la separación de conceptos, características que buscan facilitar la
  tarea de desarrollo de aplicaciones y su posterior mantenimiento.
* Existen frameworks como ``JavaScriptMVC``, ``Backbone`` o ``jQuery14`` que permiten que ciertos componentes
  ``MVC`` se ejecuten parcial o totalmente en el cliente (``AJAX``).
    * ``Modelo``: representación de la información con la cual el sistema opera, por lo tanto gestiona todos los accesos
      a dicha información, tanto consultas como actualizaciones, implementando también los privilegios de acceso que se
      hayan descrito en las especificaciones de la aplicación (lógica de negocio). Envía a la 'vista' aquella parte de
      la información que en cada momento se le solicita para que sea mostrada (típicamente a un usuario). Las peticiones
      de acceso o manipulación de información llegan al 'modelo' a través del 'controlador'.
    * ``Controlador``: Responde a eventos (usualmente acciones del usuario) e invoca peticiones al 'modelo' cuando se
      hace alguna solicitud sobre la información (por ejemplo, editar un documento o un registro en una base de datos).
      También puede enviar comandos a su 'vista' asociada si se solicita un cambio en la forma en que se presenta el '
      modelo' (por ejemplo, desplazamiento o scroll por un documento o por los diferentes registros de una base de
      datos), por tanto se podría decir que el 'controlador' hace de intermediario entre la 'vista' y el 'modelo'.
    * ``Vista``: Presenta el 'modelo' (información y lógica de negocio) en un formato adecuado para interactuar (
      usualmente la interfaz de usuario), por tanto requiere de dicho 'modelo' la información que debe representar como
      salida.

> ``Magnolia CMS``: sistema de Gestión de Contenidos que persigue la facilidad de uso y la disponibilidad, licencia Open Source (Código Abierto). La página de edición de la interfaz permite a los editores diseñar el contenido exactamente como aparecería para un visitante del sitio web. Bajo el capó, Magnolia contiene tecnología Java basada en estándares abiertos para permitir soluciones a la medida. Soporte empresarial y otros servicios están disponibles en todo el mundo por parte del vendedor y de los partners.

### 12\. MÉTRICA V3  
#### 12.1 PRUEBAS  
* ``Unitarias``: Verificar componentes de forma individual.  
* ``Integración``: Comprobar el funcionamiento de componentes entre ellos.  
* ``Del sistema``: Comprobar la integración del sistema, funcionamiento con interfaces y distintos subsistemas.  
* ``Implantación``: Aceptación del sistema, funcionamiento con interfaces y distintos subsistemas.  
* ``Aceptación``: Cumple con las expectativas del usuario para el funcionamiento esperado y, con el catálogo de
requisitos.  
* ``Regresión``: Eliminar el efecto onda, para que los cambios por peticiones no provoquen errores.  
* ``Rendimiento``: Comprobación de los tiempos de respuesta.

#### 12.2 PARTICIPANTES  
* ``Directivo``: Organización, objetivos y negocio. Interviene en todos los procesos, provee de recursos necesarios,
composición: Comité de dirección, de seguimiento, directores de usuarios y usuarios expertos.  
* ``Jefe de proyecto``: Responsable de la implantación, mantenimiento, operación, sistemas, seguridad o calidad.
Coordinación y dirección de equipos: Estimación del esfuerzo.  
* ``Consultor``: Consultores, especialistas y técnicos. Asesoramiento. Altos niveles de especialización y uso de nuevas
tecnologías.  
* ``Analista``: Elabora el catálogo de requisitos, equipos de: bases de datos, arquitectura, formación, implantación,
operación, seguridad, soporte técnico, equipo de proyecto y calidad.  
* ``Programador``: Construcción y mantenimiento del código, además de realizar pruebas unitarias y conjuntas.