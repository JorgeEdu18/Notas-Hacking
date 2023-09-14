## Level 20 → Level 21

### Problema

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from
the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

**NOTE:** Try connecting to your own network daemon to see if it works as you think

### Solición

```bash
bandit20@bandit:~$ nc -lnvp 2020 <<<VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[5] 2485623
bandit20@bandit:~$ Listening on 0.0.0.0 2020
bandit20@bandit:~$ ./suconnect 2020
Connection received on 127.0.0.1 54126
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
[2]   Done                    nc -lnvp 2020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit20@bandit:~$
```

### Notas

`nc -lnvp 2020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &`: Este comando inicia un servidor de escucha en el puerto 2020 usando `nc` (netcat). `nc`
 es una utilidad que permite la comunicación a través de redes 
utilizando TCP o UDP. En este caso, se usa para escuchar conexiones en 
el puerto 2020. La entrada `<<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT` redirige el contenido

`Listening on 0.0.0.0 2020`: Este mensaje indica que el servidor de escucha de `nc` está esperando conexiones en todas las interfaces de red (0.0.0.0) en el puerto 2020.

`./suconnect 2020`: Este comando ejecuta un programa llamado "suconnect" con el argumento "2020". Es probable que "suconnect" sea un programa diseñado para conectarse al servidor de escucha que se inició en el paso 1 que al final es concetado con el purto ip.

Despues este valida la contraseña enviada y nos envia la ctf

### CTF

NvEJF7oVjkddltPSrdKEFOllh9V1IBcq