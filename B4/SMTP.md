## SMTP: Simple Mail Transfer Protocol

### 1. ``SMTP``

- El ``SMTP (Simple Mail Transfer Protocol)`` es el protocolo utilizado para enviar mensajes de correo electrónico desde
un cliente a un servidor de correo, y desde un servidor de correo a otro servidor de correo hasta que llega al
destinatario final. Funciona sobre el puerto ``25 TCP``, aunque también se utiliza el puerto ``587 TCP sobre TLS`` y el
puerto ``465 TCP sobre SSL``.

  * ``Ventajas``: SMTP es esencial para entregar correos electrónicos, ya que establece las reglas y procedimientos para
    enviar y recibir mensajes entre servidores.
  * ``Uso``: SMTP se utiliza cada vez que envías un mensaje de correo electrónico desde tu cliente de correo hasta el
    servidor de correo del destinatario.

### 2. ``IMAP``

- ``IMAP`` es un protocolo de acceso a mensajes de correo electrónico que permite a los usuarios gestionar sus correos
  electrónicos directamente en el servidor de correo. Esto significa que los mensajes permanecen en el servidor incluso
  después de ser leídos o descargados a un cliente de correo.

    * ``Ventajas``: Permite acceder al mismo buzón de correo desde múltiples dispositivos y clientes diferentes,
      manteniendo la sincronización entre ellos. Los mensajes permanecen en el servidor, lo que facilita el acceso desde
      cualquier lugar con conexión a Internet.
    * ``Uso``: IMAP es ideal para aquellos que acceden a su correo desde múltiples dispositivos y desean mantener una
      copia de los mensajes en el servidor.

### 3. ``POP3``

- ``POP3`` también es un protocolo de acceso a mensajes de correo electrónico, pero difiere de IMAP en la forma en que
  maneja los mensajes. Con POP3, los mensajes se descargan desde el servidor a un cliente de correo y se eliminan del
  servidor una vez descargados. Por defecto, los mensajes se eliminan del servidor, aunque algunos clientes de correo
  pueden configurarse para dejar una copia en el servidor después de la descarga.

    * ``Ventajas``: POP3 es útil si deseas liberar espacio en el servidor, ya que los mensajes se almacenan localmente
      en el cliente de correo.
    * ``Uso``: adecuado para descargar correos en un único dispositivo.

### 4. ``Puertos``

| Protocolo | Puertos sin cifrado | Puertos con cifrado TLS/SSL |
| ----- | ----- | ----- |
| IMAP | 143 | 993 |
| POP3 | 110 | 995 |
| SMTP | 25 | 465 (SMTPS) o 587 (submission) |

### Códigos SMTP

Los códigos SMTP de respuesta se clasifican en función del primer dígito:

- ``2xx: Respuesta positiva``
    - El servidor ha aceptado el comando, se puede realizar una nueva petición.
    - ``250:`` OK, finalizado.
    - ``211:`` Estado del Sistema.
    - ``214:`` Ayuda.
    - ``220:`` Servidor preparado.
    - ``221:`` Cierra canal.
    - ``251:`` Redirección.

- ``3xx: Respuesta positiva transitoria``
    - Pendiente de recibir más información.
    - ``354:`` El servidor recibe direcciones de envío o recepción.

- ``4xx: Respuesta de terminación negativa transitoria``
    - Error temporal, se puede volver a solicitar la acción.
    - ``421:`` Servicio no disponible.
    - ``432:`` Recepción detenida.
    - ``449:`` Error de enrutado.
    - ``450:`` Buzón no disponible.
    - ``451:`` Error de procesamiento.

- ``5xx: Respuesta negativa``
    - El comando no ha sido aceptado y la acción solicitada no ha podido realizarse.
    - ``500:`` Error de sintaxis.
    - ``502:`` Comando no implementado.
    - ``552:`` Almacenamiento excedido.
    - ``553:`` Dirección no autorizada.

### Estándares y RFCs del SMTP

- ``RFC 5321:`` Define el estándar para el intercambio de correo entre dos PC's usando TCP/IP.
- ``RFC 5322:`` Define la sintaxis de las cabeceras de los mensajes de correo y cómo deben interpretarse (en BNF).
- ``RFC 1049:`` Describe formatos de texto plano en el cuerpo de un mensaje (ASCII 7 bits) y otros formatos como
  PostScript, SGML, TEX, etc.
