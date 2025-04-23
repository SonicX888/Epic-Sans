import pygame
import time

class Decorations(pygame.sprite.Sprite):
    def __init__(self):

        self.font = pygame.font.Font("assets/fonts/Mars_Needs_Cunnilingus.ttf", 35)
        self.stats = self.font.render("Chara LV 19 HP", True, (255, 255, 255))
        self.kr_text = self.font.render("KR", True, (255, 255, 255))

        self.buttons = [
            pygame.image.load("assets/images/buttons/buttons.png"),
            pygame.image.load("assets/images/buttons/buttons_broken1.png"),
            pygame.image.load("assets/images/buttons/buttons_broken2.png"),
            pygame.image.load("assets/images/buttons/buttons_broken3.png"),
            pygame.image.load("assets/images/buttons/buttons_broken4.png"),
            pygame.image.load("assets/images/buttons/buttons_gone1.png"),
            pygame.image.load("assets/images/buttons/buttons_gone2.png"),
            pygame.image.load("assets/images/buttons/buttons_gone3.png")
        ]
        self.button = self.buttons[0]
        self.width_button, self.height_button = self.button.get_size()
        self.x_button = 90
        self.y_button = 660
        self.rect_button = pygame.Rect(self.x_button, self.y_button, self.width_button, self.height_button)

    def update(self, play_time):
        
        if round(time.time(), 1) == play_time + 12:
            self.button = self.buttons[1]
        elif round(time.time(), 1) == play_time + 14.5:
            self.button = self.buttons[2]
        elif round(time.time(), 1) == play_time + 17:
            self.button = self.buttons[3]
        elif round(time.time(), 1) == play_time + 19.5:
            self.button = self.buttons[4]

    def draw(self, surface):

        surface.blit(self.stats, (130, 600))
        surface.blit(self.kr_text, (630, 600))
        surface.blit(self.button, self.rect_button)