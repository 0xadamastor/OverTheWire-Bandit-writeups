### Level Info

>The password for the next level is stored in the file **data.txt** next to the word **millionth**

---

### Commands

```bash
grep "millionth" data.txt
```

![](assets/bandit7/step1.png)

> **Password:** dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

### Explanation

>The password is located on the same line as the word *millionth*.  
>Using `grep` searches the file and returns the matching line containing the password.

### Into the next!

```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
```

```bash
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```