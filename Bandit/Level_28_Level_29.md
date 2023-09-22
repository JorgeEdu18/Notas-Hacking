## Level 28 → Level 29

### Problema

There is a git repository at `ssh://bandit28-git@localhost/home/bandit28-git/repo` via the port `2220`. The password for the user `bandit28-git` is the same as for the user `bandit28`.

Clone the repository and find the password for the next level.

### Solición

```bash
bandit28@bandit:~$ mktemp -d
tmp/tmp.DCkwD5smOS/
bandit28@bandit:~$ cd tmp/tmp.DCkwD5smOS/
bandit28@bandit:/tmp/tmp.DCkwD5smOS/$$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
...
bandit28-git@localhost's password: 
...
bandit28@bandit:/tmp/tmp.lGUWKxK6CU$ ls
repo
bandit28@bandit:/tmp/tmp.lGUWKxK6CU$ cd repo
bandit28@bandit:/tmp/tmp.lGUWKxK6CU/repo$ ls -la
total 16
drwxr-sr-x 3 bandit28 root 4096 Jul  3 12:30 .
drwx--S--- 3 bandit28 root 4096 Jul  3 12:30 ..
drwxr-sr-x 8 bandit28 root 4096 Jul  3 12:30 .git
-rw-r--r-- 1 bandit28 root  111 Jul  3 12:30 README.md
bandit28@bandit:/tmp/tmp.lGUWKxK6CU/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
bandit28@bandit:/tmp/tmp.DCkwD5smOS/repo$ git show 899ba88df296331cc01f30d022c006775d467f28
commit 899ba88df296331cc01f30d022c006775d467f28 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Sun Apr 23 18:04:39 2023 +0000

    fix info leak

diff --git a/README.md b/README.md
index b302105..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials

 - username: bandit29
-- password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S
+- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.DCkwD5smOS/repo$
```

### Notas

Creamos una carpeta temporal y en esa misma copiamos un repositorio para obtener la llave para el siguiente nivel

### CTF

tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S