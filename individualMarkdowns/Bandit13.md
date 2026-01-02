### Level Info

>The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.

---

### Commands

```bash
ls
cat sshkey.private
exit
nano bandit14.key
chmod 600 bandit14.key
ssh -i bandit14.key bandit14@bandit.labs.overthewire.org -p 2220
```

![](assets/bandit13/step1.png)
![](assets/bandit13/step2.png)
![](assets/bandit13/step3.png)

> **Password:** MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

### Explanation

>In this level, instead of a password, a private SSH key is provided.  
>The password for the next level can only be read by user **bandit14**, so we must authenticate as that user using the given private key.

>Using SSH with the `-i` option allows us to specify the private key file and log in directly as **bandit14**, gaining access to the next level.

>Don't forget to cat /etc/bandit_pass/bandit14

### Into the next!

```bash
ssh -i bandit14.key bandit14@bandit.labs.overthewire.org -p 2220
```
or
```bash
ssh bandit15@bandit.labs.overthewire.org -p 2220
```

```bash
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```