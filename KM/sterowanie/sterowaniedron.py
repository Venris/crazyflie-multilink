from fuzzy import fuzzyZ
x = [0,0, 0, 0];
x0 = [0, 0, 50, 0];

v = [0, 0, -3, 0];

ex = x0[0] - x[0];
ey = x0[1] - x[1];
ez = x0[2] - x[2];
eyaw = x0[3] - x[3];

T = fuzzyZ(ez,v[2])
print T