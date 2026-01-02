### Level Info

>The password for the next level is stored in a file called **"-"** located in the home directory
---
### Commands

```bash
cat ./-
```

![](assets/bandit1/step1.png)

> **Password:** 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

### Explanation

>The file is literally named **`-`**, but in Linux `-` usually means **standard input (stdin)**.
> Using **`./-`** forces the system to treat it as a **filename**.

### Into the next!

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

```bash
263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```