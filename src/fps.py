import pygame

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font("assets/fonts/DTM-Mono.otf", 40)
        self.text = self.font.render(str(self.clock.get_fps()), True, (255, 255, 255))

    def render(self, display):
        self.text = self.font.render(f"FPS: {str(round(self.clock.get_fps(), 2))}", True, (255, 255, 255))
        display.blit(self.text, (750, 10))