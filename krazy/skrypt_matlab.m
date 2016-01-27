close all

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
plot(ones(1,length(z))*0.4,'--')
plot(ones(1,length(z))*0.4,'--')
title('z')



%%

figure(2)
subplot(2,1,1)
plot(zk)
hold on
plot(ones(1,length(zk))*0.4,'--')
title('z kalman')
subplot(2,1,2)
plot(vzk)
title('z cam')
%%
% figure(3)
% subplot(3,1,1)
% plot(roll)
% title('roll dreon')
% subplot(3,1,2)
% plot(yk)
% hold on
% plot(zeros(1,length(yk)),'--')
% hold on
% plot(zeros(1,length(zk)),'--')
% title('z kalman')
% subplot(3,1,3)
% plot(z)
% title('z cam')
%% 
figure(3)
subplot(2,1,1)
plot(roll_con)
hold on
plot(rolld)
plot(rollk)
plot(yd*50)
legend('roll con','roll dron','roll kalman','y')
grid on
%%
subplot(2,1,2)
plot(pitch_con)
hold on
plot(pitchd)
plot(xd*50)
legend('pitch con','pitch dron','x')
grid on
%%
figure(4)
plot(x,y)
hold on
plot(x(1),y(1),'.r')
plot(x(end),y(end),'.g')
axis([-1,1,-1,1])
%%
figure(5)
plot3(x,y,z)
hold on
plot3(x(1),y(1),z(1),'.r')
plot3(x(end),y(end),z(end),'.g')
axis([-1,1,-1,1,0,2])
grid on


