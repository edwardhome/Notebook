# OpenCV 簡介
OpenCV的全稱是Open Source Computer Vision Library，是一個跨平台的電腦視覺庫。OpenCV是由英特爾公司發起並參與開發，以BSD授權條款授權發行，可以在商業和研究領域中免費使用。
<center> <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/OpenCV_Logo_with_text.png"> 
</center>
<center>OpenCV的LOGO</center>
OpenCV的應用其實很廣，在許多的 #程式設計 上均有OpenCV的蹤跡，其中近年來以 #python 最為熱門因此本文也將使用python進行使用與探討。

在 #機器視覺 專案的開發中，OpenCV作為較大眾的開源庫，擁有了豐富的常用影象處理函式庫，採用C/C 語言編寫，可以執行在Linux/Windows/Mac等作業系統上，能夠快速的實現一些影象處理和識別的任務。此外，OpenCV還提供了Java、 #python 、 #cuda 等的使用介面、機器學習的基礎演算法呼叫，從而使得影象處理和影象分析變得更加易於上手，讓開發人員更多的精力花在演算法的設計上。

## 應用領域
- 人機互動
	- 人臉識別
	- 運動分析
- 影像處理
	- 邊緣偵測
	- 灰階處理
	- 濾波降噪
- 物體辨別
	- 動作識別
	- 汽車安全駕駛
	- 結構分析
實務上具有許多操作是混和使用，應用上也十分複雜。

##  安裝OpenCV
以下內容均利用`python`進行操作，主要可分為`pip`與[`conda`](conda用法)兩種，分別指令如下。
### pip 套件管理器
```shell
pip install opencv-python
```
這裡會自動下載[pypi](https://pypi.org/project/opencv-python/)的最新套件內容，這個函數是目前穩定的相關內容，已經驗證過的算式會放入這裡，如果想要使用最新的套件及開發中的套件包，可以安裝這下列版本。
```shell
pip install opencv-contrib-python
```
其詳細解說如[網站](https://pypi.org/project/opencv-contrib-python/)所述。

### conda 套件安裝管理
指令如下，會從[conda套件庫](https://anaconda.org/anaconda/opencv)下載目前的版本。
```shell
conda install opencv
```
其中，利用`pip`與`conda`下載的版本會略有落差，使用實際得特別注意版本差異。

## 匯入OpenCV
在python中，[匯入](python_import語句)OpenCV程式碼如下所示：
```py
import cv2 
```
由於python是物件導向的程式語言，因此操作上都是利用`cv2`這個做為開頭，進行OpenCV的一系列函數操作。

## 基本功能
### 讀取影像
```py
cv2.imread('path/image.png',flag)
```
其中`flag`可以用下列參數作為輸入
- cv2.IMREAD_COLOR(可用`1`代替)
	- 此為預設值，會載入影片的RGB數據，忽略透明度
- cv2.IMREAD_GRAYSCALE(可用`0`代替)
	- 直接將影像轉為灰階圖片
- cv2.IMREAD_UNCHANGED(可用`-1`代替)
	- 包含透明度在內的所有資訊均轉入數據

範例示範
#python #OpenCV #程式設計 
