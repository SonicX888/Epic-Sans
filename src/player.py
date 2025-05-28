# --- Class: Player ---
# Purpose: Manages player input, movement, gravity mechanics, collision detection, and soul rendering
import pygame
import time
from keys import Keys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Movement and visual properties
        self.speed = 5
        self.size = (30, 30)
        self.collision = False

        # Load soul images (red, blue, purple, broken)
        self.souls = [
            pygame.transform.scale(pygame.image.load("assets/images/soul/red.png"), self.size),
            pygame.transform.scale(pygame.image.load("assets/images/soul/blue.png"), self.size),
            pygame.transform.scale(pygame.image.load("assets/images/soul/purple.png"), self.size),
            pygame.transform.scale(pygame.image.load("assets/images/soul/broken_soul.png"), self.size)
        ]
        self.broken_sound = pygame.mixer.Sound("assets/sounds/sound_effects/broken.wav")
        self.soul_sound = pygame.mixer.Sound("assets/sounds/sound_effects/ping.wav")

        self.soul = self.souls[0]  # Default is red soul
        self.broken = self.souls[3]

        # Positioning
        self.width_soul, self.height_soul = self.soul.get_size()
        self.x_soul = (1000 - self.width_soul) // 2
        self.y_soul = 400
        self.rect_soul = pygame.Rect(self.x_soul, self.y_soul, self.width_soul, self.height_soul)

        # State flags
        self.gameover = False
        self.sound = False
        self.blue = False

        # Gravity system
        self.gravity_active = False
        self.gravity_orientation = 0  # 0=down, 90=right, 180=up, 270=left
        self.vertical_velocity = 0
        self.gravity_force = 0.5
        self.jump_strength = 15
        self.on_ground = False
        self.offset = 25

        # Jump mechanics
        self.jumping = False
        self.jump_start_pos = None
        self.max_jump_height = 175
        self.jump_key_held = False

        self.debug = False


    def apply_gravity(self, box, platform_rects=[]):
        # Applies gravity to the soul depending on orientation and platform collision
        direction = self.gravity_orientation
        self.vertical_velocity += self.gravity_force

        if self.jumping and self.jump_start_pos is not None:
            axis = self.rect_soul.centery if direction in [0, 180] else self.rect_soul.centerx
            if abs(axis - self.jump_start_pos) >= self.max_jump_height or not self.jump_key_held:
                self.jumping = False

        if not self.jumping:
            self.vertical_velocity = max(self.vertical_velocity, 0)

        moved = False

        # Handle gravity for each direction
        if direction == 0:  # Falling down
            future_rect = self.rect_soul.move(0, self.vertical_velocity)
            for plat in platform_rects:
                if future_rect.colliderect(plat) and self.vertical_velocity > 0:
                    self.rect_soul.bottom = plat.top
                    self.vertical_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                    moved = True
                    break
            if not moved:
                self.rect_soul.centery += self.vertical_velocity
                if self.rect_soul.bottom >= box.bottom + self.offset:
                    self.rect_soul.bottom = box.bottom + self.offset
                    self.vertical_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                else:
                    self.on_ground = False

        elif direction == 180:  # Falling up
            future_rect = self.rect_soul.move(0, -self.vertical_velocity)
            for plat in platform_rects:
                if future_rect.colliderect(plat) and self.vertical_velocity > 0:
                    self.rect_soul.top = plat.bottom
                    self.vertical_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                    moved = True
                    break
            if not moved:
                self.rect_soul.centery -= self.vertical_velocity
                if self.rect_soul.top <= box.top - self.offset:
                    self.rect_soul.top = box.top - self.offset
                    self.vertical_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                else:
                    self.on_ground = False

        elif direction == 90:  # Gravity pulls right
            future_rect = self.rect_soul.move(self.vertical_velocity, 0)
            for plat in platform_rects:
                if future_rect.colliderect(plat) and self.vertical_velocity > 0:
                    self.rect_soul.right = plat.left
                    self.vertical_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                    moved = True
                    break
            if not moved:
                self.rect_soul.centerx += self.vertical_velocity
                if self.rect_soul.right >= box.right + self.offset:
                    self.rect_soul.right = box.right + self.offset
                    self.vertical_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                else:
                    self.on_ground = False

        elif direction == 270:  # Gravity pulls left
            future_rect = self.rect_soul.move(-self.vertical_velocity, 0)
            for plat in platform_rects:
                if future_rect.colliderect(plat) and self.vertical_velocity > 0:
                    self.rect_soul.left = plat.right
                    self.vertical_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                    moved = True
                    break
            if not moved:
                self.rect_soul.centerx -= self.vertical_velocity
                if self.rect_soul.left <= box.left - self.offset:
                    self.rect_soul.left = box.left - self.offset
                    self.vertical_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                else:
                    self.on_ground = False


    def update(self, box, hp, play_time, stop, beam_rects=[], bonewall_rects=[], bone_rects=[], platform_rects=[], accessory_rects=[], blue_rects=[], orange_rects=[], timestop_rects=[], ball_rects=[]):
        # Main update method for handling input, soul state, collisions, and gameover
        current_time = time.time()
        elapsed = current_time - play_time

        if hp > 0:

            # Handle soul color/state and gravity direction transitions
            if 33.25 <= elapsed < 34.25 and not self.blue:
                self.soul = pygame.transform.rotate(self.souls[1], 90)
                self.gravity_orientation = 90
                self.soul_sound.play()
                self.blue = True

            if 36 <= elapsed < 36.75 and not self.sound:
                self.soul = pygame.transform.rotate(self.souls[1], -90)
                self.gravity_orientation = 270
                self.soul_sound.play()
                self.sound = True

            if 37.5 <= elapsed < 38.75 and self.blue:
                self.soul = pygame.transform.rotate(self.souls[0], 0)
                self.gravity_orientation = 0
                self.soul_sound.play()
                self.sound = False
                self.blue = False

            if 44 <= elapsed < 45 and not self.blue:
                self.soul = pygame.transform.rotate(self.souls[1], 0)
                self.gravity_orientation = 0
                self.soul_sound.play()
                self.blue = True

            if 53 <= elapsed < 54 and not self.sound:
                self.soul = pygame.transform.rotate(self.souls[1], 90)
                self.gravity_orientation = 90
                self.soul_sound.play()
                self.sound = True

            if 65.5 <= elapsed < 66 and self.blue:
                self.soul = pygame.transform.rotate(self.souls[0], 0)
                self.gravity_orientation = 0
                self.rect_soul.centerx = (1000 - self.width_soul) // 2
                self.soul_sound.play()
                self.sound = False
                self.blue = False
            
            if 86 <= elapsed < 87 and not self.blue:
                self.soul = pygame.transform.rotate(self.souls[1], 0)
                self.gravity_orientation = 0
                self.soul_sound.play()
                self.blue = True

            if 90 <= elapsed < 91 and self.blue:
                self.soul = pygame.transform.rotate(self.souls[0], 0)
                self.gravity_orientation = 0
                self.soul_sound.play()
                self.blue = False

            # Enable or disable gravity
            self.gravity_active = self.blue if hp > 0 else False

            if not stop:
                keys = Keys()

                if keys.e:
                    self.soul_sound.play()
                    self.debug = True
                elif keys.d:
                    self.soul_sound.play()
                    self.debug = False

                if self.gravity_active:
                    self.apply_gravity(box, platform_rects)


                    if self.gravity_orientation == 0:
                        if keys.left:
                            self.rect_soul.centerx -= self.speed
                            if not self.rect_soul.colliderect(box):
                                self.rect_soul.centerx += self.speed
                        if keys.right:
                            self.rect_soul.centerx += self.speed
                            if not self.rect_soul.colliderect(box):
                                self.rect_soul.centerx -= self.speed

                        if keys.up:
                            self.jump_key_held = True
                            if self.on_ground and not self.jumping:
                                self.jumping = True
                                self.jump_start_pos = self.rect_soul.centery
                                self.vertical_velocity = -self.jump_strength

                        else:
                            self.jump_key_held = False

                    elif self.gravity_orientation == 180:
                        if keys.left:
                            self.rect_soul.centerx -= self.speed
                            if not self.rect_soul.colliderect(box):
                                self.rect_soul.centerx += self.speed
                        if keys.right:
                            self.rect_soul.centerx += self.speed
                            if not self.rect_soul.colliderect(box):
                                self.rect_soul.centerx -= self.speed

                        if keys.down:
                            self.jump_key_held = True
                            if self.on_ground and not self.jumping:
                                self.jumping = True
                                self.jump_start_pos = self.rect_soul.centery
                                self.vertical_velocity = -self.jump_strength
                        else:
                            self.jump_key_held = False

                    elif self.gravity_orientation == 90:
                        if keys.down:
                            self.rect_soul.centery += self.speed
                            if not self.rect_soul.colliderect(box):
                                self.rect_soul.centery -= self.speed
                        if keys.up:
                            self.rect_soul.centery -= self.speed
                            if not self.rect_soul.colliderect(box):
                                self.rect_soul.centery += self.speed
                        if keys.left:
                            self.jump_key_held = True
                            if self.on_ground and not self.jumping:
                                self.jumping = True
                                self.jump_start_pos = self.rect_soul.centerx
                                self.vertical_velocity = -self.jump_strength
                        else:
                            self.jump_key_held = False

                    elif self.gravity_orientation == 270:
                        if keys.down:
                            self.rect_soul.centery += self.speed
                            if not self.rect_soul.colliderect(box):
                                self.rect_soul.centery -= self.speed
                        if keys.up:
                            self.rect_soul.centery -= self.speed
                            if not self.rect_soul.colliderect(box):
                                self.rect_soul.centery += self.speed
                        if keys.right:
                            self.jump_key_held = True
                            if self.on_ground and not self.jumping:
                                self.jumping = True
                                self.jump_start_pos = self.rect_soul.centerx
                                self.vertical_velocity = -self.jump_strength
                        else:
                            self.jump_key_held = False

                else:
                    if keys.up and self.rect_soul.colliderect(box):
                        self.rect_soul.centery -= self.speed
                        if not self.rect_soul.colliderect(box):
                            self.rect_soul.centery += self.speed
                    if keys.down and self.rect_soul.colliderect(box):
                        self.rect_soul.centery += self.speed
                        if not self.rect_soul.colliderect(box):
                            self.rect_soul.centery -= self.speed
                    if keys.left and self.rect_soul.colliderect(box):
                        self.rect_soul.centerx -= self.speed
                        if not self.rect_soul.colliderect(box):
                            self.rect_soul.centerx += self.speed
                    if keys.right and self.rect_soul.colliderect(box):
                        self.rect_soul.centerx += self.speed
                        if not self.rect_soul.colliderect(box):
                            self.rect_soul.centerx -= self.speed

            if self.debug == False:
                self.collision = False
                for beam_rect in beam_rects:
                    if beam_rect[0] > -200 and beam_rect[1] > -200:
                        if self.rect_soul.colliderect(beam_rect):
                            self.collision = True
                            break
                for bonewall_rect in bonewall_rects:
                    if self.rect_soul.colliderect(bonewall_rect):
                        self.collision = True
                        break
                for bone in bone_rects:
                    if self.rect_soul.colliderect(bone):
                        self.collision = True
                        break
                for accessory in accessory_rects:
                    if self.rect_soul.colliderect(accessory):
                        self.collision = True
                        break
                for blue in blue_rects:
                    if self.rect_soul.colliderect(blue) and (keys.up or keys.down or keys.left or keys.right):
                        self.collision = True
                        break
                for orange in orange_rects:
                    if self.rect_soul.colliderect(orange) and not (keys.up or keys.down or keys.left or keys.right):
                        self.collision = True
                        break

                for tsr in timestop_rects:
                    if self.rect_soul.colliderect(tsr):
                        self.collision = True
                        break

                for ball in ball_rects:
                    if self.rect_soul.colliderect(ball):
                        self.collision = True
                        break


        # Game over handling
        if hp <= 0 and not self.gameover:
            pygame.mixer.Channel(0).stop()
            self.broken_sound.play()
            self.gameover = True

    def draw(self, surface, hp):
        # Draw the soul or broken version depending on HP
        if hp > 0:
            surface.blit(self.soul, self.rect_soul)
        else:
            surface.blit(self.broken, self.rect_soul)