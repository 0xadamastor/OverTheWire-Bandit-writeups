### Level Info

>There is a git repository at `ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo` via the port `2220`. The password for the user `bandit31-git` is the same as for the user `bandit31`.

Clone the repository and find the password for the next level.

---

### Commands

```bash
git clone ssh://bandit31-git@bandit.labs.overthewire.org:2220/home/bandit31-git/repo
# input the password from the previous level
cd repo/
echo "May I come in?" > key.txt
git add -f key.txt
# you can find the identity inside the server "cat .gitconfig"
git config user.name "bandit31"
git config user.email "bandit31@overthewire.org"
git commit -m "add key"
git push
```

![](assets/bandit31/step1.png)
![](assets/bandit31/step2.png)
![](assets/bandit31/step3.png)
![](assets/bandit31/step4.png)

> **Password:** 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K

### Explanation

>The objective of this level was not to extract hidden data from the repository, but to **interact with it by pushing a specific file** to the remote server.

>After cloning the repository, the instructions in `README.md` clearly state what is required:  
>a file named `key.txt`, containing exactly the text **"May I come in?"**, committed to the `master` branch.

>The file `key.txt` already exists in the repository but is listed in `.gitignore`, which means Git will ignore it by default and refuse to add it normally.

>To bypass this behavior, the file was explicitly force-added using `git add -f key.txt`, telling Git to track the file despite the ignore rules.

>When attempting to commit, Git required a configured username and email. These were set using the `.gitconfig` found on the OverTheWire server for this task, applied locally to the repository using `git config`.  

>Once the commit was created and pushed, a **server-side pre-receive hook** was triggered.  
>This hook validated the contents of the repository and checked whether the required conditions were met.

>Although the push was ultimately rejected, the validation hook still executed and printed the password for the next level as part of its output.
### Into the next!

```bash
ssh bandit32@bandit.labs.overthewire.org -p 2220
```

```bash
3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K
```