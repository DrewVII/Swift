import pygame
from spirball import Spirball
from pygame.locals import (
    RLEACCEL,
    KEYDOWN,
    K_DOWN,
    K_UP,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    K_SPACE,
    QUIT,
)

# Var
WIDTH = 1280
HEIGHT = 720

# Class
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.health = 75
        self.max_health = 75
        self.energy = 75
        self.max_energy = 75
        self.attack = 10
        self.velocity = 5
        self.game = game
        self.all_spirball = pygame.sprite.Group()
        self.image = pygame.image.load('.\\assets\\pic\\mc_sprite.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def remove(self):
        self.game.all_players.remove(self)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 15, self.rect.y - 13, self.max_health, 3])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 15, self.rect.y - 13, self.health, 3])

    def update_energy_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 15, self.rect.y - 10, self.max_energy, 3])
        pygame.draw.rect(surface, (0, 190, 202), [self.rect.x - 15, self.rect.y - 10, self.energy, 3])

    def spirball_launch(self):
        if self.energy > 0:
            self.all_spirball.add(Spirball(self))
            self.dissipation(25)

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
                self.remove()

    def dissipation(self, amount):
        self.energy -= amount

    def update(self, pressed_keys): # Change to move()
        if pressed_keys[K_RIGHT]:
            self.rect.x += self.velocity
        if pressed_keys[K_LEFT]:
            self.rect.x -= self.velocity
        if pressed_keys[K_UP]:
            self.rect.y -= self.velocity
        if pressed_keys[K_DOWN]:
            self.rect.y += self.velocity