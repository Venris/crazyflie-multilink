import numpy as np

a=np.array([[1,2],[3,4],[5,6]])
print a
for i in range (7,10,2):
    print np.delete(a,0,0)
    b=np.delete(a,0,0)
    print b
    a=np.append(a,[i,i+1])
    print a
