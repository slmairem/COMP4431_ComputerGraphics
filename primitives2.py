import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin, pi


windowWidth, windowHeight = 960, 720
coordinateMinX, coordinateMaxX = -200, 200
coordinateMinY, coordinateMaxY = -200, 200
backgroundColor, drawingColor = (0,0,0,1), (1,1,0,0)
pointSize, drawingWidth = 1, 1
coordinateWidth, coordinateHeight = coordinateMaxX - coordinateMinX, coordinateMaxY - coordinateMinY

def point2D(x,y,color=drawingColor,pointSize=pointSize):
    glPointSize(pointSize)
    glColor(color)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def line2D(x0,y0,x1,y1,color=drawingColor,lineWidth=drawingWidth):
    glLineWidth(lineWidth)
    glColor(color)
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()

def polygon2D(vertices,color=drawingColor,lineWidth=drawingWidth):
    glLineWidth(lineWidth)
    glColor(color)
    glBegin(GL_LINE_LOOP)
    for i in range(len(vertices)):
        glVertex2f(vertices[i][0],vertices[i][1])
    glEnd()

def polygon2Dfilled(vertices,color=drawingColor,lineWidth=drawingWidth):
    glLineWidth(lineWidth)
    glColor(color)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(len(vertices)):
        glVertex2f(vertices[i][0],vertices[i][1])
    glEnd()

def circle2D(x0, y0, r, color, lineSize):
    currentX, currentY = x0 + r, y0
    for theta in range(361):
        nextX = x0 + r * cos(theta * pi / 180)
        nextY = y0 + r * sin(theta * pi / 180) * (windowWidth / windowHeight)
        line2D(currentX, currentY, nextX, nextY, color, lineSize)
        currentX, currentY = nextX, nextY

def arc2D(x0, y0, r, fromAngle, toAngle, color, lineSize):
    currentX, currentY = x0 + r, y0
    for theta in range(fromAngle, toAngle + 1):
        nextX = x0 + r * cos(theta * pi / 180)
        nextY = y0 + r * sin(theta * pi / 180) * (windowWidth / windowHeight)
        line2D(currentX, currentY, nextX, nextY, color, lineSize)
        currentX, currentY = nextX, nextY

def arc2Dfilled(x0, y0, r, fromAngle, toAngle, color, lineSize):
    currentX, currentY = x0 + r, y0
    for theta in range(fromAngle, toAngle + 1,10):
        nextX = x0 + r * cos(theta * pi / 180)
        nextY = y0 + r * sin(theta * pi / 180)
        polygon2Dfilled([[x0,y0],[currentX,currentY],[nextX,nextY]], color=color, lineWidth=lineSize)
        currentX, currentY = nextX, nextY

def filledTriangle2D(vertices,color=drawingColor):
    glColor(color)
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0],vertex[1])
    glEnd()

def filledColorfulTriangle2D(vertices):
    color = [[1,0,0,1],[0,1,0,1],[0,0,1,1]]
    glBegin(GL_TRIANGLES)
    for i in range(len(vertices)):
        glColor(color[i])
        glVertex2f(vertices[i][0],vertices[i][1])
    glEnd()

def triangleFan2D(vertices,color=drawingColor):
    glColor(color)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(len(vertices)):
        glVertex2f(vertices[i][0],vertices[i][1])
    glEnd()

def drawCoordinates(nbOfPointsX, nbOfPointsY, color=(0.7,0.7,0.7,1)):
    width = 2

    # x-axis
    line2D(coordinateMinX,0,coordinateMaxX,0,color,width)
    intervalLength = (coordinateMaxX - coordinateMinX) / nbOfPointsX
    verticalLinesLength = (coordinateMaxY - coordinateMinY) / 200
    for i in range(1,nbOfPointsX + 1):
        x = -i * intervalLength
        line2D(x, -verticalLinesLength, x, verticalLinesLength, color, width)
        x = i * intervalLength
        line2D(x, -verticalLinesLength, x, verticalLinesLength, color, width)


    # y-axis
    line2D(0,coordinateMinY, 0, coordinateMaxY, color, width)
    intervalLength = (coordinateMaxY - coordinateMinY) / nbOfPointsY
    horizontalLinesLength = (coordinateMaxY - coordinateMinY) / 200
    for i in range(1, nbOfPointsY + 1):
        y = -i * intervalLength
        line2D(-horizontalLinesLength, y, horizontalLinesLength, y, color, width)
        y = i * intervalLength
        line2D(-horizontalLinesLength, y, horizontalLinesLength, y, color, width)


def init_viewport():
    global windowWidth, windowHeight, drawing_color

    # Setting and Displaying the Screen
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight),
                                     DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("OpenGL in Python")

    glClearColor(backgroundColor[0], backgroundColor[1],
                 backgroundColor[2], backgroundColor[3])

    # Setting the Projection and Clipping
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(coordinateMinX, coordinateMaxX, coordinateMinY, coordinateMaxY)
    glMatrixMode(GL_MODELVIEW)

