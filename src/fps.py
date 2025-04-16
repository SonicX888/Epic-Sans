import pygame

class FPS:
    
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font("assets/fonts/DTM-Mono.otf", 40)

    def draw(self, surface):
        self.text = self.font.render(f"FPS: {str(round(self.clock.get_fps()))}", True, (255, 255, 255))
        surface.blit(self.text, (825, 0))