% Actividad 5 - Sistemas Inteligentes IV
% Javier Ignacio Díaz López
% 220839937
% 17/09/2023

clear all
close all 
clc

df = readtable('df_clasificacion_1.csv');
df = readtable('df_clasificacion_2.csv');
% df = readtable('df_clasificacion_3.csv');

x_1 = df.x1;
x_2= df.x2;
Y = df.y; 
dimension = 4;
X = Polynomial_Features(x_1,x_2,dimension);

[n,m] = size(X);
w = rand(m,1);
a = 1;
lambda = .001;

TPR_plot = [];
FPR_plot = [];

for i=1:n
    h = X*w;
    g = 1./(1+exp(-h));
    w = w*(1-a*lambda)+a*X'*(Y-g);
end 


h = X*w;
g = 1./(1+exp(-h));

Yp = (g>=0.5)*1.0;

TN = 0; FP = 0; FN = 0; TP = 0;

for i=1:n
    if Y(i)==0 && Yp(i)==0
        TN = TN +1;
    elseif Y(i)==0 && Yp(i)==1
        FP = FP+1;
    elseif Y(i)==1 && Yp(i)==0
        FN = FN+1;
    elseif Y(i)==1 && Yp(i)==1
        TP = TP+1;
    end 

end

for umbral=0:0.01:1
    Yp = (g>=umbral)*1.0;

    TN = 0; FP = 0; FN = 0; TP = 0; 

    for i=1:n
        if Y(i)==0 && Yp(i)==0
            TN = TN + 1;
        elseif Y(i)==0 && Yp(i)==1
            FP = FP + 1;
        elseif Y(i)==1 && Yp(i)==0
            FN = FN + 1;
        elseif Y(i)==1 && Yp(i)==1
            TP = TP + 1;
        end 
    end 

    TPR = TP/(TP+FN);
    FPR = FP/(FP+TN);

    TPR_plot = [TPR_plot TPR];
    FPR_plot = [FPR_plot FPR];
end

figure
hold on
grid on 
title('Separación lineal (Dimension = 1)')
plot(x_1(Y==0), x_2(Y==0), 'ro', LineWidth=2)
plot(x_1(Y==1), x_2(Y==1), 'bo', LineWidth=2)

Draw_Decision_Boundary (x_1,x_2,w,dimension)
drawnow

accuarcy = (TP+TN)/(TP+TN+FP+FN)

figure
confusionchart(Y,Yp)
title('Matriz de confusión')

figure 
hold on 
grid on 
plot(FPR_plot, TPR_plot,'LineWidth', 3)
title('Curva ROC')