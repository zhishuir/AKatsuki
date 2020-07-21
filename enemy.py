import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    energy = 2
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy1_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1700), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1700), \
                        randint(0,700)


class MidEnemy(pygame.sprite.Sprite):
    energy = 3
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy2_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1700), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1700), \
                        randint(0,700)


class BigEnemy(pygame.sprite.Sprite):
    energy = 4
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy3_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down4.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down5.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down6.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1700), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1700), \
                        randint(0,700)

class RareEnemy(pygame.sprite.Sprite):
    energy = 5
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy4.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy4_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy4_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy4_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy4_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy4_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = RareEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = RareEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)


class MianjuEnemy(pygame.sprite.Sprite):
    energy = 30
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy5.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy5_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy5_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy5_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy5_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy5_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MianjuEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MianjuEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)

class DidalaEnemy(pygame.sprite.Sprite):
    energy = 5
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy6.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy6.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy4_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy4_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy4_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy4_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 6
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = DidalaEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = DidalaEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
class JiaoduEnemy(pygame.sprite.Sprite):
    energy = 25
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy7.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy7.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy7_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy7_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy7_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy7_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = JiaoduEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = JiaoduEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)

class XieEnemy(pygame.sprite.Sprite):
    energy = 4
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy8.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy8.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy8_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy8_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy8_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy8_down4.png").convert_alpha(), \
            pygame.image.load("images/enemy8_down5.png").convert_alpha(), \
            pygame.image.load("images/enemy8_down6.png").convert_alpha(), \
            pygame.image.load("images/enemy8_down7.png").convert_alpha(), \
            pygame.image.load("images/enemy8_down8.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 3
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = XieEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = XieEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
class YouEnemy(pygame.sprite.Sprite):
    energy = 10
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy9.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy9.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy9_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy9_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy9_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy9_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 5
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = YouEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = YouEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
class XiaonanEnemy(pygame.sprite.Sprite):
    energy = 15
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy10.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy10.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy10_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy10_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy10_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy10_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 4
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = XiaonanEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = XiaonanEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
class TiandaoEnemy(pygame.sprite.Sprite):
    energy = 40
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy11.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy11.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy11_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy11_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy11_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy11_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 3
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1750), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = TiandaoEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = TiandaoEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1750), \
                        randint(0,700)
class GuijiaoEnemy(pygame.sprite.Sprite):
    energy = 50
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy12.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy12.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy12_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy12_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy12_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy12_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = GuijiaoEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = GuijiaoEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
class FeiduanEnemy(pygame.sprite.Sprite):
    energy = 100
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy13.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy13.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy13_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy13_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy13_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy13_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = FeiduanEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = FeiduanEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
class JueEnemy(pygame.sprite.Sprite):
    energy = 6
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy14.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy14.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy14_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy14_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy14_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy14_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 7
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = JueEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = JueEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,1500+1 * self.width), \
                        randint(0,700)
class KakaxiEnemy(pygame.sprite.Sprite):
    energy = 2
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy15.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy15_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy15_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy15_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy15_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy15_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 7
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,2000), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = KakaxiEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = KakaxiEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,2000), \
                        randint(0,700)

class FireEnemy(pygame.sprite.Sprite):
    energy = 2
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy16.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy16_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy16_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy16_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy16_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy16_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 8
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(1500,2000), \
                        randint(0,700)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = FireEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.right -= self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = FireEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(1500,2000), \
                        randint(0,700)

