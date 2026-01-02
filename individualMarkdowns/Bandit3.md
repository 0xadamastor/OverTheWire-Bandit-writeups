### Level Info

>The password for the next level is stored in a hidden file in the **inhere** directory.

---

### Commands

```bash
ls
cd inhere
ls -la
cat ...Hiding-From-You
```

![](assets/bandit3/step1.png)

> **Password:** 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

### Explanation

>Files that start with `.` are hidden by default in Linux.  
>Using `ls -la` reveals hidden files, allowing the password file to be identified and read.

### Into the next!

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

```bash
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
```