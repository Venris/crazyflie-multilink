from numpy import cos

def control(e_wys,Vwys,orient,vorient,e_x,Vx,e_y,Vy,roll, pitch,vroll,vpitch):

    # wysokosc
    maxT=85
    minT=55
    k1h=50
    k2h=53
    T1=60+k1h * e_wys - k2h*Vwys   # dron 40/2M k1=50,k2=53,ff=60
    T=T1/(cos(roll)*cos(pitch))
    if T>maxT:
        T=maxT
    elif T<minT:
        T=minT
    # T=0

    # yaw
    maxY=50
    minY=-50
    ko=20
    kvo=20
    Y=ko*orient-kvo*vorient
    if Y>maxY:
        Y=maxY
    if Y<minY:
        Y=minY

    # roll
    grR=15
    k1r=1
    k2r=1
    k3r=0.3
    k4r=0.5

    R=-1*(k1r * e_y - k2r*Vy +k3r*roll +k4r*vroll)
    if R>grR:
        R=grR
    elif R<-grR:
        R=-grR

    #pitch

    P=k1r * e_x - k2r*Vx - k3r*pitch -k4r*vpitch
    if P>grR:
        P=grR
    elif P<-grR:
        P=-grR


    return T,Y,R,P