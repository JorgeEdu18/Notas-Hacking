## Level 29 → Level 30

### Problema

There is a git repository at `ssh://bandit29-git@localhost/home/bandit29-git/repo` via the port `2220`. The password for the user `bandit29-git` is the same as for the user `bandit29`.

Clone the repository and find the password for the next level.

### Solición

```bash
bandit29@bandit:/tmp/tmp.KVqRQcDBJG/repo$ ls
code  README.md
bandit29@bandit:/tmp/tmp.KVqRQcDBJG/repo$ git branch -a
* dev
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.KVqRQcDBJG/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

bandit29@bandit:/tmp/tmp.KVqRQcDBJG/repo$
```

### Notas

### CTF

xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS