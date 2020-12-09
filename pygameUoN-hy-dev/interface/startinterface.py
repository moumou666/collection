# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 00:03:58 2020

@author: dd394
"""
import pygame
import os
import button

cover =pygame.image.load("startinterface.png")
cover_rect = cover.get_rect()
screen= pygame.display.set_mode((1060,546))  
def StartInterface(screen):
    screen.blit(cover,cover_rect)
    button1=button.BUTTON((350,200),"      Start")
    button2=button.BUTTON((350,300),"       Exit")
    button1.draw(screen)
    button2.draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if button1.rect.collidepoint(pygame.mouse.get_pos()):
                    return
                if button2.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    os._exit(0)    
            pygame.display.flip()
#StartInterface(screen)



"""       
back = pygame.image.load(r'startinterface.png')
back_rect = back.get_rect()
screen= pygame.display.set_mode((1060,546))    
screen.blit(back,back_rect)
button1 = button.BUTTON(screen,(350,200),"      Start")
button2 = button.BUTTON(screen,(350,300),"       Exit")

while True:
    for event in pygame.event.get():          
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
"""