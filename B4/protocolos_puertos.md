# Protocolos de comunicación y sus puertos

### 1. ¿Qué es PPTP?
- **Respuesta:** PPTP (Point-to-Point Tunneling Protocol) es un protocolo utilizado para implementar redes privadas virtuales (VPN).
    - **Explicación:** PPTP permite la transferencia segura de datos a través de redes públicas, como Internet, al encapsular paquetes de datos en un túnel.

### 2. ¿Cuál es el puerto utilizado por PPTP?
- **Respuesta:** El puerto utilizado por PPTP es el 1723.
    - **Explicación:** Este puerto es utilizado para la comunicación inicial y la configuración del túnel VPN.

### 3. ¿Qué puerto utiliza el protocolo HTTP?
- **Respuesta:** El protocolo HTTP utiliza el puerto 80.
    - **Explicación:** Este puerto es estándar para la transmisión de páginas web no cifradas.

### 4. ¿Qué puerto utiliza el protocolo HTTPS?
- **Respuesta:** El protocolo HTTPS utiliza el puerto 443.
    - **Explicación:** HTTPS es la versión segura de HTTP, utilizando SSL/TLS para cifrar la comunicación, y el puerto 443 es el estándar para este tráfico seguro.

### 5. ¿Qué puerto utiliza el protocolo FTP?
- **Respuesta:** El protocolo FTP utiliza los puertos 20 y 21.
    - **Explicación:** El puerto 20 se utiliza para la transferencia de datos, mientras que el puerto 21 se usa para el control de la sesión y la autenticación.

### 6. ¿Qué puerto utiliza el protocolo SSH?
- **Respuesta:** El protocolo SSH utiliza el puerto 22.
    - **Explicación:** SSH (Secure Shell) es un protocolo de red que permite el acceso remoto seguro a través de un canal cifrado.

### 7. ¿Qué puerto utiliza el protocolo SMTP?
- **Respuesta:** El protocolo SMTP utiliza el puerto 25.
    - **Explicación:** SMTP (Simple Mail Transfer Protocol) es utilizado para el envío de correos electrónicos entre servidores.

### 8. ¿Qué puerto utiliza el protocolo DNS?
- **Respuesta:** El protocolo DNS utiliza el puerto 53.
    - **Explicación:** DNS (Domain Name System) traduce nombres de dominio a direcciones IP, y el puerto 53 es el estándar para este tipo de solicitudes.

### 9. ¿Qué puerto utiliza el protocolo POP3?
- **Respuesta:** El protocolo POP3 utiliza el puerto 110.
    - **Explicación:** POP3 (Post Office Protocol 3) es utilizado por los clientes de correo electrónico para recibir correos desde un servidor.

### 10. ¿Qué puerto utiliza el protocolo IMAP?
- **Respuesta:** El protocolo IMAP utiliza el puerto 143.
    - **Explicación:** IMAP (Internet Message Access Protocol) permite a los clientes de correo electrónico acceder a mensajes en un servidor y gestionarlos de manera remota.

### 11. ¿Qué puerto utiliza el protocolo Telnet?
- **Respuesta:** El protocolo Telnet utiliza el puerto 23.
    - **Explicación:** Telnet es un protocolo de red que permite el acceso remoto a una máquina a través de una sesión de texto.

### 12. ¿Qué puerto utiliza el protocolo SNMP?
- **Respuesta:** El protocolo SNMP utiliza el puerto 161.
    - **Explicación:** SNMP (Simple Network Management Protocol) se usa para la gestión y monitoreo de dispositivos en una red.

### 13. ¿Qué puerto utiliza el protocolo DHCP?
- **Respuesta:** El protocolo DHCP utiliza los puertos 67 y 68.
    - **Explicación:** DHCP (Dynamic Host Configuration Protocol) usa el puerto 67 para el servidor y el puerto 68 para el cliente para la asignación dinámica de direcciones IP.

### 14. ¿Qué puerto utiliza el protocolo LDAP?
- **Respuesta:** El protocolo LDAP utiliza el puerto 389.
    - **Explicación:** LDAP (Lightweight Directory Access Protocol) es utilizado para acceder a servicios de directorio en red.

