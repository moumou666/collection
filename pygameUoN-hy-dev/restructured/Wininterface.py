# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:32:19 2020

@author: 戴可昕
"""

import pygame
import tool
import font
import music
#import meet
class Wininterface:
    def __init__(self):
        pass
    def gameInfo(self,information):
        self.gameinfo=information
        self.Status=False
        self.nextStage='startgame'
        self.font=font.Font("win",self.gameinfo)
        self.magician=pygame.image.load(r'magician.png') 
        self.hero=pygame.image.load(r'hero.png')
        self.time=pygame.time.get_ticks()
        self.duration=4000
        music.s5.play()
    def update(self,surface,keys):
        self.draw(surface)
        #self.font.draw(surface)
        #meet.meet(surface,self.gameinfo,pygame.image.load("magician.png"),0,pygame.image.load("hero.png"),1000,400,200)
        if self.time==0:
            self.time=pygame.time.get_ticks()
        elif pygame.time.get_ticks()-self.time>self.duration:
            self.Status=True
            self.time=pygame.time.get_ticks()
    def draw(self,surface):
        self.org1=0
        self.org2=1000
        self.org3=20
        surface.blit(self.magician,(self.org1,200))
        surface.blit(self.hero,(self.org2,200))
        while True: 
            if self.org1 <= 400 and self.org2 >= 400:
                surface.blit(pygame.image.load("win.png"),(0,0))
                surface.blit(self.magician,(self.org1,200))
                surface.blit(self.hero,(self.org2,200))
                #self.font.font_images.append((pygame.image.load("win.png"),(0,0)))
                self.font.font_special.append((self.font.createPur(f"YOU WIN!",self.org3),(60,40)))
                self.font.font_images.append((self.font.createPur(f"Your score is {self.gameinfo['score']}",60),(80,140)))
                self.font.font_images.append((self.font.createPur("You beat the darklord, and help your tutor",30),(200,370)))
                self.font.font_images.append((self.font.createPur("to get out of the dark magic trap",30),(200,400)))
                for image in self.font.font_images:
                    surface.blit(image[0],image[1])
                for image in self.font.font_special:
                    surface.blit(image[0],image[1])
                self.font.font_special.clear()
                #self.font.draw(surface)
                self.org1 += 25
                self.org2 -= 25
                self.org3 += 5
                pygame.display.update()
                pygame.time.Clock().tick(5)
            else:
                break
        return
        #surface.fill((0,0,0))
        #self.font.update()
        #self.font.draw(surface)