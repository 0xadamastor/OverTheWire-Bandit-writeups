### Level Info

>Good job getting a shell! Now hurry and grab the password for bandit27!

---

### Commands

```bash
ls
./bandit27-do cat /etc/bandit_pass/bandit27
```

![](assets/bandit26/step1.png)
![](assets/bandit26/step2.png)

> **Password:** upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB

### Explanation

>After escaping the restricted shell and obtaining a real Bash shell as **bandit26**, it is possible to execute binaries available in the home directory.

>The file `bandit27-do` is a setuid binary that runs commands with the privileges of **bandit27**.

>By using this binary to execute `cat /etc/bandit_pass/bandit27`, the password file for the next level can be read directly.

>This level is therefore a continuation of the previous one, requiring the restricted shell escape in order to gain the necessary shell access to execute the setuid binary.

### Into the next!

```bash
ssh bandit27@bandit.labs.overthewire.org -p 2220
```

```bash
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
```