from primitives2 import *
from random import randint, random
from math import floor, cos, sin, pi


def DDA(x1, y1, x2, y2, color, width):
    dx, dy = x2 - x1, y2 - y1
    nbOfPixels = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    incX, incY = dx / nbOfPixels, dy / nbOfPixels
    x, y = x1, y1
    while nbOfPixels > 0:
        point2D(floor(x + 0.5), floor(y + 0.5), color, width)
        x, y = x + incX, y + incY
        nbOfPixels -= 1


def BresenhamLine(x1, y1, x2, y2, color, width):
    dx, dy = x2 - x1, y2 - y1
    d = 2 * dy - dx
    incE, incNE = 2 * dy, 2 * (dy - dx)
    x, y = x1, y1
    point2D(x, y, color, width)
    while x < x2:
        x += 1
        if d <= 0:
            d += incE
        else:
            d += incNE
            y += 1
        point2D(x, y, color, width)


def circle2DPoint(x0, y0, r, color, pointSize):
    for theta in range(360):
        x = x0 + r * cos(theta * pi / 180)
        y = y0 + r * sin(theta * pi / 180)
        point2D(x, y, color, pointSize)


def SymmetricPoints(x0, y0, x, y, color, pointSize):
    point2D(x0 + x, y0 + y, color, pointSize)
    point2D(x0 - x, y0 + y, color, pointSize)
    point2D(x0 + x, y0 - y, color, pointSize)
    point2D(x0 - x, y0 - y, color, pointSize)
    point2D(x0 + y, y0 + x, color, pointSize)
    point2D(x0 - y, y0 + x, color, pointSize)
    point2D(x0 + y, y0 - x, color, pointSize)
    point2D(x0 - y, y0 - x, color, pointSize)

def BresenhamCircle(x0, y0, r, color, pointSize):
    x, y, p = 0, r, 1 - r
    SymmetricPoints(x0, y0, x, y, color, pointSize)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        SymmetricPoints(x0, y0, x, y, color, pointSize)
