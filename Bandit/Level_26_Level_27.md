## Level 26 → Level 27

### Problema

Good job getting a shell! Now hurry and grab the password for bandit27!

### Solición

```bash
_                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
~                                                                                                                                                                                                                  ~                                                                                                                                                                                                                  ~                                                                                                                                                                                                                  ~                                                                                                                                                                                                                  ~                                                                      _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
~                                                                                  ~                                                                                  ~                                                                                  ~                                                                                  ~                                                                                  ~                                                                                  ~                                                                                  ~                                                                                  :shell
bandit26@bandit:~$ ls                                           1,3           All
bandit27-do  text.txt
bandit26@bandit:~$ bandit27-do id
bandit27-do: command not found
bandit26@bandit:~$ ./bandit27-do id
uid=11026(bandit26) gid=11026(bandit26) euid=11027(bandit27) groups=11026(bandit26)
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS                        ~
bandit26@bandit:~$
```

### Notas

### CTF

YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS