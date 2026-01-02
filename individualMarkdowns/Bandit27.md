### Level Info

>There is a git repository at `ssh://bandit27-git@bandit.labs.overthewire.org/home/bandit27-git/repo` via the port `2220`. The password for the user `bandit27-git` is the same as for the user `bandit27`.

>Clone the repository and find the password for the next level.

>From this level to 31, the clones must be done in your machine! It's easier, trust me. 

---

### Commands

```bash
git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo
# input the password from the previous level
cd repo/
ls
cat README
```

> **Password:** Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN

### Explanation

>A Git repository is accessible over SSH using the user **bandit27-git**, which shares the same password as **bandit27**.

>By cloning the repository via SSH on port `2220`, its contents can be retrieved locally.

>The repository contains a `README` file, which directly reveals the password for the next level.

>Reading this file provides the password for **bandit28**.

### Into the next!

```bash
ssh bandit28@bandit.labs.overthewire.org -p 2220
```

```bash
Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
```