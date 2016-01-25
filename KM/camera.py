import numpy as np
import cv2

def position(hsv,color_low,color_upper):
    area = [0,0]
    ind = 0
    cx = -1
    cy = -1
    contour_max = 0

    mask = cv2.inRange(hsv,color_low,color_upper)
#     cv2.imshow('mask',mask)

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if(len(contours)):
        area = range(len(contours))
        for index in range(len(contours)):
            area[index] = cv2.contourArea(contours[index])

        ind = np.argmax(area)
#         print(area[ind])

    if area[ind] > 0.2:
        M = cv2.moments(contours[ind])
        contour_max = contours[ind]
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

    return cx,cy,contour_max

def rysowanie(frame,x,y,contour_max,color,yy):
    cv2.putText(frame,'R: x = {0} y = {1}'.format(x,y),(20,yy), cv2.FONT_HERSHEY_SIMPLEX, 1,color,2)
    cv2.circle(frame,(x,y), 2, (255,0,255), -1)
    cv2.drawContours(frame,[contour_max], 0, (255,0,255), 2)


# def wykrywanie():
##################################################################################

lower_green = np.array([60,100,100])
upper_green = np.array([90,255,255])

###################################################################################
# cap = cv2.VideoCapture(1)
# if cap.isOpened():
#     cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,1280)
#     cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,960)
#
#
#     # cap.set(cv2.cv.CV_CAP_PROP_FRAME_COUNT,960)
#
# print cap.get(3)
# print cap.get(4)
# print cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)


# while(cap.isOpened()):
while True:
#     ret, img = cap.read()
#     img =  cv2.cvtColor(img, cv2.cv.CV_GRAY2RGB)
    a=cv2.cv.CaptureFromCAM(1)

    imgFrame=cv2.cv.QueryFrame(a)
    print imgFrame
    # cv2.cv.SetImageCOI(imgFrame,1)
    #
    # bayer=cv2.cv.CreateImage(cv2.cv.GetSize(imgFrame),cv2.cv.IPL_DEPTH_8U,1)
    # cv2.cv.Copy(imgFrame,bayer,None)
    # print "test"
    # img=cv2.cv.CreateImage(cv2.cv.GetSize(imgFrame),cv2.cv.IPL_DEPTH_8U,3)
    # cv2.cv.CvtColor(bayer,img,cv2.cv.CV_BayerGB2RGB)
#
#     blur = cv2.blur(frame,(5,5))
#
#     b,g,r = cv2.split(blur)
#     b -= 100
#     r -= 100
#     frame_mod = cv2.merge((b,g,r))
# #         cv2.imshow('blur',frame_mod)
#     hsv = cv2.cvtColor(frame_mod, cv2.COLOR_BGR2HSV)
#     x,y,contour_max = position(hsv,lower_green, upper_green)
# #     print("x = {0} y = {1} area = {3}".format(x,y,area))
#     if(x > 0):
#         rysowanie(frame,x, y, contour_max,(0,0,255),30)
#
#     # return x,y

    cv2.imshow('frame',a)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# cap.release()
cv2.destroyAllWindows()
