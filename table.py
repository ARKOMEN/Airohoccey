import pickle
import pygame, sys
from pygame.color import THECOLORS
from pygame import font
pygame.init()
names=["Unknown","Unknown","Unknown","Unknown","Unknown",0,0,0,0,0,]
pickle_file = open('my_rec.pkl', 'rb')
names = pickle.load(pickle_file)#список содеожит имена и очки
pickle_file.close()
def show_rec(names):
    nam=names[0:5]
    scores=names[5:]
    pygame.display.set_caption("Аэрохоккей")
    screen = pygame.display.set_mode([1071, 672])
    background = pygame.Surface(screen.get_size())
    background.fill([255,255,255])
    color = THECOLORS["red"]
    left=300
    top=10
    font = pygame.font.Font(None, 32)
    dlina=len(nam)
    for i in range(0,dlina):
        sc=str(scores[i])
        text = font.render(sc,1, color)
        background.blit(text, [left, top] )
        top=top+40
    top=10; left=20
    for i in range(0,dlina):
        nm=nam[i]
        text = font.render(nm,1, color)
        background.blit(text, [left, top] )
        top=top+40
    text = font.render("Press any key",True, color)
    background.blit(text, [150, 550])
    screen.blit(background, (0, 0))
    pygame.display.flip()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False
