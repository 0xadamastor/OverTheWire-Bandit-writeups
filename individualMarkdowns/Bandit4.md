### Level Info

>The password for the next level is stored in the only human-readable file in the **inhere** directory.
>Tip: if your terminal is messed up, try the “reset” command.

---

### Commands

```bash
ls
cat ./-file00
file ./*
cat ./-file07
```

![](assets/bandit4/step1.png)

> **Password:** 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

### Explanation

>Most files in the directory are binary.  
>Using file type inspection helps identify the single file containing readable text with the password.

### Into the next!

```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

```bash
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```