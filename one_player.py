import pygame, random, sys
import pickle 
from pygame.color import THECOLORS
from pygame import font
pygame.init()
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
b1xa=[-24,22]#координаты бит в 1 и 2 положении
b1ya =[580,555]
b1xb=[0,48]
b1yb=[563,555]
b1xc=[44,48]
b1yc=[626,635]
b1xd=[23,22]
b1yd=[644,635]
b1xe=[-24,22]
b1ye=[580,555]
b4xa=[-24,22]
b4ya =[260,285]
b4xb=[0,48]
b4yb=[277,285]
b4xc=[44,48]
b4yc=[214,205]
b4xd=[23,22]
b4yd=[196,205]
b4xe=[-24,22]
b4ye=[260,285]
b5xa=[1095,1049]
b5ya =[580,555]
b5xb=[1071,1023]
b5yb=[563,555]
b5xc=[1027,1023]
b5yc=[626,635]
b5xd=[1048,1049]
b5yd=[644,635]
b5xe=[1095,1049]
b5ye=[580,555]
b8xa=[1095,1049]
b8ya =[260,285]
b8xb=[1071,1023]
b8yb=[277,285]
b8xc=[1027,1023]
b8yc=[214,205]
b8xd=[1048,1049]
b8yd=[196,205]
b8xe=[1095,1049]
b8ye=[260,285]
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
studio3_file = "studio3.png"
studio3 = pygame.image.load(studio3_file)

def nastroyki():
    screen.blit(studio3,[0,0])
    font = pygame.font.Font(None, 25)
    textn = font.render("чтобы вернуться в меню, нажмите правую кнопку мыши",True, THECOLORS ["black"])
    screen.blit(textn,[325,650])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            my_down = False

def bita():#создание бит
    pygame.draw.circle(screen, THECOLORS['blue'],[35,635], 14, 0)
    pygame.draw.circle(screen, THECOLORS['blue'],[35,205], 14, 0)
    pygame.draw.circle(screen, THECOLORS['red'],[1036,635], 14, 0)
    pygame.draw.circle(screen, THECOLORS['red'],[1036,205], 14, 0)
    pygame.draw.polygon(screen, THECOLORS['blue'], [[b1xa[do],b1ya[do]], [b1xb[do],b1yb[do]], [b1xc[do],b1yc[do]], [b1xd[do],b1yd[do]], [b1xe[do],b1ye[do]]])
##    pygame.draw.polygon(screen, THECOLORS['blue'], [[b2xa[re],b2ya[re]], [b2xb[re],b2yb[re]], [b2xc[re],b2yc[re]], [b2xd[re],b2yd[re]], [b2xe[re],b2ye[re]]])
##    pygame.draw.polygon(screen, THECOLORS['blue'], [[b3xa[mi],b3ya[mi]], [b3xb[mi],b3yb[mi]], [b3xc[mi],b3yc[mi]], [b3xd[mi],b3yd[mi]], [b3xe[mi],b3ye[mi]]])
    pygame.draw.polygon(screen, THECOLORS['blue'], [[b4xa[fa],b4ya[fa]], [b4xb[fa],b4yb[fa]], [b4xc[fa],b4yc[fa]], [b4xd[fa],b4yd[fa]], [b4xe[fa],b4ye[fa]]])
    pygame.draw.polygon(screen, THECOLORS['red'], [[b5xa[sole],b5ya[sole]], [b5xb[sole],b5yb[sole]], [b5xc[sole],b5yc[sole]], [b5xd[sole],b5yd[sole]], [b5xe[sole],b5ye[sole]]])
##    pygame.draw.polygon(screen, THECOLORS['red'], [[b6xa[li],b6ya[li]], [b6xb[li],b6yb[li]], [b6xc[li],b6yc[li]], [b6xd[li],b6yd[li]], [b6xe[li],b6ye[li]]])
##    pygame.draw.polygon(screen, THECOLORS['red'], [[b7xa[ci],b7ya[ci]], [b7xb[ci],b7yb[ci]], [b7xc[ci],b7yc[ci]], [b7xd[ci],b7yd[ci]], [b7xe[ci],b7ye[ci]]])
    pygame.draw.polygon(screen, THECOLORS['red'], [[b8xa[cibemole],b8ya[cibemole]], [b8xb[cibemole],b8yb[cibemole]], [b8xc[cibemole],b8yc[cibemole]], [b8xd[cibemole],b8yd[cibemole]], [b8xe[cibemole],b8ye[cibemole]]])
    #pygame.draw.circle(screen, THECOLORS['red'],[1069,526], 14, 0)
    #pygame.draw.circle(screen, THECOLORS['blue'],[1,524], 14, 0)
    #pygame.draw.circle(screen, THECOLORS['blue'],[1,316], 14, 0)

def ball_move():#движение шайбы
    global xb, yb, randoum,dx, dy, time,gg,otbitie2,otbitie1,iu1,iu2,hx1,hy1,hx2,hy2
    pygame.draw.circle(screen, THECOLORS['black'],[xb,yb], 20, 0)
    if gg ==1:
            xb = xb + dx
            yb = yb + dy

    if time == 0:
        dx = 0
        dy = 0
    if xb - 14 <= hhx1+132 and xb - 14 >= hhx1+117 and yb>=hhy1+30 and yb <= hhy1+127 and otbitie1 == 1:
        dx=hx1
        dy=hy1
        xb = xb + dx
        yb = yb + dy
        gg=0
    if xb + 14 >= hhx2-5 and xb + 14 <= hhx2+10 and yb>=hhy2+30 and yb <= hhy2+127 and otbitie2 == 1:
        dx=hx2
        dy=hy2
        xb = xb + dx
        yb = yb + dy
        gg=0
    if otbitie1 == 0 and iu1==1:
        dx=1
        dy = 0
        iu1=0
        gg=1
    if otbitie2 == 0 and iu2==1:
        dx=-1
        dy = 0
        iu2=0
        gg=1
