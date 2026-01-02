### Level Info

>There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

---

### Commands

```bash
# You will need two terminal instances connected!
# 1st terminal:
nc -l 1337
# 2nd terminal:
./suconnect 1337
# 1st terminal: (input the password you received in the past level and you will receive a new one)
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```

![](assets/bandit20/step1.png)

> **Password:** EeoULMCra2q0dSkYj561DX7s1CpBuOBt

### Explanation

>The binary `suconnect` is a **setuid program**, meaning it executes with the privileges of **bandit21**.  
>Its purpose is to connect to `localhost` on a user-specified port, read a single line of input, and verify whether it matches the password from the previous level (**bandit20**).

>A local listener is first started using `nc` (netcat) on an arbitrary port.
>When `suconnect` is executed with the same port number, it connects back to the listener.

>The **bandit20 password** is then sent through the network connection.  
>If the password is correct, `suconnect` responds by transmitting the password for **bandit21**, which is received in the listening terminal.

### Into the next!

```bash
ssh bandit21@bandit.labs.overthewire.org -p 2220
```

```bash
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
```
