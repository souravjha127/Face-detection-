# FACE DETECTION IN AN IMAGE
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')# importing haarcascade model
img = cv2.imread('abc.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,9) # 1.1= ScaleFactor, 9 is minNeighbour -- Tunning parameters

for x,y,w,h in faces :
    img= cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    # cv2.rectangle(src, start point, end point , color , thickness)
cv2.imshow('FACE DETECTION',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
