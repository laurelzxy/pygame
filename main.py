#1ª IMPORTSS ---------------------------------------------------------------------------------------

import pygame
import random

from ghost import Ghost
from bat import Bat
from shot import Shot


#pip install pygame

#2ª INICIALIZAÇÃO -----------------------------------------------------------------------------------
#2.1 INicialização do pygame
pygame.init()

#2.2 Inicar a janela do jogo com a configuração de resolução de 840x480

LARGURA_TELA = 840
ALTURA_TELA = 480

#2.3 Criar a janela (qadro/canva)
display = pygame.display.set_mode([LARGURA_TELA,ALTURA_TELA])

#2.4  Preencher o fundo da tela  (RGB)
display.fill("#272b4f")
#2.5 Mudar o titulo da janela
pygame.display.set_caption("GAME SENAI PYTHON 98")

#2.6 Mudar o icone da janela
icone = pygame.image.load("data/ghost.png")
pygame.display.set_icon(icone)

#3ª ELEMENTOS DE TELA ---------------------------------------------------------------------------------
#3.1 Personagens (criar um grupo para os personagens)

objectGroup = pygame.sprite.Group()

batGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

#Ghost- PLayer 
#Criando o objeto SPRITE para carregar a imagem
ghost = Ghost(objectGroup)

#3.2 Fontes



#4ª VARIAVEIS GLOBAIS -------------------------------------------------------------------------------------
gameLoop = True
gameOver = False

timer = 20
tiros = 0
pontos = 0


# 4.1 Criar um clock para ajustar os frames por seg(FPS)
clock = pygame.time.Clock()

#5ª FUNÇÃO PRINCIPAL ---------------------------------------------------------------------------------------
def main():
    global gameLoop
    global gameOver

    global timer

    global clock
    global tiros

    global pontos

# GAME LOOP
    while gameLoop:

        #CLOCK para 60 fps
        clock.tick(60)

        #Event Loop - Loop eventos : verificação de todos os eventos possiveis
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = ghost.rect.center
                    print("Apertou o W")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = ghost.rect.center
        

        #CONDIÇÃOO DO JOGO RODANDO 
        if not gameOver:

            display.fill("#272b4f")

            timer += 1

        #CRIAÇÃO DO MORCEGO - BAT
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newBat = Bat(objectGroup, batGroup)

            colisao = pygame.sprite.spritecollide(
                ghost,
                batGroup,
                False,
                pygame.sprite.collide_mask
            ) 

            if colisao:
                gameOver = True
                print("GAME OVER")

            tiro = pygame.sprite.groupcollide(
                shotGroup,
                batGroup,
                True,
                True,
                pygame.sprite.collide_mask
            )

            if tiro:
                tiros += 1
                print("Score: {pontos}")


        #ATUALIZAÇÃO DOS ELEMENTOS DA TELA
            objectGroup.update()

    #DESENHAR OS GRUPOS NA TELA
        objectGroup.draw(display)
        
        pygame.display.update()



if __name__ == "__main__":
    main()