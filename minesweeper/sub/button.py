import pygame
from .config import Config


class ButtonText(pygame.sprite.Sprite):
    def __init__(self, text="默认文本", font_size=5, xy=(0, 0)):
        super().__init__()
        self.x = 0
        self.y = 0
        self.text = text
        self.xy = xy
        self.font_size = font_size

        self.state = 0
        self.background_color = (200, 200, 200)
        self.normal_color = Config.button_color['nc']
        self.pressed_color = Config.button_color['sc']

        self.button_font = pygame.font.SysFont('Microsoft YaHei', self.font_size)
        self.image = self.button_font.render(self.text, True, (0, 0, 0), self.background_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.xy
        print("按钮 %s 初始化成功" % self.text)

    def draw(self, screen):
        self.update()
        self.image = self.button_font.render(self.text, True, (0, 0, 0), self.background_color)
        screen.blit(self.image, self.rect)

    def update(self):
        if self.state == 0:
            self.background_color = self.normal_color
        elif self.state == 1:
            self.background_color = self.pressed_color

    def setleft(self, left):
        self.rect.left = left

    def setright(self, right):
        self.rect.right = right

    def getleft(self):
        return self.rect.left

    def getright(self):
        return self.rect.right

    def settop(self, top):
        self.rect.top = top

    def setbottom(self, bottom):
        self.rect.bottom = bottom

    def gettop(self):
        return self.rect.top

    def getbottom(self):
        return self.rect.bottom


class ButtonTextGroup(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.member = []

    def draw(self, screen):
        for button in self.member:
            button.update()
            button.image = button.button_font.render(button.text, True, (0, 0, 0), button.background_color)
            screen.blit(button.image, button.rect)

    def add(self, *buttontuple):
        for button in buttontuple:
            self.member.append(button)
