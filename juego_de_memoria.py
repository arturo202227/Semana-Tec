from random import shuffle
from turtle import *
import time

from freegames import path

# Cargar la imagen del carro
car = path('car.gif')

# Crear una lista de números para los cuadros
tiles = list(range(32)) * 2

# Estado del juego
state = {'marcas': []}  # Marcas de los cuadros destapados
oculto = [True] * 64  # Estado de ocultación de los cuadros
cont_tap = 0  # Contador de taps

# Función para dibujar un cuadro blanco en la posición dada
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

# Función para convertir coordenadas (x, y) en el índice de los cuadros
def indice(x, y):
    """Convertir coordenadas (x, y) a índice de los cuadros."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Función para convertir el índice de los cuadros en coordenadas (x, y)
def xy(indice):
    """Convertir índice de los cuadros a coordenadas (x, y)."""
    return (indice % 8) * 50 - 200, (indice // 8) * 50 - 200

# Función para manejar el evento de tocar un cuadro
def toque(x, y):
    """Actualizar las marcas y los cuadros ocultos según el toque."""
    global cont_tap  # Utilizar la variable global cont_tap
    cont_tap += 1  # Incrementar el contador de taps
    pos = indice(x, y)
    marcas = state['marcas']

    # Si el cuadro ya está destapado, ignorar el toque
    if pos in marcas:
        return

    # Agregar el cuadro destapado a la lista de marcas
    marcas.append(pos)

    # Si ya hay dos cuadros destapados
    if len(marcas) == 2:
        update()  # Actualizar para mostrar los números antes de iniciar el cronómetro
        ontimer(ocultar_numeros, 1000)  # Ocultar los números después de 1 segundo

    # Si ya hay más de dos cuadros destapados, eliminar el primer cuadro destapado de la lista
    if len(marcas) > 2:
        marcas.pop(0)

    update()  # Actualizar para mostrar el número en el cuadro antes de tocar otro

    # Si todos los cuadros han sido destapados
    if todos_destapados():
        print("¡Todos los cuadros han sido destapados!")
        # Aquí puedes agregar la lógica adicional que desees cuando se destapen todos los cuadros.

# Función para verificar si todos los cuadros están destapados
def todos_destapados():
    """Verificar si todos los cuadros están destapados."""
    return all(not oculto_cuadro for oculto_cuadro in oculto)

# Función para dibujar la imagen del carro y los cuadros
def dibujar():
    """Dibujar la imagen del carro y los cuadros."""
    global cont_tap  # Utilizar la variable global cont_tap
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Dibujar los cuadros
    for cont in range(64):
        if oculto[cont]:
            x, y = xy(cont)
            cuadro(x, y)

    # Mostrar los números en los cuadros destapados
    marcas = state['marcas']
    for marca in marcas:
        if oculto[marca]:
            x, y = xy(marca)
            up()
            # Centrar el dígito en el cuadro
            goto(x + 25, y + 10)
            color('black')
            write(tiles[marca], align='center', font=('Arial', 30, 'normal'))

    # Mostrar el número de taps en la pantalla
    up()  # Mover la tortuga sin dibujar
    goto(-190, 180)
    down()  # Volver a activar el dibujo
    write(f"Taps: {cont_tap}", font=('Arial', 16, 'normal'))

    update()
    ontimer(dibujar, 100)

# Función para ocultar los números después de 2 segundos
def ocultar_numeros():
    """Ocultar los números después de 2 segundos."""
    state['marcas'] = []  # Limpiar la lista de cuadros destapados
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
