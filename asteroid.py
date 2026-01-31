from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # Asteroid is too small to split
            return
        # Create 2 new smaller asteroids
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vector2 * 1.2
