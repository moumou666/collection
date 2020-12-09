# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 07:48:04 2020

@author: 戴可昕
"""
import pygame
import font
import var as v
import role
import item
import walldata
import enemy
import treasure
import random
import boss
import boss_attack

class Start:
    def __init__(self):
        pass

    def gameInfo(self,information):
        self.gameinfo=information
        self.Status=False
        self.rect=v.screen.get_rect()
        self.nextStage='win'
        self.font=font.Font("startgame",self.gameinfo)
        self.background=pygame.image.load('map1.png')
        self.backgroundRect=self.background.get_rect()
        self.gameGround=pygame.Surface((self.backgroundRect.width,self.backgroundRect.height))
        self.roleGroup = pygame.sprite.Group()
        self.setRole()
        self.setEnemy()
        self.bossGroup = pygame.sprite.Group()
        self.setBoss()
        self.bossAtkGroup = pygame.sprite.Group()
        self.bossAtkTime = 0
        self.gameWindow=v.screen.get_rect()
        self.setItem()
        self.treasureGroup1 = pygame.sprite.Group()
        self.treasureGroup2 = pygame.sprite.Group()
        self.treasureGroup3 = pygame.sprite.Group()
        #self.setTreasure()
        
    def setEnemy(self):
        self.enemyGroup = []
        #self.enemyGroupsprite = pygame.sprite.Group()
        for monster in v.mData.keys():
            self.enemyGroup.append(enemy.Enemy(monster))
            #monster.update()
            #self.enemyGroupsprite.add(enemy.Enemy(monster))


    # def setAttack(self):
    #     self.enemyAttack=pygame.sprite.Group
    #     self.enemyAttack.add()
    #     pass

    def setBoss(self):
        self.boss = boss.Boss('EndBoss')
        self.bossGroup.add(self.boss)

    def setBossAtk(self):
        # atk_mode = random.randint(1, 3)
        # if ((pygame.time.get_ticks() // 1000) % 5) == 0:
        if pygame.time.get_ticks() - self.bossAtkTime > 3500:
            self.bossAtkGroup.empty()
            self.bossAtkTime = pygame.time.get_ticks()
            if self.boss.atk_mode == 1:
                self.bossAtkGroup.add(boss_attack.BossAttack('beThunder'))
            if self.boss.atk_mode == 2:
                self.bossAtkGroup.add(boss_attack.BossAttack('beClaw1'))
            if self.boss.atk_mode == 3:
                self.bossAtkGroup.add(boss_attack.BossAttack('beEarth'))


    def setTreasure(self,x,y,m):
        
        
        if m==1:
            t=treasure.Treasure('tCheery')
            t.rect.x=x
            t.rect.y=y
            self.treasureGroup1.add(t)
        if m==2:
            t=treasure.Treasure('tAntidote')
            t.rect.x=x
            t.rect.y=y
            self.treasureGroup2.add(t)
        if m==3:
            t=treasure.Treasure('tMedicine')
            t.rect.x=x
            t.rect.y=y
            self.treasureGroup3.add(t)
            #self.treasureGroup.add(treasure.Treasure('tMedicine'))
        #for treasureName in v.tData.keys():
            #self.treasureGroup.add(treasure.Treasure(treasureName))


    def setRole(self):
        self.role=role.Role('1P')
        self.roleGroup.add(self.role)
        self.role.rect.x=74
        self.role.rect.y=382
        self.startX=0
    #ground initialize
    def setItem(self):
        self.itemGroup=pygame.sprite.Group()
        for i in walldata.walls:
            self.itemGroup.add(item.Item(i["x"],i["y"]))
    def updateRolePos(self):
        #x position
        self.role.rect.x+=self.role.xSpeed
        #if self.role.rect.x<self.startX:
            #self.role.rect.x=self.startX
        if self.role.rect.right>self.backgroundRect.width:
            self.role.rect.right=self.backgroundRect.width
        if self.role.rect.left<self.backgroundRect.left:
            self.role.rect.left=self.backgroundRect.left
        self.checkxPos()
        #y position
        
        self.role.rect.y+=self.role.ySpeed
        self.checkyPos()
        # print('X:', self.role.rect.x, '  Y:', self.role.rect.y) # 跑图测绘坐标用代码

    def updateEnemyPos(self):
        #self.enemyGroupsprite.empty()
        for monster in self.enemyGroup:
            # x position
            #self.enemyGroupsprite.empty()
            
                
            monster.rect.x += monster.xSpeed
            if monster.rect.right > self.backgroundRect.width:
                monster.rect.right = self.backgroundRect.width
            if monster.rect.left < self.backgroundRect.left:
                monster.rect.left = self.backgroundRect.left
            self.checkxPos()
            monster.rect.y += monster.ySpeed
            self.checkyPos()
                #self.enemyGroupsprite.add(monster)
    def checkxPos(self):
        role_hit=pygame.sprite.spritecollideany(self.role,self.itemGroup)
        for monster in self.enemyGroup:
            monster.enemy_hit = pygame.sprite.spritecollideany(monster, self.itemGroup)
        if role_hit:
            if self.role.rect.x<role_hit.rect.x:
                self.role.rect.right=role_hit.rect.left
            else:
                self.role.rect.left=role_hit.rect.right
            self.role.xSpeed=0
        for monster in self.enemyGroup:
            if monster.enemy_hit:
                if monster.rect.x < monster.enemy_hit.rect.x:
                    monster.rect.right = monster.enemy_hit.rect.left
                else:
                    monster.rect.left = monster.enemy_hit.rect.right
                monster.xSpeed=0
        
    def checkyPos(self):
        role_hit=pygame.sprite.spritecollideany(self.role,self.itemGroup)
        for monster in self.enemyGroup:
            monster.enemy_hit = pygame.sprite.spritecollideany(monster, self.itemGroup)
        # print(role_hit)
        if role_hit:
            if self.role.rect.bottom<role_hit.rect.bottom:
                self.role.ySpeed=0
                self.role.rect.bottom=role_hit.rect.top
                self.role.state='move'
                self.role.beingHurt=False
            else:
                self.role.ySpeed=6
                self.role.rect.top=role_hit.rect.bottom
                self.role.state='fall'
        self.checkif_Fall(self.role)
        for monster in self.enemyGroup:
            if monster.enemy_hit:
                if monster.rect.bottom < monster.enemy_hit.rect.bottom:
                    monster.ySpeed = 0
                    monster.rect.bottom = monster.enemy_hit.rect.top
                    monster.state = 'move'
                else:
                    monster.ySpeed = 6
                    monster.rect.top = monster.enemy_hit.rect.bottom
                    monster.state = 'fall'
        for monster in self.enemyGroup:
            self.checkif_Fall(monster)

    def checkif_Fall(self,sprite):
        sprite.rect.y+=1
        checkif_collide=pygame.sprite.spritecollideany(sprite,self.itemGroup)
        if not checkif_collide and sprite.state !='jump':
            sprite.state='fall'
        sprite.rect.y-=1
    def check_bullet_if_touch(self):
        for monster in self.enemyGroup:
            rolehit=pygame.sprite.collide_rect(self.role,monster)
            rush=pygame.sprite.spritecollideany(monster,self.role.player_bullets_group)
            role_hit_by_boss = pygame.sprite.spritecollideany(self.role, self.bossGroup)
            role_hit_by_boss_atk = pygame.sprite.spritecollideany(self.role, self.bossAtkGroup)
            pygame.sprite.spritecollide(monster,self.role.player_bullets_group,True)
            if rush:
                self.enemyGroup.remove(monster)
                # print(rush.rect.x,rush.rect.y)
                self.setTreasure(rush.rect.right,rush.rect.y,random.randint(1,3))
            if (rolehit or role_hit_by_boss) and not self.role.immortal:
                self.gameinfo['lives']-=1
                print('Role HP:', self.gameinfo['lives'])
                self.role.ySpeed=self.role.jumpSpeed
                self.role.beingHurt=True
                self.role.state="jump"
                if self.role.directionRight:
                    self.role.xSpeed=-5
                else:
                    self.role.xSpeed=5
            if role_hit_by_boss_atk and not self.role.immortal:
                self.gameinfo['lives']-=1
                print('Role HP:', self.gameinfo['lives'])
                self.role.ySpeed=self.role.jumpSpeed
                self.role.beingHurt=True
                self.role.state="jump"
                self.role.xSpeed=-5
                pygame.sprite.groupcollide(self.bossAtkGroup, self.roleGroup, True, False)
        boss_get_hurt = pygame.sprite.spritecollideany(self.boss, self.role.player_bullets_group)
        if boss_get_hurt:
            self.boss.HP -= 1
            print('Boss HP:', self.boss.HP)
            pygame.sprite.groupcollide(self.role.player_bullets_group, self.bossGroup, True, False)
            if self.boss.HP == 0:
                self.boss.dead = True
                self.boss.kill()
        pygame.sprite.groupcollide(self.bossAtkGroup, self.itemGroup, True, False)
        pygame.sprite.groupcollide(self.role.player_bullets_group,self.itemGroup,True,False)
        treasure1=pygame.sprite.spritecollideany(self.role,self.treasureGroup1)
        treasure2=pygame.sprite.spritecollideany(self.role,self.treasureGroup2)
        treasure3=pygame.sprite.spritecollideany(self.role,self.treasureGroup3)
        pygame.sprite.spritecollide(self.role,self.treasureGroup1,True)
        pygame.sprite.spritecollide(self.role,self.treasureGroup2,True)
        pygame.sprite.spritecollide(self.role,self.treasureGroup3,True)
        if treasure1:
            self.gameinfo['lives'] = 3
            print('Role HP:', self.gameinfo['lives'])
        if treasure2:
            if self.gameinfo['lives']<3:
                self.gameinfo['lives']+=1
                print('Role HP:', self.gameinfo['lives'])
        if treasure3:
            self.role.attackMode='eMoon'
    def update(self,surface,keys):
        self.Time=pygame.time.get_ticks()
         #           if pygame.sprite.groupcollide(self.treasureGroup1,self.itemGroup,False,False):
        for T in self.treasureGroup1:
            treasurehit1=pygame.sprite.spritecollideany(T,self.itemGroup)
            if treasurehit1:
                T.rect.bottom=treasurehit1.rect.top
            else:
                T.update()
        for T in self.treasureGroup2:
            treasurehit2=pygame.sprite.spritecollideany(T,self.itemGroup)
            if treasurehit2:
                T.rect.bottom=treasurehit2.rect.top
            else:
                T.update()
        for T in self.treasureGroup3:
            treasurehit3=pygame.sprite.spritecollideany(T,self.itemGroup)
            if treasurehit3:
                T.rect.bottom=treasurehit3.rect.top
            else:
                T.update()
        if not self.boss.dead:
            self.setBossAtk()
        else:
            self.bossAtkGroup.empty()
            self.Status = True
        self.bossAtkGroup.update()
        self.role.update(keys)
        for monster in self.enemyGroup:
            monster.update()
        self.updateEnemyPos()
        self.bossGroup.update()
        self.check_bullet_if_touch()
        self.gameinfo["score"]=41
        for monster in self.enemyGroup:
            self.gameinfo["score"]-=monster.score
        print(self.gameinfo["score"])
        if self.role.dead:
            self.updateRolePos()
            if self.Time-self.role.deathTime>2000:
                self.Status=True
                self.update_gameInfo()
        else:
            
            self.updateRolePos()
            self.updateGamewindow()
            if self.role.rect.y>v.HEIGHT or self.gameinfo['lives'] <= 0:
                self.role.getDie()
        self.draw(surface)
    def update_gameInfo(self):
        '''if self.role.dead:
            self.gameinfo['lives']-=1
        if self.gameinfo['lives']==0:
            self.nextStage="gameover"
        else:
            self.nextStage="mainmenu"'''
        if self.role.dead:
            self.nextStage="gameover"
    def updateGamewindow(self):
        x=self.gameWindow.x+v.WIDTH//3
        #print(self.role.xSpeed,self.role.rect.right,x,self.gameWindow.right)
        if self.role.xSpeed>0 and self.role.rect.right>x and self.gameWindow.right<self.backgroundRect.right - 5:
            self.gameWindow.x+=self.role.xSpeed
            self.startX=self.gameWindow.x
        elif self.role.xSpeed<0 and self.role.rect.x<self.gameWindow.x and self.role.rect.x>=0:
            self.gameWindow.x=self.role.rect.x
    def draw(self,surface):
        surface.fill((0,255,0))
        self.gameGround.blit(self.background,self.gameWindow,self.gameWindow)
        self.gameGround.blit(self.role.image,self.role.rect)
        # print('X:', self.role.rect.x, 'Y:', self.role.rect.y) # 测试用 输出主角坐标
        self.treasureGroup1.draw(self.gameGround)
        self.treasureGroup2.draw(self.gameGround)
        self.treasureGroup3.draw(self.gameGround)
        for monster in self.enemyGroup:
            self.gameGround.blit(monster.image, monster.rect)
        #self.enemyGroupsprite.draw(self.gameGround)
        self.role.player_bullets_group.draw(self.gameGround)
        # self.gameGround.blit(self.boss.image, self.boss.rect)
        self.bossGroup.draw(self.gameGround)
        # self.gameGround.blit(self.enemyGroup[7].earth_attack.image, self.enemyGroup[7].earth_attack.rect)
        self.bossAtkGroup.draw(self.gameGround)
        surface.blit(self.gameGround,(0,0),self.gameWindow)
        self.font.update()
        self.font.draw(surface)
    '''def checkif_dead(self):
        if self.role.rect.y>v.HEIGHT:
            self.role.getDie()'''