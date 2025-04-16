from primitives2 import *

init_viewport()

def blade(x, y, length, width, angle, color, thickness):
    h = 10
    halfW = width/2
    bladeCorners=[[-halfW,h],[halfW,h],[halfW,h+length],[-halfW,h+length]]
    glPushMatrix()
    glTranslate(x,y,0)
    glRotatef(angle, 0,0,1)
    line2D(0,0,0, h, color, thickness)
    polygon2D(bladeCorners, color, thickness)
    glPopMatrix()

def blades(x, y, length, width, angle, color, thickness, nbOfBlades):
    alpha = 360 / nbOfBlades
    for i in range(nbOfBlades):
        blade(x, y, length, width, i*alpha + angle, color, thickness)

def tower(x, y, length, width, color, thickness):
    halfW = width/2
    halfL = length/2
    corners=[[-halfW,-halfL],[halfW,-halfL],[halfW,halfL],[-halfW,halfL]]
    glPushMatrix()
    glTranslate(x,y,0)
    polygon2D(corners, color, thickness)
    glPopMatrix()


iteration = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # WRITE YOUR CODE HERE
    w, l = 20,100
    # blade(50, 20, l, w, angle, color=(1, 1, 0, 1), thickness=5)
    blades(5, 40, l, w, iteration, color=(1, 1, 0, 1), thickness=5, nbOfBlades=3)
    tower(0, -60, 150, 80, color=(1, 1, 0, 1), thickness=3)

    iteration += 1

    pygame.display.flip()
    pygame.time.wait(10)

# Quit Pygame
pygame.quit()