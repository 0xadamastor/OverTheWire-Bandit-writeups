### Level Info

>There is a git repository at `ssh://bandit30-git@bandit.labs.overthewire.org/home/bandit30-git/repo` via the port `2220`. The password for the user `bandit30-git` is the same as for the user `bandit30`.

Clone the repository and find the password for the next level.

---

### Commands

```bash
git clone ssh://bandit30-git@bandit.labs.overthewire.org:2220/home/bandit30-git/repo
# input the password from the previous level
cd repo/
ls
cat README.md
git tag
git show secret
```

![](assets/bandit30/step1.png)
![](assets/bandit30/step2.png)

> **Password:** fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy

### Explanation


>After cloning the repository, the working tree appears to be empty and the `README.md` file does not contain any useful information.

>In previous levels, sensitive data was hidden in commit history and in non-default branches.  
>Following the same mindset, the next step is to inspect other Git objects that may hold data, such as **tags**.

>Listing the available tags with `git tag` reveals a tag named `secret`.

>Inspecting this tag using `git show secret` displays the contents directly associated with it, which contains the password for the next level.

### Into the next!

```bash
ssh bandit31@bandit.labs.overthewire.org -p 2220
```

```bash
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
```