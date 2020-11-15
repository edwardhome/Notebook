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
