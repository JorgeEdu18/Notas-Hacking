## **Client-side-again**

## Problema

### Description

Can you break into this super secure portal? `https://jupiter.challenges.picoctf.org/problem/56816/` ([link](https://jupiter.challenges.picoctf.org/problem/56816/)) or http://jupiter.challenges.picoctf.org:56816

## Solucion

```sql
'use strict';
/** @type {!Array} */
var _0x5a46 = ["37115}", "_again_3", "this", "Password Verified", "Incorrect password", "getElementById", "value", "substring", "picoCTF{", "not_this"];
(function(data, i) {
  /**
   * @param {number} isLE
   * @return {undefined}
   */
  var write = function(isLE) {
    for (; --isLE;) {
      data["push"](data["shift"]());
    }
  };
  write(++i);
})(_0x5a46, 435);
/**
 * @param {string} level
 * @param {?} ai_test
 * @return {?}
 */
var _0x4b5b = function(level, ai_test) {
  /** @type {number} */
  level = level - 0;
  var rowsOfColumns = _0x5a46[level];
  return rowsOfColumns;
};
/**
 * @return {undefined}
 */
function verify() {
  checkpass = document[_0x4b5b("0x0")]("pass")[_0x4b5b("0x1")];
  /** @type {number} */
  split = 4;
  if (checkpass[_0x4b5b("0x2")](0, split * 2) == _0x4b5b("0x3")) {
    if (checkpass[_0x4b5b("0x2")](7, 9) == "{n") {
      if (checkpass[_0x4b5b("0x2")](split * 2, split * 2 * 2) == _0x4b5b("0x4")) {
        if (checkpass[_0x4b5b("0x2")](3, 6) == "oCT") {
          if (checkpass[_0x4b5b("0x2")](split * 3 * 2, split * 4 * 2) == _0x4b5b("0x5")) {
            if (checkpass["substring"](6, 11) == "F{not") {
              if (checkpass[_0x4b5b("0x2")](split * 2 * 2, split * 3 * 2) == _0x4b5b("0x6")) {
                if (checkpass[_0x4b5b("0x2")](12, 16) == _0x4b5b("0x7")) {
                  alert(_0x4b5b("0x8"));
                }
              }
            }
          }
        }
      }
    }
  } else {
    alert(_0x4b5b("0x9"));
  }
}
;
```

En la terminal del navegador escribimos lo siguiente

```sql
_0x4b5b("0x1")
"value"
_0x4b5b("0x2")
"substring"
_0x4b5b("0x3")
"picoCTF{"
_0x4b5b("0x4")
"not_this"
_0x4b5b("0x5")
"37115}"
_0x4b5b("0x6")
"_again_3"
_0x4b5b("0x7")
"this"
_0x4b5b("0x8")
"Password Verified"
_0x4b5b("0x9")
"Incorrect password"
_0x4b5b("0x0")
"getElementById"
```

Y este nos da la conversion, y esto los tenemos que remplazar

```sql
function verify() {
  checkpass = document[("getElementById")]("pass")[("value")];
  /** @type {number} */
  split = 4;
  if (checkpass["substring"](0, split * 2) == ("picoCTF{")) {
    if (checkpass[("substring")](7, 9) == "{n") {
      if (checkpass[("substring")](split * 2, split * 2 * 2) == ("not_this")) {
        if (checkpass[("substring")](3, 6) == "oCT") {
          if (checkpass[("substring")](split * 3 * 2, split * 4 * 2) == _04b5b("37115}")) {
            if (checkpass["substring"](6, 11) == "F{not") {
              if (checkpass[("substring")](split * 2 * 2, split * 3 * 2) == ("_again_3")) {
                if (checkpass[("substring")](12, 16) == ("this")) {
                  alert(_04b5b("Password Verified"));
                }
              }
            }
          }
        }
      }
    }
  } else {
    alert(_0x4b5b("Incorrect password"));
  }
}
```

Despues con un codigo python lo podemos resolver:

```sql
text = """
  if (checkpass["substring"](0, split * 2) == "picoCTF{") {
    if (checkpass["substring"](7, 9) == "{n") {
      if (checkpass["substring"](split * 2, split * 2 * 2) == "not_this") {
        if (checkpass["substring"](3, 6) == "oCT") {
          if (checkpass["substring"](split * 3 * 2, split * 4 * 2) == "37115}") {
            if (checkpass["substring"](6, 11) == "F{not") {
                if (checkpass["substring"](12, 16) == "this") {
              if (checkpass["substring"](split * 2 * 2, split * 3 * 2) == "_again_3") {
"""

flag = [None] * 32
split = 4
for line in text.split("\n"):
    line = line.strip()
    if line == "": 
        continue
    line = line.replace('if (checkpass["substring"](', 'flag[').replace(', ', ":").replace(') == ', '] = ').replace(') {', '')
    exec(line)

print ("".join(flag))
```

## CTF

picoCTF{not_this_again_337115}