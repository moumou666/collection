import pygame
import tool
import var as v
import attack
import random


class Boss(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.index = 0
        self.bossTime = 0
        self.atk_mode = 1
        self.dead = False
        self.atk_ready = False
        self.frames = []
        self.setStates()
        self.getImage()
        # self.rect = self.image.get_rect()
        self.setPos()
        self.setSpeed()
        self.fall()
        # self.image = self.frames[self.index]
        self.walkingTime = 0


    def setStates(self):
        self.data = v.bBoss
        self.maxHP = self.data['maxHP']
        self.HP = self.maxHP
        self.score = self.data['score']
        self.directionRight = False
        self.state = 'move'
        self.jumpStatus = True

    def setPos(self):
        self.rect.x = self.data['xPos']
        self.rect.y = self.data['yPos']

    def setSpeed(self):
        self.xSpeed = 0
        self.ySpeed = 0
        self.maxSpeedx = 5
        self.maxSpeedy = 5
        self.xAcc = 0.5
        self.yAcc = 0.5
        self.turnAcc = 1

    def getDie(self):
        pass

    def getImage(self):
        self.rightFrame = []
        self.leftFrame = []
        self.rightFrameRect = self.data['rightFrameRect']
        self.leftFrameRect = self.data['leftFrameRect']
        for frame in self.rightFrameRect:
            rightimage = tool.getImage('monster.PNG', *frame, self.data['scale'])
            self.rightFrame.append(rightimage)
        for frame in self.leftFrameRect:
            leftimage = tool.getImage('monster.PNG', *frame, self.data['scale'])
            self.leftFrame.append(leftimage)

        self.frames = self.leftFrame
        self.index = 0
        self.frontImage = tool.getImage('monster.PNG', *self.data['frontImage'], self.data['scale'])
        self.leftImage = tool.getImage('monster.PNG', *self.data['leftImage'], self.data['scale'])
        self.rightImage = tool.getImage('monster.PNG', *self.data['rightImage'], self.data['scale'])
        self.backImage = tool.getImage('monster.PNG', *self.data['backImage'], self.data['scale'])
        # self.image = self.frames[self.index]
        self.image = self.frontImage
        self.rect = self.image.get_rect()

    def changeState(self):
        # print(self.state)
        if self.state == 'fall':
            self.fall()
        if self.state == 'move':
            self.move()
        # if self.directionRight:
        #     self.image = self.rightFrame[self.index]
        # else:
        #     self.image = self.leftFrame[self.index]

    def move(self):
        # print(self.rect.x)
        # if self.xSpeed == 0:
        #     self.xSpeed = 1
        # if self.rect.x > self.data['xRightLimit']:
        #     self.xSpeed = -1
        #     self.directionRight = False
        #     self.image = self.frames[self.index]
        # if self.rect.x < self.data['xLeftLimit']:
        #     self.xSpeed = 1
        #     self.directionRight = True
        #     self.image = self.frames[self.index]
        """
        if ((pygame.time.get_ticks() // 1000) % 4) == 0:
            if self.Time - self.walkingTime > 3500:
                self.atk_mode = random.randint(1, 3)
                if self.atk_mode == 1:
                    self.image = self.leftImage
                if self.atk_mode == 2:
                    self.image = self.frontImage
                if self.atk_mode == 3:
                    self.image = self.backImage
                self.walkingTime = self.Time

        """
        if self.Time - self.walkingTime > 3500:
            self.atk_mode = random.randint(1, 3)
            if self.atk_mode == 1:
                self.image = self.leftImage
            if self.atk_mode == 2:
                self.image = self.frontImage
            if self.atk_mode == 3:
                self.image = self.backImage
            # self.image = self.frames[self.index]
            # self.index += 1
            # self.index %= 3
            self.walkingTime = self.Time
            # self.atk_ready = True


    def attack(self, method):
        pass
        """
        def getEffect(method):
            effectFrame = []
            effect = v.eData[method]
            frameRect = effect['FrameRect']
            for frame in frameRect:
                image = tool.getImage(effect['FileName'], *frame, 1)
                effectFrame.append(image)
            return effectFrame

        def earth_attack(effectFrame):
            pass

        if method == 'eEarth':
            earth_attack(getEffect(method))
        """

    def update(self):
        self.Time = pygame.time.get_ticks()
        self.changeState()

    def fall(self):
        self.ySpeed = self.calSpeed(self.ySpeed, v.Newton+1, self.maxSpeedy, True)

    def calSpeed(self,speed, acc, maxSpeed, positive):
        if positive:
            return min(speed+acc, maxSpeed)
        else:
            return max(speed-acc, -maxSpeed)