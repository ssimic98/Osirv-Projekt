import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math
def imread_rgb(file):
  image = cv.imread(file)
  rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  return rgb

def imread_grayscale(file):
  image = cv.imread(file, cv.IMREAD_GRAYSCALE)
  return image
def drawCircles(slika, kruznica):
    if kruznica  is not None:
        kruznica = np.round(kruznica[0, :]).astype("int")
        for (x, y, r) in kruznica:
            cv.circle(detekcijaSlika, (x, y), r, (0,255,0), 5)
            cv.rectangle(detekcijaSlika, (x - 2, y - 2), (x + 2, y + 2), (0,255,0), -1)
    return detekcijaSlika

slika1=imread_rgb('kovanice.png')
slika=imread_grayscale('kovanice.png')
detekcijaSlika=imread_rgb('kovanice.png')
plt.title('Izvorna slika')
plt.imshow(slika1)

plt.figure()
slikaBlur = cv.GaussianBlur(slika,(13,13),0)
plt.title('Blurana slika')


plt.imshow(slikaBlur)
kruznica = cv.HoughCircles(slikaBlur, cv.HOUGH_GRADIENT,  1, 100,param1=100,param2=90,minRadius=0,maxRadius=100)

detekcijaSlika=drawCircles(slika,kruznica)
plt.figure()
plt.title('Detekcija slika')
plt.imshow(detekcijaSlika)



