from typing import Any
import pygame


class Vida (pygame.sprite.Sprite):
    def __init__(self, x, y, tamaño_cuadricula, screen, animacion) -> None:
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