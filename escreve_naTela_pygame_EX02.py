import pygame

pygame.init()

janela = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Escrevendo na tela do pygame")
Font = pygame.font.SysFont('timesnewroman', 20)

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 255)
orange = (255, 100, 0)

im1 = "Aprender uma linguagem de programação pode ser difícil."
im2 = "Aprender com materiais em uma linguagem humana diferente é ainda mais difícil."
im3 = "Muito Obrigado."

frase_01 = Font.render(im1, False, black)
frase_02 = Font.render(im2, False, black)
frase_03 = Font.render(im3, False, orange)

contador = 0
clock = pygame.time.Clock()
while True:
    janela.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    contador += 1
    if contador <= 5:
        janela.blit(frase_01, (30, 30))
    if 5 < contador <= 10:
        janela.blit(frase_01, (30, 30))
        janela.blit(frase_02, (30, 60))
        janela.blit(frase_03, (30, 120))
    if contador > 10:
        quit()

    clock.tick(1)
    pygame.display.update()
