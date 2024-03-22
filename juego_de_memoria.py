from random import shuffle
from turtle import *
import time
import pygame

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'marcas': []}
oculto = [True] * 64
cont_tap = 0

# Inicializar pygame y cargar los sonidos
pygame.mixer.init()
fail_sound = pygame.mixer.Sound('archivo.wav')
success_sound = pygame.mixer.Sound('archivo2.wav')

def cuadro(x, y):
    """Dibujar un cuadro blanco con contorno negro en la posición (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for cont in range(4):
        forward(50)
        left(90)
    end_fill()

def indice(x, y):
    """Convertir coordenadas (x, y) a índice de los cuadros."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(indice):
    """Convertir índice de los cuadros a coordenadas (x, y)."""
    return (indice % 8) * 50 - 200, (indice // 8) * 50 - 200

def toque(x, y):
    """Actualizar las marcas y los cuadros ocultos según el toque."""
    global cont_tap
    cont_tap += 1
    pos = indice(x, y)
    marcas = state['marcas']

    if pos in marcas:
        return

    marcas.append(pos)

    if len(marcas) == 2:
        update()
        ontimer(ocultar_numeros, 2000)
        if tiles[marcas[0]] != tiles[marcas[1]]:
            fail_sound.play()
        else:
            success_sound.play()

    if len(marcas) > 2:
        marcas.pop(0)

    update()

    if todos_destapados():
        print("¡Todos los cuadros han sido destapados!")

def todos_destapados():
    """Verificar si todos los cuadros están destapados."""
    return all(not oculto_cuadro for oculto_cuadro in oculto)

def dibujar():
    """Dibujar la imagen del carro y los cuadros."""
    global cont_tap
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for cont in range(64):
        if oculto[cont]:
            x, y = xy(cont)
            cuadro(x, y)

    marcas = state['marcas']
    for marca in marcas:
        if oculto[marca]:
            x, y = xy(marca)
            up()
            goto(x + 25, y + 10)
            color('black')
            write(tiles[marca], align='center', font=('Arial', 30, 'normal'))

    up()
    goto(-190, 180)
    down()
    write(f"Taps: {cont_tap}", font=('Arial', 16, 'normal'))

    update()
    ontimer(dibujar, 100)

def ocultar_numeros():
    """Ocultar los números después de 2 segundos."""
    state['marcas'] = []
    for cont in range(64):
        if not oculto[cont]:
            oculto[cont] = True
    update()

# Mezclar los números para los cuadros
shuffle(tiles)
# Configurar la ventana de Turtle
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
# Asignar la función de toque al evento de hacer clic en la pantalla
onscreenclick(toque)
# Dibujar la imagen del carro y los cuadros
dibujar()
# Mantener la ventana abierta
done()
