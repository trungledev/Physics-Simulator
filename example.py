import pygame
from pygame.math import Vector2

pygame.init()

# ================== CONFIG ==================
WIDTH, HEIGHT = 900, 600
FPS = 60
surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

RED = (255, 80, 80)
BLUE = (80, 150, 255)
BG = (30, 30, 30)

GRAVITY = 9.8
PPM = 100  # pixels per meter

# ================== BALL CLASS ==================
class Ball:
    def __init__(self, pos, vel, mass, radius, color):
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)
        self.mass = mass
        self.invMass = 0 if mass == 0 else 1 / mass
        self.radius = radius
        self.color = color

    def update(self, dt):
        self.vel.y += GRAVITY * dt
        self.pos += self.vel * dt * PPM

    def draw(self):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
        # velocity vector
        pygame.draw.line(surface, BLUE, self.pos,
                         self.pos + self.vel * 0.1, 2)

# ================== COLLISION ==================
def resolve_collision(a: Ball, b: Ball, restitution=0.9):
    n = b.pos - a.pos
    dist = n.length()
    if dist == 0:
        return

    penetration = a.radius + b.radius - dist
    if penetration <= 0:
        return

    # normal
    n.normalize_ip()

    # relative velocity
    rv = b.vel - a.vel
    vel_along_normal = rv.dot(n)

    if vel_along_normal > 0:
        return

    # impulse
    j = -(1 + restitution) * vel_along_normal
    j /= a.invMass + b.invMass

    impulse = j * n
    a.vel -= impulse * a.invMass
    b.vel += impulse * b.invMass

    # positional correction (anti-sink)
    correction = n * (penetration / (a.invMass + b.invMass)) * 0.8
    a.pos -= correction * a.invMass
    b.pos += correction * b.invMass

# ================== OBJECTS ==================
ball1 = Ball(
    pos=(200, 200),
    vel=(2, 0),        # ném ngang
    mass=1,
    radius=20,
    color=RED
)

ball2 = Ball(
    pos=(500, 300),
    vel=(-2, 0),
    mass=2,
    radius=25,
    color=(255, 255, 0)
)

GROUND_Y = HEIGHT - 50

# ================== MAIN LOOP ==================
running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- UPDATE ----------
    ball1.update(dt)
    ball2.update(dt)

    # ground collision
    for ball in (ball1, ball2):
        if ball.pos.y + ball.radius > GROUND_Y:
            ball.pos.y = GROUND_Y - ball.radius
            ball.vel.y *= -0.8

    # ball-ball collision
    resolve_collision(ball1, ball2)

    # ---------- RENDER ----------
    surface.fill(BG)
    pygame.draw.line(surface, (120, 120, 120),
                     (0, GROUND_Y), (WIDTH, GROUND_Y), 2)

    ball1.draw()
    ball2.draw()

    pygame.display.flip()

pygame.quit()