def ball_proverka():#проверка шайбы, отбитие от бит и закругленных углов
    global xb,tyt1,tyt2,tyt3,tyt4, yb,do,fa,sole,cibemole, randoum,dx, dy,xd, yd,do,b1xa, b1ya, b1xb, b1yb, b1xc, b1yc, b1xd, b1yd, b1xe, b1ye, b4xa, b4ya, b4xb, b4yb, b4xc, b4yc, b4xd, b4yd, b4xe, b4ye, b5xa, b5ya, b5xb, b5yb, b5xc, b5yc, b5xd, b5yd, b5xe, b5ye, b8xa, b8ya, b8xb, b8yb, b8xc, b8yc, b8xd, b8yd, b8xe, b8ye

#############################################################################################################################################################################################отбитие от хоккеистов
    if gg == 1:
        if xb - 14 <= hhx1+93 and xb - 14 >= hhx1+83 and yb>=hhy1+30 and yb <= hhy1+127:
            dx=-dx
            dy = -hy1
            tyt1=0
            tyt2=0
            tyt3=0
            tyt4=0
            dx=1
        if xb + 14 >= hhx2+34 and xb + 14 <= hhx2+44 and yb>=hhy2+30 and yb <= hhy2+127:
            dy =hy2
            tyt1=0
            tyt2=0
            tyt3=0
            tyt4=0
            dx=-1
        if xb + 14 >= hhx1 and xb + 14 <= hhx1 + 5 and yb>=hhy1+30 and yb <= hhy1+127:
            dx=-dx
            dy =-hy1
            tyt1=0
            tyt2=0
            tyt3=0
            tyt4=0
        if xb - 14 <= hhx2 + 100 and xb - 14 >= hhx2 + 95 and yb>=hhy2+30 and yb <= hhy2+127:
            dx=-dx
            dy =hy2
            tyt1=0
            tyt2=0
            tyt3=0
            tyt4=0
        if yb +14 >=hhy1+70 and yb +14 <=hhy1+75 and xb >= hhx1 and xb <= hhx1 + 93:
            dy = - dy
            tyt1=0
            tyt2=0
            tyt3=0
            tyt4=0
        if yb -14 <=hhy1+127 and yb +14 >=hhy1+112 and xb >= hhx1 and xb <= hhx1 + 93:
            dy = - dy
            tyt1=0
            tyt2=0
            tyt3=0
            tyt4=0
        if yb +14 >=hhy2+70 and yb +14 <=hhy2+75 and xb >= hhx2 and xb <= hhx2 + 93:
            dy = - dy
            tyt1=0
            tyt2=0
            tyt3=0
            tyt4=0
        if yb -14 <=hhy2+127 and yb +14 >=hhy2+112 and xb >= hhx2 and xb <= hhx2 + 93:
            dy = - dy
            tyt1=0
            tyt2=0
            tyt3=0
            tyt4=0

    if (yb+14) >= screenY:#отбитие от верхней и нижней стороны поля
        dy= - dy
    if (yb-14) <= 168:
        dy = -dy
    if xb-14<=0 and yb <=screenY and yb>= 499:
        dx=-dx
    if xb-14<=0 and yb <=337 and yb>= 168:
        dx=-dx
    if xb+14>=1071 and yb <=screenY and yb>= 499:
        dx=-dx
    if xb+14>=1071 and yb <=337 and yb>= 168:
        dx=-dx
    #турбо режим
    if tyt1 ==1:
        dx = 10
        dy = -2
        if xb <=5 or xb >=1066:
            dx = 1
            dy = -1
            tyt1=0
    if tyt2 ==1:
        dx = 10
        dy = 2
        if xb <=5 or xb >=1066:
            dx = 1
            dy = 1
            tyt2=0
    if tyt3 ==1:
        dx = -10
        dy = -2
        if xb <=5 or xb >=1066:
            dx = -1
            dy = -1
            tyt3=0
    if tyt4 ==1:
        dx = -10
        dy = 2
        if xb <=5 or xb >=1066:
            dx = -1
            dy = 1
            tyt4=0
    ################################################################################################################################################################################################################# УГОЛ №4 ЛЕВЫЙ НИЖНИЙ

    if xb - 14 <= 44 and yb + 14 == 626:#изменено
        dx = - dx
    if xb - 14 <= 45 and yb + 14 == 627:
        dx = - dx
    if xb - 14 <= 47 and yb + 14 == 628:
        dx = - dx
    if xb - 14 <= 48 and yb + 14 == 629:
        dx = - dx
    if xb - 14 <= 49 and yb + 14 == 630:
        dx = - dx
    if xb - 14 <= 51 and yb + 14 == 631:
        dx = - dx
    if xb - 14 <= 52 and yb + 14 == 632:
        dx = - dx
    if xb - 14 <= 53 and yb + 14 == 633:
        dx = - dx
    if xb - 14 <= 55 and yb + 14 == 634:
        dx = - dx
    if xb - 14 <= 56 and yb + 14 == 635:
        dx = - dx
    if xb - 14 <= 57 and yb + 14 == 636:
        dx = - dx
    if xb - 14 <= 59 and yb + 14 == 637:
        dx = - dx
    if xb - 14 <= 60 and yb + 14 == 638:
        dx = - dx
    if xb - 14 <= 61 and yb + 14 == 639:
        dx = - dx
    if xb - 14 <= 63 and yb + 14 == 640:
        dx = - dx
    if xb - 14 <= 64 and yb + 14 == 641:
        dx = - dx
    if xb - 14 <= 65 and yb + 14 == 642:
        dx = - dx
    if xb - 14 <= 67 and yb + 14 == 643:
        dx = - dx
    if xb - 14 <= 68 and yb + 14 == 644:
        dx = - dx
    if xb - 14 <= 69 and yb + 14 == 645:
        dx = - dx
    if xb - 14 <= 71 and yb + 14 == 646:
        dx = - dx
    if xb - 14 <= 72 and yb + 14 == 647:
        dx = - dx
    if xb - 14 <= 73 and yb + 14 == 648:
        dx = - dx
    if xb - 14 <= 75 and yb + 14 == 649:
        dx = - dx
    if xb - 14 <= 76 and yb + 14 == 650:
        dx = - dx
    if xb - 14 <= 77 and yb + 14 == 651:
        dx = - dx
    if xb - 14 <= 79 and yb + 14 == 652:
        dx = - dx
    if xb - 14 <= 81 and yb + 14 == 653:
        dx = - dx
    if xb - 14 <= 82 and yb + 14 == 654:
        dx = - dx
    if xb - 14 <= 83 and yb + 14 == 655:
        dx = - dx
    if xb - 14 <= 85 and yb + 14 == 656:
        dx = - dx
    if xb - 14 <= 86 and yb + 14 == 657:
        dx = - dx
    if xb - 14 <= 87 and yb + 14 == 658:
        dx = - dx
    if xb - 14 <= 89 and yb + 14 == 659:
        dx = - dx
    if xb - 14 <= 90 and yb + 14 == 660:
        dx = - dx
    if xb - 14 <= 91 and yb + 14 == 661:
        dx = - dx
    if xb - 14 <= 93 and yb + 14 == 662:
        dx = - dx
    if xb - 14 <= 94 and yb + 14 == 663:
        dx = - dx
    if xb - 14 <= 95 and yb + 14 == 664:
        dx = - dx
    if xb - 14 <= 97 and yb + 14 == 665:
        dx = - dx
    if xb - 14 <= 98 and yb + 14 == 666:
        dx = - dx
    if xb - 14 <= 99 and yb + 14 == 667:
        dx = - dx
    if xb - 14 <= 101 and yb + 14 == 668:
        dx = - dx
    if xb - 14 <= 102 and yb + 14 == 669:
        dx = - dx
    if xb - 14 <= 103 and yb + 14 == 670:
        dx = - dx
    if xb - 14 <= 105 and yb + 14 == 671:
        dx = - dx
    if xb - 14 <= 106 and yb + 14 == 671:
        dx = - dx


    if do ==1:#отбитие от второй биты от ворот, если бита находится в положении 2
        if (yb+14) >= b1ya[do] and xb - 14 <= b1xb[do]:
            dy=-dy
        if xb - 14 <= b1xb[do] and yb+14 >=b1yb[do] and yb <= b1yc[do]:
            dx=-dx
            tyt1=1
    if do == 0:#отбитие от второй биты от ворот, если бита находится в положении 1
        if xb - 14 <= 1 and yb +14 >= 563 and yb +14 < 566:
            dx= - dx
        if xb - 14 <= 3 and xb - 14 > 1 and yb +14 >= 566 and yb +14 < 569:
            dx= - dx
        if xb - 14 <= 5 and xb - 14 > 3 and yb +14 >= 569 and yb +14 < 572:
            dx= - dx
        if xb - 14 <= 7 and xb - 14 > 5 and yb +14 >= 572 and yb +14 < 575:
            dx= - dx
        if xb - 14 <= 9 and xb - 14 > 7 and yb +14 >= 575 and yb +14 < 578:
            dx= - dx
        if xb - 14 <= 11 and xb - 14 > 9 and yb +14 >= 578 and yb +14 < 581:
            dx= - dx
        if xb - 14 <= 13 and xb - 14 > 11 and yb +14 >= 581 and yb +14 < 584:
            dx= - dx
        if xb - 14 <= 15 and xb - 14 > 13 and yb +14 >= 584 and yb +14 < 587:
            dx= - dx
        if xb - 14 <= 17 and xb - 14 > 15 and yb +14 >= 587 and yb +14 < 590:
            dx= - dx
        if xb - 14 <= 19 and xb - 14 > 17 and yb +14 >= 590 and yb +14 < 593:
            dx= - dx
        if xb - 14 <= 21 and xb - 14 > 19 and yb +14 >= 593 and yb +14 < 596:
            dx= - dx
        if xb - 14 <= 23 and xb - 14 > 21 and yb +14 >= 596 and yb +14 < 599:
            dx= - dx
        if xb - 14 <= 25 and xb - 14 > 23 and yb +14 >= 599 and yb +14 < 602:
            dx= - dx
        if xb - 14 <= 27 and xb - 14 > 25 and yb +14 >= 602 and yb +14 < 605:
            dx= - dx
        if xb - 14 <= 29 and xb - 14 > 27 and yb +14 >= 605 and yb +14 < 608:
            dx= - dx
        if xb - 14 <= 31 and xb - 14 > 29 and yb +14 >= 608 and yb +14 < 611:
            dx= - dx
        if xb - 14 <= 33 and xb - 14 > 31 and yb +14 >= 611 and yb +14 < 614:
            dx= - dx
        if xb - 14 <= 35 and xb - 14 > 33 and yb +14 >= 614 and yb +14 < 617:
            dx= - dx
        if xb - 14 <= 37 and xb - 14 > 35 and yb +14 >= 617 and yb +14 < 620:
            dx= - dx
        if xb - 14 <= 39 and xb - 14 > 37 and yb +14 >= 620 and yb +14 < 623:
            dx= - dx
        if xb - 14 <= 41 and xb - 14 > 39 and yb +14 >= 623 and yb +14 < 626:
            dx= - dx

            # Далее идет проверка других углов, по структуре она отличается от выше идушей только координатами и знаками.



        ############################################################################################################################################################################################################# УГОЛ № 3 ЛЕВЫЙ ВЕРХНИЙ

    if xb - 14 <= 44 and yb - 14 == 214:# если шайба летит вверх
        dx = - dx
    if xb - 14 <= 45 and yb - 14 == 213:
        dx = - dx
    if xb - 14 <= 47 and yb - 14 == 212:
        dx = - dx
    if xb - 14 <= 48 and yb - 14 == 211:
        dx = - dx
    if xb - 14 <= 49 and yb - 14 == 210:
        dx = - dx
    if xb - 14 <= 51 and yb - 14 == 209:
        dx = - dx
    if xb - 14 <= 52 and yb - 14 == 208:
        dx = - dx
    if xb - 14 <= 53 and yb - 14 == 207:
        dx = - dx
    if xb - 14 <= 55 and yb - 14 == 206:
        dx = - dx
    if xb - 14 <= 56 and yb - 14 == 205:
        dx = - dx
    if xb - 14 <= 57 and yb - 14 == 204:
        dx = - dx
    if xb - 14 <= 59 and yb - 14 == 203:
        dx = - dx
    if xb - 14 <= 60 and yb - 14 == 202:
        dx = - dx
    if xb - 14 <= 61 and yb - 14 == 201:
        dx = - dx
    if xb - 14 <= 63 and yb - 14 == 200:
        dx = - dx
    if xb - 14 <= 64 and yb - 14 == 199:
        dx = - dx
    if xb - 14 <= 65 and yb - 14 == 198:
        dx = - dx
    if xb - 14 <= 67 and yb - 14 == 197:
        dx = - dx
    if xb - 14 <= 68 and yb - 14 == 196:
        dx = - dx
    if xb - 14 <= 69 and yb - 14 == 195:
        dx = - dx
    if xb - 14 <= 71 and yb - 14 == 194:
        dx = - dx
    if xb - 14 <= 72 and yb - 14 == 193:
        dx = - dx
    if xb - 14 <= 73 and yb - 14 == 192:
        dx = - dx
    if xb - 14 <= 75 and yb - 14 == 191:
        dx = - dx
    if xb - 14 <= 76 and yb - 14 == 190:
        dx = - dx
    if xb - 14 <= 77 and yb - 14 == 189:
        dx = - dx
    if xb - 14 <= 79 and yb-14 == 188:
        dx = - dx
    if xb - 14 <= 80 and yb - 14 == 187:
        dx = - dx
    if xb - 14 <= 81 and yb - 14 == 186:
        dx = - dx
    if xb - 14 <= 83 and yb - 14 == 185:
        dx = - dx
    if xb - 14 <= 84 and yb - 14 == 184:
        dx = - dx
    if xb - 14 <= 85 and yb - 14 == 183:
        dx = - dx
    if xb - 14 <= 87 and yb - 14 == 182:
        dx = - dx
    if xb - 14 <= 88 and yb - 14 == 181:
        dx = - dx
    if xb - 14 <= 89 and yb - 14 == 180:
        dx = - dx
    if xb - 14 <= 91 and yb - 14 == 179:
        dx = - dx
    if xb - 14 <= 92 and yb - 14 == 178:
        dx = - dx
    if xb - 14 <= 93 and yb - 14 == 177:
        dx = - dx
    if xb - 14 <= 95 and yb - 14 == 176:
        dx = - dx
    if xb - 14 <= 96 and yb - 14 == 175:
        dx = - dx
    if xb - 14 <= 97 and yb - 14 == 174:
        dx = - dx
    if xb - 14 <= 99 and yb - 14 == 173:
        dx = - dx
    if xb - 14 <= 101 and yb - 14 == 172:
        dx = - dx
    if xb - 14 <= 102 and yb - 14 == 171:
        dx = - dx
    if xb - 14 <= 103 and yb - 14 == 170:
        dx = - dx
    if xb - 14 <= 105 and yb - 14 == 169:
        dx = - dx
    if xb - 14 <= 106 and yb - 14 == 168:
        dx = - dx

    if fa ==1:
        if (yb-14) <= b4ya[fa] and xb - 14 <= b4xb[fa]:
            dy=-dy
        if xb - 14 <= b4xb[fa] and yb-14 <=b4yb[fa] and yb >= b4yc[fa]:
            dx=-dx
            tyt2=1
    if fa == 0:
        if xb - 14 <= 1 and yb -14 <= 277 and yb -14 > 274:
            dx= - dx
        if xb - 14 <= 3 and xb - 14 > 1 and yb -14 <= 274 and yb -14 > 271:
            dx= - dx
        if xb - 14 <= 5 and xb - 14 > 3 and yb -14 <= 271 and yb -14 > 268:
            dx= - dx
        if xb - 14 <= 7 and xb - 14 > 5 and yb -14 <= 268 and yb -14 > 265:
            dx= - dx
        if xb - 14 <= 9 and xb - 14 > 7 and yb -14 <= 265 and yb -14 > 262:
            dx= - dx
        if xb - 14 <= 11 and xb - 14 > 9 and yb -14 <= 262 and yb -14 > 259:
            dx= - dx
        if xb - 14 <= 13 and xb - 14 > 11 and yb -14 <= 259 and yb -14 > 256:
            dx= - dx
        if xb - 14 <= 15 and xb - 14 > 13 and yb -14 <= 256 and yb -14 > 253:
            dx= - dx
        if xb - 14 <= 17 and xb - 14 > 15 and yb -14 <= 253 and yb -14 > 250:
            dx= - dx
        if xb - 14 <= 19 and xb - 14 > 17 and yb -14 <= 250 and yb -14 > 247:
            dx= - dx
        if xb - 14 <= 21 and xb - 14 > 19 and yb -14 <= 247 and yb -14 > 244:
            dx= - dx
        if xb - 14 <= 23 and xb - 14 > 21 and yb -14 <= 244 and yb -14 > 241:
            dx= - dx
        if xb - 14 <= 25 and xb - 14 > 23 and yb -14 <= 241 and yb -14 > 238:
            dx= - dx
        if xb - 14 <= 27 and xb - 14 > 25 and yb -14 <= 238 and yb -14 > 235:
            dx= - dx
        if xb - 14 <= 29 and xb - 14 > 27 and yb -14 <= 235 and yb -14 > 232:
            dx= - dx
        if xb - 14 <= 31 and xb - 14 > 29 and yb -14 <= 232 and yb -14 > 229:
            dx= - dx
        if xb - 14 <= 33 and xb - 14 > 31 and yb -14 <= 229 and yb -14 > 226:
            dx= - dx
        if xb - 14 <= 35 and xb - 14 > 33 and yb -14 <= 226 and yb -14 > 223:
            dx= - dx
        if xb - 14 <= 37 and xb - 14 > 35 and yb -14 <= 223 and yb -14 > 220:
            dx= - dx
        if xb - 14 <= 39 and xb - 14 > 37 and yb -14 <= 220 and yb -14 > 217:
            dx= - dx
        if xb - 14 <= 41 and xb - 14 > 39 and yb -14 <= 217 and yb -14 > 214:
            dx= - dx
        if xb - 14 <= 43 and xb - 14 > 41 and yb -14 <= 214 and yb -14 > 212:
            dx= - dx

    ################################################################################################################################################################################################################# УГОЛ №1 ПРАВЫЙ НИЖНИЙ


    if xb + 14 >= 1005 and yb + 14 == 626:# если шайба летит вниз
        dx = - dx
    if xb + 14 >= 1004 and yb + 14 == 627:
        dx = - dx
    if xb + 14 >= 1002 and yb + 14 == 628:
        dx = - dx
    if xb + 14 >= 1001 and yb + 14 == 629:
        dx = - dx
    if xb + 14 >= 1000 and yb + 14 == 630:
        dx = - dx
    if xb + 14 >= 998 and yb + 14 == 631:
        dx = - dx
    if xb + 14 >= 997 and yb + 14 == 632:
        dx = - dx
    if xb + 14 >= 996 and yb + 14 == 633:
        dx = - dx
    if xb + 14 >= 994 and yb + 14 == 634:
        dx = - dx
    if xb + 14 >= 993 and yb + 14 == 635:
        dx = - dx
    if xb + 14 >= 992 and yb + 14 == 636:
        dx = - dx
    if xb + 14 >= 990 and yb + 14 == 637:
        dx = - dx
    if xb + 14 >= 989 and yb + 14 == 638:
        dx = - dx
    if xb + 14 >= 988 and yb + 14 == 639:
        dx = - dx
    if xb + 14 >= 986 and yb + 14 == 640:
        dx = - dx
    if xb + 14 >= 985 and yb + 14 == 641:
        dx = - dx
    if xb + 14 >= 984 and yb + 14 == 642:
        dx = - dx
    if xb + 14 >= 982 and yb + 14 == 643:
        dx = - dx
    if xb + 14 >= 981 and yb + 14 == 644:
        dx = - dx
    if xb + 14 >= 980 and yb + 14 == 645:
        dx = - dx
    if xb + 14 >= 978 and yb + 14 == 646:
        dx = - dx
    if xb + 14 >= 977 and yb + 14 == 647:
        dx = - dx
    if xb + 14 >= 976 and yb + 14 == 648:
        dx = - dx
    if xb + 14 >= 974 and yb + 14 == 649:
        dx = - dx
    if xb + 14 >= 973 and yb + 14 == 650:
        dx = - dx
    if xb + 14 >= 972 and yb + 14 == 651:
        dx = - dx
    if xb + 14 >= 971 and yb + 14 == 652:
        dx = - dx
    if xb + 14 >= 970 and yb + 14 == 653:
        dx = - dx
    if xb + 14 >= 969 and yb + 14 == 654:
        dx = - dx
    if xb + 14 >= 967 and yb + 14 == 655:
        dx = - dx
    if xb + 14 >= 966 and yb + 14 == 656:
        dx = - dx
    if xb + 14 >= 965 and yb + 14 == 657:
        dx = - dx
    if xb + 14 >= 963 and yb + 14 == 658:
        dx = - dx
    if xb + 14 >= 962 and yb + 14 == 659:
        dx = - dx
    if xb + 14 >= 961 and yb + 14 == 660:
        dx = - dx
    if xb + 14 >= 959 and yb + 14 == 661:
        dx = - dx
    if xb + 14 >= 958 and yb + 14 == 662:
        dx = - dx
    if xb + 14 >= 957 and yb + 14 == 663:
        dx = - dx
    if xb + 14 >= 955 and yb + 14 == 664:
        dx = - dx
    if xb + 14 >= 954 and yb + 14 == 665:
        dx = - dx
    if xb + 14 >= 953 and yb + 14 == 666:
        dx = - dx
    if xb + 14 >= 951 and yb + 14 == 667:
        dx = - dx
    if xb + 14 >= 950 and yb + 14 == 668:
        dx = - dx
    if xb + 14 >= 949 and yb + 14 == 669:
        dx = - dx
    if xb + 14 >= 947 and yb + 14 == 670:
        dx = - dx
    if xb + 14 >= 946 and yb + 14 == 671:
        dx = - dx
    if xb + 14 >= 944 and yb + 14 == 671:
        dx = - dx
    if sole ==1:
        if (yb+14) >= b5ya[sole] and xb - 14 >= b5xb[sole]:
            dy=-dy
        if xb + 14 >= b5xb[sole] and yb+14 >=b5yb[sole] and yb <= b5yc[sole]:
            dx=-dx
            tyt3=1
    if sole == 0:
        if xb + 14 >= 1069  and xb -14 < 1070  and yb -14 <= 214 and yb +14 < 566:
            dx= - dx
        if xb + 14 >= 1067 and xb -14 < 1069 and yb +14 >= 566 and yb +14 < 569:
            dx= - dx
        if xb + 14 >= 1065 and xb -14 < 1067  and yb +14 >= 569 and yb +14 < 572:
            dx= - dx
        if xb + 14 >= 1063 and xb -14 < 1065  and yb +14 >= 572 and yb +14 < 575:
            dx= - dx
        if xb + 14 >= 1061 and xb -14 < 1063  and yb +14 >= 575 and yb +14 < 578:
            dx= - dx
        if xb + 14 >= 1059 and xb -14 < 1061 and yb +14 >= 578 and yb +14 < 581:
            dx= - dx
        if xb + 14 >= 1057 and xb -14 < 1059  and yb +14 >= 581 and yb +14 < 584:
            dx= - dx
        if xb + 14 >= 1055 and xb -14 < 1057 and yb +14 >= 584 and yb +14 < 587:
            dx= - dx
        if xb + 14 >= 1053 and xb -14 < 1055  and yb +14 >= 587 and yb +14 < 590:
            dx= - dx
        if xb + 14 >= 1051 and xb -14 < 1053  and yb +14 >= 590 and yb +14 < 593:
            dx= - dx
        if xb + 14 >= 1049  and xb -14 < 1051 and yb +14 >= 593 and yb +14 < 596:
            dx= - dx
        if xb + 14 >= 1047  and xb -14 < 1049 and yb +14 >= 596 and yb +14 < 599:
            dx= - dx
        if xb + 14 >= 1045 and xb -14 < 1047  and yb +14 >= 599 and yb +14 < 602:
            dx= - dx
        if xb + 14 >= 1043 and xb -14 < 1045  and yb +14 >= 602 and yb +14 < 605:
            dx= - dx
        if xb + 14 >= 1041 and xb -14 < 1043 and yb +14 >= 605 and yb +14 < 608:
            dx= - dx
        if xb + 14 >= 1039 and xb -14 < 1041  and yb +14 >= 608 and yb +14 < 611:
            dx= - dx
        if xb + 14 >= 1037 and xb -14 < 1039  and yb +14 >= 611 and yb +14 < 614:
            dx= - dx
        if xb + 14 >= 1035 and xb -14 < 1037  and yb +14 >= 614 and yb +14 < 617:
            dx= - dx
        if xb + 14 >= 1033 and xb -14 < 1035  and yb +14 >= 617 and yb +14 < 620:
            dx= - dx
        if xb + 14 >= 1031 and xb -14 < 1033  and yb +14 >= 620 and yb +14 < 623:
            dx= - dx
        if xb + 14 >= 1029 and xb -14 < 1031  and yb +14 >= 623 and yb +14 < 626:
            dx= - dx


        ############################################################################################################################################################################################################# УГОЛ №2 ПРАВЫЙ ВЕРХНИЙ


    if xb + 14 >= 1005 and yb - 14 == 214:# если шайба летит вверх
        dx = - dx
    if xb + 14 >= 1004 and yb - 14 == 213:
        dx = - dx
    if xb + 14 >= 1002 and yb - 14 == 212:
        dx = - dx
    if xb + 14 >= 1001 and yb - 14 == 211:
        dx = - dx
    if xb + 14 >= 1000 and yb - 14 == 210:
        dx = - dx
    if xb + 14 >= 998 and yb - 14 == 209:
        dx = - dx
    if xb + 14 >= 997 and yb - 14 == 208:
        dx = - dx
    if xb + 14 >= 996 and yb - 14 == 207:
        dx = - dx
    if xb + 14 >= 994 and yb - 14 == 206:
        dx = - dx
    if xb + 14 >= 993 and yb - 14 == 205:
        dx = - dx
    if xb + 14 >= 992 and yb - 14 == 204:
        dx = - dx
    if xb + 14 >= 990 and yb - 14 == 203:
        dx = - dx
    if xb + 14 >= 989 and yb - 14 == 202:
        dx = - dx
    if xb + 14 >= 988 and yb - 14 == 201:
        dx = - dx
    if xb + 14 >= 986 and yb - 14 == 200:
        dx = - dx
    if xb + 14 >= 985 and yb - 14 == 199:
        dx = - dx
    if xb + 14 >= 984 and yb - 14 == 198:
        dx = - dx
    if xb + 14 >= 982 and yb - 14 == 197:
        dx = - dx
    if xb + 14 >=981 and yb - 14 == 196:
        dx = - dx
    if xb + 14 >= 980 and yb - 14 == 195:
        dx = - dx
    if xb + 14 >= 978 and yb - 14 == 194:
        dx = - dx
    if xb + 14 >= 977 and yb - 14 == 193:
        dx = - dx
    if xb + 14 >= 976 and yb - 14 == 192:
        dx = - dx
    if xb + 14 >= 974 and yb - 14 == 191:
        dx = - dx
    if xb + 14 >= 973 and yb - 14 == 190:
        dx = - dx
    if xb + 14 >= 972 and yb - 14 == 189:
        dx = - dx
    if xb + 14 >= 970 and yb-14 ==188:
        dx = - dx
    if xb + 14 >= 969 and yb - 14 == 187:
        dx = - dx
    if xb + 14 >= 968 and yb - 14 == 186:
        dx = - dx
    if xb + 14 >= 966 and yb - 14 == 185:
        dx = - dx
    if xb + 14 >= 965 and yb - 14 == 184:
        dx = - dx
    if xb + 14 >= 964 and yb - 14 == 183:
        dx = - dx
    if xb + 14 >= 962 and yb - 14 == 182:
        dx = - dx
    if xb + 14 >= 961 and yb - 14 == 181:
        dx = - dx
    if xb + 14 >= 960 and yb - 14 == 180:
        dx = - dx
    if xb + 14 >= 958 and yb - 14 == 179:
        dx = - dx
    if xb + 14 >= 957 and yb - 14 == 178:
        dx = - dx
    if xb + 14 >= 956 and yb - 14 == 177:
        dx = - dx
    if xb + 14 >= 954 and yb - 14 == 176:
        dx = - dx
    if xb + 14 >= 953 and yb - 14 == 175:
        dx = - dx
    if xb + 14 >= 952 and yb - 14 == 174:
        dx = - dx
    if xb + 14 >= 950 and yb - 14 == 173:
        dx = - dx
    if xb + 14 >= 949 and yb - 14 == 172:
        dx = - dx
    if xb + 14 >= 948 and yb - 14 == 171:
        dx = - dx
    if xb + 14 >= 946 and yb - 14 == 170:
        dx = - dx
    if xb + 14 >= 945 and yb - 14 == 169:
        dx = - dx
    if xb + 14 >= 944 and yb - 14 == 168:
        dx = - dx


    if cibemole ==1:
        if (yb-14) <= b8ya[cibemole] and xb - 14 >= b8xb[cibemole]:
            dy=-dy
        if xb - 14 >= b8xb[cibemole] and yb-14 <=b8yb[cibemole] and yb >= b8yc[cibemole]:
            dx=-dx
            tyt4=1
    if cibemole == 0:
        if xb + 14 >= 1069 and yb -14 < 277 and yb -14 > 274:# отбивание от рокетки если шайба летит вниз
            dx= - dx
        if xb + 14 >= 1067 and xb + 14 < 1069 and yb -14 <= 274 and yb -14 > 271:
            dx= - dx
        if xb + 14 >= 1065 and xb + 14 < 1067 and yb -14 <= 271 and yb -14 > 268:
            dx= - dx
        if xb + 14 >= 1063 and xb + 14 < 1065 and yb -14 <= 268 and yb -14 > 265:
            dx= - dx
        if xb + 14 >= 1061 and xb + 14 < 1063 and yb -14 <= 265 and yb -14 > 262:
            dx= - dx
        if xb + 14 >= 1059 and xb + 14 < 1061 and yb -14 <= 262 and yb -14 > 259:
            dx= - dx
        if xb + 14 >= 1057 and xb + 14 < 1059 and yb -14 <= 259 and yb -14 > 256:
            dx= - dx
        if xb + 14 >= 1055 and xb + 14 < 1057 and yb -14 <= 256 and yb -14 > 253:
            dx= - dx
        if xb + 14 >= 1053 and xb + 14 < 1055 and yb -14 <= 253 and yb -14 > 250:
            dx= - dx
        if xb + 14 >= 1051 and xb + 14 < 1053 and yb -14 <= 250 and yb -14 > 247:
            dx= - dx
        if xb + 14 >= 1049 and xb + 14 < 1051 and yb -14 <= 247 and yb -14 > 244:
            dx= - dx
        if xb + 14 >= 1047 and xb + 14 < 1049 and yb -14 <= 244 and yb -14 > 241:
            dx= - dx
        if xb + 14 >= 1045 and xb + 14 < 1047 and yb -14 <= 241 and yb -14 > 238:
            dx= - dx
        if xb + 14 >= 1043 and xb + 14 < 1045 and yb -14 <= 238 and yb -14 > 235:
            dx= - dx
        if xb + 14 >= 1041 and xb + 14 < 1043 and yb -14 <= 235 and yb -14 > 232:
            dx= - dx
        if xb + 14 >= 1039 and xb + 14 < 1041 and yb -14 <= 232 and yb -14 > 229:
            dx= - dx
        if xb + 14 >= 1037 and xb + 14 < 1039 and yb -14 <= 229 and yb -14 > 226:
            dx= - dx
        if xb + 14 >= 1035 and xb + 14 < 1037 and yb -14 <= 226 and yb -14 > 223:
            dx= - dx
        if xb + 14 >= 1033 and xb + 14 < 1035 and yb -14 <= 223 and yb -14 > 220:
            dx= - dx
        if xb + 14 >= 1031 and xb + 14 < 1033 and yb -14 <= 220 and yb -14 > 217:
            dx= - dx
        if xb + 14 >= 1029 and xb + 14 < 1031 and yb -14 <= 217 and yb -14 > 214:
            dx= - dx
        if xb + 14 >= 1027 and xb + 14 < 1029 and yb -14 <= 214 and yb -14 > 212:
            dx= - dx

