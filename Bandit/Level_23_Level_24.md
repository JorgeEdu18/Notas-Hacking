## Level 23 → Level 24

### Problema

A program is running automatically at regular intervals from
**cron**, the time-based job scheduler. Look in **/etc/cron.d/** for
the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first
shell-script. This is a very big step and you should be proud of
yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once
executed, so you may want to keep a copy around…

### Solición

```bash
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat bandit24 /usr/bin/cronjob_bandit24.sh
cat: bandit24: No such file or directory
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo || exit 1
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -rf ./$i
    fi
done

bandit23@bandit:~$ mkdir /tmp/kd
mkdir: cannot create directory ‘/tmp/kd’: File exists
bandit23@bandit:~$ ls /tmp/
ls: cannot open directory '/tmp/': Permission denied
bandit23@bandit:~$ ls /tmp/kd
password  script.sh
bandit23@bandit:~$ cd /tmp/kd
bandit23@bandit:/tmp/kd$ ls
password  script.sh
bandit23@bandit:/tmp/kd$ cat password
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
```

### Notas
La contraseña se encutra en una carpeta temporal

### CTF

VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar