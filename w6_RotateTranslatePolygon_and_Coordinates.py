from primitives2 import *

init_viewport()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # WRITE YOUR CODE HERE
    vertex = [[-40,-40], [40,-40], [40,40], [-40,40]]

    glPushMatrix()
    polygon2D(vertex,lineWidth=3)
    drawCoordinates(80,80)

    glRotatef(30, 0.0, 0.0, 1.0)
    polygon2D(vertex,color=(1,0,0,0),lineWidth=3)

    glTranslatef(100,0,0)
    polygon2D(vertex,color=(0,0,1,0),lineWidth=3)

    glScale(2,3,0)
    polygon2D(vertex,color=(0,1,0,0),lineWidth=3)
    drawCoordinates(80,80)

    # glScale(-1,1,0) # y ekenine göre 
    # polygon2D(vertex,color=(0,1,0,0),lineWidth=3)
    
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

# Quit Pygame
pygame.quit()