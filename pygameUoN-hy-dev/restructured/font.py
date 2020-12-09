# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 05:32:08 2020

@author: 戴可昕
"""

import  pygame
import var as v
import props

class Font:
    def __init__(self,state,gameinfo):
        self.state=state
        self.gameinfo=gameinfo
        self.create_icon()
        self.create_font()
    def create_icon(self):
        self.icon_image=[]
        if self.state=="mainmenu":
            self.icon_image.append((props.Props()))
    def create_font(self):
        self.font_images=[]
        self.font_special=[]
        if self.state=="mainmenu":
            #self.font_images.append((self.create("Damn it",40),(400,100)))
            self.font_images.append((self.create("start",50),(450,340)))
            self.font_images.append((self.create("exit",50),(450,390)))
        elif self.state=="startgame":
            self.font_images.append((self.create(f"{self.gameinfo['lives']}",24),(200,10)))
            self.font_images.append((self.create(f"{self.gameinfo['score']}",24),(340,10)))
            self.font_images.append((pygame.image.load("live.png"),(150,10)))
            self.font_images.append((pygame.image.load("score.png"),(270,15)))
        elif self.state=="gameover":
            self.font_images.append((pygame.image.load("fail.png"),(0,0)))
            self.font_images.append((self.createRed("Game Over",100),(300,100)))
            
        
    def create(self,text,size):
        font=pygame.font.SysFont("Arial", size)
        font_image=font.render(text,2,(255,255,255))
        return font_image
    def createRed(self,text,size):
        font=pygame.font.SysFont("Arial", size)
        font_image=font.render(text,2,(255,0,0))
        return font_image
    def createPur(self,text,size):
        font=pygame.font.SysFont("Arial", size)
        font_image=font.render(text,2,(255,100,255))
        return font_image
    def update(self):
        for icon in self.icon_image:
            icon.update()
        
    def draw(self,surface):
        
        if not self.state=='story'or'win':
            self.create_font()
            for image in self.font_images:
                surface.blit(image[0],image[1])
            for icon in self.icon_image:
                surface.blit(icon.image,icon.rect)

            