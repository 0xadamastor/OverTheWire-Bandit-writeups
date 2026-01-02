### Level Info

>After all this `git` stuff, it’s time for another escape. Good luck!

---
### Commands

```bash
$0
cat /etc/bandit_pass/bandit33
```

![](assets/bandit32/step1.png)

> **Password:** tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0

### Explanation

>When logging in to this level, instead of a normal shell, you are placed inside a **restricted uppercase shell**.  
>This shell automatically converts all typed commands to uppercase, which normally breaks standard Linux commands like `ls`, `cat`, or `bash`.

>However, the shell still allows access to special shell variables.  
>The variable `$0` represents the name of the currently running shell.

>By typing `$0`, the shell re-executes itself, but this time it drops you into a **real interactive shell** that no longer forces commands to uppercase.

>Once a normal shell is obtained, standard commands work as expected, allowing access to the password file.

### Into the next!

```bash
ssh bandit33@bandit.labs.overthewire.org -p 2220
```

```bash
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
```