import pygame

class Shot (pygame.sprite.Sprite):

    numTiros = 0 

    @staticmethod
    def somarTiros():
        Shot.numTiros += 1

    @staticmethod
    def subtrairTiros():
        Shot.numTiros -= 1

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image =pygame.image.load("data/shot.png")
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()

        self.speed = 4

        Shot.somarTiros()


    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            Shot.subtrairTiros()
            self.kill()
