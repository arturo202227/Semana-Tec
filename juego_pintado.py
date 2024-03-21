from turtle import *
from freegames import vector

# Function to draw a line from start to end
def line(start, end):
    """Draw a line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Function to draw a square from start to end
def square(start, end):
    """Draw a square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()

# Function to draw a circle from start to end
def circle(start, end):
    """Draw a circle from start to end."""
    pass  # TODO

# Function to draw a rectangle from start to end
def rectangle(start, end):
    """Draw a rectangle from start to end."""
    pass  # TODO

# Function to draw a triangle from start to end
def triangle(start, end):
    """Draw a triangle from start to end."""
    pass  # TODO

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
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# Finish
done()
