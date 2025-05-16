import pygame
import time
import random
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
            pygame.image.load("assets/images/attacks/bones/warning.png"),
            pygame.image.load("assets/images/attacks/bones/bonewall.png")
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

        self.gaster_triggered_intro = [False, False, False, False, False, False, False, False, False, False]

        self.gaster_blaster = self.gaster_blasters[0]

        self.width_gaster_blaster, self.height_gaster_blaster = self.gaster_blaster.get_size()

        self.collision = False

        self.warning_sound = pygame.mixer.Sound("assets/sounds/sound_effects/notice.wav")

        self.warnings_active = False
        self.warnings_displayed = False
        self.bonewalls_started = False
        self.bonewalls_reversing = False
        self.bonewalls_ended = False

        # Position et rotation des warnings
        self.warnings = [
            {"pos": [395, 425], "angle": 90},
            {"pos": [495, 525], "angle": 180},
            {"pos": [595, 425], "angle": -90},
            {"pos": [495, 325], "angle": 0}
        ]

        # Position de départ et de fin des bonewalls
        self.bonewalls = [
            {"start": [295, 425], "end": [395, 425], "angle": 90, "current": [295, 425]},
            {"start": [495, 625], "end": [495, 525], "angle": 180, "current": [495, 625]},
            {"start": [695, 425], "end": [595, 425], "angle": -90, "current": [695, 425]},
            {"start": [495, 125], "end": [495, 325], "angle": 0, "current": [495, 125]}
        ]

    
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

    
    def attacks_order(self, play_time, hp):

        current_time = time.time()
        elapsed = current_time - play_time

        # Déclenchement des Gaster Blasters à des temps précis
        gaster_times = [21.5, 22.0, 22.5, 23.0, 24.6, 25, 26.25, 27.5, 28.75, 30]

        for i in range(10):
            if hp > 0:
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
                    elif i == 5:
                        self.function_gaster_blaster(False, False, 500, 200, 500, -200, -90, 0)
                        self.function_gaster_blaster(False, False, 275, 425, -125, 425, 0, 0)
                        self.gaster_triggered_intro[i] = True
                    elif i == 6:
                        self.function_gaster_blaster(False, False, 390, 200, 390, -300, -90, 0)
                        self.function_gaster_blaster(False, False, 275, 525, -225, 525, 0, 0)
                        self.function_gaster_blaster(False, False, 600, 650, 600, 1150, 90, 0)
                        self.function_gaster_blaster(False, False, 725, 325, 1225, 325, 180, 0)
                        self.gaster_triggered_intro[i] = True
                    elif i == 7:
                        x = random.randint(250, 750)
                        y = random.randint(188, 564)
                        self.function_gaster_blaster(False, False, x, y+75, x, y-500, -90, 0)
                        self.function_gaster_blaster(False, False, x, y-75, x, y+500, 90, 0)
                        self.function_gaster_blaster(False, False, x+75, y, x-500, y, 0, 0)
                        self.function_gaster_blaster(False, False, x-75, y, x+500, y, 180, 0)
                        self.gaster_triggered_intro[i] = True
                    elif i == 8:
                        x = random.randint(250, 750)
                        y = random.randint(188, 564)
                        self.function_gaster_blaster(False, False, x, y+75, x, y-500, -90, 0)
                        self.function_gaster_blaster(False, False, x, y-75, x, y+500, 90, 0)
                        self.function_gaster_blaster(False, False, x+75, y, x-500, y, 0, 0)
                        self.function_gaster_blaster(False, False, x-75, y, x+500, y, 180, 0)
                        self.gaster_triggered_intro[i] = True
                    elif i == 9:
                        x = random.randint(250, 750)
                        y = random.randint(188, 564)
                        self.function_gaster_blaster(False, False, x, y+75, x, y-500, -90, 0)
                        self.function_gaster_blaster(False, False, x, y-75, x, y+500, 90, 0)
                        self.function_gaster_blaster(False, False, x+75, y, x-500, y, 0, 0)
                        self.function_gaster_blaster(False, False, x-75, y, x+500, y, 180, 0)
                        self.gaster_triggered_intro[i] = True

        if 31.25 <= elapsed < 32.5 and self.warnings_active == False:
            self.warning_sound.play()

        # 30s : Affichage des warnings
        if 31.25 <= elapsed < 32.5:
            self.warnings_active = True
            self.warnings_displayed = True

        # 31s : Remplacement des warnings par des bonewalls
        if elapsed >= 32.5:
            self.warnings_active = False
            if self.warnings_displayed:
                self.bonewalls_started = True
                self.warnings_displayed = False

        self.update_bonewalls()

        if elapsed >= 33.75 and self.bonewalls_started and not self.bonewalls_ended:
            self.bonewalls_reversing = True


    def update_bonewalls(self):
        if not self.bonewalls_started or self.bonewalls_ended:
            return

        speed = 10  # pixels par frame

        all_at_target = True  # Pour vérifier si tous ont atteint la cible

        for bonewall in self.bonewalls:
            x, y = bonewall["current"]
            target = bonewall["start"] if self.bonewalls_reversing else bonewall["end"]
            x_target, y_target = target

            # Mouvement horizontal
            if x != x_target:
                x += speed if x < x_target else -speed
                if abs(x - x_target) < speed:
                    x = x_target
            # Mouvement vertical
            if y != y_target:
                y += speed if y < y_target else -speed
                if abs(y - y_target) < speed:
                    y = y_target

            bonewall["current"] = [x, y]

            if [x, y] != target:
                all_at_target = False

        if self.bonewalls_reversing and all_at_target:
            self.bonewalls_ended = True

    def get_bonewall_rects(self):
        bonewall_img = self.bones[12]
        bonewall_rects = []
        for b in self.bonewalls:
            rotated = pygame.transform.rotate(bonewall_img, -b["angle"])
            rect = rotated.get_rect(center=b["current"])
            bonewall_rects.append(rect)
        return bonewall_rects

    def draw(self, surface):

        # Affichage des warnings
        if self.warnings_active:
            warning_img = self.bones[11]
            for w in self.warnings:
                rotated = pygame.transform.rotate(warning_img, -w["angle"])
                rect = rotated.get_rect(center=w["pos"])
                surface.blit(rotated, rect)
        if not self.bonewalls_ended:
            # Affichage des bonewalls
            if self.bonewalls_started:
                bonewall_img = self.bones[12]
                for b in self.bonewalls:
                    rotated = pygame.transform.rotate(bonewall_img, -b["angle"])
                    rect = rotated.get_rect(center=b["current"])
                    surface.blit(rotated, rect)
