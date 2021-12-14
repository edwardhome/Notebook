---
tags: python, import, OpenCV
---


# 邊緣偵測
邊緣偵測（Edge detection）屬於機器視覺中最重要的步驟，因為要讓電腦準確的抓到影像的物體位置，需要使用大量的邊緣偵測運算，這點也是[OpenCV](openCV.md)中一個十分重要的功能。

OpenCV提供三種邊緣檢測的方式來處理**Edge detection**分別是
- [Laplacian](Laplacian邊緣偵測)（拉普拉斯算子）
- [Sobel](Sobel邊緣偵測)（索伯算子）
- Canny

這三種方法皆使用了一維甚至於二維的微分，嚴格來說，若依其使用技術原理的不同可分為兩種：
>1. **Laplacian**原稱為*Laplacian method*，透過計算零交越點上光度的二階導數（detect zero crossings of the second derivative on intensity changes）
>2. **Sobel**和**Canny**使用的則是梯度原理（Gradient methods），它是透過計算像素光度的一階導數差異（detect changes in the first derivative of intensity）來進行邊緣檢測。

這邊也針對兩種技術原理進行說明，以**Laplacian**來講，對於光學雜訊非常敏感，因此實務上來說都會將影化模糊化再進行處理，而**Sobel**與**Canny**使用相同的技術，但是二者執行上有顯著的差異以**Soble**是以簡單的捲積過濾器偵測影像水平及垂直的光度的改變，以加權平均的方式概念上，索伯算子就是一個小且是整數的濾波器對整張影像在水平及垂直方向上做捲積，因此它所需的運算資源相對較少，另一方面，對於影像中的頻率變化較高的地方，它所得的梯度之近似值也比較粗糙。
然而**Canny**相對複雜的多，Canny的目標是找到一個最優的邊緣檢測算法，最優邊緣檢測的含義是：
>- 好的檢測 - 算法能夠儘可能多地標識出圖像中的實際邊緣。
>- 好的定位 - 標識出的邊緣要與實際圖像中的實際邊緣儘可能接近。
>- 最小響應 - 圖像中的邊緣只能標識一次，並且可能存在的圖像雜訊不應標識為邊緣。

為了滿足這些要求Canny使用了變分法，這是一種尋找滿足特定功能的函數的方法。最優檢測使用四個指數函數項的和表示，但是它非常近似於高斯函數的一階導數。

#python #物件導向 #OpenCV  #邊緣偵測
