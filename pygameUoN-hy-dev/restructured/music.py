# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 15:22:16 2020

@author: dd394
"""

import pygame
import time
#pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r"stage.mp3")#加载背景音


def music():  #背景音乐，num=-1循环播放    
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

def stop(self):
    pygame.mixer.stop()
    
def vol(num):
    pygame.mixer.music.set_volume(vol)
    
class sound(): 
    def __init__(self,name,path):
        self.name = name
        self.path = pygame.mixer.Sound(path)
    def play(self):
        self.path.play()
        #time.sleep(0.1)
        #self.stop()
    def stop(self):
        self.path.stop()

s1=sound("jump",r"jump.wav")
s2=sound("gameover",r"gameover.wav")
s3=sound("attack1",r"attack1.wav")
s4=sound("attack2",r"attack2.wav") 
s5=sound("win",r"win.wav")      
"""
x=sound("po",r"test2.wav")
screen= pygame.display.set_mode((20,20))
music()

while True:
            for event in pygame.event.get():          
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    x.play()

"""              