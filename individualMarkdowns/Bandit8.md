### Level Info

>The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

---

### Commands

```bash
sort data.txt | uniq -u
```

![](assets/bandit8/step1.png)

> **Password:** 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

### Explanation


>The file contains many repeated lines, with only one line occurring once.  
>Sorting the file groups identical lines, allowing `uniq -u` to identify and display the unique line.

### Into the next!

```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
```

```bash
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```