# Comandos linux

``addgroup``

- Se utiliza para crear un grupo nuevo.
- Sintaxis: addgroup nom_grupo

> Crea un nuevo grupo llamado desarrolladores:

````bash
sudo addgroup desarrolladores
````

``adduser``

- Se utiliza para añadir un usuario. En ese momento, no solo se creará la cuenta del usuario sino también su directorio
  de trabajo, un nuevo grupo de trabajo que se llamará igual que el usuario y añadirá una serie de ficheros de
  configuración al directorio de trabajo del nuevo usuario.
- Sintaxis: adduser nom_usuario [nom_grupo]

> Crea un nuevo usuario llamado juan y lo agrega al grupo desarrolladores:

````bash
sudo adduser juan --ingroup desarrolladores
````

``alias``

- En ciertas ocasiones se suelen utilizar comandos que son difíciles de recordar o que son demasiado extensos, pero en
  UNIX existe la posibilidad de dar un nombre alternativo a un comando con el fin de que cada vez que se quiera
  ejecutar, sólo se use el nombre alternativo.
- Sintaxis: alias nom_alias=’comando’

> Crea un alias llamado ll para ls -l:

````bash
alias ll='ls -l'
````

> Guarda el alias permanentemente en el archivo .bashrc:

````bash
echo "alias ll='ls -l'" >> ~/.bashrc
source ~/.bashrc
````

``apt-cache search`` (texto)

- Muestra una lista de todos los paquetes y una breve descripción relacionado con el texto que hemos buscado.

> Busca paquetes relacionados con "nginx":

````bash
apt-cache search nginx
````

``apt-get dist-upgrade``

- Función adicional de la opción anterior que modifica las dependencias por la de las nuevas versiones de los paquetes.

> Realiza una actualización completa del sistema:

````bash
sudo apt-get update
sudo apt-get dist-upgrade
````

``apt-get install`` (paquetes)

- Instala paquetes.

> Instala el paquete curl:

````bash
sudo apt-get install curl
````

``apt-get remove`` (paquete)

- Borra paquetes. Con la opción –purge borramos tambien la configuración de los paquetes instalados.

> Elimina el paquete especificado del sistema.

````bash
sudo apt-get remove nombre_del_paquete
````

``apt-get update``

- Actualiza la lista de paquetes disponibles para instalar.

> Actualiza la lista de paquetes disponibles desde los repositorios configurados.

````bash
sudo apt-get update
````

``apt-get upgrade``

- Instala las nuevas versiones de los diferentes paquetes disponibles.

> Instala las actualizaciones disponibles para los paquetes instalados.

````bash
sudo apt-get upgrade
````

``at``

- Realiza un tarea programada una sola vez.
- Sintaxis: at [-lr] hora [fecha].

> Programa un trabajo que se ejecutará dentro de 1 minuto.

````bash
echo "echo 'Hola mundo'" | at now + 1 minute
````

``bash, sh``

- Existen varias shells para Unix, Korn-Shell (ksh), Bourne-Shell (sh), C-Shell (csh),bash.
- Sintaxis: bash / sh / ksh / csh.

> Ejecuta el script script.sh usando el intérprete bash.

````bash
bash script.sh
````

``bg``

- Manda un proceso a segundo plano.
- Sintaxis: bg PID.

> Esto envía el comando sleep 60 al fondo.

````bash
sleep 60 &
````

> Reanuda un trabajo detenido (si lo hubiera) en segundo plano.

````bash
bg
````

``cal``

- Muestra el calendario.
- Sintaxis: cal [[mes] año].

> Muestra el calendario del año 2025.

````bash
cal 2025
````

``cat``

- Muestra el contenido del archivo en pantalla en forma continua, el prompt retornará una vez mostrado el contenido de
  todo el archivo. Permite concatenar uno o mas archivos de texto.
- Sintaxis: cat nom_archivo.

> Muestra el contenido de archivo.txt en la terminal.

````bash
cal 2025
````

``cd``

- Cambia de directorio.
- Sintaxis: cd nom_directorio.

