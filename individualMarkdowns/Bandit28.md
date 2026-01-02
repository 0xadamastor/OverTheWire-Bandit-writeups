### Level Info

>There is a git repository at `ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo` via the port `2220`. The password for the user `bandit28-git` is the same as for the user `bandit28`.

Clone the repository and find the password for the next level.

---

### Commands

```bash
git clone ssh://bandit28-git@bandit.labs.overthewire.org:2220/home/bandit28-git/repo
# input the password from the previous level
cd repo/
ls
cat README.md
git log
git show d0cf2ab7dd7ebc6075b59102a980155268f0fe8f
```

![](assets/bandit28/step1.png)
![](assets/bandit28/step2.png)
![](assets/bandit28/step3.png)

> **Password:** 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7

### Explanation

>After cloning the Git repository using the credentials of **bandit28**, the only visible file in the working tree is `README.md`.

>At first glance, the password field is redacted (`xxxxxxxxxx`), suggesting that the sensitive information was intentionally removed.

>However, Git preserves the full history of a repository. Even if data is deleted or modified in later commits, it can still be recovered by inspecting earlier commits.

>By checking the commit history with `git log`, multiple commits are revealed. One of them is explicitly named **“add missing data”**, which strongly suggests that sensitive information was added at that point.

>Using `git show <commit_hash>` on that commit displays the exact changes introduced, including the previous contents of `README.md`.

>In this earlier version of the file, the password for **bandit29** is clearly visible in plain text.

>Thus, the password is recovered not from the current state of the repository, but from its commit history.

### Into the next!

```bash
ssh bandit29@bandit.labs.overthewire.org -p 2220
```

```bash
4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
```