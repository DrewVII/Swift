import pygame

class Spirball(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.attack = 30
        self.image = pygame.image.load('.\\assets\\pic\\spirball.png')
        self.image = pygame.transform.scale(self.image,(40, 20))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 50
        self.rect.y = player.rect.y

    def remove(self):
        self.player.all_spirball.remove(self)


    def move(self):
        self.rect.x += self.velocity

        for asteroid in self.player.game.check_collision(self, self.player.game.all_asteroid):
            asteroid.damage(self.attack)
            self.remove()

        if self.player.game.check_collision(self, self.player.game.all_asteroid):
            self.remove()

        if self.rect.x > 1280:
            self.remove()