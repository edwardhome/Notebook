---
tags: python
---

### 上課內容

if 判斷式
```python=
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


```python=  
for i in range(100):
    print(i)
```

匯入pandas

```python=
import pandas as pd 

df = pd.DataFrame()

print(type(df))
```

繪圖練習
```python=
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