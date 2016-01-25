import numpy as np

def wzorProst3d(p1,p2):
    wsp = np.array([p1[0],(p2[0]-p1[0]),p1[1],(p2[1]-p1[1]),p1[2],(p2[2]-p1[2])])
    return wsp

def plaszczyznaRownolegla(p1,p2,p3):
    p12 = np.array([p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]])
    p13 = np.array([p3[0]-p1[0],p3[1]-p1[1],p3[2]-p1[2]])
    wek = np.cross(p12,p13)
    A = wek[0]
    B = wek[1]
    C = wek[2]
    D = -A*p1[0] - B*p1[1] - C*p1[2]
    return A,B,C,D

def punktPrzeciecia(A,B,C,D,wsp):
    t = (-D - A*wsp[0] - B*wsp[2] - C*wsp[4]) / (A*wsp[1] + B*wsp[3] + C*wsp[5])
    x = wsp[1]*t + wsp[0]
    y = wsp[3]*t + wsp[2]
    z = wsp[5]*t + wsp[4]
    return x,y,z

def plaszczyznaProsotopadla(wsp,x,y,z):
    A = wsp[1]
    B = wsp[3]
    C = wsp[5]
    D = -A*x - B*y - C*z
    return A,B,C,D


def position_estimate(xp1,yp1,xp2,yp2):
    H = 2.0  # wysokosc kamery gornej
    h = 0.4  # wyokosc kamery bocznej
    L = 2.5  # odleglosc w Y kabery bocznej pod punkut(0,0,0)
    corner_kam_gora = np.array([(4.0/3.0),-1.0,0.0])
    width_gora = 8.0/3.0
    hight_gora = 2.0
    corner_kam_bok = np.array([-1.6,1.0,1.6])
    width_bok = 3.2
    hight_bok = 2.4

    #kamera gorna piksele
    pkam_gora = np.array([0.0, 0.0, H])
    ppik_gora = np.array([(corner_kam_gora[0] - width_gora/1280.0*xp1),(corner_kam_gora[1] + hight_gora/960.0*yp1),corner_kam_gora[2]])
    wsp_gora = wzorProst3d(pkam_gora, ppik_gora)
    #piksel pomocniczy do wyznaczania plaszczyzny
    ppik1_gora = np.array([-ppik_gora[0]+0.0001,ppik_gora[1],ppik_gora[2]])

    #kamera boczna piksele
    pkam_bok = np.array([0.0, -L, h])
    ppik_bok = np.array([(corner_kam_bok[0]+width_bok/640.0*xp2),corner_kam_bok[1],(corner_kam_bok[2]-hight_bok/480.0*yp2)])
    wsp_bok = wzorProst3d(pkam_bok, ppik_bok)

    #plaszczyzna rownolegla do piksela gornego i przechodzaca przez piksel pomocniczy
    A,B,C,D = plaszczyznaRownolegla(pkam_gora, ppik_gora, ppik1_gora)

    #punkt przeciecia plaszczyzny rownoleglej z pikselem kamery bocznej
    x1,y1,z1 = punktPrzeciecia(A, B, C, D, wsp_bok)

    #plaszczyzna prostopadla do piksela gornego i przechodzaca przez punkt(x1,y1,z1)
    A1,B1,C1,D1 = plaszczyznaProsotopadla(wsp_gora, x1, y1, z1)

    #punkt przecia plaszczyzny prosotpadlej z pikselem kamery gornej
    x2,y2,z2 = punktPrzeciecia(A1, B1, C1, D1, wsp_gora)

    #przyplizone polozenie drona
    x = (x1 + x2) / 2.0
    y = (y1 + y2) / 2.0
    z = (z1 + z2) / 2.0

    return x,y,z






######################################################################################

x,y,z = position_estimate(240, 820, 490, 280)

dron = [x,y,z]
print(dron)




