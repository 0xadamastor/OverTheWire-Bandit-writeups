### Level Info

>The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

---

### Commands

```bash
base64 -d data.txt
```

![](assets/bandit10/step1.png)

> **Password:** dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

### Explanation

>The file contains data encoded in Base64 format.  
>Using `base64 -d` decodes the content, revealing the original text which contains the password.

### Into the next!

```bash
ssh bandit11@bandit.labs.overthewire.org -p 2220
```

```bash
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```