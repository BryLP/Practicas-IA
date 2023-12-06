#Reconocimiento con el modelo creado
import cv2
import os

pathSave = "C:/Users/bryan/Documents/IA practicas/Practicas/Data"
imagePaths = os.listdir(pathSave)
print('imagePaths= ', imagePaths)

#Volvemos a utilizar reconized
recognizer = cv2.face.EigenFaceRecognizer_create()

#Leemos el modelo que se creo 
recognizer.read("modelRecognized.xml")

#medio en el que reconoceremos
camera = cv2.VideoCapture(0)

classif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = camera.read()
    if ret == False:
        break
    fgray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameAuxiliar = fgray.copy()

    objects = classif.detectMultiScale(fgray, 1.3, 5)

    for (x,y,w,h) in objects:
        rostro = frameAuxiliar[y:y+h, x:x+w]
        rostro = cv2.resize(rostro,(300,300), interpolation=cv2.INTER_CUBIC)
        result = recognizer.predict(rostro)
        
        #Nombres
        if result[1] < 12000:
            cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x,y-25), 1, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Desconocido", (x,y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

        #cv2.putText(frame, '{}'.format(result), (x,y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
        #cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    #imprimimos
    cv2.imshow("Reconocimiento :D", frame)

    #Se cierra si se presiona la tecla ESC
    escape_Key = cv2.waitKey(1)
    if escape_Key == 27:
        break

camera.release()
cv2.destroyAllWindows()