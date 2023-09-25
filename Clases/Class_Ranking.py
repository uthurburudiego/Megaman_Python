import pygame
from Clases.Class_Button import *
from Clases.Class_Label import *
from Clases.Class_Layer import *
from Clases.Class_TextBox import *
from Clases.utilidades import cargar_imagen, mostrar_mensaje


class Ranking():
    def __init__(self, screen) -> None:

        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.start_menu = True
        self.fuente = pygame.font.Font("Recursos\Fuentes\GAMERIA.ttf", 36)

        self.reiniciar_button = Button(self.width // 2 - 150, self.height // 2 + 50,
                                       cargar_imagen("Recursos/Img/Menu/btn_reiniciar.png", 80, 80), self.screen)

        self.aceptar_button = Button(self.width // 2 + 46, self.height // 2 + 50,
                                     cargar_imagen("Recursos/Img/Menu/btn_aceptar.png", 80, 80), self.screen)

        self.layer = Layer(self.width // 2 - 236, self.height // 2 - 175,
                           cargar_imagen("Recursos\Img\Menu\layer.png", 472, 350), self.screen)

        self.label = Label(self.width // 2 - 150, self.height // 2 - 300,
                           cargar_imagen("Recursos\Img\Menu\label.png", 288, 84), self.fuente, self.screen, "Game over")

        self.box = Label(self.width // 2 - 150, self.height // 2 - 50,
                         cargar_imagen("Recursos/Img/Menu/textBox.png", 288, 84), self.fuente, self.screen)

        self.text_box = TextBox(self.width // 2 - 125,
                                self.height // 2 - 30, 230, 40, 10, 40)

    def draw(self):
        self.layer.draw()
        self.label.draw()
        mostrar_mensaje(self.screen, "ingresar nombre", (self.width //
                        2 - 150, self.height // 2 - 120), self.fuente)
        self.reiniciar_button.draw()
        self.aceptar_button.draw()
        self.box.draw()
        self.text_box.draw(self.screen)

    def update(self):

        self.draw()
