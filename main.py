from typing import AbstractSet
import pygame
import time
import math
import os
from pygame import image
from pygame.constants import QUIT
from utils import scale_image, blit_rotate_center


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

GRASS = scale_image(pygame.image.load(os.path.join(__location__, 'imgs/grass.jpg')), 2.5)
TRACK = scale_image(pygame.image.load(os.path.join(__location__, 'imgs/track.png')), 0.9)

TRACK_BORDER = scale_image(pygame.image.load(os.path.join(__location__, 'imgs/track-border.png')), 0.9)
FINISH = pygame.image.load(os.path.join(__location__, 'imgs/finish.png'))

RED_CAR = scale_image(pygame.image.load(os.path.join(__location__, 'imgs/red-car.png')), 0.55)
GREEN_CAR = scale_image(pygame.image.load(os.path.join(__location__, 'imgs/green-car.png')),0.55)


WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racing Game!')

FPS = 60

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS

    def rotate(self, left = False, right = False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)



def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()

run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
player_car = PlayerCar(4, 4)


while run:
    clock.tick(FPS)

    draw(WIN, images, player_car)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)


pygame.quit()