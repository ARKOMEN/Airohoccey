import pygame, random, sys,ZASTAVKA
import pickle
from pygame.color import THECOLORS
from pygame import font
##pygame.mixer.init()
pygame.init()
pygame.display.set_caption('аэрохоккей')
screenX = 1071
screenY = 672
screen = pygame.display.set_mode([screenX,screenY])
screen.fill([255,255,255])
ugol1_file = "ugol.png"
ugol_1=pygame.image.load(ugol1_file)
ugol3_file = "ugol3.png"
ugol_3=pygame.image.load(ugol3_file)
ugol4_file = "ugol4.png"
ugol_4=pygame.image.load(ugol4_file)
ugol2_file = "ugol2.png"
ugol_2=pygame.image.load(ugol2_file)
studio2_file = "studio2.png"
studio3_file = "studio3.png"
studio2 = pygame.image.load(studio2_file)
studio3 = pygame.image.load(studio3_file)
hockey1_file = "hockey1.jpg"
hockey1 = pygame.image.load(hockey1_file)
red_file= "hokkeyred.png"
hokkeyred =pygame.image.load(red_file)
blue_file= "hokkeyblue.png"
hokkeyblue =pygame.image.load(blue_file)
pause_file="pause.png"
pause=pygame.image.load(pause_file)
pause2_file="pause2.png"
pause2=pygame.image.load(pause2_file)
vopros_file="vopros.jpg"
vopros=pygame.image.load(vopros_file)
nastroykii_file="nastroykii.png"
nastroykii=pygame.image.load(nastroykii_file)
delete_file="delete.png"
delete=pygame.image.load(delete_file)
down1=0
down2=0
down3=0
down4=0
down5=0
i=0
pas=0
io=0
o=0
r= 40
j=0
gg=1
tyt1=0
tyt2=0
tyt3=0
tyt4=0
xd=0
yd=0
d=hockey1
my_down2 = False
my_down = False
my_downn = False
my_down1 = False
my_downnn=False
bal = False
pi = 3.14
xmn = 1072
ymn = 673

xb=535
yb=420
randoum = 2
dx = 1
dy = 1
do=0
fa=0
sole=0
cibemole=0
time = 60
timet =0
timer = 0
gole1 = 0
gole2 = 0
otbitie1 =0
otbitie2=0
pyt1 =0
pyt2 =0
iu1=0
iu2=0
#
hx1 = 0#движение
hy1 = 0
hx2 = 0
hy2 = 0
hhx1 = 126
hhy1 = 372
hhx2 = 829
hhy2 = 372
#



ZASTAVKA.zastavka()
running = True      
if i == 1:
    running = False
while running:
    randoum = random.randint(0,3)
    if randoum ==0:
        dx = -dx
        dy = dy
    if randoum ==1:
        dx = -dx
        dy = -dy
    if randoum ==2:
        dx = dx
        dy = dy
    if randoum ==3:
        dx = dx
        dy = -dy
    screen.blit(studio2,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            xm=0
            ym=0
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xm,ym)= pygame.mouse.get_pos()
            time = 60
            if xm >=453 and xm<=618 and ym >= 410 and ym <= 523:
               down1=1
            if xm >=453 and xm<=618 and ym >= 60 and ym <= 165:
                down2=1
            if xm >=453 and xm<=618 and ym >= 165 and ym <= 286:
                down3=1
            if xm >=453 and xm<=618 and ym >= 286 and ym <= 404:
                down4=1
            if xm >=453 and xm<=618 and ym >= 404 and ym <= 642:
                down5=1
            if down1==1:
                import my_help
                my_help.myhelp()
                down1=0
                break
            if down2==1:
                import one_player
                one_player.one_player()
                down2=0
                break
            if down3==1:
                import multiplayer
                multiplayer.multiplayer()
                down3=0
            if down4==1:
                running = False
            if down5==1:
                pickle_file = open('my_rec.pkl', 'rb')
                names = pickle.load(pickle_file)
                pickle_file.close()
                import table
                table.show_rec(names)
                down5=0
    if i == 1:
        running = False
    pygame.time.delay(10)
    pygame.display.flip()
pygame.quit()
