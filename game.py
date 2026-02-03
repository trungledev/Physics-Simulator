# Importing the library
import pygame
import numpy as np
# Initializing Pygame
(numpass,numfail)= pygame.init()
print('Number of modules initialized successfully:',
      numpass)
# checking the initialization
is_initialized = pygame.get_init()
 
# printing the result
print('Is pygame modules initialized:',
      is_initialized)
# Initializing surface
WIDTH, HEIGHT = 800,600
surface = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
# Initializing Color
color = (255,0,0)
radius = 50
pos_x = WIDTH / 2
pos_y = HEIGHT / 2
# Drawing Rectangle
running = True

font = pygame.font.SysFont("Arial" , 18 , bold = True)
# Source - https://stackoverflow.com/a/72505464
# Posted by R4GE J4X, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-03, License - CC BY-SA 4.0

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    surface.blit(fps_t,(0,0))

v = np.array([10,0])
isCollided = False
while running:
    clock.tick(60)
    fps_counter()
    pygame.display.update()
    for event in pygame.event.get():  
      if event.type == pygame.QUIT:  
        running = False
    if pos_y >= (HEIGHT - radius) or pos_y <= 0:
      isCollided = True
    if isCollided:
        v *= -1
        isCollided = False
    pos_y += 1 * v[0] 
    pos_x += 1 * v[1]
    surface.fill((30, 30, 30))
    pygame.draw.circle(surface, color,(pos_x,pos_y),radius)
pygame.display.flip()

