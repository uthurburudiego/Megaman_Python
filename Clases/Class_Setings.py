import pygame
from Clases.Class_Button import *
from Clases.Class_Label import *
from Clases.Class_Layer import *
from Clases.Class_TextBox import *
from Clases.utilidades import cargar_imagen, mostrar_mensaje


class Setings():
    def __init__(self, screen) -> None:

        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.start_menu = False
        self.index = 0
        self.fuente = pygame.font.Font("Recursos\Fuentes\GAMERIA.ttf", 36)

        self.sonido_button = Button(self.width // 2 + 46, self.height // 2 - 140,
                                    cargar_imagen("Recursos/Img/Menu/btn_sonido.png", 80, 80), self.screen)

        self.stop_sonido_button = Button(self.width // 2 + 46, self.height // 2 - 50,
                                         cargar_imagen("Recursos/Img/Menu/btn_stop_sonido.png", 80, 80), self.screen)

        self.volumen_mas_button = Button(self.width // 2 - 80, self.height // 2 - 50,
                                         cargar_imagen("Recursos/Img/Menu/btn_adelante.png", 80, 80), self.screen)
        self.volumen_menos_button = Button(self.width // 2 - 150, self.height // 2 - 50,
                                           cargar_imagen("Recursos/Img/Menu/btn_atras.png", 80, 80), self.screen)

        self.inicio_button = Button(self.width // 2 - 150, self.height // 2 - 140,
                                    cargar_imagen("Recursos/Img/Menu/btn_inicio.png", 80, 80), self.screen)

        self.barra_sonido = Label(self.width // 2 - 150, self.height // 2 + 50,
                                  cargar_imagen(f"Recursos/Img/Menu/barra_sonido{self.index}.png", 288, 84), self.fuente, self.screen)

        self.layer = Layer(self.width // 2 - 236, self.height // 2 - 175,
                           cargar_imagen("Recursos\Img\Menu\layer.png", 472, 350), self.screen)

        self.label = Label(self.width // 2 - 150, self.height // 2 - 300,
                           cargar_imagen("Recursos\Img\Menu\label.png", 288, 84), self.fuente, self.screen, "Setings")

    def draw(self):
        if self.start_menu:
            self.layer.draw()
            self.label.draw()
            self.sonido_button.draw()
            self.stop_sonido_button.draw()
            self.volumen_mas_button.draw()
            self.volumen_menos_button.draw()
            self.inicio_button.draw()
            self.barra_sonido.draw()

    def update(self):
        self.draw()
