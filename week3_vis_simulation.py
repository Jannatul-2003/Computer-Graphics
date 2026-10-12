import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


WIDTH = 960
HEIGHT = 540

RADIUS = 250
STEP = 3

THETA_MIN = 0
THETA_MAX = 180

THETAS = list(range(THETA_MIN, THETA_MAX + 1, STEP))

# theta -> normalized error (0..1)
norm_errors = {}



def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def dda(x0, y0, x1, y1):
    """Return the list of (x, y) pixels using DDA."""

    dx = x1 - x0
    dy = y1 - y0

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return [(x0, y0)]

    x_inc = dx / steps
    y_inc = dy / steps

    points = []

    x = float(x0)
    y = float(y0)

    for _ in range(steps + 1):

        points.append(
            (int(x + sign(x) * 0.5), int(y + sign(y) * 0.5) )
        )
        x += x_inc
        y += y_inc

    return points


def line_error(points, ex, ey):
    """
    Calculate the average perpendicular distance
    of DDA pixels from the true mathematical line.
    """

    length = math.hypot(ex, ey)

    total = sum(
        abs(px * ey - py * ex) / length
        for px, py in points
    )

    return total / len(points)



def build_lines():
    """
    Generate lines from THETA_MIN to THETA_MAX,
    calculate their DDA error, and normalize the error.
    """

    lines = []

    # First calculate all lines and their raw errors
    for theta in THETAS:

        rad = math.radians(theta)

        # Exact mathematical endpoint
        ex = RADIUS * math.cos(rad)
        ey = RADIUS * math.sin(rad)

        # Integer endpoint used by DDA
        x1 = round(ex)
        y1 = round(ey)

        points = dda(
            0,
            0,
            x1,
            y1
        )

        error = line_error(
            points,
            ex,
            ey
        )

        lines.append(
            (theta, points, error)
        )

    # Find maximum error
    max_error = max(
        error
        for _, _, error in lines
    ) or 1.0

    print(
        f"{'theta':>5}  "
        f"{'pixels':>6}  "
        f"{'avg error':>10}  "
        f"{'normalized':>11}"
    )

    print("-" * 42)

    # Normalize errors
    for theta, points, error in lines:

        normalized_error = error / max_error

        # Store normalized error for later use
        norm_errors[theta] = normalized_error

        print(
            f"{theta:>5}  "
            f"{len(points):>6}  "
            f"{error:>10.4f}  "
            f"{normalized_error:>11.3f}"
        )

    return lines

LINES = build_lines()



def init():
    """Initialize OpenGL projection and background."""

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
        WIDTH / 2,
        -HEIGHT / 2,
        HEIGHT / 2
    )

    # Model-view matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    """Draw all DDA lines using normalized error as brightness."""

    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(1)

    glBegin(GL_POINTS)

    for theta, points, error in LINES:

        # Get normalized error for this angle
        brightness = norm_errors[theta]

        # Black = low error
        # White = high error
        glColor3f(
            brightness,
            brightness,
            brightness
        )

        for x, y in points:

            # Center the point inside the pixel
            glVertex2f(
                x + 0.5,
                y + 0.5
            )

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
        b"Week 3 - DDA Error Fan"
    )


    glutDisplayFunc(display)

    init()

    glutMainLoop()


if __name__ == "__main__":
    main()
