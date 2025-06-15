import pygame as pg
import random


SIZE = (1000, 1000)
screen = pg.display.set_mode(SIZE)

FPS = 10

clock = pg.time.Clock()

def draw_signals():
    rot = pg.Rect(0, SIZE[1] / 2 + 100, 250, 40)
    rot.centerx = SIZE[0] / 2
    screen.fill("green")
    pg.draw.circle(screen, pg.Color("red"), (SIZE[0] / 2, SIZE[1] / 2), 300)
    pg.draw.circle(screen, pg.Color("white"), (SIZE[0] / 2 - 150, SIZE[1] / 2 - 100), 30)
    pg.draw.circle(screen, pg.Color("white"), (SIZE[0] / 2 + 150, SIZE[1] / 2 - 100), 30)
    pg.draw.arc(screen, pg.Color("white"), rot, 3.14, 6.28, 10)




while True:

    draw_signals()
    pg.display.flip()
    clock.tick(FPS)