import pygame

pygame.init()

janela = pygame.display.set_mode([1000, 700])
pygame.display.set_caption('Respondendo a pergunta de Vidal')
font = pygame.font.SysFont('comicsans', 20)

fr1 = 'Lorem Ipsum é simplesmente um texto ficticio da industria tipografica e de impressão.'
fr2 = 'Lorem Ipsum tem sido o texto fictício padrão da indústria desde os anos 1500.'

frase_1 = font.render(fr1, False, (0, 0, 0))
frase_2 = font.render(fr2, False, (0, 0, 0))


def desenhar(cont):
    if cont > 8:
        janela.blit(frase_1, (30, 30))
    if cont > 16:
        janela.blit(frase_2, (30, 60))
    if cont > 24:
        quit()


contador = 0
clock = pygame.time.Clock()
while True:
    janela.fill((255, 255, 255))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            quit()
    contador += 1
    clock.tick(2)
    desenhar(contador)
    print(contador)
    pygame.display.update()
