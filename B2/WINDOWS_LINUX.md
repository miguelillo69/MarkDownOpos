# 1. **¿Qué es un SIstema Operativo?**

- Un Sistema Operativo (SO) es un software fundamental que actúa como intermediario entre el hardware de una computadora y las aplicaciones o programas que se ejecutan en ella. Es un componente esencial que permite la interacción del usuario con la máquina y la gestión de recursos del sistema.

# 2. **Actualización del Sistema Operativo**  
## 1. **Windows**  
* **Windows Update:** Es el método oficial proporcionado por Microsoft para mantener el sistema operativo y otros productos de Microsoft actualizados. Windows Update descarga e instala automáticamente las actualizaciones críticas, de seguridad y otras actualizaciones recomendadas para el sistema.  
* **Microsoft Update:** Es similar a Windows Update, pero también incluye actualizaciones para otros productos de Microsoft, como Microsoft Office.  
* **Actualizaciones manuales:** Puedes descargar actualizaciones directamente desde el sitio web de Microsoft y aplicarlas manualmente al sistema.  
* **Actualizaciones del fabricante del dispositivo:** Algunos fabricantes de hardware ofrecen actualizaciones específicas para sus dispositivos a través de sus sitios web o programas de actualización.  
* **Actualizaciones de software de terceros:** Además de las actualizaciones de Microsoft, muchos programas de terceros (como navegadores web, reproductores multimedia, etc.) ofrecen actualizaciones automáticas o manuales para mantener su software actualizado.


## 2. **Linux**  
* **Gestor de paquetes:** La mayoría de las distribuciones de Linux utilizan un gestor de paquetes para administrar el software del sistema. Estos gestores permiten buscar, instalar y actualizar paquetes de software, incluidos el sistema operativo y las aplicaciones.  
- **APT (Advanced Package Tool):** Es el gestor de paquetes utilizado en distribuciones basadas en Debian, como Ubuntu. Los comandos "apt-get" y "apt" se utilizan para actualizar el sistema y los paquetes instalados.  
- **DNF/YUM:** Son gestores de paquetes utilizados en distribuciones basadas en Red Hat, como Fedora y CentOS. Los comandos "dnf" y "yum" se utilizan para buscar, instalar y actualizar paquetes.  
- **Zypper:** Es el gestor de paquetes utilizado en SUSE Linux. Se utiliza para gestionar las actualizaciones del sistema y del software.  
- **Actualizaciones automáticas:** Muchas distribuciones de Linux ofrecen opciones para configurar actualizaciones automáticas, lo que permite que el sistema descargue e instale automáticamente las actualizaciones disponibles en un horario predeterminado.

## 3. **Comandos más habituales de los gestores de paquetes.**

| Gestor | Distr | Comandos más utilizados |
| ----- | ----- | ----- |
| APT | Debian, Ubuntu | `sudo apt update`: Actualiza la lista de paquetes disponibles. |
|  |  | `sudo apt upgrade`: Actualiza los paquetes instalados. |
|  |  | `sudo apt install <nombre_paquete>`: Instala un paquete. |
|  |  | `sudo apt remove <nombre_paquete>`: Desinstala un paquete. |
| DNF/YUM | Fedora, CentOS | `sudo dnf check-update`: Comprueba actualizaciones disponibles. |
|  |  | `sudo dnf update`: Actualiza los paquetes instalados. |
|  |  | `sudo dnf install <nombre_paquete>`: Instala un paquete. |
|  |  | `sudo dnf remove <nombre_paquete>`: Desinstala un paquete. |
| Zypper | openSUSE | `sudo zypper refresh`: Actualiza la lista de paquetes disponibles. |
|  |  | `sudo zypper update`: Actualiza los paquetes instalados. |
|  |  | `sudo zypper install <nombre_paquete>`: Instala un paquete. |
|  |  | `sudo zypper remove <nombre_paquete>`: Desinstala un paquete. |
| Pacman | Arch Linux | `sudo pacman -Sy`: Sincroniza la base de datos de paquetes. |
|  |  | `sudo pacman -Syu`: Actualiza todos los paquetes. |
|  |  | `sudo pacman -S <nombre_paquete>`: Instala un paquete. |
|  |  | `sudo pacman -R <nombre_paquete>`: Desinstala un paquete. |
| APK | Alpine Linux | `apk update`: Actualiza la base de datos de paquetes. |
|  |  | `apk upgrade`: Actualiza todos los paquetes. |
|  |  | `apk add <nombre_paquete>`: Instala un paquete. |
|  |  | `apk del <nombre_paquete>`: Desinstala un paquete. |

