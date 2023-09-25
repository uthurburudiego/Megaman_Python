import pygame


class Button():
    def __init__(self, x, y, image, screen) -> None:
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.prev_click = False  # Variable para almacenar el estado previo del clic

    def draw(self):
        action = False
        posicion_mouse = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        # Verificar si el mouse se posicionó en el rectángulo
        if self.rect.collidepoint(posicion_mouse):
            if mouse_click and not self.prev_click:
                action = True
                self.clicked = True
            else:
                self.clicked = False
        else:
            self.clicked = False

        self.prev_click = mouse_click  # Actualizar el estado previo del clic
        self.screen.blit(self.image, self.rect)

        return action
