# 0. Criar uma instalação Desktop --------------------------------

# PASSO 1: 

# Importar os módulos os (para interagir com o sistema operacional)
# sys (para acessar variáveis e funções do interpretador Python)
import os, sys

# Obtém o caminho completo do diretório onde o script está sendo 
# executado e armazena na variável dirpath
dirpath = os.getcwd()

# Adiciona o diretório atual ao caminho de busca do Python
# Isso permite que Python encontre módulos localizados no
# mesmo diretório que o script. No caso as subpastas de assets (data)
sys.path.append(dirpath)

# Verifica se o script está sendo executado com um executavel compilado
# ( por exemplo, usando o PyInstaller)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS) # Se estiver compilado, muda o diretorio
    # de trabalho atual para o diretorio onde os arquivos do aplicativo
    # forem extraidos

# Passo 2: Após a inserção do código acima, instalar o pyinstaller pelo
# terminal
# pip install pyinstaller

# Passo 3:  Executar o seguinte comando no terminal
# pyinstaller -F main.py

# Passo 4: Abrir o arquivo main.spec e alterar o item:
# datas = [("data", "data")],

# Passo 5:  Executar o seguinte comando no terminal
# pyinstaller main.spec



#1ª IMPORTSS ---------------------------------------------------------------------------------------

import pygame
import random

from ghost import Ghost
from bat import Bat
from shot import Shot
from zumbi import Zumbi


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

# 3.1.1 cenario - background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image, [LARGURA_TELA, ALTURA_TELA ])
bg.rect =bg .image.get_rect()

#Ghost- PLayer 
#Criando o objeto SPRITE para carregar a imagem
ghost = Ghost(objectGroup)

#3.2 Fontes
score_font = pygame.font.Font("data/Pixeltype.ttf", 50)
gameOver_font = pygame.font.Font("data/Pixeltype.ttf", 200)

#3.3 Musica de fundo
pygame.mixer.music.load("data/alienblues.wav")
pygame.mixer.music.play(-1) # -1 faz ficar a musica tocando em loop

#3.4 Efeitos sonoros
attack = pygame.mixer.Sound("data/magic1.wav")

gameOverSound = pygame.mixer.Sound("data/Production_Intro_Theme.wav")



#4ª VARIAVEIS GLOBAIS -------------------------------------------------------------------------------------
gameLoop = True
gameOver = False

timer = 20
tiros = 0
pontos = 0

numFase = 1


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

    global numFase

# GAME LOOP
    while gameLoop:

        #CLOCK para 60 fps
        clock.tick(60)

        #Event Loop - Loop eventos : verificação de todos os eventos possiveis
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            elif event.type == pygame.KEYDOWN and Shot.numTiros < 5 and not gameOver:
                if event.key == pygame.K_SPACE:
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = ghost.rect.center
                    attack.play()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and Shot.numTiros < 5 and not gameOver:
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = ghost.rect.center
                    attack.play()
        

        #CONDIÇÃOO DO JOGO RODANDO 
        if not gameOver:

            # display.fill("#272b4f")

            timer += 1

            #FASE 1 - CRIAÇÃO DO MORCEGO - BAT 
            if timer > 30 and numFase == 1:
                timer = 0
                if random.random() < 0.3:
                    newBat = Bat(objectGroup, batGroup)

            #FASE 2 - CRIAÇÃO DO ZUMBI
            if timer > 30 and numFase == 2:
                timer = 0
                if random.random() < 0.45:
                    newBat = Bat(objectGroup, batGroup)
                if random.random() < 0.25:
                    newZumbi = Zumbi(objectGroup, batGroup)

            #TROCA DE FASES
            if pontos >= 10:
                numFase = 2

            colisao = pygame.sprite.spritecollide(
                ghost,
                batGroup,
                False,
                pygame.sprite.collide_mask
            ) 

            if colisao:
                gameOver = True
                # print("GAME OVER")

            # if Bat.scapeBat:
            #     gameOver = True
            #     print("GAME OVER")

            tiro = pygame.sprite.groupcollide(
                shotGroup,
                batGroup,
                True,
                True,
                pygame.sprite.collide_mask
            )

            if tiro:
                pontos += 1
                Shot.subtrairTiros()
                print(f"Score: {pontos}")


        #ATUALIZAÇÃO DOS ELEMENTOS DA TELA
            objectGroup.update()

        #DESENHAR OS GRUPOS NA TELA
        objectGroup.draw(display)

        #INSERIR A PONTUAÇÃO NA TELA 
        score_mensagem = score_font.render(f"SCORE: {pontos}", False, "White")

        display.blit(score_mensagem, (650, 50))

        #INSERIR MENSAGEM DE GAME OVER
        if gameOver:
            gameOver_mensagem = gameOver_font.render("GAME OVER", False, "White")

            display.blit(gameOver_mensagem, (100, 150))

            pygame.mixer.music.stop()
            gameOverSound.play()


        pygame.display.update()



if __name__ == "__main__":
    main()


    #Adicionar animação
    #adicionar fase final com boss
    # adicionar vitoria