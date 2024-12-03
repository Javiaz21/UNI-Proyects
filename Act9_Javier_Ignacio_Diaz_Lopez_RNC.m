%Daniel Alejandro Claustro León 217535102
clear all
close all
clc

% T = readtable('df_agrupacion_1.csv');
T = readtable('df_agrupacion_3.csv');
% T = readtable('df_agrupacion_4.csv');
% T = readtable('df_agrupacion_6.csv');

x1 = T.x1;
x2 = T.x2;
X = [x1 x2];

n = size(X,1);

k = 3;
I = randperm(n);

M = X(I(1:k),:);

G = zeros(1,n);

for j=1:50
    cla
    hold on
    grid on 
    plot(x1,x2,'bo','LineWidth',2)

    for i=1:k
    plot(x1(G==i), x2(G==i), 'o', 'LineWidth', 2)
    plot(M(i,1), M(i,2), 'sk', 'LineWidth', 2)
    end
    
    pause(0.5)
    
    for i=1:n
        D = sqrt((X(i,1)-M(:,1)).^2+(X(i,2)-M(:,2)).^2);
        [~,b] = min(D);

        G(i) = b;
    end

    for i=1:k
        M(i,:) = mean(X(G==i,:));
    end
end 

figure 
hold on 
grid on 
plot(x1,x2,'bo','LineWidth',2)

for i=1:k
    plot(x1(G==i), x2(G==i), 'o', 'LineWidth', 2)
end