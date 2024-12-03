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
d = 7;
X = x.^(0:d);

lambda = 0.001;
I = eye(d+1, d+1);

w = inv(X'*X+lambda*I)*X'*Y;

Yp = X*w;


R2 = 1-(sum((Y-Yp).^2))/(sum((Y-mean(Y)).^2))

figure
grid on 
hold on
title('Regresión Ridge (polinomio grado 7)')
xlabel('time');
ylabel('temp');
plot(x,Y,'*','LineWidth',5)
plot(x,Yp,'r-','LineWidth',3)