from liczu import liczu

def fuzzyZ(ex, v):
    # regulator wysokosci
    
    # x - blad w danej osi
    # v - predkosc
    
    ## przynaleznosci blad wysokosci
    R=[[0,0,0],[0,0,0],[0,0,0]]
    uz = [0, 0, 0];
    x = ex;
    
    # zero
    a = -30;
    b = 0;
    c = 30;
    uz[1] = liczu(x,a,b,c,2);
    
    # bardzo nisko
    a = 0;
    b = 30;
    uz[2] = liczu(x,a,b,c,3);
    
    # bardzo wysoko
    b = -30;
    c = 0;
    uz[0] = liczu(x,a,b,c,1);
    
    ## przynaleznosci predkosci
    
    uv = [0, 0, 0];
    x = v;
    
    # zero
    a = -1;
    b = 0;
    c = 1;
    uv[1] = liczu(x,a,b,c,2);
    
    # w gore
    a = 0;
    b = 1;
    uv[2] = liczu(x,a,b,c,3);
    
    # w dol
    b = -1;
    c = 0;
    uv[0] = liczu(x,a,b,c,1);
    
    ## sterowanie
    # sterX = [55, 60, 65, 70, 80]; #DRON 40/2M
    # sterX = [55, 60, 65, 70, 80];
    sterX = [55, 60, 68, 70, 80];


    for i in range(len(uz)):
        for j in range(len(uv)):
            R[i][j] = uz[i] * uv[j];
        
    uy=[0,0,0,0,0]
    
    uy[0] = R[0][2];
    uy[1] = max(R[0][1], R[1][2]);
    uy[2] = max([R[0][0], R[1][1], R[2][2]]);
    uy[3] = max(R[1][0], R[2][1]);
    uy[4] = R[2][0];
    
    num = 0;
    for i in range(len(uy)):
        num = num + uy[i]* sterX[i];
    
    
    Sterowanie = num/ sum(uy);
    return Sterowanie

def fuzzyX(ex, v):
    # regulator wysokosci

    # x - blad w danej osi
    # v - predkosc

    ## przynaleznosci blad wysokosci
    R=[[0,0,0],[0,0,0],[0,0,0]]
    uz = [0, 0, 0];
    x = ex;

    # zero
    a = -20;
    b = 0;
    c = 20;
    uz[1] = liczu(x,a,b,c,2);

    # bardzo nisko
    a = 0;
    b = 20;
    uz[2] = liczu(x,a,b,c,3);

    # bardzo wysoko
    b = -20;
    c = 0;
    uz[0] = liczu(x,a,b,c,1);

    ## przynaleznosci predkosci

    uv = [0, 0, 0];
    x = v;

    # zero
    a = -0.2;
    b = 0;
    c = 0.2;
    uv[1] = liczu(x,a,b,c,2);

    # w gore
    a = 0;
    b = 0.2;
    uv[2] = liczu(x,a,b,c,3);

    # w dol
    b = -0.2;
    c = 0;
    uv[0] = liczu(x,a,b,c,1);

    ## sterowanie
    sterX = [-10, -5, 0, 5, 10];

    for i in range(len(uz)):
        for j in range(len(uv)):
            R[i][j] = uz[i] * uv[j];

    uy=[0,0,0,0,0]

    uy[0] = R[0][2];
    uy[1] = max(R[0][1], R[1][2]);
    uy[2] = max([R[0][0], R[1][1], R[2][2]]);
    uy[3] = max(R[1][0], R[2][1]);
    uy[4] = R[2][0];

    num = 0;
    for i in range(len(uy)):
        num = num + uy[i]* sterX[i];


    Sterowanie = num/ sum(uy);
    return Sterowanie

def fuzzyY(ex, v):
    # regulator wysokosci

    # x - blad w danej osi
    # v - predkosc

    ## przynaleznosci blad wysokosci
    R=[[0,0,0],[0,0,0],[0,0,0]]
    uz = [0, 0, 0];
    x = ex;

    # zero
    a = -20;
    b = 0;
    c = 20;
    uz[1] = liczu(x,a,b,c,2);

    # bardzo nisko
    a = 0;
    b = 20;
    uz[2] = liczu(x,a,b,c,3);

    # bardzo wysoko
    b = -20;
    c = 0;
    uz[0] = liczu(x,a,b,c,1);

    ## przynaleznosci predkosci

    uv = [0, 0, 0];
    x = v;

    # zero
    a = -0.2;
    b = 0;
    c = 0.2;
    uv[1] = liczu(x,a,b,c,2);

    # w gore
    a = 0;
    b = 0.2;
    uv[2] = liczu(x,a,b,c,3);

    # w dol
    b = -0.2;
    c = 0;
    uv[0] = liczu(x,a,b,c,1);

    ## sterowanie
    sterX = [-10, -5, 0, 5, 13];

    for i in range(len(uz)):
        for j in range(len(uv)):
            R[i][j] = uz[i] * uv[j];

    uy=[0,0,0,0,0]

    uy[0] = R[0][2];
    uy[1] = max(R[0][1], R[1][2]);
    uy[2] = max([R[0][0], R[1][1], R[2][2]]);
    uy[3] = max(R[1][0], R[2][1]);
    uy[4] = R[2][0];

    num = 0;
    for i in range(len(uy)):
        num = num + uy[i]* sterX[i];


    Sterowanie = num/ sum(uy);
    return Sterowanie

def fuzzydron(ex, v):
    # regulator wysokosci

    # x - blad w danej osi
    # v - predkosc

    ## przynaleznosci blad wysokosci
    R=[[0,0,0],[0,0,0],[0,0,0]]
    uz = [0, 0, 0];
    x = ex;

    # zero
    a = -0.20;
    b = 0;
    c = 0.20;
    uz[1] = liczu(x,a,b,c,2);

    # bardzo nisko
    a = 0;
    b = 0.20;
    uz[2] = liczu(x,a,b,c,3);

    # bardzo wysoko
    b = -0.20;
    c = 0;
    uz[0] = liczu(x,a,b,c,1);

    ## przynaleznosci predkosci

    uv = [0, 0, 0];
    x = v;

    # zero
    a = -0.2;
    b = 0;
    c = 0.2;
    uv[1] = liczu(x,a,b,c,2);

    # w gore
    a = 0;
    b = 0.2;
    uv[2] = liczu(x,a,b,c,3);

    # w dol
    b = -0.2;
    c = 0;
    uv[0] = liczu(x,a,b,c,1);

    ## sterowanie
    # sterX = [-10, -5, 0, 5, 10];
    sterX = [-15, -5, 0, 5, 15];

    for i in range(len(uz)):
        for j in range(len(uv)):
            R[i][j] = uz[i] * uv[j];

    uy=[0,0,0,0,0]

    uy[0] = R[0][2];
    uy[1] = max(R[0][1], R[1][2]);
    uy[2] = max([R[0][0], R[1][1], R[2][2]]);
    uy[3] = max(R[1][0], R[2][1]);
    uy[4] = R[2][0];

    num = 0;
    for i in range(len(uy)):
        num = num + uy[i]* sterX[i];


    Sterowanie = num/ sum(uy);
    return Sterowanie

def fuzzyKat(ex,v):

    maxY=30
    minY=-30
    k1o=0.5
    k2o=0.5
    Y=-k1o*ex-k2o*v
    if Y>maxY:
        Y=maxY
    if Y<minY:
        Y=minY

    return Y