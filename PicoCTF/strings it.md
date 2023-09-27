## **strings it**

## Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings) without running it?

## Solucion

```bash
jorgechz-picoctf@webshell:~$ ls
README.txt  strings
jorgechz-picoctf@webshell:~$ strings strings | grep pico
picoCTF{5tRIng5_1T_827aee91}
jorgechz-picoctf@webshell:~$
```

## CTF

picoCTF{5tRIng5_1T_827aee91}