import pygame
import random

class Star(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 20
        self.image = pygame.image.load('.\\assets\\pic\\star_bg.png')
        self.image = pygame.transform.scale(self.image,(5, 5))
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = random.randint(0, 720)
        
    def remove(self):
        self.game.all_stars.remove(self)

    def move(self):
        self.rect.x -= self.velocity

    def update(self):
        if self.rect.x < 0:
            self.remove()