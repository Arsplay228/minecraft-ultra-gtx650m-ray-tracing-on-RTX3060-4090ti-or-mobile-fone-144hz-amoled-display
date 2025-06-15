import pygame as pg
import random

size = (500, 500)
screen = pg.display.set_mode(size)

FPS = 10

clock = pg.time.Clock()

rect_test = pg.Rect((120, 300, 60, 90))

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # screen.fill(pg.Color(r, g, b))
    screen.fill(pg.Color("White"))
    #
    # type = random.randint(0, 3)
    #
    # if type == 0:
    #     pg.draw.circle(screen, pg.Color(r, g, b), (100, 100), 50)
    # if type == 1:
    #     pg.draw.rect(screen, pg.Color(r, g, b), (200, 300, 70, 100))
    # if type == 2:
    #     pg.draw.ellipse(screen, pg.Color(r, g, b), (170, 20, 70, 100))
    # if type == 3:
    #     pg.draw.polygon(screen, pg.Color(r, g, b), ((200, 300), (30, 20), (30, 20)))
    # pg.draw.rect(screen, pg.Color("blue"), (140, 240, 80, 110))
    # pg.draw.rect(screen, pg.Color(r, g, b), (200, 300, 70, 100), 5)
    # pg.draw.rect(screen, pg.Color(r, g, b), rect_test)
    pg.draw.line(screen,pg.Color(r, g, b), (90, 20), (10, 100))
    pg.draw.line(screen, pg.Color(r, g, b), (180, 20), (10, 200), (10))

    pg.display.flip()
    clock.tick(FPS)