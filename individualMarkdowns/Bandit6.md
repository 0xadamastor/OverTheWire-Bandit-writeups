### Level Info

>The password for the next level is stored **somewhere on the server** and has all of the following properties:

- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

---

### Commands

```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

![](assets/bandit6/step1.png)

> **Password:** morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

### Explanation

>The challenge requires locating a file anywhere on the system that matches specific ownership and size properties.

>`find /` searches the entire filesystem.  
>`-type f` limits the search to regular files.  
>`-user bandit7` filters files owned by the user *bandit7*.  
>`-group bandit6` filters files owned by the group *bandit6*.  
>`-size 33c` selects files that are exactly 33 bytes in size.  
>`2>/dev/null` suppresses permission denied errors during the search.

>This combination uniquely identifies the file containing the password.

### Into the next!

```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
```

```bash
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```