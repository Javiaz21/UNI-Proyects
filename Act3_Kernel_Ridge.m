% Actividad 3 - Sistemas Inteligentes IV
% Javier Ignacio Díaz López
% 220839937
% 03/09/2023

clear all
close all
clc

df = readtable('temp.csv');

x = df.time;
Y = df.temp;

% kernel = @(xi,xj) xi*xj'+1;
% kernel = @(xi,xj) (xi*xj'+1)^2;
% kernel = @(xi,xj) exp(-0.1*norm(xi-xj)^2);
kernel = @(xi,xj) tanh(-0.1*(xi*xj')+1);

n = size(x,1);
K = zeros(n,n);

for i=1:n
    for j=1:n
        K(i,j) = kernel(x(i,:),x(j,:));
    end
end

lambda = 1;
alpha = inv(K+lambda*eye(n,n))*Y;
Yp = K*alpha;

R2 = 1-(sum((Y-Yp).^2))/(sum((Y-mean(Y)).^2))

figure
grid on 
hold on
title('Regresión Kernel Ridge (Kernel Polinomial Sigmoidal \lambda=1)')
xlabel('time');
ylabel('temp');
plot(x,Y,'*','LineWidth',5)
plot(x,Yp,'r-','LineWidth',3)


