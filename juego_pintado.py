# FUNCIONALIDADES QUE SE AÑADIERON.
# 1.- Agregar un color nuevo.
# 2.- Dibujar un círculo.
# 3.- Dibujar un rectángulo.
# 4.- Dibujar un triángulo.

from turtle import *
from freegames import vector

# Línea.
def line(start, end):
    """Draw a line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Cuadrado
def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()

# Círculo.
def circle(start, end):
    radius = abs(end.x - start.x) / 2
    center_x = (start.x + end.x) / 2
    center_y = (start.y + end.y) / 2

    up()
    goto(center_x + radius, center_y)
    down()
    circle(radius)

# Rectángulo.
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(2):  
        forward(end.x - start.x)
        left(90)
        forward(20)  
        left(90)
    end_fill()

# Triángulo.
def triangle(start, end):
    """Draw a triangle with a fixed height of 4."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    vertex_y = start.y + 20
    goto(end.x, start.y)
    goto((start.x + end.x) / 2, vertex_y) 
    goto(start.x, start.y)
    end_fill()

# Function to handle mouse clicks for drawing shapes
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Function to store value in state at key
def store(key, value):
    """Store value in state at key."""
    state[key] = value

# Initial state
state = {'start': None, 'shape': line}

# Setup turtle window
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Key bindings
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y') # Color que se agrego : Amarillo.
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# Finish
done()
