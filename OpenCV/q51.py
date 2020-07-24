import cv2
import numpy as np


capture = cv2.VideoCapture('messi.mp4')
while(True):
     
    ret, frame = capture.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # n=2
    # kernel = np.ones((n,n),np.float32)/(n*n)
    # img = cv2.filter2D(img,-1,kernel)
    img = cv2.GaussianBlur(img,(5,5),0)
    _,thresh = cv2.threshold(img, 160,255, cv2.THRESH_BINARY)
    countours,_ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for cnt in countours:
        apcnt = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)
        # cv2.drawContours(frame, [apcnt], 0, (0,0,0), 3)
        # (x,y),radius = cv2.minEnclosingCircle(cnt)
        # center = (int(x),int(y))
        # radius = int(radius)
        # img = cv2.circle(frame,center,radius,(0,255,0),2)
        x = apcnt.ravel()[0]
        y = apcnt.ravel()[1]
        if len(apcnt) > 8 and cv2.contourArea(apcnt)<3000 and cv2.contourArea(apcnt)>400:
            a, b, w, h = cv2.boundingRect(apcnt)
            ar = w/h
            if ar>1 and ar<1.22:
                (x,y),radius = cv2.minEnclosingCircle(cnt)
                center = (int(x),int(y))
                radius = int(radius)
                img = cv2.circle(frame,center,radius,(0,255,0),2)
                cv2.putText(img, 'ball', (a,b), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))

     
    cv2.imshow('Messi', frame)
    if cv2.waitKey(30) == 27:
        break
 
capture.release()
cv2.destroyAllWindows()