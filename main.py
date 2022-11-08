import random
import pygame
import sys

# Configuración general

pygame.mixer.pre_init(44100, -16, 2, 512)  # (freq 44100 x def., -16 x def., canal 2 x def., tamaño buffer lo reducimos)
pygame.font.init()  # Inicializa el módulo font para las fuentes
pygame.init()  # Inicializa los módulos pygame y es requerido para cualquier tipo de juego
reloj = pygame.time.Clock()  # Método reloj


# Función de movimiento de bola
def animacion_bola():
    # Variables globales
    global velocidad_bola_x, velocidad_bola_y, puntos_jugador, puntos_oponente, tiempoPuntaje

    # Movimiento bola
    bola.x += velocidad_bola_x
    bola.y += velocidad_bola_y

    # Detector de colisiones bola VS bordes
    # Si la bola es ≤ 0 y está el límite en los bordes
    if bola.top <= 0 or bola.bottom >= pantalla_alto:  # vertical
        pygame.mixer.Sound.play(sonido_pong)  # Que suene sonido
        velocidad_bola_y *= -1

    # Puntuación jugador
    if bola.left <= 0:
        pygame.mixer.Sound.play(sonido_aplausos)  # Ponemos sonido cuando marca punto el jugador
        puntos_jugador += 1
        tiempoPuntaje = pygame.time.get_ticks()  # Cuanto tiempo ha estado funcionando el juego desde el inicio

    # Puntuación oponente
    if bola.right >= pantalla_ancho:  # horizontal
        pygame.mixer.Sound.play(sonido_chof)  # Ponemos sonido cuando marca punto el oponente
        #  // Velocidad_bola_x *= -1
        #  Sustituimos la línea que invierte la velocidad de la bola por una que la resetea:
        puntos_oponente += 1
        tiempoPuntaje = pygame.time.get_ticks()

    # Detector de colisiones bola VS paletas
    if bola.colliderect(jugador) and velocidad_bola_x > 0:
        pygame.mixer.Sound.play(sonido_tenis)
        if abs(bola.right - jugador.left) < 10:
            velocidad_bola_x *= -1
        elif abs(bola.bottom - jugador.top) < 10 and velocidad_bola_y > 0:
            velocidad_bola_y *= -1
        elif abs(bola.top - jugador.bottom) < 10 and velocidad_bola_y < 0:
            velocidad_bola_y *= -1
    if bola.colliderect(oponente) and velocidad_bola_x < 0:
        pygame.mixer.Sound.play(sonido_tenis)
        if abs(bola.left - oponente.right) < 10:
            velocidad_bola_x *= -1
        elif abs(bola.bottom - oponente.top) < 10 and velocidad_bola_y > 0:
            velocidad_bola_y *= -1
        elif abs(bola.top - oponente.bottom) < 10 and velocidad_bola_y < 0:
            velocidad_bola_y *= -1


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
    global velocidad_bola_x, velocidad_bola_y, tiempoPuntaje

    hora_actual = pygame.time.get_ticks()
    bola.center = (pantalla_ancho / 2, pantalla_alto / 2)

    if hora_actual - tiempoPuntaje < 700:
        tres = miFuente.render("3", False, colorGris)
        pantalla.blit(tres, (pantalla_ancho / 2 - 5, pantalla_alto / 2 + 20))
    if 700 < hora_actual - tiempoPuntaje < 1400:
        dos = miFuente.render("2", False, colorGris)
        pantalla.blit(dos, (pantalla_ancho / 2 - 6, pantalla_alto / 2 + 20))
    if 1400 < hora_actual - tiempoPuntaje < 2100:
        uno = miFuente.render("1", False, colorGris)
        pantalla.blit(uno, (pantalla_ancho / 2 - 6, pantalla_alto / 2 + 20))

    if hora_actual - tiempoPuntaje < 2100:
        velocidad_bola_x, velocidad_bola_y = 0, 0
    else:
        velocidad_bola_y = 6 * random.choice((1, -1))
        velocidad_bola_x = 6 * random.choice((1, -1))
        # Aumento de velocidad al perder
        tiempoPuntaje = False  # En vez de None


# Creación de ventana (Tamaño, titulo):
pantalla_ancho = 960
pantalla_alto = 720

pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))  # display surface
pygame.display.set_caption('Pong')

# Rectángulos del juego:
#        Pygame.Rect    (x,y,ancho,alto)
bola = pygame.Rect(pantalla_ancho / 2 - 15, pantalla_alto / 2 - 15, 25, 25)
jugador = pygame.Rect(pantalla_ancho - 20, pantalla_alto / 2 - 70, 10, 100)
oponente = pygame.Rect(10, pantalla_alto / 2 - 70, 10, 100)

# Variables colores objetos:
colorFondo = pygame.Color('grey12')
colorGris = (200, 200, 200)

# Variables de movimiento objetos:
velocidad_bola_x = 6 * random.choice((1, -1))
velocidad_bola_y = 6 * random.choice((1, -1))
velocidad_jugador = 0
velocidad_oponente = 7

# Variables de texto:
puntos_jugador = 0
puntos_oponente = 0
#                                                (Nombre fuente, tamaño)
miFuente = pygame.font.Font("Materiales/Fuentes/Goldman-Regular.ttf", 32)
miTitulo = miFuente.render(" - Juego de Ping-Pong - ", 50, 0, colorGris)

# Sonidos
sonido_pong = pygame.mixer.Sound("Materiales/Sonidos/pong.ogg")
sonido_puntos = pygame.mixer.Sound("Materiales/Sonidos/score.ogg")
sonido_aplausos = pygame.mixer.Sound("Materiales/Sonidos/applause4.mp3")
sonido_tenis = pygame.mixer.Sound("Materiales/Sonidos/tennisserve.mp3")
sonido_chof = pygame.mixer.Sound("Materiales/Sonidos/hit-arg.mp3")

# Variables tiempoPuntaje:
tiempoPuntaje = False

# Bucle (donde ejecutaremos las funciones):
while True:
    # zona inputs
    for event in pygame.event.get():  # llamadas a todos los eventos de usuarios
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Cerrar el juego una vez termina
        if event.type == pygame.KEYDOWN:  # Eventos de teclado para manejar la paleta del jugador
            if event.key == pygame.K_DOWN:
                velocidad_jugador += 6
            if event.key == pygame.K_UP:
                velocidad_jugador -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                velocidad_jugador -= 6
            if event.key == pygame.K_UP:
                velocidad_jugador += 6

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
    pantalla.blit(miTitulo, (300, 9))

    if tiempoPuntaje:
        resetear_bola()

    texto_jugador = miFuente.render(f"{puntos_jugador}", False, colorGris)  # Escribe puntos jugador
    #                             ( variable a recoger, false/true, color )
    pantalla.blit(texto_jugador, (540, 55))  # Superficie para colocar el texto sobre la superficie anterior.
    texto_oponente = miFuente.render(f"{puntos_oponente}", False, colorGris)  # Escribe puntos oponente
    pantalla.blit(texto_oponente, (400, 55))  # Superficie para colocar el texto sobre la superficie anterior.

    # Updating the Window
    pygame.display.flip()
    reloj.tick(60)  # Reloj para ejecutar el bucle = 60 veces por segundo
