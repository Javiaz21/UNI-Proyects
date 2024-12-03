% Actividad 9 - Sistemas Inteligentes IV
% Javier Ignacio Díaz López
% 220839937
% 15/10/2023

clear all
close all
clc

df = readtable('df_agrupacion_1.csv');
% df = readtable('df_agrupacion_3.csv');
% df = readtable('df_agrupacion_4.csv');
% df = readtable('df_agrupacion_6.csv');

x1 = df.x1;
x2 = df.x2;
X = [x1 x2];

n = size(X,1);

M = 1;
I = randperm(n);

W = X(I(1:M),:);

G = zeros(1,n);

for j=1:50
    cla
    hold on
    grid on 

    for i=1:M
        plot(x1(G==i), x2(G==i), 'o', 'LineWidth', 2)
        
        plot(W(i,1), W(i,2), 'sk', 'LineWidth', 3)
    end
        
    for i=1:n
        D = sqrt((X(i,1)-W(:,1)).^2+(X(i,2)-W(:,2)).^2);
        [~,b] = min(D);

        G(i) = b;
    end

    for i=1:M
        W(i,:) = mean(X(G==i,:));
    end
end 


% >>>for df_agrupacion_1<<<
% for i=1:n
%     if sqrt(x1(i).^2+x2(i).^2)>0.63
%         plot(x1(i), x2(i), 'o', 'LineWidth', 2,'Color','r')
%     end
% end