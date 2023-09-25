import pygame


class TextBox:
    def __init__(self, x, y, width, height, max_chars=10, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.text = ""
        self.active = False
        self.max_chars = max_chars  # Número máximo de caracteres permitidos

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Realiza alguna acción con el texto ingresado (en este caso, imprime en pantalla)
                print("Texto ingresado:", self.text)
                self.text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            # Verifica si no se excede del número máximo de caracteres
            elif len(self.text) < self.max_chars:
                self.text += event.unicode
        return self.text

    def draw(self, screen):
        color = pygame.Color(
            'lightskyblue3') if self.active else pygame.Color('gray')
        pygame.draw.rect(screen, color, self.rect, 2)
        text_surface = self.font.render(self.text, True, pygame.Color('black'))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
