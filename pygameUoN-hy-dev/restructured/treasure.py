import pygame
import tool
import var as v


class Treasure(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.data = v.tData
        self.getImage()
        self.rect = self.image.get_rect()
        self.setPos()

    def setPos(self):
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        self.rect.y+=2

    def getImage(self):
        own = self.data[self.name]
        img = tool.getImage(own['FileName'], *(0, 0, 34, 34), 1)
        self.image = pygame.transform.scale(img, (48, 48))