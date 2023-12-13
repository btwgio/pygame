import pygame
import sys 

pygame.init()

#tamanho da tela
screen = pygame.display.set_mode((800, 800))
#nome do jogo
pygame.display.set_caption('Cobrinha')

cobra = [(pygame.image.load('C:\Users\giov_\Downloads\Programação\pygame\acobra.png'))]

#tela preta
ctela = r'C:\Users\giov_\Downloads\Programação\pygame\fundo.png'
tela = pygame.image.load(ctela)

while True:
    for evento in pygame.event.get():
        #fechar o jogo
        if evento.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()