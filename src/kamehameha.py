import pygame
import time

class Kamehameha:
    def __init__(self, surface, image, y_position):
        self.surface = surface
        self.image = image
        self.y = y_position
        self.x = -100
        self.start_time = time.time()
        self.scale = 0.1
        self.alpha = 255
        self.phase = "grow"  # grow → oscillate → fade
        self.oscillate_time = 0
        self.done = False

    def update(self):
        now = time.time()
        elapsed = now - self.start_time

        if self.phase == "grow":
            self.scale += 1.6  # Rapid scale
            if self.scale >= 16:
                self.scale = 16
                self.phase = "oscillate"
                self.oscillate_start = now

        elif self.phase == "oscillate":
            self.oscillate_time = now - self.oscillate_start
            self.scale = 16 + 2 * abs(pygame.math.Vector2(1, 0).rotate(now * 360).x)
            if self.oscillate_time >= 5:
                self.phase = "fade"
                self.fade_start = now

        elif self.phase == "fade":
            fade_time = now - self.fade_start
            self.scale -= 1
            self.alpha = max(0, 255 - int(fade_time * 255 / 2))
            if self.alpha <= 0 or self.scale <= 0:
                self.done = True

    def draw(self):
        if self.done:
            return
        scaled = pygame.transform.scale(
            self.image,
            (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale))
        )
        scaled.set_alpha(self.alpha)
        self.rect = scaled.get_rect(midleft=(self.x, self.y))
        self.surface.blit(scaled, self.rect.topleft)

