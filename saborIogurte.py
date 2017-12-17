#viog=[2,4,3,5,4,2,3,4,3,5]
#num5=0
#for i in range (0,len(viog),1):
#    if(viog[i]==5):
#        num5=num5+1
#print("O número de testes = 5 é :", num5)



import numpy as np
from scipy.stats import mode
import cv2
import os
import csv
import time

path = '/Users/jailsoncavalcanti/Doc/imgTeste/faces'
os.chdir(path)

#Salva o arquivo com titulo atualizado por data e hora
titulo = time.strftime("%Y-%m-%d") + '_' + time.strftime("%H-%M-%S")
saida = open('face_recon_'+titulo+'.csv', 'w')
export = csv.writer(saida, quoting=csv.QUOTE_NONNUMERIC)

file_list = []

for file in os.listdir(path):
    if file.endswith(".jpg"):
        file_list.append(file)

for file in file_list:
    #Para cada arquivo na lista faça:
    #Estabelece os classificadores de face
    face_cascade = cv2.CascadeClassifier('C:/Users/Admin2/OpenCV3/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    face_alt_cascade = cv2.CascadeClassifier('C:/Users/Admin2/OpenCV3/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml')
    face_alt2_cascade = cv2.CascadeClassifier('C:/Users/Admin2/OpenCV3/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face_alt_tree_cascade = cv2.CascadeClassifier('C:/Users/Admin2/OpenCV3/opencv/sources/data/haarcascades/haarcascade_frontalface_alt_tree.xml')

    #Lê a imagem e converte para escala de cinza
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Faz as classificações
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    faces2 = face_alt_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    faces3 = face_alt2_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    faces4 = face_alt_tree_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))

    #Organiza numa as classificações numa lista para loop
    classifiers = [faces, faces2, faces3, faces4]

    # Coloca os quadrados nas faces
    for classifier in classifiers:
        for (x,y,w,h) in classifier:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        print("Para a imagem "+file+", foram encontradas {0} faces!".format(len(classifier)))

        #Exibe as imagens com retãngulos. Para exibir, descomente as três linhas abaixo
        #cv2.imshow('img',img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

    # Exibe a média, variância e moda de cada classificador
    encontrados = []

    for (classifier) in classifiers:
        x = format(len(classifier))
        encontrados.append(x)

    encontrados = np.asarray(encontrados, dtype = np.float16)
    media = np.mean(encontrados)
    variancia = np.var(encontrados)
    moda = float(mode(encontrados)[0])

    if file == file_list[0]:
        export.writerow(["imagem","media","variancia","moda"])
        export.writerow([file, media, variancia, moda])
    else:
        export.writerow([file, media, variancia, moda])

saida.close()

print('Cabô, manolo!')


imgsrc = r'/Users/jailsoncavalcanti/Doc/imgTeste/wonder_woman_b.jpg'

img = cv2.imread(imgsrc, cv2.IMREAD_GRAYSCALE)
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Texto Teste",(10,500), font, 10, (105,255,255),2, cv2.LINE_AA)

cv2.imshow("IMAGE", img)
cv2.imwrite(r'/Users/jailsoncavalcanti/Doc/imgTeste/wonder_woman_b.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

