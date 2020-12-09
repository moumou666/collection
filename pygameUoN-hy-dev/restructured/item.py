# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:42:15 2020

@author: 戴可昕
"""
import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((45,35)).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y