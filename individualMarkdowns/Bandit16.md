### Level Info

>The credentials for the next level can be retrieved by submitting the password of the current level to **a port on localhost in the range 31000 to 32000**. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

>**Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**

---

### Commands

```bash
nmap -p 31000-32000 localhost

# Connect to the open ports and check which ones speak TLS/SSL.
# Send the Bandit16 password to each TLS-enabled service.
echo "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | openssl s_client -connect localhost:31790 -quiet

# Port 31790 is the correct service, it returns the SSH private key for bandit17.
# Now, connect using the key and retrieve the bandit17
ssh -i bandit17.key bandit17@bandit.labs.overthewire.org -p 2220
# The location is the same as bandit 14 -> 15
cat /etc/bandit_pass/bandit17
```

![](assets/bandit16/step1.png)
![](assets/bandit16/step2.png)
![](assets/bandit16/step3.png)
![](assets/bandit16/step4.png)
![](assets/bandit16/step5.png)
![](assets/bandit16/step6.png)
![](assets/bandit16/step7.png)
![](assets/bandit16/step8.png)

> **Password:** EReVavePLFHtFlFsjn3hyzMlvSuSAcRD

### Explanation

>The port range **31000–32000** is scanned locally to identify which services are listening.  
Among the open ports, each service is tested to determine whether it uses **SSL/TLS**.

>Using `openssl s_client`, a TLS connection is established to the SSL-enabled ports and the **Bandit16 password** is sent to each one.
>Most of the services simply echo back the provided input, indicating they are not the correct service.

>The service running on **port 31790** behaves differently and returns an **SSH private key**, which is the credential for the next level.

> After saving the key and setting the correct file permissions (`chmod 600`), it is used to authenticate as **bandit17** via SSH and retrieve the password for the next level.
### Into the next!

```bash
ssh bandit17@bandit.labs.overthewire.org -p 2220
```

```bash
EReVavePLFHtFlFsjn3hyzMlvSuSAcRD
```
