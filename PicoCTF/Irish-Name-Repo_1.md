## **Irish-Name-Repo 1**

## Problema

There is a website running at `https://jupiter.challenges.picoctf.org/problem/33850/` ([link](https://jupiter.challenges.picoctf.org/problem/33850/)) or http://jupiter.challenges.picoctf.org:33850. Do you think you can log us in? Try to see if you can login!

## Solucion

En este caso utilizamos inyeccion SQL primero tenemos que entrar a inspecciones y poner 1 en debug

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/60379833-0249-4197-949e-08a049895cd7/c5a4f7ac-a3f5-41e5-8423-ed4d3e0b4a82/Untitled.png)

Despues en el login ponemos lo siguiente ‘or ‘1’=’1 en los dos campos en 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/60379833-0249-4197-949e-08a049895cd7/63df04ec-ed05-4080-9b45-d88a41e2d25b/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/60379833-0249-4197-949e-08a049895cd7/12b2796e-231a-4e10-8985-3cf7214e95f3/Untitled.png)

## CTF

picoCTF{s0m3_SQL_f8adf3fb}