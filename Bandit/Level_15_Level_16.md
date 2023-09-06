## Level 15 → Level 16

### Problema

The password for the next level can be retrieved by submitting the
password of the current level to **port 30001 on localhost** using
SSL encryption.

**Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use
-ign_eof and read the “CONNECTED COMMANDS” section in the manpage.
Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of
that command…**

### Solución

```bash
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Sep  4 12:14:45 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Sep  4 12:14:45 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Sep  4 12:13:45 2023 GMT; NotAfter: Sep  4 12:14:45 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEaLIudTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwOTA0MTIxMzQ1WhcNMjMwOTA0MTIxNDQ1WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCF
+mP3zN+Ram8UNNof21AqNndx5waTj2NICyDAutLp8KDlB7Z6eEqcakkGariHZEhg
ykgX0W/nxUWANwf+HbSc/l1nLJAeDAQYDI1N1ZJcVd0FxYKzD4TDtENCvYttBMip
UR6U6mpiOatNmTG1emvavkIm1iz1gv2HqrvsuJEW7lNQGfy6wuJhNWpXYkyQiaNx
Wnt418/9oI9eBdFKyCGPGEFbXpZvL0VHag3SbbdLfM2BqFDEmIWg4037tot2XY6Y
e1jsxW2dUG5jZkm9QEu2qNI23w1Jxny9ySH34CCZMKKtaoIWl/vnN6hHuAkr2SFT
i/UAo+hsKfDU1An4fjhxAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQA4
qEQlapkw1pYmuMR+Yid+HZdAmgMj0ETNClfAIFBmnRLxLLpO60f4K9fdlwr00Q/O
f/O+Z9xpM89jsBxyVUM05RIZjxXMEXxCbDagdB6Fwm+Hr8p1I709K1dkqp+YR2FE
r+X40mASrwD+6EpCwLRJrUNcT6fSGM672v5SXwdTo+zEJGmTg1cYuWC43nM4tm/W
NLCzMWbehWkXETa/q+nJKgoXcfhD655Mfh2RPy58yZaxxoKQy3U2k1PNcWYZn4mg
x5TngUyB3JJuVr24iwGQNY5qg9UI/DkKnMB9AEDMpnwBmyMWs8C5WGzTYrM4IFA+
5p/INsJEfUlU2ipU7c2Y
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: F3CF114449672F336E0C2CE73FA02C9B0A5C360532B59EB61E7FD67920E6BF49
    Session-ID-ctx:
    Resumption PSK: 092A0B44B89A46C6E3BBB72DB699B3983ED558AE433BFB7BED8BE6538E21814135030FC79796A4D2E40D08F67BE42AA8
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 0c 19 fd a8 fe 26 7c 2f-60 95 f8 b3 b2 75 e0 c7   .....&|/`....u..
    0010 - c4 98 a3 f6 11 18 a9 96-1d 3f 01 72 59 31 25 eb   .........?.rY1%.
    0020 - 61 f7 f2 06 c0 d3 36 85-21 02 06 63 a6 4f ed 81   a.....6.!..c.O..
    0030 - b1 12 ec 4e f5 6a 2e 6d-48 b1 05 fa 84 7a f1 1a   ...N.j.mH....z..
    0040 - b2 ed ff 1d 1f ca b2 ad-13 cd db 47 1c a1 40 b9   ...........G..@.
    0050 - d6 f3 bc 5d bb 88 91 64-ae a9 3d cc c6 5b 57 01   ...]...d..=..[W.
    0060 - 6a bf 2f 1e 95 9f c4 f9-77 6f cc 5d df dc d6 27   j./.....wo.]...'
    0070 - 64 14 e7 7c a9 89 a5 85-c2 bf e8 34 81 fe ba 13   d..|.......4....
    0080 - 42 a1 ee a6 4a 7b 60 6b-dc c5 82 34 c0 98 9c 34   B...J{`k...4...4
    0090 - a4 86 97 d0 0c 0c 73 53-e6 c7 7a 4b 92 b8 87 d5   ......sS..zK....
    00a0 - fd 3d 15 13 06 f1 c7 e7-c4 e1 fe 81 51 c0 fd 57   .=..........Q..W
    00b0 - 49 89 71 da 99 bb 2a f4-ee 92 dc 46 35 ed 79 12   I.q...*....F5.y.
    00c0 - d6 49 f7 c4 67 55 a1 f2-57 af 27 45 97 bc c3 10   .I..gU..W.'E....

    Start Time: 1693860349
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: D5C24809EFAABA5FDDAB7D1D8ED257224AF73A0C9D373939546826F8310C5006
    Session-ID-ctx:
    Resumption PSK: 228B83006CCBDD932E2B5EF8D8E6BA5FF076A49DA391FDCB45E0FF3683A385F460C1BF4DE0D80595E285E91FBEE7C4BD
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 0c 19 fd a8 fe 26 7c 2f-60 95 f8 b3 b2 75 e0 c7   .....&|/`....u..
    0010 - 45 50 8c 1e d3 9b 79 3a-e0 83 02 0c 70 e0 21 5b   EP....y:....p.![
    0020 - ed 26 8f 0b b9 f6 f9 7f-be 75 48 90 17 84 d7 4a   .&.......uH....J
    0030 - a8 36 54 76 57 24 8c 8b-e4 0e 03 97 9f 71 d8 f2   .6TvW$.......q..
    0040 - 9a ed 47 d4 6b 96 a8 30-eb 13 86 31 56 84 f0 1c   ..G.k..0...1V...
    0050 - e3 69 3b e5 ca 9b 55 06-bc e0 69 eb 58 35 3b 12   .i;...U...i.X5;.
    0060 - 39 6b 98 35 ef 7d e8 6d-36 51 d8 cb a7 8b 18 78   9k.5.}.m6Q.....x
    0070 - 0b a6 3c 2f 20 c2 ae b4-79 63 ac 2c f2 23 2a f8   ..</ ...yc.,.#*.
    0080 - 61 2a 11 30 ea 74 4e d7-80 dc c4 0e 77 92 4b 77   a*.0.tN.....w.Kw
    0090 - 51 2b b1 e5 2d 43 b5 10-8f 7d 4b 07 8e 5f f5 01   Q+..-C...}K.._..
    00a0 - dd 0f f2 05 cc 09 73 55-18 0e 80 20 e9 15 d3 e6   ......sU... ....
    00b0 - e6 04 83 3e cd ad b2 28-61 76 aa bd 33 6d ff 58   ...>...(av..3m.X
    00c0 - 25 e6 1a 10 a4 6d ed a5-d5 91 12 25 8f 8a f3 85   %....m.....%....

    Start Time: 1693860349
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
bandit15@bandit:~$
```

### Notas

Para conectarte a un servicio en tu localhost a través de SSL (Secure Sockets Layer) o TLS (Transport Layer Security), puedes utilizar el comando `openssl s_client`.

Aparecerá una serie de detalles sobre el certificado SSL/TLS del servidor, como la cadena de certificados y la información del certificado. Puedes examinar esta información para verificar la autenticidad del servidor.

Si la conexión se establece correctamente y el certificado es válido, podrás comenzar a interactuar con el servidor SSL/TLS. Por ejemplo, en el caso de un servidor web HTTPS, puedes enviar solicitudes HTTP como si estuvieras usando un navegador web.

### Comandos

| Comandos | Funcionalidad |
| --- | --- |
| openssl s_client | Para conectarte a un servicio en tu localhost a través de SSL |
|  |  |

### CTF

JQttfApK4SeyHwDlI9SXGR50qclOAil1