s=''
name=''
def direction(name):
    global ss,s, st,screen
    k=0#Эта переменная нужна для ввода заглавных букв. Shift здесь не работает
    hor=80
    running=True
    font = pygame.font.SysFont("Arial", 24,False,False)
    text = font.render("",1, THECOLORS ["blue"])
    screen.blit(text, [hor,50] )
    while running:
        screen.fill([255,255,255])
        color = THECOLORS["blue"]
        font = pygame.font.SysFont("Arial", 24,False,False)
        myfont = pygame.font.SysFont("Arial", 16,False,False)
        info_text=font.render("Введите ваше имя",1, THECOLORS ["red"])
        screen.blit(info_text,[50,10])
        my_text = myfont.render("Press Enter",1, THECOLORS ["black"])
        screen.blit(my_text, [hor+20,120] )
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running = False
                st=pygame.key.name(event.key)
                if k==0 and not (st=="return"):#Фамилия начинается с заглавной буквы
                    st=st.title()
                    k=1
                if st=="space":
                    st=" "
                    k=0#После пробела имя начинается с заглавной буквы
                if st=="backspace":
                    st=""
                    a=len(s)-1
                    st=st[0:a]
                if not(st=="return"):#Если не нажата Enter
                    s=s+st
                if st =="return":#Если нажата Enter
                    name=s
                    ss=s
                    running=False
        text= font.render(s,0, THECOLORS ["blue"])
        screen.blit(text, [hor,50] )
        pygame.display.flip()
        screen = pygame.display.set_mode([1071, 672])
    return(name)

