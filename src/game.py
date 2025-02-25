import pygame
import pygame_menu
from epic_sans import Epic_sans
from menu import Menu
from fps import FPS

class Game:
    def __init__(self):
        pygame.mixer.music.load("assets/sounds/themes/Menu_theme.mp3")
        pygame.mixer.music.play()

        self.running = True
        self.epic_sans = Epic_sans(750, 500) # Le joueur
        self.fps = FPS()

    # Fonction d'affichage
    def draw(self):
        Menu.surface.fill((0, 0, 0))
        self.epic_sans.draw(Menu.surface)
        pygame.display.flip()

    # Boucle de jeu principale
    def run(self):
        Menu.menu_init(Menu())
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if Menu.main_menu.is_enabled():
                Menu.main_menu.update(events)
                Menu.main_menu.draw(Menu.surface)

            if Menu.start==1:
                pygame.mixer.music.stop()
                #self.player.update()
                self.draw() # Raffraichissement de l'écran
                self.fps.render(Menu.surface)
            pygame.display.update()
            self.fps.clock.tick(60)
