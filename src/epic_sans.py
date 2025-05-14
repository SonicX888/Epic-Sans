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

        def load_images(pattern, count):
            return [pygame.image.load(pattern.format(i)) for i in range(1, count + 1)]

        # Chargement des images
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

        # Initialisation des sprites
        self._init_sprites()

    def _init_sprites(self):
        # Tête
        self.head = self.phase_1_head[0]
        self.width_head, self.height_head = self.head.get_size()
        self.x_head = 440
        self.y_head = 30
        self.rect_head = pygame.Rect(self.x_head, self.y_head, self.width_head, self.height_head)

        # Corps
        self.body = self.phase_1_body[0]
        self.width_body, self.height_body = self.body.get_size()
        self.x_body = 430
        self.y_body = 80
        self.rect_body = pygame.Rect(self.x_body, self.y_body, self.width_body, self.height_body)

        # Jambes
        self.legs = self.phase_1_legs[0]
        self.width_legs, self.height_legs = self.legs.get_size()
        self.x_legs = 430
        self.y_legs = 150
        self.rect_legs = pygame.Rect(self.x_legs, self.y_legs, self.width_legs, self.height_legs)


    def update(self):

        self.animation += 0.05
        self.new_x_head = ((math.sin(self.animation * 1.5) * 2) + self.x_head)
        self.new_y_head = ((math.sin(self.animation * 3) * 4) + self.y_head)
        #self.angle_head = ((math.sin(self.animation * 4) * 2) + 90)
        self.new_x_body = ((math.sin(self.animation * 1.5) * 2) + self.x_body)
        self.new_y_body = ((math.sin(self.animation * 3) * 3) + self.y_body)
        self.rect_head.x = self.new_x_head
        self.rect_head.y = self.new_y_head
        self.rect_body.x = self.new_x_body
        self.rect_body.y = self.new_y_body

    # Fonction récurrente de dessin
    def draw(self, surface):
        surface.blit(self.legs, self.rect_legs)
        surface.blit(self.body, self.rect_body)
        surface.blit(self.head, self.rect_head)

