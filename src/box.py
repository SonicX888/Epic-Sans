import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self):

        self.box = pygame.Rect(345, 275, 300, 300)
        self.hitbox = self.box.inflate(-70, -70)

    def draw(self, surface):

        pygame.draw.rect(surface, (255, 255, 255), self.box, 8)