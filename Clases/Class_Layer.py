import pygame


class Layer():
    def __init__(self, x, y, image, screen) -> None:
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
       

    def draw(self):
        self.screen.blit(self.image, self.rect)
        
