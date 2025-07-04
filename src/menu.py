# --- Class: Menu ---
# Purpose: Creates and manages all menu interfaces (main, settings) and sound/graphic settings
import pygame_menu
import pygame
from assets import Assets

class Menu:
    pygame.init()

    def __init__(self):

        self.assets = Assets()

        self.start = 0
        self.surface = pygame.display.set_mode((1000, 750))
        self.menu_background = (0, 0, 0)
        self.color_selection = (255, 255, 0)

        # Fonts and styling for menus
        self.font_title = self.assets.Frisky
        self.font_widget = self.assets.DTM_Mono
        self.menu_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        self.widget_color = (255, 255, 255)
        self.widget_size = 40
        self.padding = (32, 64)

        # Theme for main menu
        self.theme_main_menu = pygame_menu.Theme(
            background_color=self.menu_background,
            widget_alignment=pygame_menu.locals.ALIGN_LEFT,
            selection_color=self.color_selection,
            title_bar_style=self.menu_bar_style,
            title_font=self.font_title,
            title_font_color=(128, 0, 128),
            title_font_size=80,
            title_offset=(100, 50),
            widget_font=self.font_widget,
            widget_font_color=self.widget_color,
            widget_font_size=self.widget_size,
            widget_padding=self.padding
        )

        # Theme for credits and settings
        self.theme_settings = pygame_menu.Theme(
            background_color=self.menu_background,
            selection_color=self.color_selection,
            title_bar_style=self.menu_bar_style,
            title_close_button=False,
            widget_font=self.font_widget,
            widget_font_color=self.widget_color,
            widget_font_size=self.widget_size,
            widget_padding=self.padding,
            scrollbar_color=(255, 255, 255),
            scrollbar_slider_color=(225, 225, 225)
        )

        # Labels used in submenus
        self.settings_text = ["Settings", " "]

        # Sound on menu selection
        self.sounds = pygame_menu.sound.Sound()
        self.sounds.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, self.assets.move_selection)

        # Create menus
        self.main_menu = pygame_menu.Menu("Epic!Sans Fight", 1000, 750, theme=self.theme_main_menu)
        self.settings_menu = pygame_menu.Menu(" ", 1000, 750, theme=self.theme_settings)

        # Populate settings menu
        for j in self.settings_text:
            self.settings_menu.add.label(j, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)

        def set_music_volume(slider_value: float):
            pygame.mixer.music.set_volume(slider_value / 100.0)

        self.settings_menu.add.range_slider('Volume', 100, (0, 100), 1,
                                    rangeslider_id='range_slider',
                                    value_format=lambda x: str(int(x)),
                                    onchange=set_music_volume)
        self.settings_menu.add.button('Precedent', pygame_menu.events.BACK)
        self.settings_menu.set_sound(self.sounds, recursive=True)

        # Add image background to main menu
        self.image_decorator = pygame_menu.baseimage.BaseImage(
            image_path=self.assets.menu_epic_sans,
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
        self.image_decorator.scale(2, 2)
        self.decorator = self.main_menu.get_decorator()
        self.decorator.add_baseimage(25, -175, self.image_decorator, False)

        # Custom input controls
        pygame_menu.controls.KEY_APPLY = pygame.K_z
        pygame_menu.controls.KEY_BACK = pygame.K_x

    def start_the_game(self):
        # Called when Play is pressed
        self.start = 1
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.assets.plot_armor)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.assets.plot_armor))
        self.main_menu.clear()
        self.main_menu.full_reset()

    def settings_menu_open(self):
        # Opens the settings menu
        self.main_menu._open(self.settings_menu)

    def menu_init(self):
        # Initializes and displays the main menu with its buttons
        self.main_menu.add.button('Play', self.start_the_game)
        self.main_menu.add.button('Settings', self.settings_menu)
        self.main_menu.add.button('Exit', pygame_menu.events.EXIT)
        self.main_menu.set_sound(self.sounds, recursive=True)
