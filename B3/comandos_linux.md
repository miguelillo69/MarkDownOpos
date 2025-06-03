# Chuleta de Comandos Linux

## Comandos de Sistema

- **`uname`**: Muestra información del sistema.
    - `uname -a`: Información completa del sistema.
    - `uname -r`: Muestra la versión del kernel.
    - `uname -s`: Muestra el nombre del sistema operativo.

- **`top`**: Muestra procesos en tiempo real.
    - `top -d [segundos]`: Establece el intervalo de actualización.
    - `top -u [usuario]`: Muestra solo los procesos de un usuario específico.

- **`htop`**: Versión mejorada de `top` (requiere instalación).
    - `htop`: Ejecuta la interfaz interactiva.

- **`df`**: Muestra el uso del sistema de archivos.
    - `df -h`: Muestra el uso en formato legible.
    - `df -i`: Muestra el uso de inodos.

- **`du`**: Muestra el uso de disco de directorios.
    - `du -sh [directorio]`: Muestra el tamaño total del directorio.
    - `du -h --max-depth=1 [directorio]`: Muestra el tamaño de subdirectorios.

- **`free`**: Muestra la memoria libre y usada.
    - `free -h`: Muestra la memoria en formato legible.
    - `free -m`: Muestra la memoria en megabytes.

- **`uptime`**: Muestra el tiempo de actividad del sistema.
    - `uptime -p`: Muestra el tiempo de actividad en formato legible.

## Comandos de Archivos y Directorios

- **`ls`**: Lista archivos y directorios.
    - `ls -l`: Lista detallada con permisos, propietario, tamaño.
    - `ls -a`: Muestra archivos ocultos.
    - `ls -lh`: Muestra en formato legible por humanos.

- **`cd`**: Cambia de directorio.
    - `cd [directorio]`: Cambia al directorio especificado.
    - `cd ..`: Regresa al directorio padre.
    - `cd -`: Regresa al directorio anterior.

- **`pwd`**: Muestra el directorio de trabajo actual.

- **`cp`**: Copia archivos o directorios.
    - `cp [origen] [destino]`: Copia un archivo o directorio.
    - `cp -r [directorio] [destino]`: Copia un directorio y su contenido.
    - `cp -i [origen] [destino]`: Pide confirmación antes de sobrescribir.

- **`mv`**: Mueve o renombra archivos o directorios.
    - `mv [origen] [destino]`: Mueve o renombra un archivo o directorio.
    - `mv -i [origen] [destino]`: Pide confirmación antes de sobrescribir.

- **`rm`**: Elimina archivos o directorios.
    - `rm [archivo]`: Elimina un archivo.
    - `rm -r [directorio]`: Elimina un directorio y su contenido.
    - `rm -f [archivo]`: Elimina un archivo sin pedir confirmación.

- **`touch`**: Crea archivos vacíos o actualiza la fecha de acceso/modificación.
    - `touch [archivo]`: Crea un archivo vacío o actualiza la fecha.

- **`find`**: Busca archivos y directorios.
    - `find [directorio] -name [nombre]`: Busca archivos por nombre.
    - `find [directorio] -type f -size +1M`: Busca archivos mayores a 1 MB.

## Permisos y Propietarios

## `chmod`

El comando `chmod` en Linux se utiliza para cambiar los permisos de acceso a archivos y directorios. Los permisos se pueden establecer de dos maneras: **modo simbólico** y **modo octal**.

## Modos de Permisos

### Modo Simbólico

Los permisos se representan mediante letras y signos:

- **u**: Usuario (propietario del archivo)
- **g**: Grupo
- **o**: Otros
- **a**: Todos (u+g+o)

Los permisos se representan por:

- **r**: Lectura
- **w**: Escritura
- **x**: Ejecución

Los operadores son:

- **+**: Añadir permisos
- **-**: Eliminar permisos
- **=**: Establecer permisos exactos

#### Ejemplos:

- `chmod u+x archivo.txt`: Añade permiso de ejecución para el propietario.
- `chmod g-w archivo.txt`: Elimina el permiso de escritura para el grupo.
- `chmod o=r archivo.txt`: Establece permisos de solo lectura para otros.

### Modo Octal

Los permisos se representan por números, donde cada dígito representa los permisos para el usuario, grupo y otros, respectivamente:

