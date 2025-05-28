# --- Class: FPS ---
# Purpose: Tracks and displays the current frames per second for performance monitoring
import pygame

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()  # Pygame clock to track time
        self.font = pygame.font.Font("assets/fonts/DTM-Mono.otf", 40)  # Font used for displaying FPS

    def draw(self, surface):
        # Render and draw the current FPS on the screen
        self.text = self.font.render(f"FPS: {str(round(self.clock.get_fps()))}", True, (255, 255, 255))
        surface.blit(self.text, (825, 0))