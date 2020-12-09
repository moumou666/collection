# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 07:48:04 2020

@author: 戴可昕
"""
import pygame
import tool
import font
class Story:
    def __init__(self):
        pass
    def gameInfo(self,information):
        self.gameinfo=information
        self.Status=False
        self.nextStage='startgame'
        self.font=font.Font("story",self.gameinfo)
        self.time=pygame.time.get_ticks()

        self.duration=8000
    def update(self,surface,keys):
        self.draw(surface)
        if self.time==0:
            self.time=pygame.time.get_ticks()
        elif pygame.time.get_ticks()-self.time>self.duration:
            self.Status=True
            self.time=pygame.time.get_ticks()
            surface.fill((0,0,0))
    def draw(self,surface):
        surface.fill((0,0,0))
        #self.font.update()
        #self.font.draw(surface)
        
        if pygame.time.get_ticks()-self.time>1500: 
            self.font.font_images.append((self.font.create("The  great  magician  Morris  disappeared  in  the  battle  with  Darklord.",30),(100,100)))
        if pygame.time.get_ticks()-self.time>3000: 
            self.font.font_images.append((self.font.create("Her only disciple, Pikmin, who is also the last hope of the kingdom,",30),(100,150)))
        if pygame.time.get_ticks()-self.time>4500: 
            self.font.font_images.append((self.font.create("will embark on a journey to defeat Darklord and find her mother.",30),(100,200)))
        if pygame.time.get_ticks()-self.time>5000:
            self.font.font_images.append((self.font.createRed("Be careful! you just have three chances",50),(200,250)))
        for image in self.font.font_images:

            surface.blit(image[0],image[1])
        