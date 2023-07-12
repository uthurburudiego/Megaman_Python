import pygame
from utilidades import obtener_rectangulos


class Jugador():
    def __init__(self, pantalla, x, y, animaciones) -> None:
        self.pantalla = pantalla
        self.width = pantalla.get_width()
        self.height = pantalla.get_height()

        # animaciones
        self.flag_llegada = True
        self.animaciones = animaciones
        self.que_animacion = "quieto_derecha"
        self.index = 0
        self.cooldown = 0
        self.image = pygame.transform.scale(
            self.animaciones[self.que_animacion][self.index], (40, 50))

        # movimiento
        self.rect = self.image.get_rect()
        self.width_image = self.image.get_width()
        self.height_image = self.image.get_height()
        self.rect.x = x
        self.rect.y = y
        self.lados = obtener_rectangulos(self.rect)
        self.velocidad_y = 0
        self.velocidad_x = 5
        self.esta_saltando = False
        self.orientacion = True
        self.direccion_x = 0
        self.direccion_y = 0

    def update(self, lista_eventos, mundo):

        self.pantalla.blit(self.image, self.rect)
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.rect, 2)

        

             # check for collision
        self.in_air = True
        for cuadricula in mundo.lista_cuadricula:
            # check for collision in x direction
            if cuadricula[1].colliderect(self.rect.x + self.direccion_x, self.rect.y, self.width, self.height):
                print("colisiono en x")
                self.direccion_x = 0
            # check for collision in y direction
            if cuadricula[1].colliderect(self.rect.x, self.rect.y + self.direccion_y, self.width, self.height):
                print("colisiono en y")
                # check if below the ground i.e. jumping
                if self.velocidad_y < 0:
                    self.direccion_y = cuadricula[1].bottom - self.rect.top
                    self.velocidad_y = 0
                # check if above the ground i.e. falling
                elif self.velocidad_y >= 0:
                    self.direccion_y = cuadricula[1].top - self.rect.bottom
                    self.velocidad_y = 0
                    self.in_air = False
                   

        self.controlar_jugador()
        self.animar()
        self.gravedad()

    def controlar_jugador(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.esta_saltando == False:
            self.velocidad_y = -15
            self.esta_saltando = True
            self.que_animacion = "salto"

        if key[pygame.K_LEFT]:
            self.direccion_x -= self.velocidad_x
            self.que_animacion = 'movimiento_atras'
            self.orientacion = False
        elif key[pygame.K_RIGHT]:
            self.que_animacion = 'movimiento_adelante'
            self.direccion_x += self.velocidad_x
            self.orientacion = True
        elif self.orientacion and not self.esta_saltando:
            self.que_animacion = 'quieto_derecha'
        elif not self.orientacion and not self.esta_saltando:
            self.que_animacion = 'quieto_izquierda'

        self.rect.x = self.direccion_x
        self.rect.y = self.direccion_y


    # gravedad
      
    # litmite de pantalla

        if self.rect.bottom > self.height:
            self.rect.y = self.height - 50
            self.esta_saltando = False
            self.velocidad_y = 0
        if self.rect.right > self.width:
            self.rect.x = self.width - 40
        if self.rect.left < 0:
            self.rect.x = 0

    def animar(self):
        if self.index >= len(self.animaciones[self.que_animacion]):
            self.index = 0

        if self.cooldown > 3:
            self.image = self.animaciones[self.que_animacion][self.index]
            self.index += 1
            self.cooldown = 0
        self.cooldown += 1

    def gravedad(self):
        self.velocidad_y += 1
        if self.velocidad_y > 10:
            self.velocidad_y = 10
        self.direccion_y += self.velocidad_y

        