### Level Info

>The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

- human-readable
- 1033 bytes in size
- not executable

---

### Commands

```bash
ls
cd inhere/
ls
cd ..
find inhere -type f -size 1033c ! -executable -exec file {} \; | grep ASCII
cat inhere/maybehere07/.file2
```

![](assets/bandit5/step1.png)

> **Password:** HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

### Explanation


>The challenge requires finding a file under the *inhere* directory that is human‑readable, exactly 1033 bytes in size, and not executable.

>`find inhere` searches recursively inside the *inhere* directory.  
>`-type f` restricts the search to regular files only.  
>`-size 1033c` filters files that are exactly 1033 bytes.  
>`! -executable` excludes files with execute permissions.  
>`-exec file {} \;` runs the `file` command on each matching file to identify its type.  
>`grep ASCII` filters the output to show only human‑readable (ASCII) files.

>This combination isolates the single file containing the password.

### Into the next!

```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

```bash
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```