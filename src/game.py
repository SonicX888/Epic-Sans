import pygame
from epic_sans import Epic_sans
from menu import Menu
from fps import FPS

class Game:
    def __init__(self):

        self.menu = Menu()

        pygame.mixer.music.load("assets/sounds/themes/Menu_theme.mp3")
        pygame.mixer.music.play()

        self.running = True
        self.epic_sans = Epic_sans(750, 500) # Le joueur
        self.fps = FPS()

    # Fonction d'affichage
    def draw(self):
        self.menu.surface.fill((0, 0, 0))
        self.epic_sans.draw(self.menu.surface)
        self.fps.render(self.menu.surface)

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
                self.fps.render(self.menu.surface)

            if self.menu.start==1:
                pygame.mixer.music.stop()
                #self.player.update()
                self.draw() # Raffraichissement de l'écran
                pygame.display.flip()
            pygame.display.update()
            self.fps.clock.tick(60)
