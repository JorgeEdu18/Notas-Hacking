## Level 19 → Level 20

### Problema

The password for the next level is stored in a file **readme** in
the homedirectory. Unfortunately, someone has modified **.bashrc**
to log you out when you log in with SSH

### Solición

```bash
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit19@bandit:~$
```

### Notas

1. `./bandit20-do`: Ejecuta el programa "./bandit20-do", que parece ser una utilidad diseñada para ejecutar comandos como el usuario "bandit20". Cuando se ejecuta sin argumentos, muestra un mensaje de ejemplo de cómo se debe usar.
2. `./bandit20-do id`: Ejecuta el comando "id" como el usuario "bandit20" utilizando "./bandit20-do". El resultado muestra la información de identidad del usuario "bandit19" y el cambio temporal a "euid=11020(bandit20)".
3. `./bandit20-do cat /etc/bandit_pass/bandit20`: Utiliza "./bandit20-do" para ejecutar el comando "cat /etc/bandit_pass/bandit20" como el usuario "bandit20". Esto permite a "bandit19" leer el contenido del archivo "/etc/bandit_pass/bandit20", que es la contraseña del nivel 20.
4. El resultado del tercer comando muestra la contraseña del siguiente nivel: "VxCazJaVykI6W36BkBU0mJTCM8rR95XT".

### CTF

VxCazJaVykI6W36BkBU0mJTCM8rR95XT