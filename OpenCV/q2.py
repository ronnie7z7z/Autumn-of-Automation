import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.cvtColor(cv2.imread("as2.png"), cv2.COLOR_RGB2BGR)
rows,cols,z = img.shape

pts1 = np.float32([[130,195],[215,200],[50,350],[300,350]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg1 = cv2.warpPerspective(img,M,(300,300))


pts1 = np.float32([[130,195],[215,200],[130,270],[215,280]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg2 = cv2.warpPerspective(img,M,(300,300))

pts1 = np.float32([[0,0],[300,0],[0,350],[220,290]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg3 = cv2.warpPerspective(img,M,(300,300))

pts1 = np.float32([[150,215],[190,215],[150,240],[190,240]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg4 = cv2.warpPerspective(img,M,(300,300))

M = cv2.getRotationMatrix2D((cols/2,rows/2),70,1)
timg5 = cv2.warpAffine(img,M,(cols,rows))
pts1 = np.float32([[150,125],[300,125],[150,250],[300,250]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg5 = cv2.warpPerspective(timg5,M,(300,300))

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
timg6 = cv2.warpAffine(img,M,(cols,rows))
pts1 = np.float32([[100,75],[250,75],[100,180],[250,180]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg6 = cv2.warpPerspective(timg6,M,(300,300))

M = cv2.getRotationMatrix2D((cols/2,rows/2),25,1)
timg7 = cv2.warpAffine(img,M,(cols,rows))
pts1 = np.float32([[125,150],[250,150],[125,300],[250,300]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg7 = cv2.warpPerspective(timg7,M,(300,300))

M = cv2.getRotationMatrix2D((cols/2,rows/2),135,1)
timg8 = cv2.warpAffine(img,M,(cols,rows))
pts1 = np.float32([[150,75],[250,75],[150,200],[250,200]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg8 = cv2.warpPerspective(timg8,M,(300,300))

pts1 = np.float32([[130,195],[215,200],[130,270],[215,280]])
pts2 = np.float32([[0,0],[350,0],[0,350],[350,350]])
M = cv2.getPerspectiveTransform(pts1,pts2)
timg9 = cv2.warpPerspective(img,M,(300,300))
timg9 = cv2.bilateralFilter(timg9,20,100,75)

timg10 = cv2.bilateralFilter(img,20,100,75)

timg = [timg1, timg2, timg3, timg4, timg5, timg6, timg7, timg8, timg9, timg10]

for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(timg[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
