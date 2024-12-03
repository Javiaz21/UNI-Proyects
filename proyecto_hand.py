import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils
hands= mphands.Hands()
import csv
import math

positions= ['Open','Closed','Thumbs_up','Thumbs_down']


with open('df - Copy.csv', 'w', encoding='UTF8', newline='') as f:

    writer = csv.writer(f)
    header = ['gesture','tip1','tip2','tip3','tip4','tip5','ver']
    writer.writerow(header)
    
    for i in range(4):
    #while True:
        cv2.text
        for j in range(50):
            available, cam = cap.read()
            print(positions[i])
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
                    data = [positions[i],dt,di,dm,dr,dp,uod]
                    writer.writerow(data)
                    writer.writerow(data)
                    mpdraw.draw_landmarks(cam, handLms,)
            cam = cv2.putText(cam, positions[i], (10,10), cv2.FONT_HERSHEY_SIMPLEX,  1, (255,255,0), 2, cv2.LINE_AA) 
            cv2.imshow("Camara",cam)
            cv2.waitKey(1)
        cam = cv2.putText(cam, 'CHANGE', (100,100), cv2.FONT_HERSHEY_SIMPLEX,  1, (255,255,0), 2, cv2.LINE_AA) 
        cv2.imshow("Camara",cam)
        cv2.waitKey(1000)