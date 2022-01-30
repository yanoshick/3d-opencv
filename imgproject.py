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
width, height = 820, 860
fps = 60
clear = False
image = pygame.image.load(r'.//imgproject//test.bmp')


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
pygame.display.update()


pygame.image.save(screen, "screen.bmp")
time.sleep(8)
pygame.quit()


