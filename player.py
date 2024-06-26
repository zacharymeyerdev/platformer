# Updating the Python code for 'player.py' with comprehensive features

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, platforms, enemies, powerups):
        super().__init__()
        # Load actual sprite sheets or individual sprites here
        self.sprites = {
            'idle': self.load_sprites('idle_spritesheet.png', 4),
            'jump': self.load_sprite('jump_sprite.png'),
            'walk': self.load_sprites('walk_spritesheet.png', 6),
            'powerup': self.load_sprite('powerup_sprite.png')
        }

        self.current_sprite = 'idle'
        self.image = self.sprites[self.current_sprite][0]
        self.rect = self.image.get_rect(midbottom=(400, 300))
        self.gravity = 0
        self.speed = 5
        self.jump_speed = -15
        self.platforms = platforms
        self.enemies = enemies
        self.powerups = powerups
        self.is_jumping = False
        self.is_powered_up = False
        self.walking_frame = 0
        self.animation_frame = 0
        self.animation_speed = 0.1

    def load_sprite(self, path):
        return pygame.image.load(path).convert_alpha()

    def load_sprites(self, path, num_sprites):
        # Load a spritesheet and divide it into individual frames
        # Assuming the spritesheet is in a horizontal layout
        sheet = self.load_sprite(path)
        width = sheet.get_width() // num_sprites
        height = sheet.get_height()
        return [sheet.subsurface(pygame.Rect(i * width, 0, width, height)) for i in range(num_sprites)]

    def input(self):
        keys = pygame.key.get_pressed()
        moving = False
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            moving = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            moving = True

        # Animation Handling
        self.animation_frame += self.animation_speed
        if moving:
            self.walking_frame = int(self.animation_frame) % len(self.sprites['walk'])
            self.current_sprite = 'walk'
        elif self.is_jumping:
            self.current_sprite = 'jump'
            self.walking_frame = 0
        else:
            if self.is_powered_up:
                self.current_sprite = 'powerup'
            else:
                self.current_sprite = 'idle'
            self.walking_frame = int(self.animation_frame) % len(self.sprites[self.current_sprite])

        self.image = self.sprites[self.current_sprite][self.walking_frame]

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        self.collide_with_platforms()

    def jump(self):
        if not self.is_jumping:
            self.gravity = self.jump_speed
            self.is_jumping = True

    def collide_with_platforms(self):
        for platform in self.platforms:
            if self.rect.colliderect(platform.rect):
                if self.gravity > 0:
                    self.rect.bottom = platform.rect.top
                    self.gravity = 0
                    self.is_jumping = False

    def update(self):
        self.input()
        self.apply_gravity()
        self.check_collisions()
        self.animate()

    def check_collisions(self):
        # Check for power-up collisions
        powerup_hits = pygame.sprite.spritecollide(self, self.powerups, True)
        if powerup_hits:
            self.is_powered_up = True  # Example of a power-up effect
        # Check for enemy collisions
        enemy_hits = pygame.sprite.spritecollide(self, self.enemies, False)
        if enemy_hits:
            # Handle player-enemy collision
            pass

    def animate(self):
        # Update the walking_frame based on animation_frame and current_sprite
        self.image = self.sprites[self.current_sprite][int(self.animation_frame) % len(self.sprites[self.current_sprite])]
        self.animation_frame += self.animation_speed
