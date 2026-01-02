### Level Info

>Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not **/bin/bash**, but something else. Find out what it is, how it works and how to break out of it.

> NOTE: if you’re a Windows user and typically use Powershell to `ssh` into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.
---

### Commands

```bash
ls
cat bandit26.sshkey # save this on your machine and go back to bandit25
cat /etc/passwd
# Resize your window, so it gets REALLY SMALL
ssh -i ~/bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
v
:set shell=/bin/bash
# ENTER
:shell
# ENTER AGAIN
cat /etc/bandit_pass/bandit26
```

![](assets/bandit25/step1.png)
![](assets/bandit25/step2.png)
![](assets/bandit25/step3.png)
![](assets/bandit25/step4.png)
![](assets/bandit25/step5.png)
![](assets/bandit25/step6.png)
![](assets/bandit25/step7.png)
![](assets/bandit25/step8.png)

> **Password:** s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
### Explanation

>The user **bandit26** does not use `/bin/bash` as the login shell. Instead, the account is configured to launch a pager program (`more`) that displays a large block of text and prevents access to an interactive shell.

>By reducing the terminal window size before connecting, the output does not fit on the screen, causing the pager to pause and wait for user input. This confirms that the session is running inside `more`, not a real shell.

>The pager allows entering the `vim` editor by pressing `v`. This provides access to a full-featured editor environment running with bandit26 privileges.

>Inside `vim`, the shell used for command execution can be changed by setting `:shell=/bin/bash`.  
>
>Once this is configured, executing the `:shell` command spawns a real Bash shell.

>This effectively breaks out of the restricted environment and provides an interactive shell as **bandit26**, allowing access to the password file for the next level.

### Into the next!

```bash
ssh bandit26@bandit.labs.overthewire.org -p 2220
```

```bash
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
```