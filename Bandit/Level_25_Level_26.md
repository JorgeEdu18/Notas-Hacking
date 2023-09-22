## Level 25 → Level 26

### Problema

Logging in to bandit26 from bandit25 should be fairly easy…
The shell for user bandit26 is not **/bin/bash**, but something else.
Find out what it is, how it works and how to break out of it.

### Solición

```bash
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost -p2220
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit25/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit25/.ssh/known_hosts).
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|

                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

!!! You are trying to log into this SSH server with a password on port 2220 from localhost.
!!! Connecting from localhost is blocked to conserve resources.
!!! Please log out and log in again.
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ~                                                                      ------------------------
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
Connection to localhost closed.
bandit25@bandit:~$
bandit25@bandit:~$ esi
```

### Notas

### CTF

c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1