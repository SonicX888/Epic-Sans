# --- Class: End ---
# Purpose: Manages the game's end sequence visuals and audio
import pygame
import time
from assets import Assets

class End:
    def __init__(self, surface, start_time):

        self.assets = Assets()

        self.surface = surface  # Surface to draw on (main game window)
        self.start_time = start_time  # Time the sequence began

        # Visual and sound states
        self.black_displayed = False  # Whether the screen is fully black
        self.image_displayed = False  # Whether the end image is shown

        # Preload end screen and audio
        self.black_screen = pygame.Surface(surface.get_size())
        self.black_screen.fill((0, 0, 0))  # Fill with black
        self.end_image = pygame.image.load(self.assets.end).convert_alpha()
        self.end_sound = pygame.mixer.Sound(self.assets.end_sound)

        self.sound = False  # Whether end sound has played
        self.activated = False  # Whether end state is active

    def update(self):
        # Handle timing of black screen and image reveal
        elapsed = time.time() - self.start_time

        if elapsed >= 127 and not self.activated:
            self.activated = True  # Begin end sequence

        if elapsed >= 128 and not self.sound:
            pygame.mixer.Channel(2).play(self.end_sound)
            self.sound = True  # Play end sound once

        # Visual display timing
        if 127 <= elapsed < 128:
            self.black_displayed = True
        elif elapsed >= 128:
            self.image_displayed = True

    def draw(self):
        # Draw appropriate visual layer depending on timing
        if self.black_displayed:
            self.surface.blit(self.black_screen, (0, 0))
        if self.image_displayed:
            img_rect = self.end_image.get_rect(center=self.surface.get_rect().center)
            self.surface.blit(self.end_image, img_rect)
