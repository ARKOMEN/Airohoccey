import pygame, sys
from pygame.color import THECOLORS
from pygame import font
pygame.init()
def myhelp():
     pygame.display.set_caption("аэрохоккей")
     screen = pygame.display.set_mode([1071, 672])
     background = pygame.Surface(screen.get_size())
     background.fill([0,0,0])
     color = THECOLORS["white"]
     top=10; left=20
     font = pygame.font.Font(None, 20)
     my_file = open('HELP.txt', 'r')#Открываем файл для чтения
     lines = my_file.readlines()# Записываем строки из файла в список lines
     my_file.close()
     dlina=len(lines)#Это количество строк
     for i in range(0,dlina):
          ln=lines[i]
          dl=len(ln)-1 #Удаляем символ конца строки
          ln=ln[0:dl]
          text = font.render(ln,1, color)
          background.blit(text, [left, top] )
          top=top+20
     text = font.render("чтобы продолжить, нажмите правую кнопку мыши",True, color)
     background.blit(text, [150, 550])
     screen.blit(background, (0, 0))
     pygame.display.flip()  
     running=True
     while running:
         for event in pygame.event.get():
              if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 3:
                        running = False
     screen = pygame.display.set_mode([1071, 672])
