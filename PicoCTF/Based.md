## **Based**

## Description

To get truly 1337, you must understand different data encodings, such as
 hexadecimal or binary. Can you get the flag from this program to prove 
you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29221`.

## Solucion

```bash
jorgechz-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 29221
Let us see how data is stored
colorado
Please give the 01100011 01101111 01101100 01101111 01110010 01100001 01100100 01101111 as a word.
...
you have 45 seconds.....

Input:
colorado
Please give me the  163 154 165 144 147 145 as a word.
Input:
Too slow!
^C
jorgechz-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 29221
Let us see how data is stored
lizard
Please give the 01101100 01101001 01111010 01100001 01110010 01100100 as a word.
...
you have 45 seconds.....

Input:
lizard
Please give me the  154 151 172 141 162 144 as a word.
Input:
lizard
Please give me the 736c75646765 as a word.
Input:
sludge
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_00a975ff}
```

## Notas

En esta prueba utilice varias paginas para obtener el resultado.

La primera era convertir de binario a ASCII la pagina que utilice es: https://www.rapidtables.com/convert/number/binary-to-ascii.html

El segundo cifrado es de octal a ASCII, la pagina que use es: http://www.unit-conversion.info/texttools/octal/

El tercero cifrado es de hexadecimal a ASCII, la pagina que use es : https://www.rapidtables.com/convert/number/hex-to-ascii.html

## CTF

Flag: picoCTF{learning_about_converting_values_00a975ff}