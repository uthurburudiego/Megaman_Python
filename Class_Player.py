
import pygame
from Class_Disparos import Disparos


class Player():
    def __init__(self, x, y, screen, animaciones):

        self.reiniciar(x, y, screen, animaciones)

    def update(self, mundo, grupo_enemigos, grupo_trampas, grupo_items, grupo_disparos, grupo_disparos_boss):
        delta_x = 0
        delta_y = 0

        self.animar()
        # get keypresses
        delta_x = self.mover(delta_x, grupo_disparos)

        # add gravity
        delta_y = self.gravedad(delta_y)

        # # verificar colisiones
        for cuadrado in mundo.lista_cuadricula:
           # verificar colision en x
            if cuadrado[1].colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
                delta_x = 0
            # verificar colision en y
            if cuadrado[1].colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
                # verificar si está debajo del suelo
                if self.velocidad_y < 0:
                    delta_y = cuadrado[1].bottom - self.rect.top
                    self.velocidad_y = 0
                # comprobar si está por encima del suelo
                elif self.velocidad_y >= 0:
                    delta_y = cuadrado[1].top - self.rect.bottom
                    self.velocidad_y = 0
                    self.esta_cayendo = False

        # verificar colisiones con enemigos
            if (self.cooldown_vidas > 3000 and (pygame.sprite.spritecollide(self, grupo_enemigos, False) or
                                                pygame.sprite.spritecollide(self, grupo_trampas, False) or
                                                pygame.sprite.spritecollide(self, grupo_disparos_boss, False))):
                self.que_animacion = "daño"
                self.recibiendo_daño = True
                self.vidas -= 1
                self.cooldown_vidas = 0
            self.cooldown_vidas += 1

        # colision con items
        if pygame.sprite.spritecollide(self, grupo_items, True):
            self.vidas += 1

        # Actualizar coordenadas del jugador
        self.rect.x += delta_x
        self.rect.y += delta_y

        # litmite de pantalla

        if self.rect.bottom > self.screen.get_width():
            self.rect.bottom = self.screen.get_height()
            delta_y = 0

        if self.rect.x > self.screen.get_width() - 40:
            self.rect.x = self.screen.get_width()
        if self.rect.x < 0:
            self.rect.x = 0

        # draw player onto screen
        self.screen.blit(self.image, self.rect)

    def animar(self):
        if self.index >= len(self.animaciones[self.que_animacion]):
            self.index = 0

        if self.cooldown_frames > 3:
            self.image = self.animaciones[self.que_animacion][self.index]
            self.index += 1
            self.cooldown_frames = 0
        self.cooldown_frames += 1

    def mover(self, delta_x, grupo_disparos):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.esta_cayendo == False:
            self.velocidad_y = -15
            self.esta_cayendo = True
            self.que_animacion = "salto"
            self.recibiendo_daño = False

        if key[pygame.K_LEFT]:
            delta_x -= self.velocidad_x
            self.direction = -1
            self.que_animacion = "movimiento_atras"
            self.recibiendo_daño = False
        elif key[pygame.K_RIGHT]:
            delta_x += self.velocidad_x
            self.direction = 1
            self.que_animacion = "movimiento_adelante"
            self.recibiendo_daño = False
        elif key[pygame.K_SPACE] and self.direction == 1:
            self.que_animacion = 'ataque_derecha'
            self.disparo(grupo_disparos)
        elif key[pygame.K_SPACE] and self.direction == -1:
            self.que_animacion = 'ataque_izquierda'
            self.disparo(grupo_disparos)
        elif self.direction == 1 and not self.esta_cayendo and not self.recibiendo_daño:
            self.que_animacion = 'quieto_derecha'
        elif self.direction == -1 and not self.esta_cayendo and not self.recibiendo_daño:
            self.que_animacion = 'quieto_izquierda'

        return delta_x

    def gravedad(self, delta_y):
        self.velocidad_y += 1
        if self.velocidad_y > 10:
            self.velocidad_y = 10
        delta_y += self.velocidad_y
        return delta_y

    def reiniciar(self, x, y, screen, animaciones):
        self.screen = screen

        # animaciones
        self.flag_llegada = True
        self.animaciones = animaciones
        self.que_animacion = "quieto_derecha"
        self.index = 0
        self.cooldown_frames = 0
        self.image = pygame.transform.scale(
            self.animaciones[self.que_animacion][self.index], (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocidad_y = 0
        self.velocidad_x = 5
        self.esta_cayendo = False
        self.direction = 0

        self.cooldown_vidas = 0
        self.vidas = 3
        self.recibiendo_daño = False
        self.exit = False
        self.llaves = 0

        self.cooldown_disparos = 0

    def disparo(self, grupo_disparos):
        if self.cooldown_disparos > 8:
            bala = Disparos(self.rect.x + self.width * self.direction,
                            self.rect.y + self.height/2, self.screen, self.direction, pygame.image.load("Recursos/Img/Proyectiles/1.png"))
            grupo_disparos.add(bala)
            self.cooldown_disparos = 0
        self.cooldown_disparos += 1
