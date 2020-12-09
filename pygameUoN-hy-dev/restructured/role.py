# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 04:24:59 2020

@author: 戴可昕
"""

import pygame
import var as v
import tool
import music
import bullet
import random
import music
class Role(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.immortal = False # 快速跑图无敌状态
        self.index=0
        self.frames=[]
        self.getImage()
        #self.rect=self.image.get_rect()
        self.setStates()
        self.setSpeed()
        self.setTime()
        #self.bullet=attack.Attack('eEarth')
        self.image=self.frames[self.index]
        self.player_bullets_group = pygame.sprite.Group()

    def setStates(self):
        self.directionRight=True
        self.dead=False
        self.state='stand'
        self.jumpStatus=True
        self.xuetiao=None
        self.touxiang=None
        self.bulletCooltime=0
        self.CoolTime=20
        self.bulletStatus=True
        self.attackMode='eEarth'
        self.beingHurt=False
    def setSpeed(self):
        self.xSpeed=0
        self.ySpeed=0
        self.maxSpeedx=10
        self.maxSpeedy=5.5
        self.jumpSpeed=-20
        self.xAcc=1
        self.acc=1
        self.turnAcc=5
        self.Newton=1
    def setTime(self):
        self.walkingTime=0
        self.deathTime=0
    def getDie(self):
        self.dead=True
        self.ySpeed=self.jumpSpeed
        self.frame_index=1
        self.state='die'
        self.deathTime=self.Time
    def getImage(self):
        self.rightFrame=[]
        self.leftFrame=[]
        self.hurtFrame=[]
        self.convert_hurtFrame=[]
        self.dieFrame=[]
        self.convert_dieFrame=[]
        frameRects=[(0, 96, 48, 48),(48, 96, 48, 48),(96, 96, 48, 48)]
        frameRects1=[(384,192,64,64),(448,192,64,64),(512,192,64,64)]
        frameRects2=[(384,320,64,64),(448,320,64,64),(512,320,64,64)]
        for frame in frameRects:
            rightimage=tool.getImage('role.png', *frame,1)
            leftimage=pygame.transform.flip(rightimage, True, False)
            self.rightFrame.append(rightimage)
            self.leftFrame.append(leftimage)
        for frame1 in frameRects1:
            rightimage1=tool.getImage('role1.png', *frame1,2/3)
            leftimage1=pygame.transform.flip(rightimage1, True, False)
            self.hurtFrame.append(rightimage1)
            self.convert_hurtFrame.append(leftimage1)
        for frame2 in frameRects2:
            rightimage2=tool.getImage('role1.png', *frame2,2/3)
            leftimage2=pygame.transform.flip(rightimage2, True, False)
            self.dieFrame.append(rightimage2)
            self.convert_dieFrame.append(leftimage2)
        self.frames=self.rightFrame
        self.index=0
        self.image=self.frames[self.index]
        self.rect=self.image.get_rect()
    def updateBullet(self):
        for bulleT in self.player_bullets_group:
            if bulleT.move():
                self.player_bullets_group.remove(bulleT)
        if not self.bulletStatus:
            if self.bulletCooltime == 0:
                self.bulletStatus=True
            else:
                self.bulletCooltime-=1
        self.player_bullets_group.update()
    def update(self,keys):
        self.Time=pygame.time.get_ticks()
        #change states
        self.updateBullet()
        #self.changeJumpStatus(keys)
        #detect jump Status and change it
        if self.directionRight:
            self.image=self.rightFrame[self.index]
            if self.beingHurt:
                self.image=self.convert_hurtFrame[self.index]
            if self.dead:
                self.image=self.convert_dieFrame[self.index]
        else:
            self.image=self.leftFrame[self.index]
            if self.beingHurt:
                self.image=self.hurtFrame[self.index]
            if self.dead:
                self.image=self.dieFrame[self.index]
        if not keys[pygame.K_SPACE]:
            self.jumpStatus=True
        if self.state=='stand':
            self.stand(keys)
        elif self.state=="move":
            self.move(keys)
        elif self.state=='jump':
            self.jump(keys)
        elif self.state=="fall":
            self.fall(keys)
        elif self.state=="die":
            #print(self.rect.y)
            self.rect.y+=self.ySpeed
            self.ySpeed+=self.Newton

    def attack(self):
        if self.attackMode=='eMoon':
            music.s3.play()
        else: music.s4.play()
        if self.attackMode=='eMoon':
            self.CoolTime=5
            return bullet.playerAttack(self.attackMode,self.rect.x,self.rect.y,self.directionRight,5,random.randint(-2,2))
        return bullet.playerAttack(self.attackMode,self.rect.x,self.rect.y,self.directionRight,5,0)
    def setAttack(self):
        self.bulletCooltime=self.CoolTime
        self.bulletStatus=False
        self.player_bullets_group.add(self.attack())
    def stand(self,keys):
        self.index=0
        self.xSpeed=0
        self.ySpeed=0
        if keys[pygame.K_d]:
            self.directionRight=True
            self.state="move"
        elif keys[pygame.K_a]:
            self.directionRight=False
            self.state="move"
        elif keys[pygame.K_SPACE] and self.jumpStatus:
            music.s1.play()
            self.state="jump"
            self.ySpeed=self.jumpSpeed
        if keys[pygame.K_l] and self.bulletCooltime==0:
            self.setAttack()
        if keys[pygame.K_F1]:
            self.immortal = not self.immortal
            print('Role immortal:', self.immortal)

    def move(self,keys):
        self.xAcc=self.acc
        if keys[pygame.K_SPACE]and self.jumpStatus:
            music.s1.play()
            self.state="jump"
            self.ySpeed=self.jumpSpeed
        if keys[pygame.K_l] and self.bulletCooltime==0:
            self.setAttack()
        if self.Time-self.walkingTime>100:
            
            self.index +=1
            self.index %=3
            
            self.walkingTime=self.Time
        if keys[pygame.K_d]:
            self.directionRight=True
            if self.xSpeed<0:
                #self.index=1
                self.xAcc=self.turnAcc
            self.xSpeed=tool.calSpeed(self.xSpeed,self.xAcc,self.maxSpeedx,self.directionRight)
        elif keys[pygame.K_a]:
            self.directionRight=False
            if self.xSpeed>0:
                #self.index=1
                self.xAcc=self.turnAcc
            self.xSpeed=tool.calSpeed(self.xSpeed,self.xAcc,self.maxSpeedx,self.directionRight)
        else:
            if self.directionRight:
                self.xSpeed-=self.xAcc
                if self.xSpeed<=0:
                    self.xSpeed=0
                    self.state='stand'
            else:
                self.xSpeed+=self.xAcc
                if self.xSpeed>=0:
                    self.xSpeed=0
                    self.state='stand'
    def jump(self,keys):
        if not self.beingHurt:
            self.index=1
        else:
            if self.Time-self.walkingTime>100:
            
                self.index +=1
                self.index %=3
            
                self.walkingTime=self.Time
        self.ySpeed+=self.Newton
        self.jumpStatus=False
        if keys[pygame.K_l] and self.bulletCooltime==0:
            self.setAttack()
        if self.ySpeed>=0:
            self.state='fall'
        if keys[pygame.K_d]:
            self.xSpeed=tool.calSpeed(self.xSpeed,self.xAcc,self.maxSpeedx,True)
        elif keys[pygame.K_a]:
            self.xSpeed=tool.calSpeed(self.xSpeed,self.xAcc,self.maxSpeedx,False)
        if not keys[pygame.K_SPACE]:
            
            self.state='fall'

    def fall(self,keys):
        if keys[pygame.K_l] and self.bulletCooltime==0:
            self.setAttack()

        self.ySpeed=tool.calSpeed(self.ySpeed,self.Newton+1,self.maxSpeedy,True)
        '''if self.rect.bottom>430:
            self.rect.bottom=430
            self.ySpeed=0
            self.state="move"'''
    '''def die(self,keys):
        self.rect.y+=self.ySpeed
        self.ySpeed+=self.Newton
        
    def calSpeed(self,speed,acc,maxSpeed,positive):
        if positive:
            return min(speed+acc,maxSpeed)
        else:
            return max(speed-acc,-maxSpeed)'''