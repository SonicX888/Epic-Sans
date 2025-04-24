import pygame
import time

class Decorations(pygame.sprite.Sprite):
    def __init__(self):

        self.heartbreaking_sound = pygame.mixer.Sound("assets/sounds/sound_effects/Heartbreaking.wav")
        self.current_button_index = 0  # pour suivre l'état actuel


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
        elapsed = time.time() - play_time
        new_index = 0  # par défaut aucun bouton

        if elapsed >= 19.5:
            new_index = 4
        elif elapsed >= 17:
            new_index = 3
        elif elapsed >= 14.5:
            new_index = 2
        elif elapsed >= 12:
            new_index = 1

        if new_index != self.current_button_index:
            self.current_button_index = new_index
            self.button = self.buttons[new_index]
            self.heartbreaking_sound.play()


    def draw(self, surface):

        surface.blit(self.stats, (130, 600))
        surface.blit(self.kr_text, (630, 600))
        surface.blit(self.button, self.rect_button)