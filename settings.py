import pygame

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def toggle_fullscreen_mode():
    global SCREEN_WIDTH, SCREEN_HEIGHT, FULLSCREEN_MODE
    if FULLSCREEN_MODE:
        SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Windowed mode resolution
        FULLSCREEN_MODE = False
    else:
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h  # Fullscreen resolution
        FULLSCREEN_MODE = True

# Colors
BG_COLOR = (135, 206, 250)  # Sky blue background
PLAYER_COLOR = (255, 0, 0)  # Red
ENEMY_COLOR = (0, 0, 255)   # Blue

# Player settings
PLAYER_SPEED = 5
JUMP_HEIGHT = -15
GRAVITY = 1

# Enemy settings
ENEMY_SPEED = 2

# Game difficulty levels
DIFFICULTY = {'easy': 1, 'medium': 2, 'hard': 3}

# Control settings (keybindings)
CONTROLS = {
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'jump': pygame.K_SPACE
}

# Audio settings
MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.7
MUSIC_MUTE = False
SFX_MUTE = False

# Function to toggle music mute
def toggle_music_mute():
    global MUSIC_MUTE
    MUSIC_MUTE = not MUSIC_MUTE
    # Adjust the volume in the game as per the MUSIC_MUTE status

# Graphics settings
GRAPHICS_QUALITY = 'high'  # Options: 'low', 'medium', 'high'
BACKGROUND_DETAIL = 'high'
CHARACTER_ANIMATIONS = 'high'

# Dynamic resolution setting
def set_resolution(option_index):
    global SCREEN_WIDTH, SCREEN_HEIGHT
    RESOLUTION_OPTIONS = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]
    SCREEN_WIDTH, SCREEN_HEIGHT = RESOLUTION_OPTIONS[option_index]
    # Update game screen resolution here

# Performance settings
FRAME_RATE_CAP = 60
VSYNC_ENABLED = True

# UI settings
SHOW_HUD = True
HUD_COLOR = (0, 0, 0)  # Black
FONT_SIZE = 20
