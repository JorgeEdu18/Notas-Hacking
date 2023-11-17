# reverse_cipher

## Descripción

We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev_this). Can you reverse the flag.

## Solución

Vamos a utilizar a la aplicación

![Untitled](reverse_cipher%208ae4abbc27e24c0fbe75ea0b42ab26df/Untitled.png)

![Untitled](reverse_cipher%208ae4abbc27e24c0fbe75ea0b42ab26df/Untitled%201.png)

Cambiamos la variable local_20 por flagfile

local_28 → flagrev

local_50 → flag

local_10 → i

local_9 → rev

![Untitled](reverse_cipher%208ae4abbc27e24c0fbe75ea0b42ab26df/Untitled%202.png)

```python
cifrado = open('rev_this','r').read()
print(cifrado)

flag=''
for i in range(8, len(cifrado)-1):
			if i & 1 == 0
					flag += chr(ord(cifrado[i])-5)
			else:
					flag += chr(ord(cifrado[i]+2)
print(flag)
```

## CTF

![Untitled](reverse_cipher%208ae4abbc27e24c0fbe75ea0b42ab26df/Untitled%203.png)