# GDB Test Drive

## Descripción

## Solución

Para superar este desafío, una vez que hayamos descargado el archivo, necesitamos asegurarnos de tener la librería gdb instalada.

Si ya está instalada, nos movemos al directorio donde se encuentra nuestro archivo y ejecutamos los comandos siguientes:
chmod +x gdbme
gdb gdbme
layout asm

Después de ejecutar los comandos mencionados anteriormente, se abrirá una nueva ventana que mostrará instrucciones del lenguaje ensamblador. Posteriormente, solo necesitamos seguir y aplicar dichas instrucciones.

break *(main+99)
run
jump *(main+104)

Cuando ejecutemos la última instrucción, obtendremos la bandera.

![Untitled](GDB%20Test%20Drive%20090e5f17ead34f99953abe4a6db97cd9/Untitled.png)

![Untitled](GDB%20Test%20Drive%20090e5f17ead34f99953abe4a6db97cd9/Untitled%201.png)

## CTF