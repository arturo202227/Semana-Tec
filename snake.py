# Version final

from random import randrange
from turtle import *
import pygame

from freegames import square, vector

# Inicializar Pygame y cargar los sonidos
pygame.mixer.init()

"""Condiciones iniciales"""
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Colores aleatorios para la serpiente y la comida al inicio del juego
snake_color = (randrange(256) / 255, randrange(256) / 255, randrange(256) / 255)
food_color = (randrange(256) / 255, randrange(256) / 255, randrange(256) / 255)

# Sonidos
food_sound = pygame.mixer.Sound('archivo4.wav')  # Sonido de comida
fail_sound = pygame.mixer.Sound('archivo.wav')  # Sonido de fallo


def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Devolver Verdadero si la cabeza está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Mueve la serpiente y la comida hacia adelante un segmento."""
    global food, snake_color, food_color

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        fail_sound.play()  # Reproducir sonido de fallo
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        food_sound.play()  # Reproducir sonido de comida

    else:
        snake.pop(0)

    # Mueve la comida con un 10% de probabilidad en cada paso
    if randrange(10) == 0:
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    # Verifica que la comida se encuentre dentro de los parámetros y corrige si es necesario
    if not inside(food):
        if food.x < -200:
            food.x = -200
        elif food.x > 190:
            food.x = 190
        if food.y < -200:
            food.y = -200
        elif food.y > 190:
            food.y = 190

    # Verifica si la serpiente comió
    if head == food:
        print('Snake:', len(snake))
        snake.append(snake[-1].copy())  # Agrega una nueva sección a la serpiente

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)  # Usar el color de la serpiente

    square(food.x, food.y, 9, food_color)  # Usar el color de la comida
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