- ``RFC 974:`` Estándar para el procedimiento de enrutado de mensajes basado en DNS-MX.

### Extensiones del SMTP

- ``MIME (Multipurpose Internet Mail Extensions):`` Permite el intercambio de diferentes tipos de archivos (texto,
  audio, vídeo, etc.) superando las limitaciones de ASCII-7. Es un estándar de Internet que extiende el formato de los
  correos electrónicos para soportar texto en múltiples idiomas, caracteres especiales, imágenes, archivos adjuntos y
  otros tipos de contenido no ASCII. MIME define cómo deben formatearse los mensajes para incluir información adicional
  y cómo deben manejarse los diferentes tipos de datos.
    - Campos MIME: `Content-Type`, `Content-Transfer-Encoding`, `Content-Description`, `Content-ID`.
    - Características principales de MIME:
        - ``Tipo de contenido (Content-Type):`` Especifica el tipo de datos en el cuerpo del mensaje, como `text/plain`
          para texto sin formato, `text/html` para HTML, `image/jpeg` para imágenes, etc.
        - ``Codificación de contenido (Content-Transfer-Encoding):`` Define cómo se codifican los datos para que puedan
          ser transmitidos de forma segura a través de sistemas de correo electrónico que solo manejan caracteres ASCII.
          Algunos métodos comunes son Base64 y Quoted-Printable.
        - ``Encabezados MIME (MIME Headers):`` Agrega información adicional en los encabezados del correo electrónico,
          como el tipo de contenido, la codificación utilizada, el nombre del archivo adjunto, etc.
        - ``Multipart:`` Permite que un mensaje de correo electrónico contenga varios elementos en diferentes partes (
          por ejemplo, texto e imágenes), cada uno con su propio tipo de contenido.
    - Usos de MIME:
        - ``Correo Electrónico:`` MIME es ampliamente utilizado para enviar correos electrónicos con texto enriquecido,
          imágenes, archivos adjuntos y contenido multimedia. - ``Web:`` MIME también se usa en la web para definir el
          tipo de contenido de los archivos transmitidos, como HTML, CSS, JavaScript, imágenes, videos, etc.
    - MIME ha sido fundamental para mejorar la funcionalidad del correo electrónico y la web, permitiendo una
      comunicación más rica y diversa.


- ``ODMR (On-Demand Mail Relay):`` Permite que el correo sea transmitido a receptores que se conecten intermitentemente
  después de ser autenticados.

- ``ESMTP (Extended SMTP):`` Protocolo extendido definido en la ``RFC 4954`` para autenticar la identidad del cliente.
    - ``EHLO dominio:`` Verifica la existencia del dominio.
    - ``ETRN dominio:`` Permite al cliente solicitar todos los mensajes que el servidor tenga destinados para él.
    - ``AUTH:`` Negocia un protocolo de seguridad para el intercambio de datos.

### Proceso de Envío de un Mensaje SMTP

#### HELO -> MAIL FROM -> RCPT TO -> DATA -> QUIT o TURN

1. ``Conexión:`` El emisor SMTP establece una conexión TCP con el servidor destino. Espera un código `220 Service ready`
   o `421 Service not available`.
2. ``Identificación:`` Envía el comando `HELO` o `EHLO` para identificarse.
3. ``Inicio de Transacción:`` El emisor envía el comando `MAIL FROM` para iniciar la transacción del mensaje.
4. ``Destinatarios:`` Envía comandos `RCPT TO` para cada destinatario del mensaje.
5. ``Contenido del Mensaje:`` Envía el comando `DATA` para notificar el inicio del contenido del mensaje.
6. ``Envío de Datos:`` El cliente envía los datos del mensaje, incluyendo las cabeceras.
7. ``Finalización:`` El emisor termina la sesión con `QUIT` o continúa enviando nuevos mensajes.

### Comandos SMTP Principales

- ``HELO:`` Identificación del cliente al servidor.
- ``EHLO:`` Identificación extendida para soportar comandos adicionales.
- ``MAIL FROM:`` Indica el remitente del mensaje.
- ``RCPT TO:`` Indica los destinatarios del mensaje.
- ``DATA:`` Inicia la transferencia del contenido del mensaje.
- ``QUIT:`` Termina la sesión.
- ``TURN:`` Intercambia roles entre cliente y servidor sin una nueva conexión.
- ``ETRN:`` Solicita al servidor enviar todos los mensajes pendientes.
- ``AUTH:`` Negocia el protocolo de seguridad.
- ``PIPELINING:`` Permite enviar comandos en secuencia sin esperar respuesta.
- ``CHUNKING:`` Permite enviar grandes bloques de datos en partes.
- ``VRFY:`` Verifica la existencia de un buzón en el servidor.
- ``HELP:`` Muestra los comandos compatibles con el servicio SMTP.
- ``STARTTLS:`` Activa la seguridad a nivel de transporte.

