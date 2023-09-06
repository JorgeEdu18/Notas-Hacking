## Level 10 → Level 11

### Problema

The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

### Solución

```bash
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ base64 data.txt > data3.txt
-bash: data3.txt: Permission denied
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$
```

### Notas

Utilizamos el comando base64 para que desconvierta el texto 

### Comandos

| Comandos |  |
| --- | --- |
| base64 -d | Decodificación de texto en Base64 |
| cat  | Imprima el texto |

### CTF

6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM