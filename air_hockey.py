import pygame, random, sys,ZASTAVKA
import pickle
from pygame.color import THECOLORS
from pygame import font
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



photo0_file="1.png"
p1p0=pygame.image.load(photo0_file)
photo1_file="1 — копия.png"
p1p1=pygame.image.load(photo1_file)
photo2_file="1 — копия (2).png"
p1p2=pygame.image.load(photo2_file)
photo3_file="1 — копия (3).png"
p1p3=pygame.image.load(photo3_file)
photo4_file="1 — копия (4).png"
p1p4=pygame.image.load(photo4_file)
photo5_file="1 — копия (5).png"
p1p5=pygame.image.load(photo5_file)
photo6_file="1 — копия (6).png"
p1p6=pygame.image.load(photo6_file)
photo7_file="1 — копия (7).png"
p1p7=pygame.image.load(photo7_file)
photo8_file="1 — копия (8).png"
p1p8=pygame.image.load(photo8_file)
photo9_file="1 — копия (9).png"
p1p9=pygame.image.load(photo9_file)
photo10_file="1 — копия (10).png"
p1p10=pygame.image.load(photo10_file)
photo11_file="1 — копия (11).png"
p1p11=pygame.image.load(photo11_file)
photo12_file="1 — копия (12).png"
p1p12=pygame.image.load(photo12_file)
photo13_file="1 — копия (13).png"
p1p13=pygame.image.load(photo13_file)
photo14_file="1 — копия (14).png"
p1p14=pygame.image.load(photo14_file)
photo15_file="1 — копия (15).png"
p1p15=pygame.image.load(photo15_file)
photo16_file="1 — копия (16).png"
p1p16=pygame.image.load(photo16_file)
photo17_file="1 — копия (17).png"
p1p17=pygame.image.load(photo17_file)
photo18_file="1 — копия (18).png"
p1p18=pygame.image.load(photo18_file)
photo19_file="1 — копия (19).png"
p1p19=pygame.image.load(photo19_file)
photo20_file="1 — копия (20).png"
p1p20=pygame.image.load(photo20_file)
photo21_file="1 — копия (21).png"
p1p21=pygame.image.load(photo21_file)
photo22_file="1 — копия (22).png"
p1p22=pygame.image.load(photo22_file)
photo23_file="1 — копия (23).png"
p1p23=pygame.image.load(photo23_file)
photo24_file="1 — копия (24).png"
p1p24=pygame.image.load(photo24_file)
photo25_file="1 — копия (25).png"
p1p25=pygame.image.load(photo25_file)
photo26_file="1 — копия (26).png"
p1p26=pygame.image.load(photo26_file)
photo27_file="1 — копия (27).png"
p1p27=pygame.image.load(photo27_file)
photo28_file="1 — копия (28).png"
p1p28=pygame.image.load(photo28_file)
photo29_file="1 — копия (29).png"
p1p29=pygame.image.load(photo29_file)
photo30_file="1 — копия (30).png"
p1p30=pygame.image.load(photo30_file)
photo31_file="1 — копия (31).png"
p1p31=pygame.image.load(photo31_file)
photo32_file="1 — копия (32).png"
p1p32=pygame.image.load(photo32_file)
photo33_file="1 — копия (33).png"
p1p33=pygame.image.load(photo33_file)
photo34_file="1 — копия (34).png"
p1p34=pygame.image.load(photo34_file)
photo35_file="1 — копия (35).png"
p1p35=pygame.image.load(photo35_file)
photo36_file="1 — копия (36).png"
p1p36=pygame.image.load(photo36_file)
photo37_file="1 — копия (37).png"
p1p37=pygame.image.load(photo37_file)
photo38_file="1 — копия (38).png"
p1p38=pygame.image.load(photo38_file)
photo39_file="1 — копия (39).png"
p1p39=pygame.image.load(photo39_file)
photo40_file="1 — копия (40).png"
p1p40=pygame.image.load(photo40_file)
photo41_file="1 — копия (41).png"
p1p41=pygame.image.load(photo41_file)
photo42_file="1 — копия (42).png"
p1p42=pygame.image.load(photo42_file)
photo43_file="1 — копия (43).png"
p1p43=pygame.image.load(photo43_file)
photo44_file="1 — копия (44).png"
p1p44=pygame.image.load(photo44_file)
photo45_file="1 — копия (45).png"
p1p45=pygame.image.load(photo45_file)
photo46_file="1 — копия (46).png"
p1p46=pygame.image.load(photo46_file)
photo47_file="1 — копия (47).png"
p1p47=pygame.image.load(photo47_file)
photo48_file="1 — копия (48).png"
p1p48=pygame.image.load(photo48_file)
photo49_file="1 — копия (49).png"
p1p49=pygame.image.load(photo49_file)

photo0_file="2 — копия (10).jpeg"
p2p0=pygame.image.load(photo0_file)
photo1_file="2 — копия (9).jpeg"
p2p1=pygame.image.load(photo1_file)
photo2_file="2 — копия (8).jpeg"
p2p2=pygame.image.load(photo2_file)
photo3_file="2 — копия (7).jpeg"
p2p3=pygame.image.load(photo3_file)
photo4_file="2 — копия (6).jpeg"
p2p4=pygame.image.load(photo4_file)
photo5_file="2 — копия (5).jpeg"
p2p5=pygame.image.load(photo5_file)
photo6_file="2 — копия (4).jpeg"
p2p6=pygame.image.load(photo6_file)
photo7_file="2 — копия (3).jpeg"
p2p7=pygame.image.load(photo7_file)
photo8_file="2 — копия (2).jpeg"
p2p8=pygame.image.load(photo8_file)
photo9_file="2 — копия.jpeg"
p2p9=pygame.image.load(photo9_file)
photo10_file="2.jpeg"
p2p10=pygame.image.load(photo10_file)
photo11_file="2 — копия (11).jpeg"
p2p11=pygame.image.load(photo11_file)
photo12_file="2 — копия (12).jpeg"
p2p12=pygame.image.load(photo12_file)
photo13_file="2 — копия (13).jpeg"
p2p13=pygame.image.load(photo13_file)
photo14_file="2 — копия (14).jpeg"
p2p14=pygame.image.load(photo14_file)
photo15_file="2 — копия (15).jpeg"
p2p15=pygame.image.load(photo15_file)
photo16_file="2 — копия (16).jpeg"
p2p16=pygame.image.load(photo16_file)
photo17_file="2 — копия (17).jpeg"
p2p17=pygame.image.load(photo17_file)
photo18_file="2 — копия (18).jpeg"
p2p18=pygame.image.load(photo18_file)
photo19_file="2 — копия (19).jpeg"
p2p19=pygame.image.load(photo19_file)
photo20_file="2 — копия (20).jpeg"
p2p20=pygame.image.load(photo20_file)
photo21_file="2 — копия (21).jpeg"
p2p21=pygame.image.load(photo21_file)
photo22_file="2 — копия (22).jpeg"
p2p22=pygame.image.load(photo22_file)
photo23_file="2 — копия (23).jpeg"
p2p23=pygame.image.load(photo23_file)
photo24_file="2 — копия (24).jpeg"
p2p24=pygame.image.load(photo24_file)
photo25_file="2 — копия (25).jpeg"
p2p25=pygame.image.load(photo25_file)
photo26_file="2 — копия (26).jpeg"
p2p26=pygame.image.load(photo26_file)
photo27_file="2 — копия (27).jpeg"
p2p27=pygame.image.load(photo27_file)
photo28_file="2 — копия (28).jpeg"
p2p28=pygame.image.load(photo28_file)
photo29_file="2 — копия (29).jpeg"
p2p29=pygame.image.load(photo29_file)
photo30_file="2 — копия (30).jpeg"
p2p30=pygame.image.load(photo30_file)
photo31_file="2 — копия (31).jpeg"
p2p31=pygame.image.load(photo31_file)
photo32_file="2 — копия (32).jpeg"
p2p32=pygame.image.load(photo32_file)
photo33_file="2 — копия (33).jpeg"
p2p33=pygame.image.load(photo33_file)
photo34_file="2 — копия (34).jpeg"
p2p34=pygame.image.load(photo34_file)
photo35_file="2 — копия (35).jpeg"
p2p35=pygame.image.load(photo35_file)
photo36_file="2 — копия (36).jpeg"
p2p36=pygame.image.load(photo36_file)
photo37_file="2 — копия (37).jpeg"
p2p37=pygame.image.load(photo37_file)
photo38_file="2 — копия (38).jpeg"
p2p38=pygame.image.load(photo38_file)
photo39_file="2 — копия (39).jpeg"
p2p39=pygame.image.load(photo39_file)
photo40_file="2 — копия (40).jpeg"
p2p40=pygame.image.load(photo40_file)
photo41_file="2 — копия (41).jpeg"
p2p41=pygame.image.load(photo41_file)
photo42_file="2 — копия (42).jpeg"
p2p42=pygame.image.load(photo42_file)
photo43_file="2 — копия (43).jpeg"
p2p43=pygame.image.load(photo43_file)
photo44_file="2 — копия (44).jpeg"
p2p44=pygame.image.load(photo44_file)
photo45_file="2 — копия (45).jpeg"
p2p45=pygame.image.load(photo45_file)
photo46_file="2 — копия (46).jpeg"
p2p46=pygame.image.load(photo46_file)
photo47_file="2 — копия (47).jpeg"
p2p47=pygame.image.load(photo47_file)
photo48_file="2 — копия (48).jpeg"
p2p48=pygame.image.load(photo48_file)
photo49_file="2 — копия (49).jpeg"
p2p49=pygame.image.load(photo49_file)

photo0_file="3.jpg"
p30=pygame.image.load(photo0_file)
photo1_file="3 — копия.jpg"
p31=pygame.image.load(photo1_file)
photo2_file="3 — копия (2).jpg"
p32=pygame.image.load(photo2_file)
photo3_file="3 — копия (3).jpg"
p33=pygame.image.load(photo3_file)
photo4_file="3 — копия (4).jpg"
p34=pygame.image.load(photo4_file)
photo5_file="3 — копия (5).jpg"
p35=pygame.image.load(photo5_file)
photo6_file="3 — копия (6).jpg"
p36=pygame.image.load(photo6_file)
photo7_file="3 — копия (7).jpg"
p37=pygame.image.load(photo7_file)
photo8_file="3 — копия (8).jpg"
p38=pygame.image.load(photo8_file)
photo9_file="3 — копия (9).jpg"
p39=pygame.image.load(photo9_file)
photo10_file="3 — копия (10).jpg"
p310=pygame.image.load(photo10_file)
photo11_file="3 — копия (11).jpg"
p311=pygame.image.load(photo11_file)
photo12_file="3 — копия (12).jpg"
p312=pygame.image.load(photo12_file)
photo13_file="3 — копия (13).jpg"
p313=pygame.image.load(photo13_file)
photo14_file="3 — копия (14).jpg"
p314=pygame.image.load(photo14_file)
photo15_file="3 — копия (15).jpg"
p315=pygame.image.load(photo15_file)
photo16_file="3 — копия (16).jpg"
p316=pygame.image.load(photo16_file)
photo17_file="3 — копия (17).jpg"
p317=pygame.image.load(photo17_file)
photo18_file="3 — копия (18).jpg"
p318=pygame.image.load(photo18_file)
photo19_file="3 — копия (19).jpg"
p319=pygame.image.load(photo19_file)
photo20_file="3 — копия (20).jpg"
p320=pygame.image.load(photo20_file)
photo21_file="3 — копия (21).jpg"
p321=pygame.image.load(photo21_file)
photo22_file="3 — копия (22).jpg"
p322=pygame.image.load(photo22_file)
photo23_file="3 — копия (23).jpg"
p323=pygame.image.load(photo23_file)
photo24_file="3 — копия (24).jpg"
p324=pygame.image.load(photo24_file)
photo25_file="3 — копия (25).jpg"
p325=pygame.image.load(photo25_file)
photo26_file="3 — копия (26).jpg"
p326=pygame.image.load(photo26_file)
photo27_file="3 — копия (27).jpg"
p327=pygame.image.load(photo27_file)
photo28_file="3 — копия (28).jpg"
p328=pygame.image.load(photo28_file)
photo29_file="3 — копия (29).jpg"
p329=pygame.image.load(photo29_file)
photo30_file="3 — копия (30).jpg"
p330=pygame.image.load(photo30_file)
photo31_file="3 — копия (31).jpg"
p331=pygame.image.load(photo31_file)
photo32_file="3 — копия (32).jpg"
p332=pygame.image.load(photo32_file)
photo33_file="3 — копия (33).jpg"
p333=pygame.image.load(photo33_file)
photo34_file="3 — копия (34).jpg"
p334=pygame.image.load(photo34_file)
photo35_file="3 — копия (35).jpg"
p335=pygame.image.load(photo35_file)
photo36_file="3 — копия (36).jpg"
p336=pygame.image.load(photo36_file)
photo37_file="3 — копия (37).jpg"
p337=pygame.image.load(photo37_file)
photo38_file="3 — копия (38).jpg"
p338=pygame.image.load(photo38_file)
photo39_file="3 — копия (39).jpg"
p339=pygame.image.load(photo39_file)
photo40_file="3 — копия (40).jpg"
p340=pygame.image.load(photo40_file)
photo41_file="3 — копия (41).jpg"
p341=pygame.image.load(photo41_file)
photo42_file="3 — копия (42).jpg"
p342=pygame.image.load(photo42_file)
photo43_file="3 — копия (43).jpg"
p343=pygame.image.load(photo43_file)
photo44_file="3 — копия (44).jpg"
p344=pygame.image.load(photo44_file)
photo45_file="3 — копия (45).jpg"
p345=pygame.image.load(photo45_file)
photo46_file="3 — копия (46).jpg"
p346=pygame.image.load(photo46_file)
photo47_file="3 — копия (47).jpg"
p347=pygame.image.load(photo47_file)
photo48_file="3 — копия (48).jpg"
p348=pygame.image.load(photo48_file)
photo49_file="3 — копия (49).jpg"
p349=pygame.image.load(photo49_file)

photo0_file="4.jpeg"
p40=pygame.image.load(photo0_file)
photo1_file="4 — копия.jpeg"
p41=pygame.image.load(photo1_file)
photo2_file="4 — копия (2).jpeg"
p42=pygame.image.load(photo2_file)
photo3_file="4 — копия (3).jpeg"
p43=pygame.image.load(photo3_file)
photo4_file="4 — копия (4).jpeg"
p44=pygame.image.load(photo4_file)
photo5_file="4 — копия (5).jpeg"
p45=pygame.image.load(photo5_file)
photo6_file="4 — копия (6).jpeg"
p46=pygame.image.load(photo6_file)
photo7_file="4 — копия (7).jpeg"
p47=pygame.image.load(photo7_file)
photo8_file="4 — копия (8).jpeg"
p48=pygame.image.load(photo8_file)
photo9_file="4 — копия (9).jpeg"
p49=pygame.image.load(photo9_file)
photo10_file="4 — копия (10).jpeg"
p410=pygame.image.load(photo10_file)
photo11_file="4 — копия (11).jpeg"
p411=pygame.image.load(photo11_file)
photo12_file="4 — копия (12).jpeg"
p412=pygame.image.load(photo12_file)
photo13_file="4 — копия (13).jpeg"
p413=pygame.image.load(photo13_file)
photo14_file="4 — копия (14).jpeg"
p414=pygame.image.load(photo14_file)
photo15_file="4 — копия (15).jpeg"
p415=pygame.image.load(photo15_file)
photo16_file="4 — копия (16).jpeg"
p416=pygame.image.load(photo16_file)
photo17_file="4 — копия (17).jpeg"
p417=pygame.image.load(photo17_file)
photo18_file="4 — копия (18).jpeg"
p418=pygame.image.load(photo18_file)
photo19_file="4 — копия (19).jpeg"
p419=pygame.image.load(photo19_file)
photo20_file="4 — копия (20).jpeg"
p420=pygame.image.load(photo20_file)
photo21_file="4 — копия (21).jpeg"
p421=pygame.image.load(photo21_file)
photo22_file="4 — копия (22).jpeg"
p422=pygame.image.load(photo22_file)
photo23_file="4 — копия (23).jpeg"
p423=pygame.image.load(photo23_file)
photo24_file="4 — копия (24).jpeg"
p424=pygame.image.load(photo24_file)
photo25_file="4 — копия (25).jpeg"
p425=pygame.image.load(photo25_file)
photo26_file="4 — копия (26).jpeg"
p426=pygame.image.load(photo26_file)
photo27_file="4 — копия (27).jpeg"
p427=pygame.image.load(photo27_file)
photo28_file="4 — копия (28).jpeg"
p428=pygame.image.load(photo28_file)
photo29_file="4 — копия (29).jpeg"
p429=pygame.image.load(photo29_file)
photo30_file="4 — копия (30).jpeg"
p430=pygame.image.load(photo30_file)
photo31_file="4 — копия (31).jpeg"
p431=pygame.image.load(photo31_file)
photo32_file="4 — копия (32).jpeg"
p432=pygame.image.load(photo32_file)
photo33_file="4 — копия (33).jpeg"
p433=pygame.image.load(photo33_file)
photo34_file="4 — копия (34).jpeg"
p434=pygame.image.load(photo34_file)
photo35_file="4 — копия (35).jpeg"
p435=pygame.image.load(photo35_file)
photo36_file="4 — копия (36).jpeg"
p436=pygame.image.load(photo36_file)
photo37_file="4 — копия (37).jpeg"
p437=pygame.image.load(photo37_file)
photo38_file="4 — копия (38).jpeg"
p438=pygame.image.load(photo38_file)
photo39_file="4 — копия (39).jpeg"
p439=pygame.image.load(photo39_file)
photo40_file="4 — копия (40).jpeg"
p440=pygame.image.load(photo40_file)
photo41_file="4 — копия (41).jpeg"
p441=pygame.image.load(photo41_file)
photo42_file="4 — копия (42).jpeg"
p442=pygame.image.load(photo42_file)
photo43_file="4 — копия (43).jpeg"
p443=pygame.image.load(photo43_file)
photo44_file="4 — копия (44).jpeg"
p444=pygame.image.load(photo44_file)
photo45_file="4 — копия (45).jpeg"
p445=pygame.image.load(photo45_file)
photo46_file="4 — копия (46).jpeg"
p446=pygame.image.load(photo46_file)
photo47_file="4 — копия (47).jpeg"
p447=pygame.image.load(photo47_file)
photo48_file="4 — копия (48).jpeg"
p448=pygame.image.load(photo48_file)
photo49_file="4 — копия (49).jpeg"
p449=pygame.image.load(photo49_file)


photo0_file="5.jpg"
p50=pygame.image.load(photo0_file)
photo1_file="5 — копия.jpg"
p51=pygame.image.load(photo1_file)
photo2_file="5 — копия (2).jpg"
p52=pygame.image.load(photo2_file)
photo3_file="5 — копия (3).jpg"
p53=pygame.image.load(photo3_file)
photo4_file="5 — копия (4).jpg"
p54=pygame.image.load(photo4_file)
photo5_file="5 — копия (5).jpg"
p55=pygame.image.load(photo5_file)
photo6_file="5 — копия (6).jpg"
p56=pygame.image.load(photo6_file)
photo7_file="5 — копия (7).jpg"
p57=pygame.image.load(photo7_file)
photo8_file="5 — копия (8).jpg"
p58=pygame.image.load(photo8_file)
photo9_file="5 — копия (9).jpg"
p59=pygame.image.load(photo9_file)
photo10_file="5 — копия (10).jpg"
p510=pygame.image.load(photo10_file)
photo11_file="5 — копия (11).jpg"
p511=pygame.image.load(photo11_file)
photo12_file="5 — копия (12).jpg"
p512=pygame.image.load(photo12_file)
photo13_file="5 — копия (13).jpg"
p513=pygame.image.load(photo13_file)
photo14_file="5 — копия (14).jpg"
p514=pygame.image.load(photo14_file)
photo15_file="5 — копия (15).jpg"
p515=pygame.image.load(photo15_file)
photo16_file="5 — копия (16).jpg"
p516=pygame.image.load(photo16_file)
photo17_file="5 — копия (17).jpg"
p517=pygame.image.load(photo17_file)
photo18_file="5 — копия (18).jpg"
p518=pygame.image.load(photo18_file)
photo19_file="5 — копия (19).jpg"
p519=pygame.image.load(photo19_file)
photo20_file="5 — копия (20).jpg"
p520=pygame.image.load(photo20_file)
photo21_file="5 — копия (21).jpg"
p521=pygame.image.load(photo21_file)
photo22_file="5 — копия (22).jpg"
p522=pygame.image.load(photo22_file)
photo23_file="5 — копия (23).jpg"
p523=pygame.image.load(photo23_file)
photo24_file="5 — копия (24).jpg"
p524=pygame.image.load(photo24_file)
photo25_file="5 — копия (25).jpg"
p525=pygame.image.load(photo25_file)
photo26_file="5 — копия (26).jpg"
p526=pygame.image.load(photo26_file)
photo27_file="5 — копия (27).jpg"
p527=pygame.image.load(photo27_file)
photo28_file="5 — копия (28).jpg"
p528=pygame.image.load(photo28_file)
photo29_file="5 — копия (29).jpg"
p529=pygame.image.load(photo29_file)
photo30_file="5 — копия (30).jpg"
p530=pygame.image.load(photo30_file)
photo31_file="5 — копия (31).jpg"
p531=pygame.image.load(photo31_file)
photo32_file="5 — копия (32).jpg"
p532=pygame.image.load(photo32_file)
photo33_file="5 — копия (33).jpg"
p533=pygame.image.load(photo33_file)
photo34_file="5 — копия (34).jpg"
p534=pygame.image.load(photo34_file)
photo35_file="5 — копия (35).jpg"
p535=pygame.image.load(photo35_file)
photo36_file="5 — копия (36).jpg"
p536=pygame.image.load(photo36_file)
photo37_file="5 — копия (37).jpg"
p537=pygame.image.load(photo37_file)
photo38_file="5 — копия (38).jpg"
p538=pygame.image.load(photo38_file)
photo39_file="5 — копия (39).jpg"
p539=pygame.image.load(photo39_file)
photo40_file="5 — копия (40).jpg"
p540=pygame.image.load(photo40_file)
photo41_file="5 — копия (41).jpg"
p541=pygame.image.load(photo41_file)
photo42_file="5 — копия (42).jpg"
p542=pygame.image.load(photo42_file)
photo43_file="5 — копия (43).jpg"
p543=pygame.image.load(photo43_file)
photo44_file="5 — копия (44).jpg"
p544=pygame.image.load(photo44_file)
photo45_file="5 — копия (45).jpg"
p545=pygame.image.load(photo45_file)
photo46_file="5 — копия (46).jpg"
p546=pygame.image.load(photo46_file)
photo47_file="5 — копия (47).jpg"
p547=pygame.image.load(photo47_file)
photo48_file="5 — копия (48).jpg"
p548=pygame.image.load(photo48_file)
photo49_file="5 — копия (49).jpg"
p549=pygame.image.load(photo49_file)

photo0_file="6.jpg"
p60=pygame.image.load(photo0_file)
photo1_file="6 — копия.jpg"
p61=pygame.image.load(photo1_file)
photo2_file="6 — копия (2).jpg"
p62=pygame.image.load(photo2_file)
photo3_file="6 — копия (3).jpg"
p63=pygame.image.load(photo3_file)
photo4_file="6 — копия (4).jpg"
p64=pygame.image.load(photo4_file)
photo5_file="6 — копия (5).jpg"
p65=pygame.image.load(photo5_file)
photo6_file="6 — копия (6).jpg"
p66=pygame.image.load(photo6_file)
photo7_file="6 — копия (7).jpg"
p67=pygame.image.load(photo7_file)
photo8_file="6 — копия (8).jpg"
p68=pygame.image.load(photo8_file)
photo9_file="6 — копия (9).jpg"
p69=pygame.image.load(photo9_file)
photo10_file="6 — копия (10).jpg"
p610=pygame.image.load(photo10_file)
photo11_file="6 — копия (11).jpg"
p611=pygame.image.load(photo11_file)
photo12_file="6 — копия (12).jpg"
p612=pygame.image.load(photo12_file)
photo13_file="6 — копия (13).jpg"
p613=pygame.image.load(photo13_file)
photo14_file="6 — копия (14).jpg"
p614=pygame.image.load(photo14_file)
photo15_file="6 — копия (15).jpg"
p615=pygame.image.load(photo15_file)
photo16_file="6 — копия (16).jpg"
p616=pygame.image.load(photo16_file)
photo17_file="6 — копия (17).jpg"
p617=pygame.image.load(photo17_file)
photo18_file="6 — копия (18).jpg"
p618=pygame.image.load(photo18_file)
photo19_file="6 — копия (19).jpg"
p619=pygame.image.load(photo19_file)
photo20_file="6 — копия (20).jpg"
p620=pygame.image.load(photo20_file)
photo21_file="6 — копия (21).jpg"
p621=pygame.image.load(photo21_file)
photo22_file="6 — копия (22).jpg"
p622=pygame.image.load(photo22_file)
photo23_file="6 — копия (23).jpg"
p623=pygame.image.load(photo23_file)
photo24_file="6 — копия (24).jpg"
p624=pygame.image.load(photo24_file)
photo25_file="6 — копия (25).jpg"
p625=pygame.image.load(photo25_file)
photo26_file="6 — копия (26).jpg"
p626=pygame.image.load(photo26_file)
photo27_file="6 — копия (27).jpg"
p627=pygame.image.load(photo27_file)
photo28_file="6 — копия (28).jpg"
p628=pygame.image.load(photo28_file)
photo29_file="6 — копия (29).jpg"
p629=pygame.image.load(photo29_file)
photo30_file="6 — копия (30).jpg"
p630=pygame.image.load(photo30_file)
photo31_file="6 — копия (31).jpg"
p631=pygame.image.load(photo31_file)
photo32_file="6 — копия (32).jpg"
p632=pygame.image.load(photo32_file)
photo33_file="6 — копия (33).jpg"
p633=pygame.image.load(photo33_file)
photo34_file="6 — копия (34).jpg"
p634=pygame.image.load(photo34_file)
photo35_file="6 — копия (35).jpg"
p635=pygame.image.load(photo35_file)
photo36_file="6 — копия (36).jpg"
p636=pygame.image.load(photo36_file)
photo37_file="6 — копия (37).jpg"
p637=pygame.image.load(photo37_file)
photo38_file="6 — копия (38).jpg"
p638=pygame.image.load(photo38_file)
photo39_file="6 — копия (39).jpg"
p639=pygame.image.load(photo39_file)
photo40_file="6 — копия (40).jpg"
p640=pygame.image.load(photo40_file)
photo41_file="6 — копия (41).jpg"
p641=pygame.image.load(photo41_file)
photo42_file="6 — копия (42).jpg"
p642=pygame.image.load(photo42_file)
photo43_file="6 — копия (43).jpg"
p643=pygame.image.load(photo43_file)
photo44_file="6 — копия (44).jpg"
p644=pygame.image.load(photo44_file)
photo45_file="6 — копия (45).jpg"
p645=pygame.image.load(photo45_file)
photo46_file="6 — копия (46).jpg"
p646=pygame.image.load(photo46_file)
photo47_file="6 — копия (47).jpg"
p647=pygame.image.load(photo47_file)
photo48_file="6 — копия (48).jpg"
p648=pygame.image.load(photo48_file)
photo49_file="6 — копия (49).jpg"
p649=pygame.image.load(photo49_file)

photo0_file="7.jpg"
p70=pygame.image.load(photo0_file)
photo1_file="7 — копия.jpg"
p71=pygame.image.load(photo1_file)
photo2_file="7 — копия (2).jpg"
p72=pygame.image.load(photo2_file)
photo3_file="7 — копия (3).jpg"
p73=pygame.image.load(photo3_file)
photo4_file="7 — копия (4).jpg"
p74=pygame.image.load(photo4_file)
photo5_file="7 — копия (5).jpg"
p75=pygame.image.load(photo5_file)
photo6_file="7 — копия (6).jpg"
p76=pygame.image.load(photo6_file)
photo7_file="7 — копия (7).jpg"
p77=pygame.image.load(photo7_file)
photo8_file="7 — копия (8).jpg"
p78=pygame.image.load(photo8_file)
photo9_file="7 — копия (9).jpg"
p79=pygame.image.load(photo9_file)
photo10_file="7 — копия (10).jpg"
p710=pygame.image.load(photo10_file)
photo11_file="7 — копия (11).jpg"
p711=pygame.image.load(photo11_file)
photo12_file="7 — копия (12).jpg"
p712=pygame.image.load(photo12_file)
photo13_file="7 — копия (13).jpg"
p713=pygame.image.load(photo13_file)
photo14_file="7 — копия (14).jpg"
p714=pygame.image.load(photo14_file)
photo15_file="7 — копия (15).jpg"
p715=pygame.image.load(photo15_file)
photo16_file="7 — копия (16).jpg"
p716=pygame.image.load(photo16_file)
photo17_file="7 — копия (17).jpg"
p717=pygame.image.load(photo17_file)
photo18_file="7 — копия (18).jpg"
p718=pygame.image.load(photo18_file)
photo19_file="7 — копия (19).jpg"
p719=pygame.image.load(photo19_file)
photo20_file="7 — копия (20).jpg"
p720=pygame.image.load(photo20_file)
photo21_file="7 — копия (21).jpg"
p721=pygame.image.load(photo21_file)
photo22_file="7 — копия (22).jpg"
p722=pygame.image.load(photo22_file)
photo23_file="7 — копия (23).jpg"
p723=pygame.image.load(photo23_file)
photo24_file="7 — копия (24).jpg"
p724=pygame.image.load(photo24_file)
photo25_file="7 — копия (25).jpg"
p725=pygame.image.load(photo25_file)
photo26_file="7 — копия (26).jpg"
p726=pygame.image.load(photo26_file)
photo27_file="7 — копия (27).jpg"
p727=pygame.image.load(photo27_file)
photo28_file="7 — копия (28).jpg"
p728=pygame.image.load(photo28_file)
photo29_file="7 — копия (29).jpg"
p729=pygame.image.load(photo29_file)
photo30_file="7 — копия (30).jpg"
p730=pygame.image.load(photo30_file)
photo31_file="7 — копия (31).jpg"
p731=pygame.image.load(photo31_file)
photo32_file="7 — копия (32).jpg"
p732=pygame.image.load(photo32_file)
photo33_file="7 — копия (33).jpg"
p733=pygame.image.load(photo33_file)
photo34_file="7 — копия (34).jpg"
p734=pygame.image.load(photo34_file)
photo35_file="7 — копия (35).jpg"
p735=pygame.image.load(photo35_file)
photo36_file="7 — копия (36).jpg"
p736=pygame.image.load(photo36_file)
photo37_file="7 — копия (37).jpg"
p737=pygame.image.load(photo37_file)
photo38_file="7 — копия (38).jpg"
p738=pygame.image.load(photo38_file)
photo39_file="7 — копия (39).jpg"
p739=pygame.image.load(photo39_file)
photo40_file="7 — копия (40).jpg"
p740=pygame.image.load(photo40_file)
photo41_file="7 — копия (41).jpg"
p741=pygame.image.load(photo41_file)
photo42_file="7 — копия (42).jpg"
p742=pygame.image.load(photo42_file)
photo43_file="7 — копия (43).jpg"
p743=pygame.image.load(photo43_file)
photo44_file="7 — копия (44).jpg"
p744=pygame.image.load(photo44_file)
photo45_file="7 — копия (45).jpg"
p745=pygame.image.load(photo45_file)
photo46_file="7 — копия (46).jpg"
p746=pygame.image.load(photo46_file)
photo47_file="7 — копия (47).jpg"
p747=pygame.image.load(photo47_file)
photo48_file="7 — копия (48).jpg"
p748=pygame.image.load(photo48_file)
photo49_file="7 — копия (49).jpg"
p749=pygame.image.load(photo49_file)


photo0_file="8.jpg"
p80=pygame.image.load(photo0_file)
photo1_file="8 — копия.jpg"
p81=pygame.image.load(photo1_file)
photo2_file="8 — копия (2).jpg"
p82=pygame.image.load(photo2_file)
photo3_file="8 — копия (3).jpg"
p83=pygame.image.load(photo3_file)
photo4_file="8 — копия (4).jpg"
p84=pygame.image.load(photo4_file)
photo5_file="8 — копия (5).jpg"
p85=pygame.image.load(photo5_file)
photo6_file="8 — копия (6).jpg"
p86=pygame.image.load(photo6_file)
photo7_file="8 — копия (7).jpg"
p87=pygame.image.load(photo7_file)
photo8_file="8 — копия (8).jpg"
p88=pygame.image.load(photo8_file)
photo9_file="8 — копия (9).jpg"
p89=pygame.image.load(photo9_file)
photo10_file="8 — копия (10).jpg"
p810=pygame.image.load(photo10_file)
photo11_file="8 — копия (11).jpg"
p811=pygame.image.load(photo11_file)
photo12_file="8 — копия (12).jpg"
p812=pygame.image.load(photo12_file)
photo13_file="8 — копия (13).jpg"
p813=pygame.image.load(photo13_file)
photo14_file="8 — копия (14).jpg"
p814=pygame.image.load(photo14_file)
photo15_file="8 — копия (15).jpg"
p815=pygame.image.load(photo15_file)
photo16_file="8 — копия (16).jpg"
p816=pygame.image.load(photo16_file)
photo17_file="8 — копия (17).jpg"
p817=pygame.image.load(photo17_file)
photo18_file="8 — копия (18).jpg"
p818=pygame.image.load(photo18_file)
photo19_file="8 — копия (19).jpg"
p819=pygame.image.load(photo19_file)
photo20_file="8 — копия (20).jpg"
p820=pygame.image.load(photo20_file)
photo21_file="8 — копия (21).jpg"
p821=pygame.image.load(photo21_file)
photo22_file="8 — копия (22).jpg"
p822=pygame.image.load(photo22_file)
photo23_file="8 — копия (23).jpg"
p823=pygame.image.load(photo23_file)
photo24_file="8 — копия (24).jpg"
p824=pygame.image.load(photo24_file)
photo25_file="8 — копия (25).jpg"
p825=pygame.image.load(photo25_file)
photo26_file="8 — копия (26).jpg"
p826=pygame.image.load(photo26_file)
photo27_file="8 — копия (27).jpg"
p827=pygame.image.load(photo27_file)
photo28_file="8 — копия (28).jpg"
p828=pygame.image.load(photo28_file)
photo29_file="8 — копия (29).jpg"
p829=pygame.image.load(photo29_file)
photo30_file="8 — копия (30).jpg"
p830=pygame.image.load(photo30_file)
photo31_file="8 — копия (31).jpg"
p831=pygame.image.load(photo31_file)
photo32_file="8 — копия (32).jpg"
p832=pygame.image.load(photo32_file)
photo33_file="8 — копия (33).jpg"
p833=pygame.image.load(photo33_file)
photo34_file="8 — копия (34).jpg"
p834=pygame.image.load(photo34_file)
photo35_file="8 — копия (35).jpg"
p835=pygame.image.load(photo35_file)
photo36_file="8 — копия (36).jpg"
p836=pygame.image.load(photo36_file)
photo37_file="8 — копия (37).jpg"
p837=pygame.image.load(photo37_file)
photo38_file="8 — копия (38).jpg"
p838=pygame.image.load(photo38_file)
photo39_file="8 — копия (39).jpg"
p839=pygame.image.load(photo39_file)
photo40_file="8 — копия (40).jpg"
p840=pygame.image.load(photo40_file)
photo41_file="8 — копия (41).jpg"
p841=pygame.image.load(photo41_file)
photo42_file="8 — копия (42).jpg"
p842=pygame.image.load(photo42_file)
photo43_file="8 — копия (43).jpg"
p843=pygame.image.load(photo43_file)
photo44_file="8 — копия (44).jpg"
p844=pygame.image.load(photo44_file)
photo45_file="8 — копия (45).jpg"
p845=pygame.image.load(photo45_file)
photo46_file="8 — копия (46).jpg"
p846=pygame.image.load(photo46_file)
photo47_file="8 — копия (47).jpg"
p847=pygame.image.load(photo47_file)
photo48_file="8 — копия (48).jpg"
p848=pygame.image.load(photo48_file)
photo49_file="8 — копия (49).jpg"
p849=pygame.image.load(photo49_file)

photo0_file="9.jpg"
p90=pygame.image.load(photo0_file)
photo1_file="9 — копия.jpg"
p91=pygame.image.load(photo1_file)
photo2_file="9 — копия (2).jpg"
p92=pygame.image.load(photo2_file)
photo3_file="9 — копия (3).jpg"
p93=pygame.image.load(photo3_file)
photo4_file="9 — копия (4).jpg"
p94=pygame.image.load(photo4_file)
photo5_file="9 — копия (5).jpg"
p95=pygame.image.load(photo5_file)
photo6_file="9 — копия (6).jpg"
p96=pygame.image.load(photo6_file)
photo7_file="9 — копия (7).jpg"
p97=pygame.image.load(photo7_file)
photo8_file="9 — копия (8).jpg"
p98=pygame.image.load(photo8_file)
photo9_file="9 — копия (9).jpg"
p99=pygame.image.load(photo9_file)
photo10_file="9 — копия (10).jpg"
p910=pygame.image.load(photo10_file)
photo11_file="9 — копия (11).jpg"
p911=pygame.image.load(photo11_file)
photo12_file="9 — копия (12).jpg"
p912=pygame.image.load(photo12_file)
photo13_file="9 — копия (13).jpg"
p913=pygame.image.load(photo13_file)
photo14_file="9 — копия (14).jpg"
p914=pygame.image.load(photo14_file)
photo15_file="9 — копия (15).jpg"
p915=pygame.image.load(photo15_file)
photo16_file="9 — копия (16).jpg"
p916=pygame.image.load(photo16_file)
photo17_file="9 — копия (17).jpg"
p917=pygame.image.load(photo17_file)
photo18_file="9 — копия (18).jpg"
p918=pygame.image.load(photo18_file)
photo19_file="9 — копия (19).jpg"
p919=pygame.image.load(photo19_file)
photo20_file="9 — копия (20).jpg"
p920=pygame.image.load(photo20_file)
photo21_file="9 — копия (21).jpg"
p921=pygame.image.load(photo21_file)
photo22_file="9 — копия (22).jpg"
p922=pygame.image.load(photo22_file)
photo23_file="9 — копия (23).jpg"
p923=pygame.image.load(photo23_file)
photo24_file="9 — копия (24).jpg"
p924=pygame.image.load(photo24_file)
photo25_file="9 — копия (25).jpg"
p925=pygame.image.load(photo25_file)
photo26_file="9 — копия (26).jpg"
p926=pygame.image.load(photo26_file)
photo27_file="9 — копия (27).jpg"
p927=pygame.image.load(photo27_file)
photo28_file="9 — копия (28).jpg"
p928=pygame.image.load(photo28_file)
photo29_file="9 — копия (29).jpg"
p929=pygame.image.load(photo29_file)
photo30_file="9 — копия (30).jpg"
p930=pygame.image.load(photo30_file)
photo31_file="9 — копия (31).jpg"
p931=pygame.image.load(photo31_file)
photo32_file="9 — копия (32).jpg"
p932=pygame.image.load(photo32_file)
photo33_file="9 — копия (33).jpg"
p933=pygame.image.load(photo33_file)
photo34_file="9 — копия (34).jpg"
p934=pygame.image.load(photo34_file)
photo35_file="9 — копия (35).jpg"
p935=pygame.image.load(photo35_file)
photo36_file="9 — копия (36).jpg"
p936=pygame.image.load(photo36_file)
photo37_file="9 — копия (37).jpg"
p937=pygame.image.load(photo37_file)
photo38_file="9 — копия (38).jpg"
p938=pygame.image.load(photo38_file)
photo39_file="9 — копия (39).jpg"
p939=pygame.image.load(photo39_file)
photo40_file="9 — копия (40).jpg"
p940=pygame.image.load(photo40_file)
photo41_file="9 — копия (41).jpg"
p941=pygame.image.load(photo41_file)
photo42_file="9 — копия (42).jpg"
p942=pygame.image.load(photo42_file)
photo43_file="9 — копия (43).jpg"
p943=pygame.image.load(photo43_file)
photo44_file="9 — копия (44).jpg"
p944=pygame.image.load(photo44_file)
photo45_file="9 — копия (45).jpg"
p945=pygame.image.load(photo45_file)
photo46_file="9 — копия (46).jpg"
p946=pygame.image.load(photo46_file)
photo47_file="9 — копия (47).jpg"
p947=pygame.image.load(photo47_file)
photo48_file="9 — копия (48).jpg"
p948=pygame.image.load(photo48_file)
photo49_file="9 — копия (49).jpg"
p949=pygame.image.load(photo49_file)

photo0_file="10.jpg"
p100=pygame.image.load(photo0_file)
photo1_file="10 — копия.jpg"
p101=pygame.image.load(photo1_file)
photo2_file="10 — копия (2).jpg"
p102=pygame.image.load(photo2_file)
photo3_file="10 — копия (3).jpg"
p103=pygame.image.load(photo3_file)
photo4_file="10 — копия (4).jpg"
p104=pygame.image.load(photo4_file)
photo5_file="10 — копия (5).jpg"
p105=pygame.image.load(photo5_file)
photo6_file="10 — копия (6).jpg"
p106=pygame.image.load(photo6_file)
photo7_file="10 — копия (7).jpg"
p107=pygame.image.load(photo7_file)
photo8_file="10 — копия (8).jpg"
p108=pygame.image.load(photo8_file)
photo9_file="10 — копия (9).jpg"
p109=pygame.image.load(photo9_file)
photo10_file="10 — копия (10).jpg"
p1010=pygame.image.load(photo10_file)
photo11_file="10 — копия (11).jpg"
p1011=pygame.image.load(photo11_file)
photo12_file="10 — копия (12).jpg"
p1012=pygame.image.load(photo12_file)
photo13_file="10 — копия (13).jpg"
p1013=pygame.image.load(photo13_file)
photo14_file="10 — копия (14).jpg"
p1014=pygame.image.load(photo14_file)
photo15_file="10 — копия (15).jpg"
p1015=pygame.image.load(photo15_file)
photo16_file="10 — копия (16).jpg"
p1016=pygame.image.load(photo16_file)
photo17_file="10 — копия (17).jpg"
p1017=pygame.image.load(photo17_file)
photo18_file="10 — копия (18).jpg"
p1018=pygame.image.load(photo18_file)
photo19_file="10 — копия (19).jpg"
p1019=pygame.image.load(photo19_file)
photo20_file="10 — копия (20).jpg"
p1020=pygame.image.load(photo20_file)
photo21_file="10 — копия (21).jpg"
p1021=pygame.image.load(photo21_file)
photo22_file="10 — копия (22).jpg"
p1022=pygame.image.load(photo22_file)
photo23_file="10 — копия (23).jpg"
p1023=pygame.image.load(photo23_file)
photo24_file="10 — копия (24).jpg"
p1024=pygame.image.load(photo24_file)
photo25_file="10 — копия (25).jpg"
p1025=pygame.image.load(photo25_file)
photo26_file="10 — копия (26).jpg"
p1026=pygame.image.load(photo26_file)
photo27_file="10 — копия (27).jpg"
p1027=pygame.image.load(photo27_file)
photo28_file="10 — копия (28).jpg"
p1028=pygame.image.load(photo28_file)
photo29_file="10 — копия (29).jpg"
p1029=pygame.image.load(photo29_file)
photo30_file="10 — копия (30).jpg"
p1030=pygame.image.load(photo30_file)
photo31_file="10 — копия (31).jpg"
p1031=pygame.image.load(photo31_file)
photo32_file="10 — копия (32).jpg"
p1032=pygame.image.load(photo32_file)
photo33_file="10 — копия (33).jpg"
p1033=pygame.image.load(photo33_file)
photo34_file="10 — копия (34).jpg"
p1034=pygame.image.load(photo34_file)
photo35_file="10 — копия (35).jpg"
p1035=pygame.image.load(photo35_file)
photo36_file="10 — копия (36).jpg"
p1036=pygame.image.load(photo36_file)
photo37_file="10 — копия (37).jpg"
p1037=pygame.image.load(photo37_file)
photo38_file="10 — копия (38).jpg"
p1038=pygame.image.load(photo38_file)
photo39_file="10 — копия (39).jpg"
p1039=pygame.image.load(photo39_file)
photo40_file="10 — копия (40).jpg"
p1040=pygame.image.load(photo40_file)
photo41_file="10 — копия (41).jpg"
p1041=pygame.image.load(photo41_file)
photo42_file="10 — копия (42).jpg"
p1042=pygame.image.load(photo42_file)
photo43_file="10 — копия (43).jpg"
p1043=pygame.image.load(photo43_file)
photo44_file="10 — копия (44).jpg"
p1044=pygame.image.load(photo44_file)
photo45_file="10 — копия (45).jpg"
p1045=pygame.image.load(photo45_file)
photo46_file="10 — копия (46).jpg"
p1046=pygame.image.load(photo46_file)
photo47_file="10 — копия (47).jpg"
p1047=pygame.image.load(photo47_file)
photo48_file="10 — копия (48).jpg"
p1048=pygame.image.load(photo48_file)
photo49_file="10 — копия (49).jpg"
p1049=pygame.image.load(photo49_file)


photo0_file="11.jfif"
p110=pygame.image.load(photo0_file)
photo1_file="11 — копия.jfif"
p111=pygame.image.load(photo1_file)
photo2_file="11 — копия (2).jfif"
p112=pygame.image.load(photo2_file)
photo3_file="11 — копия (3).jfif"
p113=pygame.image.load(photo3_file)
photo4_file="11 — копия (4).jfif"
p114=pygame.image.load(photo4_file)
photo5_file="11 — копия (5).jfif"
p115=pygame.image.load(photo5_file)
photo6_file="11 — копия (6).jfif"
p116=pygame.image.load(photo6_file)
photo7_file="11 — копия (7).jfif"
p117=pygame.image.load(photo7_file)
photo8_file="11 — копия (8).jfif"
p118=pygame.image.load(photo8_file)
photo9_file="11 — копия (9).jfif"
p119=pygame.image.load(photo9_file)
photo10_file="11 — копия (10).jfif"
p1110=pygame.image.load(photo10_file)
photo11_file="11 — копия (11).jfif"
p1111=pygame.image.load(photo11_file)
photo12_file="11 — копия (12).jfif"
p1112=pygame.image.load(photo12_file)
photo13_file="11 — копия (13).jfif"
p1113=pygame.image.load(photo13_file)
photo14_file="11 — копия (14).jfif"
p1114=pygame.image.load(photo14_file)
photo15_file="11 — копия (15).jfif"
p1115=pygame.image.load(photo15_file)
photo16_file="11 — копия (16).jfif"
p1116=pygame.image.load(photo16_file)
photo17_file="11 — копия (17).jfif"
p1117=pygame.image.load(photo17_file)
photo18_file="11 — копия (18).jfif"
p1118=pygame.image.load(photo18_file)
photo19_file="11 — копия (19).jfif"
p1119=pygame.image.load(photo19_file)
photo20_file="11 — копия (20).jfif"
p1120=pygame.image.load(photo20_file)
photo21_file="11 — копия (21).jfif"
p1121=pygame.image.load(photo21_file)
photo22_file="11 — копия (22).jfif"
p1122=pygame.image.load(photo22_file)
photo23_file="11 — копия (23).jfif"
p1123=pygame.image.load(photo23_file)
photo24_file="11 — копия (24).jfif"
p1124=pygame.image.load(photo24_file)
photo25_file="11 — копия (25).jfif"
p1125=pygame.image.load(photo25_file)
photo26_file="11 — копия (26).jfif"
p1126=pygame.image.load(photo26_file)
photo27_file="11 — копия (27).jfif"
p1127=pygame.image.load(photo27_file)
photo28_file="11 — копия (28).jfif"
p1128=pygame.image.load(photo28_file)
photo29_file="11 — копия (29).jfif"
p1129=pygame.image.load(photo29_file)
photo30_file="11 — копия (30).jfif"
p1130=pygame.image.load(photo30_file)
photo31_file="11 — копия (31).jfif"
p1131=pygame.image.load(photo31_file)
photo32_file="11 — копия (32).jfif"
p1132=pygame.image.load(photo32_file)
photo33_file="11 — копия (33).jfif"
p1133=pygame.image.load(photo33_file)
photo34_file="11 — копия (34).jfif"
p1134=pygame.image.load(photo34_file)
photo35_file="11 — копия (35).jfif"
p1135=pygame.image.load(photo35_file)
photo36_file="11 — копия (36).jfif"
p1136=pygame.image.load(photo36_file)
photo37_file="11 — копия (37).jfif"
p1137=pygame.image.load(photo37_file)
photo38_file="11 — копия (38).jfif"
p1138=pygame.image.load(photo38_file)
photo39_file="11 — копия (39).jfif"
p1139=pygame.image.load(photo39_file)
photo40_file="11 — копия (40).jfif"
p1140=pygame.image.load(photo40_file)
photo41_file="11 — копия (41).jfif"
p1141=pygame.image.load(photo41_file)
photo42_file="11 — копия (42).jfif"
p1142=pygame.image.load(photo42_file)
photo43_file="11 — копия (43).jfif"
p1143=pygame.image.load(photo43_file)
photo44_file="11 — копия (44).jfif"
p1144=pygame.image.load(photo44_file)
photo45_file="11 — копия (45).jfif"
p1145=pygame.image.load(photo45_file)
photo46_file="11 — копия (46).jfif"
p1146=pygame.image.load(photo46_file)
photo47_file="11 — копия (47).jfif"
p1147=pygame.image.load(photo47_file)
photo48_file="11 — копия (48).jfif"
p1148=pygame.image.load(photo48_file)
photo49_file="11 — копия (49).jfif"
p1149=pygame.image.load(photo49_file)



photo0_file="12.jpg"
p1200=pygame.image.load(photo0_file)
photo1_file="12 — копия.jpg"
p1201=pygame.image.load(photo1_file)
photo2_file="12 — копия (2).jpg"
p1202=pygame.image.load(photo2_file)
photo3_file="12 — копия (3).jpg"
p1203=pygame.image.load(photo3_file)
photo4_file="12 — копия (4).jpg"
p1204=pygame.image.load(photo4_file)
photo5_file="12 — копия (5).jpg"
p1205=pygame.image.load(photo5_file)
photo6_file="12 — копия (6).jpg"
p1206=pygame.image.load(photo6_file)
photo7_file="12 — копия (7).jpg"
p1207=pygame.image.load(photo7_file)
photo8_file="12 — копия (8).jpg"
p1208=pygame.image.load(photo8_file)
photo9_file="12 — копия (9).jpg"
p1209=pygame.image.load(photo9_file)
photo10_file="12 — копия (10).jpg"
p1210=pygame.image.load(photo10_file)
photo11_file="12 — копия (11).jpg"
p1211=pygame.image.load(photo11_file)
photo12_file="12 — копия (12).jpg"
p1212=pygame.image.load(photo12_file)
photo13_file="12 — копия (13).jpg"
p1213=pygame.image.load(photo13_file)
photo14_file="12 — копия (14).jpg"
p1214=pygame.image.load(photo14_file)
photo15_file="12 — копия (15).jpg"
p1215=pygame.image.load(photo15_file)
photo16_file="12 — копия (16).jpg"
p1216=pygame.image.load(photo16_file)
photo17_file="12 — копия (17).jpg"
p1217=pygame.image.load(photo17_file)
photo18_file="12 — копия (18).jpg"
p1218=pygame.image.load(photo18_file)
photo19_file="12 — копия (19).jpg"
p1219=pygame.image.load(photo19_file)
photo20_file="12 — копия (20).jpg"
p1220=pygame.image.load(photo20_file)
photo21_file="12 — копия (21).jpg"
p1221=pygame.image.load(photo21_file)
photo22_file="12 — копия (22).jpg"
p1222=pygame.image.load(photo22_file)
photo23_file="12 — копия (23).jpg"
p1223=pygame.image.load(photo23_file)
photo24_file="12 — копия (24).jpg"
p1224=pygame.image.load(photo24_file)
photo25_file="12 — копия (25).jpg"
p1225=pygame.image.load(photo25_file)
photo26_file="12 — копия (26).jpg"
p1226=pygame.image.load(photo26_file)
photo27_file="12 — копия (27).jpg"
p1227=pygame.image.load(photo27_file)
photo28_file="12 — копия (28).jpg"
p1228=pygame.image.load(photo28_file)
photo29_file="12 — копия (29).jpg"
p1229=pygame.image.load(photo29_file)
photo30_file="12 — копия (30).jpg"
p1230=pygame.image.load(photo30_file)
photo31_file="12 — копия (31).jpg"
p1231=pygame.image.load(photo31_file)
photo32_file="12 — копия (32).jpg"
p1232=pygame.image.load(photo32_file)
photo33_file="12 — копия (33).jpg"
p1233=pygame.image.load(photo33_file)
photo34_file="12 — копия (34).jpg"
p1234=pygame.image.load(photo34_file)
photo35_file="12 — копия (35).jpg"
p1235=pygame.image.load(photo35_file)
photo36_file="12 — копия (36).jpg"
p1236=pygame.image.load(photo36_file)
photo37_file="12 — копия (37).jpg"
p1237=pygame.image.load(photo37_file)
photo38_file="12 — копия (38).jpg"
p1238=pygame.image.load(photo38_file)
photo39_file="12 — копия (39).jpg"
p1239=pygame.image.load(photo39_file)
photo40_file="12 — копия (40).jpg"
p1240=pygame.image.load(photo40_file)
photo41_file="12 — копия (41).jpg"
p1241=pygame.image.load(photo41_file)
photo42_file="12 — копия (42).jpg"
p1242=pygame.image.load(photo42_file)
photo43_file="12 — копия (43).jpg"
p1243=pygame.image.load(photo43_file)
photo44_file="12 — копия (44).jpg"
p1244=pygame.image.load(photo44_file)
photo45_file="12 — копия (45).jpg"
p1245=pygame.image.load(photo45_file)
photo46_file="12 — копия (46).jpg"
p1246=pygame.image.load(photo46_file)
photo47_file="12 — копия (47).jpg"
p1247=pygame.image.load(photo47_file)
photo48_file="12 — копия (48).jpg"
p1248=pygame.image.load(photo48_file)
photo49_file="12 — копия (49).jpg"
p1249=pygame.image.load(photo49_file)

