# --- Class: GasterBlaster ---
# Purpose: Manages the behavior and rendering of Gaster Blasters, including animation, shooting, and visual effects.
import pygame
import math
import time

class GasterBlaster:
    def __init__(self, small, fake, x, y, start_x, start_y, angle, shoot_delay, assets, surface):
        self.surface = surface  # Display surface to draw onto
        self.small = small  # Flag indicating if it's a small Gaster Blaster

        # Assign animation frames based on size
        self.frames = assets[:6] if not small else assets[6:12]
        self.beam = assets[12]  # Beam sprite

        # Movement and position vectors
        self.start_pos = pygame.Vector2(start_x, start_y)
        self.target_pos = pygame.Vector2(x, y)
        self.position = pygame.Vector2(start_x, start_y)

        # Timing and animation
        self.start_time = time.time()
        self.duration_move = 1.0  # Time to move to target position
        self.current_angle = 0
        self.target_angle = angle

        # Load and play charge sound
        self.sound_charged = pygame.mixer.Sound("assets/sounds/sound_effects/charged.wav")
        self.sound_shoot = pygame.mixer.Sound("assets/sounds/sound_effects/shoot.wav")
        self.black_screen = pygame.mixer.Sound("assets/sounds/sound_effects/black.wav")
        pygame.mixer.Channel(1).play(self.sound_charged)

        # Flags to manage state
        self.ready = False
        self.fake = fake  # Fake Gaster Blasters show a black screen
        self.shoot_delay = shoot_delay
        self.shoot_timer_started = False
        self.shooting = False
        self.recoiling = False
        self.done = False

        # Animation control
        self.animation_index = 0
        self.animation_timer = time.time()
        self.animation_speed = 0.1
        self.charge_animation_done = False

        # Beam rendering
        self.beam_scale = 0
        self.beam_growing = True
        self.beam_alpha = 255
        self.beam_cache = {}

        # Recoil direction based on angle
        radians = math.radians(-self.target_angle)
        self.recoil_direction = pygame.Vector2(math.cos(radians), math.sin(radians))

        # Black screen effect timing
        self.black_screen_displayed = False
        self.black_screen_duration = 0.5
        self.black_screen_end_time = None
        self.black_screen_played = False
        self.black_screen_removed_sound_played = False

        self.animation_delay_started = False  # Indicates if the delay before the animation has started
        self.animation_start_time = None  # Timestamp of when the animation delay started

    def get_beam_image(self, scale):
        # Retrieve or create a scaled and rotated beam image
        key = (self.target_angle, round(scale, 2))
        if key not in self.beam_cache:
            raw_beam = pygame.transform.scale(
                self.beam, (int(self.beam.get_width() * 3), int(self.beam.get_height() * 3))
            )
            rotated = pygame.transform.rotate(raw_beam, self.target_angle)
            scaled = pygame.transform.scale(
                rotated,
                (int(rotated.get_width() * scale), int(rotated.get_height() * scale))
            )
            self.beam_cache[key] = scaled
        return self.beam_cache[key]

    def update(self, player):
        # Update Gaster Blaster state each frame
        now = time.time()

        if not self.ready:
            # Move into position
            t = min((now - self.start_time) / self.duration_move, 1)
            self.position = self.start_pos.lerp(self.target_pos, t)
            self.current_angle = (1 - t) * 720 + t * self.target_angle

            if t >= 1:
                self.ready = True
                self.ready_time = now
                if self.fake:
                    self.black_screen_start = now

        elif self.fake:
            # Handle fake Gaster Blaster black screen effect
            if not self.black_screen_displayed and now - self.black_screen_start >= 0.5:
                self.black_screen_displayed = True
                self.black_screen_end_time = now + self.black_screen_duration
                pygame.mixer.Channel(0).pause()
                self.black_screen.play()

            elif self.black_screen_displayed:
                if now >= self.black_screen_end_time:
                    if not self.black_screen_removed_sound_played:
                        self.black_screen.play()
                        pygame.mixer.Channel(0).unpause()
                        self.black_screen_removed_sound_played = True
                    self.done = True

        elif not self.shooting:
            # Delay before shooting animation
            if not self.animation_delay_started:
                self.animation_delay_started = True
                self.animation_start_time = now

            elif now - self.animation_start_time >= self.shoot_delay:
                # Animate charge-up before firing
                if not self.charge_animation_done:
                    if now - self.animation_timer > self.animation_speed:
                        self.animation_index += 1
                        if self.animation_index >= 4:
                            self.animation_index = 4
                            self.charge_animation_done = True
                            self.shoot_time = time.time()
                            self.sound_shoot.play()
                        self.animation_timer = now
                else:
                    self.shooting = True

        elif self.shooting and not self.recoiling:
            # Shooting logic with beam scaling
            elapsed = now - self.shoot_time
            if elapsed < 1.5:
                if elapsed >= 0.3:
                    # Grow/shrink beam depending on size and angle
                    if (not self.small and self.target_angle in (90, -90, 180, 0)) or (self.small and self.target_angle in (45, -45, 135, -135)):
                        if self.beam_growing:
                            self.beam_scale += 0.15
                            if self.beam_scale >= 2.8:
                                self.beam_growing = False
                        else:
                            self.beam_scale -= 0.06
                            if self.beam_scale <= 0:
                                self.beam_scale = 0
                    elif not self.small and self.target_angle in (45, -45, 135, -135):
                        if self.beam_growing:
                            self.beam_scale += 0.3
                            if self.beam_scale >= 5.6:
                                self.beam_growing = False
                        else:
                            self.beam_scale -= 0.12
                            if self.beam_scale <= 0:
                                self.beam_scale = 0
                    elif self.small and self.target_angle in (90, -90, 180, 0):
                        if self.beam_growing:
                            self.beam_scale += 0.075
                            if self.beam_scale >= 1.4:
                                self.beam_growing = False
                        else:
                            self.beam_scale -= 0.03
                            if self.beam_scale <= 0:
                                self.beam_scale = 0
                if elapsed >= 0.5:
                    self.recoiling = True
                    self.recoil_start = now
            else:
                self.done = True

        elif self.recoiling:
            # Recoil logic and fade out
            recoil_elapsed = now - self.recoil_start
            self.position += self.recoil_direction * 200 * recoil_elapsed * -1
            self.beam_alpha = max(0, 255 - int(recoil_elapsed * 510))

            if now - self.animation_timer > self.animation_speed:
                self.animation_index = (self.animation_index + 1) % 2 + 4
                self.animation_timer = now

            if recoil_elapsed > 1:
                self.done = True

    def draw(self):
        if self.done:
            return

        # Draw body
        frame = self.frames[min(self.animation_index, len(self.frames) - 1)]
        rotated_img = pygame.transform.rotate(frame, self.current_angle)
        self.gb_rect = rotated_img.get_rect(center=(self.position.x, self.position.y))
        self.surface.blit(rotated_img, self.gb_rect.topleft)

        # Draw beam if firing
        if self.shooting and not self.fake:
            beam_image = self.get_beam_image(self.beam_scale)
            beam_image.set_alpha(self.beam_alpha)
            radians = math.radians(self.target_angle)
            if self.target_angle in (0, 180):
                offset = pygame.Vector2(math.cos(radians), math.sin(radians)) * 75

            match self.target_angle:
                case 0:
                    self.beam_rect = beam_image.get_rect(midleft=(self.position.x + offset[0], self.position.y + offset[1]))
                case -45:
                    self.beam_rect = beam_image.get_rect(topleft=(self.position.x * 1.1, self.position.y * 1.1))
                case 45:
                    self.beam_rect = beam_image.get_rect(bottomleft=(self.position.x + 25, self.position.y + -25))
                case -90:
                    if self.small:
                        self.beam_rect = beam_image.get_rect(topleft=(self.position.x * 0.93, self.position.y * 1.2))
                    else:
                        self.beam_rect = beam_image.get_rect(topleft=(self.position.x - 30, self.position.y * 1.2))
                case 90:
                    if self.small:
                        self.beam_rect = beam_image.get_rect(bottomleft=(self.position.x * 0.93, self.position.y * 0.8))
                    else:
                        self.beam_rect = beam_image.get_rect(bottomleft=(self.position.x - 30, self.position.y * 0.8))
                case 135:
                    self.beam_rect = beam_image.get_rect(bottomright=(self.position.x * 0.9, self.position.y * 0.9))
                case -135:
                    self.beam_rect = beam_image.get_rect(topright=(self.position.x + -25, self.position.y + 25))
                case 180:
                    self.beam_rect = beam_image.get_rect(midright=(self.position.x + offset[0], self.position.y + offset[1]))

            self.surface.blit(beam_image, self.beam_rect.topleft)

        # Draw black screen overlay if fake
        if self.fake and self.black_screen_displayed and time.time() < self.black_screen_end_time:
            s = pygame.Surface(self.surface.get_size())
            s.fill((0, 0, 0))
            self.surface.blit(s, (0, 0))
