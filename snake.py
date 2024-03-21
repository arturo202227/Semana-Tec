"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

"""Import libraries"""
from random import randrange
from turtle import *

from freegames import square, vector

"""Initial conditions"""
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
def move():
    """Move snake and food forward one segment."""
    global food  # Use global keyword to modify the food variable

    head = snake[-1].copy()
    head.move(aim)

    # Check if the snake hits the boundaries or collides with itself
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Check if the snake has eaten the food
    if head == food:
        print('Snake:', len(snake))
        # Generate new random coordinates for the food
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Move the food randomly
    direction = randrange(4)  # 0: right, 1: left, 2: up, 3: down
    if direction == 0:
        food.x += 10
    elif direction == 1:
        food.x -= 10
    elif direction == 2:
        food.y += 10
    else:
        food.y -= 10

    # Check if the food is inside the boundaries, adjust if necessary
    if not inside(food):
        if food.x < -200:
            food.x = -200
        elif food.x > 190:
            food.x = 190
        if food.y < -200:
            food.y = -200
        elif food.y > 190:
            food.y = 190

    # Check if the snake has eaten food and make it grow
    if head == food:
        print('Snake:', len(snake))
        # Add a new segment to the snake
        snake.append(snake[-1].copy())

    clear()

    # Draw the snake and the food
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    # Call the move() function again after 100 milliseconds
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