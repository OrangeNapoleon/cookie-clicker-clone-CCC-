#!/usr/bin/env python3

import pygame
from pygame.locals import *
import pytomlpp

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

#TOML
config_data = pytomlpp.load('config.toml')

swidth = config_data['screen']['width']
sheight = config_data['screen']['height']
#TOML

white = (255, 255, 255)

#SCREEN
screen = pygame.display.set_mode((swidth, sheight))

pygame.display.set_caption("cockie clicker")
#SCREEN

#COOKIE
cookieimg = pygame.image.load('cookie.png')

cookie = cookieimg.get_rect()

cookie.x = (swidth/2)-(cookie.width/2)
cookie.y = (sheight/2)-(cookie.height/2)
#SCREEN

#FONT
font = 0                #finish
#FONT

fps = 60

pressed = False

click = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN and not pressed:
            pressed = True
            l, m, r = pygame.mouse.get_pressed()
            if l:
                click += 1
            print(click)
        if event.type == MOUSEBUTTONUP:
            pressed = False

    screen.fill(white)

    screen.blit(cookieimg, cookie)

    pygame.display.update()
    clock.tick(fps)
