from primitives import *

def det(x1,y1,x2,y2,x,y):
    return (x2-x1)*(y-y1) - (y2-y1)*(x-x1)

def windingNumber(vertex,point):
    windNumber = 0
    x, y = point[0], point[1]
    n = len(vertex)
    for i in range(n):
        x1, y1 = vertex[i][0], vertex[i][1]
        x2, y2 = vertex[(i + 1) % n][0], \
            vertex[(i + 1) % n][1]
        if y1 <= y < y2:
            if det(x1,y1,x2,y2,x,y) > 0:
                windNumber += 1
        if y2 <= y < y1:
            if det(x1,y1,x2,y2,x,y) < 0:
                windNumber -= 1
    return not windNumber == 0

def rayCasting(vertx, point):
    counter = 0
    x, y = point[0], point[1]
    n = len(vertex)
    for i in range(n):
        x1, y1 = vertex[i][0], vertex[i][1]
        x2, y2 = vertex[(i + 1) % n][0], \
            vertex[(i + 1) % n][1]
        if min(y1,y2) < y < max(y1,y2):
            if x <= x1 + (y-y1)*(x2-x1)/(y2-y1):
                counter += 1

    return counter % 2 == 1

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

    # WRITE YOUR CODE BELOW

    vertex = [[5, 3], [10, 6], [12, 12], [8, 10], [2, 13]]
    point1, point2 = [6,7], [7,11]
    polygon2D(vertex)
    point2D(point1[0],point1[1],(0,1,0,1),pointSize=15)
    point2D(point2[0],point2[1],(1,0,0,1),pointSize=15)

    if (rayCasting(vertex,point2)):
        print("Point(",point2[0],",",point2[1],") is inside")
    else:
        print("Point(", point2[0], ",", point2[1], ") is outside")

    pygame.display.flip()
    pygame.time.wait(100)

    glFlush()

pygame.quit()