# 3. **Mantenimiento de los Sistemas Operativos**  
## 1. **Programas en Windows**  
* **Disk Cleanup**: Elimina archivos temporales y otros innecesarios para liberar espacio en el disco.  
* **Disk Defragmenter**: Reorganiza los archivos fragmentados en el disco para mejorar el rendimiento.  
* **Windows Update**: Proporciona actualizaciones para el sistema operativo y otros productos Microsoft.  
* **Task Scheduler**: Permite programar y automatizar tareas y procesos.  
* **Event Viewer**: Proporciona un registro de eventos y errores, lo cual es útil para la resolución de problemas.  
* **Resource Monitor**: Muestra información detallada sobre el uso de CPU, memoria, disco y red.  
* **Security and Maintenance**: Ofrece recomendaciones de seguridad y mantenimiento, y también puede ayudar en la resolución de problemas.  
* **Windows Defender**: Herramienta integrada de protección contra malware y antivirus.

## 2. **Comandos en Windows**

| Comando | Descripción | Opciones Comunes y Importantes |
| ----- | ----- | ----- |
| `sfc` | Escanea y restaura archivos de sistema corruptos | `/scannow`, `/verifyonly` |
| `chkdsk` | Comprueba y repara errores en el disco duro | `/f` (reparar), `/r` (recuperar), `/x` (desmontar) |
| `diskpart` | Gestiona particiones y discos | `list`, `select`, `create`, `delete`, `format` |
| `ipconfig` | Muestra y gestiona la configuración de red | `/all`, `/release`, `/renew`, `/flushdns` |
| `netstat` | Muestra estadísticas de red | `-a` (todo), `-b` (binarios), `-n` (numérico) |
| `wmic` | Interfaz unificada para la administración del sistema | Diversas consultas y comandos |
| `defrag` | Desfragmenta discos | `/O` (optimizar), `/A` (analizar), `/X` (consolidar) |
| `gpupdate` | Actualiza políticas de grupo | `/force`, `/logoff`, `/sync` |
| `nslookup` | Consulta servidores DNS | `-type`, `server` (especificar servidor) |
| `sc` | Gestionar servicios de Windows | `query`, `start`, `stop`, `config` |
| `tasklist` | Muestra la lista de procesos en ejecución | `/S` (sistema remoto), `/M` (módulos) |
| `taskkill` | Termina procesos | `/F` (forzar), `/IM` (nombre imagen) |
| `bcdedit` | Gestiona la configuración de arranque | `/create`, `/delete`, `/set` |
| `reg` | Realiza operaciones en el registro de Windows | `add`, `delete`, `query`, `export`, `import` |
| `cleanmgr` | Limpia archivos innecesarios | `/sagerun` (configuración guardada) |

## 3. **PowerShell**

| Cmdlet | Descripción | Parámetros y Opciones Comunes |
| ----- | ----- | ----- |
| `Get-Process` | Lista los procesos en ejecución | `-Name`, `-Id` |
| `Stop-Process` | Termina un proceso | `-Name`, `-Id`, `-Force` |
| `Get-Service` | Lista los servicios en el sistema | `-Name`, `-Status` |
| `Start-Service` | Inicia un servicio | `-Name`, `-PassThru` |
| `Stop-Service` | Detiene un servicio | `-Name`, `-Force`, `-PassThru` |
| `Restart-Service` | Reinicia un servicio | `-Name`, `-Force`, `-PassThru` |
| `Get-EventLog` | Obtiene eventos del registro de eventos | `-LogName`, `-EntryType`, `-After`, `-Before` |
| `Clear-EventLog` | Limpia un registro de eventos | `-LogName` |
| `Get-HotFix` | Muestra las actualizaciones instaladas | `-Id`, `-Description` |
| `Install-WindowsUpdate` | Instala actualizaciones de Windows | `-MicrosoftUpdate`, `-IgnoreReboot` |
| `Get-Disk` | Muestra información sobre discos | `-Number`, `-PartitionStyle` |
| `Clear-Disk` | Limpia un disco | `-Number`, `-RemoveData` |
| `Format-Volume` | Formatea una partición de disco | `-DriveLetter`, `-FileSystem`, `-NewFileSystemLabel` |
| `Test-Connection` | Prueba una conexión de red | `-ComputerName`, `-Count`, `-Quiet` |
| `New-NetFirewallRule` | Crea una nueva regla de firewall | `-Name`, `-Action`, `-Direction`, `-Protocol` |
| `Get-NetIPAddress` | Muestra información de configuración IP | `-InterfaceAlias`, `-AddressFamily` |
| `Restart-Computer` | Reinicia una computadora | `-ComputerName`, `-Force` |
| `Set-ExecutionPolicy` | Cambia la política de ejecución de PowerShell | `-ExecutionPolicy`, `-Scope` |

