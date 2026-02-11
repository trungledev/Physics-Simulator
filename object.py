from pygame.math import Vector2
class Object:
    # Force => Acceleration => Velocity => Position
    def __init__(self,force):
        self.force = force
        pass