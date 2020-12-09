# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 04:27:55 2020

@author: 戴可昕
"""
#import sys
import pygame
import var as v
import os
class Game:
    def __init__(self,stateDict,startState):
        self.stateDict=stateDict
        self.state=self.stateDict[startState]
        self.screen=pygame.display.get_surface()
        self.clock=pygame.time.Clock()
        self.keys=pygame.key.get_pressed()
    def update(self):
        if self.state.Status:
            gameinfo=self.state.gameinfo
            nextState=self.state.nextStage
            self.state=self.stateDict[nextState]
            self.state.Status=False
            self.state.gameInfo(gameinfo)
        #print(self.state)
        self.state.update(self.screen,self.keys)
    def run (self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.display.quit()
                    os._exit(0)
                elif event.type==pygame.KEYDOWN:
                    self.keys=pygame.key.get_pressed()
                elif event.type==pygame.KEYUP:
                    self.keys=pygame.key.get_pressed()
            #self.screen.fill(pygame.Color('black'))
            self.update()
            pygame.display.update()
            self.clock.tick(30)
def getImage(directory,x,y,width,height,scale):
    image=pygame.image.load(directory).subsurface(pygame.Rect(x,y,width,height))
    
    image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    return image
def calSpeed(speed,acc,maxSpeed,positive):
    if positive:
        return min(speed+acc,maxSpeed)
    else:
        return max(speed-acc,-maxSpeed)