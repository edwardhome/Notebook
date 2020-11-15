import cv2 
import numpy as np

A = np.array(cv2.imread('Lenna.jpg',cv2.IMREAD_COLOR))
B = np.array(cv2.imread('Lenna.jpg',cv2.IMREAD_GRAYSCALE))
C = np.array(cv2.imread('Lenna.jpg',cv2.IMREAD_UNCHANGED))

A_size = np.shape(A)
B_size = np.shape(B)
C_size = np.shape(C)

print(A_size)
print(B_size)
print(C_size)

cv2.imshow('B',(A[:,:,0])) #取得影像藍色數據
cv2.imshow('G',(A[:,:,1])) #取得影像綠色數據
cv2.imshow('R',(A[:,:,2])) #取得影像紅色數據
cv2.imshow('all',(A[:,:,:])) #取得影像所有數據f
cv2.imshow('gray',B) #取得影像數據
cv2.waitKey(0)
cv2.destroyAllWindows()