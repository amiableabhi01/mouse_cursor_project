import cv2
import numpy as np
def nothing(x):
    pass
# Create a black image, a window
kernel = np.zeros((300,512,3), np.uint8)
name = 'Calibrate' 
cv2.namedWindow(name)
# create trackbars for color change
cv2.createTrackbar('Hue', name, 0, 255, nothing)
cv2.createTrackbar('Sat', name, 0, 255, nothing)
cv2.createTrackbar('Val', name, 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch, name,0,1,nothing)

while(1):
    cv2.imshow(name,kernel)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

   # get current positions of four trackbars
    hue = cv2.getTrackbarPos('Hue', name)
    sat = cv2.getTrackbarPos('Sat', name)
    val = cv2.getTrackbarPos('Val', name)
    s = cv2.getTrackbarPos(switch,name)
    
    if s == 0:
        kernel[:] = 0
    else:
        kernel[:] = [hue,sat,val]

cv2.destroyAllWindows()
