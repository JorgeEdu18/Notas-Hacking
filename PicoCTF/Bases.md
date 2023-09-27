## Bases

## Problema

### Description

What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

## Solucion

```bash
jorgechz-picoctf@webshell:~$ echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
l3arn_th3_r0p35jorgechz-picoctf@webshell:~$
```

## Notas

Utilizamos eso para convertirlo a ascii

## CTF

picoCTF{l3arn_th3_r0p35}