## **plumbing**

## Description

Sometimes you need to handle process data outside of a file. Can you 
find a way to keep the output from this program and search for the flag?
 Connect to `jupiter.challenges.picoctf.org 7480`.

## Solucion

```bash
jorgechz-picoctf@webshell:~$ ls
README.txt
jorgechz-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 7480 >> archivo.txt
^Z
[1]+  Stopped                 nc jupiter.challenges.picoctf.org 7480 >> archivo.txt
jorgechz-picoctf@webshell:~$ ls
README.txt  archivo.txt
jorgechz-picoctf@webshell:~$ grep "pico" archivo.txt 
picoCTF{digital_plumb3r_06e9d954}
jorgechz-picoctf@webshell:~$
```

## CTF

picoCTF{digital_plumb3r_06e9d954}