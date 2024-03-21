"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

"""Import libraries"""
from random import randrange
from turtle import *

from freegames import vector

"""Initial conditions"""
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Move ball and targets."""
    # Generate new random targets
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move all targets and wrap them to the opposite side if they go out of the screen
    for target in targets:
        target.x -= 1  # +0.5 speed

        # Wrap the target to the opposite side if it goes out of the screen
        if not inside(target):
            target.x = 200

    # Move the ball if it's inside the screen
    if inside(ball):
        speed.y -= 0.5  # +0.15 speed
        ball.move(speed)

    # Clear duplicates of targets that have been hit by the ball
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # Draw the targets and the ball
    draw()

    # Schedule the next move
    ontimer(move, 20)  # Faster validation

"""Screen setup"""
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()