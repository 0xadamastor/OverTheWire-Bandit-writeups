### Level Info

>A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

---

### Commands

```bash
cd /etc/cron.d/
ls
cat cronjob_bandit22
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

![](assets/bandit21/step1.png)

> **Password:** tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q

### Explanation

>The directory `/etc/cron.d/` contains cron job definitions that specify commands executed automatically at scheduled intervals.  
>The file `cronjob_bandit22` reveals that the script `/usr/bin/cronjob_bandit22.sh` is executed every minute as the user **bandit22**.

>The script reads the password for bandit22 from `/etc/bandit_pass/bandit22` and writes it to a file in the `/tmp` directory, changing its permissions to make it readable.

>By locating and reading the generated file in `/tmp`, the password for the next level is obtained.

### Into the next!

```bash
ssh bandit22@bandit.labs.overthewire.org -p 2220
```

```bash
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```
