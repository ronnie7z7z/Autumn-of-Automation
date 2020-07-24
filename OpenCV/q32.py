import cv2
 
capture = cv2.VideoCapture(0)
 
while(True):
     
    ret, img = capture.read()
    #Choose what you want boiii
    img =cv2.Canny(img,20,100)
    # img = cv2.Laplacian(img,cv2.CV_8U)
    # img = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
    # img = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)  
    cv2.imshow('video', img)
     
    if cv2.waitKey(1) == 27:
        break
 
capture.release()
cv2.destroyAllWindows()