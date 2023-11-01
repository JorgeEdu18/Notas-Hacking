# information

## Descripción

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg)

## Solución

Al abrir la imagen 

 

![Untitled](information%207bd5e1846d16438eb1f4de9becb73639/Untitled.png)

A simple vista no se puede observar nada, entonces tenemos que ir a los metadatos de la imagen

![Untitled](information%207bd5e1846d16438eb1f4de9becb73639/Untitled%201.png)

En la licencia se puede observar que esta encriptado a base64, entonces se tiene que desencriptar 

![Untitled](information%207bd5e1846d16438eb1f4de9becb73639/Untitled%202.png)

## CTF

picoCTF{the_m3tadata_1s_modified}