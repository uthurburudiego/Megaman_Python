import pygame


def dibujar_cuadricula(screen: pygame.Surface, tamaño_cuadricula: int):
    width = screen.get_width()
    height = screen.get_height()

    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line *
                         tamaño_cuadricula), (width, line * tamaño_cuadricula))
        pygame.draw.line(screen, (255, 255, 255), (line *
                         tamaño_cuadricula, 0), (line * tamaño_cuadricula, height))


def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada


def obtener_rectangulos(principal) -> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(
        principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(
        principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(
        principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(
        principal.left, principal.top, principal.width, 10)
    return diccionario


def mostrar_mensaje(screen, texto, posicion):
    font = pygame.font.Font(None, 24)  # Crea una fuente
    mensaje = font.render(texto, True, (255, 255, 255))  # Renderiza el texto
    screen.blit(mensaje, posicion)  # Muestra el mensaje en la pantalla


########################################################################################################################################
    # CARGA DE IMAGENES #

def cargar_imagenes_personaje():
    personaje_quieto_derecha = [
        pygame.image.load("Recursos/Img/Player/Megaman/quieto (1).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/quieto (2).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/quieto (3).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/quieto (4).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/quieto (5).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/quieto (6).png")
    ]
    personaje_quieto_izquierda = girar_imagenes(
        personaje_quieto_derecha, True, False)

    personaje_movimiento_adelante = [
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (1).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (2).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (3).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (4).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (5).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (6).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (7).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (8).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (9).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/movimiento (10).png")
    ]

    personaje_movimiento_atras = girar_imagenes(
        personaje_movimiento_adelante, True, False)

    personaje_salto = [
        pygame.image.load("Recursos/Img/Player/Megaman/saltar (1).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/saltar (2).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/saltar (3).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/saltar (4).png")
    ]

    personaje_ataque_derecha = [
        pygame.image.load("Recursos/Img/Player/Megaman/atacar (1).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/atacar (2).png"),
        pygame.image.load("Recursos/Img/Player/Megaman/atacar (3).png"),
    ]
    personaje_ataque_izquierda = girar_imagenes(
        personaje_ataque_derecha, True, False)

    personaje_daño = [
        pygame.image.load("Recursos\Img\Player\Megaman\daño.png"),
        pygame.image.load("Recursos\Img\Player\Megaman\daño (2).png"),
        pygame.image.load("Recursos\Img\Player\Megaman\daño (3).png"),
        pygame.image.load("Recursos\Img\Player\Megaman\daño (4).png"),
        pygame.image.load("Recursos\Img\Player\Megaman\daño (5).png"),
    ]

    return {
        'quieto_derecha': personaje_quieto_derecha,
        'quieto_izquierda': personaje_quieto_izquierda,
        'movimiento_adelante': personaje_movimiento_adelante,
        'movimiento_atras': personaje_movimiento_atras,
        'salto': personaje_salto,
        'ataque_derecha': personaje_ataque_derecha,
        'ataque_izquierda': personaje_ataque_izquierda,
        'daño': personaje_daño
    }


def cargar_imagenes_enemigo():
    personaje_quieto = [
        pygame.image.load("Recursos\Img\Enemys\BombMan\quieto.png"),
        pygame.image.load("Recursos\Img\Enemys\BombMan\quieto (1).png"),
        pygame.image.load("Recursos\Img\Enemys\BombMan\quieto (2).png"),
        pygame.image.load("Recursos\Img\Enemys\BombMan\quieto (3).png"),
        pygame.image.load("Recursos\Img\Enemys\BombMan\quieto (4).png")
    ]

    personaje_muerto = [
        pygame.image.load("Recursos\Img\Enemys\BombMan\explosion(1).png"),
        pygame.image.load("Recursos\Img\Enemys\BombMan\explosion(2).png"),
        pygame.image.load("Recursos\Img\Enemys\BombMan\explosion(3).png"),
        pygame.image.load("Recursos\Img\Enemys\BombMan\explosion(4).png"),

    ]

    return {
        'quieto_derecha': personaje_quieto,
        'muerto': personaje_muerto
    }


def cargar_imagenes_items():
    item = [
        pygame.image.load("Recursos/Img/Items/vida (1).png"),
        pygame.image.load("Recursos/Img/Items/vida (2).png"),
        pygame.image.load("Recursos/Img/Items/vida (3).png"),
        pygame.image.load("Recursos/Img/Items/vida (4).png"),
        pygame.image.load("Recursos/Img/Items/vida (5).png"),
        pygame.image.load("Recursos/Img/Items/vida (6).png"),
        pygame.image.load("Recursos/Img/Items/vida (7).png")
    ]
    return item


def cargar_imagenes_lampara():
    salida = [
        pygame.image.load("Recursos\Img\Items\salida (1).png"),
        pygame.image.load("Recursos\Img\Items\salida (2).png"),
        pygame.image.load("Recursos\Img\Items\salida (3).png"),

    ]
    saliendo = [
        pygame.image.load("Recursos\Img\Items\salida (4).png"),
        pygame.image.load("Recursos\Img\Items\salida (5).png"),
    ]
    return{
        'salida': salida,
        'saliendo': saliendo
    }


def cargar_imagenes_salida():
    salida = [
        pygame.image.load("Recursos\Img\Maps\door_1.png"),
        pygame.image.load("Recursos\Img\Maps\door_2.png"),
        pygame.image.load("Recursos\Img\Maps\door_3.png"),
        pygame.image.load("Recursos\Img\Maps\door_4.png"),
        pygame.image.load("Recursos\Img\Maps\door_5.png"),
    ]
    return salida


def cargar_imagenes_boss():
    boss = [
        pygame.image.load("Recursos/Img/Enemys/Boss/boss_01.png"),
        pygame.image.load("Recursos/Img/Enemys/Boss/boss_02.png"),
        pygame.image.load("Recursos/Img/Enemys/Boss/boss_03.png"),
        pygame.image.load("Recursos/Img/Enemys/Boss/boss_04.png"),
        pygame.image.load("Recursos/Img/Enemys/Boss/boss_05.png"),
    ]
    boss = girar_imagenes(boss, True, False)
    return boss
