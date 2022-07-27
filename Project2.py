#RealTime Color Detection

#The main idea is to convert the input RGB image (BGR in the case of OpenCV because that’s how images are formatted in this module)
# to HSV format, which will make it easier for us to mask the specific color out of the frame.
# That is, whatever color in the provided HSV range will be given a value of 255 and
# others will be simply 0, and as a result,
# every object with color in the specified range will change to white leaving the rest of the image i.e. background black.
#To show the color we need to bitwise and the current frame with the mask.
# For this, there is an inbuilt function called bitwise_and()
#importing the libraries
import cv2
import numpy as np

#Initializing the Camera

FW = 300
FH = 200
cap = cv2.VideoCapture(0)
cap.set(3, FW)
cap.set(4, FH)

def empty(a):
    pass
# Introduce Trackbar in new window
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
# create Trackbar
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)

while True:

    Success, img = cap.read()
    # Convert color format from BGR to HSV
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

   # get Trackback values to filter a color
    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
  # Create a mask that will give us values that are in this range
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,upper)
    result = cv2.bitwise_and(img,img, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([mask,result,img])

    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
