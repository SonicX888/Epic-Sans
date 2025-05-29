# --- Class: Ball ---
# Purpose: Projectile attack entity that moves and despawns off-screen
import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("assets/images/attacks/others/ball.png"), (50, 50))  # Load and scale ball image
        self.rect = self.image.get_rect(center=(x, y))  # Positioning rectangle
        self.pos = (x, y)  # Position stored as float (for sub-pixel accuracy)
        self.direction = direction  # Movement direction in degrees
        self.speed = speed  # Movement speed

    def calculate_new_xy(self, old_xy, speed, angle_in_degrees):
        # Calculate new position using polar coordinates based on angle and speed
        move_vec = pygame.math.Vector2()
        move_vec.from_polar((speed, angle_in_degrees))
        return old_xy + move_vec

    def update(self, surface):
        # Update ball's position and remove it if it goes off-screen
        self.pos = self.calculate_new_xy(self.pos, self.speed, -self.direction)
        self.rect.center = round(self.pos[0]), round(self.pos[1])

        # Kill the ball if it's no longer within the visible surface
        if not surface.get_rect().colliderect(self.rect):
            self.kill()

    def draw(self, surface):
        # Render ball onto the given surface
        surface.blit(self.image, self.rect)
