import pygame
import sys 

pygame.init()

#tamanho da tela
screen = pygame.display.set_mode((800, 800))
#nome do jogo
pygame.display.set_caption('Cobrinha')

#cobra e seu tamanho
def a_cobra(imagem_cobra):
    cobra = [(pygame.image.load('acobra.png'))]
    imagem_cobra = pygame.transform.scale(cobra, (20, 20))
    return imagem_cobra

#tela preta
ctela = r'C:\Users\giov_\Downloads\Programação\pygame\fundo.png'
tela = pygame.image.load(ctela)

while True:
    for evento in pygame.event.get():
        #fechar o jogo
        if evento.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()