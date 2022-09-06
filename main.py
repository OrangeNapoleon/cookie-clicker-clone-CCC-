#!/usr/bin/env python3

import pygame
from pygame.locals import *
import pytomlpp

pygame.init()

config_data = pytomlpp.load('config.toml')

swidth = config_data['screen']['width']
sheight = config_data['screen']['height']

white = (255, 255, 255)

screen = pygame.display.set_mode((swidth, sheight))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill(white)

    pygame.display.update()