> Cambia el directorio actual a la ruta especificada.

````bash
cd /ruta/a/directorio
````

``chattr``

- Cambiar atributos de un fichero.
- Sintaxis: chattr atributos nom_archivo.

> Hace que archivo.txt no pueda ser modificado (inmutable).

````bash
sudo chattr +i archivo.txt
````

``chgrp``

- Cambia el grupo al que pertenece el archivo.
- Sintaxis: chgrp nom_grupo nom_archivo.

> Cambia el grupo de archivo.txt al grupo especificado.

````bash
sudo chgrp grupo archivo.txt
````

``chmod``

- Utilizado para cambiar la proteción o permisos de accesos a los archivos.
    - r:lectura
    - w:escritura
    - x:ejecución
    - +: añade permisos
    - -:quita permisos
    - u:usuario
    - g:grupo del usuario
    - o:otros
- Sintaxis: chmod permisos nom_archivo

> Añadir el permiso de ejecución para el usuario.
>
>Quitar el permiso de lectura para el grupo.

````bash
chmod u+x archivo.txt
chmod g-r archivo.txt
````

- Significado:
    - u+x:
        - ``u`` → usuario
        - ``+`` → añade
        - ``x`` → permiso de ejecución
        - ⇒ Añade el permiso de ejecución para el usuario.

    - g-r:
        - ``g`` → grupo del usuario
        - ``-`` → quita
        - ``r`` → permiso de lectura
        - ⇒ Quita el permiso de lectura para el grupo.

> Cambia los permisos de archivo.sh para que el propietario pueda leer, escribir y ejecutar, y el resto sólo pueda leer y ejecutar.

````bash
chmod 755 archivo.sh
````

- Primer dígito: permisos del propietario (user, u)
- Segundo dígito: permisos del grupo (group, g)
    - Tercer dígito: permisos de otros (others, o)

> | Permiso | Valor numérico | Descripción          |
>  |---------|----------------|----------------------|
>  | r       | 4              | lectura (read)       |
>  | w       | 2              | escritura (write)    |
>  | x       | 1              | ejecución (execute)  |

- Los valores se suman para formar el dígito de cada grupo:
    - 0: sin permisos (---)
    - 1: solo ejecución (--x)
    - 2: solo escritura (-w-)
    - 3: escritura y ejecución (-wx)
    - 4: solo lectura (r--)
    - 5: lectura y ejecución (r-x)
    - 6: lectura y escritura (rw-)
    - 7: lectura, escritura y ejecución (rwx)

``chown``

- Cambia el propietario de un archivo.
- Sintaxis: chown nom_propietario nom_archivo.

> Cambia el propietario y/o grupo de un archivo.

````bash
sudo chown usuario:grupo archivo.txt
````

``chroot``

- Nos permite cambiar el directorio raiz.
- Sintaxis: chroot nom_directorio_raiz.

> Cambia el directorio raíz aparente

````bash
sudo chroot /nuevo/directorio/raiz
````

``clear``

- Limpia la pantalla, y coloca el prompt al principio de la misma.
- Sintaxis: clear.

> Limpia la terminal.

````bash
clear
````

``cmp, diff``

- Permite la comparación de dos archivos, línea por línea. Es utilizado para compara archivos de datos.
- Sintaxis: diff nom_archivo1 nom_archivo2 / cmp nom_archivo1 nom_archivo2.

> Compara archivos.

````bash
cmp archivo1.txt archivo2.txt
diff archivo1.txt archivo2.txt
````

``cp``

- Copia archivos en el directorio indicado.
- Sintaxis: cp nom_archivo nom_directorio.

> cp archivo.txt /ruta/destino/

````bash
cp archivo.txt /ruta/destino/
````

``crontab``
Realizar una tarea programada de forma regular. Sintaxis: minuto(0-59) hora(0-23) dia_mes(1-31) mes(1-12) dia_semana(
0-6) comando.
> Edita el archivo de tareas programadas.

````bash
crontab -e
````

- Ejemplos de líneas en el archivo crontab:

