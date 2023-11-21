# Bit-O-Asm-2

## Descripción

Can you figure out what is in the `eax` register? Put your answer in the
picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax`
register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.
Download the assembly dump [here](https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt).

## Solucion

```python
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret

Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print(int("0x9fe1a",16))
654874
>>>
```

## CTF

picoCTF{654874}