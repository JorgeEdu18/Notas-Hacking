## **PW Crack 3**

## Description

Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/18/level3.py) and you'll
need the encrypted [flag](https://artifacts.picoctf.net/c/18/level3.flag.txt.enc) and the
[hash](https://artifacts.picoctf.net/c/18/level3.hash.bin) in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by
examining the password checker script.

## Solucion

```bash
jorgechz-picoctf@webshell:~$ nano level3.py 
jorgechz-picoctf@webshell:~$ python level3.py 
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_6f98a49f}
jorgechz-picoctf@webshell:~$ cat level3.py 
import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_3_pw_check():
   for user_pw in ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]:
       user_pw_hash = hash_pw(user_pw)

       if user_pw_hash == correct_pw_hash:
          print("Welcome back... your flag, user:")
          decryption = str_xor(flag_enc.decode(), user_pw)
          print(decryption)
          return

level_3_pw_check()

# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

jorgechz-picoctf@webshell:~$
```

Modificamos el archivo [level3.py](http://level3.py). Utilizamos un ciclo for para que este pase los datos de la lista hasta que valide el correcto y a partir de eso nos pasa la bandera

## CTF

picoCTF{m45h_fl1ng1ng_6f98a49f}