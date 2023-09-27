## RUNMEPY

## Description

Run the `runme.py` script to get the flag. Download the script with your
browser or with `wget` in the webshell.
[Download runme.py Python script](https://artifacts.picoctf.net/c/34/runme.py)

## Solucion

```bash
jorgechz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/34/runme.py
--2023-09-27 15:13:02--  https://artifacts.picoctf.net/c/34/runme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.18, 3.160.5.71, 3.160.5.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'runme.py.3'

runme.py.3            100%[=======================>]     270  --.-KB/s    in 0s      

2023-09-27 15:13:02 (2.92 MB/s) - 'runme.py.3' saved [270/270]

jorgechz-picoctf@webshell:~$ ls
README.txt  runme.py  runme.py.1  runme.py.2  runme.py.3
jorgechz-picoctf@webshell:~$ python runme.py
picoCTF{run_s4n1ty_run}
```

## CTF

picoCTF{run_s4n1ty_run}