### Otras Extensiones

- ``8BITMIME:`` Soporta la transmisión de datos en 8 bits.
- ``SMTPUTF8:`` Permite la codificación UTF-8 de nombres de buzón y campos de cabecera.
- ``NOOP:`` Mantiene la conexión activa sin enviar datos.
- ``EXPN:`` Verifica listas de correo.

---

Este resumen cubre los aspectos principales del protocolo SMTP, incluyendo códigos de respuesta, estándares, extensiones
y comandos utilizados en la transferencia de correos electrónicos.

| Código | Descripción |
| :---- | :---- |
| 2 xx | Respuesta positiva: la acción solicitada se ha realizado correctamente. Se puede iniciar una nueva solicitud. |
| 3 xx | Respuesta temporal positiva: se ha aceptado el pedido, pero la acción solicitada está pendiente de recibir más información. El cliente SMTP debería enviar otro comando que especifique esta información. |
| 4 xx | Respuesta negativa de finalización transitoria: el pedido no ha sido aceptado y la acción solicitada no ha podido producirse. Sin embargo, la condición del error es temporal y la acción puede solicitarse de nuevo. |
| 5 xx | Respuesta negativa: el pedido no ha sido aceptado y la acción solicitada no ha podido producirse. El cliente SMTP no debería repetir la misma petición. |

A continuación encontrará la mayoría de los códigos de respuesta negativos SMTP utilizados por los servidores:

