import numpy as np
import cv2

#######################################################################################################
# FUNKCJE

def position(hsv,color_low,color_upper):
    area = [0,0]
    ind = 0
    cx = -1
    cy = -1
    contour_max = 0

    mask = cv2.inRange(hsv,color_low,color_upper)
    cv2.imshow('mask',mask)

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if(len(contours)):
        area = range(len(contours))
        for index in range(len(contours)):
            area[index] = cv2.contourArea(contours[index])

        ind = np.argmax(area)
        print(area[ind])

    if area[ind] > 1.0:
        M = cv2.moments(contours[ind])
        contour_max = contours[ind]
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

    return cx,cy,contour_max

# funkcja do rysowania na klatce
def rysowanie(frame,x,y,contour_max,color,yy):
    cv2.putText(frame,'B: x = {0} y = {1}'.format(x,y),(20,yy), cv2.FONT_HERSHEY_SIMPLEX, 1,color,2)
    cv2.circle(frame,(x,y), 3, (255,0,255), -1)
    cv2.drawContours(frame,[contour_max], 0, (255,0,255), 2)

# funkcja do wykrywania kata
def dec(img,color_low,color_upper,x,y):
    area = [0.0,0.0]
    indmax1 = 0
    indmax2 = 0
    dec = np.NaN
    cx1 = np.NaN
    cy1 = np.NaN
    cx2 = np.NaN
    cy2 = np.NaN

    mask = cv2.inRange(hsv,color_low,color_upper)
#     cv2.imshow('mask',mask)

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if(len(contours) > 1):
        area = range(len(contours))
        for index in range(len(contours)):
            area[index] = cv2.contourArea(contours[index])

        maxsort = np.argsort(area)
        indmax1 = maxsort[len(maxsort)-1]
        indmax2 = maxsort[len(maxsort)-2]
    if(area[indmax1] > 1.0 and area[indmax2]  > 1.0 ):
        M1 = cv2.moments(contours[indmax1])
        M2 = cv2.moments(contours[indmax2])
        # sodek 1 leda
        if(M1['m00'] != 0.0 and M2['m00'] != 0.0):
            cx1 = M1['m10']/M1['m00']
            cy1 = M1['m01']/M1['m00']
            # srodek 2 leda
            cx2 = M2['m10']/M2['m00']
            cy2 = M2['m01']/M2['m00']
            print("1 = {0:.2f},{1:.2f}  2 = {2:.2f},{3:.2f}".format(cx1,cy1,cx2,cy2))
            if(cx1 == cx2):
                if(cx1 >= x):
                    dec = 90.0
                else:
                    dec = -90.0
            else:
                a = (cy1-cy2)/(cx1-cx2)
                b = cy1 - a * cx1
                dec = np.arctan(a)*180.0/3.14159
                if(y < (a*x+b) and dec < 0.0):
                    dec = 180.0 + dec
                elif(y < (a*x+b) and dec > 0.0):
                    dec = -180.0 + dec
                elif(dec == 0.0 and y > cy1):
                    dec = 180.0


    print(dec)
    return dec,cx1,cy1,cx2,cy2

#######################################################################################################
# PROGRAM

cap = cv2.VideoCapture(1)

print( cap.isOpened())
print(cap.get(3))
print(cap.get(4))

# RED
lower_red = np.array([0,100,100])
upper_red = np.array([40,255,255])

 # GREEN
lower_green = np.array([60,80,80])
upper_green = np.array([75,255,255])

# BLUE
lower_blue = np.array([90,100,100])
upper_blue = np.array([110,255,255])


##########################################
# PETLA GLOWNA
# fourcc = cv2.cv.CV_FOURCC('XVID')
video = cv2.VideoWriter('video.avi',-1,5,(640,480))

while(cap.isOpened()):

    ret, frame = cap.read()
    blur = cv2.blur(frame,(3,3))
    cv2.imwrite('frame.jpg',frame)



    ##############################################################
    # WYKRYWANIE DRONA (RED)
    b,g,r = cv2.split(blur)
    b -= 50
    r -= 50
    blur_mod = cv2.merge((b,g,r))
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    x,y,contour_max = position(hsv,lower_green, upper_green)


    ##############################################################
    # WYKRYWANIE KATA (BLUE)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    kat,cx1,cy1,cx2,cy2 = dec(hsv,lower_blue, upper_blue,x,y)

    ##############################################################
    # RYSOWANIE
    if(x > 0):
        rysowanie(frame,x, y, contour_max,(0,0,255),30)
    if(not np.isnan(cx1)):
        cv2.line(frame,(int(cx1),int(cy1)),(int(cx2),int(cy2)),(255,0,0),2)
        cv2.putText(frame,'kat = {0:.2f}'.format(kat),(20,60), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2)


    cv2.imshow('frame',frame)
    video.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
video.release()
cv2.destroyAllWindows()
print("THE END")