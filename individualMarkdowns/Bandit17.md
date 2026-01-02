### Level Info

>There are 2 files in the homedirectory: **passwords.old and passwords.new**. The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old and passwords.new**

**NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19**

---

### Commands

```bash
diff passwords.old passwords.new
```

![](assets/bandit17/step1.png)

> **Password:** x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO

### Explanation

>The `diff` command is used to compare the files `passwords.old` and `passwords.new` line by line.
>Since the password for the next level is the **only line that differs** between the two files, the output of `diff` directly reveals the updated password.

### Into the next!

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220
```

```bash
x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```
