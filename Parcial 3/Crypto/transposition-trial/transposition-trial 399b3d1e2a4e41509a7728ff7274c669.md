# transposition-trial

## Descripción

Our data got 
corrupted on the way here. Luckily, nothing got replaced, but every 
block of 3 got scrambled around! The first word seems to be three 
letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message [here](https://artifacts.picoctf.net/c/193/message.txt).

## Solución

```python
with open("message.txt") as fl:
    contenido = fl.read()

for i in range(0, len(contenido),3):
    chunk = contenido[i:i+3]
    a,b,c = chunk
    print(c + a + b, end="" )
```

## CTF

The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}