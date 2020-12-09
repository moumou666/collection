import pygame
import tool
import random
import var as v


class BossAttack(pygame.sprite.Sprite):
    def __init__(self, method):
        pygame.sprite.Sprite.__init__(self)
        self.method = method
        self.index = 0
        self.Time = 0
        self.data = v.beData[self.method]
        self.frameNumber = self.data['FrameNumber']
        self.fileName = self.data['FileName']
        self.scale = self.data['scale']
        self.getEffect()
        self.rect = self.image.get_rect()
        self.setPos()


    def setPos(self):
        if self.method == 'beThunder' or self.method == 'beClaw1' or self.method == 'beClaw2':
            self.rect.x = random.randint(self.data['RestrictZone'][0],
                                         self.data['RestrictZone'][1])
            self.rect.y = random.randint(self.data['RestrictZone'][2],
                                         self.data['RestrictZone'][3])
        if self.method == 'beEarth':
            self.rect.x = self.data['RestrictZone'][1]
            self.rect.y = self.data['RestrictZone'][2]

    def updatePos(self):
        if self.method == 'beEarth':
            self.rect.x -= 3
            if self.rect.x < self.data['RestrictZone'][0]:
                self.rect.x = self.data['RestrictZone'][1]
        if self.method == 'beClaw1':
            self.rect.x -= 2
            self.rect.y += 2
        if self.method == 'beThunder':
            self.rect.y += 2


    def getEffect(self):
        self.effectFrame = []
        effect = v.beData[self.method]
        frameRect = effect['FrameRect']
        for frame in frameRect:
            image = tool.getImage(effect['FileName'], *frame, 1)
            image = pygame.transform.scale(image, self.scale)
            self.effectFrame.append(image)
        self.image = self.effectFrame[self.index]

    def update(self):
        self.updatePos()
        self.image = self.effectFrame[self.index]
        if pygame.time.get_ticks() - self.Time > 100:
            self.index += 1
            self.index %= self.frameNumber
            self.Time = pygame.time.get_ticks()
