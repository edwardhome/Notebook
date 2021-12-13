---
tags: python, 迴圈, 陳述式
---

# 流程控制

在[while](python_while語句.md)、[for](python_for語句.md)及[if](python_if語句.md)中都有提到的流程控制，其中有三種不同的功能

- `break` 意為強制跳脫整個迴圈
- `continue` 強制跳出本次迴圈，繼續進行下一圈
- `pass` 不做任何事情，所有程式是繼續

## break

直接中斷程式

```py
i = 10
while True:
    if i > 10:
        break
    else:
        print(i)
        i += 1
```

當 `i` 大於10的時候，直接中斷程式

## continue

```py
i = 0
for i in range(10):
    if i % 2 == 0:
        continue
    else:
        i += 1
    print(i)
    time.sleep(0.5)
```

當`i`除以2餘數等於零的時候，跳過該迴圈，並繼續執行

## pass

```py
i = 0 
for i in range(10):
    if i == 5:
        pass
    else:
        print(i)
    i += 1
    time.sleep(0.5)
```

當`i`等於5的時候，不執行列印工作，其餘照舊。
