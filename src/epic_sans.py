import pygame
import pygame_menu
import math

class Epic_sans(pygame.sprite.Sprite):
    # Initialisation du joueur
    # @param x - Coordonnées X du joueur ; en fonction du coin supérieur gauche.
    # @param y - Coordonnées Y du joueur ; en fonction du coin supérieur gauche.
    def __init__(self):
        super().__init__()

        self.animation = 0
        self.x_head = 0
        self.y_head = 0
        self.angle_head = 0
        self.x_body = 0
        self.y_body = 0

        self.phase_1_head = []
        self.phase_1_body = []
        self.phase_1_legs = [pygame.image.load("assets/images/phase_1_legs/legs1.png")]
        self.phase_15_head = []
        self.phase_2_head = []
        self.phase_2_body = [pygame.image.load("assets/images/phase_2_body/body1.png")]
        self.phase_2_legs = [pygame.image.load("assets/images/phase_2_legs/legs1.png")]
        self.phase_25_head = []
        self.phase_25_body = [pygame.image.load("assets/images/phase_2.5_body/body1.png")]
        self.phase_25_legs = [pygame.image.load("assets/images/phase_2.5_legs/legs1.png")]
        self.phase_3_head = []
        self.phase_3_body = []
        self.phase_3_left_arm = []
        self.phase_3_right_arm = []
        self.phase_3_legs = []
        self.phase_3_animation = []

        for i in range(1, 4):
            add = pygame.image.load(f"assets/images/phase_1_head/head{i}.png")
            self.phase_1_head.append(add)

        for i in range(1, 3):
            add = pygame.image.load(f"assets/images/phase_1_body/body{i}.png")
            self.phase_1_body.append(add)

        for i in range(1, 3):
            add = pygame.image.load(f"assets/images/phase_1.5_head/head{i}.png")
            self.phase_15_head.append(add)

        for i in range(1, 3):
            add = pygame.image.load(f"assets/images/phase_2_head/head{i}.png")
            self.phase_2_head.append(add)

        for i in range(1, 4):
            add = pygame.image.load(f"assets/images/phase_2.5_head/head{i}.png")
            self.phase_25_head.append(add)

        for i in range(1, 6):
            add = pygame.image.load(f"assets/images/phase_3_head/head{i}.png")
            self.phase_3_head.append(add)

        for i in range(1, 19):
            add = pygame.image.load(f"assets/images/phase_3_body/body{i}.png")
            self.phase_3_body.append(add)

        for i in range(1, 4):
            add = pygame.image.load(f"assets/images/phase_3_left_arm/left_arm{i}.png")
            self.phase_3_left_arm.append(add)

        for i in range(1, 3):
            add = pygame.image.load(f"assets/images/phase_3_right_arm/right_arm{i}.png")
            self.phase_3_right_arm.append(add)

        for i in range(1, 6):
            add = pygame.image.load(f"assets/images/phase_3_legs/legs{i}.png")
            self.phase_3_legs.append(add)

        for i in range(1, 9):
            add = pygame.image.load(f"assets/images/phase_3_animation/animation{i}.png")
            self.phase_3_animation.append(add)

        # Image de départ
        self.head = self.phase_1_head[0]
        self.width_head, self.height_head = self.head.get_size()
        self.rect_head = pygame.Rect(460, 30, self.width_head, self.height_head)

        self.body = self.phase_1_body[0]
        self.width_body, self.height_body = self.body.get_size()
        self.rect_body = pygame.Rect(450, 80, self.width_body, self.height_body)

        self.legs = self.phase_1_legs[0]
        self.width_legs, self.height_legs = self.legs.get_size()
        self.rect_legs = pygame.Rect(450, 150, self.width_legs, self.height_legs)

        # On commence à la première frame
        # width, height = self.image.get_size()
        # Image de départ
        # self.rect = pygame.Rect(center(width, height)[0], center(width, height)[1], width, height)

    def update(self, screen):

        self.animation += 0.05
        self.x_head = ((math.sin(self.animation * 1.5) * 2) + 460)
        self.y_head = ((math.sin(self.animation * 3) * 4) + 30)
        self.angle_head = ((math.sin(self.animation * 4) * 2) + 90)
        self.x_body = ((math.sin(self.animation * 1.5) * 2) + 450)
        self.y_body = ((math.sin(self.animation * 3) * 3) + 80)
        self.rect_head.x = self.x_head
        self.rect_head.y = self.y_head
        self.rect_body.x = self.x_body
        self.rect_body.y = self.y_body

    # Fonction récurrente de dessin
    def draw(self, screen):
        screen.blit(self.legs, self.rect_legs)
        screen.blit(self.body, self.rect_body)
        screen.blit(self.head, self.rect_head)

