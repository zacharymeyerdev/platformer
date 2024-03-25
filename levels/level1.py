import pygame
from level import Level, Platform, MovingPlatform, Enemy, PowerUp

class Level1(Level):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_platforms()
        self.init_enemies()
        self.init_powerups()
        self.init_puzzle()

    def init_ui(self):
        self.font = pygame.font.Font(None, 36)
        self.instructions = [
            ('Use arrow keys to move', (100, 450)),
            ('Jump on platforms', (350, 350)),
            ('Avoid enemies', (550, 250)),
            ('Collect items', (700, 200)),
            ('Solve puzzles to progress', (750, 150)),
            ('Time your jumps', (600, 270)),
            ('Watch out for enemies', (850, 220))
        ]

    def init_platforms(self):
        # Create static and moving platforms
        self.create_platform(100, 500, 200, 50)
        self.create_platform(350, 400, 150, 50)
        self.create_moving_platform(600, 300, 200, 50, (550, 650))
        self.create_platform(850, 250, 150, 50)

    def init_enemies(self):
        # Create enemy instance
        self.enemy = Enemy(860, 210)  # Positioned to provide a challenge
        self.enemies.add(self.enemy)

    def init_powerups(self):
        # Create power-up instances
        self.create_powerup(400, 350, 'coin')
        self.create_powerup(610, 250, 'heart')

    def init_puzzle(self):
        # Create puzzle platform
        self.puzzle_platform = MovingPlatform(750, 200, 100, 20, (700, 800))
        self.moving_platforms.add(self.puzzle_platform)

    def run(self):
        super().run()  # Running the base level run method

        # Display instructions
        for text, position in self.instructions:
            instruction_surf = self.font.render(text, True, (255, 255, 255))
            self.display_surface.blit(instruction_surf, position)
