import pygame


class TextBox:
    def __init__(self, x, y, width, height, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.text = ""
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Realiza alguna acción con el texto ingresado
                print("Texto ingresado:", self.text)
                self.text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        color = pygame.Color(
            'lightskyblue3') if self.active else pygame.Color('gray')
        pygame.draw.rect(screen, color, self.rect, 2)
        text_surface = self.font.render(self.text, True, pygame.Color('black'))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        #incluir en el metodo update()
        #for event in pygame.event.get():
        #    self.text_box.handle_event(event)
         
