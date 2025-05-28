# --- Class: Decorations ---
# Purpose: Manages UI elements like the name label, KR label, and button animation during the intro
import pygame
import time

class Decorations(pygame.sprite.Sprite):
    def __init__(self):
        # Load button break sound effect
        self.heartbreaking_sound = pygame.mixer.Sound("assets/sounds/sound_effects/Heartbreaking.wav")

        # Track which button image is currently shown
        self.current_button_index = 0

        # Setup fonts for labels
        self.font = pygame.font.Font("assets/fonts/Mars_Needs_Cunnilingus.ttf", 35)
        self.stats = self._render_text("Chara LV 19 HP")
        self.kr_text = self._render_text("KR")

        # Load button images for animation
        self.buttons = self._load_buttons()
        self.button = self.buttons[0]

        # Position of the button display
        self.x_button = 90
        self.y_button = 660
        self.width_button, self.height_button = self.button.get_size()
        self.rect_button = pygame.Rect(self.x_button, self.y_button, self.width_button, self.height_button)

    def _render_text(self, text, color=(255, 255, 255)):
        # Render a text label with the given font and color
        return self.font.render(text, True, color)

    def _load_buttons(self):
        # Load all button animation frames
        button_paths = [
            "assets/images/buttons/buttons.png",
            "assets/images/buttons/buttons_broken1.png",
            "assets/images/buttons/buttons_broken2.png",
            "assets/images/buttons/buttons_broken3.png",
            "assets/images/buttons/buttons_broken4.png",
            "assets/images/buttons/buttons_gone1.png",
            "assets/images/buttons/buttons_gone2.png",
            "assets/images/buttons/buttons_gone3.png"
        ]
        return [pygame.image.load(path) for path in button_paths]

    def update(self, play_time):
        # Update button animation based on the elapsed time
        elapsed = time.time() - play_time
        new_index = 0

        # Time-based button change
        if elapsed >= 19.5:
            new_index = 4
        elif elapsed >= 17:
            new_index = 3
        elif elapsed >= 14.5:
            new_index = 2
        elif elapsed >= 12:
            new_index = 1

        # If the index changes, update and play sound
        if new_index != self.current_button_index:
            self.current_button_index = new_index
            self.button = self.buttons[new_index]
            self.heartbreaking_sound.play()

    def draw(self, surface, intro, hp):
        # Draw UI labels and button if intro has passed and player is alive
        if hp > 0:
            surface.blit(self.stats, (130, 600))
            surface.blit(self.kr_text, (630, 600))
        if not intro:
            surface.blit(self.button, self.rect_button)
