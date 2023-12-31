import pygame
from time import time
from random import randint

pygame.init()

#висота та ширина
w_win = 700
h_win = 500

#кольори
blue = (125, 249, 255)
green = (62, 218, 148)
red = (255, 0, 0)
bleck = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 228, 107)

#створи вікно гри
window = pygame.display.set_mode((w_win, h_win))

FPS = 55
clock = pygame.time.Clock()

# супер клас
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
        self.speed = speed
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #безкінечний цикл

class Player(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image, speed)

    def move(self):
        move_ = pygame.key.get_pressed()   
        if move_[pygame.K_w]:
            if self.rect.y >= 0:
                self.rect.y += self.speed   
        if move_[pygame.K_s]:
            if self.rect.y <= 500:
                self.rect.y -= self.speed

menu = pygame.image.load('1636934079_67-bogatyr-club-p-chernii-ekran-fon-74.jpg')

game = True
finish = False

while game:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    if not finish:
        window.blit(menu(0, 0))

        #оброби подію «клік за кнопкою "Закрити вікно"»
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()
        pygame.display.update()
        clock.tick(FPS)