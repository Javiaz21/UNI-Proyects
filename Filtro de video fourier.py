#Javier Ignacio Díaz López - Proyecto MMIII - 2021B

import cv2
import scipy.fft
import numpy as np
import time
import serial

arduino= serial.Serial('COM5',9600,timeout=0.2)
cap=cv2.VideoCapture(1)                                             #>Recibe el video de una cámara
kernel = (1/49)*np.ones((7,7))                                      #>Matriz para filtrado por convolución
filtro_base=np.zeros((480,640,3))                                   #>Arreglo de zeros con las mismas dimensiones que la imágen para la báse del filtro pasa bajas
filtro_bajas=cv2.circle(filtro_base,(320,240),80,(1,1,1),-1)        #>Dibuja un círculo al centro de la imágen con valores 1 para pasar las frecuencias bajas
filtro_altas=1-filtro_bajas                                         #>Calcula la inversa del filtro pasa bajas para crear un filtro pasa altas
kernel=np.ones((3,3),np.uint8)
point_matrix = np.zeros((1,2),np.int32)
SS_flag_L = 0
SS_flag_R = 0
hsv_pixel = np.zeros((3),np.int32)
error_x=0
error_y=0
error_pos=0
datos_arduino=arduino.readline()
x = 0
y = 0
h = 0
w = 0

#cv2.imshow('Filtro', filtro_bajas)

for i in range(2100):
    fg, img= cap.read()
    filtro_normal=cv2.filter2D(img,-1,kernel)       #>Filtro por convolución
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     #>Conversión a escala de grises por si se quiere filtrar sin colores
    gray_64= np.float64(gray)                       
    img_64= np.float64(img)
    
    
    #>>Bloque de código de cálculos de fourier:
    
    fourier= scipy.fft.fftn(img_64)                 #>Transformada rápida de fourier
    fourier_s= scipy.fft.fftshift(fourier)          #>'shift' de la transformada: ordena las frecuencias bajas al centro
    fourier_filtro=fourier_s*filtro_bajas           #>Aplica el filtro deseado a la transformada multiplicándolos (para cambiar el tipo del filtro solo cambie la variable de filtrado utilizada)
    fourier_i= scipy.fft.ifftn(fourier_filtro)      #>Calcula la transformada inversa con el filtro ya aplicado
    fourier_i=np.uint8(np.abs(fourier_i))           #>Cambia el tipo de dato de la transformada inversa para mostrarla

    
    #>>Obtener valores de pixel con click para la máscara

    def mousePoints(event,x,y,flags,params):
        global SS_flag_R, SS_flag_L, captura, hsv_pixel, BGR_pixel
        
        #>>Click derecho para tomar captura
        
        if event == cv2.EVENT_RBUTTONDOWN:
            captura = fourier_i
            cv2.imshow('Captura', captura)
            cv2.setMouseCallback('Captura', mousePoints)
            SS_flag_R = SS_flag_R + 1
            print(SS_flag_R)
        
        #>>Click izquierdo para tomar captura
        
        if event == cv2.EVENT_LBUTTONDOWN:
            point_matrix[0] = x,y
            SS_flag_L = SS_flag_L + 1
            print(point_matrix)
            hsv_cap= cv2.cvtColor(captura, cv2.COLOR_BGR2HSV)
            BGR_pixel=captura[point_matrix[0][1],point_matrix[0][0]]   
            hsv_pixel=hsv_cap[point_matrix[0][1],point_matrix[0][0]]
            print(hsv_pixel)
    
    
    #>>Bloque de detección de máscara.
    
    hsv= cv2.cvtColor(fourier_i, cv2.COLOR_BGR2HSV)
    print(hsv_pixel)   
    low=int(hsv_pixel[0])
    up=int(hsv_pixel[0])
    mask=cv2.inRange(hsv,(low-10,100,30),(up+10,255,255))
    blur=cv2.GaussianBlur(mask,(7,7),1)
    canny=cv2.Canny(blur,200,200)
    color=cv2.dilate(canny,kernel,iterations=7)
    cv2.imshow('Mascara', color)
    contornos,J=cv2.findContours(color,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    
    #Detección de existencia de una figura a rastrear

    for cnt in contornos:
        area=cv2.contourArea(cnt)
        if area>2100:
            perimetro=cv2.arcLength(cnt,True)
            aprox= cv2.approxPolyDP(cnt,0.02*perimetro,True)
            x,y,w,h=cv2.boundingRect(aprox) 
            cv2.drawContours(fourier_i,cnt,-1,(255,0,0),7)
            cv2.rectangle(fourier_i,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),3)
            cv2.line(fourier_i, (320,240), (x+np.int32(w/2),y+np.int32(h/2)), (0,0,255), 3)

            #>>Cálculos de error para control de servomotores con arduino

            error_x=320-(x+int(w/2))
            error_y=240-(y+int(h/2))
            error_x_str=str(error_x)
            error_y_str=str(error_y)
            error_pos=np.sqrt(error_x**2+error_y**2)
            if(error_x>32):    
                arduino.write(b"0")
                print('ERROR X++',error_x)
            elif(error_x<-32):
                arduino.write(b"1")
                print('ERROR X--',error_x)
            elif(error_y>24):    
                arduino.write(b"2")
                print('ERROR Y++',error_y)
            elif(error_y<-24):
                arduino.write(b"3")
                print('ERROR Y--',error_y)
            else:
                arduino.write(b"9")
    
    datos=arduino.readline()
    print('datos Arduino ==>>',datos)    
    
    
    #>>Bloque de código de separación de los canales de color
    """
    B= fourier_i.copy()         #>Canal Azul
    B[:,:,1]=0
    B[:,:,2]=0
    G = fourier_i.copy()        #>Canal Verde
    G[:,:,0]=0
    G[:,:,2]=0
    R = fourier_i.copy()        #>Canal Rojo
    R[:,:,0]=0
    R[:,:,1]=0
    """
    
    #>>Bloque de código para ordenar la escala logarítmica de las imágenes en dominio frecuencia
    
    log = np.log10(np.abs(fourier))
    logs = np.log10(np.abs(fourier_s))
    logf = np.log10(np.abs(fourier_filtro))
    
    cv2.imshow('Imagen Original', img)
    cv2.imshow('Imagen filtrada fourier', fourier_i)
    if SS_flag_R==1:
        cv2.imshow('Captura', captura)
        cv2.setMouseCallback('Captura', mousePoints)
    else:
        cv2.setMouseCallback('Imagen Original', mousePoints)
    
    
    #>>Bloque de código que muestra cada uno de los pasos del procesamiento de la imágen
    
    """
    cv2.imshow('Imagen filtrada normal', filtro_normal)
    cv2.imshow('Imagen sin escalar', np.uint8(fourier))
    cv2.imshow('Imagen Gris', gray)
    cv2.imshow('Transformada', np.uint8(255*log/np.max(log)))
    cv2.imshow('Transformada Ordenada', np.uint8(255*logs/np.max(logs)))
    cv2.imshow('Canal Rojo Transformado',R)
    cv2.imshow('Canal Verde Transformado',G)
    cv2.imshow('Canal Azul Transformado',B)
    """
    cv2.imshow('Transformada Filtrada', np.uint8(255*logf/np.max(logf)))


    if cv2.waitKey(1) == 27:
        break