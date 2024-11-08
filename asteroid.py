import pygame
import random
import constants as C
from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x, y, radius, velocity=0):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= C.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - C.ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius, v1 * 1.2)
        Asteroid(self.position.x, self.position.y, new_radius, v2 * 1.2)