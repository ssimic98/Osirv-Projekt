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

def show_image(image):
  plt.imshow(image)
def draw_lines(img, lines):
  a,b,c = lines.shape
  for i in range(a):
      rho = lines[i][0][0]
      theta = lines[i][0][1]
      a = math.cos(theta)
      b = math.sin(theta)
      x0, y0 = a*rho, b*rho
      pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
      pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
      cv.line(img, pt1, pt2, (255, 0, 0), 3, cv.LINE_AA)
  return img
  

slika=imread_rgb('sudoku.png')
plt.title('Izvorna slika')
plt.imshow(slika)
plt.figure()
slikaBlur=cv.GaussianBlur(slika,(5,5),100)
slikaEdge=cv.Canny(slikaBlur,0,100)
plt.title('Blurana slika')
plt.imshow(slikaBlur)
plt.figure()
lines=cv.HoughLines(slikaEdge, 1, math.pi/180, 200, np.array([]), 0, 0)
slikaIzvorna=draw_lines(slika,lines)
plt.title('Slika  pravaca')
plt.imshow(slikaIzvorna)
plt.figure()
plt.imshow(slikaEdge)



