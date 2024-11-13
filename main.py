# Lib
import pygame
import random
import os
from game import Game
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

pygame.init()

# Var
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND = '.\\assets\\pic\\background_stage2.jpg'
bg_img = pygame.image.load(BACKGROUND)
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

game = Game()

all_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()

screen_rect = screen.get_rect()

ADDASTEROID = pygame.USEREVENT + 1
pygame.time.set_timer(ADDASTEROID, 250)
ADDSTAR = pygame.USEREVENT + 2
pygame.time.set_timer(ADDSTAR, 100)

done = True

# Game 
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(".\\assets\\bgm\\EscapeThem.mp3")
pygame.mixer.music.play(loops=-1)

while done:

    screen.blit(bg_img,(0,0))
    
    for player in game.all_players:
        screen.blit(game.player.image,game.player.rect)
        
    game.player.all_spirball.draw(screen)

    game.all_asteroid.draw(screen)

    game.all_stars.draw(screen)

    game.player.update_health_bar(screen)

    game.player.update_energy_bar(screen)
    
    
    pressed_keys = pygame.key.get_pressed()
    game.player.update(pressed_keys)

    """if pygame.sprite.spritecollideany(game.player, game.all_asteroid):
        game.player.kill()
        done = False"""
    
    for spirball in game.player.all_spirball:
        spirball.move()

    for asteroid in game.all_asteroid:
        asteroid.move()

    for star in game.all_stars:
        star.move()

    for event in pygame.event.get():
    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = False
        
            elif event.key == K_SPACE:
                game.player.spirball_launch()

        elif event.type == ADDASTEROID:
            game.spawn_asteroid()

        elif event.type == ADDSTAR:
            game.spawn_star()

        elif event.type == pygame.QUIT:
            done = False

    game.player.rect.clamp_ip(screen_rect)
    clock.tick(300)

    pygame.display.flip()