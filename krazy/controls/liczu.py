def  liczu(x,a,b,c, index):
    
    if index == 2 :
        if (x >= a) and (x <= b):
            u = (x-a)/ (b-a)
        elif (x > b) and (x <= c):
            u = (c-x)/ (c-b)
        else:
            u = 0
        
        
    elif index == 1:
        if (x >= b) and (x <= c):
            u = (c-x)/ (c-b)
        elif x < b:
            u = 1
        else:
            u = 0
        
        
    elif index == 3:
        if (x >= a) and (x <= b):
            u = (x-a)/ (b-a)
        elif x > b :
            u = 1
        else:
            u = 0
        
    else:
        u = 0
    
    return u