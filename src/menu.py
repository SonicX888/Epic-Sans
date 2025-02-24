import pygame_menu
import pygame

class Menu:
    pygame.init()
    start = 0
    surface = pygame.display.set_mode((1000, 750))
    menu_background=(0, 0, 0)
    color_selection = (255, 255, 0)
    font_title = "assets/fonts/Frisky.ttf"
    font_widget = "assets/fonts/DTM-Mono.otf"
    menu_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
    widget_color = (255, 255, 255)
    widget_size = 40
    padding = (32, 64)
    title_offset_y = 40

    theme_main_menu = pygame_menu.Theme(background_color=menu_background,
                                       widget_alignment=pygame_menu.locals.ALIGN_LEFT,
                                       selection_color=color_selection,
                                       title_bar_style=menu_bar_style,
                                       title_font=font_title,
                                       title_font_color=(128,0,128),
                                       title_font_size=80,
                                       title_offset=(100, title_offset_y),
                                       widget_font=font_widget,
                                       widget_font_color=widget_color,
                                       widget_font_size=widget_size,
                                       widget_padding=padding)

    theme_credits = pygame_menu.Theme(background_color=menu_background,
                                      selection_color=color_selection,
                                      title_bar_style=menu_bar_style,
                                      title_close_button=False,
                                      widget_font=font_widget,
                                      widget_font_color=widget_color,
                                      widget_font_size=widget_size,
                                      widget_padding=padding,
                                      scrollbar_color=(255, 255, 255),
                                      scrollbar_slider_color=(225, 225, 225))

    settings_text = ["Settings",
                    " "]

    credits_text = ["Credits",
                    " "]

    sounds = pygame_menu.sound.Sound()
    sounds.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, "assets/sounds/sound_effects/move selection.wav")

    main_menu = pygame_menu.Menu("Epic!Sans Fight", 1000, 750, theme=theme_main_menu)
    credits_menu = pygame_menu.Menu(" ", 1000, 750, theme=theme_credits)
    settings_menu = pygame_menu.Menu(" ", 1000, 750, theme=theme_credits)

    custom_controller = pygame_menu.controls.Controller()

    def btn_move_up(self, event):
        return pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]

    custom_controller.move_up = btn_move_up

    def btn_move_down(self, event):
        return pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_z]

    custom_controller.move_down = btn_move_down

    def start_the_game():
        Menu.start = 1
        Menu.main_menu.clear()
        Menu.main_menu.full_reset()

    def settings_menu_open():
        Menu.main_menu._open(Menu.settings_menu)

    def credits_menu_open():
        Menu.main_menu._open(Menu.credits_menu)


    def menu_init(self):

        Menu.main_menu.add.button('Play', Menu.start_the_game)
        Menu.main_menu.add.button('Settings', Menu.settings_menu)
        Menu.main_menu.add.button('Credits', Menu.credits_menu_open)
        Menu.main_menu.add.button('Exit', pygame_menu.events.EXIT)
        Menu.main_menu.set_sound(Menu.sounds, recursive=True)

        Menu.main_menu.set_controller(Menu.custom_controller)

    for i in credits_text:
        credits_menu.add.label(i, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    credits_menu.add.button('Precedent', pygame_menu.events.BACK)
    credits_menu.set_sound(sounds, recursive=True)

    for j in settings_text:
        settings_menu.add.label(j, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)

    def set_music_volume(slider_value: float):
        pygame.mixer.music.set_volume(slider_value / 100.0)  # Convert range 0-100 to 0.0-1.0

    # Add the range slider and link it to set_music_volume
    settings_menu.add.range_slider('Volume', 100, (0, 100), 1,
                                   rangeslider_id='range_slider',
                                   value_format=lambda x: str(int(x)),
                                   onchange=set_music_volume)
    settings_menu.add.button('Precedent', pygame_menu.events.BACK)
    settings_menu.set_sound(sounds, recursive=True)