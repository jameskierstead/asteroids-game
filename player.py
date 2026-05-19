import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape

# Step 2: Create Player class inheriting from CircleShape
class Player(CircleShape):
    
    # Step 3: The constructor
    def __init__(self, x, y):
        # 3.1 Call the parent class's constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # 3.2 Create the rotation attribute
        self.rotation = 0

    # Step 4: Paste the provided triangle method exactly as written
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Step 5: Override the draw method
    def draw(self, screen):
        # draw.polygon takes: surface, color, points list, line width
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # Step 6: add the rotate method
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # Step 7 & 8: Add the update method and hook up the keys
    def update(self, dt):
        keys = pygame.key.get_pressed()
   
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
