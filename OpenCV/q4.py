import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("shapes.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# n=2
# kernel = np.ones((n,n),np.float32)/(n*n)
# dst = cv2.filter2D(img,-1,kernel)
_,thresh = cv2.threshold(img, 240,255, cv2.THRESH_BINARY)

countours,_ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for cnt in countours:
    apcnt = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)
    cv2.drawContours(img, [apcnt], 0, (0,0,255), 3)
    x = apcnt.ravel()[0]
    y = apcnt.ravel()[1]
    if len(apcnt) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(apcnt) == 4:
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(apcnt)
        barea = w*h
        if barea/area>0.98 and barea/area<1.02:
            ar = w/h
            if ar>0.98 and ar<1.02: #We should keep a margin of error due to the noise
                cv2.putText(img, "Square", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
            else:
                cv2.putText(img, "Rectangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        else:
            cv2.putText(img, "Diamond/Rhombus", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
           
    else:
        x, y, w, h = cv2.boundingRect(apcnt)
        ar = w/h
        if ar>0.98 and ar<1.02:
            cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        else:
            cv2.putText(img, "Oval", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))   


plt.imshow(img,'gray')
plt.show()

