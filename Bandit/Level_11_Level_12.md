## Level 11 → Level 12

### Problema

The password for the next level is stored in the file **data.txt**,
where all lowercase (a-z) and uppercase (A-Z) letters have been
rotated by 13 positions

### Solución

```bash
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ echo data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
qngn.gkg
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
bandit11@bandit:~$
```

### Notas

La parte clave aquí es la especificación de los conjuntos de caracteres `'A-Za-z'` y `'N-ZA-Mn-za-m'`, que indica que se deben rotar las letras del alfabeto tanto en mayúsculas como en minúsculas.

### Comandos

| Comandos | Funcion |
| --- | --- |
| tr | para realizar una rotación de caracteres aplicando una transformación de caracteres. |
|  |  |

### CTF

JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv