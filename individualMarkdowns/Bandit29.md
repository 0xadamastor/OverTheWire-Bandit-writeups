### Level Info

>There is a git repository at `ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo` via the port `2220`. The password for the user `bandit29-git` is the same as for the user `bandit29`.

Clone the repository and find the password for the next level.

---
### Commands

```bash
git clone ssh://bandit29-git@bandit.labs.overthewire.org:2220/home/bandit29-git/repo
# input the password from the previous level
cd repo/
ls
cat README.md
git branch -a
git checkout dev
cat README.md
```

![](assets/bandit29/step1.png)
![](assets/bandit29/step2.png)
![](assets/bandit29/step3.png)

> **Password:** qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL

### Explanation

>After cloning the repository, the default `master` branch does not contain the password, only a placeholder indicating that no passwords should exist in production.

>By listing all available branches with `git branch -a`, it becomes clear that there are additional remote branches, including a `dev` branch.

>Switching to the `dev` branch reveals a different version of the repository contents.  
>In this branch, the `README.md` file contains the credentials for the next level.

### Into the next!

```bash
ssh bandit30@bandit.labs.overthewire.org -p 2220
```

```bash
qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
```