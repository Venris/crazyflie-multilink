% clear all

figure(1)

subplot(3,1,1)
plot(zeros(1,length(x)),'--')
hold on
plot(x)

plot(xk)
title('x')

subplot(3,1,2)
plot(y)
hold on
plot(yk)
title('y')

subplot(3,1,3)

plot(z)
hold on
plot(zk)
title('z')




figure(2)
subplot(3,1,1)
plot(thrust)
title('thrust')
subplot(3,1,2)
plot(zd)
hold on
plot(zeros(1,length(zd)),'--')
title('z dron')
subplot(3,1,3)
plot(vzk)
title('Vz kalman')





