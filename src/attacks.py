# --- Class: Attacks ---
# Purpose: Manages all attacks in the game, including bones, Gaster Blasters, and special bonewall sequences.
import pygame
import random
import time
from gasterblaster import GasterBlaster
from bones import Bones
from timestopmanager import TimeStopManager
from kamehameha import Kamehameha
from assets import Assets

class Attacks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.assets = Assets()

        # Load bone and platform images
        self.platforms = [pygame.image.load(self.assets.platform)]
        self.attacks = [
            pygame.image.load(self.assets.long_bone), #0
            pygame.image.load(self.assets.cross_bone), #1
            pygame.image.load(self.assets.little_bone), #2
            pygame.image.load(self.assets.long_medium_bone_jump), #3
            pygame.image.load(self.assets.medium_bone_jump), #4
            pygame.image.load(self.assets.medium_bone), #5
            pygame.transform.scale(pygame.transform.rotate(pygame.image.load(self.assets.MEGA_bone), 90), (1000, 1000)), #6
            pygame.image.load(self.assets.semi_circle_bone), #7
            pygame.image.load(self.assets.warning), #8
            pygame.image.load(self.assets.bonewall), #9
            pygame.image.load(self.assets.bottom_bone), #10
            pygame.image.load(self.assets.top_bone), #11
            pygame.image.load(self.assets.medium_blue_bone), #12
            pygame.image.load(self.assets.medium_orange_bone), #13
            pygame.image.load(self.assets.fist), #14
            pygame.image.load(self.assets.road_roller_image), #15
            pygame.image.load(self.assets.pillar) #16
        ]

        self.ora = pygame.mixer.Sound(self.assets.ORA)
        self.za_warudo = pygame.mixer.Sound(self.assets.za_warudo)
        self.resume = pygame.mixer.Sound(self.assets.resume)
        self.za_warudo_words = pygame.mixer.Sound(self.assets.za_warudo_words)
        pygame.mixer.set_num_channels(10)
        self.za_warudo_channel = pygame.mixer.Channel(5)


        # Load Gaster Blaster images
        self.gaster_blasters = [
            pygame.image.load(self.assets.gaster_blaster1),
            pygame.image.load(self.assets.gaster_blaster2),
            pygame.image.load(self.assets.gaster_blaster3),
            pygame.image.load(self.assets.gaster_blaster4),
            pygame.image.load(self.assets.gaster_blaster5),
            pygame.image.load(self.assets.gaster_blaster6),
            pygame.image.load(self.assets.small_gaster_blaster1),
            pygame.image.load(self.assets.small_gaster_blaster2),
            pygame.image.load(self.assets.small_gaster_blaster3),
            pygame.image.load(self.assets.small_gaster_blaster4),
            pygame.image.load(self.assets.small_gaster_blaster5),
            pygame.image.load(self.assets.small_gaster_blaster6),
            pygame.image.load(self.assets.beam1)
        ]

        # Active attack instances
        self.active_gaster_blasters = []
        self.moving_bones = []

        # Trigger flags for timeline-based attack activation
        self.triggered = [False] * 29

        # Utility
        self.gaster_blaster = self.gaster_blasters[0]
        self.width_gaster_blaster, self.height_gaster_blaster = self.gaster_blaster.get_size()
        self.collision =  ()

        # Warning system
        self.warning_sound = pygame.mixer.Sound(self.assets.notice)
        self.warnings_active = False
        self.warnings_displayed = False

        # Bonewall system flags
        self.bonewalls_started = False
        self.bonewalls_reversing = False
        self.bonewalls_ended = False
        self.bonewalls_exiting = False

        # Platform logic
        self.platform_enable = False

        # Warnings and bonewall data structures
        self.warnings = [
            {"pos": [405, 425], "angle": 90},
            {"pos": [495, 515], "angle": 180},
            {"pos": [585, 425], "angle": -90},
            {"pos": [495, 335], "angle": 0}
        ]

        self.bonewalls = [
            {"start": [245, 425], "end": [385, 425], "angle": 90, "current": [245, 425]},
            {"start": [495, 675], "end": [495, 535], "angle": 180, "current": [495, 675]},
            {"start": [745, 425], "end": [605, 425], "angle": -90, "current": [745, 425]},
            {"start": [495, 175], "end": [495, 315], "angle": 0, "current": [495, 175]}
        ]

        self.stop = False
        self.time_stop_manager = None
        self.time_stop_sound = False

        self.kamehameha = []

    def update_kamehameha(self):
        for beam in self.kamehameha:
            beam.update()
        self.kamehameha = [b for b in self.kamehameha if not b.done]

    def draw_kamehameha(self):
        for beam in self.kamehameha:
            beam.draw()

    def time_stop(self):
        self.time_stop_manager = TimeStopManager(self.attacks)

    def draw_time_stop(self, surface, hp):
        if self.time_stop_manager:
            self.time_stop_manager.update(Bones, hp)
            self.time_stop_manager.draw(surface, hp)
            if self.time_stop_manager.done:
                self.time_stop_manager = None

    
    def function_gaster_blaster(self, small, fake, x, y, start_x, start_y, angle, shoot):
        # Spawn a new Gaster Blaster with given parameters and append it to active list
        gb = GasterBlaster(small, fake, x, y, start_x, start_y, angle, shoot, self.gaster_blasters, pygame.display.get_surface())
        gb.debug = False
        self.active_gaster_blasters.append(gb)

    def update_gaster_blasters(self, player, hp):
        # Update all active Gaster Blasters and remove those marked done
        if hp > 0:
            for gb in self.active_gaster_blasters:
                gb.update(player)
            self.active_gaster_blasters = [gb for gb in self.active_gaster_blasters if not gb.done]

    def draw_gaster_blasters(self, hp):
        # Draw all active Gaster Blasters
        if hp > 0:
            for gb in self.active_gaster_blasters:
                gb.draw()

    def move(self, bone_images, start_x, start_y, end_x, end_y, speeds, delays, platform, blue, orange, reverse=False):
        # Spawn moving bone attacks using provided parameters
        start_time = time.time()
        for i in range(len(bone_images)):
            bone = Bones(
                bone_images[i],
                start_x[i], start_y[i],
                end_x[i], end_y[i],
                speeds[i],
                start_time + delays[i],  # delay each bone independently
                platform,
                blue,
                orange,
                reverse=reverse
            )
            self.moving_bones.append(bone)

    def update_bones(self, hp):
        # Update each bone and keep those that are not finished
        if hp > 0:
            updated_bones = []
            for bone in self.moving_bones:
                if not bone.update():
                    updated_bones.append(bone)
            self.moving_bones = updated_bones

    def draw_bones(self, surface, hp):
        # Draw all moving bones
        if hp > 0:
            for bone in self.moving_bones:
                bone.draw(surface)

    def attacks_order(self, play_time, hp, box_x, box_width, soulx, souly):

        # Trigger attacks based on elapsed time and current HP
        current_time = time.time()
        elapsed = current_time - play_time

        # Predefined timeline of event triggers
        times = [21.5, #0
                 22.0, #1
                 22.5, #2
                 23.0, #3
                 24.6, #4
                 25, #5
                 25.75, #6 
                 26.5, #7
                 27.25, #8
                 28, #9
                 31.25, #10 
                 33.5, #11
                 36, #12
                 37.5, #13
                 42, #14
                 44, #15
                 53, #16
                 66, #17
                 71, #18
                 73, #19
                 75, #20
                 79, #21
                 86, #22
                 90, #23
                 91, #24
                 92, #25
                 95, #26
                 98.5, #27
                 100] #28
        if hp > 0:
            for i in range(29):
                if hp > 0 and elapsed >= times[i] and not self.triggered[i]:
                    # Trigger each event only once when its time arrives
                    if i == 0:
                        self.function_gaster_blaster(False, False, 190, 200, 190, -200, -90, 1.5)
                    elif i == 1:
                        self.function_gaster_blaster(False, False, 390, 200, 390, -200, -90, 1)
                    elif i == 2:
                        self.function_gaster_blaster(False, False, 615, 200, 615, -200, -90, 0.5)
                    elif i == 3:
                        self.function_gaster_blaster(False, False, 830, 200, 830, -200, -90, 0)
                    elif i == 4:
                        self.finished_intro = True
                    elif i == 5:
                        self.function_gaster_blaster(False, False, 500, 200, 500, -200, -90, 0)
                        self.function_gaster_blaster(False, False, 275, 425, -125, 425, 0, 0)
                    elif i == 6:
                        self.function_gaster_blaster(False, False, 390, 200, 390, -300, -90, 0)
                        self.function_gaster_blaster(False, False, 275, 525, -225, 525, 0, 0)
                        self.function_gaster_blaster(False, False, 600, 650, 600, 1150, 90, 0)
                        self.function_gaster_blaster(False, False, 725, 325, 1225, 325, 180, 0)
                    elif i in (7, 8, 9):
                        # Randomized 4-directional blaster bursts
                        x = random.randint(250, 750)
                        y = random.randint(188, 564)
                        self.function_gaster_blaster(False, False, x, y+75, x, y-500, -90, 0)
                        self.function_gaster_blaster(False, False, x, y-75, x, y+500, 90, 0)
                        self.function_gaster_blaster(False, False, x+75, y, x-500, y, 0, 0)
                        self.function_gaster_blaster(False, False, x-75, y, x+500, y, 180, 0)
                    elif i == 10:
                        self.function_gaster_blaster(False, False, 500, 200, 500, -200, -90, 0)
                    elif i == 11:
                        self.function_gaster_blaster(False, False, 275, 425, -125, 425, 0, 0)
                    elif i == 12:
                        # Move bonewalls horizontally
                        self.move([self.attacks[9]], [-100], [315], [1250], [315], [10], [0], False, False, False, False)
                        self.move([self.attacks[9]], [-100], [525], [1250], [525], [10], [0], False, False, False, False)
                    elif i == 13:
                        for j in range(0, 825, 75):
                            self.function_gaster_blaster(False, False, 90+j, 200, 90+j, -200, -90, 2)
                    elif i == 14:
                        # Fake Gaster Blasters in all directions
                        for k in range(19):
                            x, y = random.randint(0, 1000), random.randint(0, 750)
                            o = random.randint(0, 7)
                            angles = [0, 90, 180, -90, 45, -45, 135, -135]
                            dx = [x-1000, x, x+1000, x, x-1000, x-1000, x+1000, x+1000]
                            dy = [y, y+1000, y, y-1000, y+1000, y-1000, y+1000, y-1000]
                            self.function_gaster_blaster(False, True, x, y, dx[o], dy[o], angles[o], 1)
                    elif i == 15:
                        # Cross attacks from all sides
                        for l in range(17):
                            self.move([self.attacks[5]], [1000], [350], [-50], [350], [20], [l/2], False, False, False, False)
                            self.move([self.attacks[5]], [1000], [650], [-50], [650], [20], [l/2], False, False, False, False)
                            self.move([self.attacks[5]], [-50], [350], [1000], [350], [20], [l/2], False, False, False, False)
                            self.move([self.attacks[5]], [-50], [650], [1000], [650], [20], [l/2], False, False, False, False)
                    elif i == 16:
                        self.move([self.attacks[6]], [1500], [500], [850], [500], [3], [5], False, False, False, True)
                    elif i == 17:
                        for l in range(5):
                            self.move([self.attacks[12]], [325], [420], [675], [420], [5], [l], False, True, False, False)
                    elif i == 18:
                        self.move([self.attacks[0]], [325], [365], [550], [365], [5], [0], False, False, False, True)
                        self.move([pygame.transform.rotate(self.attacks[0], 90)], [420], [275], [420], [500], [5], [0], False, False, False, True)
                    elif i == 19:
                        self.move([self.attacks[0]], [625], [365], [425], [365], [5], [0], False, False, False, True)
                        self.move([pygame.transform.rotate(self.attacks[0], 90)], [420], [575], [420], [350], [5], [0], False, False, False, True)
                    elif i == 20:
                        pygame.mixer.Channel(2).play(self.ora)
                        for o in range(4):
                            y1 = random.randint(325, 525)
                            y2 = random.randint(325, 525)
                            self.move([pygame.transform.rotate(self.attacks[14], -90)], [245], [y1], [745], [y1], [8], [o], False, False, False, False)
                            self.move([pygame.transform.rotate(self.attacks[14], 90)], [745], [y2], [245], [y2], [8], [o], False, False, False, False)
                    elif i == 21:
                        for l in range(6):
                            self.function_gaster_blaster(False, False, 500, 200, 500, -200, -90, l)
                            a = random.randint(0, 1)
                            if a == 0:
                                self.move([pygame.transform.rotate(self.attacks[12], 90)], [485], [175], [485], [675], [10], [l], False, True, False, False)
                            elif a == 1:
                                self.move([pygame.transform.rotate(self.attacks[13], 90)], [485], [175], [485], [675], [10], [l], False, False, True, False)
                    elif i == 22:
                        a = 0
                        for m in range(9):
                            if a == 0:
                                self.move([self.attacks[2]], [-50], [550], [1000], [550], [15], [m/2], False, False, False, False)
                                a = 1
                            else:
                                self.move([self.attacks[12]], [-50], [420], [1000], [420], [15], [m/2], False, True, False, False)
                                a = 0
                    elif i == 23:
                        self.function_gaster_blaster(False, False, soulx, souly-150, soulx, souly-1000, -90, 0)
                        self.function_gaster_blaster(False, False, soulx, souly+150, soulx, souly+1000, 90, 0)
                        self.function_gaster_blaster(False, False, soulx-150, souly, soulx-1000, souly, 0, 0)
                        self.function_gaster_blaster(False, False, soulx+150, souly, soulx+1000, souly, 180, 0)
                    elif i == 24:
                        self.function_gaster_blaster(False, False, soulx, souly-150, soulx, souly-1000, -90, 0)
                        self.function_gaster_blaster(False, False, soulx, souly+150, soulx, souly+1000, 90, 0)
                        self.function_gaster_blaster(False, False, soulx-150, souly, soulx-1000, souly, 0, 0)
                        self.function_gaster_blaster(False, False, soulx+150, souly, soulx+1000, souly, 180, 0)
                    elif i == 25:
                        self.function_gaster_blaster(False, False, soulx, souly-150, soulx, souly-1000, -90, 0)
                        self.function_gaster_blaster(False, False, soulx, souly+150, soulx, souly+1000, 90, 0)
                        self.function_gaster_blaster(False, False, soulx-150, souly, soulx-1000, souly, 0, 0)
                        self.function_gaster_blaster(False, False, soulx+150, souly, soulx+1000, souly, 180, 0)
                    elif i == 26:
                        pygame.mixer.Channel(9).play(self.za_warudo_words)
                        self.time_stop()
                        self.stop = True
                        pygame.mixer.Channel(0).pause()
                    elif i == 27:
                        pygame.mixer.Channel(2).play(self.resume)
                    elif i == 28:
                        self.stop = False
                        pygame.mixer.Channel(0).unpause()
                    self.triggered[i] = True  # Mark event as triggered

            if elapsed >= 93 and not self.time_stop_sound:
                self.za_warudo_channel.play(self.za_warudo)
                self.time_stop_sound = True

            # Manage timed warning + bonewall phases
            if 29.5 <= elapsed < 30.5 and not self.warnings_active:
                self.warning_sound.play()
                self.warnings_active = True
                self.warnings_displayed = True

            if 30.5 <= elapsed < 31.25:
                self.warnings_active = False
                if self.warnings_displayed:
                    self.bonewalls_started = True
                    self.warnings_displayed = False

            if 31.25 <= elapsed < 32 and self.bonewalls_started and not self.bonewalls_ended:
                self.bonewalls_exiting = True

            if 33.5 <= elapsed < 34.5 and not self.warnings_active:
                # Reconfigure bonewall for second wave
                self.warning_sound.play()
                self.warnings_active = True
                self.warnings_displayed = False
                self.bonewalls_started = False
                self.bonewalls_reversing = False
                self.bonewalls_ended = False
                self.bonewalls_exiting = False
                self.warnings = [{"pos": [box_x+box_width-50, 425], "angle": -90}]
                self.bonewalls = [{"start": [box_x+box_width+100, 425], "end": [box_x+box_width-40, 425], "angle": -90, "current": [box_x+box_width+100, 425]}]
                self.warnings_displayed = True

            if 34.5 <= elapsed < 35:
                self.warnings_active = False
                self.bonewalls_started = True
                self.warnings_displayed = False

            if 35 <= elapsed < 36.25 and self.bonewalls_started and not self.bonewalls_ended:
                self.bonewalls_exiting = True

            # Trigger platform pattern at the end
            if 54 <= elapsed < 63 and not self.platform_enable:
                rotated = pygame.transform.rotate(self.platforms[0], 90)
                start_y1 = 250
                end_y1 = 600
                for m in range(0, 16):
                    for n in range(0, 600, 100):
                        self.move([rotated], [300+n], [start_y1], [300+n], [end_y1], [3], [m/1.5], True, False, False, False)
                        start_y1, end_y1 = end_y1, start_y1
                self.platform_enable = True

            if elapsed >= 115 and not hasattr(self, "beam115_triggered"):
                beam_img = self.gaster_blasters[12]  # beam image
                self.kamehameha.append(Kamehameha(pygame.display.get_surface(), beam_img, y_position=420))
                self.beam115_triggered = True

            # Update bonewall positions if active
            self.update_bonewalls()

    def update_bonewalls(self):
        # Animate bonewalls into or out of the play area
        if not self.bonewalls_started or self.bonewalls_ended:
            return

        speed = 10
        all_exited = True

        for bonewall in self.bonewalls:
            x, y = bonewall["current"]
            dx = dy = 0

            if not self.bonewalls_exiting:
                # Move towards end position
                x_end, y_end = bonewall["end"]
                if x != x_end:
                    dx = speed if x < x_end else -speed
                    if abs(x - x_end) < speed:
                        dx = x_end - x
                if y != y_end:
                    dy = speed if y < y_end else -speed
                    if abs(y - y_end) < speed:
                        dy = y_end - y
            else:
                # Move back towards start
                x_start, y_start = bonewall["start"]
                dx = x_start - bonewall["end"][0]
                dy = y_start - bonewall["end"][1]
                length = (dx**2 + dy**2)**0.5
                if length != 0:
                    dx = dx / length * speed
                    dy = dy / length * speed

            x += int(dx)
            y += int(dy)
            bonewall["current"] = [x, y]

            if 0 <= x <= 1100 and 0 <= y <= 850:
                all_exited = False

        if self.bonewalls_exiting and all_exited:
            self.bonewalls_ended = True
            self.warnings_active = False

    def get_bonewall_rects(self):
        # Return the rectangles for all bonewalls for collision detection
        bonewall_img = self.attacks[9]
        bonewall_rects = []
        for b in self.bonewalls:
            rotated = pygame.transform.rotate(bonewall_img, -b["angle"])
            rect = rotated.get_rect(center=b["current"])
            bonewall_rects.append(rect)
        return bonewall_rects

    def draw(self, surface):
        # Draw warnings and bonewalls if active
        if self.warnings_active:
            warning_img = self.attacks[8]
            for w in self.warnings:
                rotated = pygame.transform.rotate(warning_img, -w["angle"])
                rect = rotated.get_rect(center=w["pos"])
                surface.blit(rotated, rect)

        if not self.bonewalls_ended and self.bonewalls_started:
            bonewall_img = self.attacks[9]
            for b in self.bonewalls:
                rotated = pygame.transform.rotate(bonewall_img, -b["angle"])
                rect = rotated.get_rect(center=b["current"])
                surface.blit(rotated, rect)
