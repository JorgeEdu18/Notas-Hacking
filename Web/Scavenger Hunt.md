## **Scavenger Hunt**

## Problema

There is some interesting information hidden around this site [http://mercury.picoctf.net:39698/](http://mercury.picoctf.net:39698/). Can you find it?

## Solucion

Tenemos que buscar en los archivos fuentes para encotrar la bandera

![Untitled](Web%20863a3cdab87449c985c1b49358e932e3/Untitled%209.png)

![Untitled](Web%20863a3cdab87449c985c1b49358e932e3/Untitled%2010.png)

En el archivo js nos muestra un mensaje, en el cual podemos deducir que la siguiente parte se va a encontrar en el archivo rorbots.txt. al ingresar ese archivo robots.txt aparece los siguiente

![Untitled](Web%20863a3cdab87449c985c1b49358e932e3/Untitled%2011.png)

En algunas paginas por defecto guardan en un servidor apache algunas configuraciones para acceder a esas configuraciones ponemos el siguiente link .htaccess

![Untitled](Web%20863a3cdab87449c985c1b49358e932e3/Untitled%2012.png)

Nos pide que busquemos en otro sitio [https://en.wikipedia.org/wiki/.DS_Store](https://en.wikipedia.org/wiki/.DS_Store). .DS_store guarda mucha mas informacion

![Untitled](Web%20863a3cdab87449c985c1b49358e932e3/Untitled%2013.png)