- **4**: Lectura (r)
- **2**: Escritura (w)
- **1**: Ejecución (x)
- **0**: Sin permisos

Cada combinación de permisos se suma:

- **7**: Lectura, escritura y ejecución (rwx)
- **6**: Lectura y escritura (rw-)
- **5**: Lectura y ejecución (r-x)
- **4**: Solo lectura (r--)

#### Ejemplos:

- `chmod 755 archivo.txt`: Permite al propietario leer, escribir y ejecutar; al grupo y otros solo leer y ejecutar.
- `chmod 644 archivo.txt`: Permite al propietario leer y escribir; al grupo y otros solo leer.
- `chmod 700 archivo.txt`: Permite al propietario leer, escribir y ejecutar; ningún permiso para el grupo y otros.

## Opciones Adicionales

- **-R**: Aplica los cambios de forma recursiva a todos los archivos y directorios dentro de un directorio.

#### Ejemplo:

- `chmod -R 755 directorio/`: Cambia los permisos de todos los archivos y subdirectorios en `directorio/` a `755`.

- **--reference=archivo**: Cambia los permisos de `archivo` para que coincidan con los permisos de otro `archivo`.

#### Ejemplo:

- `chmod --reference=archivo1 archivo2`: Establece los permisos de `archivo2` igual a los de `archivo1`.

- **-v**: Muestra una salida detallada de los cambios realizados.

#### Ejemplo:

- `chmod -v 644 archivo.txt`: Muestra un mensaje indicando que los permisos del archivo `archivo.txt` han sido cambiados a `644`.

## Resumen de Comandos

| Comando          | Descripción                                    |
|------------------|------------------------------------------------|
| `chmod 777 archivo.txt` | Permite lectura, escritura y ejecución para todos. |
| `chmod 755 archivo.txt` | Permite lectura, escritura y ejecución para el propietario; lectura y ejecución para el grupo y otros. |
| `chmod 644 archivo.txt` | Permite lectura y escritura para el propietario; solo lectura para el grupo y otros. |
| `chmod +x archivo.txt` | Añade permiso de ejecución para el propietario. |
| `chmod u-r archivo.txt` | Elimina el permiso de lectura para el propietario. |
| `chmod -R 700 directorio/` | Establece permisos `700` de forma recursiva en todos los archivos y subdirectorios dentro de `directorio/`. |
| `chmod -v 644 archivo.txt` | Muestra un mensaje detallado de los cambios realizados en los permisos del archivo. |

## Notas

- El modo simbólico es más legible y permite cambios específicos en los permisos, mientras que el modo octal es más compacto y rápido para establecer permisos completos.
- La opción `-v` es útil para verificar y confirmar los cambios realizados en los permisos, proporcionando retroalimentación inmediata sobre las modificaciones.

Esta chuleta proporciona una visión completa de las opciones y usos comunes del comando `chmod` en Linux, incluyendo la opción `-v` para la salida detallada de cambios.


## `chown` en Linux

El comando `chown` se utiliza para cambiar el propietario y el grupo de uno o más archivos o directorios en Linux. A continuación, se detalla el uso y las opciones disponibles.

## Sintaxis Básica

```bash
chown [opciones] nuevo_propietario:nuevo_grupo archivo(s)
```

- **`chgrp`**: Cambia el grupo de archivos o directorios.
    - `chgrp [grupo] [archivo]`: Cambia el grupo.
    - `chgrp -R [grupo] [directorio]`: Cambia el grupo recursivamente.

## Comandos de Procesos

- **`ps`**: Muestra información de procesos.
    - `ps aux`: Muestra todos los procesos.
    - `ps -ef`: Muestra una lista completa de procesos.
    - `ps -u [usuario]`: Muestra procesos de un usuario específico.

- **`kill`**: Envía una señal a un proceso.
    - `kill [pid]`: Envía la señal por defecto (terminar) al proceso con el ID especificado.
    - `kill -9 [pid]`: Envía una señal de terminación forzada.

- **`pkill`**: Mata procesos por nombre.
    - `pkill [nombre_proceso]`: Mata todos los procesos con el nombre especificado.
    - `pkill -f [nombre_proceso]`: Mata procesos que coincidan con el patrón en la línea de comando.

- **`bg`**: Reanuda un trabajo en segundo plano.
    - `bg [job_id]`: Reanuda el trabajo especificado en segundo plano.

- **`fg`**: Trae un trabajo al primer plano.
    - `fg [job_id]`: Trae el trabajo especificado al primer plano.

- **`jobs`**: Lista los trabajos en segundo plano.
    - `jobs -l`: Muestra el ID de los trabajos junto con el proceso.

## Comandos de Red

- **`ifconfig`** o **`ip`**: Muestra o configura interfaces de red.
    - `ifconfig`: Muestra la configuración de la red (puede requerir privilegios de administrador).
    - `ip a`: Muestra todas las interfaces y sus direcciones.
    - `ip link set [interfaz] up`: Activa una interfaz.
    - `ip link set [interfaz] down`: Desactiva una interfaz.

- **`ping`**: Envía paquetes ICMP para comprobar la conectividad.
    - `ping [host]`: Envía paquetes a la dirección o nombre del host.
    - `ping -c [n] [host]`: Envía `n` paquetes.

- **`netstat`** o **`ss`**: Muestra conexiones de red.
    - `netstat -tuln`: Muestra puertos y servicios en uso.
    - `ss -tuln`: Alternativa más moderna a `netstat`.
    - `ss -s`: Muestra un resumen de las conexiones.

- **`wget`** o **`curl`**: Descarga archivos desde la web.
    - `wget [url]`: Descarga un archivo desde una URL.
    - `wget -O [archivo] [url]`: Descarga un archivo y lo guarda con un nombre específico.
    - `curl -O [url]`: Descarga un archivo desde una URL.
    - `curl -L [url]`: Sigue redireccionamientos.

## Gestión de Paquetes

- **`apt-get`** (Debian/Ubuntu):
    - `apt-get update`: Actualiza la lista de paquetes.
    - `apt-get upgrade`: Actualiza todos los paquetes instalados.
    - `apt-get install [paquete]`: Instala un paquete.
    - `apt-get remove [paquete]`: Elimina un paquete.
    - `apt-get autoremove`: Elimina paquetes que ya no son necesarios.

- **`yum`** (CentOS/RHEL):
    - `yum update`: Actualiza la lista de paquetes.
    - `yum install [paquete]`: Instala un paquete.
    - `yum remove [paquete]`: Elimina un paquete.
    - `yum list installed`: Lista todos los paquetes instalados.

- **`rpm`** (Red Hat/CentOS):
    - `rpm -ivh [paquete.rpm]`: Instala un paquete RPM.
    - `rpm -e [paquete]`: Elimina un paquete RPM.
    - `rpm -qa`: Lista todos los paquetes RPM instalados.
    - `rpm -ql [paquete]`: Lista archivos de un paquete RPM.

## Comandos de Texto

- **`cat`**: Muestra el contenido de un archivo.
    - `cat [archivo]`: Muestra el contenido del archivo.
    - `cat [archivo1] [archivo2] > [archivo3]`: Combina archivos en uno nuevo.

- **`more`** o **`less`**: Muestra el contenido de un archivo página por página.
    - `more [archivo]`: Muestra el archivo página por página.
    - `less [archivo]`: Similar a `more`, pero con capacidades de desplazamiento hacia atrás.

## `grep`
- **Descripción:** Busca texto en archivos.
- **Uso Básico:** `grep [patrón] [archivo]`
  - **Descripción:** Busca el patrón en el archivo especificado.
- **Opciones:**
  - `-r [patrón] [directorio]`
    - **Descripción:** Busca recursivamente en directorios.
  - `-i [patrón] [archivo]`
    - **Descripción:** Ignora la distinción entre mayúsculas y minúsculas.
  - `-v [patrón] [archivo]`
    - **Descripción:** Muestra las líneas que no coinciden con el patrón.
  - `-n [patrón] [archivo]`
    - **Descripción:** Muestra el número de línea junto con las líneas que coinciden con el patrón.

#### Ejemplo

- **Buscar un patrón en un archivo:**
  ```bash
  grep "error" archivo.log
  ```

- **`sed`**: Editor de texto en línea de comandos.
    - `sed 's/[busca]/[reemplaza]/g' [archivo]`: Sustituye texto en un archivo.
    - `sed -i 's/[busca]/[reemplaza]/g' [archivo]`: Sustituye texto en el archivo directamente.

