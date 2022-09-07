import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 1000,600

SCREEN = pygame.display.set_mode(SIZE)

RED_COLOR = 255,0,0
BLACK_COLOR = 0,0,0
WHITE_COLOR = 255,255,255
BLUE_COLOR = 0,0,255

SCREEN.fill(WHITE_COLOR)

rect_x = 0
rect_y = 0
rect_w = 50
rect_h = 50

while True:

    # Events
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()  # quit python

    # pygame.draw.rect(SCREEN, RED_COLOR, [rect_x, rect_y, rect_w, rect_h])

    for i in range(10):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        rect_x = (rect_w + 5) * i
        pygame.draw.rect(SCREEN, color, [rect_x, rect_y, rect_w, rect_h])

    # to update the screen
    pygame.display.flip()