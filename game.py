# Importing the library
import pygame

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
surface = pygame.display.set_mode((400,300))

# Initializing Color
color = (255,0,0)

# Drawing Rectangle
running = True
while running:  
  
    pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.display.update()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False
pygame.display.flip()

