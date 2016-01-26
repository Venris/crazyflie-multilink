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
plot(zk)
hold on
plot(zeros(1,length(zk)),'--')
title('z kalman')
subplot(3,1,3)
plot(z)
title('z cam')

figure(3)
subplot(3,1,1)
plot(roll)
title('roll dreon')
subplot(3,1,2)
plot(yk)
hold on
plot(zeros(1,length(yk)),'--')
% hold on
% plot(zeros(1,length(zk)),'--')
% title('z kalman')
% subplot(3,1,3)
% plot(z)
% title('z cam')
% 







