import numpy as np
#from PIL import Image
import cv2
from matplotlib import pyplot as plt

def getSquare(im, threshold):
    from PIL import Image
    im = im.crop(getBox(im, threshold))
    return im

def getNumpySquare(im, Y1, Y2, X1, X2):
    #This is called numpy slicing.
    #NOTE: its im[y:y+h, x:x+w] 
    #We first supply the startY and endY coordinates, followed by the startX and endX coordinates to the slice.
    #so [Y1:Y2, X1:X2] 
    im = im[Y1:Y2, X1:X2]
    return im
    

img = cv2.imread("/home/copypasta/CST205/handwriting/testSubjects/test1.JPG")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#res = cv2.resize(img,None, fx=.5, fy=.5, interpolation = cv2.INTER_AREA)
img = getSquare(img, 75)
img = cv2.resize(img, (0,0), fx=0.01, fy=0.01)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    print x,y


plt.imshow(img),plt.show()
