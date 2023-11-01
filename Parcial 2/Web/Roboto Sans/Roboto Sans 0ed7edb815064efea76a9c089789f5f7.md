# Roboto Sans

## Descripción

The flag is somewhere on this web application not necessarily on the website. Find it.
Check [this](http://saturn.picoctf.net:59901/) out.

## Solución

Por el nombre del reto, podemos pensar que se trata de buscar en el archivo robots.txt, entonces en el path agregamos la ruta de robots.txt

![Untitled](Roboto%20Sans%200ed7edb815064efea76a9c089789f5f7/Untitled.png)

Probamos cada una de ellas y al parecer no nos deja, pero en `anMvbXlmaWxlLnR4dA==` podemos observar que esta codificado por base 64. 

![Untitled](Roboto%20Sans%200ed7edb815064efea76a9c089789f5f7/Untitled%201.png)

Al descodificarla y agregarla al path nos aparece la bandera

![Untitled](Roboto%20Sans%200ed7edb815064efea76a9c089789f5f7/Untitled%202.png)

## CTF

`picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}`