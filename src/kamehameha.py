# --- Class: Kamehameha ---
# Purpose: Giant energy beam with grow, oscillate, and fade phases
import pygame
import time

class Kamehameha:
    def __init__(self, surface, image, y_position):
        self.surface = surface  # Surface to draw on
        self.image = image  # Image of the beam
        self.y = y_position  # Vertical center of the beam
        self.x = -100  # Initial x offset (enters from left)
        self.start_time = time.time()

        # Beam visual effects
        self.scale = 0.1  # Initial scale for "grow" phase
        self.alpha = 255  # Beam transparency

        # Animation phases: grow → oscillate → fade
        self.phase = "grow"
        self.oscillate_time = 0  # Tracks oscillation duration
        self.done = False  # Whether the beam is finished

    def update(self):
        now = time.time()
        elapsed = now - self.start_time

        if self.phase == "grow":
            # Scale beam quickly during entry
            self.scale += 1.6
            if self.scale >= 16:
                self.scale = 16
                self.phase = "oscillate"
                self.oscillate_start = now

        elif self.phase == "oscillate":
            # Sway beam slightly to simulate power
            self.oscillate_time = now - self.oscillate_start
            self.scale = 16 + 2 * abs(pygame.math.Vector2(1, 0).rotate(now * 360).x)
            if self.oscillate_time >= 5:
                self.phase = "fade"
                self.fade_start = now

        elif self.phase == "fade":
            # Shrink and fade out
            fade_time = now - self.fade_start
            self.scale -= 1
            self.alpha = max(0, 255 - int(fade_time * 255 / 2))
            if self.alpha <= 0 or self.scale <= 0:
                self.done = True

    def draw(self):
        if self.done:
            return

        # Scale and draw beam image
        scaled = pygame.transform.scale(
            self.image,
            (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale))
        )
        scaled.set_alpha(self.alpha)
        self.rect = scaled.get_rect(midleft=(self.x, self.y))
        self.surface.blit(scaled, self.rect.topleft)
