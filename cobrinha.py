import pygame
import sys
import random

pygame.init()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
#comandos <^>

#tamanho da tela
screen = pygame.display.set_mode((600, 600))
#nome do jogo
pygame.display.set_caption('Cobrinha')
relogio = pygame.time.Clock()

# desenhar a cobra
def desenha_cobra(imagem_cobra, posicao):
    screen.blit(imagem_cobra, posicao)

#como desenhar a maçã
def desenha_maca(imagem_maca, posicao):
    screen.blit(imagem_maca, posicao)

#tela preta
tela = pygame.image.load('fundo.png')

#carregar imagem e definir tamanho/escala
imagem_cobra = pygame.image.load('acobra.png')
imagem_cobra = pygame.transform.scale(imagem_cobra, (15, 15))

imagem_maca = pygame.image.load('maca.png')
imagem_maca = pygame.transform.scale(imagem_maca, (25, 25))

#posição da maçã e da cobra
posicao_maca = (random.randint(0, 590), random.randint(0, 590))
posicao_cobra = (random.randint(0, 590), random.randint(0, 590))

while True:
    for evento in pygame.event.get():
        #fechar o jogo
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed() #controles do jogo

    screen.fill((0, 0, 0))
    desenha_cobra(imagem_cobra, posicao_cobra)
    
    desenha_maca(imagem_maca, posicao_maca)

    pygame.display.update()