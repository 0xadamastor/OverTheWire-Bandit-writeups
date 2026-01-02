### Level Info

>The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.

---

### Commands

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat *"
```

![](assets/bandit18/step1.png)

> **Password:** cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

### Explanation


>The `.bashrc` file for **bandit18** is configured to immediately terminate the SSH session upon login, preventing an interactive shell from being used.

>By supplying a command directly to the `ssh` client, the command is executed **before** the logout behavior in `.bashrc` takes effect.  
>This allows reading files from the home directory without starting an interactive session.

>The command `cat *` is used to display the contents of all files in the directory, which includes the `readme` file containing the password for the next level.

### Into the next!

```bash
ssh bandit19@bandit.labs.overthewire.org -p 2220
```

```bash
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```
