## **Wave a flag**

## Problema

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm) has extraordinarily helpful information...

## Solucion

```bash
jorgechz-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm
--2023-09-25 16:45:34--  https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm
Resolving [mercury.picoctf.net](http://mercury.picoctf.net/) ([mercury.picoctf.net](http://mercury.picoctf.net/))... 18.189.209.142
Connecting to [mercury.picoctf.net](http://mercury.picoctf.net/) ([mercury.picoctf.net](http://mercury.picoctf.net/))|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10936 (11K) [application/octet-stream]
Saving to: 'warm.1'

warm.1                100%[=======================>]  10.68K  --.-KB/s    in 0s

2023-09-25 16:45:34 (292 MB/s) - 'warm.1' saved [10936/10936]

jorgechz-picoctf@webshell:~$ ls
README.txt  flag  flag.1  warm  warm.1
jorgechz-picoctf@webshell:~$ chmod x+ warm
chmod: invalid mode: 'x+'
Try 'chmod --help' for more information.
jorgechz-picoctf@webshell:~$ chmod +x warm
jorgechz-picoctf@webshell:~$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}
jorgechz-picoctf@webshell:~$
```

## CTF

picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}