## **Magikarp Ground Mission**

## Description

Do you know how to 
move between directories and read files in the shell? Start the 
container, `ssh` to it, and then `ls` once connected to begin. Login via
 `ssh` as `ctf-player` with the password, `a13b7f9d`

| Challenge Endpoints |  |
| --- | --- |
| SSH | ssh ctf-player@venus.picoctf.net -p 57948 |

## Solucion

```bash
jorgechz-picoctf@webshell:~$ ssh ctf-player@venus.picoctf.net -p 57948
ctf-player@venus.picoctf.net's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Mon Sep 25 17:19:34 2023 from 127.0.0.1
ctf-player@pico-chall$
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat 1of3.flag.txt 
picoCTF{xxsh_
ctf-player@pico-chall$
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ cat 2of3.flag.txt 
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$
ctf-player@pico-chall$ ls
2of3.flag.txt  dev   instructions-to-3of3.txt  media  proc  sbin  tmp
bin            etc   lib                       mnt    root  srv   usr
boot           home  lib64                     opt    run   sys   var
ctf-player@pico-chall$ cat instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ cd
ctf-player@pico-chall$ cat 3of3.flag.txt 
71be5264}
ctf-player@pico-chall$
```

## Notas

Utilizamos ssh para entrar, la contraseña es a13b7f9d, despues entramos y buscamos los archivos con el nombre de instructions y seguir las instrucciones

## CTF

picoCTF{xxsh_0ut_0f_\/\/4t3r_71be5264}