- **`awk`**: Procesador de textos y generación de reportes.
    - `awk '{print $1}' [archivo]`: Imprime la primera columna de un archivo.
    - `awk -F ':' '{print $1}' [archivo]`: Usa ':' como delimitador y muestra la primera columna.

## Otros Comandos Útiles

- **`echo`**: Muestra un mensaje o variable.
    - `echo [mensaje]`: Muestra el mensaje en la consola.
    - `echo $[variable]`: Muestra el valor de una variable.

- **`history`**: Muestra el historial de comandos.
    - `history`: Muestra el historial de comandos.
    - `history | grep [comando]`: Busca un comando específico en el historial.

- **`man`**: Muestra el manual de un comando.
    - `man [comando]`: Muestra la página de manual para el comando especificado.
    - `man -k [palabra]`: Busca en las páginas de manual.

- **`alias`**: Crea alias de comandos.
    - `alias ll='ls -la'`: Crea un alias para `ls -la`.
    - `unalias [alias]`: Elimina un alias.

- **`tar`**: Archivo y compresión.
    - `tar -cvf [archivo.tar] [directorio]`: Crea un archivo tar.
    - `tar -xvf [archivo.tar]`: Extrae un archivo tar.
    - `tar -czvf [archivo.tar.gz] [directorio]`: Crea un archivo tar comprimido con gzip.
    - `tar -xzvf [archivo.tar.gz]`: Extrae un archivo tar comprimido con gzip.

- **`gzip`** y **`gunzip`**: Compresión y descompresión.
    - `gzip [archivo]`: Comprime un archivo.
    - `gunzip [archivo.gz]`: Descomprime un archivo.

- **`zip`** y **`unzip`**: Archivo y compresión ZIP.
    - `zip [archivo.zip] [archivos]`: Crea un archivo zip.
    - `unzip [archivo.zip]`: Extrae un archivo zip.
    - `zip -r [archivo.zip] [directorio]`: Crea un archivo zip recursivamente.
    - `unzip -l [archivo.zip]`: Muestra el contenido del archivo zip sin extraer.

---
## `traceroute` en Linux

El comando `traceroute` se utiliza para rastrear la ruta que siguen los paquetes de datos desde el host origen hasta el destino.

## Sintaxis Básica

```bash
traceroute [opciones] destino

traceroute -m 20 -n www.google.com
```
### Opciones
|Opción|	Descripción|
|:-----:|:------------:|
| -4 | Fuerza el uso de IPv4 en lugar de IPv6.|
| -6 | Fuerza el uso de IPv6 en lugar de IPv4.|
| -a | Muestra los nombres de los hosts en lugar de las direcciones IP.|
| -d | Muestra información de depuración adicional.|
| -f <hops> | Establece el número de saltos inicial desde el origen. Útil para comenzar el rastreo a partir de un punto específico.|
| -i <interfaz> | Especifica la interfaz de red a utilizar para el rastreo.|
| -m <max_hops> | Establece el número máximo de saltos (hops) a seguir antes de dar por terminado el rastreo.|
| -n | Muestra las direcciones IP en lugar de intentar resolver los nombres de los hosts.|
| -p <puerto> | Especifica el puerto a utilizar para el rastreo. Por defecto, se usa el puerto 33434.|
| -q <n> | Establece el número de consultas por salto. El valor predeterminado es 3.|
| -r | Realiza el rastreo usando una ruta estática sin realizar la búsqueda del nombre de dominio.|
| -s <source_address> | Especifica la dirección IP de origen que debe usarse para el rastreo.|
| -t <ttl> | Establece el Time-To-Live (TTL) inicial para los paquetes enviados.|
| -w <timeout> | Establece el tiempo de espera para cada respuesta en segundos. El valor predeterminado es 5 segundos.|
| -z <packet_size> | Establece el tamaño del paquete en bytes.|
| -h | Muestra la ayuda y las opciones del comando traceroute.|
| `-I` | Usa paquetes ICMP Echo en lugar de UDP. |
| `-T` | Usa paquetes TCP SYN en lugar de UDP. |

## Ejemplo de Uso

```bash
traceroute -m 30 www.example.com
```