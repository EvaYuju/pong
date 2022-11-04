# OK a) Cancha de 960 pixels de ancho por 720 de alto
# OK b) Pelota de 25 pixels de ancho y alto
# OK c) Palas de 10 pixels de ancho por 100 de alto
# d) Dentro de la ventana del juego (no en el marco de la aplicación), encima del marcador, aparecerá la leyenda
# "Juego de Ping-Pong"
# e) El movimiento del jugador contrario no depende de nuestra voluntad
# f) El marcador aparecerá en la parte superior de la cancha dibujada
# g) No aparecerá ninguna variable o función escrita en inglés
# h) No hay problema en utilizar en este caso variables globales
# i) Los sonidos suministrados deben asociarse al golpeo con la pala, a un tanto que sube al marcador, un rebote
# contra pared, comienzo de partida y ganador/perdedor de partida. Todos ellos pueden ser cambiados al gusto si
# se quiere
# j) El tipo de letra a usar para los textos será Goldman-Regular.ttf
# k) El código escrito en Python debe estar trufado de comentarios detallados con objeto de que otro desarrollador
# pueda entenderlo de una sola lectura

import pygame
import sys

# General setup / configuración general
pygame.init()  # Inicializa los módulos pygame y es requerido para cualquier tipo de juego
reloj = pygame.time.Clock()  # Método reloj


# Función de movimiento de bola
def animacion_bola():
    # Vbles globales
    global velocidad_bola_x, velocidad_bola_y

    # Movimiento bola
    bola.x += velocidad_bola_x
    bola.y += velocidad_bola_y
    # Detector de colisiones bola VS bordes
    if bola.top <= 0 or bola.bottom >= pantalla_alto:  # vertical
        velocidad_bola_y *= -1
    if bola.left <= 0 or bola.right >= pantalla_ancho:  # horizontal
        velocidad_bola_x *= -1
    # Detector de colisiones bola VS paletas
    if bola.colliderect(jugador) or bola.colliderect(oponente):
        velocidad_bola_x *= -1


# Creación de ventana (Tamaño, titulo):
pantalla_ancho = 960
pantalla_alto = 720

pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))  # display surface
pygame.display.set_caption('Pong')

# Rectángulos del juego (Game rectangles)
#        Pygame.Rect    (x,y,ancho,alto)
bola = pygame.Rect(pantalla_ancho / 2 - 15, pantalla_alto / 2 - 15, 25, 25)
jugador = pygame.Rect(pantalla_ancho - 20, pantalla_alto / 2 - 70, 10, 100)
oponente = pygame.Rect(10, pantalla_alto / 2 - 70, 10, 100)

# Variables colores objetos:
colorFondo = pygame.Color('grey12')
colorGris = (200, 200, 200)

# Variables movimiento objetos:
velocidad_bola_x = 7
velocidad_bola_y = 7
velocidad_jugador = 0
# velocidad_oponente = 0

# Bucle (donde ejecutaremos las funciones):
while True:
    # zona inputs
    for event in pygame.event.get():  # llamadas a todos los eventos de usuarios
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Cerrar el juego una vez termina
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocidad_jugador +=7
            if event.key == pygame.K_UP:
                velocidad_jugador -=7
    # Hemos movido la función definida al principio y ahora la llamamos en el bucle
    animacion_bola()
    jugador.y += velocidad_jugador

    # Visuals / Dibujos *** Importante orden , se dibujan en orden por encima de los anteriores ***
    pantalla.fill(colorFondo)  # Añadimos color al fondo
    pygame.draw.rect(pantalla, colorGris, jugador)  # dibujo paleta jugador
    pygame.draw.rect(pantalla, colorGris, oponente)  # dibujo paleta oponente
    pygame.draw.ellipse(pantalla, colorGris, bola)  # Dibujo bola
    pygame.draw.aaline(pantalla, colorGris, (pantalla_ancho / 2, 0), (pantalla_ancho / 2, pantalla_alto))

    # Updating the Window
    pygame.display.flip()
    reloj.tick(60)  # Reloj para ejecutar el bucle = 60 veces por segundo
