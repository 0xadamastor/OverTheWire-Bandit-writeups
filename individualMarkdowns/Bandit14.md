### Level Info

>The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.

---

### Commands

```bash
echo "MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS" | nc localhost 30000
```

![](assets/bandit14/step1.png)

> **Password:** 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

### Explanation

>This level introduces a network service running locally on the server.  
>The password must be sent to **port 30000 on localhost**.

>Using `echo`, the current password is provided as input.  
>The pipe (`|`) forwards this input to `nc` (netcat), which opens a TCP connection to the specified port.

>When the correct password is received, the service returns the password for the next level.

### Into the next!

```bash
ssh bandit15@bandit.labs.overthewire.org -p 2220
```

```bash
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```
