#Saul Alejandro Ayala Alaniz 220976969
#Javier Ignacio Díaz López 220839937

import numpy as np
import pickle
import cv2
import mediapipe as mp
import math

cap = cv2.VideoCapture(1)
mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils
hands= mphands.Hands()

positions= ['Open','Closed','Thumbs_up','Thumbs_down']

model = pickle.load(open('proyecto-training.sav','rb'))

N = 200
i = 0

while(i<N):
        
    available, cam = cap.read()
    camRGB=cv2.cvtColor(cam,cv2.COLOR_BGR2RGB)
    results=hands.process(camRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                if id==0:
                    x0=lm.x
                    y0=lm.y

                if id==4:
                    xt=lm.x
                    yt=lm.y
                
                if id==8:
                    xi=lm.x
                    yi=lm.y

                if id==12:
                    xm=lm.x
                    ym=lm.y

                if id==16:
                    xr=lm.x
                    yr=lm.y

                if id==20:
                    xp=lm.x
                    yp=lm.y

            dt=math.sqrt(abs(x0-xt)**2+abs(y0-xt)**2)
            di=math.sqrt(abs(x0-xi)**2+abs(y0-xi)**2)
            dm=math.sqrt(abs(x0-xm)**2+abs(y0-xm)**2)
            dr=math.sqrt(abs(x0-xr)**2+abs(y0-xr)**2)
            dp=math.sqrt(abs(x0-xp)**2+abs(y0-xp)**2)
            uod=y0-yt
            data = [str(dt),str(di),str(dm),str(dr),str(dp),str(uod)]
            data = np.asanyarray(data)
            y = model.predict(data.reshape(-1,6))
            cv2.imshow("Camara",cam)
            cv2.waitKey(1)
            #i = i + 1
            d = y[0]
            print('iteration:',i,', data=',data, ', \nposition=', d)
            i = i + 1
            