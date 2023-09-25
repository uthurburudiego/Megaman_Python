from typing import Any
import pygame
from Clases.Class_Player import*


class Vida (pygame.sprite.Sprite):
    def __init__(self, x, y, screen, animacion) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.animacion = animacion

        self.index = 0
        self.cooldown_frames = 0
        self.image = pygame.transform.scale(
            self.animacion[self.index], (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        self.animar()

    def animar(self):
        if self.index >= len(self.animacion):
            self.index = 0

        if self.cooldown_frames > 3:
            self.image = self.animacion[self.index]
            self.index += 1
            self.cooldown_frames = 0
        self.cooldown_frames += 1


class Lamps (pygame.sprite.Sprite):
    def __init__(self, x, y, screen, animacion) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.index = 0
        self.que_animacion = "salida"
        self.cooldown_frames = 0
        self.animacion = animacion
        self.image = self.animacion[self.que_animacion][self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.salida = False
        self.sonido_items = pygame.mixer.Sound("Recursos/Songs/tocarItem.mp3")
        self.sonido_items.set_volume(0.1)

    def update(self,  personaje: Player) -> None:

        if personaje.rect.colliderect(self.rect) and not self.salida:
            self.sonido_items.play()
            self.salida = True
            personaje.llaves += 1
        if self.salida:
            self.que_animacion = "saliendo"
        else:
            self.que_animacion = "salida"

        self.animar()

    def animar(self):
        if self.index >= len(self.animacion[self.que_animacion]):
            self.index = 0

        if self.cooldown_frames > 3:
            self.image = self.animacion[self.que_animacion][self.index]
            self.index += 1
            self.cooldown_frames = 0
        self.cooldown_frames += 1
