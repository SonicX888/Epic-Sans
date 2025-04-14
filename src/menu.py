import pygame_menu
import pygame

class Menu:
    pygame.init()
    def __init__(self):
    
        self.start = 0
        self.surface = pygame.display.set_mode((1000, 750))
        self.menu_background=(0, 0, 0)
        self.color_selection = (255, 255, 0)
        self.font_title = "assets/fonts/Frisky.ttf"
        self.font_widget = "assets/fonts/DTM-Mono.otf"
        self.menu_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        self.widget_color = (255, 255, 255)
        self.widget_size = 40
        self.padding = (32, 64)

        self.theme_main_menu = pygame_menu.Theme(background_color=self.menu_background,
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
                                                 widget_padding=self.padding)

        self.theme_credits = pygame_menu.Theme(background_color=self.menu_background,
                                               selection_color=self.color_selection,
                                               title_bar_style=self.menu_bar_style,
                                               title_close_button=False,
                                               widget_font=self.font_widget,
                                               widget_font_color=self.widget_color,
                                               widget_font_size=self.widget_size,
                                               widget_padding=self.padding,
                                               scrollbar_color=(255, 255, 255),
                                               scrollbar_slider_color=(225, 225, 225))

        self.settings_text = ["Settings",
                        " "]

        self.credits_text = ["Credits",
                        " "]

        self.sounds = pygame_menu.sound.Sound()
        self.sounds.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, "assets/sounds/sound_effects/move selection.wav")

        self.main_menu = pygame_menu.Menu("Epic!Sans Fight", 1000, 750, theme=self.theme_main_menu)
        self.credits_menu = pygame_menu.Menu(" ", 1000, 750, theme=self.theme_credits)
        self.settings_menu = pygame_menu.Menu(" ", 1000, 750, theme=self.theme_credits)

        for i in self.credits_text:
            self.credits_menu.add.label(i, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
        self.credits_menu.add.button('Precedent', pygame_menu.events.BACK)
        self.credits_menu.set_sound(self.sounds, recursive=True)

        for j in self.settings_text:
            self.settings_menu.add.label(j, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)

        def set_music_volume(slider_value: float):
            pygame.mixer.music.set_volume(slider_value / 100.0)  # Convert range 0-100 to 0.0-1.0

        # Add the range slider and link it to set_music_volume
        self.settings_menu.add.range_slider('Volume', 100, (0, 100), 1,
                                    rangeslider_id='range_slider',
                                    value_format=lambda x: str(int(x)),
                                    onchange=set_music_volume)
        self.settings_menu.add.button('Precedent', pygame_menu.events.BACK)
        self.settings_menu.set_sound(self.sounds, recursive=True)

        self.image_decorator = pygame_menu.baseimage.BaseImage(image_path="assets/images/menu_epic_sans.png",
                                                        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
        self.image_decorator.scale(2, 2)
        self.decorator = self.main_menu.get_decorator()
        self.decorator.add_baseimage(25, -175, self.image_decorator, False)

        pygame_menu.controls.KEY_APPLY = pygame.K_z
        pygame_menu.controls.KEY_BACK = pygame.K_x

    '''custom_controller = pygame_menu.controls.Controller()

    def btn_move_up(self, event):
        return pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]

    custom_controller.move_up = btn_move_up

    def btn_move_down(self, event):
        return pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_z]

    custom_controller.move_down = btn_move_down'''

    def start_the_game(self):
        self.start = 1
        self.main_menu.clear()
        self.main_menu.full_reset()

    def settings_menu_open(self):
        self.main_menu._open(self.settings_menu)

    def credits_menu_open(self):
        self.main_menu._open(self.credits_menu)


    def menu_init(self):

        self.main_menu.add.button('Play', self.start_the_game)
        self.main_menu.add.button('Settings', self.settings_menu)
        self.main_menu.add.button('Credits', self.credits_menu_open)
        self.main_menu.add.button('Exit', pygame_menu.events.EXIT)
        self.main_menu.set_sound(self.sounds, recursive=True)

        #Menu.main_menu.set_controller(Menu.custom_controller)