## Opciones y Parámetros de ExecutionPolicy Restricted en PowerShell

- La directiva `ExecutionPolicy` en PowerShell determina las reglas bajo las cuales se pueden ejecutar los scripts en un sistema. Una de las políticas más restrictivas es `Restricted`.

### `-ExecutionPolicy Restricted`

- La política `Restricted` es la configuración predeterminada de PowerShell y está diseñada para evitar la ejecución de scripts. 
- Cuando está configurada en `Restricted`, PowerShell solo permite la ejecución de comandos interactivos (comandos ejecutados manualmente en la consola) y no permite la ejecución de ningún script, incluidos los scripts `.ps1`.

#### Parámetros relacionados con `ExecutionPolicy`

- **`-ExecutionPolicy`**: Especifica la política de ejecución que debe usarse. Los posibles valores son: `Restricted`, `AllSigned`, `RemoteSigned`, `Unrestricted`, `Bypass`, y `Undefined`.

- **`-Scope`**: Define el alcance de la política de ejecución. Puede ser:
    - `Process`: Aplica la política de ejecución solo a la sesión actual de PowerShell.
    - `CurrentUser`: Aplica la política al usuario actual.
    - `LocalMachine`: Aplica la política a todos los usuarios del sistema.

#### Ejemplos de Uso

