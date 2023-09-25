import pygame


class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y, size, direccion, image) -> None:
        super().__init__()
        self.pantalla = size
        self.image = image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.velocidad = 10
        self.direccion = direccion

    def update(self) -> None:
        self.rect.x += self.velocidad * self.direccion
        if self.rect.left > self.pantalla.get_width():
            self.kill()
