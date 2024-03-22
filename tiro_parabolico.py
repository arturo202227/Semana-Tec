from random import randrange
from turtle import *
import pygame

from freegames import vector

# Inicializar Pygame y cargar el sonido de la bola y la pérdida
pygame.mixer.init()

"""Condiciones inciales"""
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Cargar sonidos
ball_sound = pygame.mixer.Sound('archivo5.wav')  # Cambia 'archivo5.wav' al nombre de tu archivo de sonido
impact_sound = pygame.mixer.Sound('archivo6.wav')  # Cambia 'archivo6.wav' al nombre de tu archivo de sonido


def tap(x, y):
    """Responde al tap de la pantalla"""
    global ball_sound

    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25
        ball_sound.play()  # Reproducir sonido de la bola


def inside(xy):
    """Devuelve Verdadero si xy está dentro de la pantalla."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Dibuja la pelota y los objetivos."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Mueve la bola y los objetos"""


    # Genera nuevos objetivos aleatorios
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Regresa los objetivos si se salen de la pantalla
    for target in targets:
        target.x -= 1  # +0.5 velocidad
        if not inside(target):
            target.x = 200

    # Mueve la bola si esta afuera de la pantalla
    if inside(ball):
        speed.y -= 0.5  # +0.15 velocidad
        ball.move(speed)

    # Quita los objetos impactados
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            impact_sound.play()  # Reproducir sonido de impacto

    # Dibuja la bola y los objetos
    draw()

    # Temporizador en milisegundos
    ontimer(move, 20)  # Validación más rápida


"""Setup de la pantalla"""
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