def one_player():
    global ss,name,s,screen,down1,gg,xd,yd,pas ,i,hokkeyblue, my_downn,xmn,ymn,io, pi,dy,dx,do,re,mi,fa,sole,li,ci,cibemole,time,timer,timet,gole1,gole2,xb,yb,hx1,hy1,hx2,hy2,hhx1,hhy1,hhx2,hhy2,otbitie1,otbitie2,iu1,iu2,tyt1,tyt2,tyt3,tyt4
    my_down1 = True
    direction(name)
    while my_down1:
        io = 0
        xd = dx
        yd = dy
        screen.fill(THECOLORS['white'])
        screen.blit(ugol_2,[966,166])
        screen.blit(ugol_1,[967,440])
        screen.blit(ugol_3,[-21,166])
        screen.blit(ugol_4,[-21,440])
        screen.blit(pause,[0,0])
        screen.blit(vopros,[116,0])
        screen.blit(nastroykii,[839,0])
        screen.blit(delete,[955,0])
        font = pygame.font.SysFont("Arial", 60,False,False)
        text= font.render(s,0, THECOLORS ["blue"])
        screen.blit(text, [10,100] )
        font = pygame.font.SysFont("Arial", 60,False,False)
        text212= font.render("Computer",0, THECOLORS ["blue"])
        screen.blit(text212, [640,100] )
        pygame.draw.lines(screen, THECOLORS['blue'],False,[[357,screenY],[357,168]],5)
        pygame.draw.lines(screen, THECOLORS['blue'],False,[[714,screenY],[714,168]],5)
        pygame.draw.lines(screen, THECOLORS['red'],False,[[535,screenY],[535,168]],5)
        pygame.draw.circle(screen, THECOLORS['red'],[535,420], 10, 0)
        pygame.draw.circle(screen, THECOLORS['red'],[535,420], 147, 6)
        pygame.draw.circle(screen, THECOLORS['blue'],[892,546], 100, 6)
        pygame.draw.circle(screen, THECOLORS['blue'],[892,294], 100, 6)
        pygame.draw.circle(screen, THECOLORS['blue'],[179,546], 100, 6)
        pygame.draw.circle(screen, THECOLORS['blue'],[179,294], 100, 6)
        pygame.draw.circle(screen, THECOLORS['blue'],[892,294], 10, 0)
        pygame.draw.circle(screen, THECOLORS['blue'],[892,546], 10, 0)
        pygame.draw.circle(screen, THECOLORS['blue'],[179,546], 10, 0)
        pygame.draw.circle(screen, THECOLORS['blue'],[179,294], 10, 0)
        pygame.draw.lines(screen, THECOLORS['black'],False,[[0,168],[screenX,168]],5)
        pygame.draw.lines(screen, THECOLORS['black'],False,[[0,168],[0,screenY]],10)
        pygame.draw.lines(screen, THECOLORS['black'],False,[[0,screenY],[screenX,screenY]],10)
        pygame.draw.lines(screen, THECOLORS['black'],False,[[screenX,screenY],[screenX,168]],12)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[0,84],[1071,84]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[465,84],[465,168]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[606,84],[606,168]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[535,0],[535,84]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[676,0],[676,84]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[394,0],[394,84]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[232,0],[232,84]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[839,0],[839,84]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[116,0],[116,84]],2)
        pygame.draw.lines(screen,THECOLORS['black'],False,[[955,0],[955,84]],2)
        pygame.draw.lines(screen, THECOLORS['yellow'],False,[[screenX-2,337],[screenX-2,499]],10)
        pygame.draw.lines(screen, THECOLORS['yellow'],False,[[0,337],[0,499]],10)
        bita()
        ball_move()
        hhx1 = hhx1+hx1
        hhy1 = hhy1+hy1
        hhx2 = hhx2+hx2
        hhy2 = hhy2+hy2
        screen.blit(hokkeyblue,[hhx1,hhy1])
        screen.blit(hokkeyred,[hhx2,hhy2])
        if hhx1 <= 105:
           hhx1 = 105
        if hhx1 >= 408:
           hhx1 = 408
        if hhy1 <= 168:
           hhy1 = 168
        if hhy1 >= 555:
           hhy1 = 555
        if hhx2 <= 535:
           hhx2 = 535
        if hhx2 >= 850:
           hhx2 = 850
        if hhy2 <= 168:
           hhy2 = 168
        if hhy2 >= 555:
           hhy2 = 555
        if timer==0:
            timet= timet + 1
        if timet ==310:
            timer = 1
        if timer == 1:
            timet = timet - 1
        if timet == 0:
            timer =0
        if timet == 0:
            time=time-1
        if timet == 310:
            time=time-1
        if time == 0:
            my_down1 = False
        if xb <= 0:
            gole1 = gole1 + 1
            xb = 535
            yb = 420
        if xb >= 1071:
            gole2 = gole2 + 1
            xb = 535
            yb = 420
        if my_down1 == False:
            gole1 =0
            gole2 =0
        if hhy2+98 > yb:
            hy2 = -1
        if hhy2+98 < yb:
            hy2 = 1
        if xb >= 960 and yb <= 399:
            cibemole = 1
        if xb >= 960 and yb >= 440:
            sole = 1
        time = str(time)
        font = pygame.font.Font(None, 130)
        texttime = font.render(time,True, THECOLORS ["black"])
        screen.blit(texttime,[490,80])
        time = int(time)
        gole1=str(gole1)
        textgole1 = font.render(gole1,True, THECOLORS ["black"])
        screen.blit(textgole1,[540,10])
        gole1 = int(gole1)
        gole2=str(gole2)
        textgole2 = font.render(gole2,True, THECOLORS ["black"])
        screen.blit(textgole2,[399,10])
        gole2 = int(gole2)
