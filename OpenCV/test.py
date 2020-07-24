#BASIC IMAGE READING AND SAVING/COPYING

# import cv2 as cv
# import sys

# img = cv.imread(cv.samples.findFile("dp2.jpg"))

# if img is None:
#     sys.exit("Could not read the image.")

# cv.imshow("A Human", img)
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("dp3.png", img)

#SIMPLE/GLOBAL THRESHOLDING

# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread("dp2.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in range(6):
#     plt.subplot(2,3,i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])

# plt.show()

# ADAPTIVE THRESHOLD

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('bnw2.jpg',0)
# img = cv2.medianBlur(img,5)

# ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]

# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

#OTSU THRSHOLDING

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('ap.png',0)

# # global thresholding
# ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# # Otsu's thresholding
# ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# # Otsu's thresholding after Gaussian filtering
# blur = cv2.GaussianBlur(img,(5,5),0)
# ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# # plot all the images and their histograms
# images = [img, 0, th1,
#           img, 0, th2,
#           blur, 0, th3]
# titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
#           'Original Noisy Image','Histogram',"Otsu's Thresholding",
#           'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

# for i in range(3):
#     plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
#     plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
#     plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
#     plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
# plt.show()

#SEGMENTATION, RGB, BGR, HSV Patterns 

# import numpy as np
# import cv2  
# from matplotlib import pyplot as plt
# from matplotlib import colors
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm


# dark = cv2.cvtColor(cv2.imread('dark.jpg'), cv2.COLOR_RGB2BGR)
# hsv_dark = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)

# h, s, v = cv2.split(hsv_dark)
# fig = plt.figure() 
# axis = fig.add_subplot(1, 1, 1, projection="3d")

# pixel_colors = dark.reshape((np.shape(dark)[0]*np.shape(dark)[1], 3))
# norm = colors.Normalize(vmin=-1.,vmax=1.)
# norm.autoscale(pixel_colors)
# pixel_colors = norm(pixel_colors).tolist()


# axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
# axis.set_xlabel("Hue")
# axis.set_ylabel("Saturation")
# axis.set_zlabel("Value")
# plt.show()
# cv2.destroyAllWindows()

#GEOMETRIC CHANGES



#BLURRING

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('as2.png')
# n=10

# kernel = np.ones((n,n),np.float32)/(n*n)
# dst = cv2.filter2D(img,-1,kernel)

# plt.subplot(1,5,1),plt.imshow(img)
# plt.xticks([]), plt.yticks([])
# plt.subplot(1,5,2),plt.imshow(dst)
# plt.xticks([]), plt.yticks([])

# blur = cv2.GaussianBlur(img,(5,5),0)
# median = cv2.medianBlur(img,5)
# biblur = cv2.bilateralFilter(img,9,75,75)

# izzz = [blur, median, biblur]
# for i in range(3):
#     plt.subplot(1,5,i+3),plt.imshow(img)
#     plt.xticks([]), plt.yticks([])
# plt.show()

#EDGE DETECTION

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('sudoku.jpg',0)

# laplacian = cv2.Laplacian(img,cv2.CV_64F)
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# plt.subplot(2,2,1)
# plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])

# plt.subplot(2,2,2)
# plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

# plt.subplot(2,2,3)
# plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

# plt.subplot(2,2,4)
# plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

# plt.show()

#CONTOURS

import numpy as np
import cv2
from matplotlib import pyplot as plt

im = cv2.imread('dp2.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(imgray, contours, -1, (0,0,0), 3)
plt.imshow(img, 'gray')
plt.show()
cv2.destroyAllWindows()
