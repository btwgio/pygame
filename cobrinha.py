import pygame
import sys 
import random 

pygame.init()

#tamanho da tela
screen = pygame.display.set_mode((800, 800))
#nome do jogo
pygame.display.set_caption('Cobrinha')

#cobra e seu tamanho
def a_cobra(imagem_cobra, tamanho):
    imagem_cobra = pygame.image.load('acobra.png')
    tamanho = pygame.transform.scale(imagem_cobra, (20, 20))
    cobra_t = pygame.Surface((10,10))

def apple(maca, posicao):
    imagem_maca = pygame.image.load('maca.png')
    imagem_maca = pygame.transform.scale(imagem_maca, (10, 10))
    posicao = (random.randint(0,790), random.randint(0,790))

#tela preta
tela = pygame.image.load('fundo.png')

while True:
    for evento in pygame.event.get():
        #fechar o jogo
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    screen.blit(a_cobra, apple)
    pygame.display.update()