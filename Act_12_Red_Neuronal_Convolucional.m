% Actividad 12 - Sistemas Inteligentes IV
% Javier Ignacio Díaz López
% 220839937
% 05/11/2023

clear all
close all
clc

load training

I = imread("maskoff.jpg");

I = imresize(I, [227 227]);

[YPred,probs] = classify(trainedNetwork_1,I);
imshow(I)
label = YPred;
title(string(label) + ", " + num2str(100*max(probs),3) + "%");
