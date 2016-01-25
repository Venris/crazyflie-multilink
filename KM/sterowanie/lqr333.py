def control(wys_z,wys,Vwys,orient,x_z,x,Vx,y_z,y,Vy):

    # wysokosc
    maxT=80
    minT=50
    k1h=0.5
    k2h=20.0
    T=60+(k1h * (wys_z - wys) - k2h*Vwys)
    if T>maxT:
        T=maxT
    elif T<minT:
        T=minT
    R=0
    P=0
    Y=0
    return T,R,P,Y