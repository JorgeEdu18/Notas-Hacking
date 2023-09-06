## Level 14 → Level 15

### Problema

The password for the next level can be retrieved by submitting the
password of the current level to **port 30000 on localhost**.

### Solución

```bash
bandit14@bandit:~$ ls
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.

Wrong! Please enter the correct current password
Connection closed by foreign host.
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

Connection closed by foreign host.
bandit14@bandit:~$
```

### Notas

Se ejecuto `telnet localhost 30000` para conectarte a tu localhost en el puerto 30000. Esto inicia una conexión a un servicio que está escuchando en ese puerto en tu propia máquina.

### Comandos

| Comandos | Funcion |
| --- | --- |
| Telnet http://localhost -puerto | Puedes reemplazar "puerto" con el número de puerto al que deseas conectarte en el localhost. Por ejemplo, si deseas conectarte al puerto 80 (HTTP), puedes ejecutar: |
|  |  |

### CTF

jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt