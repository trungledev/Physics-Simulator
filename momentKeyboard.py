import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WASD Movement")
clock = pygame.time.Clock()

player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:  # Left
        player_x -= SPEED
    if keys[pygame.K_d]:  # Right
        player_x += SPEED
    if keys[pygame.K_w]:  # Up
        player_y -= SPEED
    if keys[pygame.K_s]:  # Down
        player_y += SPEED

    # Giữ nhân vật trong màn hình
    player_x = max(0, min(player_x, WIDTH - player_size))
    player_y = max(0, min(player_y, HEIGHT - player_size))

    screen.fill((30, 30, 30))
    pygame.draw.rect(
        screen,
        (0, 200, 255),
        (player_x, player_y, player_size, player_size),
    )

    pygame.display.flip()