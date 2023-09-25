import pygame
from Clases.Class_Disparos import Disparos
from Clases.Class_Player import Player


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, animacion) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.animacion = animacion
        self.que_animacion = "quieto_derecha"
        self.index = 0
        self.cooldown = 0
        self.image = pygame.transform.scale(
            self.animacion[self.que_animacion][self.index], (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mover_direccion = 1
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocidad_y = 0
        self.velocidad_x = 5
        self.esta_cayendo = False
        self.direction = 0
        self.contador_movimiento = 0

    def update(self, mundo, grupo_disparos) -> None:

        self.move_enemy()
        self.animar()

        delta_x = 0
        delta_y = 0
        # add gravity
        self.velocidad_y += 1
        if self.velocidad_y > 10:
            self.velocidad_y = 10
        delta_y += self.velocidad_y

        # verificar colision
        for tile in mundo.lista_cuadricula:
            # verificar colision en x
            if tile[1].colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
                delta_x = 0
            # verificar colision en y
            if tile[1].colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
                # verificar si está debajo del suelo
                if self.velocidad_y < 0:
                    delta_y = tile[1].bottom - self.rect.top
                    self.velocidad_y = 0
                # comprobar si está por encima del suelo
                elif self.velocidad_y >= 0:
                    delta_y = tile[1].top - self.rect.bottom
                    self.velocidad_y = 0
                    self.esta_cayendo = False

        if pygame.sprite.spritecollide(self, grupo_disparos, True):
            self.kill()

        # Actualizar coordenadas del enemigo
        self.rect.x += delta_x
        self.rect.y += delta_y
        if self.rect.bottom > self.screen.get_width():
            self.rect.bottom = self.screen.get_height()
            delta_y = 0

    def move_enemy(self):
        self.rect.x += self.mover_direccion
        self.contador_movimiento += 1
        if abs(self.contador_movimiento) > 50:
            self.mover_direccion *= -1
            self.contador_movimiento *= -1

    def animar(self):
        if self.index >= len(self.animacion[self.que_animacion]):
            self.index = 0

        if self.cooldown > 3:
            self.image = self.animacion[self.que_animacion][self.index]
            self.index += 1
            self.cooldown = 0
        self.cooldown += 1


class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, animacion) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.animacion = animacion
        self.index = 0
        self.cooldown = 0
        self.image = self.animacion[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mover_direccion = 1
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocidad_y = 0
        self.velocidad_x = 5
        self.direction = 1
        self.cooldown_disparos = 0
        self.contador_movimiento = 0
        self.vida_enemigo = 20

    def update(self, mundo, grupo_disparos, jugador: Player, grupo_disparos_boss) -> None:
        print(self.vida_enemigo)

        if pygame.sprite.spritecollide(self, grupo_disparos, True):

            self.vida_enemigo -= 1

        if self.vida_enemigo <= 0:
            jugador.score += 3000
            jugador.llaves = 3
            self.kill()

        self.disparo(grupo_disparos_boss)
        self.move_enemy()
        self .animar()

    def animar(self):
        if self.index >= len(self.animacion):
            self.index = 0

        if self.cooldown > 3:
            self.image = self.animacion[self.index]
            self.index += 1
            self.cooldown = 0
        self.cooldown += 1

    def move_enemy(self):
        self.rect.x += self.mover_direccion
        self.rect.y += self.mover_direccion

        self.contador_movimiento += 1
        if abs(self.contador_movimiento) > 50:

            self.mover_direccion *= -1
            self.contador_movimiento *= -1

    def disparo(self, grupo_disparos):
        if self.cooldown_disparos > 40:
            bala = Disparos(self.rect.x + self.width * self.direction,
                            self.rect.y + self.height/2 + 30, self.screen, self.direction, pygame.image.load("Recursos\Img\Enemys\Boss\disparo.png"))
            grupo_disparos.add(bala)
            self.cooldown_disparos = 0
        self.cooldown_disparos += 1
