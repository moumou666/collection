# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:29:43 2020

@author: 戴可昕
"""
import pygame
import tool
import font
import music
# import startinterface
class GameOver():
    def __init__(self):
        pass
    def gameInfo(self,information):
        self.gameinfo=information
        self.Status=False
        self.nextStage='mainmenu'
        music.s2.play()
        self.font=font.Font("gameover",self.gameinfo)
        self.time=0
        self.duration=4000
    def update(self,surface,keys):
        self.draw(surface)
        if self.time==0:
            self.time=pygame.time.get_ticks()
        elif pygame.time.get_ticks()-self.time>self.duration:
            self.Status=True
            self.time=pygame.time.get_ticks()

    def draw(self,surface):
        surface.fill((0,0,0))
        #self.font.update()
        self.font.draw(surface)