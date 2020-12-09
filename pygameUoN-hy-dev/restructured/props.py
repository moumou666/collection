# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 06:04:59 2020

@author: 戴可昕
"""

import pygame
import var as v
import tool
class Props(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames=[]
        self.index=0
        frameRects=[(9*48,48*4,48,48),(9*48,48*5,48,48),(9*48,48*6,48,48),(9*48,48*7,48,48)]
        self.loadImages(frameRects)
        self.image=self.frames[self.index]
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=350
        self.time=0
    def loadImages(self,frameRects):
        for frame in frameRects: 
            self.frames.append(tool.getImage("monster.png", *frame, 4))
    def update(self):
        self.current_time=pygame.time.get_ticks()
        frame_duration=[300,100,150]
        if self.time==0:
            self.time=self.current_time
        elif self.current_time-self.time>frame_duration[self.index]:
            self.index+=1
            self.index%=3
            self.time=self.current_time
        self.image=self.frames[self.index]