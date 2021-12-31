import cv2  

img = cv2.imread('bottle3.jpg')
x, y = img.shape[0:2]
img = cv2.resize(img,(int(y / 10), int(x / 10)))
cv2.namedWindow("img",cv2.WINDOW_NORMAL)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret,binary = cv2.threshold(gray,35,255,cv2.THRESH_BINARY)  

binary,contours,hierarchy= cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
binary = cv2.cvtColor(binary,cv2.COLOR_GRAY2BGR)
cv2.drawContours(binary,contours,-1,(0,0,255))

cv2.imshow("img", binary)
#cv2.imshow("img", img)  
cv2.waitKey(0) 