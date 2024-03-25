import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))  # Blue colored enemy
        self.rect = self.image.get_rect(midbottom=(600, 300))

    def update(self):
        # Basic enemy movement or behavior
