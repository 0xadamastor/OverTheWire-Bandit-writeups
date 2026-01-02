### Level Info

>To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

---

### Commands

```bash
ls
./bandit20-do
./bandit20-do whoami
./bandit20-do cat /etc/bandit_pass/bandit20
```

![](assets/bandit19/step1.png)

> **Password:** 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO

### Explanation

>The file `bandit20-do` is a **setuid binary**, meaning it executes with the privileges of its owner, which is **bandit20**, regardless of the current user.

>Running the binary without arguments displays usage instructions, indicating that it can be used to execute arbitrary commands as bandit20.  
>By supplying a command such as `whoami`, it can be confirmed that the command is executed with bandit20 privileges.

>Using the setuid binary to run `cat /etc/bandit_pass/bandit20` allows reading the password file for the next level, which is normally inaccessible, thus revealing the password for **bandit20**.
### Into the next!

```bash
ssh bandit20@bandit.labs.overthewire.org -p 2220
```

```bash
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```
