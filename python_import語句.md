---
tags: python, 物件導向, import
---
# import 的用法

在python裡面，如果要匯入相關的函式或已經由第三方開發者開發的套件庫，可使用`import`的方式匯入，而套件要如何安裝，則可使用[conda](conda用法)或pip指令進行安裝

## import 使用情境

準備建立稍大型的專案的時候，學習如何組織化你的 Python 專案是一大要點。Python 提供的 `module`（模組）與 `package`（套件）是建立架構的基本元件，但在`module`之間為了重複使用一些 `function`（函數）或 [`class`](python_class語句)（類別）而必須互相 `import`（匯入），使用上一個不注意就會掉入混亂的 import 陷阱。

## 模組與套件

基本上每一個python的程式檔就是一個**模組**，而裡面可以定義各種*函式*、*類別*與*變數*，如果每一個模組都等同一個檔案的話，那套件就如同這個檔案庫的目錄。

### 範例套件

- 套件(`package`)
  - 模組1(`module_1`)
  - 模組2(`module_2`)
    - 2子模組1(`submodule_2-1`)
    - 2子模組2(`submodule_2-2`)

參考 [PEP328](https://www.python.org/dev/peps/pep-0328/#guido-s-decision '範例')提供的範例

```sh
package
├── __init__.py
├── subpackage1
│   ├── __init__.py
│   ├── moduleX.py
│   └── moduleY.py
├── subpackage2
│   ├── __init__.py
│   └── moduleZ.py
└── moduleA.py
```

如果要呼叫相關套件，則須透過下列形式進行呼叫。

## 語句結構

匯入**numpy**套件

```py
import numpy
```

利用 `import` 直接匯入模組名稱，但是這樣在引用的時候需要完整的寫出模組名稱來，有時候顯的不是很方便，故可以利用`as`該模組名稱取一個別名。
如：

```py
import numpy as np
```

而套件或許有很多子模組，有時候不一定需要會出所有的模組，因此可以透過`from`來針對需要的部份匯入指定的子模組。
如：

```py
from numpy import array as arr
```

當然，以`numpy`為例我們一般來說不會只匯入`array`，不過如果模組十分巨大，只會入特定模組可以降低程式的衝突及最後包裝完成執行檔後所佔用的空間喔。

## 模組所在位置

一般來說再python直譯器直接執行

```py
import sys
sys.path
```

所出現的位置，正式可以使用`import`匯入的位置喔。

## 匯入自定義子程式

在[class](python_class語句.md)中，有提到可以將程式進行包裝，並且具備物件導向與繼承的能力，同樣的可以將打包程式利用`import`進行匯入，並且用物件導向的方式進行操作與使用。
