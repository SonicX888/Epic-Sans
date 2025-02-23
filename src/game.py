import pygame
#from player import Player
from menu import Menu

class Game:
    def __init__(self):
        pygame.mixer.music.load("assets/sounds/themes/Menu_theme.mp3")
        pygame.mixer.music.play()

        self.clock = pygame.time.Clock()
        self.running = True
        #self.player = Player(400, 300) # Le joueur

    # Fonction d'affichage
    def draw(self):
        Menu.surface.fill((255, 255, 255))
        #self.player.draw(Menu.surface)
        pygame.display.flip()

    # Boucle de jeu principale
    def run(self):
        Menu.menu_init()
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
                self.clock.tick(60)

            pygame.display.update()
