import pygame
import time

class End:
    def __init__(self, surface, start_time):
        self.surface = surface
        self.start_time = start_time
        self.black_displayed = False
        self.image_displayed = False
        self.black_screen = pygame.Surface(surface.get_size())
        self.black_screen.fill((0, 0, 0))
        self.end_image = pygame.image.load("assets/images/end.png").convert_alpha()
        self.end_sound = pygame.mixer.Sound("assets/sounds/sound_effects/end.wav")
        self.sound = False
        self.activated = False

    def update(self):
        elapsed = time.time() - self.start_time

        if elapsed >= 127 and not self.activated:
            self.activated = True

        if elapsed >= 128 and not self.sound:
            pygame.mixer.Channel(2).play(self.end_sound)
            self.sound = True

        if 127 <= elapsed < 128:
            self.black_displayed = True
        elif elapsed >= 128:
            self.image_displayed = True

    def draw(self):
        if self.black_displayed:
            self.surface.blit(self.black_screen, (0, 0))
        if self.image_displayed:
            img_rect = self.end_image.get_rect(center=self.surface.get_rect().center)
            self.surface.blit(self.end_image, img_rect)
