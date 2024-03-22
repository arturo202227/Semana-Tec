# FUNCIONALIDADES QUE SE AÑADIERON.
# 1.- Contar y desplegar el número de taps.
# 2.- Detectar cuando todos los cuadros se han destapado.
# 3.- Centrar el dígito en el cuadro.
# 4.- Mejora extra.

from random import shuffle
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Variable para llevar el conteo de taps

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count  # Utilizar la variable global tap_count
    tap_count += 1  # Incrementar el contador de taps
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    global tap_count  # Utilizar la variable global tap_count
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        number = tiles[mark]
        # Ajusta manualmente las coordenadas para centrar el número
        if number < 10:
            goto(x + 15, y)
        else:
            goto(x + 5, y)  # Ajusta para números de dos dígitos
        color('black')
        write(number, font=('Arial', 30, 'normal'))

    # Mostrar el número de taps en la pantalla
    up()  # Mover la tortuga sin dibujar
    goto(-190, 180)
    down()  # Volver a activar el dibujo
    write(f"Taps: {tap_count}", font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)



shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
