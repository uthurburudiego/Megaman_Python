import pygame
from Clases.Class_Button import *
from Clases.Class_Label import *
from Clases.Class_Layer import *
from Clases.Class_TextBox import *
from Clases.utilidades import cargar_imagen, mostrar_mensaje


class Opciones():
    def __init__(self, screen) -> None:

        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.start_menu = False
        self.fuente = pygame.font.Font("Recursos\Fuentes\GAMERIA.ttf", 36)

        self.niveles_button = Button(self.width // 2 + 28, self.height // 2 - 140,
                                     cargar_imagen("Recursos/Img/Menu/btn_levels.png", 120, 80), self.screen)

        self.setings_button = Button(self.width // 2 + 46, self.height // 2 - 50,
                                     cargar_imagen("Recursos/Img/Menu/btn_config.png", 80, 80), self.screen)

        self.rating_button = Button(self.width // 2 + 50, self.height // 2 + 30,
                                    cargar_imagen("Recursos/Img/Menu/btn_ranking.png", 80, 80), self.screen)

        self.back_button = Button(self.width // 2 - 150, self.height // 2 + 80,
                                  cargar_imagen("Recursos/Img/Menu/btn_atras.png", 60, 60), self.screen)

        self.layer = Layer(self.width // 2 - 236, self.height // 2 - 175,
                           cargar_imagen("Recursos\Img\Menu\layer.png", 472, 350), self.screen)

        self.label = Label(self.width // 2 - 150, self.height // 2 - 300,
                           cargar_imagen("Recursos\Img\Menu\label.png", 288, 84), self.fuente, self.screen, "Options")

    def draw(self):
        if self.start_menu:
            self.layer.draw()
            mostrar_mensaje(self.screen, "Levels", (self.width //
                            2 - 150, self.height // 2 - 120), self.fuente)
            mostrar_mensaje(self.screen, "Setings", (self.width //
                            2 - 150, self.height // 2 - 30), self.fuente)
            mostrar_mensaje(self.screen, "Rating", (self.width //
                            2 - 150, self.height // 2 + 50), self.fuente)
            self.label.draw()
            self.setings_button.draw()
            self.rating_button.draw()
            self.niveles_button.draw()
            self.back_button.draw()

    def update(self):
        self.draw()