### 15. ¿Qué puerto utiliza el protocolo RDP?
- **Respuesta:** El protocolo RDP utiliza el puerto 3389.
    - **Explicación:** RDP (Remote Desktop Protocol) permite el acceso remoto a escritorios y sistemas a través de una interfaz gráfica.

## GRE (Generic Routing Encapsulation)
- **Descripción:** GRE es un protocolo de encapsulamiento utilizado para transportar paquetes de diferentes protocolos de red a través de una red IP.
- **Propósito:** Permite la creación de túneles para transportar paquetes de un protocolo sobre otro, facilitando la comunicación entre redes privadas a través de una red pública.
- **Uso Común:** Es utilizado en configuraciones de VPN, para crear túneles punto a punto y en la transmisión de datos de protocolos que no son IP.
- 
# Listado de Protocolos TCP/IP

| Protocolo     | Descripción                                                                                               | Opciones y Detalles                                      |
|---------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| **IP (Internet Protocol)** | Encargado de direccionar y enrutar paquetes de datos entre dispositivos en una red.                         | IPv4 e IPv6 son las versiones más comunes.              |
| **TCP (Transmission Control Protocol)** | Protocolo orientado a conexión que garantiza la entrega ordenada y sin errores de los datos.              | Utiliza el puerto 80 para HTTP, 443 para HTTPS, etc.    |
| **UDP (User Datagram Protocol)** | Protocolo sin conexión que permite el envío de datagramas sin garantías de entrega o orden.                  | Utilizado en aplicaciones como streaming y juegos.      |
| **HTTP (Hypertext Transfer Protocol)** | Protocolo de comunicación para la transmisión de información en la web.                                        | HTTP/1.1, HTTP/2, y HTTP/3 son versiones comunes.       |
| **HTTPS (Hypertext Transfer Protocol Secure)** | Versión segura de HTTP que cifra la comunicación para proteger la privacidad.                                   | Usa el puerto 443 por defecto.                          |
| **FTP (File Transfer Protocol)** | Protocolo para la transferencia de archivos entre un cliente y un servidor.                                     | Funciona en los puertos 20 (datos) y 21 (control).      |
| **SFTP (SSH File Transfer Protocol)** | Protocolo para la transferencia de archivos que utiliza cifrado SSH para mayor seguridad.                       | Utiliza el puerto 22 por defecto.                       |
| **SMTP (Simple Mail Transfer Protocol)** | Protocolo para el envío de correos electrónicos entre servidores de correo.                                       | Opera en el puerto 25.                                  |
| **IMAP (Internet Message Access Protocol)** | Protocolo para la recuperación de correos electrónicos desde un servidor.                                         | Utiliza el puerto 143 (sin cifrar) o 993 (cifrado).      |
| **POP3 (Post Office Protocol version 3)** | Protocolo para la recuperación de correos electrónicos que descarga mensajes al dispositivo del usuario.            | Opera en el puerto 110 (sin cifrar) o 995 (cifrado).    |
| **DHCP (Dynamic Host Configuration Protocol)** | Protocolo que asigna direcciones IP dinámicamente a dispositivos en una red.                                       | Funciona en el puerto 67 (servidor) y 68 (cliente).     |
| **DNS (Domain Name System)** | Protocolo que traduce nombres de dominio a direcciones IP numéricas.                                               | Usa el puerto 53 para consultas y respuestas.           |
| **ICMP (Internet Control Message Protocol)** | Protocolo utilizado para enviar mensajes de error y operativos relacionados con la red.                             | Usado por comandos como `ping` y `traceroute`.          |
| **ARP (Address Resolution Protocol)** | Protocolo que traduce direcciones IP en direcciones MAC dentro de una red local.                                  | Opera en el puerto 0 (sin puerto específico).           |
| **Telnet**    | Protocolo que permite el acceso remoto a sistemas a través de una línea de comandos.                           | Usualmente usa el puerto 23.                            |
| **SSH (Secure Shell)** | Protocolo para acceso remoto seguro a través de una línea de comandos.                                            | Usa el puerto 22.                                       |
| **SNMP (Simple Network Management Protocol)** | Protocolo para la gestión y monitoreo de dispositivos en una red.                                                  | Usa el puerto 161 para solicitudes y 162 para traps.    |
| **RDP (Remote Desktop Protocol)** | Protocolo de Microsoft para el acceso remoto a escritorios de Windows.                                            | Opera en el puerto 3389.                                |
| **NTP (Network Time Protocol)** | Protocolo para sincronizar la hora entre sistemas a través de una red.                                           | Usa el puerto 123.                                      |
| **LDAP (Lightweight Directory Access Protocol)** | Protocolo para acceder y mantener servicios de directorio como servidores de usuarios.                           | Opera en el puerto 389 (sin cifrar) o 636 (cifrado).    |
| **SIP (Session Initiation Protocol)** | Protocolo para la gestión de sesiones de comunicación en tiempo real como llamadas VoIP.                           | Utiliza el puerto 5060 (sin cifrar) o 5061 (cifrado).    |
| **RADIUS (Remote Authentication Dial-In User Service)** | Protocolo para la autenticación, autorización y contabilidad de usuarios en redes.                              | Usa el puerto 1812 para autenticación.                 |
| **TFTP (Trivial File Transfer Protocol)** | Protocolo simple para la transferencia de archivos, generalmente en redes locales.                                | Opera en el puerto 69.                                  |
| **MPLS (Multiprotocol Label Switching)** | Protocolo de conmutación de etiquetas que dirige los datos a través de redes mediante etiquetas en lugar de direcciones. | No usa puertos específicos, se basa en etiquetas.       |
| **GRE (Generic Routing Encapsulation)**       | Encapsula paquetes de diferentes protocolos para su transporte a través de una red IP. | Crear túneles y transportar datos de protocolos no IP. |


