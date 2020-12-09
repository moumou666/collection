# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 05:14:14 2020

@author: 戴可昕
"""
import var as v
import pygame
import font 
import tool
import os

class Mainmenu:
    def __init__(self):
        information={"score":0,
                     "lives":3,
                     "role_state":'basic'
                     }
        self.gameInfo(information)
    def gameInfo(self,information):
        self.gameinfo=information
        self.background=pygame.image.load('startinterface.png')
        self.rect=v.screen.get_rect()
        self.font=font.Font("mainmenu",self.gameinfo)
        self.Status=False
        self.nextStage='story'
        #choose cursor
        self.cursor=pygame.sprite.Sprite()
        self.cursor.image=tool.getImage("role.png",0,0,48,48,1)
        self.cursor.rect=self.cursor.image.get_rect()
        self.cursor.rect.x=400
        self.cursor.rect.y=340
        self.cursor.state="start"

    def update_cursor(self,keys):
        if keys[pygame.K_w]:
            self.cursor.state='start'
            self.cursor.rect.y=340
        elif keys[pygame.K_s]:
            self.cursor.state='exit'
            self.cursor.rect.y=390
        elif keys[pygame.K_RETURN]:
            self.reset_gameInfo()
            if self.cursor.state=='start':
                self.Status=True
            elif self.cursor.state=='exit':
                self.Status=True
                pygame.quit()
                os._exit(0)    
    def update(self,surface,keys):
        self.update_cursor(keys)
        surface.blit(self.background,self.rect)
        surface.blit(self.cursor.image,self.cursor.rect)
        self.font.update()
        self.font.draw(surface)
    def reset_gameInfo(self):
        self.gameinfo.update({"score":0,
                     "lives":3,
                     "role_state":'basic'
                     })
