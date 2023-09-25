import pygame


class Button():
    def __init__(self, x, y, image, screen) -> None:
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        posicion_mouse = pygame.mouse.get_pos()

        # aca preguntamos por si el mouse se posiciono en el rectangulo
        if self.rect.collidepoint(posicion_mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.screen.blit(self.image, self.rect)

        return action
