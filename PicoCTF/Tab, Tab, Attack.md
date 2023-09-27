## **Tab, Tab, Attack**

## Problema

Using tabcomplete in the Terminal will add years to your life, esp. when
 dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/9689f2b453ad5daeb73ca7534e4d1521/Addadshashanammu.zip)

## Solucion

```bash
jorgechz-picoctf@webshell:~$ ls
Addadshashanammu.zip  README.txt  flag  ltdis.sh  static  warm
jorgechz-picoctf@webshell:~$ chmod +x Addadshashanammu.zip 
jorgechz-picoctf@webshell:~$ unzip Addadshashanammu.zip 
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
jorgechz-picoctf@webshell:~$ ls
Addadshashanammu  Addadshashanammu.zip  README.txt  flag  ltdis.sh  static  warm
jorgechz-picoctf@webshell:~$ cd Addadshashanammu/
jorgechz-picoctf@webshell:~/Addadshashanammu$ ls
Almurbalarammi
jorgechz-picoctf@webshell:~/Addadshashanammu$ cd Almurbalarammi/
jorgechz-picoctf@webshell:~/Addadshashanammu/Almurbalarammi$ ls
Ashalmimilkala
jorgechz-picoctf@webshell:~/Addadshashanammu/Almurbalarammi$ cd Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
jorgechz-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabita
shpi/Maelkashishi/Onnissiralis/Ularradallaku$ ls
fang-of-haynekhtnamet
jorgechz-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabita
shpi/Maelkashishi/Onnissiralis/Ularradallaku$ strings fang-of-haynekhtnamet | grep "pico"
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_2bcfb2ab}
jorgechz-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabita
shpi/Maelkashishi/Onnissiralis/Ularradallaku$
```

## CTF

picoCTF{l3v3l_up!_t4k3_4_r35t!_2bcfb2ab}