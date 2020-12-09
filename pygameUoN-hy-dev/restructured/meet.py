# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 00:12:40 2020

@author: dd394
"""
import pygame
import font
"""
my_image1 = pygame.image.load(r'win.png')
my_image2 = pygame.image.load(r'magician.png') 
my_image3 = pygame.image.load(r'hero .png')
rect3 = my_image3.get_rect()
screen= pygame.display.set_mode((1060,546))
"""

def meet(gameinfo,surface,image1,ini1,image2,ini2,dest,height):
    fon = font.Font("win",gameinfo)
    surface.blit(image1,(ini1,height))
    surface.blit(image2,(ini2,height))
    while True: 
        if ini1 <= dest and ini2 >= dest:
            pygame.display.update()
            surface.blit(pygame.image.load("win.png"),(0,0))
            surface.blit(image1,(ini1,height))
            surface.blit(image2,(ini2,height))
            fon.draw(surface)
            ini1 += 25
            ini2 -= 25
            pygame.time.Clock().tick(5)
        else:
            break
    return

            
            
    