| Códigos de respuesta | Detalles | Acciones |
| :---- | :---- | :---- |
| 420 | Tiempo excedido, problema de conexión | Este mensaje de error solo es devuelto por los servidores mail GroupWise. Contacte con el administrador del servidor de correo de destino |
| 421 | Servicio no disponible, canal de transmisión en curso de cierre | Procedente del error indeterminado, asegúrese de que el envío a otro dominio funciona. Si es así, vuelva a intentarlo más tarde |
| 432 | Recepción del email en el servidor Exchange detenido | Este mensaje de error solo es devuelto por los servidores de correo Microsoft Exchange. Contacte con el administrador del servidor de correo de destino |
| 449 | Un error de enrutado | Este mensaje de error solo es devuelto por los servidores de correo Microsoft Exchange. Microsoft recomienda realizar un diagnóstico con su herramienta WinRoute |
| 450 | Petición de acción de correo no efectuada: buzón de correo no disponible (por ejemplo, buzón de correo ocupado o temporalmente bloqueado por razones de seguridad o de blacklistage) | Compruebe si su dirección IP del servidor de correo no es blacklistada ([SpamHaus](https://check.spamhaus.org/)) y si su email no incluye palabras que se refieran al spam. |
| 451 | Se ha interrumpido la acción necesaria: Error de procesamiento local | Esto puede deberse a una sobrecarga momentánea, o a una verificación del SPF del dominio emisor incorrecta. Consulte el mensaje complementario que le haya proporcionado el servidor o contacte con el administrador del servidor si persiste |
| 452 | Acción solicitada no realizada: sistema de almacenamiento insuficiente | Su servidor de correo está "sobrecargado". Esto también puede deberse a un gran número de mensajes que intentan ser enviados a la vez. Por favor, compruebe su bandeja de salida e inténtelo de nuevo |
| 455 | Servidor incapaz de recibir la configuración | Espere un tiempo y vuelva a intentarlo. En caso de fallo, contacte con el administrador del servidor de correo del destinatario |
| 500 | Error de sintaxis, comando no reconocido (puede incluir errores como una línea de comandos demasiado larga) | Esto suele ser causado por el antivirus o firewall del remitente. Compruebe esto y vuelva a intentarlo |
| 501 | Error de sintaxis en los parámetros o argumentos | Esto suele deberse a una dirección de correo de destinatario errónea o a un problema de antivirus o firewall en el lado del remitente. Compruebe la dirección de destino y su antivirus o firewall. |
| 502 | Pedido no implementado | Los parámetros o opciones utilizados al enviar el email con su servidor SMTP son reconocidos pero desactivados en su configuración. Por favor, contacte con su proveedor de servicio. |
| 503 | El servidor ha encontrado una mala secuencia de comandos. | Esto suele deberse a un problema de autenticación. Asegúrese de estar bien autenticado en el servidor SMTP en lo que respecta a la configuración de su cliente de correo. |
| 504 | Parámetro de órdenes no implementado | Los parámetros o opciones utilizados al enviar el email con su servidor SMTP son reconocidos pero desactivados en su configuración. Por favor, contacte con su proveedor de servicio. |
| 535 | falló durante la autenticación | Se ha generado la información de usuario/contraseña o el envío puede estar bloqueado en su dirección de correo. Compruebe el estado de su dirección de correo electrónico desde el área de cliente de OVHcloud. Un cambio de la contraseña puede desbloquear el envío si la cuenta ha sido bloqueada por spam, consulte nuestra guía [¿Qué hacer con una cuenta bloqueada debido a correo no deseado?](https://help.ovhcloud.com/csm/es-es-email-blocked-for-spam?id=kb_article_view&sysparm_article=KB0053429) para más información |
| 550 | Acción solicitada no realizada: buzón de correo no disponible | El servidor de correo de destino no ha podido verificar la dirección de correo electrónico utilizada. Esto suele deberse a una dirección de correo electrónico de destino no válida, pero también puede significar que el servidor de correo de destino tenga problemas de cortafuegos o conectividad. Compruebe la dirección de correo electrónico del destinatario e inténtelo de nuevo |
| 550 5.7.1 | Email rejected per policy reason | El servidor de correo de destino rechazó la dirección de correo de envío por motivos de política de seguridad. Estas razones pueden ser múltiples, normalmente se detallan con el código de error. En algunos casos, puede ser una dirección IP de la cadena de transmisión que está presente en una lista de rechazo. Para comprobar la reputación de una dirección IP, puede probarla, por ejemplo, en [MXtoolbox](https://maxtoolbox.com/blacklists.aspx) o comprobar la cadena de transmisión de un mensaje de correo desde la dirección de correo electrónico correspondiente con [Mailtester](https://www.mail-tester.com/) |
| 550 5.7.26 | This message does not have authentication information or fails to pass authentication checks | El correo electrónico fue rechazado porque el servicio de correo electrónico del remitente no tiene configurado SPF o DKIM en su nombre de dominio. Se recomienda configurar un registro SPF de prioridad, que es compatible con todas nuestras soluciones de correos electrónicos. Use nuestra guía "[Mejorar la seguridad del correo electrónico mediante el registro SPF](https://help.ovhcloud.com/csm/es-es-dns-spf-record?id=kb_article_view&sysparm_article=KB0051709)". Si su oferta de correo electrónico tiene la opción DKIM, puede implementarla usando nuestra guía “[Mejorar la seguridad del correo electrónico mediante el registro DKIM](https://help.ovhcloud.com/csm/es-es-dns-zone-dkim?id=kb_article_view&sysparm_article=KB0058253)”. |
| 551 | Usuario no local | Esto se usa generalmente como una estrategia de prevención contra el spam. Por alguna razón, el relevo de correo no está autorizado a transferir su mensaje a otro servidor distinto del suyo. Por favor, contacte con su proveedor de servicio. |
| 552 | Petición de acción de correo interrumpida: espacio de almacenamiento superado | El usuario al que ha intentado contactar ya no tiene espacio disponible para recibir mensajes. Desafortunadamente, la única solución es contactar con el destinatario a través de otro método |
| 553 | Acción solicitada no realizada: dirección de correo electrónico no autorizada | Esto suele deberse a una dirección de correo electrónico de destino incorrecta. Por favor, compruebe que la dirección de correo electrónico es correcta. |
| 554 | Transacción fallida, "Aquí no hay servicios SMTP" | En general, se trata de un problema de lista negra. Compruebe si su dirección IP del servidor de correo no es blacklistada ([SpamHaus](https://check.spamhaus.org/)) |
| 555 | MAIL FROM / RCPT TO, parámetros no reconocidos o no implementados | El servidor SMTP saliente no guarda correctamente la dirección de correo electrónico utilizada en los parámetros "De" o "A". Por favor, compruebe que las direcciones de correo electrónico indicadas son correctas y también que no ha superado el límite establecido por OVHcloud: 200 emails /hora por cuenta y 300 emails /hora/ip |

