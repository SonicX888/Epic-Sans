import pygame

class Attacks(pygame.sprite.Sprite):
    def __init__(self):

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

        self.play_intro = True
        self.order = ""

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
    
    def intro(self, x):
        if self.play_intro == True:
            self.bone = self.bones[7]
            self.width_bone, self.height_bone = self.bone.get_size()
            self.y_bone = 750
            for i in range(0, 12):
                self.rect_bone = pygame.Rect(x, self.y_bone, self.width_bone, self.height_bone)
                self.order = "intro"
                self.y_bone -= 10

    def draw(self, surface):
        if self.order == "intro":
            surface.blit(self.bone, self.rect_bone)