import pygame
from player import Player
from asteroid import Asteroid
from star import Star

class Game:
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        
        self.all_stars = pygame.sprite.Group()
        self.spawn_star()
        
        self.asteroid = Asteroid(self)
        self.all_asteroid = pygame.sprite.Group()
        self.spawn_asteroid()

    def spawn_star(self):
        star = Star(self)
        self.all_stars.add(star)

    def spawn_asteroid(self):
        asteroid = Asteroid(self)
        self.all_asteroid.add(asteroid)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)