# 利用Lapacian進行邊緣偵測
在[邊緣偵測](OpenCV邊緣偵測)中提到，可以利用OpenCV對影像做出邊緣偵測的運算，以下利用[python](使用python的基本概念)進行簡單的影像運算。

## 使用影像
這次一樣使用經典圖片，萊娜圖。
<center> <img src="https://upload.wikimedia.org/wikipedia/zh/3/34/Lenna.jpg"> </center>

## 範例
1. 首先先匯入相關函式
	```py
	import cv2
	import numpy as np
	import argparse
	```
	其中，[`argparse`](argparse簡介)是一個內建模組主要用來完成文字命令列的一些操作，這裡就不多做說明。
2. 利用[`def`](python_def語句)先行撰寫一個顯示模組，主要讓不同的圖片均可輸入並顯示
	```python
	def display(windowsName,img):
		cv2.namedWindow(windowsName, cv2.WINDOW_NORMAL) #使視窗可調整，並命名
		size = img.shape# 影像尺寸最佳化
		h = size[0]
		w = size[1]
		while(True):
			if w>800 or h>800:
				w = int(w/2)
				h = int(h/2)
			else:
				break
		cv2.resizeWindow(windowsName,w,h)
		cv2.imshow(windowsName,img)
		cv2.waitKey(0)
	```
3. 讀取圖片並完成`Laplacian`完成邊緣計算
	```py
	ap = argparse.ArgumentParser()
	ap.add_argument('-i',required= True,help='Path to the image')
	args = vars(ap.parse_args())
	image = cv2.imread(args['i'],flags=0)
	imagename = args['i']
	display(imagename,image)
	lap = cv2.Laplacian(image, cv2.CV_64F)#將函數轉為浮點格式CV_64F
	lap = np.uint8(np.absolute(lap))#取得絕對值後轉為8bit資訊
	lap = abs(255-lap)
	display('LAP',lap)
	```
	>使用Laplacian找出邊緣。注意使用此函數除了傳入灰階影像之外，亦須指定輸出的影像浮點格式CV_64F
	為什麼是使用64bits而非灰階的8bits呢？因為Laplacian過程需進行black-to-white及white-to-black兩種轉換
	在微分的梯度計算（gradient）中black-to-white屬於正向的運算而white-to-black則是負向
	灰階的8bits格式僅能儲存0-255的正值，因此必須使用64bits。
	注意在接下來須取其絕對值並轉為8bit的灰階資訊，這是一般在運行Laplacian運算時所建議的方法
	網路上的說法是此方式可保留所有的邊緣資訊：先轉出為64bit，再取絕對值轉為8bit。
4. 輸出圖片
	```py
	cv2.imwrite('.\\edge_lenna.png',lap)
	```

<center><img src="https://github.com/edwardhome/Notebook/blob/main/opencv_test/edge_lenna.png?raw=true"></center>

<center>輸出結果</center>