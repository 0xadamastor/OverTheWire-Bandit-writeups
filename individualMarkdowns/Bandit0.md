### Level Info

> The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. 
> Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

---
### Commands

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
password:bandit0
cat readme
```
![](assets/bandit0/step1.png)
![](assets/bandit0/step2.png)

> **Password:** ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
### Explanation

>Just read the file using cat.
### Into the next!

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

```bash
ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
```
