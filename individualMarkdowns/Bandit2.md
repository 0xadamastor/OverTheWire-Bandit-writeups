### Level Info

>The password for the next level is stored in a file called **-** located in the home directory
---
### Commands

```bash
cat -- "--spaces in this filename--"
```

![](assets/bandit2/step1.png)

> **Password:** MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

### Explanation

>The filename contains spaces, so it must be quoted.
> Since it also starts with `--`, the `--` argument is required to stop option parsing.

### Into the next!

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

```bash
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```