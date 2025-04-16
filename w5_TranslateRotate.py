from line_circle_drawing_algorithms import *

pygame.init()
init_viewport()

circles = []
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # WRITE YOUR CODE BELOW
    vertex = [[-30,-30], [30,-30], [30,30], [-30,30]]
    glPushMatrix()
    polygon2D(vertex,lineWidth=3)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(50,50,0)
    glRotatef(30.0,0.0,0.0,1.0)
    polygon2D(vertex, color=(0,1,0,1),lineWidth=3)
    glPopMatrix()
    

    pygame.display.flip()
    pygame.time.wait(100)

    glFlush()

pygame.quit()