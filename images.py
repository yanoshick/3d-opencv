# opencv imagaes application for python3
import cv2
import numpy as np
import pygame
import os
import math
import time

os.environ["SDL_VIDEO_CENTERED"]='1'
black, white, blue  = (20, 20, 20), (230, 230, 230), (0, 154, 255)
green, red  = (20, 250, 20), (250, 20, 20)
cyan, magenta, yellow = (20, 230, 230), (230, 20, 230), (230, 230, 20)
width, height = 721, 721
fps = 60
clear = False
image = pygame.image.load(r'.//textue_rot-60.png')


#scan/drawing line ... with DDA (Digital Differential Analyzer
def scanline(x1,y1,x2,y2):
    pointslst = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx >= dy: d = dx
    else: d = dy
    if d == 0: 
        print("zero line!!!")
        pygame.quit()
        exit()
    #print(d)
    dx = float(x2 - x1) / d
    dy = float(y2 - y1) / d
    x = x1
    y = y1
    i = 1
    while i <= d:
        x = x + dx
        y = y + dy
        i = i + 1
        pointslst.append((int(x), int(y)))
    return(pointslst)
        
def drawline(scr,x1,y1,x2,y2,color):
    list=scanline(x1,y1,x2,y2)
    for i in range(len(list)):
        x = list[i][0]
        y = list[i][1]
        i = i + 1
        #scr.set_at((int(x), int(y)), img_texture[y][x])
        scr.set_at((int(x), int(y)), color)

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

pygame.init()
pygame.display.set_caption("Image Drawing Board")
screen = pygame.display.set_mode((width, height))
if clear==False: 
    screen.blit(image, (0, 0))
else:
    screen.fill(white)
print("======= Hello opencv images! ========")
clock = pygame.time.Clock()
clock.tick(fps)

# -----  drawing hexagon
# middle point
x0 = 360
y0 = 360
# radius
r = 12
for i in range(0,6):  
    angle = i * (3.14/3)  #180/3=60 degrees
    x1 = x0 
    y1 = y0 
    x2 = int(x0 + r*math.cos(angle) +0.5)
    y2 = int(y0 + r*math.sin(angle) +0.5) 
    print( str(int(0.5+angle*57.295779513)) + " deg." )
    drawline(screen,x1,y1,x2,y2,red)
# middle point
screen.set_at((int(x0), int(y0)), green)
# upper part (1/6) of hexagon 
angle4 = 4 * (3.14/3)  #180/3=60 degrees
x2 = int(x0 + r*math.cos(angle4) +0.5)
y2 = int(y0 + r*math.sin(angle4) +0.5) 
list1 = scanline(x0,y0,x2,y2)
angle5 =  5 * (3.14/3)  #180/3=60 degrees
x3 = int(x0 + r*math.cos(angle5) +0.5)
y3 = int(y0 + r*math.sin(angle5) +0.5) 
list2 = scanline(x0,y0,x3,y3)
print((list1,list2))
for i in range(len(list1)):
    drawline(screen,list1[i][0]-1,list1[i][1],list2[i][0],list2[i][1],black)
pygame.display.update()
time.sleep(5)
    

img = cv2.imread('lena.png')
cv2.imshow("Lena original", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
affine_warp = np.array([[2, 0, 0], [0, 1, 0]], dtype=np.float32)
dsize = (img.shape[1]*2, img.shape[0])
warped_img = cv2.warpAffine(img, affine_warp, dsize)
cv2.imshow("2x Horizontal Stretching", warped_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

img = cv2.imread('texture.png')
rot_img = rotate_image(img, -60)
cv2.imshow("Image Left Rotation", rot_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#image = pygame.image.load(r'.//lena.png')
#screen.blit(image, (0, 100))
clock.tick(fps)
pygame.display.update()
pygame.image.save(screen, "screen.png")
time.sleep(8)
pygame.quit()


