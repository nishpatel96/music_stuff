""" Draw the piano in this module"""
import math
import draw_piano as piano
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame,(810,600))
    frame = cv2.flip(frame,1)
    # frame = cv2.GaussianBlur(frame,(5,5),0)
    # #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # Make a copy of image to add transparent piano later
    overlay = frame.copy()
    #

    # Draw the piano keys
    x1 = 2
    y1 = 300
    for i in range(13):
        if i==0 or i==5 or i==12:
            key = piano.L_key(x1, y1)
            key.drawKey(frame)
            x1 = x1 + 60
        elif i==2 or i==7 or i==9:
            key = piano.uKey(x1, y1)
            key.drawKey(frame)
            x1 = x1 + 60
        elif i==4 or i==11:
            key = piano.backLKey(x1, y1)
            key.drawKey(frame)
            x1 = x1 + 60
        elif i == 1 or i==3 or i==6 or i==8 or i==10:
            key = piano.blackKey(x1, y1)
            key.drawKey(frame)
            x1 = x1 + 60

    # hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #
    # lower_black = np.array([0,0,0]) # get the proper values from experimenting with trackbar.
    # upper_black = np.array([255,255,50])
    # mask = cv2.inRange(hsv, lower_black, upper_black)
    
    # contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #
    # for contour in contours:   
    #     if cv2.contourArea(contour)>14000 and cv2.contourArea(contour)<26000:
    #         # print(cv2.contourArea(contour))
    #         cv2.drawContours(frame, contour,-1,(0,0,255),3)
    #
    #         hull = cv2.convexHull(contour,returnPoints = False)
    #         defects = cv2.convexityDefects(contour,hull)
    #
    #         for i in range(defects.shape[0]):
    #             s,e,f,d = defects[i,0]
    #             start = tuple(contour[s][0])
    #             end = tuple(contour[e][0])
    #             far = tuple(contour[f][0])
    #             x,y,p,q=start[0],start[1],far[0],far[1]
    #             dist = math.sqrt((x - p)**2 + (y - q)**2)
    #
    #             # cv2.line(frame,start,end,[0,255,0],2) draws the convex hull polygon.
    #             if (dist>=50):
    #                 cv2.circle(frame,start,5,[20,240,255],-1) # draws the finger tips.
    
    alpha = 0.5  # Transparency factor.

    # Following line overlays transparent rectangle over the image
    cv2.addWeighted(frame, alpha, overlay, 1 - alpha, 0, overlay)

    cv2.imshow('frame',overlay)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
