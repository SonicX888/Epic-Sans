import time
import pygame

class HP:

    def __init__(self):
        pygame.init()

        self.hp = 92
        self.max_hp = 92
        self.kr = 0

        self.hp_color = (255, 254, 0)
        self.kr_color = (221, 0, 255)
        self.no_hp_color = (255, 0, 0)
        self.hp_x = 425
        self.hp_y = 600
        self.hp_height = 30
        self.no_hp_width = 184

        self.rect_no_hp = pygame.Rect(self.hp_x, self.hp_y, self.no_hp_width, self.hp_height)

        self.font = pygame.font.Font("assets/fonts/Mars_Needs_Cunnilingus.ttf", 35)

        self.kr_timer = time.time()

    def update(self):
        if self.kr > 0 and self.hp > 0:
            current_time = time.time()
            if current_time - self.kr_timer >= max(0.01, 1.8 / self.kr):
                self.hp -= 1
                self.kr -= 1
                if self.kr > self.hp - 1:
                    self.kr = self.hp - 1
                self.kr_timer = current_time
                self.hp = max(0, self.hp)

        # Met à jour les tailles des barres
        self.hp_width = (self.hp - self.kr) * 2
        self.kr_width = self.hp * 2
        self.rect_hp = pygame.Rect(self.hp_x, self.hp_y, self.hp_width, self.hp_height)
        self.rect_kr = pygame.Rect(self.hp_x, self.hp_y, self.kr_width, self.hp_height)

    def add_karma(self):
        self.kr += 1
        if self.kr > self.hp - 1:
            self.kr = self.hp - 1

    def collision(self, collision):
        if collision == True:
            self.add_karma()

    def draw(self, surface):
        
        pygame.draw.rect(surface, self.no_hp_color, self.rect_no_hp)
        pygame.draw.rect(surface, self.kr_color, self.rect_kr)
        pygame.draw.rect(surface, self.hp_color, self.rect_hp)

        self.hp_value = self.font.render(f"{self.hp}/92", True, (255, 255, 255))
        surface.blit(self.hp_value, (700, 600))