import pygame
import random
import math

class Zumbi (pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/frame-2.png")

        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(900, 50, 100, 100)

        self.rect.x = 840+ random.randint(1, 400)
        self.rect.y = 1 + random.randint(1, 400)

        self.speed = 1 + random.random()* 2

        self.timer = 0


    def update(self, *args):

        self.timer += 0.001

        self.rect.x -= self.speed
        self.rect.y = self.rect.y + (math.sin(self.timer) * 2)

        if self.rect.right < 0 or self.rect.top > 500:
            self.kill()