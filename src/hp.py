# --- Class: HP ---
# Purpose: Manages the player's HP, Karma reduction over time, game over state, and UI rendering
import time
import pygame
from assets import Assets

class HP:
    def __init__(self):
        pygame.init()

        self.assets = Assets()

        # Health and Karma values
        self.hp = 92
        self.max_hp = 92
        self.kr = 0  # Karma damage over time

        # Health bar display settings
        self.hp_color = (255, 254, 0)  # Yellow
        self.kr_color = (221, 0, 255)  # Purple
        self.no_hp_color = (255, 0, 0)  # Red (empty bar)

        self.hp_x = 425
        self.hp_y = 600
        self.hp_height = 30
        self.no_hp_width = 184
        self.rect_no_hp = pygame.Rect(self.hp_x, self.hp_y, self.no_hp_width, self.hp_height)

        # Font for HP text
        self.font = pygame.font.Font(self.assets.Mars_Needs_Cunnilingus, 35)

        # Sound effects
        self.sound_damage = pygame.mixer.Sound(self.assets.damage)
        self.sound_gameover = pygame.mixer.Sound(self.assets.GameOver_sound)

        # Game over image setup
        self.gameover = False
        self.gameover_image = pygame.image.load(self.assets.GameOver_image)
        self.width_gameover, self.height_gameover = self.gameover_image.get_size()
        self.x_gameover = (1000 - self.width_gameover) // 2
        self.y_gameover = (750 - self.height_gameover) // 2 - 100
        self.rect_gameover = pygame.Rect(self.x_gameover, self.y_gameover, self.width_gameover, self.height_gameover)
        self.gameover_alpha = 0  # Fade effect
        self.fade_speed = 3

        # Timing for karma and death sequence
        self.death_time = None
        self.kr_timer = time.time()

    def update(self):
        # Reduce HP over time if Karma (KR) is active
        if self.kr > 0 and self.hp > 0:
            current_time = time.time()
            if current_time - self.kr_timer >= max(0.01, 1.8 / self.kr):
                self.hp -= 1
                self.kr -= 1
                if self.kr > self.hp - 1:
                    self.kr = self.hp - 1
                self.kr_timer = current_time
                self.hp = max(0, self.hp)

        # Update rects based on current HP and KR
        self.hp_width = (self.hp - self.kr) * 2
        self.kr_width = self.hp * 2
        self.rect_hp = pygame.Rect(self.hp_x, self.hp_y, self.hp_width, self.hp_height)
        self.rect_kr = pygame.Rect(self.hp_x, self.hp_y, self.kr_width, self.hp_height)

        # Trigger gameover if HP reaches 0
        if self.hp <= 0 and self.death_time is None:
            self.death_time = time.time()

        if self.death_time is not None:
            # Play sound and fade in Game Over screen
            if time.time() - self.death_time >= 3 and not self.gameover:
                self.sound_gameover.play()
                self.gameover = True

            if self.gameover and self.gameover_alpha < 255:
                self.gameover_alpha += self.fade_speed
                self.gameover_alpha = min(255, self.gameover_alpha)

    def add_karma(self):
        # Increases Karma (KR) and plays damage sound
        if self.hp > 0:
            self.kr += 1
            self.sound_damage.play()
            if self.kr > self.hp - 1:
                self.kr = self.hp - 1

    def collision(self, collision):
        # Apply Karma on collision, reduce HP to 0 if only 1 left
        if collision:
            self.add_karma()
            if self.hp == 1:
                self.hp -= 1

    def draw(self, surface):
        # Draw health bars or Game Over screen based on HP
        if self.hp > 0:
            pygame.draw.rect(surface, self.no_hp_color, self.rect_no_hp)
            pygame.draw.rect(surface, self.kr_color, self.rect_kr)
            pygame.draw.rect(surface, self.hp_color, self.rect_hp)
            self.hp_value = self.font.render(f"{self.hp}/92", True, (255, 255, 255))
            surface.blit(self.hp_value, (700, 600))
        else:
            gameover_surf = self.gameover_image.convert_alpha()
            gameover_surf.set_alpha(self.gameover_alpha)
            surface.blit(gameover_surf, self.rect_gameover)
