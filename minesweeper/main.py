import sys
import pygame
import random
import pymysql
from sub.config import Config
from sub.button import ButtonText, ButtonTextGroup
import time


def screen_create(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(Config.title)
    # icon图标
    icon = pygame.image.load(Config.images['icon'])
    pygame.display.set_icon(icon)
    return screen


class Block(pygame.sprite.Sprite):

    def __init__(self, xy=(35, 35)):
        super().__init__()
        self.x = xy[0]
        self.y = xy[1]
        self.xy = xy
        self.image = pygame.image.load(Config.images['unknown'])
        self.rect = self.image.get_rect()
        self.state = 'unknown'
        self.hide = '0'

    def covered(self):
        self.state = self.hide

    def draw(self, screen):
        self.image = pygame.image.load(Config.images[self.state])
        screen.blit(self.image, self.rect)


class Map:
    def __init__(self, size):
        self.size = size

        pygame.init()

    def create(self):
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                pass

    def draw(self, screen):
        pass


class Timer:
    def __init__(self):
        self.time_start = time.time()


class History:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = screen_create((800, 600))

        # 按钮
        button_group = ButtonTextGroup()
        button_1 = ButtonText(Config.button_text['1'],
                              Config.button_parameter['f'])
        button_2 = ButtonText(Config.button_text['2'],
                              Config.button_parameter['f'])
        button_3 = ButtonText(Config.button_text['3'],
                              Config.button_parameter['f'])
        button_1.setleft(0)
        button_1.settop(0)
        button_2.setleft(button_1.getright() + 1)
        button_2.settop(0)
        button_3.setleft(button_2.getright() + 1)
        button_3.settop(0)

        button_group.add(button_1, button_2, button_3)
        # 方块
        block_group = pygame.sprite.Group()

        running = True
        while running:

            screen.fill((255, 255, 255))
            button_group.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_1.rect.collidepoint(event.pos):
                        button_1.state = 1
                    if button_2.rect.collidepoint(event.pos):
                        button_2.state = 1
                    if button_3.rect.collidepoint(event.pos):
                        button_3.state = 1

                elif event.type == pygame.MOUSEBUTTONUP:
                    button_1.state = 0
                    button_2.state = 0
                    button_3.state = 0

            clock.tick(Config.FPS)
            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
