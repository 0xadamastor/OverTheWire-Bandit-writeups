### Level Info

>The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

---

### Commands

```bash
mkdir /tmp/and_binho_berde
cd /tmp/and_binho_berde
cp ~/data.txt .
xxd -r data.txt > data
file data
# Decompress according to the detected format:
# gzip  -> gunzip
# bzip2 -> bunzip2
# tar   -> tar -xf
```

![](assets/bandit12/step1.png)
![](assets/bandit12/step2.png)

> **Password:** FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

### Explanation

>The file `data.txt` was a hexadecimal dump of a compressed file.  
>The hexdump was first reversed to its binary form using `xxd -r`.

>Each compression layer was then identified with the `file` command and removed using the appropriate decompression tool (gzip, bzip2, or tar).  
>This process was repeated until a human‑readable text file was obtained, revealing the password.

### Into the next!

```bash
ssh bandit13@bandit.labs.overthewire.org -p 2220
```

```bash
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```