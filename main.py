import cv2
from PIL import Image
import numpy as np
from renk_algila import get_limits

frameTime = 30

yellow = [0,0,255]
cap = cv2.VideoCapture('vid_1.avi')
while (cap.isOpened):
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit =np.array([160,50,50])
    upperLimit = np.array([180,255,255])
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    
    mask_=Image.fromarray(mask)
    
    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0),5)
    cv2.imshow('frame',mask)
    if cv2.waitKey(frameTime) & 0xFF == ord('q'):
        break
cap.release()
 

cv2.destroyAllWindows()