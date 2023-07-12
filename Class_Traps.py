import pygame


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