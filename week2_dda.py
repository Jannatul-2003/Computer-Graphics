import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


WIDTH = 960
HEIGHT = 540


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def DDA(x0, y0, x1, y1):

    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x0
    y = y0

    glBegin(GL_POINTS)

    for i in range(steps + 1):    
        px = int(x + sign(x) * 0.5)
        py = int(y + sign(y) * 0.5)    
        glVertex2i(px, py)
    
        x += x_inc
        y += y_inc

    glEnd()


def display():
    glPointSize(10.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    DDA(-5, 7, 6, -8)
    glFlush()


def init():

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-48.0, 47.0, -27.0, 26.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    window = glutCreateWindow(
        b"Computer Graphics Lab - Week 2 - DDA"
    )
    print("Window created:", window)
    if window == 0:
        print("ERROR: GLUT failed to create the window.")
        return

    init()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()