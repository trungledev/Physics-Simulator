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
WHITE = (255,255,255)
YELLOW = (255, 255, 0)
GRAVITY = 9.8
GROUND_Y = HEIGHT - 50

# Initializing surface
surface = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

# Property of circle
radius = 20
pos_x = WIDTH / 3
pos_y = 100
pos = Vector2(pos_x,pos_y)
mass = 0.5 # kg
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
    v_scale = v * 5 # Scale 
    pos_x, pos_y = pos.x, pos.y
    force_x = pos_x + v_scale.x
    force_y = pos_y + v_scale.y
    pygame.draw.line(surface, YELLOW,(pos_x,pos_y),(force_x,force_y),2)

def acceleration(f,m):
    return f / m

p = Vector2(0,GRAVITY)
f =  Vector2(0,0)
g = 9.8
k = 1
restitution = 0.9   # hệ số đàn hồi (nảy)

velocity = Vector2(0,0)
invMass = 1/mass
PIXELS_PER_METER = 100
isCollided = False

running = True
while running:
    dt = clock.tick(FPS) / 1000 
    pygame.display.update()
    fps_counter()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:  # Quit
        running = False
    
    f = p 
    velocity += f * dt
    pos += velocity * dt * PIXELS_PER_METER
    
    # ---------- COLLISION WITH GROUND ----------
    if pos.y + radius > GROUND_Y:
        pos.y = GROUND_Y - radius
        velocity.y *= -restitution   # bật lên

        # chống rung
        if abs(velocity.y) < 1:
            velocity.y = 0
    
    surface.fill((30, 30, 30)) 
    pygame.draw.line(surface,WHITE,(0, GROUND_Y),(WIDTH, GROUND_Y))
    pygame.draw.circle(surface, RED, (pos.x, pos.y), radius)
    force_counter(pos, velocity)
    
pygame.display.flip()

