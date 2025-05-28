# --- Class: Game ---
# Purpose: Manages the entire game loop, initialization, updates, and rendering of all components
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
from ball import Ball
from end import End

class Game:
    def __init__(self):
        # Instantiate all game components
        self.player = Player()
        self.epic_sans = Epic_sans()
        self.menu = Menu()
        self.attacks = Attacks()
        self.hp = HP()
        self.box = Box()
        self.decorations = Decorations()
        self.fps = FPS()
        self.intro = Intro()

        # Load and play main menu music
        pygame.mixer.music.load("assets/sounds/themes/Menu_theme.mp3")
        pygame.mixer.music.play(loops=-1)

        # Game state flags and timer
        self.play = 0
        self.play_time = time.time()
        self.running = True

        # Side barriers around the box
        self.s1_width = 375
        self.s1_height = 1000
        self.s1 = pygame.Surface((self.s1_width, self.s1_height))
        self.s1.fill((0, 0, 0))
        self.s2_width = 1000
        self.s2_height = 375
        self.s2 = pygame.Surface((self.s2_width, self.s2_height))
        self.s2.fill((0, 0, 0))

        self.balls = pygame.sprite.Group()
        self.ball_start_time = None
        
    def function_play_time(self):
        # Set play_time when the game starts
        if self.play == 1:
            self.play_time = round(time.time(), 1)
            self.end = End(self.menu.surface, self.play_time)

    def update(self):
        # Update all game elements per frame
        self.intro.attacks_order(self.play_time)
        self.attacks.attacks_order(self.play_time, self.hp.hp, self.box.x, self.box.width, self.player.rect_soul.centerx, self.player.rect_soul.centery)
        self.attacks.update_bones(self.hp.hp)
        self.box.update(self.play_time)
        self.epic_sans.update(self.play_time, self.hp.hp, self.attacks.stop)

        # Generate rects for collision detection
        accessory_rects = []
        for a in self.epic_sans.accessory_instances:
            if not a.finished:
                w, h = a.image.get_size()
                rect = pygame.Rect(a.pos[0], a.pos[1], w, h)
                accessory_rects.append(rect)

        beam_rects = [gb.beam_rect for gb in self.attacks.active_gaster_blasters if hasattr(gb, "beam_rect")]
        bone_rects = [bone.rect for bone in self.attacks.moving_bones if hasattr(bone, "rect") and not bone.platform and not bone.blue and not bone.orange]
        platform_rects = [bone.rect for bone in self.attacks.moving_bones if hasattr(bone, "rect") and bone.platform]
        blue_rects = [bone.rect for bone in self.attacks.moving_bones if hasattr(bone, "rect") and bone.blue]
        orange_rects = [bone.rect for bone in self.attacks.moving_bones if hasattr(bone, "rect") and bone.orange]
        bonewall_rects = self.attacks.get_bonewall_rects()
        time_stop_rects = []
        ball_rects = [ball.rect for ball in self.balls]
        kamehameha_rects = [b.rect for b in self.attacks.kamehameha if hasattr(b, "rect") and not b.done]
        combined_beam_rects = beam_rects + kamehameha_rects
        if self.attacks.time_stop_manager:
            time_stop_rects = self.attacks.time_stop_manager.get_collision_rects()
        # Update player and HP logic
        self.player.update(self.box.hitbox, self.hp.hp, self.play_time, self.attacks.stop, combined_beam_rects, bonewall_rects, bone_rects, platform_rects, accessory_rects, blue_rects, orange_rects, time_stop_rects, ball_rects)

        self.hp.collision(self.player.collision)
        self.hp.update()

        # Update UI elements
        self.decorations.update(self.play_time)
        self.attacks.update_gaster_blasters(self.player.rect_soul, self.hp.hp)

        current_time = time.time()
        if self.hp.hp > 0:
            if 105 <= current_time - self.play_time <= 110:
                if pygame.time.get_ticks() % 3 == 0:
                    direction = (pygame.time.get_ticks() // 3) % 360
                    speed = 5
                    self.balls.add(Ball(500, 400, direction, speed))
            elif 110 <= current_time - self.play_time <= 115:
                if pygame.time.get_ticks() % 3 == 0:
                    direction = (pygame.time.get_ticks() // 3) % 360
                    speed = 5
                    self.balls.add(Ball(250, 100, direction, speed))
                    self.balls.add(Ball(750, 100, -direction, speed))

            self.balls.update(self.menu.surface)
            self.attacks.update_kamehameha()
            self.end.update()

    def draw(self):
        # Clear screen and draw all elements
        self.menu.surface.fill((0, 0, 0))
        self.attacks.draw(self.menu.surface)
        self.attacks.draw_bones(self.menu.surface, self.hp.hp)

        # Draw side barriers around the box
        self.menu.surface.blit(self.s1, (self.box.x - self.s1_width, -225))
        self.menu.surface.blit(self.s1, (self.box.x + self.box.width, -225))
        self.menu.surface.blit(self.s2, (0, self.box.y - self.s2_height))
        self.menu.surface.blit(self.s2, (0, self.box.y + self.box.height))

        # Draw game entities
        self.hp.draw(self.menu.surface)
        self.player.draw(self.menu.surface, self.hp.hp)
        if self.hp.hp > 0:
            self.box.draw(self.menu.surface, self.hp.hp)
            self.epic_sans.draw(self.menu.surface, self.hp.hp)
            self.decorations.draw(self.menu.surface, self.intro.finished_intro, self.hp.hp)
            self.intro.draw(self.menu.surface)
            self.fps.draw(self.menu.surface)
            self.attacks.draw_time_stop(self.menu.surface, self.hp.hp)
            self.balls.draw(self.menu.surface)
            self.attacks.draw_gaster_blasters(self.hp.hp)
            self.attacks.draw_kamehameha()
            self.end.draw()

    def run(self):
        # Run main game loop
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

            if self.menu.start == 1:
                self.play += 1
                self.function_play_time()
                self.update()
                self.draw()
                pygame.display.flip()

            pygame.display.update()
            self.fps.clock.tick(60)
