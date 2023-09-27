## **Codebook**

## Problema

Run the Python script

```
code.py
```

in the same directory as

```
codebook.txt
```

- [Download code.py](https://artifacts.picoctf.net/c/2/code.py)
- [Download codebook.txt](https://artifacts.picoctf.net/c/2/codebook.txt)

## Solucion

```bash
jorgechz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/2/code.py
--2023-09-25 23:33:35--  https://artifacts.picoctf.net/c/2/code.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.71, 3.160.5.42, 3.160.5.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.71|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1278 (1.2K) [application/octet-stream]
Saving to: 'code.py'

code.py               100%[=======================>]   1.25K  --.-KB/s    in 0s      

2023-09-25 23:33:35 (386 MB/s) - 'code.py' saved [1278/1278]

jorgechz-picoctf@webshell:~$ ls
README.txt  code.py
jorgechz-picoctf@webshell:~$ python code.py
Couldn't find codebook.txt. Did you download that file into the same directory as this script?
jorgechz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/2/codebook.txt
--2023-09-25 23:34:31--  https://artifacts.picoctf.net/c/2/codebook.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.18, 3.160.5.71, 3.160.5.93, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27 [application/octet-stream]
Saving to: 'codebook.txt'

codebook.txt          100%[=======================>]      27  --.-KB/s    in 0s      

2023-09-25 23:34:31 (14.6 MB/s) - 'codebook.txt' saved [27/27]

jorgechz-picoctf@webshell:~$ ls
README.txt  code.py  codebook.txt
jorgechz-picoctf@webshell:~$ cat codebook.txt 
azbycxdwevfugthsirjqkplomn
jorgechz-picoctf@webshell:~$ python code.py
picoCTF{c0d3b00k_455157_7d102d7a}
```

## Notas

## CTF

picoCTF{c0d3b00k_455157_7d102d7a}