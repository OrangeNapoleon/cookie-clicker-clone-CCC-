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
msg_font = pygame.font.SysFont("MathJax_Typewriter", 300)
txt = font.render('no clicks lollllll', False, black)
sign_txt = msg_font.render('', False, black)
sign = False
miner_count = font.render('', False, black)
up1 = font.render('1-miner:100', False, black)
#FONT

#UPGRADES
miners = 0
#UPGRADES

fart = pygame.mixer.Sound('fart.wav')

fps = 60

pressed = False

clicks = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN and fullscreen:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_1:
                if clicks >= 100:
                    clicks -= 100
                    miners += 1
                    miner_count = font.render('minors: ' + str(miners), False, black)
                    txt = font.render('no clicks lollllll', False, black)
                else:
                    sign_txt = msg_font.render('UR BROKE LMFAOOOOOOO', False, black)
                    sign = True
        if event.type == MOUSEBUTTONDOWN and not pressed:
            pressed = True
            mouse_pos = pygame.mouse.get_pos()
            if cookie.collidepoint(mouse_pos):
                l,_,r = pygame.mouse.get_pressed()
                if l:
                    clicks += 1
                if r:
                    fart.play()
                txt = font.render('clicks: ' + str(clicks), False, black)
        if event.type == MOUSEBUTTONUP:
            pressed = False

    screen.fill(white)

    screen.blit(txt, (0,0))
    screen.blit(cookieimg, cookie)
    screen.blit(up1, (0, sheight-100))
    screen.blit(miner_count, (0, 60))
    if sign:
        sign = False
        screen.blit(sign_txt, (0,sheight/2))
        screen.blit(sign_txt, (0,sheight-300))
        screen.blit(sign_txt, (0,0))
        pygame.display.update()
        pygame.time.wait(500)

    pygame.display.update()
    clock.tick(fps)
