# Modelo–vista–controlador  
* Modelo-vista-controlador (MVC) es un patrón de arquitectura de software, que separa los datos y principalmente lo que es la lógica de negocio de una aplicación de su representación y el módulo encargado de gestionar los eventos y las comunicaciones. Para ello MVC propone la construcción de tres componentes distintos que son el modelo, la vista y el controlador; es decir: por un lado define componentes para la representación de la información y, por otro lado, para la interacción del usuario.1 2 Este patrón de arquitectura de software se basa en las ideas de reutilización de código y la separación de conceptos, características que buscan facilitar la tarea de desarrollo de aplicaciones y su posterior mantenimiento
## Historia
* El patrón MVC fue una de las primeras ideas en el campo de las interfaces gráficas de usuario y uno de los primeros trabajos en describir e implementar aplicaciones software en términos de sus diferentes funciones.5  

* MVC fue introducido por Trygve Reenskaug (web personal (http://heim.ifi.uio.no/\~trygver)) en Smalltalk-76 durante su visita a Xerox Parc6 7 en los años 70, seguidamente, en los años 80, Jim Althoff y otros implementaron una versión de MVC para la biblioteca de clases de Smalltalk-80.8 Solo más tarde, en 1988, MVC se expresó como un concepto general en un artículo9 sobre Smalltalk-80.  

*En esta primera definición de MVC el controlador se definía como «el módulo que se ocupa de la entrada» (de forma similar a como la vista «se ocupa de la salida»). Esta definición no tiene cabida en las aplicaciones modernas en las que esta funcionalidad es asumida por una combinación de la 'vista' y algún framework moderno para desarrollo. El 'controlador', en las aplicaciones modernas de la década de 2000, es un módulo o una sección intermedia de código, que hace de intermediario de la comunicación entre el 'modelo' y la 'vista', y unifica la validación (utilizando llamadas directas o el «observer» para desacoplar el 'modelo' de la 'vista' en el 'modelo' activo10 ).  

* Algunos aspectos del patrón MVC han evolucionado dando lugar a ciertas variantes del concepto original, ya que «las partes del MVC clásico realmente no tienen sentido para los clientes actuales»:11  
  * HMVC (MVC Jerárquico)  
  * MVA (Modelo-Vista-Adaptador)  
  * MVP (Modelo-Vista-Presentador)  
  * MVVM (Modelo-Vista Vista-Modelo)
  * ... y otros que han adaptado MVC a diferentes contextos.  

## Descripción del patrón
* De manera genérica, los componentes de MVC se podrían definir como sigue:  
  * El Modelo: Es la representación de la información con la cual el sistema opera, por lo tanto gestiona todos los accesos a dicha información, tanto consultas como actualizaciones, implementando también los privilegios de acceso que se hayan descrito en las especificaciones de la aplicación (lógica de negocio). Envía a la 'vista' aquella parte de la información que en cada momento se le solicita para que sea mostrada (típicamente a un usuario). Las peticiones de acceso o manipulación de información llegan al 'modelo' a través del 'controlador'.12  
  * El Controlador: Responde a eventos (usualmente acciones del usuario) e invoca peticiones al 'modelo' cuando se hace alguna solicitud sobre la información (por ejemplo, editar un documento o un registro en una base de datos). También puede enviar comandos a su 'vista' asociada si se solicita un cambio en la forma en que se presenta el 'modelo' (por ejemplo, desplazamiento o scroll por un documento o por los diferentes registros de una base de datos), por tanto se podría decir que el 'controlador' hace de intermediario entre la 'vista' y el 'modelo' (véase Middleware).  
  * La Vista: Presenta el 'modelo' (información y lógica de negocio) en un formato adecuado para interactuar (usualmente la interfaz de usuario), por tanto requiere de dicho 'modelo' la información que debe representar como salida.  

## Interacción de los componentes
* Aunque se pueden encontrar diferentes implementaciones de MVC, el flujo de control que se sigue generalmente es el siguiente:  
  * 1\. **El usuario** interactúa con la interfaz de usuario de alguna forma (por ejemplo, el usuario pulsa un botón, enlace, etc.)  
  * 2\. **El controlador** recibe (por parte de los objetos de la interfaz-vista) la notificación de la acción solicitada por el usuario. El controlador gestiona el evento que llega, frecuentemente a través de un gestor de eventos (handler) o callback.  
  * 3\. **El controlador** accede al modelo, actualizándolo, posiblemente modificándolo de forma adecuada a la acción solicitada por el usuario (por ejemplo, el controlador actualiza el carro de la compra del usuario). Los controladores complejos están a menudo estructurados usando un patrón de comando que encapsula las acciones y simplifica su extensión.  
  * 4\. **El controlador** delega a los objetos de la vista la tarea de desplegar la interfaz de usuario. La vista obtiene sus datos del modelo para generar la interfaz apropiada para el usuario donde se reflejan los cambios en el modelo (por ejemplo, produce un listado del contenido del carro de la compra). El modelo no debe tener conocimiento directo sobre la vista. Sin embargo, se podría utilizar el patrón Observador para proveer cierta indirección entre el modelo y la vista, permitiendo al modelo notificar a los interesados de cualquier cambio. Un objeto vista puede registrarse con el modelo y esperar a los cambios, pero aun así el modelo en sí mismo sigue sin saber nada de la vista. Este uso del patrón Observador no es posible en las aplicaciones Web puesto que las clases de la vista están desconectadas del modelo y del controlador. En general el controlador no pasa objetos de dominio (el modelo) a la vista aunque puede dar la orden a la vista para que se actualice. Nota: En algunas implementaciones la vista no tiene acceso directo al modelo, dejando que el controlador envíe los datos del modelo a la vista. Por ejemplo en el MVC usado por Apple en su framework Cocoa. Suele citarse como Modelo-Interface-Control, una variación del MVC más puro  
  * 5\. **La interfaz** de usuario espera nuevas interacciones del usuario, comenzando el ciclo nuevamente...  

## MVC y bases de datos
* Muchos sistemas \[informáticos\] utilizan un sistema de gestión de base de datos el cual gestiona los datos que debe utilizar la aplicación; en líneas generales del MVC dicha gestión corresponde al modelo. La unión entre capa de presentación y capa de negocio conocido en el paradigma de la Programación por capas representaría la integración entre la Vista y su correspondiente Controlador de eventos y acceso a datos, MVC no pretende discriminar entre capa de negocio y capa de presentación pero sí pretende separar la capa visual gráfica de su correspondiente programación y acceso a datos, algo que mejora el desarrollo y mantenimiento de la Vista y el Controlador en paralelo, ya que ambos cumplen ciclos de vida muy distintos entre sí.  

## Uso en aplicaciones Web
* Aunque originalmente MVC fue desarrollado para aplicaciones de escritorio, ha sido ampliamente adaptado como arquitectura para diseñar e implementar aplicaciones web en los principales lenguajes de programación. Se han desarrollado multitud de frameworks, comerciales y no comerciales, que implementan este patrón (ver apartado siguiente "Frameworks MVC"); estos frameworks se diferencian básicamente en la interpretación de como las funciones MVC se dividen entre cliente y servidor.  
* Los primeros frameworks MVC para desarrollo web planteaban un enfoque de cliente ligero en el que casi todas las funciones, tanto de la vista, el modelo y el controlador recaían en el servidor. En este enfoque, el cliente manda la petición de cualquier hiperenlace o formulario al controlador y después recibe de la vista una página completa y actualizada (u otro documento); tanto el modelo como el controlador (y buena parte de la vista) están completamente alojados en el servidor. Como las tecnologías web han madurado, ahora existen frameworks como JavaScriptMVC, Backbone o jQuery14 que permiten que ciertos componentes MVC se ejecuten parcial o totalmente en el cliente (véase AJAX).

## Frameworks MVC

| Lenguaje               | Licencia                                | Nombre                                                 |
|------------------------|-----------------------------------------|--------------------------------------------------------|
| .NET                   | Castle Project                          | MonoRail                                               |
| .NET                   | Apache                                  | Spring.NET                                             |
| .NET                   | Apache                                  | Maverick.NET                                           |
| .NET                   | MS-PL                                   | ASP.NET MVC                                            |
| .NET                   | Microsoft Patterns & Practices          | User Interface Process (UIP) Application Block         |
| C++                    | BSD license                             | treefrog                                               |
| Delphi/ Object Pascal   | Apache                                  | Delphi MVC Framework                                   |
| Delphi/ Object Pascal   | Apache                                  | mORMot Framework                                       |
| Objective C            | Apple                                   | Cocoa                                                  |
| Ruby                   | MIT                                     | Ruby on Rails                                          |
| Ruby                   | MIT                                     | Merb                                                   |
| Ruby                   | MIT                                     | Ramaze                                                 |
| Ruby                   | MIT                                     | Rhodes                                                 |
| Java                   | Apache                                  | Grails                                                 |
| Java                   | GPL                                     | Interface Java Objects                                 |
| Java                   | LGPL                                    | Framework Dinámica                                     |
| Java                   | Apache                                  | Struts                                                 |
| Java                   | Apache                                  | Brutos framework                                       |
| Java                   | Apache                                  | Beehive                                                |
| Java                   | Apache                                  | Spring                                                 |
| Java                   | Apache                                  | Tapestry                                               |
| Java                   | Apache                                  | Aurora                                                 |
| Java                   | Apache                                  | JavaServerFaces                                        |
| Java                   | Apache                                  | PrimeFaces                                             |
| Java                   | Apache                                  | Vaadin                                                 |
| JavaScript             | GPLv3                                   | Sails.JS                                               |
| JavaScript             | GPLv3                                   | ExtJS 4                                                |
| JavaScript             | MIT                                     | AngularJS                                              |
| JavaScript             | MIT                                     | Nest                                                   |
| Perl                   | GPL                                     | Mojolicious                                            |
| Perl                   | GPL                                     | Catalyst                                               |
| Perl                   | GPL                                     | CGI::Application                                       |
| Perl                   | GPL                                     | Gantry Framework                                       |
| Perl                   | GPL                                     | Jifty                                                  |
| Perl                   | GPL                                     | Maypole                                                |
| Perl                   | GPL                                     | OpenInteract2                                          |
| Perl                   | Comercial                               | PageKit                                                |
| Perl                   | GPL                                     | Cyclone 3                                              |
| Perl                   | GPL                                     | CGI::Builder                                           |
| PHP                    | GPL                                     | BitPHP                                                 |
| PHP                    | BSD                                     | phalcon                                                |
| PHP                    | MIT                                     | Laravel                                                |
| PHP                    | GPL                                     | Self Framework                                         |
| PHP                    | LGPL                                    | ZanPHP                                                 |
| PHP                    | LGPL                                    | Tlalokes                                               |
| PHP                    | GPL                                     | SiaMVC                                                 |
| PHP                    | LGPL                                    | Agavi                                                  |
| PHP                    | BSD                                     | Zend Framework, proyecto continuado como Laminas Framework |
| PHP                    | MIT                                     | CakePHP                                                |
| PHP                    | GNU/GPL                                 | KumbiaPHP                                              |
| PHP                    | MIT                                     | Symfony                                                |
| PHP                    | MIT                                     | QCodo                                                  |
| PHP                    | GNU/GPL                                 | CodeIgniter                                            |
| PHP                    | GNU/GPL                                 | Polka-PHP                                              |
| PHP                    | BSD                                     | Kohana                                                 |
| PHP                    | MPL 1.1                                 | PHP4ECore                                              |
| PHP                    | GNU                                     | Practico                                               |
| PHP                    | GNU                                     | FlavorPHP                                              |
| PHP                    | Apache 2.0                              | Yupp PHP Framework                                     |
| PHP                    | BSD                                     | Yii PHP Framework                                      |
| PHP                    | GPL                                     | Osezno PHP Framework                                   |
| PHP                    | MIT                                     | Simple PHP Framework (sPHPf)                           |
| PHP                    | GNU/GPL                                 | gvHidra                                                |
| Python                 | ZPL                                     | Zope3                                                  |
| Python                 | Varias                                  | Turbogears                                             |
| Python                 | GPL                                     | Web2py                                                 |
| Python                 | BSD                                     | Pylons                                                 |
| Python                 | BSD                                     | Django                                                 |
| AS3                    | Adobe Open Source                       | Cairngorm                                              |
| AS3 y Flex             | MIT License                             | CycleFramework                                         |
- [ ] ----
----
