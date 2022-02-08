import pygame, sys
from pygame.color import THECOLORS
from pygame import font
pygame.init()
def zastavka():
    pygame.display.set_caption("Аэрохоккей")
    screen = pygame.display.set_mode([1071, 672])
    background = pygame.Surface(screen.get_size())
    background.fill([0,0,0])
    screen.blit(background, (0, 0))
    pygame.time.delay(10)
    pygame.display.flip()
    running = True
    r = 40
    studio_file = "studio.png"
    studio = pygame.image.load(studio_file)
    hockey2_file = "hockey2.jpg"
    hockey2 = pygame.image.load(hockey2_file)
    pygame.display.flip() 
    while running:
        screen.fill([255,255,255])
        if r>0:
            screen.blit(studio,[0,0])
            r=r-1
            pygame.time.delay(10)
        if r == 0:
            screen.blit(hockey2,[0,0])
        pygame.display.flip() 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False
    screen = pygame.display.set_mode([1071, 672])
