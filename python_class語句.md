---
tags: python, 程式設計, 物件導向
---

# 類別

在學習程式語言時，或多或少都有聽過物件導向程式設計(Object-oriented programming，簡稱OOP)，它是一個具有物件(Object)概念的開發方式，能夠提高軟體的重用性、擴充性及維護性，在開發大型的應用程式時更是被廣為使用，所以在現今多數的程式語言都有此種開發方式，[`Python`](./使用Python.md)當然也不例外。而要使用物件導向程式設計就必須對類別(Class)及物件(Object)等有一些基本的了解。其中`class`通常與[`def`](python_def語句.md)一起出現。

## 主要結構

- 類別(Class)
- 物件(Object)
- 屬性(Attribute)
- 建構式(Constructor)
- 方法(Method)

```python
# 電腦類別
class Computer:
    # 建構式
    def __init__(self, cpu_name, gpu_name):
        self.cpu = cpu_name  # cpu屬性
        self.gpu = gpu_name  # gpu屬性
    # 方法(Method)
    def dothing(self):
        print(f"My computer is {self.cpu} and {self.gpu} .")
```

---

### 類別(Class)

簡單來說，就是物件(Object)的藍圖(blueprint)。就像要生產一部汽車時，都會有設計圖，藉此可以知道此類汽車會有哪些特性及功能，類別(Class)就類似設計圖，會定義未來產生物件(Object)時所擁有的屬性(Attribute)及方法(Method)。

而定義類別的語法如下：

```python
class classname：
    statement
```

依照命名方式，一般會讓*每個單字*的字首**大寫**表示，且不得使用底線**_**或是空白分隔單字。
範例如下：

```python
#範例1
class Computer:
    def __init__(self, input1, input2):
        self.A = input1
#範例2
class MyComputer:
```

---

### 物件(Object)

就是透過類別(Class)實際建立的實體，就像實際生產出來的汽車(例如：Mazda)。類別(Class)與物件(Object)的關係就像汽車設計圖與汽車實體。而建立物件(Object)的語法如下：

```python
object_name = classname()
```

這邊設計一個簡單範例：

```py
class Desktop:
    pass
class Notebook:
    pass

Macbook = Notebook() # 我們定義Macbook是筆電類別

print(isinstance(Macbook,Desktop))
print(isinstance(Macbook,Notebook))
```

輸出結果

```sh
False
True
```

### 建構式(Constructor)

於建立物件(Object)的同時，會自動執行的方法(Method)。所以通常我們會在建構式(Constructor)中初始化物件(Object)的屬性值(Attribute)。至少要有一個self參數，之後利用逗號區隔其他屬性，語法如下：

```py
class Notebook():
    def __init__(self, cpu_name, display_inch):
        self.cpu = cpu_name
        self.dispalysize = display_inch
```

而這個**self**是什麼意思呢?
它代表了實體物件的參考，也就是目前的物件(**Object**)。這個*self*就是告訴類別(**Class**)目前是在設定哪一個物件的屬性(**Attribute**)。所以範例中的意思就是此物件的`cpu`屬性等於傳入的`cpu_name`屬性值，此物件的`displaysize`屬性等於傳入的`display_inch`屬性值，而傳入屬性值的方式就是在建立物件的時候，如下範例：

---

### 屬性(Attribute)

負責存放物件(Object)的資料。設定物件(Object)的屬性值語法如下：

```py
object_name.attribute_name = value
```

套用前面的範例可以得知

```py
class Notebook():
    def __init__(self, cpu_name, display_inch):
        self.cpu = cpu_name
        self.dispalysize = display_inch

MacbookPro = Notebook('M1',13)

print(MacbookPro.cpu)
print(MacbookPro.dispalysize)
```

執行結果

```sh
M1
13
```

---

### 方法(Method)

可以想像是物件(Object)的行為。定義方法(**Method**)和函式(**Function**)的語法很像，都是def關鍵字開頭，接著自訂名稱，但是方法(Method)和建構式(Constructor)一樣至少要有一個self參數，語法如下：

```py
def method_name(self):
    statement
```

簡單來說，任何你希望這個程式做的事情，都可以放在**方法**這個位置，讓物件導向幫你完成想做的事情。

---

## 繼承

繼承(Inheritance)顧名思義，就是會有父類別(或稱基底類別Base Class)及子類別(Sub Class)的階層關係。子類別會擁有父類別公開的屬性(Attribute)及方法(Method)。
所以Python繼承(Inheritance)的概念就是將各類別(Class)會共同使用的屬性(Attribute)或方法(Method)放在一個獨立的類別(Class)中，其它的類別(Class)透過繼承(Inheritance)的方式來擁有，降低程式碼的重複性。

### 一般形式

先來看一段程式碼

```py
class Desktop:
    def __init__(self,name,cpu, disk, power):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.display =display
        self.power = power
    def start(self):
        print("您的電腦已開啟")
class Notebook:
    def __init__(self, name,cpu, disk, display, battery):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.display = display
        self.battery = battery
    def start(self):
        print("您的電腦已開啟")
class Phone:
    def __init__(self, name,cpu, disk, display, battery, camera):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.display = display
        self.battery = battery
        self.camera = camera
    def start(self):
        print("您的手機已開啟")
# 指定物件所屬類別
A = Notebook('MacbookPro','M1','256GB',13,'23000mAh')
B = Desktop('iMac','i7 10700','1TB','110V')
C= Phone('iPhone12','A14','256GB',6.1,'2000mAh',3)
# 執行物件方法

A.start()
B.start()
C.start()
```

執行結果

```sh
您的電腦已開啟
您的電腦已開啟
您的手機已開啟
```

---

### 繼承語法

但是，一段程式碼重複部份如此之多，這邊應該針對內容進行精簡化。因此有了**繼承**（inheritance），利用繼承語法將父類別使得相同的方法可以不用在做一次，也使得未來維護程式碼時較為簡單。

範例如下：

```py
class Device:
    def __init__(self,name):
        self.name=name
    def start(self):
        print(f'您的{self.name}已經開啟')
class Desktop(Device):
    def __init__ (self,name,cpu,disk,power):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.power=power
    def start(self):
        super().start() #執行父類別的功能
        print('系統已啟動windows 10')
        print('------------------------')
class Notebook(Device):
    def __init__ (self, name,cpu,disk,display, battery):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.display = display
        self.battery = battery
    def start(self):
        super().start()
        print('系統已啟動macOS Big sur')
        print('------------------------')
class Phone(Device):
    def __init__ (self, name,cpu,disk,display, battery, camera):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.display = display
        self.battery = battery
        self.camera = camera
    def start(self):
        super().start()
        print('系統已啟動ios 14')
        print('------------------------')
# 指定物件所屬類別
A = Notebook('MacbookPro','M1','256GB',13,'23000mAh')
B = Desktop('Xeno','i7 10700','1TB','110V')
C= Phone('iPhone12','A14','256GB',6.1,'2000mAh',3)
# 執行物件方法

A.start()
B.start()
C.start()
```

執行結果

```sh
您的MacbookPro已經開啟
系統已啟動macOS Big sur
------------------------
您的Xeno已經開啟
系統已啟動windows 10
------------------------
您的iPhone12已經開啟
系統已啟動ios 14
------------------------
```