##        pygame.mixer.music.load("твоя музыка.mp3")
##        pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                hx1 = 0
                hy1 = 0
                while do>0:
                    do = do - 1
##                while re>0:
##                    re = re - 1
##                while mi>0:
##                    mi = mi - 1
                while fa>0:
                    fa = fa - 1
                while sole>0:
                    sole = sole - 1
##                while li>0:
##                    li = li - 1
##                while ci>0:
##                    ci = ci - 1
                while cibemole>0:
                    cibemole = cibemole - 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    hx1 = -1
                if event.key == pygame.K_d:
                    hx1 = 1
                if event.key == pygame.K_w:
                    hy1 = -1
                if event.key == pygame.K_s:
                    hy1 = 1
                if event.key == pygame.K_v:
                    while do<1:
                        do = do + 1
##                    while re<2:
##                        re = re + 1
                if event.key == pygame.K_c:
##                    while mi<2:
##                        mi = mi + 1
                    while fa<1:
                        fa = fa + 1
                if event.key == pygame.K_LSHIFT:
                    otbitie1 =1
                    iu1=1
                if event.key == pygame.K_LCTRL:
                    otbitie1 =0
            if event.type == pygame.QUIT:
                i = 1
                my_down = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                my_downn = True
                (xmn,ymn)= event.pos
        och=gole2

        if my_downn:
            if xmn >=116 and ymn >=0 and xmn<=232 and ymn <=84:
                down1=1
            if xmn >=0 and ymn >=0 and xmn<=116 and ymn <=84:
                pas=1
            if xmn >=839 and ymn >=0 and xmn<=955 and ymn <=84:
                nastroyki()
            if xmn >=955 and ymn >=0 and xmn<=1071 and ymn <=84:
                io = 1
                gole1 =0
                gole2 = 0
                s=''
                my_downn=False
            if down1==1:
                import my_help
                my_help.myhelp()
                down1=0
                break
        if io == 1:
            my_down1 = False
        ball_proverka()
        if pas==1:
            screen.blit(pause2,[397,320])
            dx = 0
            dy = 0
            hx1=0
            hy1=0
            hx2=0
            hy2=0
            timet =156
            font = pygame.font.Font(None, 25)
            textpas = font.render("чтобы продолжить, нажмите правую кнопку мыши",True, THECOLORS ["black"])
            screen.blit(textpas,[325,650])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pas=0
                    dx=xd
                    dy=yd
                    timet =0
        pygame.display.flip()
        screen = pygame.display.set_mode([1071, 672])
    myn=ss
    pickle_file = open('my_rec.pkl', 'rb')
    names = pickle.load(pickle_file)
    pickle_file.close()
    nam=names[0:5]
    scores=names[5:]
    scores.append(och)#добавляем в список очки игрока
    scores.sort(reverse=True)#Cортируем список по убыванию
    del scores[len(scores)-1]#Удаляем последний элемент списка
    if och in scores:#если очки остаются в списке
        k=scores.index(och)#находим порядковый номер очков
        nam.insert(k,myn)#Вставляем имя игрока на позицию очков
        del nam[len(nam)-1]#удаляем последнее имя
        nam.extend(scores)#объединяем имена и очки в один список
        names=nam
        pickle_file = open('my_rec.pkl', 'wb')#записываем новую таблицу в файл
        pickle.dump(names, pickle_file)
        pickle_file.close()
        import table
        table.show_rec(names)#Выводим на экран новую таблицу
    else:#Если не попали в рекорды
        font = pygame.font.Font(None, 50)
        text = font.render("Не вошли в рекорды",True, THECOLORS ["red"])
        screen.blit(text, [10, 250] )
        pygame.display.flip()
        pygame.time.delay(4000)
    pygame.display.flip()
    screen = pygame.display.set_mode([1071, 672])
