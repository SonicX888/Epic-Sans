# --- Class: Box ---
# Purpose: Represents the combat box area, including position and dynamic resizing during fight phases
import pygame
import time

class Box(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize box dimensions and position
        self.width = 300
        self.height = 300
        self.x = 345
        self.y = 275

    def update(self, play_time):
        # Update the box size and position based on elapsed fight time
        current_time = time.time()
        elapsed = current_time - play_time

        # Expand the box left/right during a specific fight phase
        if 31.5 <= elapsed < 33.5 and self.x > 45:
            self.width += 20
            self.x -= 10

        # Contract the box back to original position after another phase
        if 65 <= elapsed < 67 and self.x < 355:
            self.width -= 20
            self.x += 10

        if 86 <= elapsed < 88 and self.x > 45:
            self.width += 20
            self.x -= 10

        # Update the box and its hitbox (for collisions)
        self.box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hitbox = self.box.inflate(-70, -70)

    def draw(self, surface, hp):
        # Draw the white box outline if the player is still alive
        if hp > 0:
            pygame.draw.rect(surface, (255, 255, 255), self.box, 8)