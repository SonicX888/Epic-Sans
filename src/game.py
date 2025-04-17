import pygame
from player import Player
from epic_sans import Epic_sans
from menu import Menu
from decorations import Decorations
from fps import FPS

class Game:
    def __init__(self):

        self.player = Player()
        self.epic_sans = Epic_sans()
        self.menu = Menu()
        self.decorations = Decorations()
        self.fps = FPS()

        pygame.mixer.music.load("assets/sounds/themes/Menu_theme.mp3")
        pygame.mixer.music.play(loops=-1)

        self.running = True

    # Fonction d'affichage
    def draw(self):
        self.menu.surface.fill((0, 0, 0))
        self.epic_sans.draw(self.menu.surface)
        self.player.draw(self.menu.surface)
        self.decorations.draw(self.menu.surface)
        self.fps.draw(self.menu.surface)

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
                self.epic_sans.update()
                self.player.update()
                self.draw() # Raffraichissement de l'écran
                pygame.display.flip()
            pygame.display.update()
            self.fps.clock.tick(60)
