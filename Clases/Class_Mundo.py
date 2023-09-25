import pygame
from Clases.utilidades import *
import json
from Clases.Class_Enemy import Enemy, Boss
from Clases.Class_Button import Button
from Clases.Class_Layer import Layer

from Clases.Class_Items import*
from Clases.Class_Obstaculos import*
from Clases.Class_Menu import*
from Clases.Class_Opciones import*
from pygame import mixer

# Constantes para el tipo de cuadricula
TIPO_LAVA = 1
TIPO_PINCHOS = 2
TIPO_PUERTA = 8
TIPO_ENEMIGO = 3
TIPO_BOSS = 9
TIPO_VIDA = 4
TIPO_LAMPARA = 7
TIPO_PISO = 5
TIPO_TIERRA = 6


# Crear los grupos para elemtos del juego
grupo_puerta = pygame.sprite.Group()
grupo_lamparas = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()
grupo_disparos = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_boss = pygame.sprite.Group()
grupo_disparos_boss = pygame.sprite.Group()
grupo_trampas = pygame.sprite.Group()

# Cargar todas las imagenes
tierra_img = pygame.image.load("Recursos/Img/Maps/bloque_tierra.png")
piso_img = pygame.image.load("Recursos/Img/Maps/bloque_metal.png")
animacion_enemigo = cargar_imagenes_enemigo()
animacion_boss = cargar_imagenes_boss()
animaciones_jugador = cargar_imagenes_personaje()
animacion_vida = cargar_imagenes_items()
animacion_lamparas = cargar_imagenes_lampara()
animacion_salida = cargar_imagenes_salida()


class Mundo():
    def __init__(self, screen) -> None:

        self.nivel = 1
        self.lista_cuadricula = []
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.menu = Menu(self.screen)
        self.opciones = Opciones(self.screen)
        self.jugador = Player(100, self.height - 100,
                              self.screen, animaciones_jugador)

        # Sonidos
        self.sonido_ambiente = pygame.mixer.Sound(
            "Recursos\Songs\megaman-1.mp3")
        self.sonido_ambiente.set_volume(0.2)

        # buttons
        self.restart_button = Button(self.width // 2 - 50, self.height // 2 - 100,
                                     pygame.image.load("Recursos/Img/Menu/btn_reiniciar.png"), self.screen)

        self.diseñar_mapa()

    def update(self):
        run = True
        key = key = pygame.key.get_pressed()

        # Si no esta el menu abierto
        if not self.menu.start_menu:
            self.draw()
            if self.jugador.vidas > 0:

                # Si pasa de Nivel
                if self.jugador.exit:
                    self.nivel += 1
                    self.jugador.exit = False
                    self.reiniciar_nivel()
                self.jugador.update(self,
                                    grupo_enemigos, grupo_trampas, grupo_items, grupo_disparos, grupo_disparos_boss)
                grupo_disparos.draw(self.screen)
                grupo_disparos.update()
                # Si el jugador pierde todas la vidas
            elif self.restart_button.draw():

                self.reiniciar_nivel()
                self.jugador.reiniciar(
                    100, self.height - 100, self.screen, animaciones_jugador)
            # MENU DE OPCIONES
        if self.menu.start_menu or key[pygame.K_ESCAPE]:
            self.menu.start_menu = True
            if not self.opciones.start_menu:
                self.menu.draw()

            # aca va a estar el menu
            if self.menu.inicio_button.clicked:  # ENTRAR AL JUEGO
                self.menu.start_menu = False
            if self.menu.exit_button.clicked:  # CERRAR EL JUEGO
                run = False
            if self.menu.option_button.clicked:
                self.opciones.start_menu = True
                if self.menu.start_menu:
                    self.opciones.draw()
            if self.opciones.back_button.clicked:
                self.opciones.start_menu = False
                self.menu.start_menu = True

        return run

    # DISEÑO DE MAPA

    def draw(self):

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

    def reiniciar_nivel(self):

        self.jugador.rect.x = 100
        self.jugador.rect.y = self.height - 100
        self.jugador.llaves = 0

        grupo_enemigos.empty()
        grupo_boss.empty()
        grupo_trampas.empty()
        grupo_items.empty()
        grupo_lamparas.empty()
        grupo_puerta.empty()
        self.lista_cuadricula.clear()

        self.diseñar_mapa()
        self.draw()

    def diseñar_mapa(self):
        tamaño_cuadricula = 50
        contar_fila = 0

        with open(f"Recursos/Archivos/Nivel_0{self.nivel}.json", "r") as archivo:
            data = json.load(archivo)

        for fila in data:
            contar_columna = 0
            for cuadricula in fila:
                ##############################  Obstaculos ##############################
                if cuadricula == TIPO_LAVA:
                    lava = Lava(contar_columna * tamaño_cuadricula,
                                contar_fila * tamaño_cuadricula + (tamaño_cuadricula // 2),  tamaño_cuadricula)
                    grupo_trampas.add(lava)

                if cuadricula == TIPO_PINCHOS:
                    pinchos = Pinchos(contar_columna * tamaño_cuadricula,
                                      contar_fila * tamaño_cuadricula + (tamaño_cuadricula // 2),  tamaño_cuadricula)
                    grupo_trampas.add(pinchos)

                if cuadricula == TIPO_PUERTA:
                    puerta = Puerta(contar_columna * tamaño_cuadricula,
                                    contar_fila * tamaño_cuadricula, tamaño_cuadricula, animacion_salida)
                    grupo_puerta.add(puerta)
                ##############################  ENEMIGOS  ##############################
                    # agregar Enemigos #3
                if cuadricula == TIPO_ENEMIGO:
                    enemigo = Enemy(contar_columna * tamaño_cuadricula,
                                    contar_fila * tamaño_cuadricula + 15, self.screen, animacion_enemigo)
                    grupo_enemigos.add(enemigo)

                if cuadricula == TIPO_BOSS:
                    boss = Boss(contar_columna * tamaño_cuadricula,
                                contar_fila * tamaño_cuadricula + 15, self.screen, animacion_boss)
                    grupo_boss.add(boss)
                ##############################  ITEMS  ##############################
                if cuadricula == TIPO_VIDA:
                    vida = Vida(contar_columna * tamaño_cuadricula,
                                contar_fila * tamaño_cuadricula + 15, self.screen, animacion_vida)
                    grupo_items.add(vida)

                if cuadricula == TIPO_LAMPARA:
                    salida = Lamps(contar_columna * tamaño_cuadricula,
                                   contar_fila * tamaño_cuadricula + 15, self.screen, animacion_lamparas)
                    grupo_lamparas.add(salida)
                 ##############################  PLATAFORMAS  ##############################
                if cuadricula == TIPO_PISO:
                    img = pygame.transform.scale(
                        piso_img, (tamaño_cuadricula, tamaño_cuadricula))
                    img_rect = img.get_rect()
                    img_rect.x = contar_columna * tamaño_cuadricula
                    img_rect.y = contar_fila * tamaño_cuadricula
                    cuadricula = (img, img_rect)
                    self.lista_cuadricula.append(cuadricula)

                if cuadricula == TIPO_TIERRA:
                    img = pygame.transform.scale(
                        tierra_img, (tamaño_cuadricula, tamaño_cuadricula))
                    img_rect = img.get_rect()
                    img_rect.x = contar_columna * tamaño_cuadricula
                    img_rect.y = contar_fila * tamaño_cuadricula
                    cuadricula = (img, img_rect)
                    self.lista_cuadricula.append(cuadricula)
                contar_columna += 1
            contar_fila += 1
