# for 迴圈的用法
Foreachy在電腦程式語言中，泛指一種流程控制，通常來表示迴圈遍歷陣列或集合中的元素，在`Python` 中以 `for`做為語句的開頭搭配`in`、`range`這兩個關鍵字作為控制邏輯。

## 範例
```py
for i in range(5):
	print(i)
```

解釋如下：
- 將 `i` 放入 `for` 迴圈
- 其長度範圍有**5**
- 列印出`i`的數值
- 判斷`i`是否小於**5**
- 若不小於**5**則跳出迴圈

結果：

	0
	1
	2
	3
	4
---
### range的用法
`range`在python裡面，可以以括號宣告長度，主要有兩種方法

- 不指定起始數字

	```py
	for i in range(3):
		print(i)
	```

	輸出結果：
	
		0
		1
		2
	從0開始到2結束，一共執行三次迴圈。
- 指定起始數字
	```py
	
	for i in range(1,6,2):
		print(i)
		
	```
	輸出結果：
	
		1
		3
		5
	從1開始到6結束，每隔2執行一次，一共執行三次迴圈
	

## 與字串的應用
[`list`](python_列表) 使用中括號 \[\] 將數字、文字等元素包起來。
例如，使用 \[1, 2, 3, 4, 5\]這樣的語法即可建立內含1、2、3、4、5 共 5 個元素的 [list](python_列表)。下面是一個使用 `for`迴圈將 [list](python_列表) 中的序列性資料逐一列印出來的例子：

```py
data = ['王大明','孫小美','李小華','韓天霸']
for i in data:
	print(i)
```
結果：

	王大明
	孫小美
	李小華
	韓天霸

其內容不僅可以放入數字，也可以以物件為導向

#python #迴圈 #程式設計 