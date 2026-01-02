### Level Info

>The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL/TLS encryption.

>**Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**

---

### Commands

```bash
openssl s_client -connect localhost:30001
# input the password from Bandit14: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

![](assets/bandit15/step2.png)
![](assets/bandit15/step1.png)

> **Password:** kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

### Explanation

>`openssl s_client` is used to establish a TLS connection to `localhost` on port `30001`.  
>Once connected, the current level’s password is typed manually and sent to the service.

>If the password is correct, the server responds with the password for the next level.

>Messages like **DONE**, **RENEGOTIATING**, or **KEYUPDATE** are part of the TLS handshake and can be ignored.

### Into the next!

```bash
ssh bandit16@bandit.labs.overthewire.org -p 2220
```

```bash
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
```