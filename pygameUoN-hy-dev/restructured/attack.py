import pygame
import tool
import var as v


class Attack(pygame.sprite.Sprite):
    def __init__(self, method):
        pygame.sprite.Sprite.__init__(self)
        self.method = method
        self.index = 0
        self.Time = 0
        self.frameNumber = v.eData[self.method]['FrameNumber']
        self.fileName = v.eData[self.method]['FileName']
        self.getEffect()
        self.rect = self.image.get_rect()
        self.setPos()
    
    
    def setPos(self):
        self.rect.x = 0
        self.rect.y = 0

    def updatePos(self, xPos, yPos, directionRight):
        if directionRight:
            self.rect.x = xPos + 60 + 48
        else:
            self.rect.x = xPos - 60 - 48
        self.rect.y = yPos + 48

    def getEffect(self):
        self.effectFrame = []
        effect = v.eData[self.method]
        frameRect = effect['FrameRect']
        for frame in frameRect:
            image = tool.getImage(effect['FileName'], *frame, 1)
            image = pygame.transform.scale(image, (48, 48))
            self.effectFrame.append(image)
        self.image = self.effectFrame[self.index]

    def update(self, xPos, yPos, directionRight):
        self.updatePos(xPos, yPos, directionRight)
        self.image = self.effectFrame[self.index]
        if pygame.time.get_ticks() - self.Time > 100:
            self.index += 1
            self.index %= self.frameNumber
            self.Time = pygame.time.get_ticks()