php=[p1p1,p1p49,p1p48,p1p47,p1p46,p1p45,p1p44,p1p43,p1p42,p1p41,p1p40,p1p39,p1p38,p1p37,p1p36,p1p35,p1p34,p1p33,p1p32,p1p31
     ,p1p30,p1p29,p1p28,p1p27,p1p26,p1p25,p1p24,p1p23,p1p22,p1p21,p1p20,p1p19,p1p18,p1p17,p1p16,p1p15,p1p14,p1p13,p1p12,
     p1p11,p1p10,p1p9,p1p8,p1p7,p1p6,p1p5,p1p4,p1p3,p1p2,p1p0,
     p1p0,p1p2,p1p3,p1p4,p1p5,p1p6,p1p7,p1p8,p1p9,p1p10,p1p11,p1p12,p1p13,p1p14,p1p15,p1p16,p1p17,p1p18,p1p19,p1p20
     ,p1p21,p1p22,p1p23,p1p24,p1p25,p1p26,p1p27,p1p28,p1p29,p1p30,p1p31,p1p32,p1p33,p1p34,p1p35,p1p36,p1p37,p1p38,p1p39,
     p1p40,p1p41,p1p42,p1p43,p1p44,p1p45,p1p46,p1p47,p1p48,p1p49,p1p1,
     
     p2p9,p2p49,p2p48,p2p47,p2p46,p2p45,p2p44,p2p43,p2p42,p2p41,p2p40,p2p39,p2p38,p2p37,p2p36,p2p35,p2p34,p2p33,p2p32,p2p31
     ,p2p30,p2p29,p2p28,p2p27,p2p26,p2p25,p2p24,p2p23,p2p22,p2p21,p2p20,p2p19,p2p18,p2p17,p2p16,p2p15,p2p14,p2p13,p2p12,
     p2p11,p2p10,p2p0,p2p1,p2p2,p2p3,p2p4,p2p5,p2p6,p2p7,p2p8,
     p2p8,p2p7,p2p6,p2p5,p2p4,p2p3,p2p2,p2p1,p2p0,p2p10,p2p11,p2p12,p2p13,p2p14,p2p15,p2p16,p2p17,p2p18,p2p19,p2p20
     ,p2p21,p2p22,p2p23,p2p24,p2p25,p2p26,p2p27,p2p28,p2p29,p2p30,p2p31,p2p32,p2p33,p2p34,p2p35,p2p36,p2p37,p2p38,p2p39,
     p2p40,p2p41,p2p42,p2p43,p2p44,p2p45,p2p46,p2p47,p2p48,p2p49,p2p9,

    p31,p349,p348,p347,p346,p345,p344,p343,p342,p341,p340,p339,p338,p337,p336,p335,p334,p333,p332,p331
     ,p330,p329,p328,p327,p326,p325,p324,p323,p322,p321,p320,p319,p318,p317,p316,p315,p314,p313,p312,
     p311,p310,p39,p38,p37,p36,p35,p34,p33,p32,p30,
     p30,p32,p33,p34,p35,p36,p37,p38,p39,p310,p311,p312,p313,p314,p315,p316,p317,p318,p319,p320
     ,p321,p322,p323,p324,p325,p326,p327,p328,p329,p330,p331,p332,p333,p334,p335,p336,p337,p338,p339,
     p340,p341,p342,p343,p344,p345,p346,p347,p348,p349,p31,

    p41,p449,p448,p447,p446,p445,p444,p443,p442,p441,p440,p439,p438,p437,p436,p435,p434,p433,p432,p431
     ,p430,p429,p428,p427,p426,p425,p424,p423,p422,p421,p420,p419,p418,p417,p416,p415,p414,p413,p412,
     p411,p410,p49,p48,p47,p46,p45,p44,p43,p42,p40,
     p40,p42,p43,p44,p45,p46,p47,p48,p49,p410,p411,p412,p413,p414,p415,p416,p417,p418,p419,p420
     ,p421,p422,p423,p424,p425,p426,p427,p428,p429,p430,p431,p432,p433,p434,p435,p436,p437,p438,p439,
     p440,p441,p442,p443,p444,p445,p446,p447,p448,p449,p41,

    p51,p549,p548,p547,p546,p545,p544,p543,p542,p541,p540,p539,p538,p537,p536,p535,p534,p533,p532,p531
     ,p530,p529,p528,p527,p526,p525,p524,p523,p522,p521,p520,p519,p518,p517,p516,p515,p514,p513,p512,
     p511,p510,p59,p58,p57,p56,p55,p54,p53,p52,p50,
     p50,p52,p53,p54,p55,p56,p57,p58,p59,p510,p511,p512,p513,p514,p515,p516,p517,p518,p519,p520
     ,p521,p522,p523,p524,p525,p526,p527,p528,p529,p530,p531,p532,p533,p534,p535,p536,p537,p538,p539,
     p540,p541,p542,p543,p544,p545,p546,p547,p548,p549,p51,


    p61,p649,p648,p647,p646,p645,p644,p643,p642,p641,p640,p639,p638,p637,p636,p635,p634,p633,p632,p631
     ,p630,p629,p628,p627,p626,p625,p624,p623,p622,p621,p620,p619,p618,p617,p616,p615,p614,p613,p612,
     p611,p610,p69,p68,p67,p66,p65,p64,p63,p62,p60,
     p60,p62,p63,p64,p65,p66,p67,p68,p69,p610,p611,p612,p613,p614,p615,p616,p617,p618,p619,p620
     ,p621,p622,p623,p624,p625,p626,p627,p628,p629,p630,p631,p632,p633,p634,p635,p636,p637,p638,p639,
     p640,p641,p642,p643,p644,p645,p646,p647,p648,p649,p61,

    p71,p749,p748,p747,p746,p745,p744,p743,p742,p741,p740,p739,p738,p737,p736,p735,p734,p733,p732,p731
     ,p730,p729,p728,p727,p726,p725,p724,p723,p722,p721,p720,p719,p718,p717,p716,p715,p714,p713,p712,
     p711,p710,p79,p78,p77,p76,p75,p74,p73,p72,p70,
     p70,p72,p73,p74,p75,p76,p77,p78,p79,p710,p711,p712,p713,p714,p715,p716,p717,p718,p719,p720
     ,p721,p722,p723,p724,p725,p726,p727,p728,p729,p730,p731,p732,p733,p734,p735,p736,p737,p738,p739,
     p740,p741,p742,p743,p744,p745,p746,p747,p648,p749,p71,


    p81,p849,p848,p847,p846,p845,p844,p843,p842,p841,p840,p839,p838,p837,p836,p835,p834,p833,p832,p831
     ,p830,p829,p828,p827,p826,p825,p824,p823,p822,p821,p820,p819,p818,p817,p816,p815,p814,p813,p812,
     p811,p810,p89,p88,p87,p86,p85,p84,p83,p82,p80,
     p80,p82,p83,p84,p85,p86,p87,p88,p89,p810,p811,p812,p813,p814,p815,p816,p817,p818,p819,p820
     ,p821,p822,p823,p824,p825,p826,p827,p828,p829,p830,p831,p832,p833,p834,p835,p836,p837,p838,p839,
     p840,p841,p842,p843,p844,p845,p846,p847,p848,p849,p81,


    p91,p949,p948,p947,p946,p945,p944,p943,p942,p941,p940,p939,p938,p937,p936,p935,p934,p933,p932,p931
     ,p930,p929,p928,p927,p926,p925,p924,p923,p922,p921,p920,p919,p918,p917,p916,p915,p914,p913,p912,
     p911,p910,p99,p98,p97,p96,p95,p94,p93,p92,p90,
     p90,p92,p93,p94,p95,p96,p97,p98,p99,p910,p911,p912,p913,p914,p915,p916,p917,p918,p919,p920
     ,p921,p922,p923,p924,p925,p926,p927,p928,p929,p930,p931,p932,p933,p934,p935,p936,p937,p938,p939,
     p940,p941,p942,p943,p944,p945,p946,p947,p948,p949,p91,


    p101,p1049,p1048,p1047,p1046,p1045,p1044,p1043,p1042,p1041,p1040,p1039,p1038,p1037,p1036,p1035,p1034,p1033,p1032,p1031
     ,p1030,p1029,p1028,p1027,p1026,p1025,p1024,p1023,p1022,p1021,p1020,p1019,p1018,p1017,p1016,p1015,p1014,p1013,p1012,
     p1011,p1010,p109,p108,p107,p106,p105,p104,p103,p102,p100,
     p100,p102,p103,p104,p105,p106,p107,p108,p109,p1010,p1011,p1012,p1013,p1014,p1015,p1016,p1017,p1018,p1019,p1020
     ,p1021,p1022,p1023,p1024,p1025,p1026,p1027,p1028,p1029,p1030,p1031,p1032,p1033,p1034,p1035,p1036,p1037,p1038,p1039,
     p1040,p1041,p1042,p1043,p1044,p1045,p1046,p1047,p1048,p1049,p101,


    p111,p1149,p1148,p1147,p1146,p1145,p1144,p1143,p1142,p1141,p1140,p1139,p1138,p1137,p1136,p1135,p1134,p1133,p1132,p1131
     ,p1130,p1129,p1128,p1127,p1126,p1125,p1124,p1123,p1122,p1121,p1120,p1119,p1118,p1117,p1116,p1115,p1114,p1113,p1112,
     p1111,p1110,p119,p118,p117,p116,p115,p114,p113,p112,p110,
     p110,p112,p113,p114,p115,p116,p117,p118,p119,p1110,p1111,p1112,p1113,p1114,p1115,p1116,p1117,p1118,p1119,p1120
     ,p1121,p1122,p1123,p1124,p1125,p1126,p1127,p1128,p1129,p1130,p1131,p1132,p1133,p1134,p1135,p1136,p1137,p1138,p1139,
     p1140,p1141,p1142,p1143,p1144,p1145,p1146,p1147,p1148,p1149,p111,



    p1201,p1249,p1248,p1247,p1246,p1245,p1244,p1243,p1242,p1241,p1240,p1239,p1238,p1237,p1236,p1235,p1234,p1233,p1232,p1231
     ,p1230,p1229,p1228,p1227,p1226,p1225,p1224,p1223,p1222,p1221,p1220,p1219,p1218,p1217,p1216,p1215,p1214,p1213,p1212,
     p1211,p1210,p1209,p1208,p1207,p1206,p1205,p1204,p1203,p1202,p1200,
     p1200,p1202,p1203,p1204,p1205,p1206,p1207,p1208,p1209,p1210,p1211,p1212,p1213,p1214,p1215,p1216,p1217,p1218,p1219,p1220
     ,p1221,p1222,p1223,p1224,p1225,p1226,p1227,p1228,p1229,p1230,p1231,p1232,p1233,p1234,p1235,p1236,p1237,p1238,p1239,
     p1240,p1241,p1242,p1243,p1244,p1245,p1246,p1247,p1248,p1249,p1201]

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
cisterna1=0
cisterna2=0
cisterna=0
xm=0
ym=0
#



ZASTAVKA.zastavka()
running = True      
if i == 1:
    running = False
while running:
    colorcolor1="blue"
    colorcolor2="blue"
    colorcolor3="blue"
    colorcolor4="blue"
    colorcolor5="blue"
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
    screen.blit(php[cisterna],[0,0])
    if cisterna1 ==2:
        cisterna2+=1
    if cisterna2 ==1:
        cisterna+=1
    if cisterna1 == 2:
        cisterna1=0
    if cisterna2 == 1:
        cisterna2=0
    if cisterna == 1200:
        cisterna=0
    cisterna1+=1
    for event in pygame.event.get():
        (xm,ym)= pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            xm=0
            ym=0
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xm,ym)= pygame.mouse.get_pos()
            time = 60
            if xm >=453 and xm<=618 and ym >= 406 and ym <= 524:
               down1=1
            if xm >=453 and xm<=618 and ym >= 60 and ym <= 165:
                down2=1
            if xm >=453 and xm<=618 and ym >= 165 and ym <= 286:
                down3=1
            if xm >=453 and xm<=618 and ym >= 286 and ym <= 404:
                down4=1
            if xm >=453 and xm<=618 and ym >= 524 and ym <= 648:
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
    if xm >=453 and xm<=618 and ym >= 406 and ym <= 524:
        colorcolor4="red"
    if xm >=453 and xm<=618 and ym >= 60 and ym <= 165:
        colorcolor1="red"
    if xm >=453 and xm<=618 and ym >= 165 and ym <= 286:
        colorcolor2="red"
    if xm >=453 and xm<=618 and ym >= 286 and ym <= 404:
        colorcolor3="red"
    if xm >=453 and xm<=618 and ym >= 524 and ym <= 648:
        colorcolor5="red"

    pygame.draw.lines(screen, colorcolor1,False,[[470,166],[600,166]],5)
    pygame.draw.lines(screen, colorcolor2,False,[[470,286],[600,286]],5)
    pygame.draw.lines(screen, colorcolor3,False,[[470,404],[600,404]],5)
    pygame.draw.lines(screen, colorcolor4,False,[[470,523],[600,523]],5)
    pygame.draw.lines(screen, colorcolor5,False,[[470,643],[600,643]],5)
    font1 = pygame.font.SysFont("Arial", 40,False,False)
    font = pygame.font.SysFont("Arial", 24,False,False)
    text665 = font1.render("МЕНЮ",1, THECOLORS['blue'])
    screen.blit(text665, [485,26] )
    text666 = font.render("один игрок",1, colorcolor1)
    screen.blit(text666, [487,126] )
    text667 = font.render("мультиплеер",1, colorcolor2)
    screen.blit(text667, [475,246] )
    text668 = font.render("выход",1, colorcolor3)
    screen.blit(text668, [510,364] )
    text669 = font.render("помощь",1, colorcolor4)
    screen.blit(text669, [500,483] )
    text670 = font.render("таблица рекордов",1, colorcolor5)
    screen.blit(text670, [450,603] )
    if i == 1:
        running = False
    pygame.time.delay(10)
    pygame.display.flip()
pygame.quit()
