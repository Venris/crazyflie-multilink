function Sterowanie = fuzzyZ(ex, v)
clc
% regulator wysokosci

% x - blad w danej osi
% v - predkosc

%% przynaleznosci blad wysokosci
uz = [0 0 0];
x = ex;

% zero
a = -30;
b = 0;
c = 30;
uz(2) = liczu(x,a,b,c,2);

% bardzo nisko
a = 0;
b = 30;
uz(3) = liczu(x,a,b,c,3);

% bardzo wysoko
b = -30;
c = 0;
uz(1) = liczu(x,a,b,c,1);

%% przynaleznosci predkosci

uv = [0 0 0];
x = v;

% zero
a = -0.3;
b = 0;
c = 0.3;
uv(2) = liczu(x,a,b,c,2);

% w gore
a = 0;
b = 0.3;
uv(3) = liczu(x,a,b,c,3);

% w dol
b = -0.3;
c = 0;
uv(1) = liczu(x,a,b,c,1);

%% sterowanie
sterX = [40, 50, 65, 70, 80];

for i = 1: length(uz)
    for j = 1: length(uv)
        R(i,j) = uz(i) * uv(j);
    end
end

uy(1) = R(1,3);
uy(2) = max(R(1,2), R(2,3));
uy(3) = max([R(1,1) R(2,2) R(3,3)]);
uy(4) = max(R(2,1), R(3,2));
uy(5) = R(3,1);

num = 0;
for i = 1: length(uy)
    num = num + uy(i)* sterX(i);
end

Sterowanie = num/ sum(uy);
