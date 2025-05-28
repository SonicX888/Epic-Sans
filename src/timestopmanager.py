import pygame
import time
import random

class TimeStopManager:
    def __init__(self, attacks):
        self.attacks = attacks
        self.start_time = time.time()
        self.bones = []
        self.bones_spawned = 0
        self.bones_to_spawn_times = [self.start_time + 3 + i * 0.1 for i in range(20)]
        self.bone_start_times = [self.start_time + 8 + i * 0.1 for i in range(20)]
        self.road_roller_pos = [200, -400]
        self.road_roller_done = False
        self.surface_alpha = 180
        self.done = False
        self.road_roller_sound = pygame.mixer.Sound("assets/sounds/sound_effects/road_roller.wav")

    def get_collision_rects(self):
        rects = []

        for bone in self.bones:
            if hasattr(bone, "rect"):
                rects.append(bone.rect)

        # Road Roller
        if 0 < self.road_roller_pos[1] < 1000:
            road_rect = self.attacks[15].get_rect(topleft=self.road_roller_pos)
            rects.append(road_rect)

        return rects

    def update(self, Bones, hp):
        now = time.time()
        if hp > 0:
            # Spawn bones progressively starting at 4s
            while (self.bones_spawned < 20 and now >= self.bones_to_spawn_times[self.bones_spawned]):
                x = random.randint(50, 950)
                start_time = self.bone_start_times[self.bones_spawned]
                bone = Bones(self.attacks[5], x, 100, x, 1100, 10, start_time, False, False, False, False)
                bone.active = False  # It will activate on its own based on start_time
                bone.visible = True  # Important : os visibles dès leur apparition
                self.bones.append(bone)
                self.bones_spawned += 1

            # Fade overlay after 5s
            if now - self.start_time >= 5 and self.surface_alpha > 0:
                self.surface_alpha -= 10

            # End of time stop effect
            if now - self.start_time >= 15:
                self.done = True

    def draw(self, surface, hp):
        if hp > 0:
            if self.done:
                return

            now = time.time()
            elapsed = now - self.start_time

            # Overlay
            overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            overlay.fill((50, 50, 50, self.surface_alpha))
            surface.blit(overlay, (0, 0))

            # Road roller logic
            if 2 <= elapsed <= 7:
                if self.road_roller_pos[1] < -50:
                    self.road_roller_pos[1] += 20
                elif elapsed >= 6 and self.road_roller_pos[1] < 250:
                    self.road_roller_pos[1] += 20
                if not self.road_roller_done:
                    pygame.mixer.Channel(4).play(self.road_roller_sound)
                    self.road_roller_done = True
                surface.blit(self.attacks[15], self.road_roller_pos)
            elif elapsed >= 7:
                self.road_roller_pos[1] = 1500

            # Bone draw (Bones manage their own timing internally)
            for bone in self.bones:
                bone.update()
                bone.draw(surface)
