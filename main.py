import pygame
from pygame.locals import*
import json


from Class_Mundo import Mundo

pygame.init()

clock = pygame.time.Clock()
fps = 50
width = 1000
height = 1000


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Megaman")


# Carga de imagenes:
background_image = pygame.transform.scale(pygame.image.load(
    "Recursos/Img/Maps/Niveles/background.png"), (width, height))




mundo = Mundo(screen)


run = True
while run:
    clock.tick(fps)
    screen.blit(background_image, (0, 0))

    run = mundo.draw()
    #dibujar_cuadricula(screen, 50)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
