import pygame
import time
from gasterblaster import GasterBlaster

class Attacks(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.bones = [
            pygame.image.load("assets/images/attacks/bones/big_bone.png"),
            pygame.image.load("assets/images/attacks/bones/bone_parkour.png"),
            pygame.image.load("assets/images/attacks/bones/cross_bone.png"),
            pygame.image.load("assets/images/attacks/bones/little_bone_jump.png"),
            pygame.image.load("assets/images/attacks/bones/little_bone.png"),
            pygame.image.load("assets/images/attacks/bones/long_medium_bone_jump.png"),
            pygame.image.load("assets/images/attacks/bones/medium_bone_jump.png"),
            pygame.image.load("assets/images/attacks/bones/medium_bone.png"),
            pygame.image.load("assets/images/attacks/bones/MEGA_bone.png"),
            pygame.image.load("assets/images/attacks/bones/semi-circle_bone.png"),
            pygame.image.load("assets/images/attacks/bones/small_hole_bone.png"),
            pygame.image.load("assets/images/attacks/bones/warning.png")
        ]

        self.gaster_blasters = [
            pygame.image.load("assets/images/attacks/gaster_blaster/gaster_blaster1.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/gaster_blaster2.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/gaster_blaster3.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/gaster_blaster4.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/gaster_blaster5.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/gaster_blaster6.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/small_gaster_blaster1.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/small_gaster_blaster2.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/small_gaster_blaster3.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/small_gaster_blaster4.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/small_gaster_blaster5.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/small_gaster_blaster6.png"),
            pygame.image.load("assets/images/attacks/gaster_blaster/beam1.png")
        ]

        self.active_gaster_blasters = []  # Liste des GasterBlasters en cours

        self.play_intro = True
        self.finished_intro = False

        # Compteurs de mouvement pour chaque bone
        self.bone_steps_intro = [0, 0, 0, 0]
        self.gaster_triggered_intro = [False, False, False, False, False]
        self.last_move_time = time.time()
        self.step_interval = 0.01  # temps entre chaque déplacement

        self.bone = self.bones[7]
        self.width_bone, self.height_bone = self.bone.get_size()
        self.x1_bone = 190
        self.x2_bone = 390
        self.x3_bone = 615
        self.x4_bone = 830
        self.y1_bone = 750
        self.y2_bone = 750
        self.y3_bone = 750
        self.y4_bone = 750
        self.rect_bone1 = pygame.Rect(self.x1_bone, self.y1_bone, self.width_bone, self.height_bone)
        self.rect_bone2 = pygame.Rect(self.x2_bone, self.y2_bone, self.width_bone, self.height_bone)
        self.rect_bone3 = pygame.Rect(self.x3_bone, self.y3_bone, self.width_bone, self.height_bone)
        self.rect_bone4 = pygame.Rect(self.x4_bone, self.y4_bone, self.width_bone, self.height_bone)

        self.gaster_blaster = self.gaster_blasters[0]

        self.width_gaster_blaster, self.height_gaster_blaster = self.gaster_blaster.get_size()

        self.collision = False

    '''def update(self, play_time):
        
        if round(time.time(), 1) == play_time + 12:
            self.button = self.buttons[1]
        elif round(time.time(), 1) == play_time + 14.5:
            self.button = self.buttons[2]
        elif round(time.time(), 1) == play_time + 17:
            self.button = self.buttons[3]
        elif round(time.time(), 1) == play_time + 19.5:
            self.button = self.buttons[4]

    def draw(self, surface):

        surface.blit(self.stats, (130, 600))
        surface.blit(self.kr_text, (630, 600))
        surface.blit(self.button, self.rect_button)'''
    
    def function_gaster_blaster(self, small, fake, x, y, start_x, start_y, angle, shoot):
        gb = GasterBlaster(small, fake, x, y, start_x, start_y, angle, shoot, self.gaster_blasters, pygame.display.get_surface())
        gb.debug = False
        self.active_gaster_blasters.append(gb)

    def update_gaster_blasters(self, player):
        for gb in self.active_gaster_blasters:
            gb.update(player)
        self.active_gaster_blasters = [gb for gb in self.active_gaster_blasters if not gb.done]

    def draw_gaster_blasters(self):
        for gb in self.active_gaster_blasters:
            gb.draw()

    
    def intro(self, play_time):
        if not self.play_intro:
            return

        current_time = time.time()
        elapsed = current_time - play_time

        # Durées après lesquelles chaque bone commence à bouger
        bone_start_times = [12.0, 14.5, 17.0, 19.5]

        for i in range(4):
            if elapsed >= bone_start_times[i] and self.bone_steps_intro[i] < 5:
                # Vérifie que le délai est écoulé depuis le dernier mouvement
                if current_time - self.last_move_time >= self.step_interval:
                    if i == 0:
                        self.y1_bone -= 20
                        self.rect_bone1 = pygame.Rect(self.x1_bone, self.y1_bone, self.width_bone, self.height_bone)
                    elif i == 1:
                        self.y2_bone -= 20
                        self.rect_bone2 = pygame.Rect(self.x2_bone, self.y2_bone, self.width_bone, self.height_bone)
                    elif i == 2:
                        self.y3_bone -= 20
                        self.rect_bone3 = pygame.Rect(self.x3_bone, self.y3_bone, self.width_bone, self.height_bone)
                    elif i == 3:
                        self.y4_bone -= 20
                        self.rect_bone4 = pygame.Rect(self.x4_bone, self.y4_bone, self.width_bone, self.height_bone)

                    self.bone_steps_intro[i] += 1
                    self.last_move_time = current_time

        # Déclenchement des Gaster Blasters à des temps précis
        gaster_times = [21.5, 22.0, 22.5, 23.0, 24.6]

        for i in range(5):
            if elapsed >= gaster_times[i] and not self.gaster_triggered_intro[i]:
                if i == 0:
                    self.function_gaster_blaster(False, False, 190, 200, 190, -200, -90, 1.5)
                    self.gaster_triggered_intro[i] = True
                elif i == 1:
                    self.function_gaster_blaster(False, False, 390, 200, 390, -200, -90, 1)
                    self.gaster_triggered_intro[i] = True
                elif i == 2:
                    self.function_gaster_blaster(False, False, 615, 200, 615, -200, -90, 0.5)
                    self.gaster_triggered_intro[i] = True
                elif i == 3:
                    self.function_gaster_blaster(False, False, 830, 200, 830, -200, -90, 0)
                    self.gaster_triggered_intro[i] = True
                elif i == 4:
                    self.finished_intro = True
                    self.gaster_triggered_intro[i] = True

    def draw_intro(self, surface):
        if self.finished_intro == False:
            surface.blit(self.bone, self.rect_bone1)
            surface.blit(self.bone, self.rect_bone2)
            surface.blit(self.bone, self.rect_bone3)
            surface.blit(self.bone, self.rect_bone4)