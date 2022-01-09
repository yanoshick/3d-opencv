# opencv imagaes application for python3
import cv2
import numpy as np



print("Hello opencv images!!!")

img = cv2.imread('lena.png')
cv2.imshow("Lena original", img)

affine_warp = np.array([[2, 0, 0], [0, 1, 0]], dtype=np.float32)
dsize = (img.shape[1]*2, img.shape[0])
warped_img = cv2.warpAffine(img, affine_warp, dsize)

cv2.imshow("2x Horizontal Stretching", warped_img)
cv2.waitKey(0)

