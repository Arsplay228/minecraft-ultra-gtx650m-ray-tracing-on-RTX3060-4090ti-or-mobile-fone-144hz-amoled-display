import pygame as pg
import random


size = (1000, 1000)
screen = pg.display.set_mode(size)

FPS = 10

clock = pg.time.Clock()

def draw_signals():
    pg.draw.circle(screen, pg.Color("yellow"), (400, 400), 300)
    pg.draw.circle(screen, pg.Color("orange"), (500, 150), 20)
    pg.draw.circle(screen, pg.Color("orange"), (600, 340), 60)
    pg.draw.circle(screen, pg.Color("orange"), (200, 500), 60)
    pg.draw.circle(screen, pg.Color("orange"), (400, 370), 20)
    pg.draw.circle(screen, pg.Color("orange"), (300, 200), 50)
    pg.draw.circle(screen, pg.Color("orange"), (500, 640), 20)


while True:

    draw_signals()
    pg.display.flip()
    clock.tick(FPS)