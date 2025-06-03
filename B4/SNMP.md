# Introducción a SNMP

## Gestión de Redes

### ¿Qué es SNMP?

**SNMP** (Protocolo Simple de Gestión de Red) es un estándar ampliamente reconocido con muchas herramientas disponibles. Está presente en cualquier dispositivo de red decente.  
Basado en un modelo de solicitud/respuesta: **GET / SET**.

- **GET** se utiliza para monitoreo.
- **OIDs** (Identificadores de Objeto): claves para identificar cada dato en las respuestas.

#### Concepto de MIBs (Base de Información de Gestión)

Una **MIB** es una colección de OIDs.

### Encuestas típicas con SNMP

- **Dispositivos de red**: Bytes de entrada/salida por interfaz, errores, carga de CPU, tiempo de actividad, temperatura, etc.
- **Clientes (servidores o desktops)**: Espacio en disco duro, software instalado, procesos en ejecución, etc.

Windows y UNIX tienen agentes de SNMP.

### Protocolo y versiones de SNMP

- **Protocolo**: UDP, puerto 161.
- **Versiones**:
    - **v1 (1988)** – RFC1155, RFC1156, RFC1157: Especificación original.
    - **v2** – RFC1901 a RFC1908 + RFC2578: Nuevos tipos de datos y métodos mejorados de recopilación (GETBULK). Versión más usada: v2c (sin método de alta seguridad).
    - **v3** – RFC3411 a RFC3418: Alta seguridad.

### Roles de SNMP

- **Entidad gestora**: Recopila y presenta la información de dispositivos y servidores.
- **Dispositivo gestionado**: Contiene un agente de gestión que responde a las encuestas de la entidad gestora.

### ¿Cómo funciona SNMP?

#### Comandos Básicos

- **GET**: Solicita un valor de variable único.
- **GET-NEXT**: Solicita el siguiente valor (recursivo, para listas).
- **GET-RESPONSE**: Respuesta a GET/SET, o error.
- **SET**: Configura un valor o ejecuta una acción.
- **TRAP**: Notificación espontánea de incidente (fallo de línea, temperatura por encima del límite, etc.).

### OIDs y MIBs

- **OID (Identificadores de Objeto)**: Clave única para seleccionar un objeto particular en el dispositivo. Los OIDs se presentan en forma jerárquica en un árbol para asegurar su unicidad.
- **MIB (Base de Información de Gestión)**: Una colección de OIDs relacionados. Es una correlación de OIDs numéricos a nombres legibles.

#### Ejemplos de Árbol MIB
![Descripción de la imagen](https://www.incibe.es/sites/default/files/blog/SNMP/img_2_arbol_mib_representando_oid.png)

- **MIB-2**: Incluye subgrupos como `system`, `interfaces`, `ip`, `snmp`, entre otros.

### Archivos de MIB

Los archivos de MIB definen los objetos que se pueden encuestar, incluyendo:

- **Nombre de objeto**
- **Descripción de objeto**
- **Tipo de dato** (integer, texto, lista)

Utilizan una estructura de texto con ASN.1.

### Ejemplo de MIB

````plaintext
sysUpTime OBJECT-TYPE
SYNTAX TimeTicks
ACCESS read-only
STATUS mandatory
DESCRIPTION
"The time (in hundredths of a second) since the
network management portion of the system was last
re-initialized."
::= { system 3 }
````
### Encuestando un agente SNMP
#### Comandos típicos para encuestar:
- snmpget
- snmpwalk
- snmpstatus
- snmptable

#### Sintaxis
````bash
snmpXXX -c community -v1 host [oid]
snmpXXX -c community -v2c host [oid]
````
### Fallas comunes de SNMP
 - Dispositivo fuera de línea o inalcanzable.
 - Dispositivo sin un agente de SNMP.
 - Dispositivo configurado con otro texto de comunidad.
 - Dispositivo configurado para rechazar encuestas de SNMP desde su dirección de IP.
### SNMP Versión 3 y Seguridad
- SNMP v1 y v2c son inseguros. SNMP v3 fue creado para resolver esto, ofreciendo autenticación, integridad, privacidad y validez temporal mediante claves de usuario y firmas digitales.
- Niveles de Seguridad
  - **noAuthPriv**: Sin autenticación, sin privacidad.
  - **authNoPriv**: Con autenticación, sin privacidad.
  - **authPriv**: Con autenticación y privacidad.
### Configuración de SNMPv3
#### En Cisco
````java
snmp-server view vista-ro internet included
snmp-server group ReadGroup v3 auth read vista-ro
snmp-server user admin ReadGroup v3 auth md5 xk122r56
````

#### En Net-SNMP
````bash
# apt-get install snmp snmpd
# net-snmp-config --create-snmpv3-user -a "xk122r56" admin
/usr/sbin/snmpd
# snmpwalk -v3 -u admin -l authNoPriv -a MD5 -A "xk122r56" 127.0.0.1
````
### Materias Opcionales
#### SNMP y Seguridad
- Mandador (Controlador de Mensajes)
- Sistema secundario de procesar mensajes
- Sistema secundario de seguridad
- Sistema secundario de control de acceso

### Tipos de Mensajes en SNMP
- El protocolo SNMP (Simple Network Management Protocol) utiliza diferentes tipos de mensajes para la gestión y monitoreo de dispositivos en una red. Estos mensajes son:

- **GetRequest**: Solicita información específica de un dispositivo de red.
- **GetNextRequest**: Recupera la siguiente variable en la jerarquía MIB (Management Information Base) del dispositivo.
- **GetBulkRequest**: Permite recuperar grandes volúmenes de datos en una sola solicitud (introducido en SNMPv2c).
- **SetRequest**: Modifica o establece el valor de una variable en un dispositivo.
- **Response**: Envía la respuesta del dispositivo a un mensaje de solicitud (Get, Set, etc.).
- **Trap**: Envía notificaciones no solicitadas desde el agente SNMP al gestor, alertando sobre eventos importantes o fallos.
- **InformRequest**: Similar a Trap, pero requiere una confirmación del gestor de que el mensaje ha sido recibido (introducido en SNMPv2c).
- **Report**: Utilizado en SNMPv3 para comunicar errores o problemas específicos de seguridad.

Estos mensajes permiten la comunicación entre los agentes SNMP (dispositivos administrados) y los gestores SNMP (aplicaciones de monitoreo) para mantener la red funcionando de manera eficiente.