#!/usr/bin/env python3

import pygame
from pygame.locals import *
import pytomlpp
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

#TOML
config_data = pytomlpp.load('config.toml')

swidth = config_data['screen']['width']
sheight = config_data['screen']['height']

fullscreen = config_data['fullscreen']
#TOML

#COLOUR
white = (255, 255, 255)
black = (0,0,0)
#COLOUR

#SCREEN
if fullscreen:
    if os.name == 'posix':
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        info = pygame.display.Info()
        width, height = info.current_w, info.current_h
        screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    else:
        screen = pygame.display.set_mode((swidth, sheight), FULLSCREEN)
else:
    screen = pygame.display.set_mode((swidth, sheight))

pygame.display.set_caption("cockie clicker")
icon = pygame.image.load("cookie_icn.png")
pygame.display.set_icon(icon)
#SCREEN

#COOKIE
cookieimg = pygame.image.load('cookie.png')

cookie = cookieimg.get_rect()

cookie.x = (swidth/2)-(cookie.width/2)
cookie.y = (sheight/2)-(cookie.height/2)
#COOKE

#FONT
font = pygame.font.SysFont("MathJax_Typewriter", 50)
txt = font.render('no clicks lollllll', False, black)
#FONT

fart = pygame.mixer.Sound('fart.wav')

fps = 60

pressed = False

click = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN and fullscreen:
            if event.type == K_ESC:
                pygame.quit()
                exit()
        if event.type == MOUSEBUTTONDOWN and not pressed:
            pressed = True
            mouse_pos = pygame.mouse.get_pos()
            if cookie.collidepoint(mouse_pos):
                l,_,r = pygame.mouse.get_pressed()
                if l:
                    click += 1
                if r:
                    fart.play()
                txt = font.render('clicks: ' + str(click), False, black)
        if event.type == MOUSEBUTTONUP:
            pressed = False

    screen.fill(white)

    screen.blit(txt, (0,0))
    screen.blit(cookieimg, cookie)

    pygame.display.update()
    clock.tick(fps)
