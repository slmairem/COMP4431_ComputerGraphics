from primitives import *
from random import randint, random
from math import floor

def DDA(x1,y1,x2,y2, color, width):
    dx, dy = x2-x1, y2-y1
    nbOfPixels = abs(dx) if abs(dx) > abs (dy) else abs(dy)
    incX = dx / nbOfPixels
    incY = dy / nbOfPixels
    x, y = x1, y1
    while nbOfPixels > 0:
        point2D (floor(x+0.5), floor(y+0.5), color, width)
        x, y = x + incX, y + incY
        nbOfPixels = nbOfPixels - 1

def Bresenham(x1,y1,x2,y2,color,width):
    dx, dy = x2-x1, y2-y1
    d = 2*dy - dx
    incE = 2 * dy
    incNE = 2 * (dy-dx)
    x, y = x1, y1
    point2D(x,y,color,width)
    while x < x2:
        x = x+1
        if d <= 0:
            d = d + incE
        else:
            d = d + incNE
            y = y + 1
        point2D(x,y,color,width)

pygame.init()

init_viewport()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #Setting the ModelView State
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # WRITE YOUR CODE HERE
    DDA(50,450,200,500, (0,0,1,0), 10)
    Bresenham(60,600,100,500, (1,0,0,0), 20)

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()