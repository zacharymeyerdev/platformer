# Updating the Python code for 'enemy.py' with comprehensive features

enemy_py_code_v5 = """
import pygame
import random
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, movement_type='patrol', attack_range=200, health=100):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.movement_speed = 2
        self.movement_type = movement_type
        self.patrol_points = [x, x + 100]
        self.direction = 1
        self.attack_range = attack_range
        self.health = health
        self.is_stunned = False
        self.stun_duration = 0

    def patrol(self):
        if self.rect.x <= self.patrol_points[0] or self.rect.x >= self.patrol_points[1]:
            self.direction *= -1
        self.rect.x += self.movement_speed * self.direction

    def follow_player(self, player):
        if self.is_stunned:
            return
        player_distance = Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        if player_distance.length() <= self.attack_range:
            if player.rect.x < self.rect.x:
                self.rect.x -= self.movement_speed
            elif player.rect.x > self.rect.x:
                self.rect.x += self.movement_speed

    def random_movement(self):
        if self.is_stunned:
            return
        self.rect.x += random.choice([-1, 1]) * self.movement_speed
        self.rect.y += random.choice([-1, 1]) * self.movement_speed

    def attack_player(self, player):
        if self.is_stunned:
            return
        # Define attack logic (e.g., reducing player health)

    def update(self, player=None):
        if self.is_stunned:
            self.stun_duration -= 1
            if self.stun_duration <= 0:
                self.is_stunned = False
            return

        if self.movement_type == 'patrol':
            self.patrol()
        elif self.movement_type == 'follow':
            if player:
                self.follow_player(player)
                self.attack_player(player)
        elif self.movement_type == 'random':
            self.random_movement()

        # Additional behaviors like reacting to player's actions can be added here

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # Handle enemy defeat (e.g., disappearing or playing an animation)
            pass

    def stun(self, duration):
        self.is_stunned = True
        self.stun_duration = duration
"""
