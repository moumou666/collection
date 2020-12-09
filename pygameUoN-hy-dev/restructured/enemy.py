import pygame
import tool
import var as v
import attack


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.index = 0
        self.frames = []
        self.setStates()
        self.getImage()
        
        self.rect = self.image.get_rect()
        self.setPos()
        self.setSpeed()
        self.setTime()
        self.fall()
        self.image = self.frames[self.index]
        if name == 'mEndBoss':
            self.earth_attack = attack.Attack('eEarth')

    def setStates(self):
        self.data = v.mData[self.name]
        self.MAX_HP = 10
        self.HP = self.MAX_HP
        self.score = self.data['score']
        self.directionRight = True
        self.state = 'stand'
        self.jumpStatus = True

    def setPos(self):
        self.rect.x = self.data['xLeftLimit']
        self.rect.y = 20

    def setSpeed(self):
        self.xSpeed = 0
        self.ySpeed = 0
        self.maxSpeedx = 5
        self.maxSpeedy = 5
        self.xAcc = 0.5
        self.yAcc = 0.5
        self.turnAcc = 1

    def setTime(self):
        self.walkingTime = 0

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

        self.frames = self.rightFrame
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect()

    def changeState(self):
        # print(self.state)
        if self.state == 'fall':
            self.fall()
        if self.state == 'move':
            self.move()
        if self.directionRight:
            self.image = self.rightFrame[self.index]
        else:
            self.image = self.leftFrame[self.index]

    def move(self):
        # print(self.rect.x)
        if self.xSpeed == 0:
            self.xSpeed = 1
        if self.rect.x > self.data['xRightLimit']:
            self.xSpeed = -1
            self.directionRight = False
            self.image = self.frames[self.index]
        if self.rect.x < self.data['xLeftLimit']:
            self.xSpeed = 1
            self.directionRight = True
            self.image = self.frames[self.index]
        if self.Time - self.walkingTime > 100:
            self.index += 1
            self.index %= 3
            self.walkingTime = self.Time

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