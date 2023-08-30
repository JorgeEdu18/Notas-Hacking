# Bandit Level 0 a Level 10

## Level 0 → Level 1

### Problema

The password for the next level is stored in a file called
**readme** located in the home directory. Use this password to log
into bandit1 using SSH. Whenever you find a password for a level,
use SSH (on port 2220) to log into that level and continue the game.

## Commands you may need to solve this level

[ls](https://man7.org/linux/man-pages/man1/ls.1.html), [cd](https://man7.org/linux/man-pages/man1/cd.1p.html), [cat](https://man7.org/linux/man-pages/man1/cat.1.html) ,[file](https://man7.org/linux/man-pages/man1/file.1.html),[du](https://man7.org/linux/man-pages/man1/du.1.html),[find](https://man7.org/linux/man-pages/man1/find.1.html)

### Solución

```scheme
bandit0@bandit:~$ ls -l
total 24
4 drwxr-xr-x  2     0     0 4096 Apr 23 18:04 .
4 drwxr-xr-x 70     0     0 4096 Apr 23 18:05 ..
4 -rw-r--r--  1     0     0  220 Jan  6  2022 .bash_logout
4 -rw-r--r--  1     0     0 3771 Jan  6  2022 .bashrc
4 -rw-r--r--  1     0     0  807 Jan  6  2022 .profile
4 -rw-r-----  1 11001 11000   33 Apr 23 18:04 readme
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
bandit0@bandit:~$ pwd
/home/bandit0
```

### Comandos utilizados

| Comandos | Extensión | Utilidad |
| --- | --- | --- |
| ls | -l | Sirve para ver los archivos en formato largo |
| cat |  | Mostrar el Contenido de un Archivo |

### CTF

NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

## Level 1 → Level 2

### Problema

The password for the next level is stored in a file called **-** located in the home directory

### Solución

```scheme
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit1@bandit:~$
```

### Notas

Para este nivel ocupamos que la ubicación actual del archivo debido a su nombre. Para esto utilizamos 

. → Toda el path de la ubicación donde se encuentra

/ → Guion para el archivo

( - ) → Es el nombre del archivo

### CTF

rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

## Level 2 → Level 3

### Problema

The password for the next level is stored in a file called **spaces in this filename** located in the home directory

### Solución

```scheme
bandit2@bandit:~$ ls -l
total 24
drwxr-xr-x  2     0     0 4096 Apr 23 18:04 .
drwxr-xr-x 70     0     0 4096 Apr 23 18:05 ..
-rw-r--r--  1     0     0  220 Jan  6  2022 .bash_logout
-rw-r--r--  1     0     0 3771 Jan  6  2022 .bashrc
-rw-r--r--  1     0     0  807 Jan  6  2022 .profile
-rw-r-----  1 11003 11002   33 Apr 23 18:04 spaces in this filename
bandit2@bandit:~$ cat spaces\ in\ this\ filename
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
```

### Notas

Para este ctf se tuvo que utilizar el \ para que el cat pudiera leer el documento, esto debido a que el nombre del archivo tiene espacios. Tambies te puede utilizar ‘cat 'spaces in this filename’ o poner el nombre de la ruta completa.

### CTF

aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

## Level 3 → Level 4

### Problema

The password for the next level is stored in a hidden file in the
**inhere** directory.

### Solución

```scheme
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2     0     0 4096 Apr 23 18:04 .
drwxr-xr-x 3     0     0 4096 Apr 23 18:04 ..
-rw-r----- 1 11004 11003   33 Apr 23 18:04 .hidden
bandit3@bandit:~/inhere$ cat .hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
bandit3@bandit:~/inhere$
```

### Notas

Al ser un archivo oculto tuvimos que utilizar el comando  ls - para poder encotrarlo.

### Comandos

| Comandos | extension | Utilidad |
| --- | --- | --- |
| ls | -a                                                     -l | -a : No ignora los archivos que inican con punto.                             -l Muestra los archivo en version larga.    |
| cat |  |  |
| cd |  | entrar a una carpeta |
| pwd |  | Saber en que carpeta te encuentras |

### CTF

2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

## Level 4 → Level 5

### Problema

The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.

### Solución

```scheme
.~�&ϯ"PT�Ibandit4@bandit:~/inhere$ cat ./-file06
'�cwk^j�����M����;,��co�9bandit4@bandit:~/inhere$ cat ./-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
```

### Notas

Utilice cat para ir en carpeta en carpeta. Pero no es lo optimo, pudimos utilizar el comando ‘file’ este determina el tipo de archivo.

```bash
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: Non-ISO extended-ASCII text, with no line terminators
bandit4@bandit:~/inhere$
```

### CTF

lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

## Level 5 → Level 6

### Problema

The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

- human-readable
- 1033 bytes in size
- not executable

## Solucion

```scheme
bandit5@bandit:~/inhere$ find . -type f -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```

Utilice find para que buscara en todo la carpeta un archivo un archivo regular y que pese 1033 bytes.

### Comandos que se usarón

| Comando | extensión |  |
| --- | --- | --- |
| Find | - type f | para buscar exclusivamente archivos regulares (no directorios ni otro tipo de archivos especiales) en la ubicación especificada. |
|  | -size  | Busca por el tamaño, en este caso son 1033 bytes (c) |

## Level 6 → Level 7

### Problema

The password for the next level is stored **somewhere on the server** and has all of the following properties:

- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

### Solución

```scheme
bandit6@bandit:~$ ls -la
total 20
drwxr-xr-x  2 0 0 4096 Apr 23 18:04 .
drwxr-xr-x 70 0 0 4096 Apr 23 18:05 ..
-rw-r--r--  1 0 0  220 Jan  6  2022 .bash_logout
-rw-r--r--  1 0 0 3771 Jan  6  2022 .bashrc
-rw-r--r--  1 0 0  807 Jan  6  2022 .profile
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c
find: ‘/var/log’: Permission denied
find: ‘/var/crash’: Permission denied
find: ‘/var/spool/rsyslog’: Permission denied
find: ‘/var/spool/bandit24’: Permission denied
find: ‘/var/spool/cron/crontabs’: Permission denied
find: ‘/var/tmp’: Permission denied
find: ‘/var/lib/polkit-1’: Permission denied
/var/lib/dpkg/info/bandit7.password
find: ‘/var/lib/chrony’: Permission denied
find: ‘/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/amazon’: Permission denied
find: ‘/var/lib/update-notifier/package-data-downloads/partial’: Permission denied
find: ‘/var/lib/snapd/void’: Permission denied
find: ‘/var/lib/snapd/cookie’: Permission denied
find: ‘/var/lib/ubuntu-advantage/apt-esm/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/private’: Permission denied
find: ‘/var/snap/lxd/common/lxd’: Permission denied
find: ‘/var/cache/ldconfig’: Permission denied
find: ‘/var/cache/apt/archives/partial’: Permission denied
find: ‘/var/cache/pollinate’: Permission denied
find: ‘/var/cache/private’: Permission denied
find: ‘/var/cache/apparmor/a4dd844e.0’: Permission denied
find: ‘/var/cache/apparmor/8eeb6286.0’: Permission denied
find: ‘/drifter/drifter14_src/axTLS’: Permission denied
find: ‘/home/bandit29-git’: Permission denied
find: ‘/home/drifter6/data’: Permission denied
find: ‘/home/bandit28-git’: Permission denied
find: ‘/home/drifter8/chroot’: Permission denied
find: ‘/home/ubuntu’: Permission denied
find: ‘/home/bandit5/inhere’: Permission denied
find: ‘/home/bandit27-git’: Permission denied
find: ‘/home/bandit30-git’: Permission denied
find: ‘/home/bandit31-git’: Permission denied
find: ‘/boot/efi’: Permission denied
find: ‘/proc/tty/driver’: Permission denied
find: ‘/proc/2568499/task/2568499/fd/6’: No such file or directory
find: ‘/proc/2568499/task/2568499/fdinfo/6’: No such file or directory
find: ‘/proc/2568499/fd/5’: No such file or directory
find: ‘/proc/2568499/fdinfo/5’: No such file or directory
find: ‘/etc/polkit-1/localauthority’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
find: ‘/etc/multipath’: Permission denied
find: ‘/etc/sudoers.d’: Permission denied
find: ‘/dev/mqueue’: Permission denied
find: ‘/dev/shm’: Permission denied
find: ‘/tmp’: Permission denied
find: ‘/snap’: Permission denied
find: ‘/lost+found’: Permission denied
find: ‘/run/chrony’: Permission denied
find: ‘/run/user/11018’: Permission denied
find: ‘/run/user/11026’: Permission denied
find: ‘/run/user/11028’: Permission denied
find: ‘/run/user/11002’: Permission denied
find: ‘/run/user/8004’: Permission denied
find: ‘/run/user/11031’: Permission denied
find: ‘/run/user/11010’: Permission denied
find: ‘/run/user/11027’: Permission denied
find: ‘/run/user/11011’: Permission denied
find: ‘/run/user/11032’: Permission denied
find: ‘/run/user/11022’: Permission denied
find: ‘/run/user/11017’: Permission denied
find: ‘/run/user/11007’: Permission denied
find: ‘/run/user/11030’: Permission denied
find: ‘/run/user/11019’: Permission denied
find: ‘/run/user/11023’: Permission denied
find: ‘/run/user/11015’: Permission denied
find: ‘/run/user/11009’: Permission denied
find: ‘/run/user/11025’: Permission denied
find: ‘/run/user/11003’: Permission denied
find: ‘/run/user/11001’: Permission denied
find: ‘/run/user/11020’: Permission denied
find: ‘/run/user/11014’: Permission denied
find: ‘/run/user/11006/systemd/inaccessible/dir’: Permission denied
find: ‘/run/user/11008’: Permission denied
find: ‘/run/user/11016’: Permission denied
find: ‘/run/user/11013’: Permission denied
find: ‘/run/user/11000’: Permission denied
find: ‘/run/user/11005’: Permission denied
find: ‘/run/user/11024’: Permission denied
find: ‘/run/user/11012’: Permission denied
find: ‘/run/user/11004’: Permission denied
find: ‘/run/sudo’: Permission denied
find: ‘/run/screen/S-bandit21’: Permission denied
find: ‘/run/screen/S-bandit20’: Permission denied
find: ‘/run/multipath’: Permission denied
find: ‘/run/cryptsetup’: Permission denied
find: ‘/run/lvm’: Permission denied
find: ‘/run/credentials/systemd-sysusers.service’: Permission denied
find: ‘/run/systemd/propagate’: Permission denied
find: ‘/run/systemd/unit-root’: Permission denied
find: ‘/run/systemd/inaccessible/dir’: Permission denied
find: ‘/run/lock/lvm’: Permission denied
find: ‘/root’: Permission denied
find: ‘/sys/kernel/tracing’: Permission denied
find: ‘/sys/kernel/debug’: Permission denied
find: ‘/sys/fs/pstore’: Permission denied
find: ‘/sys/fs/bpf’: Permission denied
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

```

### Comandos

| Comando |  |
| --- | --- |
| ls | -la |
| find | -size (tamaño), -user(usuario), -group (grupo) |
| cat |  |

### CTF

z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

### Level 7 → Level 8

### Problema

The password for the next level is stored in the file **data.txt** next to the word **millionth**

### Solución

```bash
bandit7@bandit:~$ bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ grep "millionth" data.txt
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP
bandit7@bandit:~$
```

### Comandos

| Comando |  | utilidad |
| --- | --- | --- |
| grep | grep “palabra” | Busca la palabra ingresada en el archivo que se le pide e imprime el resultado |
| ls |  |  |

### CTF

TESKZC0XvTetK0S9xNwm25STk5iWrBvP

## Level 8 → Level 9

### Problema

### Solución

```bash
bandit8@bandit:~$ sort data.txt | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
bandit8@bandit:~$
```

### Notas

Primero ordenamos el archvio, ya que el comando uniq lo que hace es comparar las palabras con sus vecinas por ejemplo (1← 2 → 3) y en este caso no nos sirve por eso primero lo ordenamos para que los repetidos esten junto y así encontrar la CTF.

### Comandos

| Comandos |  |  |
| --- | --- | --- |
| Sort |  | Ordena el texto de un documento |
| Uniq | -u | Muestra las lineas unicas del documento  |

### CTF

EN632PlfYiZbn3PhVK3XOGSlNInNE00t

## Level 9 → Level 10

### Problema

The password for the next level is stored in the file **data.txt**
in one of the few human-readable strings, preceded by several ‘=’
characters.

### Solución

```bash
bandit9@bandit:~$ strings data.txt | grep '=' | sort | uniq
$Z=_
4========== the#
5P=GnFE
'DN9=5
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
========== is
nd?=
========== password
q=W
&S=(
=^,T,?
=TU%
W=y
X=K,
```

### Notas

busca y muestra líneas que contienen el símbolo "=", las ordena alfabéticamente y elimina líneas duplicadas en la salida.

### Comandos

| Comandos | utilidad |
| --- | --- |
| strings | El comando strings busca y muestra las cadenas de caracteres legibles del archivo. |
| grep | se utiliza para buscar líneas que contengan un patrón específico en un conjunto de datos. En este caso, busca líneas que contienen el símbolo "=” |
| sort | se utiliza para ordenar esas líneas en orden alfabético. |
| uniq | se utiliza para eliminar líneas duplicadas de la salida. |

### CTF

**G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s**