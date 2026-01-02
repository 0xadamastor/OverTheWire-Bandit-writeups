### Level Info

>The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

---

### Commands

```bash
strings data.txt | grep "="
```

![](assets/bandit9/step1.png)

> **Password:** FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

### Explanation

>The file contains binary data with a few human‑readable strings.  
>The `strings` command extracts readable text, and `grep "="` filters the lines preceded by `=` to reveal the password.

### Into the next!

```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
```

```bash
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```