# FUNCIONALIDADES QUE SE AÑADIERON.
# 1.- Agregar un color nuevo.
# 2.- Dibujar un círculo.
# 3.- Dibujar un rectángulo.
# 4.- Dibujar un triángulo.

#  Importación para dibujar gráficos y una clase de tipo "vector".
from turtle import *
from freegames import vector

# Dibujo de una línea. 
def line(start, end):
    up()                            # Levanta el lápiz para moverse sin dibujar.
    goto(start.x, start.y)          # Mueve el cursor a la coordenada inicial.
    down()                          # Baja el lápiz para comenzar a dibujar.
    goto(end.x, end.y)              # Dibuja una línea desde la coordenada inicial hasta la final.

# Dibujo de un cuadrado.
def square(start, end):
    up()                            # Levanta el lápiz para moverse sin dibujar.
    goto(start.x, start.y)          # Mueve el cursor a la coordenada inicial.
    down()                          # Baja el lápiz para comenzar a dibujar.
    begin_fill()                    # Comienza con el cuadrado.
    for _ in range(4):              # Repite cuatro veces para dibujar los cuatro lados del cuadrado.
        forward(end.x - start.x)    # Avanza la distancia entre el inicio y el final en la dirección actual (horizontal o vertical).
        left(90)                    # Gira 90 grados a la izquierda para dibujar el siguiente lado.
    end_fill()

# Círculo  // PENDIENTE.
# def circle(center, radius):

# Dibuja un retángulo.
def rectangle(start, end):
    up()                            # Levanta el lápiz para moverse sin dibujar.
    goto(start.x, start.y)          # Mueve el cursor a la coordenada inicial.
    down()                          # Baja el lápiz para comenzar a dibujar.
    begin_fill()                    # Comienza con el rectángulo.
    for _ in range(2):              # Repite dos veces para dibujar los dos lados largos del rectángulo.
        forward(end.x - start.x)    # Avanza la distancia entre el inicio y el final en la dirección actual (horizontal)
        left(90)                    # Gira 90 grados a la izquierda para dibujar el siguiente lado (ancho).
        forward(20)                 # Avanza una distancia fija para dibujar los lados cortos.
        left(90)                    # Gira 90 grados a la izquierda para dibujar el siguiente lado (largo).
    end_fill()


# Dibuja un triángulo.
def triangle(start, end):
    up()                            # Levanta el lápiz para moverse sin dibujar.
    goto(start.x, start.y)          # Mueve el cursor a la coordenada inicial.
    down()                          # Baja el lápiz para comenzar a dibujar.
    begin_fill()                    # Comienza a rellenar el triángulo.
    vertex_y = start.y + 20         # Calcula la coordenada y del vértice superior del triángulo.
    goto(end.x, start.y)            # Primer lado: desde el inicio hasta el extremo derecho.
    goto((start.x + end.x) / 2, vertex_y)  # Segundo lado: desde el extremo derecho hasta el vértice superior.
    goto(start.x, start.y)          # Tercer lado: desde el vértice superior hasta el inicio.
    end_fill()

# Maneja clicks del mouse.
def tap(x, y):
    start = state['start']          # Obtiene el punto de inicio actualmente almacenado en el estado.
    if start is None:
        state['start'] = vector(x, y)# Almacena el punto actual como el punto de inicio
    else:
        shape = state['shape']      # Si hay un punto de inicio almacenado, obtiene la forma que se va a dibujar.
        end = vector(x, y)          # Crea un vector con las coordenadas del punto actual.
        shape(start, end)           # Llama a la función correspondiente para dibujar la forma, pasando el punto de inicio y el punto actual.
        state['start'] = None       # Reinicia el punto de inicio para que se pueda dibujar una nueva forma.


# Guardar valor en una llave..
def store(key, value):
    state[key] = value

# Estado inicial.
state = {'start': None, 'shape': line}

# Definir pantalla de dibujo.
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# LLaves para definir color y figura. 
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

# Fin del programa.
done()
