import time
import pygame

class HP:

    def __init__(self):
        pygame.init()

        self.hp = 92
        self.max_hp = 92
        self.kr = 0

        self.hp_color = (255, 254, 0)
        self.kr_color = (221, 0, 255)
        self.no_hp_color = (255, 0, 0)
        self.hp_x = 425
        self.hp_y = 600
        self.hp_height = 30
        self.no_hp_width = 184

        self.rect_no_hp = pygame.Rect(self.hp_x, self.hp_y, self.no_hp_width, self.hp_height)

        self.font = pygame.font.Font("assets/fonts/Mars_Needs_Cunnilingus.ttf", 35)

        self.sound_damage = pygame.mixer.Sound("assets/sounds/sound_effects/damage.wav")

        self.gameover = False
        self.sound_gameover = pygame.mixer.Sound("assets/sounds/themes/GameOver.wav")
        self.gameover_image = pygame.image.load("assets/images/GameOver.png")
        self.width_gameover, self.height_gameover = self.gameover_image.get_size()
        self.x_gameover = (1000 - self.width_gameover) // 2
        self.y_gameover = (750 - self.height_gameover) // 2 - 100
        self.rect_gameover = pygame.Rect(self.x_gameover, self.y_gameover, self.width_gameover, self.height_gameover)
        self.gameover_alpha = 0  # alpha initial (complètement transparent)
        self.fade_speed = 3      # vitesse d’apparition (peut être ajustée)

        self.death_time = None  # moment où les HP atteignent 0
        self.kr_timer = time.time()

    def update(self):
        if self.kr > 0 and self.hp > 0:
            current_time = time.time()
            if current_time - self.kr_timer >= max(0.01, 1.8 / self.kr):
                self.hp -= 1
                self.kr -= 1
                if self.kr > self.hp - 1:
                    self.kr = self.hp - 1
                self.kr_timer = current_time
                self.hp = max(0, self.hp)

        # Met à jour les tailles des barres
        self.hp_width = (self.hp - self.kr) * 2
        self.kr_width = self.hp * 2
        self.rect_hp = pygame.Rect(self.hp_x, self.hp_y, self.hp_width, self.hp_height)
        self.rect_kr = pygame.Rect(self.hp_x, self.hp_y, self.kr_width, self.hp_height)

        if self.hp <= 0 and self.death_time is None:
            self.death_time = time.time()  # enregistre le moment de la mort

        # Attends 3 secondes après la mort pour afficher le gameover
        if self.death_time is not None:
            if time.time() - self.death_time >= 3 and not self.gameover:
                self.sound_gameover.play()
                self.gameover = True

            if self.gameover and self.gameover_alpha < 255:
                self.gameover_alpha += self.fade_speed
                self.gameover_alpha = min(255, self.gameover_alpha)

    def add_karma(self):
        self.kr += 1
        self.sound_damage.play()
        if self.kr > self.hp - 1:
            self.kr = self.hp - 1

    def collision(self, collision):
        if collision == True:
            self.add_karma()

        if collision == True and self.hp == 1:
            self.hp -= 1

    def draw(self, surface):
        
        if self.hp > 0:
            pygame.draw.rect(surface, self.no_hp_color, self.rect_no_hp)
            pygame.draw.rect(surface, self.kr_color, self.rect_kr)
            pygame.draw.rect(surface, self.hp_color, self.rect_hp)

            self.hp_value = self.font.render(f"{self.hp}/92", True, (255, 255, 255))
            surface.blit(self.hp_value, (700, 600))
        else:
            # Surface intermédiaire avec alpha
            gameover_surf = self.gameover_image.convert_alpha()
            gameover_surf.set_alpha(self.gameover_alpha)
            surface.blit(gameover_surf, self.rect_gameover)
