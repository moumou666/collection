# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 01:09:06 2020

@author: dd394
"""
import pygame
pygame.init()
class BUTTON:
    def __init__(self,position,text):
        self.width = 310
        self.height = 65
        self.left, self.top = position
        self.text = text
    def draw(self,screen):
        pygame.draw.line(screen,(150, 150, 150), (self.left, self.top), (self.left+self.width, self.top), 5)
        pygame.draw.line(screen,(150, 150, 150), (self.left, self.top-2), (self.left, self.top+self.height), 5)
        pygame.draw.line(screen,(50, 50, 50), (self.left, self.top+self.height), (self.left+self.width, self.top+self.height), 5)
        pygame.draw.line(screen,(50, 50, 50), (self.left+self.width, self.top+self.height), [self.left+self.width, self.top], 5)
        self.rect = pygame.draw.rect(screen,(100, 100, 100),(self.left, self.top, self.width, self.height))
        font=pygame.font.SysFont("Arial",45) 
        cont=font.render(self.text,1,( 255, 0, 0))
        screen.blit(cont,(self.left+50,self.top+5))




"""
back = pygame.image.load(r'startinterface.png')
back_rect = back.get_rect()
screen= pygame.display.set_mode((1060,546))    
screen.blit(back,back_rect)
button1 = BUTTON(screen,(350,200),"       cool")
button2 = BUTTON(screen,(350,300),"mingrixiang")

while True:
    for event in pygame.event.get():          
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
"""