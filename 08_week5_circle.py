import os
import sys

# glx only exists on Linux; Windows uses its default platform
if sys.platform.startswith("linux"):
    os.environ["PYOPENGL_PLATFORM"] = "glx"

import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


WIDTH = 960
HEIGHT = 540

r=100
x_c=0
y_c=0
dx=2
dy=-1

FRAME_MS = 16


def draw8way(x, y, x_c, y_c):

    glVertex2i(x_c + x, y_c + y)    # zone 0
    glVertex2i(x_c + y, y_c + x)    # zone 1
    glVertex2i(x_c - y, y_c + x)    # zone 2
    glVertex2i(x_c - x, y_c + y)    # zone 3
    glVertex2i(x_c - x, y_c - y)    # zone 4
    glVertex2i(x_c - y, y_c - x)    # zone 5
    glVertex2i(x_c + y, y_c - x)    # zone 6
    glVertex2i(x_c + x, y_c - y)    # zone 7


def drawCircle(r, x_c, y_c):

    # Midpoint circle in zone 0: from (r, 0) up to the line y = x
    d = 5 - 4*r
    x = r
    y = 0

    while y <= x:

        draw8way(x, y, x_c, y_c)

        dN = 8 * y + 12
        dNW = 8 * (y - x) + 20

        y += 1

        if d < 0:
            d += dN     #dN
        else:
            x -= 1
            d += dNW    #dNW


def animate(value):

    global x_c, y_c, dx, dy

    x_c += dx
    y_c += dy

    if x_c + r > (WIDTH / 2) - 1 or x_c - r < -(WIDTH / 2): #horizontal bounce
        dx *= -1

    if y_c + r > (HEIGHT / 2) - 1 or y_c - r < -(HEIGHT / 2): #vertical bounce
        dy *= -1

    glutPostRedisplay()

    glutTimerFunc(FRAME_MS, animate, 0)


def init():

    # Black background
    glClearColor(
        0.0,
        0.0,
        0.0,
        1.0
    )

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(
        -WIDTH / 2,
        (WIDTH / 2)-1,
        -HEIGHT / 2,
        (HEIGHT / 2)-1
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(1)

    glBegin(GL_POINTS)

    drawCircle(r, x_c, y_c)

    glEnd()

    glutSwapBuffers()


def main():

    glutInit()

    glutInitDisplayMode(
        GLUT_RGB | GLUT_DOUBLE
    )

    glutInitWindowSize(
        WIDTH,
        HEIGHT
    )

    glutInitWindowPosition(
        100,
        100
    )

    # Create OpenGL window
    glutCreateWindow(
        b"Week 5 - Bouncing Circle"
    )

    glutDisplayFunc(display)

    glutTimerFunc(FRAME_MS, animate, 0)

    init()

    glutMainLoop()


if __name__ == "__main__":
    main()
