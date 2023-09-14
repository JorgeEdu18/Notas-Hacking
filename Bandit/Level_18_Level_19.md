## Level 18 → Level 19

### Problema

The password for the next level is stored in a file **readme** in
the homedirectory. Unfortunately, someone has modified **.bashrc**
to log you out when you log in with SSH

### Solición

```bash
C:\Users\Jorge>ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/cat readme
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|

                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
awhqfNnAbc1naukrpqDYcF95h7HoMTrC

C:\Users\Jorge>
```

### Notas

En este nivel al no poder ingresar de forma correcta ya que tenia un script en el bash el cual no nos permitia entrar, insertamos /bi/cat readme esto para que podamos leer el readme y poder extraer la contraseña

### CTF

awhqfNnAbc1naukrpqDYcF95h7HoMTrC