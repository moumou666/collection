# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:36:49 2020

@author: 戴可昕
"""

import pygame
import tool
import var as v


class playerAttack(pygame.sprite.Sprite):
    def __init__(self, method,x,y,directionRight,speedx,speedy):
        pygame.sprite.Sprite.__init__(self)
        self.method = method
        self.index = 0
        self.Time = 0
        self.frameNumber = v.eData[self.method]['FrameNumber']
        self.fileName = v.eData[self.method]['FileName']
        self.getEffect()
        self.rect = self.image.get_rect()
        self.directionRight=directionRight
        #self.setPos()
        self.startX=x
        self.rect.x = x
        self.rect.y = y
        self.speedx=speedx
        self.speedy=speedy

    def move(self):

        if self.directionRight:
            self.rect = self.rect.move(self.speedx, self.speedy)
        else:
            self.rect = self.rect.move(-self.speedx, self.speedy)
        
        if (self.rect.top < 0) or (self.rect.bottom > 546) or (self.rect.left < 0) or (self.rect.right > self.startX+1060):
            return True
        #print(self.rect.left,self.rect.right,self.rect.bottom,self.rect.top)
        return False

    def getEffect(self):
        self.effectFrame = []
        effect = v.eData[self.method]
        frameRect = effect['FrameRect']
        for frame in frameRect:
            image = tool.getImage(effect['FileName'], *frame, 1)
            image = pygame.transform.scale(image, (48, 48))
            self.effectFrame.append(image)
        self.image = self.effectFrame[self.index]

    def update(self):
        #self.updatePos(xPos, yPos, directionRight)
        self.image = self.effectFrame[self.index]
        if pygame.time.get_ticks() - self.Time > 100:
            self.index += 1
            self.index %= self.frameNumber
            self.Time = pygame.time.get_ticks()
