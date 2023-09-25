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
from Clases.Class_Ranking import*
from Clases.Class_Setings import*
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
        self.setings = Setings(self.screen)
        self.rating = Ranking(self.screen)
        self.volumen = 0.1
        self.jugador = Player(100, self.height - 100,
                              self.screen, animaciones_jugador)
        self.fuente = pygame.font.Font("Recursos\Fuentes\GAMERIA.ttf", 36)
        self.tiempo = 0
        self.game_over = False
        self.jugador_name = ""

        # Sonidos
        self.sonido_ambiente = pygame.mixer.Sound(
            "Recursos\Songs\megaman-1.mp3")
        self.sonido_ambiente.set_volume(self.volumen)

        # buttons
        self.restart_button = Button(self.width // 2 - 50, self.height // 2 - 100,
                                     pygame.image.load("Recursos/Img/Menu/btn_restart.png"), self.screen)

        self.text_box = TextBox(self.width // 2 - 150,
                                self.height // 2 - 50, 288, 84, 10)

        self.diseñar_mapa()

    def update(self):
        run = True
        key = key = pygame.key.get_pressed()
        for event in pygame.event.get():
            self.jugador_name = self.rating.text_box.handle_event(event)
        # Si no esta el menu abierto
        if not self.menu.start_menu and not self.game_over:
            self.tiempo = int(pygame.time.get_ticks() / 1000)
            self.jugador.time = self.tiempo
            self.draw()
            if self.jugador.vidas > 0:
                mostrar_mensaje(
                    self.screen, f"lives {self.jugador.vidas}", (80, 80), self.fuente)
                mostrar_mensaje(
                    self.screen, f"time {self.tiempo}", (self.width // 2, 80), self.fuente)
                mostrar_mensaje(
                    self.screen, f"score {self.jugador.score}", (self.width - 250, 80), self.fuente)

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
            elif self.rating.start_menu:
                self.rating.draw()
                if self.rating.reiniciar_button.clicked:
                    self.rating.start_menu = False
                    self.reiniciar_nivel()
                    self.jugador.reiniciar(
                        100, self.height - 100, self.screen, animaciones_jugador)
                if self.rating.aceptar_button.clicked:
                    with open("Recursos\Archivos\Puntajes.json", 'w') as archivo:
                        json.dump(
                            f"nombre: {self.jugador_name} - Score: {self.jugador.final_score}",archivo)
            # MENU DE OPCIONES
        if self.menu.start_menu or key[pygame.K_ESCAPE]:
            self.menu.start_menu = True
            if not self.opciones.start_menu:
                self.menu.draw()

            # aca va a estar el menu
            if self.menu.inicio_button.clicked:
                self.menu.start_menu = False  # ENTRAR AL JUEGO
            if self.menu.exit_button.clicked:
                run = False  # CERRAR EL JUEGO
            if self.menu.option_button.clicked:  # ABRE OPCIONES
                self.opciones.start_menu = True
                if self.menu.start_menu:
                    if not self.setings.start_menu:
                        self.opciones.draw()
                if self.opciones.setings_button.clicked:
                    self.setings.start_menu = True  # ABRE SETINGS
                    self.setings.draw()
                    if self.setings.sonido_button.clicked:
                        # Prendemos musica de fondo
                        self.sonido_ambiente.play(-1)
                    if self.setings.stop_sonido_button.clicked:
                        self.sonido_ambiente.stop()  # Paramos musica de fondo
                    if self.setings.volumen_mas_button.clicked:
                        if self.setings.index <= 5:
                            self.setings.index += 1
                            self.volumen += 0.1
                    if self.setings.volumen_menos_button.clicked:
                        if self.setings.index >= 0:
                            self.setings.index -= 1
                            self.volumen -= 0.1
                    if self.setings.inicio_button.clicked:
                        self.setings.start_menu = False
                self.sonido_ambiente.set_volume(self.volumen)

            if self.opciones.back_button.clicked:  # Aca se cierran
                self.opciones.start_menu = False

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
        self.rating.start_menu = True

        self.diseñar_mapa()
        self.draw()

    def diseñar_mapa(self):
        tamaño_cuadricula = 50
        contar_fila = 0

        try:
            with open(f"Recursos/Archivos/Nivel_0{self.nivel}.json", "r") as archivo:
                data = json.load(archivo)
        except FileNotFoundError:
            # Maneja la excepción si el archivo no existe
            print(f"El archivo Nivel_0{self.nivel}.json no se encuentra.")
        except json.JSONDecodeError as e:
            # Maneja la excepción si hay un error en el formato JSON
            print(f"Error en el formato JSON del archivo: {e}")
        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            print(f"Ocurrió un error al cargar el archivo: {e}")

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
