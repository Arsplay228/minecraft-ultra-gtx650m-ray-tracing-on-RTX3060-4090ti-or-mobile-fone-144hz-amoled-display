import random

import  pygame as pg



class Sun(pg.sprite.Sprite):
    def __init__(self, screen_size):
        pg.sprite.Sprite.__init__(self)
        self.screen_size = screen_size
        self.image = pg.image.load("images/sun.png")
        self.image = pg.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(center=(950, 50))
        self.moving_down = True
    def update(self):
        if self.moving_down:
            self.rect.y += 1
            if self.rect.bottom > self.screen_size[1]:
                self.moving_down = False
        else:
            self.rect.y -= 1
            if self.rect.top < 1:
                self.moving_down = True

class Steave(pg.sprite.Sprite):
    def __init__(self, screen_size):
        pg.sprite.Sprite.__init__(self)
        self.screen_size = screen_size
        self.image = pg.image.load("images/steave.png")
        self.image = pg.transform.scale(self.image, (self.screen_size[0] * 0.28, self.screen_size[1] * 0.5))
        self.rect = self.image.get_rect(bottom=self.screen_size[1] - 200)

    def update(self, events):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= 3
        if keys[pg.K_d]:
            self.rect.x += 3
        if keys[pg.K_w]:
            self.rect.y -= 3
        if keys[pg.K_s]:
            self.rect.y += 3

class Cloud(pg.sprite.Sprite):
    def __init__(self, screen_size, center, speed, direction):
        pg.sprite.Sprite.__init__(self)
        self.screen_size = screen_size
        self.speed = speed
        self.image = pg.image.load("images/skycloud.png")
        self.image = pg.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect(center=center)
        self.direction = direction

    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
            if self.rect.left > self.screen_size[0]:
                self.rect.right = 0
        elif self.direction == "left":
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.rect.left = self.screen_size[0]

class Bee(pg.sprite.Sprite):
    def __init__(self, screen_size):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/пчела.png")
        self.image = pg.transform.scale(self.image, (50, 50))
        self.screen_size = screen_size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_size[0])
        self.rect.y = random.randint(0, screen_size[1] - 200)
    def update(self):
        if random.randint(0, 1):
            self.rect.x -= 1
        else:
            self.rect.x += 1

        if random.randint(0, 1):
            self.rect.y -= 1
        else:
            self.rect.y += 1