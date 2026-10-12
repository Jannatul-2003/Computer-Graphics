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

RADIUS = 250
STEP = 1

THETA_MIN = 0
THETA_MAX = 360

THETAS = list(range(THETA_MIN, THETA_MAX + 1, STEP))

# One color per zone
RED = (1.0, 0.0, 0.0)
GREEN = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)
YELLOW = (1.0, 1.0, 0.0)
CYAN = (0.0, 1.0, 1.0)
WHITE = (1.0, 1.0, 1.0)
MAGENTA = (1.0, 0.0, 1.0)
GREY = (0.5, 0.5, 0.5)


def drawline_0(x0, y0, x1, y1):
    
    glColor3f(*RED)

    dx = x1 - x0
    dy = y1 - y0

    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x = x0
    y = y0

    while x <= x1:

        glVertex2i(x, y)

        x += 1

        if d > 0:
            y += 1
            d += dNE
        else:
            d += dE



def drawline_1(x0, y0, x1, y1):

    glColor3f(*GREEN)

    dx = x1 - x0
    dy = y1 - y0

    d = dy - 2 * dx 
    dN = -2 * dx
    dNE = 2 * (dy - dx)
    x = x0
    y = y0

    while y <= y1:

        glVertex2i(x, y)

        y += 1

        if d > 0:
            d += dN
        else:
            x += 1
            d += dNE


def drawline_2(x0, y0, x1, y1):

    glColor3f(*BLUE)

    dx = x1 - x0
    dy = y1 - y0

    d = -2 * dx - dy
    dN = -2 * dx
    dNW = -2 * (dx + dy)
    x = x0
    y = y0

    while y <= y1:

        glVertex2i(x, y)

        y += 1

        if d > 0:
            x -= 1
            d += dNW
        else:
            d += dN


def drawline_3(x0, y0, x1, y1):

    glColor3f(*YELLOW)

    dx = x1 - x0
    dy = y1 - y0

    d = -2 * dy - dx
    dW = -2 * dy
    dNW = -2 * (dx + dy)
    x = x0
    y = y0

    while x >= x1:

        glVertex2i(x, y)

        x -= 1

        if d > 0:
            d += dW
        else:
            y += 1
            d += dNW


def drawline_4(x0, y0, x1, y1):

    glColor3f(*CYAN)

    dx = x1 - x0
    dy = y1 - y0

    d = dx - 2 * dy
    dW = -2 * dy
    dSW = 2 * (dx - dy) 
    x = x0
    y = y0

    while x >= x1:

        glVertex2i(x, y)

        x -= 1

        if d > 0:
            y -= 1
            d += dSW
        else:
            d += dW


def drawline_5(x0, y0, x1, y1):

    glColor3f(*WHITE)

    dx = x1 - x0
    dy = y1 - y0

    d = -dy + 2 * dx
    dS = 2 * dx
    dSW = 2 * (dx - dy)
    x = x0
    y = y0

    while y >= y1:

        glVertex2i(x, y)

        y -= 1

        if d > 0:
            d += dS
        else:
            x -= 1
            d += dSW


def drawline_6(x0, y0, x1, y1):

    glColor3f(*MAGENTA)

    dx = x1 - x0
    dy = y1 - y0

    d = 2 * dx + dy
    dS = 2 * dx
    dSE = 2 * (dx + dy)
    x = x0
    y = y0

    while y >= y1:

        glVertex2i(x, y)

        y -= 1

        if d > 0:
            x += 1
            d += dSE
        else:
            d += dS


def drawline_7(x0, y0, x1, y1):

    glColor3f(*GREY)

    dx = x1 - x0
    dy = y1 - y0

    d = 2 * dy + dx
    dE = 2 * dy
    dSE = 2 * (dx + dy)
    x = x0
    y = y0

    while x <= x1:

        glVertex2i(x, y)

        x += 1

        if d > 0:
            d += dE
        else:
            y -= 1
            d += dSE


def drawLine(x0, y0, x1, y1):

    dx = x1 - x0
    dy = y1 - y0

    if abs(dx) >= abs(dy):    # zone 0, 3, 4, 7

        if dx >= 0 and dy >= 0:
            drawline_0(x0, y0, x1, y1)
        elif dx >= 0 and dy < 0:
            drawline_7(x0, y0, x1, y1)
        elif dx < 0 and dy >= 0:
            drawline_3(x0, y0, x1, y1)
        else:
            drawline_4(x0, y0, x1, y1)

    else:                     # zone 1, 2, 5, 6

        if dx >= 0 and dy >= 0:
            drawline_1(x0, y0, x1, y1)
        elif dx < 0 and dy >= 0:
            drawline_2(x0, y0, x1, y1)
        elif dx < 0 and dy < 0:
            drawline_5(x0, y0, x1, y1)
        else:
            drawline_6(x0, y0, x1, y1)


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

    for theta in THETAS:

        rad = math.radians(theta)

        x1 = round(RADIUS * math.cos(rad))
        y1 = round(RADIUS * math.sin(rad))

        drawLine(0, 0, x1, y1)

    glEnd()

    glFlush()


def main():

    glutInit()

    glutInitDisplayMode(
        GLUT_RGB | GLUT_SINGLE
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
        b"Week 4 - Color Zone"
    )

    glutDisplayFunc(display)

    init()

    glutMainLoop()


if __name__ == "__main__":
    main()
