### Level Info

>The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

---

### Commands

```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

![](assets/bandit11/step1.png)

> **Password:** 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

### Explanation

### Explanation

>The file content is encoded using the ROT13 cipher, which shifts each letter by 13 positions.  

>**Syntax:** `tr SET1 SET2`  
>- `SET1` represents the characters to be replaced (here: all uppercase and lowercase letters `'A-Za-z'`).  
>- `SET2` represents the characters to map them to (here: `'N-ZA-Mn-za-m'`, i.e., letters rotated 13 positions).  

>Each letter in the file is translated according to this mapping, revealing the password.  

### Into the next!

```bash
ssh bandit12@bandit.labs.overthewire.org -p 2220
```

```bash
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```