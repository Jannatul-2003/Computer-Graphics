import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WIDTH = 960
HEIGHT = 540


def draw_pixel(x, y):
    # glClear(GL_COLOR_BUFFER_BIT)
    # glColor3f(1.0, 0.0, 0.0)

    # Set drawing color to white
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def draw_nine_pixel():

    # Set drawing color to white
    # glColor3f(0.0, 0.0, 1.0)

    glBegin(GL_POINTS)
    for x in range(-1,2):
        for y in range(-1,2):
            glVertex2i(x,y)
    glEnd()

def display():
    # Clear the screen with black
    glPointSize(1.0)

    glClear(GL_COLOR_BUFFER_BIT)

    # # Set drawing color to white
    glColor3f(1.0, 1.0, 1.0)

    # Draw a pixel at (100, 50)
    draw_pixel(100, 50)

    draw_nine_pixel()

    glFlush()


def init():
    # Black background
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Set up 2D graph-paper coordinates
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(-480.0, 480.0,-270.0, 270.0,)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # One-pixel point

def main():
    # Initialize GLUT
    glutInit(sys.argv)

    # Single buffer + RGB color
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Create 960 × 540 window
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)

    # Create OpenGL window
    window = glutCreateWindow(b"Computer Graphics Lab - Week 1")

    print("Window created:", window)

    if window == 0:
        print("ERROR: GLUT failed to create the window.")
        return

    # OpenGL initialization must happen after the window is created
    init()

    # Register display callback
    glutDisplayFunc(display)


    # Start event loop
    glutMainLoop()


if __name__ == "__main__":
    main()