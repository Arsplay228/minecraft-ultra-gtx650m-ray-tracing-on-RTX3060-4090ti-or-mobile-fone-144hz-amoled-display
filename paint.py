import pygame as pg
import random
from sprites import *

pg.display.set_caption("Minecraft")
icon = pg.image.load("images/icon1.png")
pg.display.set_icon(icon)

pg.mixer.init()

SIZE = (1000, 1000)
screen = pg.display.set_mode(SIZE)

pg.mixer.music.load("sounds/fon.mp3")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play()
hello = pg.mixer.Sound("sounds/hello.mp3")

bees = pg.sprite.Group()
bee_range = random.randint(10, 35)
for bee in range(bee_range):
    bees.add(Bee(SIZE))





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

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 800)
    def update(self):
        if random.randint(0, 1):
            self.rect.x -= 1
        else:
            self.rect.x += 1

        if random.randint(0, 1):
            self.rect.y -= 1
        else:
            self.rect.y += 1
bees.add(Bee(screen))
sun = Sun(screen_size=SIZE)
steave = Steave(screen_size=SIZE)
cloud = Cloud(screen_size=SIZE, center=(150, 130), speed=1, direction="right")
cloud2 = Cloud(screen_size=SIZE, center=(780, 250), speed=1, direction="left")
clouds = pg.sprite.Group(cloud, cloud2)

FPS = 60
clock = pg.time.Clock()

grass = pg.Rect(0, SIZE[1] * 0.75, 2000, 500)

grass_image = pg.image.load("images/grass.png")
grass_image = pg.transform.scale(grass_image, (grass.width, grass.height))





steave_image = pg.image.load("images/steave.png")
steave_image = pg.transform.scale(steave_image, (SIZE[0] * 0.28, SIZE[1] * 0.5))
steave_rect = steave_image.get_rect(bottom=grass.top + 25)
steave_image1 = pg.transform.flip(steave_image, False, False)



background_immage = pg.image.load("images/cloud.jpg")
background_immage1 = pg.transform.scale(background_immage, (SIZE[0] / 0.50, SIZE[1] * 1.30))


def draw_sprites():
    screen.blit(background_immage1, (0, 0))
    screen.blit(sun.image, sun.rect)
    clouds.draw(screen)
    screen.blit(grass_image, grass)
    screen.blit(steave_image, steave.rect)
    bees.draw(screen)


def move(starship_rect, events):
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                starship_rect.x -= 1
            elif event.key == pg.K_d:
                starship_rect.x += 1
            elif event.key == pg.K_q:
                starship_rect.x -= 10
            elif event.key == pg.K_e:
                starship_rect.x += 10

def mouse_cloud():
    mouse_pos = pg.mouse.get_pos()
    mouse_keys = pg.mouse.get_pressed()

    if mouse_keys[0]:
        cloud.rect.center = mouse_pos
    elif mouse_keys[2]:
        cloud2.rect.center = mouse_pos

while True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                steave_rect.y -= 5
            elif event.key == pg.K_s:
                steave_rect.y += 5
            elif event.key == pg.K_SPACE:
                hello.play()
    move(sun.rect, events)
    bees.update()
    sun.update()
    clouds.update()
    steave.update(events)
    mouse_cloud()
    draw_sprites()
    pg.display.flip()
    clock.tick(FPS)