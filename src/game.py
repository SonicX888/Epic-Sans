import pygame
import time
from player import Player
from epic_sans import Epic_sans
from menu import Menu
from attacks import Attacks
from hp import HP
from box import Box
from decorations import Decorations
from fps import FPS

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

        pygame.mixer.music.load("assets/sounds/themes/Menu_theme.mp3")
        pygame.mixer.music.play(loops=-1)

        self.play = 0
        self.play_time = time.time()

        self.running = True

    def function_play_time(self):

        if self.play == 1:
            self.play_time = round(time.time(), 1)

    def intro(self):
        if round(time.time(), 1) == self.play_time + 12:
            self.attacks.intro(190)
        elif round(time.time(), 1) == self.play_time + 14.5:
            self.attacks.intro(390)
        elif round(time.time(), 1) == self.play_time + 17:
            self.attacks.intro(615)
        elif round(time.time(), 1) == self.play_time + 19.5:
            self.attacks.intro(830)

    def update(self):
        self.epic_sans.update()
        self.player.update(self.box.hitbox)
        self.hp.collision(self.player.collision)
        self.hp.update()
        self.decorations.update(self.play_time)


    # Fonction d'affichage
    def draw(self):
        self.menu.surface.fill((0, 0, 0))
        self.hp.draw(self.menu.surface)
        self.epic_sans.draw(self.menu.surface)
        self.player.draw(self.menu.surface)
        self.box.draw(self.menu.surface)
        self.decorations.draw(self.menu.surface)
        self.fps.draw(self.menu.surface)
        self.attacks.draw(self.menu.surface)

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
                self.intro()
                self.update()
                self.draw()
                pygame.display.flip()
            pygame.display.update()
            self.fps.clock.tick(60)
