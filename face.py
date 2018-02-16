#!/usr/bin/python

# referencia https://www.youtube.com/watch?v=h5z8jrW9CtY
# arquivo para estudo



import cv2

imagem = raw_input('Imagem: ')

clf = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #clasificador

img = cv2.imread(imagem) #le a imagem

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #imagem cinza

faces = clf.detectMultiScale(gray, 1.3, 5) #(imagem, quanto a imagem reduz, tamanho)

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 5)# desenha o retangulo


cv2.imshow('imagem', img)

cv2.waitKey(0)
cv2.destroyAllwindows()


