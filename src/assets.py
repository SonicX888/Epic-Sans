# --- Class: Assets ---
# Purpose: Centralizes and organizes all file paths for game assets. It handles dynamic resolution of asset locations depending on whether the application is running in a development environment or as a bundled executable.
import sys
import os

class Assets:
  def __init__(self):
    # Determine the base path for assets depending on whether the app is frozen (e.g. packaged with PyInstaller)
    if getattr(sys, 'frozen', False):
      base_path = sys._MEIPASS  # Temporary folder used by PyInstaller
    else:
      base_path = os.path.abspath(".")  # Use current directory when running normally

    # Base path to all assets
    assets_path = os.path.join(base_path, "assets")

    # Paths to subfolders within the assets directory
    images_path = os.path.join(assets_path, "images")
    attacks_path = os.path.join(images_path, "attacks")
    buttons_path = os.path.join(images_path, "buttons")
    epic_sans_path = os.path.join(images_path, "epic_sans")
    icons_path = os.path.join(images_path, "icons")
    slices_path = os.path.join(images_path, "slices")
    soul_path = os.path.join(images_path, "soul")

    # Attack image subfolders
    bones_path = os.path.join(attacks_path, "bones")
    gaster_blaster_path = os.path.join(attacks_path, "gaster_blaster")
    others_path = os.path.join(attacks_path, "others")

    # Epic Sans character sprite subfolders
    accessories_path = os.path.join(epic_sans_path, "accessories")
    phase_1_body_path = os.path.join(epic_sans_path, "phase_1_body")
    phase_1_head_path = os.path.join(epic_sans_path, "phase_1_head")
    phase_1_legs_path = os.path.join(epic_sans_path, "phase_1_legs")
    phase_15_head_path = os.path.join(epic_sans_path, "phase_1.5_head")
    phase_25_body_path = os.path.join(epic_sans_path, "phase_2.5_body")
    phase_25_head_path = os.path.join(epic_sans_path, "phase_2.5_head")
    phase_25_legs_path = os.path.join(epic_sans_path, "phase_2.5_legs")
    phase_2_body_path = os.path.join(epic_sans_path, "phase_2_body")
    phase_2_head_path = os.path.join(epic_sans_path, "phase_2_head")
    phase_2_legs_path = os.path.join(epic_sans_path, "phase_2_legs")
    phase_3_body_path = os.path.join(epic_sans_path, "phase_3_body")
    phase_3_head_path = os.path.join(epic_sans_path, "phase_3_head")
    phase_3_legs_path = os.path.join(epic_sans_path, "phase_3_legs")
    phase_3_left_arm_path = os.path.join(epic_sans_path, "phase_3_left_arm")
    phase_3_right_arm_path = os.path.join(epic_sans_path, "phase_3_right_arm")
    phase_3_anim_path = os.path.join(epic_sans_path, "phase_3_animation")

    # Bone attack sprites
    self.bonewall = os.path.join(bones_path, "bonewall.png")
    self.bottom_bone = os.path.join(bones_path, "bottom_bone.png")
    self.cross_bone = os.path.join(bones_path, "cross_bone.png")
    self.little_bone = os.path.join(bones_path, "little_bone.png")
    self.long_bone = os.path.join(bones_path, "long_bone.png")
    self.long_medium_bone_jump = os.path.join(bones_path, "long_medium_bone_jump.png")
    self.medium_blue_bone = os.path.join(bones_path, "medium_blue_bone.png")
    self.medium_bone = os.path.join(bones_path, "medium_bone.png")
    self.medium_bone_jump = os.path.join(bones_path, "medium_bone_jump.png")
    self.medium_orange_bone = os.path.join(bones_path, "medium_orange_bone.png")
    self.MEGA_bone = os.path.join(bones_path, "MEGA_bone.png")
    self.semi_circle_bone = os.path.join(bones_path, "semi-circle_bone.png")
    self.top_bone = os.path.join(bones_path, "top_bone.png")
    self.warning = os.path.join(bones_path, "warning.png")

    # Gaster blaster sprites
    self.beam1 = os.path.join(gaster_blaster_path, "beam1.png")
    self.gaster_blaster1 = os.path.join(gaster_blaster_path, "gaster_blaster1.png")
    self.gaster_blaster2 = os.path.join(gaster_blaster_path, "gaster_blaster2.png")
    self.gaster_blaster3 = os.path.join(gaster_blaster_path, "gaster_blaster3.png")
    self.gaster_blaster4 = os.path.join(gaster_blaster_path, "gaster_blaster4.png")
    self.gaster_blaster5 = os.path.join(gaster_blaster_path, "gaster_blaster5.png")
    self.gaster_blaster6 = os.path.join(gaster_blaster_path, "gaster_blaster6.png")
    self.small_gaster_blaster1 = os.path.join(gaster_blaster_path, "small_gaster_blaster1.png")
    self.small_gaster_blaster2 = os.path.join(gaster_blaster_path, "small_gaster_blaster2.png")
    self.small_gaster_blaster3 = os.path.join(gaster_blaster_path, "small_gaster_blaster3.png")
    self.small_gaster_blaster4 = os.path.join(gaster_blaster_path, "small_gaster_blaster4.png")
    self.small_gaster_blaster5 = os.path.join(gaster_blaster_path, "small_gaster_blaster5.png")
    self.small_gaster_blaster6 = os.path.join(gaster_blaster_path, "small_gaster_blaster6.png")

    # Other attack-related images
    self.ball = os.path.join(others_path, "ball.png")
    self.fist = os.path.join(others_path, "fist.png")
    self.pillar = os.path.join(others_path, "pillar.png")
    self.pillar1 = os.path.join(others_path, "pillar1.png")
    self.platform = os.path.join(others_path, "platform.png")
    self.road_roller_image = os.path.join(others_path, "road_roller.png")

    # Button graphics
    self.buttons = os.path.join(buttons_path, "buttons.png")
    self.buttons_broken1 = os.path.join(buttons_path, "buttons_broken1.png")
    self.buttons_broken2 = os.path.join(buttons_path, "buttons_broken2.png")
    self.buttons_broken3 = os.path.join(buttons_path, "buttons_broken3.png")
    self.buttons_broken4 = os.path.join(buttons_path, "buttons_broken4.png")
    self.buttons_gone1 = os.path.join(buttons_path, "buttons_gone1.png")
    self.buttons_gone2 = os.path.join(buttons_path, "buttons_gone2.png")
    self.buttons_gone3 = os.path.join(buttons_path, "buttons_gone3.png")

    # Accessories
    self.accessory1 = os.path.join(accessories_path, "accessory1.png")
    self.accessory2 = os.path.join(accessories_path, "accessory2.png")

    # Phase 1 body parts
    self.body1_p1 = os.path.join(phase_1_body_path, "body1.png")
    self.body2_p1 = os.path.join(phase_1_body_path, "body2.png")
    self.head1_p1 = os.path.join(phase_1_head_path, "head1.png")
    self.head2_p1 = os.path.join(phase_1_head_path, "head2.png")
    self.head3_p1 = os.path.join(phase_1_head_path, "head3.png")
    self.legs1_p1 = os.path.join(phase_1_legs_path, "legs1.png")

    # Phase 1.5 and 2.5 heads and bodies
    self.head1_p15 = os.path.join(phase_15_head_path, "head1.png")
    self.head2_p15 = os.path.join(phase_15_head_path, "head2.png")
    self.body1_p25 = os.path.join(phase_25_body_path, "body1.png")
    self.head1_p25 = os.path.join(phase_25_head_path, "head1.png")
    self.head2_p25 = os.path.join(phase_25_head_path, "head2.png")
    self.head3_p25 = os.path.join(phase_25_head_path, "head3.png")
    self.legs1_p25 = os.path.join(phase_25_legs_path, "legs1.png")

    # Phase 2 body parts
    self.body1_p2 = os.path.join(phase_2_body_path, "body1.png")
    self.head1_p2 = os.path.join(phase_2_head_path, "head1.png")
    self.head2_p2 = os.path.join(phase_2_head_path, "head2.png")
    self.legs1_p2 = os.path.join(phase_2_legs_path, "legs1.png")

    # Phase 3 body parts and animation frames (using list comprehensions for multiple frames)
    self.body_p3 = [os.path.join(phase_3_body_path, f"body{i}.png") for i in range(1, 18 + 1)]
    self.head_p3 = [os.path.join(phase_3_head_path, f"head{i}.png") for i in range(1, 5 + 1)]
    self.legs_p3 = [os.path.join(phase_3_legs_path, f"legs{i}.png") for i in range(1, 5 + 1)]
    self.left_arm_p3 = [os.path.join(phase_3_left_arm_path, f"left_arm{i}.png") for i in range(1, 3 + 1)]
    self.right_arm_p3 = [os.path.join(phase_3_right_arm_path, f"right_arm{i}.png") for i in range(1, 2 + 1)]
    self.animation_p3 = [os.path.join(phase_3_anim_path, f"animation{i}.png") for i in range(1, 8 + 1)]

    # Miscellaneous UI assets
    self.icon = os.path.join(icons_path, "icon.png")
    self.slices = [os.path.join(slices_path, f"Slice{i}.png") for i in range(1, 6 + 1)]

    # Soul color images
    self.blue = os.path.join(soul_path, "blue.png")
    self.broken_soul = os.path.join(soul_path, "broken_soul.png")
    self.purple = os.path.join(soul_path, "purple.png")
    self.red = os.path.join(soul_path, "red.png")

    # General UI screens
    self.end = os.path.join(images_path, "end.png")
    self.GameOver_image = os.path.join(images_path, "GameOver.png")
    self.menu_epic_sans = os.path.join(images_path, "menu_epic_sans.png")

    # Fonts used in the game
    fonts_path = os.path.join(assets_path, "fonts")
    self.DTM_Mono = os.path.join(fonts_path, "DTM-Mono.otf")
    self.Frisky = os.path.join(fonts_path, "Frisky.ttf")
    self.Mars_Needs_Cunnilingus = os.path.join(fonts_path, "Mars_Needs_Cunnilingus.ttf")

    # Sound paths
    sounds_path = os.path.join(assets_path, "sounds")
    sound_effects_path = os.path.join(sounds_path, "sound_effects")
    themes_path = os.path.join(sounds_path, "themes")

    # Sound effects
    self.black = os.path.join(sound_effects_path, "black.wav")
    self.broken = os.path.join(sound_effects_path, "broken.wav")
    self.charged = os.path.join(sound_effects_path, "charged.wav")
    self.damage = os.path.join(sound_effects_path, "damage.wav")
    self.dust = os.path.join(sound_effects_path, "dust.wav")
    self.end_sound = os.path.join(sound_effects_path, "end.wav")
    self.Heartbreaking = os.path.join(sound_effects_path, "Heartbreaking.wav")
    self.hit = os.path.join(sound_effects_path, "hit.wav")
    self.kamehameha = os.path.join(sound_effects_path, "kamehameha.wav")
    self.move_selection = os.path.join(sound_effects_path, "move selection.wav")
    self.notice = os.path.join(sound_effects_path, "notice.wav")
    self.ORA = os.path.join(sound_effects_path, "ORA.wav")
    self.ping = os.path.join(sound_effects_path, "ping.wav")
    self.resume = os.path.join(sound_effects_path, "resume.wav")
    self.road_roller_sound = os.path.join(sound_effects_path, "road_roller.wav")
    self.shoot = os.path.join(sound_effects_path, "shoot.wav")
    self.slash = os.path.join(sound_effects_path, "slash.wav")
    self.za_warudo = os.path.join(sound_effects_path, "za_warudo.wav")
    self.za_warudo_words = os.path.join(sound_effects_path, "za_warudo_words.wav")

    # Background music / themes
    self.GameOver_sound = os.path.join(themes_path, "GameOver.wav")
    self.Menu_theme = os.path.join(themes_path, "Menu_theme.mp3")
    self.plot_armor = os.path.join(themes_path, "plot_armor.mp3")
