import cv2
import numpy as np
from matplotlib import pyplot as plt

oimg = cv2.cvtColor(cv2.imread("dp2.jpg"), cv2.COLOR_RGB2BGR)
grayimg = cv2.cvtColor(oimg, cv2.COLOR_BGR2GRAY)
ret, bnwimg = cv2.threshold(grayimg, 127, 255, cv2.THRESH_BINARY)

titles = ['Original Pic', 'Grayscale Pic', 'B&W Binary']
images = [oimg, grayimg, bnwimg]

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

cv2.imwrite('dpgray.jpg', grayimg)