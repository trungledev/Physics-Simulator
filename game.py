# Importing the library
import pygame
from pygame.math import Vector2
import math
# Initializing Pygame
(numpass,numfail)= pygame.init()
print('Number of modules initialized successfully:',
      numpass)
# checking the initialization
is_initialized = pygame.get_init()
 
# printing the result
print('Is pygame modules initialized:',
      is_initialized)
WIDTH, HEIGHT = 800,600
FPS = 60
BLUE = (0, 0, 255)
RED = (255,0,0)

GRAVITY = 9.8

# Initializing surface
surface = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

# Property of circle
radius = 20
pos_x = WIDTH / 2
pos_y = 100
m = 0.5 # kg
h = (600 - pos_y) /1000

font = pygame.font.SysFont("Arial" , 18 , bold = True)
# Source - https://stackoverflow.com/a/72505464
# Posted by R4GE J4X, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-03, License - CC BY-SA 4.0

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    surface.blit(fps_t,(0,0))

def force_counter(pos, v):
    pos_x, pos_y = pos
    v = v * 100 # scale
    force_x = pos_x + v.x
    force_y = pos_y + v.y
    pygame.draw.line(surface, BLUE,(pos_x,pos_y),(force_x,force_y),2)

def acceleration(f,m):
    return f / m

p = Vector2(0,m * GRAVITY)
f =  Vector2(10,0)
g = 9.8
k = 1
v0 = Vector2(0,0)
isCollided = False
e = 0.9 # Hệ số đàn hồi với đất
delta_t = 0.01
# phản lực sau va chạm  
def get_reaction_free_fall(h, m):
    f = Vector2(0,- (1-e)*m*math.sqrt(2*g*h)) / delta_t
    return f

running = True
while running:
    clock.tick(FPS)
    fps_counter()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:  # Quit
        running = False
    if pos_y - HEIGHT + radius > 1e-3:
        isCollided = True
    if isCollided:
        f_react = get_reaction_free_fall(h,m)  
        h *= e**2
        f = f_react
        isCollided = False
        
    dt = clock.tick(60) / 1000 
    if h > 1e-3:
        f += p * dt
    else:
        f = Vector2()
    a = acceleration(f,m)
    pos_y += 0.5 * a.y * dt ** 2 * 1000
    
    v = v0 + a * dt
    surface.fill((30, 30, 30))
    
    force_counter((pos_x,pos_y), v)
    pygame.draw.circle(surface, RED,(pos_x,pos_y), radius,1)
pygame.display.flip()