## Listado de puertos TCP/UDP
| Puerto    | Descripción                                                             |
|-----------|-------------------------------------------------------------------------|
| 1/TCP     | TCP Servicio de multiplexado de puertos (TCPMUX)                        |
| 5/TCP     | Remote Job Entry (RJE)                                                  |
| 7/TCP     | Protocolo Echo (Responde con eco a llamadas remotas)                    |
| 9/TCP     | Protocolo Discard (Elimina cualquier dato que recibe)                   |
| 13/TCP    | Daytime (Fecha y hora actuales)                                         |
| 17/TCP    | Quote of the Day (Cita del Día)                                         |
| 18/TCP    | Message Send Protocol (MSP)                                             |
| 20/TCP    | FTP. File Transfer Protocol – Datos                                     |
| 21/TCP    | FTP. File Transfer Protocol – Control                                   |
| 22/TCP    | SSH, SCP, SFTP. Remote Login Protocol                                   |
| 23/TCP    | Telnet (manejo remoto de equipo, inseguro)                              |
| 25/TCP    | SMTP. Simple Mail Transfer Protocol (email)                             |
| 29/TCP    | MSG ICP                                                                 |
| 37/TCP    | Time Protocol. Sincroniza hora y fecha                                  |
| 39/TCP    | Protocolo de ubicación de recursos (RLP)                                |
| 42/TCP    | Servicio de nombres de Internet (nameserver)                            |
| 43/TCP    | WHOIS. Servicio de directorio                                           |
| 49/TCP    | Login Host Protocol. Acceso y autenticación basado en TCP/IP (Login)    |
| 53/UDP    | DNS. Domain Name System. Sistema de Nombres de Dominio                  |
| 67/UDP    | BOOTP (BootStrap Protocol) (Server), también usado por DHCP             |
| 68/UDP    | BOOTP (BootStrap Protocol) (Server), también usado por DHCP             |
| 69/UDP    | TFTP. Trivial File Transfer Protocol                                    |
| 70/TCP    | Gopher                                                                  |
| 79/TCP    | Finger                                                                  |
| 80/TCP    | HTTP. HyperText Transfer Protocol                                       |
| 88/TCP    | Kerberos. Agente de autenticación                                       |
| 95/TCP    | Extensión de Telnet                                                     |
| 109/TCP   | POP2. Post Office Protocol (email)                                      |
| 110/TCP   | POP3. Post Office Protocol (email)                                      |
| 115/TCP   | SFTP. Simple File Transfer Protocol                                     |
| 118/TCP   | SQL Services                                                            |
| 119/TCP   | NNTP. Newsgroup. Usado en los grupos de noticias de usenet              |
| 123/UDP   | NTP. Protocolo de sincronización de tiempo                              |
| 137/UDP   | NetBIOS. Name Service                                                   |
| 138/UDP   | NetBIOS. Datagram Service                                               |
| 139/TCP   | NetBIOS. Session Service                                                |
| 143/TCP   | IMAP. Internet Message Access Protocol v2 (email)                       |
| 161/UDP   | SNMP. Simple Network Management Protocol                                |
| 177/TCP   | XDMCP. Protocolo de gestión de displays en X11                          |
| 179/TCP   | BGP. Border Gateway Protocol. (Intercambio de tablas de rutas entre ISP)|
| 194/TCP   | IRC. Internet Relay Chat                                                |
| 201/TCP   | Enrutamiento AppleTalk                                                  |
| 202/TCP   | Enlace de nombres AppleTalk                                             |
| 204/TCP   | Echo AppleTalk                                                          |
| 206/TCP   | Zona de información AppleTalk                                           |
| 220/TCP   | IMAP. Internet Message Access Protocol v3 (email)                       |
| 389/TCP   | LDAP. Lightweight Directory Access Protocol                             |
| 443/TCP   | HTTPS sobre SSL. Usado para la transferencia segura de páginas web      |
| 445/TCP   | Microsoft-DS (Active Directory, compartición de ficheros)               |
| 465/TCP   | SMTP sobre SSL. Simple Mail Transfer Protocol (email)                   |
| 515/TCP   | LPD/LPR. Impresión en Windows                                           |
| 520/UDP   | RIP. Routing Information Protocol (Protocolo de Información de Enrutamiento)|
| 546/TCP   | DHCPv6 Client                                                           |
| 547/TCP   | DHCPv6 Server                                                           |
| 563/TCP   | NNTP sobre SSL. Usado en grupos de noticias de usenet                   |
| 587/TCP   | SMTP sobre TLS. Simple Mail Transfer Protocol (email)                   |
| 631/TCP   | CUPS. Common Unix Printing System                                       |
| 636/TCP   | LDAP sobre SSL/TLS. Lightweight Directory Access Protocol               |
| 993/TCP   | IMAP sobre SSL/TLS. Internet Message Access Protocol v4 (email)         |
| 995/TCP   | POP3 sobre SSL. Post Office Protocol (email)                            |
| 1080/TCP  | SOCKS. Proxy                                                            |
| 1433/TCP  | Microsoft-SQL-Server                                                    |
| 1434/TCP  | Microsoft-SQL-Monitor                                                   |
| 1512/TCP  | WINS. Windows Internet Naming Service                                   |
| 3128/TCP  | HTTP usado por web caches y por defecto en Squid Proxy                  |
| 3306/TCP  | MySQL                                                                   |
| 3389/TCP  | RDP. Remote Desktop Protocol                                            |
| 3396/TCP  | Novell agente de impresión NDPS                                         |
| 5000/TCP  | UPNP. Universal plug-and-play                                           |
| 5400/TCP  | VNC. Virtual Network Computing. Escritorio remoto (HTTP)                |
| 5500/TCP  | VNC. Virtual Network Computing. Escritorio remoto (HTTP)                |
| 5600/TCP  | VNC. Virtual Network Computing. Escritorio remoto (HTTP)                |
| 5700/TCP  | VNC. Virtual Network Computing. Escritorio remoto (HTTP)                |
| 5800/TCP  | VNC. Virtual Network Computing. Escritorio remoto (HTTP)                |
| 5900/TCP  | VNC. Virtual Network Computing. Escritorio remoto                       |
| 6000/TCP  | X11. Usado para X-windows                                               |
| 6129/TCP  | Dameware. Software de conexión remota                                   |
| 8000/TCP  | iRDMI. Intel Remote Desktop Management Interface (Streaming Shoutcast)  |
| 8080/TCP  | HTTP alternativo al puerto 80. También default en servidor Tomcat       |
| 9800/TCP  | WebDAV                                                                  |
| 1000/TCP  | Webmin                                                                  |
