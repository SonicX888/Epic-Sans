import pygame
import time

class Intro(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.bones = [
            pygame.image.load("assets/images/attacks/bones/medium_bone.png")
        ]

        self.play_intro = True
        self.finished_intro = False

        # Compteurs de mouvement pour chaque bone
        self.bone_steps_intro = [0, 0, 0, 0]
        self.last_move_time = time.time()
        self.step_interval = 0.01  # temps entre chaque déplacement

        self.bone = self.bones[0]
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

    def attacks_order(self, play_time):
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
        
        if elapsed >= 24.6:
            self.finished_intro = True

    def draw(self, surface):
        if self.finished_intro == False:
            surface.blit(self.bone, self.rect_bone1)
            surface.blit(self.bone, self.rect_bone2)
            surface.blit(self.bone, self.rect_bone3)
            surface.blit(self.bone, self.rect_bone4)