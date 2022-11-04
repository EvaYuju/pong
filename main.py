import sys

import pygame

# General setup / configuración general
pygame.init()    # Inicializa los módulos pygame y es requerido para cualquier tipo de juego
clock = pygame.time.Clock()  # Método reloj

# Creación de ventana (Tamaño, titulo:
screen_width = 1080
screen_heigth = 660
screen = pygame.display.set_mode((screen_width, screen_heigth))   # display surface
pygame.display.set_caption('Pong')

# Rectángulos del juego (Game rectangles)
#        Pygame.Rect    (x,y,Width,heigth)
ball = pygame.Rect(screen_width/2 - 15, screen_heigth/2-15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_heigth/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_heigth/2 - 70, 10, 140)

# Variables colores objetos:
bg_color = pygame.Color('grey12')
ligh_grey = (200, 200, 200)

# Bucle :
while True:
    # Handling input
    for event in pygame.event.get():     # llamadas a todos los eventos de usuarios
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Cerrar el juego una vez termina
    # Visuals / Dibujos
    screen.fill(bg_color)   # Añadimos color al fondo
    pygame.draw.rect(screen, ligh_grey, player)     # dibujo paleta jugador
    pygame.draw.rect(screen, ligh_grey, opponent)   # dibujo paleta oponente
    pygame.draw.ellipse(screen, ligh_grey, ball)    # Dibujo bola
    pygame.draw.aaline(screen, ligh_grey, (screen_width/2, 0), (screen_width/2, screen_heigth))

    # Updating the Window
    pygame.display.flip()
    clock.tick(60)
