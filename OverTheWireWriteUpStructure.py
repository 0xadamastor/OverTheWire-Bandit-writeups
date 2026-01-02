#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create_bandit_file(level_num):
    
    filename = f"Bandit{level_num}.md"
    next_level = level_num + 1
    prev_level = level_num - 1
    
    content = f"""### Level Info

>

---

### Commands

```bash
```

> **Password:**

### Explanation

>

### Into the next!

```bash
ssh bandit{next_level}@bandit.labs.overthewire.org -p 2220
```

```bash

```

[[Bandit{next_level}]]
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created: {filename}")

def main():
    """Main function"""
    print("Creating Bandit files from 3 to 33...\n")
    
    for i in range(3, 34):
        create_bandit_file(i)
    
    print(f"\n✓ Total: {33-3+1} files created successfully!")

if __name__ == "__main__":
    main()