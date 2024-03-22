# Version final

import pygame
from turtle import *
from freegames import vector

# Inicializar el módulo de sonido de pygame
pygame.mixer.init()

# Cargar el archivo de sonido
sound = pygame.mixer.Sound("archivo7.wav")

# Función para reproducir el sonido
def play_sound():
    sound.play()

# Función para detener el sonido
def stop_sound():
    sound.stop()

# Dibujo de una línea. 
def line(start, end):
    play_sound()  # Reproducir el sonido
    up()                            
    goto(start.x, start.y)          
    down()                          
    goto(end.x, end.y)              
    stop_sound()                    # Detener el sonido al completar el dibujo.

# Dibujo de un cuadrado.
def square(start, end):
    play_sound()  # Reproducir el sonido
    up()                            
    goto(start.x, start.y)          
    down()                          
    begin_fill()                    
    for _ in range(4):              
        forward(end.x - start.x)    
        left(90)                    
    end_fill()
    stop_sound()                    # Detener el sonido al completar el dibujo.

# Dibujo un círculo.
def circulo(start, end):
    play_sound()  # Reproducir el sonido
    center = (start + end) / 2      
    radius = abs(end - start) / 2   
    up()                            
    goto(center.x, center.y - radius)
    down()                          
    begin_fill()                    
    circle(radius)                  
    end_fill()
    stop_sound()                    # Detener el sonido al completar el dibujo.

# Dibuja un retángulo.
def rectangle(start, end):
    play_sound()  # Reproducir el sonido
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
    stop_sound()                    # Detener el sonido al completar el dibujo.

# Dibuja un triángulo.
def triangle(start, end):
    play_sound()  # Reproducir el sonido
    up()                            
    goto(start.x, start.y)          
    down()                          
    begin_fill()                    
    vertex_y = start.y + 20         
    goto(end.x, start.y)            
    goto((start.x + end.x) / 2, vertex_y)  
    goto(start.x, start.y)          
    end_fill()
    stop_sound()                    # Detener el sonido al completar el dibujo.

# Maneja clicks del mouse.
def tap(x, y):
    start = state['start']          
    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']      
        end = vector(x, y)          
        shape(start, end)           
        state['start'] = None       

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
onkey(lambda: color('yellow'), 'Y')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()
