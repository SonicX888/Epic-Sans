# --- Class: Epic_sans ---
# Purpose: Handles Epic!Sans character rendering, animations, and orchestrates accessory effects during phase 3
import pygame
import math
import time
import random
from accessory import Accessory

class Epic_sans(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Animation tracking
        self.animation = 0
        self.x_head = 0
        self.y_head = 0
        self.angle_head = 0
        self.x_body = 0
        self.y_body = 0

        self.ball_pulse_scale = 1.75
        self.ball_pulse_direction = 1
        self.ball_alpha = 191

        # Accessory control
        self.accessory_instances = []
        self.accessory_stage = 0
        self.accessory_timer = 0
        self.Accessory = Accessory  # Reference to Accessory class

        # Helper to load multiple frame images
        def load_images(pattern, count):
            return [pygame.image.load(pattern.format(i)) for i in range(1, count + 1)]

        # Load assets for all Epic!Sans phases
        self.phase_1_head = load_images("assets/images/epic_sans/phase_1_head/head{}.png", 3)
        self.phase_1_body = load_images("assets/images/epic_sans/phase_1_body/body{}.png", 2)
        self.phase_1_legs = [pygame.image.load("assets/images/epic_sans/phase_1_legs/legs1.png")]

        self.phase_15_head = load_images("assets/images/epic_sans/phase_1.5_head/head{}.png", 2)

        self.phase_2_head = load_images("assets/images/epic_sans/phase_2_head/head{}.png", 2)
        self.phase_2_body = [pygame.image.load("assets/images/epic_sans/phase_2_body/body1.png")]
        self.phase_2_legs = [pygame.image.load("assets/images/epic_sans/phase_2_legs/legs1.png")]

        self.phase_25_head = load_images("assets/images/epic_sans/phase_2.5_head/head{}.png", 3)
        self.phase_25_body = [pygame.image.load("assets/images/epic_sans/phase_2.5_body/body1.png")]
        self.phase_25_legs = [pygame.image.load("assets/images/epic_sans/phase_2.5_legs/legs1.png")]

        self.phase_3_head = load_images("assets/images/epic_sans/phase_3_head/head{}.png", 5)
        self.phase_3_body = load_images("assets/images/epic_sans/phase_3_body/body{}.png", 18)
        self.phase_3_left_arm = load_images("assets/images/epic_sans/phase_3_left_arm/left_arm{}.png", 3)
        self.phase_3_right_arm = load_images("assets/images/epic_sans/phase_3_right_arm/right_arm{}.png", 2)
        self.phase_3_legs = load_images("assets/images/epic_sans/phase_3_legs/legs{}.png", 5)
        self.phase_3_animation = load_images("assets/images/epic_sans/phase_3_animation/animation{}.png", 8)

        # Load accessory sprite
        self.accessories = load_images("assets/images/epic_sans/accessories/accessory{}.png", 2)

        self.slices = load_images("assets/images/Slices/Slice{}.png", 6)

        # Initialize head/body/legs rects
        self._init_sprites()

        self.kamehameha = pygame.mixer.Sound("assets/sounds/sound_effects/kamehameha.wav")
        self.slash = pygame.mixer.Sound("assets/sounds/sound_effects/slash.wav")
        self.hit = pygame.mixer.Sound("assets/sounds/sound_effects/hit.wav")
        self.dust = pygame.mixer.Sound("assets/sounds/sound_effects/dust.wav")
        self.sound = False
        self.sound2 = False
        self.sound3 = False
        self.sound4 = False
        self.sound5 = False
        self.sound6 = False

        self.final_animation_active = False
        self.final_animation_start_time = None
        self.final_animation_index = 0
        self.final_animation_pos = (self.x_head, self.y_head)

        self.phase_115_active = False
        self.left_arm_image = self.phase_3_left_arm[2]
        self.right_arm_image = self.phase_3_right_arm[1]
        self.ball_image = self.accessories[1]

        self.left_arm_base_pos = (self.x_body + 10, self.y_body + -30)
        self.right_arm_base_pos = (self.x_body + 35, self.y_body + 30)
        self.ball_pos = (self.x_body + 25, self.y_body + 15)

        self.left_arm_rect = self.left_arm_image.get_rect(topleft=self.left_arm_base_pos)
        self.right_arm_rect = self.right_arm_image.get_rect(topleft=self.right_arm_base_pos)
        self.ball_rect = self.ball_image.get_rect(topleft=self.ball_pos)

        self.slice_animation_active = False
        self.slice_animation_start_time = None
        self.slice_index = 0
        self.slices_done = False

        self.alpha_fade_active = False
        self.fade_alpha = 255

        self.phase_3_body_index = 0
        self.phase_3_body_timer = time.time()

        self.slice_90_animation_active = False
        self.slice_90_animation_start_time = None
        self.slice_90_index = 0
        self.slice_90_done = False

    def _init_sprites(self):
        # Set initial positions and rectangles for parts
        self.head = self.phase_1_head[0]
        self.width_head, self.height_head = self.head.get_size()
        self.x_head = 440
        self.y_head = 30
        self.rect_head = pygame.Rect(self.x_head, self.y_head, self.width_head, self.height_head)

        self.body = self.phase_1_body[0]
        self.width_body, self.height_body = self.body.get_size()
        self.x_body = 430
        self.y_body = 80
        self.rect_body = pygame.Rect(self.x_body, self.y_body, self.width_body, self.height_body)

        self.legs = self.phase_1_legs[0]
        self.width_legs, self.height_legs = self.legs.get_size()
        self.x_legs = 430
        self.y_legs = 150
        self.rect_legs = pygame.Rect(self.x_legs, self.y_legs, self.width_legs, self.height_legs)

        self.left_hand = None
        self.x_left_hand = 400
        self.y_left_hand = 100
        self.rect_left_hand = pygame.Rect(self.x_left_hand, self.y_left_hand, *self.body.get_size())

        self.right_hand = None
        self.x_right_hand = 495
        self.y_right_hand = 100
        self.rect_right_hand = pygame.Rect(self.x_right_hand, self.y_right_hand, *self.body.get_size())

    def update(self, play_time, hp, stop):

        if hp > 0:
            # Update position for simple floating animation
            current_time = time.time() - play_time

            if 92 <= current_time < 93 and not self.slice_90_animation_active and not self.slice_90_done:
                self.slice_90_animation_active = True
                self.slice_90_animation_start_time = time.time()
                self.slice_90_index = 0

            if self.slice_90_animation_active:
                elapsed = time.time() - self.slice_90_animation_start_time
                self.slice_90_index = int(elapsed / 0.2)

                if self.slice_90_index >= len(self.slices):
                    self.slice_90_animation_active = False
                    self.slice_90_done = True

            if current_time >= 92 and not self.sound5:
                pygame.mixer.Channel(7).play(self.slash)
                self.sound5 = True

            if current_time >= 93 and not self.sound6:
                pygame.mixer.Channel(8).play(self.hit)
                self.sound6 = True

            self.animation += 0.05
            if not self.phase_115_active and current_time < 93:

                self.new_x_head = ((math.sin(self.animation * 1.5) * 2) + self.x_head)
                self.new_y_head = ((math.sin(self.animation * 3) * 4) + self.y_head)
                self.new_x_body = ((math.sin(self.animation * 1.5) * 2) + self.x_body)
                self.new_y_body = ((math.sin(self.animation * 3) * 3) + self.y_body)
                self.rect_head.x = self.new_x_head
                self.rect_head.y = self.new_y_head
                self.rect_body.x = self.new_x_body
                self.rect_body.y = self.new_y_body

            if not self.phase_115_active and 93 <= current_time < 115:

                self.new_x_head = ((math.sin(self.animation * 2) * 3) + self.x_head)
                self.new_y_head = ((math.sin(self.animation * 4) * 3) + self.y_head)
                self.new_x_body = ((math.sin(self.animation * 2) * 3) + self.x_body)
                self.new_y_body = ((math.sin(self.animation * 4) * 2) + self.y_body)
                self.new_x_left_hand = ((math.sin(self.animation * 2) * 3) + self.x_left_hand)
                self.new_y_left_hand = ((math.sin(self.animation * 4) * 2) + self.y_left_hand)
                self.new_x_right_hand = ((math.sin(self.animation * 2) * 3) + self.x_right_hand)
                self.new_y_right_hand = ((math.sin(self.animation * 4) * 2) + self.y_right_hand)
                self.rect_head.x = self.new_x_head - 5
                self.rect_head.y = self.new_y_head
                self.rect_body.x = self.new_x_body
                self.rect_body.y = self.new_y_body
                self.rect_left_hand.x = self.new_x_left_hand
                self.rect_left_hand.y = self.new_y_left_hand
                self.rect_right_hand.x = self.new_x_right_hand
                self.rect_right_hand.y = self.new_y_right_hand
                if time.time() - self.phase_3_body_timer > 0.1:
                    self.phase_3_body_index = (self.phase_3_body_index + 1) % 4
                    self.phase_3_body_timer = time.time()
                self.body = self.phase_3_body[self.phase_3_body_index]


            # Trigger accessory animations after specific time phases
            if current_time >= 66 and self.accessory_stage == 0:
                self.accessory_instances.append(self.Accessory(self.accessories[0], "oval", 200))
                self.accessory_stage = 1

            if self.accessory_stage == 1 and self.accessory_instances[-1].finished:
                self.accessory_instances.append(self.Accessory(self.accessories[0], "oval_low", 350))
                self.accessory_stage = 2

            if self.accessory_stage == 2 and self.accessory_instances[-1].finished:
                self.accessory_instances.append(self.Accessory(self.accessories[0], "oscillate", 50))
                self.accessory_stage = 3

            if 93 <= current_time < 115:
                self.head = self.phase_3_head[0]
                self.legs = self.phase_3_legs[0]
                self.left_hand = self.phase_3_left_arm[0]
                self.right_hand = self.phase_3_right_arm[0]

            if current_time >= 107 and not self.sound:
                pygame.mixer.Channel(6).play(self.kamehameha)
                self.sound = True

            if 107 <= current_time < 115 and not self.final_animation_active:
                self.final_animation_active = True
                self.final_animation_start_time = time.time()

            if self.final_animation_active:
                elapsed = time.time() - self.final_animation_start_time
                frame = int(elapsed / 0.1)
                if frame < len(self.phase_3_animation):
                    self.final_animation_index = frame
                else:
                    self.final_animation_index = len(self.phase_3_animation) - 1

            # Update active accessories
            for a in self.accessory_instances:
                a.update(hp, stop)

            if  115 <= current_time <= 120 and not self.phase_115_active:
                self.phase_115_active = True
                self.final_animation_active = False

                self.head = self.phase_3_head[3]
                self.body = self.phase_3_body[16]
                self.legs = self.phase_3_legs[3]

                self.rect_head = pygame.Rect(self.x_head+55, self.y_head+5, *self.head.get_size())
                self.rect_body = pygame.Rect(self.x_body+35, self.y_body+15, *self.body.get_size())
                self.rect_legs = pygame.Rect(self.x_legs, self.y_legs, *self.legs.get_size())

            if self.phase_115_active:
                self.left_arm_rect.topleft = (
                    self.left_arm_base_pos[0] + random.randint(-2, 2),
                    self.left_arm_base_pos[1] + random.randint(-2, 2)
                )
                self.right_arm_rect.topleft = (
                    self.right_arm_base_pos[0] + random.randint(-2, 2),
                    self.right_arm_base_pos[1] + random.randint(-2, 2)
                )
                self.ball_rect.topleft = (
                    self.ball_pos[0],
                    self.ball_pos[1]
                )

            if self.ball_pulse_direction == 1:
                self.ball_pulse_scale += 0.01
                if self.ball_pulse_scale >= 2:
                    self.ball_pulse_direction = -1
            else:
                self.ball_pulse_scale -= 0.01
                if self.ball_pulse_scale <= 1.5:
                    self.ball_pulse_direction = 1

            if self.ball_image:
                original_size = self.ball_image.get_size()
                new_size = (
                    int(original_size[0] * self.ball_pulse_scale),
                    int(original_size[1] * self.ball_pulse_scale)
                )
                self.scaled_ball = pygame.transform.smoothscale(self.ball_image, new_size)

                self.scaled_ball.set_alpha(self.ball_alpha)

                self.ball_x = self.ball_rect.centerx - new_size[0] // 2
                self.ball_y = self.ball_rect.centery - new_size[1] // 2
            
            if current_time >= 120 and not self.sound2:
                pygame.mixer.Channel(7).play(self.slash)
                self.sound2 = True

            if current_time >= 120 and not self.slice_animation_active and not self.slices_done:
                self.slice_animation_active = True
                self.slice_animation_start_time = time.time()
                self.slice_index = 0

            if self.slice_animation_active:
                elapsed = time.time() - self.slice_animation_start_time
                self.slice_index = int(elapsed / 0.2)

                if self.slice_index >= len(self.slices):
                    self.slice_animation_active = False
                    self.slices_done = True

            if current_time >= 121 and not self.sound3:
                pygame.mixer.Channel(8).play(self.hit)
                self.sound3 = True

            if current_time >= 121:
                self.left_arm_image = None
                self.right_arm_image = None
                self.ball_image = None
                self.head = self.phase_3_head[4]
                self.body = self.phase_3_body[17]
                self.legs = self.phase_3_legs[4]
                self.rect_head = pygame.Rect(self.x_head+10, self.y_head+10, *self.head.get_size())
                self.rect_body = pygame.Rect(self.x_body+10, self.y_body+10, *self.body.get_size())
                self.rect_legs = pygame.Rect(self.x_legs+10, self.y_legs+10, *self.legs.get_size())

            if current_time >= 123 and not self.sound4:
                pygame.mixer.Channel(9).play(self.dust)
                self.sound4 = True

            if current_time >= 123 and not self.alpha_fade_active:
                self.alpha_fade_active = True

            if self.alpha_fade_active and self.fade_alpha > 0:
                self.fade_alpha -= 5
                self.head.set_alpha(self.fade_alpha)
                self.body.set_alpha(self.fade_alpha)
                self.legs.set_alpha(self.fade_alpha)

    def draw(self, surface, hp):

        if hp > 0:
            if self.final_animation_active:
                image = self.phase_3_animation[self.final_animation_index]
                surface.blit(image, self.final_animation_pos)

            elif self.slice_animation_active:
                if self.slice_index < len(self.slices):
                    slice_image = self.slices[self.slice_index]
                    self.rect_body_pos = pygame.Rect(465, 95, self.width_body, self.height_body)
                    slice_rect = slice_image.get_rect(bottomleft=self.rect_body_pos.center)
                    surface.blit(slice_image, slice_rect)

            elif self.phase_115_active:
                surface.blit(self.legs, self.rect_legs)
                surface.blit(self.body, self.rect_body)
                surface.blit(self.head, self.rect_head)

                if self.left_arm_image:
                    surface.blit(self.left_arm_image, self.left_arm_rect)
                if self.right_arm_image:
                    surface.blit(self.right_arm_image, self.right_arm_rect)
                if self.ball_image:
                    surface.blit(self.scaled_ball, (self.ball_x, self.ball_y))

            elif self.slice_90_animation_active:
                if self.slice_90_index < len(self.slices):
                    slice_image = pygame.transform.rotate(self.slices[self.slice_90_index], 90)
                    slice_rect = slice_image.get_rect(center=(self.rect_head.centerx, self.rect_head.centery))
                    surface.blit(slice_image, slice_rect)

            else:
                for a in self.accessory_instances:
                    surface.blit(a.image, a.pos)
                surface.blit(self.legs, self.rect_legs)
                if self.right_hand:
                    surface.blit(self.right_hand, self.rect_right_hand)
                surface.blit(self.body, self.rect_body)
                surface.blit(self.head, self.rect_head)
                if self.left_hand:
                    surface.blit(self.left_hand, self.rect_left_hand)

