## Level 12 → Level 13

### Problema

The password for the next level is stored in the file **data.txt**,
which is a hexdump of a file that has been repeatedly compressed.
For this level it may be useful to create a directory under /tmp in
which you can work using mkdir. For example: mkdir /tmp/myname123.
Then copy the datafile using cp, and rename it using mv (read the
manpages!)

### Solucion

```bash
bandit12@bandit:~$ ls -man
total 24
drwxr-xr-x  2     0     0 4096 Apr 23 18:04 .
drwxr-xr-x 70     0     0 4096 Apr 23 18:05 ..
-rw-r--r--  1     0     0  220 Jan  6  2022 .bash_logout
-rw-r--r--  1     0     0 3771 Jan  6  2022 .bashrc
-rw-r-----  1 11013 11012 2642 Apr 23 18:04 data.txt
-rw-r--r--  1     0     0  807 Jan  6  2022 .profile
bandit12@bandit:~$ xxd -r data.txt | file -
/dev/stdin: gzip compressed data, was "data2.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat | file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat |file -
/dev/stdin: gzip compressed data, was "data4.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar x0 | file -
tar: Options '-[0-7][lmh]' not supported by *this* tar
Try 'tar --help' or 'tar --usage' for more information.
/dev/stdin: empty
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO |file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | file -
/dev/stdin: gzip compressed data, was "data9.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat | file -
/dev/stdin: ASCII text
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat |
> ^C
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```

### Notas

Para este CTF estuvo más complicado, ya que primero se tiene que convertir el contenido del texto de hexadecimal en binario, despues descomprimir el archivo, despues descomprimirlo, este es un bucle muy complejo.

### Comandos

| Comandos | Funcion |
| --- | --- |
| xxd -r data.txt | file - | se utiliza para convertir datos hexadecimales en binarios. Aquí, se está tomando el contenido del archivo "data.txt" en formato hexadecimal y se revierte a su forma binaria original. |
| xxd -r data.txt | zcat | file - | se revierte el contenido hexadecimal del archivo "data.txt" y luego se utiliza el comando zcat para descomprimir el archivo. |
| xxd -r data.txt | zcat | bzcat | file - | El contenido hexadecimal se revierte, se descomprime primero con zcat, luego con bzcat, |
| xxd -r data.txt | zcat | bzcat | zcat | file - | : El contenido hexadecimal se revierte y pasa por una serie de descompresiones con zcat y bzcat, y finalmente se utiliza file para determinar el tipo de archivo. |
| xxd -r data.txt | zcat | bzcat | zcat | tar x0 | file - | Se intenta extraer el contenido del archivo con tar x0, pero se produce un error ya que la opción -0 no es compatible con tar. Sin embargo, el comando file aún se utiliza para determinar el tipo de archivo del resultado, que en este caso es "empty" (vacío). |
| xxd -r data.txt | zcat | bzcat | zcat | tar xO | file - | Similar al paso 4, pero se utiliza tar xO en lugar de tar x0 para extraer el contenido del archivo sin errores. El comando file se utiliza para determinar el tipo de archivo del resultado, que en este caso es un archivo "tar". |
| xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO |file - | El contenido extraído se pasa nuevamente por dos comandos tar xO, lo que indica que se están extrayendo archivos dentro de archivos. El comando file se utiliza para determinar el tipo de archivo del resultado, que en este caso es un archivo comprimido con bzip2. |
| xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | file - | El contenido extraído se pasa nuevamente por bzcat, que descomprime aún más. Luego, se utiliza file para determinar el tipo de archivo del resultado, que en este caso es un archivo "tar". |
| xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | file - | El contenido extraído se pasa nuevamente por tar xO, lo que indica que se están extrayendo más archivos. El comando file se utiliza para determinar el tipo de archivo del resultado, que en este caso es un archivo comprimido con gzip. |
| xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat | file - | El contenido extraído se pasa nuevamente por zcat, lo que indica que se está extrayendo un archivo final. El comando file se utiliza para determinar el tipo de archivo del resultado, que en este caso es un archivo de texto ASCII. |

### CTF

wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw