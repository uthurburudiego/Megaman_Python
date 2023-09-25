import pygame
from Clases.Class_Button import *
from Clases.Class_Label import *
from Clases.Class_Layer import *
from Clases.Class_TextBox import *
from Clases.utilidades import cargar_imagen, mostrar_mensaje


class Menu():
    def __init__(self, screen) -> None:

        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.start_menu = True
        self.fuente = pygame.font.Font("Recursos\Fuentes\GAMERIA.ttf", 36)

        self.inicio_button = Button(self.width // 2 + 48, self.height // 2 - 140,
                                    cargar_imagen("Recursos/Img/Menu/btn_inicio.png", 80, 80), self.screen)

        self.option_button = Button(self.width // 2 + 46, self.height // 2 - 50,
                                    cargar_imagen("Recursos/Img/Menu/btn_opciones.png", 80, 80), self.screen)

        self.exit_button = Button(self.width // 2 + 50, self.height // 2 + 30,
                                  cargar_imagen("Recursos/Img/Menu/btn_exit.png", 80, 80), self.screen)

        self.layer = Layer(self.width // 2 - 236, self.height // 2 - 175,
                           cargar_imagen("Recursos\Img\Menu\layer.png", 472, 350), self.screen)

        self.label = Label(self.width // 2 - 150, self.height // 2 - 300,
                           cargar_imagen("Recursos\Img\Menu\label.png", 288, 84), self.fuente, self.screen, "Menu")

    def draw(self):
        self.layer.draw()
        mostrar_mensaje(self.screen, "Start", (self.width //
                        2 - 150, self.height // 2 - 120), self.fuente)
        mostrar_mensaje(self.screen, "Option", (self.width //
                        2 - 150, self.height // 2 - 30), self.fuente)
        mostrar_mensaje(self.screen, "Exit", (self.width //
                        2 - 150, self.height // 2 + 50), self.fuente)
        self.label.draw()
        self.option_button.draw()
        self.exit_button.draw()
        self.inicio_button.draw()

    def update(self):
        self.draw()
