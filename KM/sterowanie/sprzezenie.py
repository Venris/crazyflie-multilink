
def control(wys_z,wys,Vwys,orient,x_z,x,Vx,y_z,y,Vy):

    # wysokosc
    maxT=80
    minT=50
    k1h=0.5
    k2h=10
    T=60+k1h * (wys_z - wys) - k2h*Vwys
    if T>maxT:
        T=maxT
    elif T<minT:
        T=minT

    # yaw
    maxY=10
    minY=-10
    ko=1
    Y=-ko*orient
    if Y>maxY:
        Y=maxY
    if Y<minY:
        Y=minY

    # roll
    grR=10
    k1r=-1
    k2r=0.15
    R=k1r * (y_z - y) - k2r*Vy
    if R>grR:
        R=grR
    elif R<-grR:
        R=-grR

    #pitch
    grP=10
    k1p=1
    k2p=0.15
    P=k1p * (y_z - y) - k2p*Vy
    if P>grP:
        P=grP
    elif P<-grP:
        P=-grP


    return T,Y,R,P