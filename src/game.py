import pygame
import time
from keys import Keys
from player import Player
from epic_sans import Epic_sans
from menu import Menu
from attacks import Attacks
from hp import HP
from box import Box
from decorations import Decorations
from fps import FPS
from intro import Intro

class Game:
    def __init__(self):

        self.player = Player()
        self.epic_sans = Epic_sans()
        self.menu = Menu()
        self.attacks = Attacks()
        self.hp = HP()
        self.box = Box()
        self.decorations = Decorations()
        self.fps = FPS()
        self.intro = Intro()

        pygame.mixer.music.load("assets/sounds/themes/Menu_theme.mp3")
        pygame.mixer.music.play(loops=-1)

        self.play = 0
        self.play_time = time.time()

        self.running = True

    def function_play_time(self):

        if self.play == 1:
            self.play_time = round(time.time(), 1)

    def update(self):

        self.intro.attacks_order(self.play_time)
        self.attacks.attacks_order(self.play_time, self.hp.hp)
        self.epic_sans.update()
        beam_rects = [gb.beam_rect for gb in self.attacks.active_gaster_blasters if hasattr(gb, "beam_rect")]
        beam_alpha = [gb.beam_alpha for gb in self.attacks.active_gaster_blasters if hasattr(gb, "beam_alpha")]
        bonewall_rects = self.attacks.get_bonewall_rects()
        self.player.update(self.box.hitbox, self.hp.hp, beam_rects, beam_alpha, bonewall_rects)
        self.hp.collision(self.player.collision)
        self.hp.update()
        self.decorations.update(self.play_time)
        self.attacks.update_gaster_blasters(self.player.rect_soul)


    # Fonction d'affichage
    def draw(self):
        self.menu.surface.fill((0, 0, 0))
        self.attacks.draw(self.menu.surface)
        s1 = pygame.Surface((375, 1000))
        s1.fill((0, 0, 0))
        self.menu.surface.blit(s1, (-30, -225))
        self.menu.surface.blit(s1, (645, -225))
        s2 = pygame.Surface((300, 375))
        s2.fill((0, 0, 0))
        self.menu.surface.blit(s2, (345, -100))
        self.menu.surface.blit(s2, (345, 575))
        self.hp.draw(self.menu.surface)
        self.epic_sans.draw(self.menu.surface, self.hp.hp)
        self.player.draw(self.menu.surface, self.hp.hp)
        self.box.draw(self.menu.surface, self.hp.hp)
        self.decorations.draw(self.menu.surface, self.intro.finished_intro, self.hp.hp)
        self.intro.draw(self.menu.surface)
        self.fps.draw(self.menu.surface)
        self.attacks.draw_gaster_blasters()

    # Boucle de jeu principale
    def run(self):
        self.menu.menu_init()
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if self.menu.main_menu.is_enabled():
                self.menu.main_menu.update(events)
                self.menu.main_menu.draw(self.menu.surface)
                self.fps.draw(self.menu.surface)

            if self.menu.start==1:
                self.play += 1
                self.function_play_time()
                self.update()
                self.draw()
                pygame.display.flip()
            pygame.display.update()
            self.fps.clock.tick(60)
