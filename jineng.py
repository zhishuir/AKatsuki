import pygame

class Zhengqi(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/use_zhengqi.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 30
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.right += self.speed

        if self.rect.right < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Baowei(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/use_baowei.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 10
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.right += self.speed

        if self.rect.right < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
