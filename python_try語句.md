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
|異常名稱|名詞解釋|
|---|---|
| BaseException             |所有異常的基類|
| SystemExit                |解釋器請求退出|
| KeyboardInterrupt         |用戶中斷執行(通常是輸入`ctrl+c`)|
| Exception                 |常規錯誤的基類|
| StopIteration             |迭代器沒有更多的值|
| GeneratorExit             |產生器(generator)發生異常來通知退出|
| StandardError             |所有的內建標準異常的基類|
| ArithmeticError           |所有數值計算錯誤的基類|
| FloatingPointError        |浮點計算錯誤|
| OverflowError             |數值運算超出最大限制|
| ZeroDivisionError         |除(或取模)零 (所有數據類型)|
| AssertionError            |斷言語句失敗|
| AttributeError            |對像沒有這個屬性|
| EOFError                  |沒有內建輸入,到達EOF標記|
| EnvironmentError          |操作系統錯誤的基類|
| IOError                   |輸入/輸出操作失敗|
| OSError                   |操作系統錯誤|
| WindowsError              |系統調用失敗|
| ImportError               |導入模塊/對象失敗|
| LookupError               |無效數據查詢的基類|
| IndexError                |序列中沒有此索引(index)|
| KeyError                  |映射中沒有這個鍵|
| MemoryError               |記憶體溢出錯誤(對於Python 直譯器不是致命的)|
| NameError                 |未聲明/初始化對象 (沒有屬性)|
| UnboundLocalError         |訪問未初始化的本地變量|
| ReferenceError            |弱引用(Weak reference)試圖訪問已經垃圾回收了的對象|
| RuntimeError              |一般的運行時錯誤|
| NotImplementedError       |尚未實現的方法|
| SyntaxError               |Python 語法錯誤|
| IndentationError          |縮排錯誤|
| TabError                  |Tab 和空格混用|
| SystemError               |一般的解釋器系統錯誤|
| TypeError                 |對類型無效的操作|
| ValueError                |傳入無效的參數|
| UnicodeError              |Unicode 相關的錯誤|
| UnicodeDecodeError        |Unicode 解碼時的錯誤|
| UnicodeEncodeError        |Unicode 編碼時錯誤|
| UnicodeTranslateError     |Unicode 轉換時錯誤|
| Warning                   |警告的基類|
| DeprecationWarning        |關於被棄用的特徵的警告|
| FutureWarning             |關於構造將來語義會有改變的警告|
| OverflowWarning           |舊的關於自動提升為長整型(long)的警告|
| PendingDeprecationWarning |關於特性將會被廢棄的警告|
| RuntimeWarning            |可疑的運行時行為(runtime behavior)的警告|
| SyntaxWarning             |可疑的語法的警告|
| UserWarning               |用戶產生的警告|

---

## try-except-eles

相關範例

```py
def try_test(obj):
	try:
		a = float(obj)
	except (ValueError, TypeError):
		a = "異常產生，輸入資訊必為數字或可轉浮點數之字串\n"
	else:
		print(f"確認執行，輸入的型態為{type(obj)}，將其轉化為{type(a)}")
	print(a)
	return a

try_test("fdsa")
try_test(123.5)
try_test(1)
try_test("0.58")
```

## try-finally

`finally`為不管怎樣都要執行，通常使用情境為讀取文件的時候，有可能因為外部輸入的文件導致python無法讀取到他，這時候雖然捕獲異常，可是仍就得要中止程式執行，此時就可以利用`finally`的指令進行最後處理。不過以檔案的模式目前在[with](python_with語句.md)已經有妥善的處理了。

## try-except-else-finally

可不可以全部加在一起，當然可以只有`try`與`except`兩者為必要的，其餘均為可選。
依據個人的程式撰寫，當然可以選擇用不同的方式去處理屬於該程式會遇到的例外狀況。

