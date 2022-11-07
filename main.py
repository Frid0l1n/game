import pygame
import sys
import time

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Hello")
screen = pygame.display.set_mode((900, 900), 0, 32)
white = (255,255,255)
pos = 0
framerate = 144

last_time = time.time()

while True:

    dt = time.time() -last_time
    dt *=144
    last_time = time.time()

    screen.fill((0,0,0))

    pos += 1 * dt

    r = pygame.Rect(pos, 200, 100, 100)
    pygame.draw.rect(screen, white, r)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()