1. **Establecer la política de ejecución en `Restricted` a nivel del equipo:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope LocalMachine
```

2. **Verificar la política de ejecución actual:**

```powershell
Get-ExecutionPolicy
```

#### Consideraciones

- La política `Restricted` es la más segura ya que bloquea todos los scripts.
- Es adecuada para entornos donde la seguridad es crítica y no se desea la ejecución de scripts automatizados.

#### Conclusión

- Utilizar `Restricted` puede proporcionar un nivel de seguridad alto, pero también limita la automatización. Es ideal para entornos controlados donde solo se permite la ejecución manual de comandos.


## 4. **Net**

| Comando | Descripción | Opciones y Usos Comunes |
| ----- | ----- | ----- |
| `net user` | Administra cuentas de usuario | `username`, `/add`, `/delete`, `/active:yes/no` |
| `net localgroup` | Administra grupos locales | `groupname`, `/add`, `/delete` |
| `net view` | Muestra una lista de recursos compartidos | `/DOMAIN:domainname` |
| `net share` | Administra recursos compartidos | `sharename`, `/add`, `/delete`, `/remark:text` |
| `net use` | Conecta o desconecta un recurso compartido | `\\computer\share`, `/delete`, `/persistent:yes/no` |
| `net start` | Inicia un servicio | `servicename` |
| `net stop` | Detiene un servicio | `servicename` |
| `net send` | Envía un mensaje en una red (obsoleto) | `username`, `message` |
| `net session` | Muestra o desconecta sesiones con el equipo | `\\computername`, `/delete` |
| `net time` | Muestra o sincroniza la hora del sistema con un servidor | `\\computername`, `/set` |
| `net config` | Muestra la configuración de servicios | `server`, `workstation` |
| `net statistics` | Muestra estadísticas del servicio | `server`, `workstation` |
| `net print` | Administra trabajos de impresión (obsoleto) | `/delete`, `jobid` |

## 5. **Mantenimiento Ubuntu**

| Comando | Opción | Descripción |
| ----- | ----- | ----- |
| apt | update | Actualiza la lista de paquetes disponibles. |
|  | upgrade | Actualiza los paquetes instalados. |
|  | autoremove | Elimina paquetes innecesarios. |
| dpkg | \--list | Lista los paquetes instalados. |
|  | \-i paquete.deb | Instala un paquete. |
| fsck | /dev/sda1 | Comprueba y repara la partición sda1. |
| journalctl | \-xe | Muestra mensajes de registro detallados. |
| top / htop | \- | Muestra la utilización de recursos en tiempo real. |
| uname | \-a | Muestra todos los detalles del sistema. |
| lscpu, lsblk, lsmem | \- | Muestra información sobre la CPU, los bloques y la memoria, respectivamente. |
| systemctl | start servicio | Inicia un servicio. |
|  | enable servicio | Habilita un servicio al inicio. |
| ifconfig / ip | a | Muestra la configuración de red usando el comando `ip`. |
| df | \-h | Muestra el uso del disco en formato legible. |
| du | \-sh directorio | Muestra el uso del disco en un directorio específico. |
| find | /ruta \-name "nombre" | Busca archivos con un nombre específico. |
| cron | crontab \-e | Edita el archivo crontab del usuario actual. |
| tar | \-cvzf archivo.tar.gz /ruta | Comprime una ruta en un archivo tar. |
| ps | aux | Muestra todos los procesos del sistema. |
| kill | \-9 PID | Fuerza el cierre de un proceso por su PID. |
| useradd / userdel | username | Agrega o elimina un usuario. |

## 6. **Comandos importantes Ubuntu**

| Comando | Opción | Descripción |
| ----- | ----- | ----- |
| apt | update | Actualiza la lista de paquetes disponibles. |
|  | upgrade | Actualiza los paquetes instalados. |
|  | autoremove | Elimina paquetes innecesarios. |
| dpkg | \--list | Lista los paquetes instalados. |
|  | \-i paquete.deb | Instala un paquete. |
|  | \-r paquete | Elimina un paquete. |
| fsck | /dev/sda1 | Comprueba y repara la partición sda1. |
|  | \-a | Repara automáticamente el sistema de archivos. |
|  | \-f | Fuerza la comprobación incluso si el sistema parece limpio. |
| journalctl | \-xe | Muestra mensajes de registro detallados. |
|  | \-f | Muestra los registros en tiempo real. |
|  | \--since "YYYY-MM-DD HH:MM:SS" | Muestra registros desde una fecha y hora específicas. |
| top | \- | Muestra la utilización de recursos en tiempo real. |
| uname | \-a | Muestra todos los detalles del sistema. |
|  | \-r | Muestra la versión del kernel. |
|  | \-m | Muestra la arquitectura de la máquina. |
| lscpu | \- | Muestra información sobre la CPU. |
| lsblk | \- | Muestra información sobre los dispositivos de bloque. |
| lsmem | \- | Muestra información sobre la memoria. |
| systemctl | start servicio | Inicia un servicio. |
|  | enable servicio | Habilita un servicio al inicio. |
|  | status servicio | Muestra el estado de un servicio. |
| ifconfig / ip | a | Muestra la configuración de red. |
| df | \-h | Muestra el uso del disco en formato legible. |
|  | \-T | Incluye el tipo de sistema de archivos. |
| du | \-sh directorio | Muestra el uso del disco en un directorio específico. |
|  | \-a | Muestra el uso del disco para todos los archivos, no solo directorios. |
| find | /ruta \-name "nombre" | Busca archivos con un nombre específico. |
|  | \-type d | Busca solo directorios. |
|  | \-mtime \-N | Busca archivos modificados en los últimos N días. |
| cron | crontab \-e | Edita el archivo crontab del usuario actual. |
|  | crontab \-l | Lista las entradas crontab actuales. |
|  | crontab \-r | Elimina el archivo crontab del usuario actual. |
| tar | \-cvzf archivo.tar.gz /ruta | Comprime una ruta en un archivo tar. |
|  | \-xvzf archivo.tar.gz | Extrae un archivo tar. |
|  | \-tvf archivo.tar | Lista el contenido de un archivo tar. |
| ps | aux | Muestra todos los procesos del sistema. |
|  | \-e | Muestra todos los procesos. |
|  | \-u usuario | Muestra procesos de un usuario específico. |
| kill | \-9 PID | Fuerza el cierre de un proceso por su PID. |
|  | \-SIGKILL PID | Envía la señal SIGKILL a un proceso. |
|  | \-l | Lista todas las señales disponibles. |
| useradd | \-m | Crea el directorio principal para el nuevo usuario. |
|  | \-G grupo | Agrega el usuario a un grupo adicional. |
| userdel | \-r | Elimina el directorio principal del usuario. |
| wget | \-O file | Descarga un archivo a una ruta específica. |
|  | \-c | Continúa una descarga interrumpida. |
|  | \--recursive | Descarga todos los archivos de un sitio web. |
| curl | \-O | Descarga un archivo. |
|  | \-I | Muestra solo la cabecera de una respuesta HTTP. |
|  | \-d "data" | Envía datos en una petición POST. |
| ssh | \-l usuario | Conecta a un servidor SSH como un usuario específico. |
|  | \-p puerto | Conecta a un puerto específico en el servidor SSH. |
|  | \-i clave | Utiliza una clave específica para la autenticación. |
| scp | usuario@host:/ruta | Copia archivos a través de SSH. |
|  | \-r | Copia directorios recursivamente. |
|  | \-P puerto | Utiliza un puerto específico. |
| sed | 's/foo/bar/g' | Reemplaza "foo" por "bar" en una entrada. |
|  | \-n | Suprime la salida automática de patrones. |
|  | \-i | Editar archivos en su lugar (in-situ). |
| grep | \-i | Busca sin tener en cuenta mayúsculas y minúsculas. |
|  | \-r | Busca recursivamente en directorios. |
|  | \-E | Utiliza expresiones regulares extendidas. |
| chmod | \+x archivo | Da permiso de ejecución a un archivo. |
|  | \-R | Cambia permisos recursivamente. |
|  | 755 archivo | Establece los permisos a 755\. |
| chown | usuario:grupo archivo | Cambia el propietario y grupo de un archivo. |
|  | \-R | Cambia propietario y grupo recursivamente. |
|  | \-h | Cambia el propietario de un enlace simbólico y no del archivo referenciado. |
| ping | \-c N | Envía N pings. |
|  | \-i segundos | Intervalo entre pings. |
|  | \-s tamaño | Tamaño de los paquetes de ping. |
| rsync | \-a | Copia archivos recursivamente y preserva permisos. |
|  | \--delete | Elimina archivos en el destino que no estén en el origen. |
|  | \-z | Comprime los datos durante la transferencia. |
| nano/pico/vim | \- | Editores de texto en la línea de comandos. |
| locate | nombre\_archivo | Busca archivos por nombre. |
|  | \-i | Busca sin tener en cuenta mayúsculas y minúsculas. |
|  | \-r expresion\_regular | Busca usando una expresión regular. |
| mount | /dev/sda1 /mnt | Monta un dispositivo en un punto de montaje. |
|  | \-o ro | Monta como solo lectura. |
|  | \-t tipo | Especifica el tipo de sistema de archivos. |
| umount | /mnt | Desmonta un punto de montaje. |
| umask | sin opción | Muestra la máscara actual en formato octal. |
|  | \-S | Muestra la máscara en formato simbólico, por ejemplo, `u=rwx,g=rx,o=rx`. |
|  | 022 | Establece la máscara a 022\. Esto significa que los nuevos archivos tendrán permisos 755 y los nuevos directorios tendrán permisos 644\. |

## 7. **Estructura de directorios raíz de Ubuntu**

| Carpeta | Descripción |
| ----- | ----- |
| /bin | Binarios esenciales del sistema. |
| /boot | Archivos de arranque del sistema. |
| /dev | Dispositivos del sistema. |
| /etc | Archivos de configuración del sistema y aplicaciones. |
| /home | Directorios personales de los usuarios. |
| /lib y /lib64 | Bibliotecas compartidas del sistema. |
| /media | Punto de montaje para dispositivos extraíbles. |
| /mnt | Punto de montaje para sistemas de archivos temporales o externos. |
| /opt | Directorio para paquetes de software de terceros. |
| /root | Directorio personal del usuario root. |
| /sbin | Binarios del sistema que requieren permisos de superusuario (root). |
| /srv | Datos servidos por el sistema. |
| /tmp | Directorio temporal para archivos temporales. |
| /usr | Subdirectorios con programas, bibliotecas y datos no esenciales. |
| /var | Archivos variables, como registros de sistema y bases de datos. |

## 8. **Estructura de carpetas raíz de Windows**

| Carpeta | Descripción |
| ----- | ----- |
| C:\\ | Unidad principal del sistema, donde se instala Windows. |
| C:\\Windows | Contiene los archivos del sistema operativo Windows. |
| C:\\Program Files | Contiene las aplicaciones instaladas para todos los usuarios. |
| C:\\Program Files (x86) | Contiene las aplicaciones instaladas para usuarios de 32 bits. |
| C:\\Users | Contiene los perfiles de usuario, incluyendo el perfil del usuario actual. |
| C:\\Documents and Settings | Contenía los perfiles de usuario en versiones anteriores de Windows. |
| C:\\ProgramData | Contiene datos de configuración y programas compartidos para todos los usuarios. |
| C:\\Windows\\System32 | Contiene archivos esenciales del sistema y las bibliotecas (DLL). |
| C:\\Windows\\SysWOW64 | Contiene archivos del sistema de 32 bits en sistemas de 64 bits. |
| C:\\Windows\\SystemApps | Contiene aplicaciones del sistema de Windows Store. |
| C:\\Windows\\Temp | Directorio temporal para archivos temporales. |
| C:\\Windows\\Users | Contiene perfiles de usuario adicionales. |
| C:\\Windows\\WinSxS | Almacena múltiples versiones de archivos de sistema compartidos. |
| C:\\Windows\\Fonts | Contiene fuentes (tipografías) instaladas en el sistema. |

