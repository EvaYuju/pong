# OK a) Cancha de 960 pixels de ancho por 720 de alto
# OK b) Pelota de 25 pixels de ancho y alto
# OK c) Palas de 10 pixels de ancho por 100 de alto
# d) Dentro de la ventana del juego (no en el marco de la aplicación), encima del marcador, aparecerá la leyenda
# "Juego de Ping-Pong"
# OK e) El movimiento del jugador contrario no depende de nuestra voluntad
# f) El marcador aparecerá en la parte superior de la cancha dibujada
# OK g) No aparecerá ninguna variable o función escrita en inglés
# h) No hay problema en utilizar en este caso variables globales
# i) Los sonidos suministrados deben asociarse al golpeo con la pala, a un tanto que sube al marcador, un rebote
# contra pared, comienzo de partida y ganador/perdedor de partida. Todos ellos pueden ser cambiados al gusto si
# se quiere
# OK j) El tipo de letra a usar para los textos será Goldman-Regular.ttf
# OK k) El código escrito en Python debe estar trufado de comentarios detallados con objeto de que otro desarrollador
# pueda entenderlo de una sola lectura
import random

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
        #  Velocidad_bola_x *= -1 // Sustituimos la línea que invierte la velocidad de la bola por una que la resetea :
        resetear_bola()
    # Detector de colisiones bola VS paletas
    if bola.colliderect(jugador) or bola.colliderect(oponente):
        velocidad_bola_x *= -1


# Función de movimiento de la paleta del jugador
def animacion_jugador():
    # Constantes paleta
    jugador.y += velocidad_jugador
    # Condición si la paleta del jugador toca el borde superior o inferior
    if jugador.top <= 0:
        jugador.top = 0
    if jugador.bottom >= pantalla_alto:
        jugador.bottom = pantalla_alto


# Función de movimiento de la paleta del oponente
def animacion_oponente():
    # Movimiento paleta:
    if oponente.top < bola.y:
        oponente.top += velocidad_oponente
    if oponente.bottom > bola.y:
        oponente.bottom -= velocidad_oponente
    # Controlar tocar borde superior/inferior
    if oponente.top <= 0:
        oponente.top = 0
    if oponente.bottom >= pantalla_alto:
        oponente.bottom = pantalla_alto


# Función resetear bola :
def resetear_bola():
    # Vbles globales bola
    global velocidad_bola_x, velocidad_bola_y
    bola.center = (pantalla_ancho / 2, pantalla_alto / 2)
    # Aumento de velocidad al perder
    velocidad_bola_y *= random.choice((1, -1))
    velocidad_bola_x *= random.choice((1, -1))


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

# Variables de movimiento objetos:
velocidad_bola_x = 7 * random.choice((1, -1))
velocidad_bola_y = 7 * random.choice((1, -1))
velocidad_jugador = 0
velocidad_oponente = 7

# Variables de texto:
Puntos_jugador = 0
Puntos_oponente = 0
#                                                (Nombre fuente, tamaño)
Fuente_1 = pygame.font.Font(pygame.font.match_font("Goldman-Regular.ttf"), 32)



# Bucle (donde ejecutaremos las funciones):
while True:
    # zona inputs
    for event in pygame.event.get():  # llamadas a todos los eventos de usuarios
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Cerrar el juego una vez termina
        if event.type == pygame.KEYDOWN:  # Eventos de teclado para manejar la paleta del jugador
            if event.key == pygame.K_DOWN:
                velocidad_jugador += 7
            if event.key == pygame.K_UP:
                velocidad_jugador -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                velocidad_jugador -= 7
            if event.key == pygame.K_UP:
                velocidad_jugador += 7

    # Hemos movido las funciones definidas al principio y las llamamos en el bucle
    animacion_bola()
    animacion_jugador()
    animacion_oponente()

    # Visuals / Dibujos *** Importante orden , se dibujan en orden por encima de los anteriores ***
    pantalla.fill(colorFondo)  # Añadimos color al fondo
    pygame.draw.rect(pantalla, colorGris, jugador)  # dibujo paleta jugador
    pygame.draw.rect(pantalla, colorGris, oponente)  # dibujo paleta oponente
    pygame.draw.ellipse(pantalla, colorGris, bola)  # Dibujo bola
    pygame.draw.aaline(pantalla, colorGris, (pantalla_ancho / 2, 0), (pantalla_ancho / 2, pantalla_alto))

    texto_jugador = Fuente_1.render(f"{Puntos_jugador}", False, colorGris)  # Escribe puntos jugador
    pantalla.blit(texto_jugador, (500, 340))  # Superficie para colocar el texto sobre la superficie anterior.

    #texto_oponente

    # Updating the Window
    pygame.display.flip()
    reloj.tick(60)  # Reloj para ejecutar el bucle = 60 veces por segundo
