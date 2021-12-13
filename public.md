---
tags: python
---
# 聯合大學Python課程

本章節主要敘述Python相關內容與練習程式，針對相關操作說明連結如下所述
與上週相關的內容如下：
[conda用法](conda用法.md)
[使用Python](使用Python.md)
[12/07上課內容](#1207上課內容)
相關內容，均會在這裡同步更新，也方便各位同學下載範例程式碼。

## 12/12上課內容

1. 相關函式教學
2. 運算子
3. 物件導向
4. 例外處理
5. 習題練習

## 12/07上課內容

if 判斷式

```python
a = int(input("輸入A= "))
b = 2

if a>b:
    print("a比b大")
elif a<b:
    print("a比b小")
else:
    print("a=b")
```

for 迴圈

```python
for i in range(100):
    print(i)
```

匯入pandas

```python
import pandas as pd 

df = pd.DataFrame()

print(type(df))
```

繪圖練習

```python
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10],columns=["000"])
df2 = df*df
print(df)

fig = plt.figure()
ax = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax.plot(df)
ax2.plot(df2)
plt.show()
```
