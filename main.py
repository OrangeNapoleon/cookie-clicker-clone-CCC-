#!/usr/bin/env python3

import pygame
from pygame.locals import *
import pytomlpp

pygame.init()

clock = pygame.time.Clock()

config_data = pytomlpp.load('config.toml')

swidth = config_data['screen']['width']
sheight = config_data['screen']['height']

white = (255, 255, 255)

screen = pygame.display.set_mode((swidth, sheight))

pygame.display.set_caption("cockie clicker")

cookieimg = pygame.image.load('cookie.png')

cookie = cookieimg.get_rect()

cookie.x = (swidth/2)-(cookie.width/2)
cookie.y = (sheight/2)-(cookie.height/2)

fps = 60

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill(white)

    screen.blit(cookieimg, cookie)

    pygame.display.update()
    clock.tick(fps)
