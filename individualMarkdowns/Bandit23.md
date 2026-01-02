### Level Info

>A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

---

### Commands

```bash
cd /etc/cron.d/
ls
cat /usr/bin/cronjob_bandit24.sh
```

### Script
```bash
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/bandit24_pass
chmod 644 /tmp/bandit24_pass
```

### Commands

```bash
cat /tmp/bandit24_pass
```

![](assets/bandit23/step1.png)
![](assets/bandit23/step2.png)
![](assets/bandit23/step3.png)

> **Password:** gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8

### Explanation

>The cron configuration shows that the script `/usr/bin/cronjob_bandit24.sh` is executed every minute as the user **bandit24**.

>This script navigates to the directory `/var/spool/bandit24/foo` and executes every file in that directory that is owned by **bandit23**, deleting each script after execution.

>By creating a custom shell script owned by bandit23 and placing it in this directory, it is possible to have it executed automatically with **bandit24** privileges.

>The custom script reads the password from `/etc/bandit_pass/bandit24` and writes it to a temporary file before being deleted by the cron job.

>After the cron job runs, the generated file remains accessible, revealing the password for the next level.

### Into the next!

```bash
ssh bandit24@bandit.labs.overthewire.org -p 2220
```

```bash
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
```