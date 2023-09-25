import pygame


class Label:
    def __init__(self, x, y, image, font, screen, text):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = font
        self.text = text
        self.font_color = (0, 0, 0)  # Color del texto (negro por defecto)

    def draw(self):
        # Dibujar la imagen
        self.screen.blit(self.image, self.rect)

        # Crear un objeto de texto renderizado
        text_surface = self.font.render(self.text, True, self.font_color)

        # Obtener el rectángulo del texto y centrarlo en el rectángulo de la imagen
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center

        # Dibujar el texto en la misma superficie que la imagen
        self.screen.blit(text_surface, text_rect)
