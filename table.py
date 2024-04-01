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
    color = THECOLORS["blue"]
    left=650
    top=60
    font = pygame.font.Font(None, 45)
    dlina=len(nam)
    for i in range(0,dlina):
        sc=str(scores[i])
        text = font.render(sc,1, color)
        background.blit(text, [left, top] )
        top=top+60
    top=60; left=370
    for i in range(0,dlina):
        nm=nam[i]
        text = font.render(nm,1, color)
        background.blit(text, [left, top] )
        top=top+60
    text = font.render("Press any key",True, color)
    background.blit(text, [150, 550])
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen,color,(360,50,380,56),3)
    pygame.draw.rect(screen,color,(360,106,380,56),3)
    pygame.draw.rect(screen,color,(360,162,380,56),3)
    pygame.draw.rect(screen,color,(360,218,380,56),3)
    pygame.draw.rect(screen,color,(360,274,380,56),3)
    pygame.display.flip()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False
show_rec(names)
