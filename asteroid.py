import pygame
import random  # Step 3.2: Import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event  # Step 3.1: Import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    # The new split method!
    def split(self):
        # Step 1: Immediately kill the current asteroid
        self.kill()

        # Step 2: Check if it's already a small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Step 3.1: Log the split
        log_event("asteroid_split")

        # Step 3.2: Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Step 3.3 & 3.4: Create two new vectors rotated in opposite directions
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)

        # Step 3.5: Calculate the new, smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Step 3.6: Create the two new Asteroid objects
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Step 3.7 & 3.8: Set their velocities and scale them up by 1.2 to make them faster
        asteroid_1.velocity = new_vector_1 * 1.2
        asteroid_2.velocity = new_vector_2 * 1.2
