---
tags: python, 陳述式
---

# try 的使用方法

中文表示**嘗試**的意思，言下之意為嘗試並且處理例外的工作

標準撰寫方式

```py
a = 1 
b = 0
try:
    c = a / b 
except ZeroDivisionError:
    print("無法除以零")
```


## 常見的錯誤形式

[標準錯誤](https://www.runoob.com/python/python-exceptions.html)