import pygame
import sys
from settings import *
from level import Level  # Make sure Level includes all level components
from player import Player
from enemy import Enemy  # Ensure this is the updated Enemy class
from powerup import PowerUp  # Ensure this is the updated PowerUp class

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Platformer Game')
        self.clock = pygame.time.Clock()

        # Initialize Level and Player
        self.current_level = Level()  # Assumes Level class can handle its own initialization
        self.player = Player(self.current_level.platforms, self.current_level.enemies, self.current_level.powerups)

        # Initialize audio
        self.jump_sound = pygame.mixer.Sound('assets/sounds/jump.wav')
        self.collect_sound = pygame.mixer.Sound('assets/sounds/collect.wav')
        self.game_over_sound = pygame.mixer.Sound('assets/sounds/game_over.wav')

        self.score = 0
        self.lives = 3

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                        self.jump_sound.play()

            self.screen.fill(BG_COLOR)
            self.current_level.run()  # Run the current level
            self.player.update()  # Update player

            # Handle Collisions and Power-ups
            self.handle_collisions()

            # Rendering
            self.current_level.render(self.screen)  # Ensure level has a render method
            self.screen.blit(self.player.image, self.player.rect)

            # UI Display
            self.display_ui()

            pygame.display.update()
            self.clock.tick(FPS)

    def handle_collisions(self):
        # Implement collision handling
        # Check for power-ups, enemy collisions, etc.

    def display_ui(self):
        # Implement UI display for score, lives, etc.
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', 1, (10, 10, 10))
        lives_text = font.render(f'Lives: {self.lives}', 1, (10, 10, 10))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))

if __name__ == '__main__':
    game = Game()
    game.run()
