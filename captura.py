# Reconocimiento facial - Captura de imagenes

import cv2
import os
import imutils

objectName = "Bryan"
pathSave = "C:/Users/bryan/Documents/IA practicas/Practicas/Data"
pathObject = pathSave + "/" + objectName

#Si no existe la carpeta con el nombre del objeto, se crea
if not os.path.exists(pathObject):
    print("Se creo la carpeta -> " + objectName + " dentro de la carpeta Data")
    os.makedirs(pathObject)

#Se usa la camara como captura
camera = cv2.VideoCapture(0)

c = 0
classif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while True:
    #Se redimensiona la imagen y se hace de color gris
    ret, frame = camera.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=640)
    fgray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameAuxiliar = frame.copy()

    objects = classif.detectMultiScale(fgray, 1.3, 5)

    #Dibuja rectangulo y se guarda la imagen
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        rostro = frameAuxiliar[y:y+h, x:x+w]
        rostro = cv2.resize(rostro,(300,300), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(pathObject + "/object_{}.jpg".format(c), rostro)
        c = c + 1
    cv2.imshow("fotograma", frame)

    #Se detiene la captura cuando se toma 300 fotos o si se presiona la tecla ESC
    escape_Key = cv2.waitKey(1)
    if escape_Key == 27 or c >= 300:
        break

camera.release()
cv2.destroyAllWindows()
