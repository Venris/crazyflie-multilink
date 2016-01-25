function u = liczu(x,a,b,c, index)

if index == 2 
    if (x >= a) && (x <= b)
        u = (x-a)/ (b-a);
    elseif (x > b) && (x <= c)
        u = (c-x)/ (c-b);
    else
        u = 0;
    end
    
elseif index == 1
    if (x >= b) && (x <= c)
        u = (c-x)/ (c-b);
    elseif x < b
        u = 1;
    else
        u = 0;
    end
    
elseif index == 3
    if (x >= a) && (x <= b)
        u = (x-a)/ (b-a);
    elseif x > b 
        u = 1;
    else
        u = 0;
    end
else
    u = 0;
end