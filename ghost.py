import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        #Carregar uma imagem para uso
        self.image = pygame.image.load("data/ghost-x4.gif")
        #Redimencional a imagem para usar em 100% do retangulo
        self.image = pygame.transform.scale(self.image,[100, 100])
        #ajustando o retangulo (POSITION)
        self.rect = pygame.Rect(50, 50, 100, 100)   

    #aceleração do plyer
        self.speed = 0
        self.acceleration =0.1

    def update(self, *args):
        #MOVIMENTAÇÃO DO PLAYER
        keys = pygame.key.get_pressed()

    #Velocidade do player
        if keys[pygame.K_w]:
            self.speed -= self.acceleration
        elif keys[pygame.K_UP]:
            self.speed -= self.acceleration
        elif keys[pygame.K_s]:
            self.speed += self.acceleration
        elif keys[pygame.K_DOWN]:
            self.speed += self.acceleration
        else:
            self.speed *= 0.95

        self.rect.y += self.speed

    #DEFINIR LIMITES DE TELA
        if self.rect.top < 0:
            self.rect.top=0
            self.speed =0
        elif self.rect.bottom > 480:
            self.rect.bottom =480
            self.speed =0