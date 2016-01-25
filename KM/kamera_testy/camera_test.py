import numpy as np
import cv2
from time import sleep

i=0
cap = cv2.VideoCapture(1)

if(cap.isOpened()):
    print "kamera wlaczona"
    # print  cv2.cv.CV_CAP_PROP_FRAME_HEIGHT1
    ret1 = cap.set(3,1920)
    ret1 = cap.set(4,1080)
    print cap.get(cv2.CAP_PROP_FORMAT)
    # ret1 = cap.set(cv2.CAP_PROP_FRAME_COUNT,1.0)
    # print ret1
    print cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print cap.get(3)
    print cap.get(4)
#     print cap.get(cv2.cv.CV_CAP_PROP_FORMAT)


else:
    cap.open()

    # print ret1
# fourcc = cv2.cv.CV_FOURCC(*'DIVX')
# video = cv2.VideoWriter('video.avi',-1,5,(640,480))
while(cap.isOpened()):

    ret, frame = cap.read()
    # img=cv2.


    # frame2 = cv2.cvtColor(frame,cv2.COLOR_BAYER_GB2BGR)
    y,u,v = cv2.split(frame)

    # bayer = cv2.    CreateImage( cvGetSize(imgFrame), IPL_DEPTH_8U, 1);
    # cvCopy(imgFrame,bayer,NULL);
    y2 = cv2.cvtColor(y+u+v,cv2.COLOR_BAYER_BG2GRAY)
    # frame3 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if (i==0):
        print "ramka1\n",y
        print "\nramka2\n",y2
        # print "\nramka3\n",
        print y==y2
        i=1
        cv2.imwrite('frame.tif',frame)


    #
    # ret, gb = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
    #
    # gb = cv2.bitwise_not(gb)
    #
    # contour,hier = cv2.findContours(gb,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    #
    # for cnt in contour:
    #     cv2.drawContours(gb,[cnt],0,255,-1)
    # gray = cv2.bitwise_not(gb)
    #
    # cv2.drawContours(gray,contour,-1,(0,255,0),3)


    cv2.imshow('test', cv2.resize(y,(640,480)))
    cv2.imshow('test2', cv2.resize(y2,(640,480)))
    cv2.resizeWindow('test',640,480)
    # cv2.imshow('test3', v)
    # video.write(y)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# video.release()
cv2.destroyAllWindows()