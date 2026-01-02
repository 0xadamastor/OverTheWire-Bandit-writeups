### Level Info

>A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

---

### Commands

```bash
cd /etc/cron.d
ls
cat cronjob_bandit23
cat /usr/bin/cronjob_bandit23.sh
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
# copy the md5 hash
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

![](assets/bandit22/step1.png)
![](assets/bandit22/step2.png)
![](assets/bandit22/step3.png)

> **Password:** 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga

### Explanation

>The cron configuration in `/etc/cron.d/` shows that the script `/usr/bin/cronjob_bandit23.sh` is executed every minute as the user **bandit23**.

>The script generates a filename by computing the MD5 hash of the string `I am user bandit23` and uses it as the name of a file in `/tmp`.

>The password for bandit23 is then copied from `/etc/bandit_pass/bandit23` into that file.

>By reproducing the same MD5 hash locally and reading the corresponding file in `/tmp`, the password for the next level is obtained.

### Into the next!

```bash
ssh bandit23@bandit.labs.overthewire.org -p 2220
```

```bash
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
```
