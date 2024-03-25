import pygame
from settings import *
from enemy import Enemy  # Assuming an enemy class is defined
from powerup import PowerUp  # Assuming a powerup class is defined

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class MovingPlatform(Platform):
    def __init__(self, x, y, width, height, movement_range, color=(123, 104, 238)):
        super().__init__(x, y, width, height, color)
        self.movement_range = movement_range
        self.movement_direction = 1

    def update(self):
        self.rect.x += self.movement_direction
        if self.rect.x > self.movement_range[1] or self.rect.x < self.movement_range[0]:
            self.movement_direction *= -1

class Trap(Platform):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, (255, 0, 0))  # Red color for traps

class PuzzleElement(Platform):
    def __init__(self, x, y, width, height, puzzle_type):
        color = (0, 255, 0) if puzzle_type == 'switch' else (255, 255, 0)
        super().__init__(x, y, width, height, color)
        self.puzzle_type = puzzle_type

    def solve_puzzle(self, player):
        # Puzzle solving logic here

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.platforms = pygame.sprite.Group()
        self.moving_platforms = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.puzzles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Example level layout
        self.create_platform(100, 500, 200, 50)
        self.create_platform(350, 400, 200, 50)
        self.create_moving_platform(600, 300, 200, 50, (550, 650))
        self.create_trap(750, 250, 100, 20)
        self.create_puzzle(900, 200, 100, 50, 'switch')

        # Add enemies, power-ups, etc.

    def create_platform(self, x, y, width, height):
        platform = Platform(x, y, width, height)
        self.platforms.add(platform)

    def create_moving_platform(self, x, y, width, height, movement_range):
        moving_platform = MovingPlatform(x, y, width, height, movement_range)
        self.moving_platforms.add(moving_platform)

    def create_trap(self, x, y, width, height):
        trap = Trap(x, y, width, height)
        self.traps.add(trap)

    def create_puzzle(self, x, y, width, height, puzzle_type):
        puzzle = PuzzleElement(x, y, width, height, puzzle_type)
        self.puzzles.add(puzzle)

    def run(self):
        for group in [self.platforms, self.moving_platforms, self.traps, self.puzzles]:
            for element in group:
                self.display_surface.blit(element.image, element.rect)
                if isinstance(element, MovingPlatform):
                    element.update()
        # Additional level logic, enemy updates, etc.
