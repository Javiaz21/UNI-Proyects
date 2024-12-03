#Javier Ignacio Díaz López      220839937
#Saul Alejandro Ayala Alanis    220976969

import serial
import numpy as np
import pickle 
import cv2

serialPort = serial.Serial(port = "COM3", baudrate=9600)

model = pickle.load(open('Trained_Model.sav','rb'))

N = 1000
i = 0

while(True):
    if(serialPort.in_waiting > 0):
        serial_input = serialPort.readline()
        serial_decode = serial_input.decode('Ascii')
        serial_decode = serial_decode.split(sep=',')
        serial_decode.pop()
        
        if(len(serial_decode)==5):
            data = [float(j) for j in serial_decode]
            data_array = np.asanyarray(data)
            y = model.predict(data_array.reshape(-1,1))
            print('homs: ',int(y[1]))

            
            i = i + 1

            if cv2.waitKey(1) == 27:
                break
            

serialPort.close()



