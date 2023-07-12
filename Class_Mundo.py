import pygame

from utilidades import *
import json
from Class_Enemy import Enemy, Boss
from Class_Player import Player
from Class_Button import Button
from Class_Items import*
from Class_Nivel import Nivel
from Class_Obstaculos import*


tamaño_cuadricula = 50
grupo_puerta = pygame.sprite.Group()
grupo_lamparas = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()
grupo_disparos = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_boss = pygame.sprite.Group()
grupo_disparos_boss = pygame.sprite.Group()
grupo_trampas = pygame.sprite.Group()
tierra_img = pygame.image.load("Recursos/Img/Maps/bloque_tierra.png")
piso_img = pygame.image.load("Recursos/Img/Maps/bloque_metal.png")

animacion_enemigo = cargar_imagenes_enemigo()
animacion_boss = cargar_imagenes_boss()
animaciones_jugador = cargar_imagenes_personaje()
animacion_vida = cargar_imagenes_items()
animacion_lamparas = cargar_imagenes_lampara()
animacion_salida = cargar_imagenes_salida()
nivel = Nivel()


class Mundo():
    def __init__(self, screen) -> None:
        with open(f"Nivel_0{nivel.que_nivel}.json", "r") as archivo:
            data = json.load(archivo)
        self.lista_cuadricula = []
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.start_menu = True
        self.jugador = Player(100, self.height - 100,
                              self.screen, animaciones_jugador)

        # buttons
        self.restart_button = Button(self.width // 2 - 50, self.height // 2 + 100,
                                     pygame.image.load("Recursos/Img/Menu/restart_btn.png"), self.screen)
        self.start_button = Button(self.width // 2 - 350, self.height // 2 - 63,
                                   pygame.image.load("Recursos/Img/Menu/start_btn.png"), self.screen)
        self.save_button = Button(self.width // 2 - 279, self.height // 2,
                                  pygame.image.load("Recursos/Img/Menu/save_btn.png"), self.screen)
        self.exit_button = Button(self.width // 2, self.height // 2 - 63,
                                  pygame.image.load("Recursos/Img/Menu/exit_btn.png"), self.screen)

    # DISEÑO DE MAPA

        contar_fila = 0
        for fila in data:
            contar_columna = 0
            for cuadricula in fila:
                ##############################  Obstaculos ##############################
                # agregar lava #1
                if cuadricula == 1:
                    lava = Lava(contar_columna * tamaño_cuadricula,
                                contar_fila * tamaño_cuadricula + (tamaño_cuadricula // 2),  tamaño_cuadricula)
                    grupo_trampas.add(lava)
                if cuadricula == 2:
                    pinchos = Pinchos(contar_columna * tamaño_cuadricula,
                                      contar_fila * tamaño_cuadricula + (tamaño_cuadricula // 2),  tamaño_cuadricula)
                    grupo_trampas.add(pinchos)
                if cuadricula == 8:
                    puerta = Puerta(contar_columna * tamaño_cuadricula,
                                    contar_fila * tamaño_cuadricula, tamaño_cuadricula, animacion_salida)
                    grupo_puerta.add(puerta)
                ##############################  ENEMIGOS  ##############################
                    # agregar Enemigos #3
                if cuadricula == 3:
                    enemigo = Enemy(contar_columna * tamaño_cuadricula,
                                    contar_fila * tamaño_cuadricula + 15, self.screen, animacion_enemigo)
                    grupo_enemigos.add(enemigo)
                if cuadricula == 9:
                    boss = Boss(contar_columna * tamaño_cuadricula,
                                contar_fila * tamaño_cuadricula + 15, self.screen, animacion_boss)
                    grupo_boss.add(boss)
                ##############################  ITEMS  ##############################
                    # VIDAS #4
                if cuadricula == 4:
                    vida = Vida(contar_columna * tamaño_cuadricula,
                                contar_fila * tamaño_cuadricula + 15, self.screen, animacion_vida)
                    grupo_items.add(vida)
                    # LAMPARAS #7
                if cuadricula == 7:
                    salida = Lamps(contar_columna * tamaño_cuadricula,
                                   contar_fila * tamaño_cuadricula + 15, self.screen, animacion_lamparas)
                    grupo_lamparas.add(salida)
                 ##############################  PLATAFORMAS  ##############################
                # agregar piso #5
                if cuadricula == 5:
                    img = pygame.transform.scale(
                        piso_img, (tamaño_cuadricula, tamaño_cuadricula))
                    img_rect = img.get_rect()
                    img_rect.x = contar_columna * tamaño_cuadricula
                    img_rect.y = contar_fila * tamaño_cuadricula
                    cuadricula = (img, img_rect)
                    self.lista_cuadricula.append(cuadricula)

                # agregar tierra
                if cuadricula == 6:
                    img = pygame.transform.scale(
                        tierra_img, (tamaño_cuadricula, tamaño_cuadricula))
                    img_rect = img.get_rect()
                    img_rect.x = contar_columna * tamaño_cuadricula
                    img_rect.y = contar_fila * tamaño_cuadricula
                    cuadricula = (img, img_rect)
                    self.lista_cuadricula.append(cuadricula)
                contar_columna += 1
            contar_fila += 1

    def draw(self):
        run = True
        key = key = pygame.key.get_pressed()

        if not self.start_menu:
            for cuadricula in self.lista_cuadricula:
                self.screen.blit(cuadricula[0], cuadricula[1])
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 cuadricula[1], 2)

            grupo_enemigos.draw(self.screen)
            grupo_enemigos.update(self, grupo_disparos)
            grupo_boss.draw(self.screen)
            grupo_boss.update(self, grupo_disparos,
                              self.jugador, grupo_disparos_boss)
            grupo_disparos_boss.draw(self.screen)
            grupo_disparos_boss.update()
            grupo_trampas.draw(self.screen)
            grupo_items.draw(self.screen)
            grupo_items.update()
            grupo_lamparas.draw(self.screen)
            grupo_lamparas.update(self.jugador)
            grupo_puerta.draw(self.screen)
            grupo_puerta.update(self.jugador)

            if self.jugador.vidas > 0:
                # cambiar de nivel
                if self.jugador.exit:
                    nivel.que_nivel += 1
                    self.jugador.exit = False
                    self.reiniciar_nivel()
                self.jugador.update(self,
                                    grupo_enemigos, grupo_trampas, grupo_items, grupo_disparos, grupo_disparos_boss)
                grupo_disparos.draw(self.screen)
                grupo_disparos.update()

    # Si el jugador pierde todas la vidas
            elif self.restart_button.draw():
                self.jugador.reiniciar(
                    100, self.height - 100, self.screen, animaciones_jugador)

            mostrar_mensaje(
                self.screen, f"vidas : {self.jugador.vidas}", (60, 60))
        if self.start_menu or key[pygame.K_ESCAPE]:
            self.start_menu = True
            # aca va a estar el menu
            if self.start_button.draw():
                self.start_menu = False
            if self.exit_button.draw():
                run = False

        return run

    def reiniciar_nivel(self):
        self.lista_cuadricula = []
        self.jugador.reiniciar(100, self.height - 100,
                               self.screen, animaciones_jugador)
        grupo_enemigos.empty()
        grupo_boss.empty()
        grupo_trampas.empty()
        grupo_items.empty()
        grupo_lamparas.empty()
        grupo_puerta.empty()
        mundo = Mundo(self.screen)
