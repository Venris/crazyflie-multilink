
def control(e_wys,Vwys,orient,vorient,e_x,Vx,e_y,Vy):

    # wysokosc
    maxT=80
    minT=55
    k1h=50
    k2h=60
    T=60+k1h * e_wys - k2h*Vwys   # dron 40/2M k1=50,k2=53,ff=60
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
    grR=10
    k1r=10
    k2r=20
    R=-1*(k1r * e_y - k2r*Vy)
    if R>grR:
        R=grR
    elif R<-grR:
        R=-grR

    #pitch
    grP=10
    k1p=10
    k2p=20
    P=k1p * e_x - k2p*Vx
    if P>grP:
        P=grP
    elif P<-grP:
        P=-grP


    return T,Y,R,P