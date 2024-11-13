import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.health = 10
        self.max_health = 10
        self.attack = 25
        self.game = game
        self.image = pygame.image.load('.\\assets\\pic\\asteroid1.png')
        self.image = pygame.transform.scale(self.image,(40, 20))
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = random.randint(0, 720)
        self.velocity = random.randint(10, 20)

    def remove(self):
        self.game.all_asteroid.remove(self)

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
                self.remove()

    def move(self):
        self.rect.x -= self.velocity
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(25)
            self.remove()

    def update(self):
        if self.rect.x < 0:
            self.remove()