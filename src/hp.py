import pygame

class HP:
    def __init__(self):

        self.hp_color = (255, 254, 0)
        self.hp_x = 425
        self.hp_y = 600
        self.hp_width = 184
        self.hp_height = 30

        self.rect_hp = pygame.Rect(self.hp_x, self.hp_y, self.hp_width, self.hp_height)


    def draw(self, surface):

        pygame.draw.rect(surface, self.hp_color, self.rect_hp)