> 1. Ejecutar un script todos los días a las 2:30 AM

````bash
30 2 * * * /ruta/al/script.sh
````

> 2. Ejecutar un comando cada 5 minutos

````bash
*/5 * * * * /ruta/al/comando
````

> 3. Ejecutar cada lunes a las 9 AM

````bash
0 9 * * 1 /ruta/al/script.sh
````

> 4. Ejecutar cada 15 minutos, entre las 8 y 10 de la mañana, de lunes a viernes

````bash
*/15 8-10 * * 1-5 /ruta/al/script.sh
````

> 5. Ejecutar cada primer día del mes a la medianoche

````bash
0 0 1 * * /ruta/al/script.sh
````

> 6. Enviar un recordatorio por correo cada día a las 6 PM

````bash
0 18 * * * echo "Recuerda hacer tu respaldo" | mail -s "Recordatorio" usuario@dominio.com
````

> 7. Borrar archivos temporales cada domingo a la 1 AM

````bash
0 1 * * 0 rm -rf /ruta/temporal/*
````

> 8. Reiniciar un servicio cada día a la medianoche

````bash
0 0 * * * systemctl restart apache2
````

> 9. Ejecutar un script cada hora

````bash
0 * * * * /ruta/al/script.sh
````

``cut``

- Tiene como uso principal mostrar una columna de una salida determinada.
    - La opción -d va seguida del delimitador de los campos y la opción -f va seguida del número de campo a mostrar.
    - El “delimitador” por defecto es el tabulador, nosotros lo cambiamos con la opción -d.
- Sintaxis: cut [opciones] nom_archivo.

> Corta campos de un archivo o entrada.

````bash
cut -d ':' -f1 /etc/passwd
````

>- Ejemplo 1: Cortar campos separados por dos puntos (:)
>    - Extrae el nombre de usuario del archivo /etc/passwd:

````bash
cut -d ':' -f 1 /etc/passwd
````

> - Ejemplo 2: Cortar varias columnas
>     - Extrae el usuario y el directorio de inicio del archivo /etc/passwd:

````bash
cut -d ':' -f 1,6 /etc/passwd
````

>- Ejemplo 3: Cortar caracteres específicos
>    - Muestra los primeros 4 caracteres de cada línea de un archivo:

````bash
cut -c 1-4 archivo.txt
````

>- Ejemplo 4: Cortar el último carácter de cada línea

````bash
cut -c -1 archivo.txt
````

>- Ejemplo 5: Cortar desde un carácter en adelante
>    - Muestra desde el tercer carácter hasta el final de cada línea:

````bash
cut -c 3- archivo.txt
````

>- Ejemplo 6: Usar echo y cut juntos

````bash
echo "Hola Mundo" | cut -d ' ' -f 2
# Salida: Mundo
````

>- Ejemplo 7: Cortar usando tabulador como delimitador

````bash
cut -d $'\t' -f 2 archivo_tab.txt
````

``date``

- Retorna el día, fecha, hora (con minutos y segundos) y año.
- Sintaxis: date.

> Muestra o establece la fecha y hora.

````bash
date
````

``delgroup``

- Se utiliza para eliminar un grupo.
- Sintaxis: delgroup nom_grupo.

> Elimina un grupo.

 ````bash
sudo delgroup nombre_del_grupo
````

``deluser``

- Elimina una cuenta de usuario. La pega de este comando es que no elimina automáticamente el directorio de trabajo del
  usuario.
- Sintaxis: deluser nom_usuario.

> Elimina un usuario.

 ````bash
sudo deluser nombre_del_usuario
````

``df``

- Muestra los sistemas de ficheros montados.
- Sintaxis:df

> Muestra el espacio en disco.

 ````bash
df -h
````

``dmesg``

- Muestra los mensajes del kernel durante el inicio del sistema.
- Sintaxis: dmesg.

> Muestra mensajes del núcleo.

 ````bash
dmesg | less
````

``Dpkg -reconfigure`` (paquetes)

- Volver a reconfigurar un paquete ya instalado.

> Reconfigura un paquete instalado.

 ````bash
sudo dpkg-reconfigure paquete
````

``du``

- Sirve para ver lo que me ocupa cada directorio dentro del directorio en el que me encuentro y el tamaño total.
- Sintaxis: du

> Muestra el uso de disco.

 ````bash
du -sh /ruta/al/directorio
````

``echo``

- Muestra un mensaje por pantalla.
- Sintaxis: echo “Cadena”.

> Muestra un texto o variable.

 ````bash
echo "Hola, mundo"
````

``eject``

- Mediante la utilización de este comando se conseguirá la expulsión de la unidad de CD, siempre y cuando esta no esté
  en uso.
- Sintaxis: eject.

> Expulsa un medio extraíble.

 ````bash
eject /dev/cdrom
````

``env``
Para ver las variables globales. Sintaxis: env.

``exit``
Cierra las ventanas o las conexiones remotas establecidas o las conchas abiertas. Antes de salir es recomendable
eliminar todos los trabajos o procesos de la estación de trabajo. Sintaxis: exit.

``fg``
Manda un proceso a primer plano. Sintaxis: fg PID.

``file``
Determina el tipo del o los archivo(s) indicado(s). Sintaxis: file nom_archivo.

``find``
Busca los archivos que satisfacen la condición en el directorio indicado. Sintaxis: find nom_directorio o nom_archivo
condición.

``finger``
Permite encontrar información acerca de un usuario. Sintaxis: finger / finger usuario.

``free``
Muestra información sobre el estado de la memoria del sistema, tanto la swap como la memoria física.Tambien muestra el
buffer utilizado por el kernel. Sintaxis: free.

``fsck``
Para chequear si hay errores en nuestro disco duro. Sintaxis: fsck ­t fs_typo dispositivo.

``ftp``
Protocolo de Transferencia de Archivos, permite transferir archivos de y para computadores remotos. Sintaxis: ftp
maquina_remota.

``grep``
Su funcionalidad es la de escribir en salida estándar aquellas líneas que concuerden con un patrón. Busca patrones en
archivos. Sintaxis: grep [-cilnv] expr nom_archivos.

``gzip``
Comprime solo archivo utilizando la extensión .gz. Sintaxis: gzip nom_archivo.

``head``
Muestra las primeras lineas de un fichero. Sintaxis: head -count nom_archivo.

``history``
Lista los más recientes comandos que se han introducido en la ventana. Es utilizado para repetir comandos ya tipeados,
con el comando !. Sintaxis: history

``id``
Numero id de un usuario. Sintaxis: id

``ifconfig``
Obtener información de la configuración de red. Sintaxis: ifconfig.

``insmod``
Carga en memoria un módulo. Sintaxis: insmod

``job``
Lista los procesos que se están ejecutando en segundo plano. Sintaxis: jobs

``kill``
Permite interactuar con cualquier proceso mandando señales.Kill (pid) termina un proceso y Kill -9 (pid) fuerza a
terminar un proceso en caso de que la anterior opción falle. Sintaxis: kill [opciones] PID.

``last``
Este comando permite ver las últimas conexiones que han tenido lugar. Sintaxis: last.

``less``
Muestra el archivo de la misma forma que more, pero puedes regresar a la página anterior presionando las teclas “u” o
“b”. Sintaxis: less nom_archivo

``ln``
Sirve para crear enlaces a archivos, es decir, crear un fichero que apunta a otro. Puede ser simbólico si usamos -s o
enlace duro. Sintaxis: ln [-s] nom_archivo nom_acceso.

``logout``
Las sesiones terminan con el comando logout. Sintaxis: logout.

``lpr``
Imprime un archivo en la impresora predeterminada. Sintaxis: lpr -[lista de requerimientos]/ lpr -P nombre_archivo.

``ls``
Lista los archivos y directorios dentro del directorio de trabajo. Sintaxis: ls.

``lsattr``
Ver atributos de un fichero. Sintaxis: lsattr nom_archivo.

``lsmod``
Muestra los módulos cargados en memoria. Sintaxis: lsmod.

``mail``
Para enviar/recibir correo a/de otros usuarios de la red, o dentro de nuestro ordenador. Sintaxis: mail.

``make``
Es una herramienta que controla la creación de ejecutables y otros archivos de un programa a partir de los archivos
fuente. Sintaxis: make.

``man``
Ofrece información acerca de los comandos o tópicos del sistema UNIX, así como de los programas y librerías existentes.
Sintaxis: man comando.

``mkdir``
Crea un nuevo directorio. Sintaxis: mkdir nom_directorio.

``mv``
Este comando sirve para renombrar un conjunto. Sintaxis: mmv nom_archivos1 nom_archivos2.

``more``
Muestra el archivo en pantalla. Presionando enter, se visualiza linea por linea. Presinando la barra espaciadora,
pantalla por pantalla. Si desea salir, presiona q. Sintaxis: more nom_archivo.

``mount``
En Linux no existen las unidades A: ni C: sino que todos los dispositivos “cuelgan” del directorio raíz /. Para acceder
a un disco es necesario primero montarlo, esto es asignarle un lugar dentro del árbol de directorios del sistema.
Sintaxis: mount -t sistema_de_archivo dispositivo nom_directorio.

``mv``
Mueve archivos o subdirectorios de un directorio a otro, o cambiar el nombre del archivo o directorio. Sintaxis: mv
nom_archivo1 …nom_archivoN nom_directorio.

``netstat``
Muestra las conexiones y puertos abiertos por los que se establecen las comunicaciones. Sintaxis: netstat.

``nice``
Permite cambiar la prioridad de un proceso en nuestro sistema. Sintaxis: nice -n prioridad PID.

``passwd``
Se utiliza para establecer la contraseña a un usuario. Sintaxis: passwd nom_usuario.

``ping``
El comando ping se utiliza generalmente para testear aspectos de la red, como comprobar que un sistema está encendido y
conectado; esto se consigue enviando a dicha máquina paquetes ICMP. El ping es útil para verificar instalaciones TCP/IP.
Este programa nos indica el tiempo exacto que tardan los paquetes de datos en ir y volver a través de la red desde
nuestro PC a un determinado servidor remoto. Sintaxis: ping (maquina).

``poweroff``
Apagar el ordenador. Sintaxis: poweroff.

``ps``
Muestra información acerca de los procesos activos. Sin opciones, muestra el número del proceso, terminal, tiempo
acumulado de ejecución y el nombre del comando. Sintaxis: ps.

``pstree``
Muestra un árbol de procesos. Sintaxis: pstree.

``pwd``
Muestra el directorio actual de trabajo. Sintaxis: pwd.

``reset``
Si observamos que escribimos en pantalla y no aparece el texto pero al pulsar enter realmente se está escribiendo, o que
los colores o los textos de la consola se corrompen, puede ser que alguna aplicación en modo texto haya finalizado
bruscamente no restaurando los valores estándar de la consola al salir. Con esto forzamos unos valores por defecto,
regenerando la pantalla. Sintaxis: reset.

``rlogin``
Conectan un host local con un host remoto. Sintaxis: rlogin maquina_remota.

``rm``
Remueve o elimina un archivo. Sintaxis: rm nom_archivo.

``rmdir``
Elimina el directorio indicado, el cual debe estar vacío. Sintaxis: rmdir nom_directorio.

``rmmod``
Descarga de memoria un módulo, pero sólo si no está siendo usado. Sintaxis: rmmod.

``route``
El comando route se utiliza para visualizar y modificar la tabla de enrutamiento. Sintaxis: route (muestra información
del comando route).

``scp``
Sirve para hacer una copia segura entre dos ordenadores. La información viaja encriptada. Sintaxis: scp
usuario@servidor:directorio_servidor directorio_local.

``set``
Para ver las variables de entorno. Sintaxis: set.

``sftp``
Protocolo de Transferencia de Archivos, permite transferir archivos de y para computadores remotos. La información viaja
encriptada. Sintaxis: sftp maquina_remota.

``sort``
Muestra el contenido de un fichero, pero mostrando sus líneas en orden alfabético. Sintaxis: Sort [opciones]
nom_archivo.

``ssh`` (Secure Shell Client)
Es un programa para conectarse en una máquina remota y ejecutar programas en ella. Utilizado para reemplazar el rlogin y
rsh, además provee mayor seguridad en la comunicación entre dos hosts. El ssh se conecta al host indicado, donde el
usuario de ingresar su identificación (login y password) en la máquina remota, la cual realiza una autentificación del
usuario. Sintaxis: ssh maquina_remota.

``startx``
Inicia el entorno gráfico(servidor X). Sintaxis: startx.

``su``
Con este comando accedemos al sistema como root. Sintaxis: su.

``tail``
Este comando es utilizado para examinar las últimas líneas de un fichero. Sintaxis: tail -count nom_archivo.

``tar``
Comprime archivos y directorios utilizando la extensión .tar. Sintaxis: tar -[arg] nom_archivo.tar nom_archivo.

``telnet``
Conecta el host local con un host remoto, usando la interfaz TELNET. Sintaxis: telnet maquina_remota

``top``
Muestra los procesos que se ejecutan en ese momento, sabiendo los recursos que se están consumiendo(Memoria,CPU,…).Es
una mezcla del comando uptime,free y ps. Sintaxis: top.

``touch``
Crea un archivo vacio. Sintaxis: touch nom_archivo.

``traceroute``
Permite determinar la ruta tomada por un paquete para alcanzar su destino en Internet. Sintaxis: traceroute [opciones]
host [tamaño del paquete].

``umask``
Establece la máscara de permisos. Los permisos con los que se crean los directorios y los archivos por defecto.
Sintaxis: umask a-rwx,u+rw,g+r.

``umount``
Establece la máscara de permisos. Los permisos con los que se crean los directorios y los archivos por defecto.
Sintaxis: umask a-rwx,u+rw,g+r.

``unalias``
Borra un alias. Sintaxis: unalias nom_alias.

``uniq``
Este comando lee un archivo de entrada y compara las líneas adyacentes escribiendo solo una copia de las líneas a la
salida. La segunda y subsecuentes copias de las líneas de entrada adyacentes repetidas no serán escritas. Las líneas
repetidas no se detectarán a menos que sean adyacentes. Si no se especifica algún archivo de entrada se asume la entrada
estándar. Sintaxis: uniq [opciones] nom_archivo_entrada nom_archivo_salida.

``uptime``
Nos indica el tiempo que ha estado corriendo la máquina. Sintaxis: uptime.

``vi``
Permite editar un archivo en el directorio actual de trabajo. Es uno de los editores de texto más usado en UNIX.
Sintaxis: vi nom_archivo.

``view``
Es similar al vi, solo que no permite guardar modificaciones en el archivo, es para leer el contenido del archivo.
Sintaxis: view nom_archivo.

``wc``
Cuenta los caráteres, palabras y líneas del archivo de texto. Sintaxis: wc nom_archivo.

``whereis``
Devuelve la ubicación del archivo especificado, si existe. Sintaxis: whereis nomb_archivo.

``who``, w Lista quienes están conectado al servidor, con nombre de usuario, tiempo de conexión y el computador remoto
desde donde se conecta. Sintaxis: who / w.

``whoami``
Escribe su nombre de usuario en pantalla. Sintaxis: whoami.

``xmessage``
Enviar un mensaje al display de otro usuario o al nuestro propio. Sintaxis: xmessage (mensaje) / export
DISPLAY=157.92.49.211:0 xmessage Hola!!.

``yes``

- Escribe “y” continuamente.
    - Sintaxis: yes.

``&``

- Añadiendo un & al final del comando haremos que se comando ese ejecute en segundo plano.
    - Sintaxis: nom_comando&.

``!``

- Repite el último comando colocando la letra con la que comienza el comando o su número de history.
    - Sintaxis: !.