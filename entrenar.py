#Archivo para entrenar con las fotos obtenidas

import cv2
import os
import numpy as np 

pathSave = "C:/Users/bryan/Documents/IA practicas/Practicas/Data"
carpetsList = os.listdir(pathSave)
print(" detectados: ", carpetsList)

#Arreglos para entrenamiento
labels = []
pictureData = []
label = 0

for nameDir in carpetsList:
    pathObject = pathSave + "/" + nameDir
    
    for pictureName in os.listdir(pathObject):
        print("Leyendo: " + nameDir + "/" + pictureName)
        #Agregamos las etiquetas para diferenciar los datos (fotos) al arreglo  
        labels.append(label)
        pictureData.append(cv2.imread(pathObject + "/" + pictureName, 0)) #con el 0 convertimos las imagenes en blanco y negro
        image = cv2.imread(pathObject + "/" + pictureName, 0)
        cv2.imshow("foto", image)
        cv2.waitKey(10)
    label = label + 1

#Entrenamiento
recognizer = cv2.face.EigenFaceRecognizer_create()

recognizer.train(pictureData, np.array(labels))

#Guardamos el entrenamiento en un modelo

recognizer.write("modelRecognized.xml")
