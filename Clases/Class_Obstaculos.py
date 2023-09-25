import pygame
from Clases.Class_Player import Player


class Lava (pygame.sprite.Sprite):
    def __init__(self, x, y, tamaño_cuadricula) -> None:
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("Recursos/Img/Maps/Trampas/lava.png")
        self.image = pygame.transform.scale(
            image, (tamaño_cuadricula, tamaño_cuadricula // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pinchos(Lava):
    def __init__(self, x, y, tamaño_cuadricula) -> None:
        super().__init__(x, y, tamaño_cuadricula)
        image = pygame.image.load("Recursos/Img/Maps/Trampas/pinchos .png")
        
        self.image = pygame.transform.scale(
            image, (tamaño_cuadricula, tamaño_cuadricula // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Puerta(pygame.sprite.Sprite):
    def __init__(self, x, y, tamaño_cuadricula, animacion) -> None:
        super().__init__()
        self.index = 0
        self.animacion = animacion
        self.image = self.animacion[self.index]
        self.image = pygame.transform.scale(
            self.image, (tamaño_cuadricula // 2, tamaño_cuadricula))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, personaje: Player):

        if personaje.rect.colliderect(self.rect):
            if personaje.llaves == 4:
                personaje.exit = True
            elif personaje.llaves < 4:
                personaje.rect.x = self.rect.x - personaje.width
        self.index = personaje.llaves
        self.image = self.animacion[self.index]
