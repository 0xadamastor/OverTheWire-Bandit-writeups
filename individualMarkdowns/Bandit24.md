### Level Info

>A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.  
>You do not need to create new connections each time

---

### Commands

```bash
for i in $(seq -w 0000 9999); do
  echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i" # bandit24Password
done | nc localhost 30002
```

![](assets/bandit24/step1.png)

> **Password:** iCi86ttT4KSNe1armKiwbQNmB3YJP3q4

### Explanation

>The service listening on port `30002` requires the password from the previous level (**bandit24**) together with a 4‑digit numeric PIN in order to return the password for the next level.

>Since there is no method to discover the PIN directly, a brute‑force approach is used by trying all possible combinations from `0000` to `9999`.

>The one line script generates every possible PIN, appends it to the known bandit24 password, and sends each attempt to the daemon.  
>The daemon allows multiple attempts over a single connection, making it possible to test all combinations efficiently without reconnecting.

>In the code, `seq -w 0000 9999` produces all 4‑digit PINs with leading zeros.  
>The `for` loop iterates over each value and formats the input exactly as expected by the service.  
>The entire output is then piped into `nc`, which maintains a single TCP connection to the daemon on port `30002`, ensuring that all attempts are processed in order until the correct PIN is found and the password for **bandit25** is returned.

### Into the next!

```bash
ssh bandit25@bandit.labs.overthewire.org -p 2220
```

```bash
iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```
