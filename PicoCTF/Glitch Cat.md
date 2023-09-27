## **Glitch Cat**

## Description

Our flag printing service has started glitching!
`$ nc saturn.picoctf.net 49700`

## Solucion

```bash
jorgechz-picoctf@webshell:~$ nc saturn.picoctf.net 49700
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
jorgechz-picoctf@webshell:~$ nano archivo.py
jorgechz-picoctf@webshell:~$ python archivo.py 
picoCTF{gl17ch_m3_n07_a4392d2e}
jorgechz-picoctf@webshell:~$
```

```bash
jorgechz-picoctf@webshell:~$ cat archivo.py 
print('picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}')
```

## CTF

picoCTF{5tRIng5_1T_827aee91}