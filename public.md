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

[課程連結](https://github.com/edwardhome/Notebook)

## 12/12上課內容

1. 相關函式教學
2. 運算子
3. 物件導向
4. 例外處理
5. 習題練習

### 練習1

比較一下四則運算的差異，並且利用`python`進行一個公式解$ x = \frac {-b \pm \sqrt {b^2- 4ac}} {2a} $，針對下列一元二次方程式求其根。

方程式：

- $x^2+5x-24 = 0$
- $3x^2+7x+5 = 0$
- $x^2-14x+49 = 0$

>提示：可使用 `input()`函式，分別針對 $x^2$ 與 $x$ 的系數做輸入，在套入公式求解。

### 練習2

例外練習，利用例外處理進行判斷除以0並且不會直接中斷程式

功能需求:


### 練習3

利用`import`匯入`math`套件庫，並且利用物件導向的概念將光學常用的公式，以`def`的形式做成套件庫，並且在主程式呼叫使用，且設定中斷以便可以隨時退出。

功能需求

1. 折射定律：輸入折射率與入射角使程式計算折射角(以度度量呈現)
2. 布魯斯特角：承上所述，將所輸入的折射率求得其布魯斯特角的數值。
3. 最大臨界角:針對入射面與折射面的材料不同求得最大臨界角。

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
