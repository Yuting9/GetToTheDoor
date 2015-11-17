#COLT AND YUTING MADE DIS |
#IT IS REALLY AWESOME GAME|
#MADE FOR ICS2O CLASS     |
#THE BEST GAME EVER       ValueError
#Further edited, should be better than before
import pygame
from pygame.color import THECOLORS
import time,os
import platform
import random
from pygame.locals import *
pygame.mixer.init()
pygame.init()
saveas="savefile"
keep=True
size=(600,500)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Get to The Door') 
screen = pygame.display.get_surface()
myfont = pygame.font.SysFont("Times New Roman", 30)
infont = pygame.font.SysFont("Times New Roman", 50)
clock=pygame.time.Clock()
fire=False
x=0
y=50
amx=0
amy=0
xMov=0
yMov=0
counter=1
i=0
test=pygame.display.get_driver()
sc1=pygame.image.load("sc1.gif").convert()
sc2=pygame.image.load("sc2.gif").convert()
sc3=pygame.image.load("sc3.gif").convert()
sc4=pygame.image.load("sc4.gif").convert()
bullet=pygame.image.load("Black_Dot.gif").convert()
nge=pygame.image.load("NewGameEmpty.png").convert()
ngn=pygame.image.load("NewGameNew.png").convert()
ngi=pygame.image.load("NewGameinstructions.png").convert()
ngl=pygame.image.load("NewGameleave.png").convert()
cge=pygame.image.load("continueGameEmpty.png").convert()
cgn=pygame.image.load("continueGameNew.png").convert()
cgi=pygame.image.load("continueGameinstructions.png").convert()
cgc=pygame.image.load("continueGameContinue.png").convert()
cgl=pygame.image.load("continueGameleave.png").convert()
pm=pygame.image.load("pausemenu.png").convert()
pe=pygame.image.load("pauseexit.png").convert()
pr=pygame.image.load("pauseresume.png").convert()
nl=pygame.image.load("nextlevel.png").convert()
ll=pygame.image.load("loselevel.png").convert()
tp1=pygame.image.load("tpmeter1.gif").convert()
tp2=pygame.image.load("tpmeter2.gif").convert()
tp3=pygame.image.load("tpmeter3.gif").convert()
tp4=pygame.image.load("tpmeter4.gif").convert()
tp5=pygame.image.load("tpmeter5.gif").convert()
tp6=pygame.image.load("tpmeter6.gif").convert()
inst1e=pygame.image.load("inst1e.png").convert()
inst1l=pygame.image.load("inst1l.png").convert()
inst1n=pygame.image.load("inst1n.png").convert()
inst2e=pygame.image.load("inst2e.png").convert()
inst2l=pygame.image.load("inst2l.png").convert()
inst2n=pygame.image.load("inst2n.png").convert()
background=pygame.image.load("bg.png").convert()
black=pygame.image.load("black.png").convert()
#to run in loop
waytofire=True
jumping=False
def shoot(true,bull,x,y,targets):
    if(x-50,y) in grounds and not true:
        return x,y
    bulletx=0
    if true:
        bulletx=1
        x+=20
    else:
        bulletx=-1
    while True:
        screen.blit(bull, (x,y+100))
        pygame.display.flip()
        x+=bulletx
        if ((x,y) in grounds and true) or((x-50,y) in grounds and not true):
            if not true:
                return x,y
            else:
                return x-50,y
        elif (x,y) in winway:
            return x,y
def pause():
    hem=True
    while hem==True:
        clock.tick(120)
        screen.fill((50,50,50))
        #txt file will have info, placed in a list to read
        screen.blit(pm,(0,0))
        if pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[1]>= 100 and  pygame.mouse.get_pos()[0]<= 450 and  pygame.mouse.get_pos()[1]<=200 :
            screen.blit(pr,(0,0))
        elif pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[1]>= 300 and  pygame.mouse.get_pos()[0]<= 450 and  pygame.mouse.get_pos()[1]<=400 :
            screen.blit(pe,(0,0))
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                keepgoing = False
            elif ev.type == MOUSEBUTTONDOWN:
               if pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[1]>= 100 and  pygame.mouse.get_pos()[0]<= 450 and  pygame.mouse.get_pos()[1]<=200 :
                    return True
               elif pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[1]>= 300 and  pygame.mouse.get_pos()[0]<= 450 and  pygame.mouse.get_pos()[1]<=400 :
                    return False
        pygame.display.flip()
def end():
    print("END")
    keepgoing=False
    keep=False
def zombie():
    pass
def climb(y):
    y+=1
laser=pygame.mixer.Sound("LASER.ogg")
def normshoot(true,bull,x,y,targets,boss):
    pygame.mixer.Sound.play(laser)
    bulletx=0
    if(x-50,y) in grounds and not true:
        return 0
    if true:
        bulletx=1
        x+=20
    else:
        bulletx=-1
    if not boss:
        while True:
            screen.blit(bull, (x,y+10))
            pygame.display.flip()
            x+=bulletx
            if (x,y) in targets:
                place=targets.index((x,y))
                enemies.remove(enemies[place])
                whererthey.remove((x,y))
                return True
                break
            elif ((x,y) in grounds and true) or (x,y) in winway or ((x-50,y) in grounds and not true):
                break
    else:
        while True:
            screen.blit(bull, (x,y+10))
            pygame.display.flip()
            x+=bulletx
            ad,bd=targets[0]
            if x >= ad and x <= ad+100 and y <= bd+100 and y >= bd:
                return True
            elif ((x,y) in grounds and true) or (x,y) in winway or ((x-50,y) in grounds and not true):
                break
hitwall=False
grounds=[]
ladders=[]
winway=[]
def mapsetup(grounds,txt,back):
    tat=""
    with open(txt) as text:
        for word in text:
            tat+=word
    tat=tat.replace("\n",",")
    tat=tat.split(",")
    screen = pygame.display.set_mode((600,500))
    screen.blit(back, (0,0))
    ladder=pygame.image.load("ladder.gif").convert()
    ground=pygame.image.load("ground.png").convert()
    door1=pygame.image.load("door1.png").convert()
    door2=pygame.image.load("door2.png").convert()
    door1_O=pygame.image.load("door1_O.png").convert()
    door2_O=pygame.image.load("door2_O.png").convert()
    x=0 
    y=0
    for item in tat:
        if item=="H":
            screen.blit(ladder,(x,y))
            if (x,y) not in ladders:
                ladders.append((x,y))
        elif item=="_":
            screen.blit(ground,(x,y))
            grounds.append((x,y))
        elif item=="n":
            screen.blit(door1,(x,y))
            if (x,y) not in winway:
                winway.append((x,y))
        elif item=="U":
            screen.blit(door2,(x,y))
        elif item=="O":
            screen.blit(door1_O,(x,y))
            x1=x
            y2=y
        elif item=="<":
            screen.blit(door2_O,(x,y))
        if y!=450:
            y+=50
        elif y==450:
            y=0
            x=x+50
    return x1,y2
ch1="char1.gif"
ch2="char2.gif"
live=True
scene="start"
lista=""
with open ("savefile.txt") as ready:
    for qqqqq in ready:
        print(qqqqq)
        lista+=(qqqqq)
lista=lista.split()
keepgoing=True
win=False
right=False
left=False
up=False
down=False
try:
    shootable=True
    pygame.mixer.music.load("MUSIC.ogg")
    pygame.mixer.music.play()
    while keepgoing:
        lista=""
        with open ("savefile.txt") as ready:
            for qqqqq in ready:
                lista+=(qqqqq)
        lista=lista.split()
        yes=True
        background=pygame.image.load("bg.png").convert()
        keep=True
        win=False
        live=True
        if scene=="NewGame":
            open("savefile.txt" , "w").write("map1"+" cont")
        if scene=="start":
            if "new" in lista:
                screen.blit(ngn,(0,0))
                if pygame.mouse.get_pos()[0]>=50 and pygame.mouse.get_pos()[1]>= 350 and  pygame.mouse.get_pos()[0]<= 150 and  pygame.mouse.get_pos()[1]<=400 :
                    screen.blit(nge,(0,0))
                elif pygame.mouse.get_pos()[0]>=50 and pygame.mouse.get_pos()[1]>= 420 and  pygame.mouse.get_pos()[0]<= 150 and  pygame.mouse.get_pos()[1]<=470 :
                    screen.blit(ngi,(0,0))
                elif pygame.mouse.get_pos()[0]>=450 and pygame.mouse.get_pos()[1]>= 420 and  pygame.mouse.get_pos()[0]<= 550 and  pygame.mouse.get_pos()[1]<=470 :
                    screen.blit(ngl,(0,0))
            elif "cont" in lista:
                screen.blit(cge,(0,0))
                if pygame.mouse.get_pos()[0]>=50 and pygame.mouse.get_pos()[1]>= 350 and  pygame.mouse.get_pos()[0]<= 150 and  pygame.mouse.get_pos()[1]<=400 :
                    screen.blit(cgn,(0,0))
                elif pygame.mouse.get_pos()[0]>=450 and pygame.mouse.get_pos()[1]>= 350 and  pygame.mouse.get_pos()[0]<= 550 and  pygame.mouse.get_pos()[1]<=400 :
                    screen.blit(cgc,(0,0))
                elif pygame.mouse.get_pos()[0]>=50 and pygame.mouse.get_pos()[1]>= 420 and  pygame.mouse.get_pos()[0]<= 150 and  pygame.mouse.get_pos()[1]<=470 :
                    screen.blit(cgi,(0,0))
                elif pygame.mouse.get_pos()[0]>=450 and pygame.mouse.get_pos()[1]>= 420 and  pygame.mouse.get_pos()[0]<= 550 and  pygame.mouse.get_pos()[1]<=470 :
                    screen.blit(cgl,(0,0))
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    keepgoing=False
                elif ev.type == MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0]>=50 and pygame.mouse.get_pos()[1]>= 350 and  pygame.mouse.get_pos()[0]<= 150 and  pygame.mouse.get_pos()[1]<=400 :
                        scene="NewGame"
                        numsup=0
                    elif  pygame.mouse.get_pos()[0]>=450 and pygame.mouse.get_pos()[1]>= 350 and  pygame.mouse.get_pos()[0]<= 550 and  pygame.mouse.get_pos()[1]<=400  and "cont" in lista:
                        scene="Continue"
                        numsup=0
                    elif pygame.mouse.get_pos()[0]>=50 and pygame.mouse.get_pos()[1]>= 420 and  pygame.mouse.get_pos()[0]<= 150 and  pygame.mouse.get_pos()[1]<=470 :
                        scene="Instructions"
                    elif pygame.mouse.get_pos()[0]>=450 and pygame.mouse.get_pos()[1]>= 420 and  pygame.mouse.get_pos()[0]<= 550 and  pygame.mouse.get_pos()[1]<=470:
                        keepgoing=False
            pygame.display.flip()
        elif scene=="Instructions":
            while keep:
                screen.blit(inst1e,(0,0))
                if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[1]>= 450 and  pygame.mouse.get_pos()[0]<= 100 and  pygame.mouse.get_pos()[1]<=500 :
                    screen.blit(inst1l,(0,0))
                elif pygame.mouse.get_pos()[0]>=500 and pygame.mouse.get_pos()[1]>= 450 and  pygame.mouse.get_pos()[0]<= 600 and  pygame.mouse.get_pos()[1]<=500 :
                    screen.blit(inst1n,(0,0))
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT:
                        keep=False
                        keepgoing=False
                    elif ev.type==pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[1]>= 450 and  pygame.mouse.get_pos()[0]<= 100 and  pygame.mouse.get_pos()[1]<=500 :
                            scene="start"
                            keep=False
                        elif pygame.mouse.get_pos()[0]>=500 and pygame.mouse.get_pos()[1]>= 450 and  pygame.mouse.get_pos()[0]<= 600 and  pygame.mouse.get_pos()[1]<=500 :
                            scene="Instructions2"
                            keep=False
                pygame.display.flip()                    
        elif scene=="Instructions2":
            while keep:
                screen.blit(inst2e,(0,0))
                if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[1]>= 450 and  pygame.mouse.get_pos()[0]<= 100 and  pygame.mouse.get_pos()[1]<=500 :
                    screen.blit(inst2l,(0,0))
                elif pygame.mouse.get_pos()[0]>=500 and pygame.mouse.get_pos()[1]>= 450 and  pygame.mouse.get_pos()[0]<= 600 and  pygame.mouse.get_pos()[1]<=500 :
                    screen.blit(inst2n,(0,0))
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT:
                        keep=False
                        keepgoing=False
                    elif ev.type==pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[1]>= 450 and  pygame.mouse.get_pos()[0]<= 100 and  pygame.mouse.get_pos()[1]<=500 :
                            scene="start"
                            keep=False
                        elif pygame.mouse.get_pos()[0]>=500 and pygame.mouse.get_pos()[1]>= 450 and  pygame.mouse.get_pos()[0]<= 600 and  pygame.mouse.get_pos()[1]<=500 :
                            scene="Instructions"
                            keep=False
                pygame.display.flip()
        elif scene=="Exit":
            keepgoing=False
        elif scene=="DED":
            screen.blit(ll,(0,0))
            while keep:
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT:
                        keep=False
                        keepgoing=False
                    elif ev.type==pygame.MOUSEBUTTONDOWN or ev.type==pygame.KEYDOWN:
                        scene= "start"
                        keep=False
                pygame.display.flip()
        elif scene=="WIN":
            levnum=""
            with open('savefile.txt') as omgomg:
                for stooped in omgomg:
                    levnum=stooped
            levnum=levnum.split()
            levnum=levnum[0]
            levnum=int(levnum[3:])
            screen.blit(nl,(0,0)) 
            while keep:
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT:
                        keep=False
                        keepgoing=False
                    if ev.type==pygame.KEYDOWN:
                            if ev.key==K_SPACE:
                                levnum+=1
                                scene=str("map"+str(levnum))
                                print(scene)
                                if scene == "map21":
                                    scene = "END"
                                open("savefile.txt" , "w").write(scene+" cont")
                                keep=False
                pygame.display.flip()
            continue
        elif scene == "END":
            open("savefile.txt" , "w").write("map1"+" new")
            scene="Fin"
        elif scene == "Fin":
            end=pygame.image.load("end.png")
            screen.blit(end,(0,0))
            keep=True
            while keep:
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT:
                        keep=False
                        keepgoing=False
                    if ev.type==pygame.KEYDOWN:
                        scene="start"
                        keep=False
                pygame.display.flip()
        else:
            fire=False
            shootable=True
            with open("savefile.txt") as textfileomg:
                for word in textfileomg:
                    scene=word
            scene=scene.split()
            scene=scene[0]
            asdfs=""
            enemies=[]
            with open(scene+"enemies.txt") as ens:
                for word in ens:
                    asdfs+=word
            asdfs=asdfs.split()
            for tuu in asdfs:
                enemies.append(tuu.split(","))
            whererthey=[]
            for x in range(len(enemies)):
                whererthey.append([])
            x2,y2=mapsetup(grounds,scene+".txt",background)
            x3=x2
            y3=y2+50
            shotcont=0
            if scene == "map20":
                numsup=0
            elif numsup == 0:
                numsup=2
            while keep:
                boss=False
                grounds=[]
                ladders=[]
                winway=[]
                mapsetup(grounds,scene+".txt",background)
                hitwall=False
                clock.tick(60)
                char1=pygame.image.load(ch1).convert()
                char2=pygame.image.load(ch2).convert()
                screen.blit(char1, (x2,y2))
                screen.blit(char2, (x3,y3))
                z1=pygame.image.load("zomb1.gif").convert()
                z2=pygame.image.load("zomb2.gif").convert()
                wheretofind=0
                for an in enemies:
                    if scene != "map20":
                        z=int(an[0])
                        o=int(an[1])
                        turned=bool(an[2])
                        cunoma=bool(an[5])
                        if not cunoma:
                            z1=pygame.image.load("zomb1.gif").convert()
                            z2=pygame.image.load("zomb2.gif").convert()
                        else:
                            z1=pygame.image.load("zomb1_L.gif").convert()
                            z2=pygame.image.load("zomb2_L.gif").convert()
                        counterized=int(an[3])
                        alive=bool(an[4])
                        if not alive:
                            continue
                        screen.blit(z1, (z,o))
                        screen.blit(z2, (z,o+50))
                        if (z+50,o) in grounds or (z-50,o) in grounds or (((z-50,o+100) not in grounds and turned) and ((z-40,o+100) not in grounds and turned)and((z-30,o+100) not in grounds and turned)and((z-20,o+100) not in grounds and turned)and((z-10,o+100) not in grounds and turned))or (((z+50,o+100) not in grounds and not turned) and ((z+40,o+100) not in grounds and not turned) and ((z+30,o+100) not in grounds and not turned) and ((z+20,o+100) not in grounds and not turned) and ((z+10,o+100) not in grounds and not turned)):
                            turned=not(turned)
                        if counterized==3:
                            if turned:
                                z+=-10
                                cunoma=False
                            else:
                                z+=10
                                cunoma=True
                            counterized=0
                        counterized+=1
                        where=enemies.index(an)
                        enemies[where]=[z,o,turned,counterized,alive,cunoma]
                        whererthey[where]=(z,o)
                    else:
                        boss=True
                        damage=int(an[0])
                        qq=int(an[1])
                        qw=int(an[2])
                        if damage == 4:
                            numsup=6
                            break
                        else:
                            bossy=pygame.image.load("boss"+str(damage)+".gif").convert()
                            willitfire=random.randint(1,500)
                            screen.blit(bossy, (qq,qw))
                            if y2+10 > qw:
                                qw+=2
                            if y2+10 < qw:
                                qw-=2
                            where=enemies.index(an)
                            enemies[where]=[damage,qq,qw]
                            whererthey[where]=(qq,qw)
                            if willitfire > 450 and not fire:
                                amx=0
                                amy=0
                                fire=True
                                amx=qq
                                amy=qw+10
                            if fire:
                                screen.blit(bullet, (amx,amy+50))
                                screen.blit(bossy, (qq,qw))
                                pygame.display.flip()
                                amx+=3
                                if amx >= x2 and amx <= x2+50 and amy >= y2-50 and amy <= y2+50:
                                    screen.blit(ll,(0,0))
                                    while keep:
                                        for ev in pygame.event.get():
                                            if ev.type==pygame.QUIT:
                                                keep=False
                                                keepgoing=False
                                            elif ev.type==pygame.MOUSEBUTTONDOWN or ev.type==pygame.KEYDOWN:
                                                scene= "start"
                                                keep=False
                                        pygame.display.flip()
                                elif amx+50 == 600:
                                    print("nope")
                                    fire=False
                if (x2,y2) in whererthey or (x2+10,y2+10) in whererthey or (x2+20,y2+20) in whererthey or (x2+30,y2+30) in whererthey or (x2+40,y2+40) in whererthey or (x2-10,y2-10) in whererthey or (x2-20,y2-20) in whererthey or (x2-30,y2-30) in whererthey or (x2-40,y2-40) in whererthey:
                    live=False
                if not(live):
                    keep=False
                    scene="DED"
                if (x2,y2) in winway:
                    win=True
                if win:
                    keep=False
                    scene="WIN"
                y2+=50
                y3+=50
                if (x3,y3) in grounds or (x3,y3) in ladders:
                    y2-=50
                    y3-=50
                if not shootable:
                    shotcont+=1
                    if shotcont >= 100:
                        shootable=True
                        shotcont=0
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT:
                        keep=False
                        keepgoing=False
                    elif ev.type==pygame.KEYDOWN:
                        if ev.key==pygame.K_p:
                            if not (pause()):
                                keep=False
                                scene="start"
                        elif ev.key==pygame.K_RSHIFT or ev.key==pygame.K_LSHIFT:
                             if numsup > 0:
                                mapsetup(grounds,scene+".txt",background)
                                for an in enemies:
                                    if numsup==1:
                                        screen.blit(tp1,(0,0))
                                    if numsup==2:
                                        screen.blit(tp2,(0,0))
                                    if numsup==3:
                                        screen.blit(tp3,(0,0))
                                    if numsup==4:
                                        screen.blit(tp4,(0,0))
                                    if numsup==5:
                                        screen.blit(tp5,(0,0))
                                    if numsup==6:
                                        screen.blit(tp6,(0,0))
                                    pygame.display.flip()
                                    if not boss:
                                        z=int(an[0])
                                        o=int(an[1])
                                        turned=bool(an[2])
                                        counterized=int(an[3])
                                        alive=bool(an[4])
                                        if turned:
                                            z1=pygame.image.load("zomb1.gif").convert()
                                            z2=pygame.image.load("zomb2.gif").convert()
                                        else:
                                            z1=pygame.image.load("zomb1_L.gif").convert()
                                            z2=pygame.image.load("zomb2_L.gif").convert()
                                        if not alive:
                                            continue
                                        screen.blit(z1, (z,o))
                                        screen.blit(z2, (z,o+50))
                                        if (z+50,o) in grounds or (z-50,o) in grounds or (((z-50,o+100) not in grounds and turned) and ((z-40,o+100) not in grounds and turned)and((z-30,o+100) not in grounds and turned)and((z-20,o+100) not in grounds and turned)and((z-10,o+100) not in grounds and turned))or (((z+50,o+100) not in grounds and not turned) and ((z+40,o+100) not in grounds and not turned) and ((z+30,o+100) not in grounds and not turned) and ((z+20,o+100) not in grounds and not turned) and ((z+10,o+100) not in grounds and not turned)):
                                            turned=not(turned)
                                        if counterized>=33:
                                            if turned:
                                                z+=-10
                                            else:
                                                z+=10
                                            counterized=0
                                        counterized+=1
                                x2,y2=shoot(waytofire,black,x2,y2,whererthey)
                                x3=x2
                                y3=y2+50
                                numsup-=1
                        elif ev.key==pygame.K_SPACE:
                            if numsup==1:
                                screen.blit(tp1,(0,0))
                            if numsup==2:
                                screen.blit(tp2,(0,0))
                            if numsup==3:
                                screen.blit(tp3,(0,0))
                            if numsup==4:
                                screen.blit(tp4,(0,0))
                            if numsup==5:
                                screen.blit(tp5,(0,0))
                            if numsup==6:
                                screen.blit(tp6,(0,0))
                            pygame.display.flip()
                            if shootable:
                                if normshoot(waytofire,bullet,x2,y2,whererthey,boss) and not boss:
                                    numsup+=1
                                elif normshoot(waytofire,bullet,x2,y2,whererthey,boss) and boss:
                                    enemies[0]=[damage+1,qq,qw]
                                    print(enemies[0])
                                print("BLAM")
                                shootable=False
                        elif ev.key==K_RIGHT:#HERE
                            right=True
                        elif ev.key==K_LEFT:
                            left=True
                        elif ev.key==pygame.K_DOWN:
                            if (x2,y2) not in grounds or (x3,y3) not in grounds:
                                y2+=50
                                y3+=50
                            if (x2,y2) in grounds or (x3,y3) in grounds:
                                y2-=50
                                y3-=50
                        elif ev.key==pygame.K_UP:
                            if (x2,y2) in ladders or (x3,y3) in ladders:
                                y2-=50
                                y3-=50
                            if (x2,y2) in grounds or (x3,y3) in grounds:
                                y2+=50
                                y3+=50
                            else:
                                pass
                    elif ev.type==pygame.KEYUP:
                        if ev.key==K_RIGHT:
                            right=False 
                        if ev.key==K_LEFT:
                            left=False
                if left:
                    waytofire=False
                    x2-=50
                    x3-=50
                    if (x2,y2) in grounds or (x3,y3) in grounds or ((x3,y3+50) not in grounds and (x3,y3+50) not in ladders):
                        x2+=50
                        x3+=50
                    ch1="char1_L.gif"
                    ch2="char2_L.gif"
                if right:
                    x2+=50
                    x3+=50
                    if (x2,y2) in grounds or (x3,y3) in grounds or ((x3,y3+50) not in grounds and (x3,y3+50) not in ladders):
                        x2-=50
                        x3-=50
                    waytofire=True
                    ch1="char1.gif"
                    ch2="char2.gif"
                if numsup==1:
                    screen.blit(tp1,(0,0))
                elif numsup==2:
                    screen.blit(tp2,(0,0))
                elif numsup==3:
                    screen.blit(tp3,(0,0))
                elif numsup==4:
                    screen.blit(tp4,(0,0))
                elif numsup==5:
                    screen.blit(tp5,(0,0))
                elif numsup==6:
                    screen.blit(tp6,(0,0))
                elif numsup>=6:
                    numsup=6
                if shootable:
                    screen.blit(sc4,(550,0))
                elif shotcont >=75:
                    screen.blit(sc3,(550,0))
                elif shotcont >=50:
                    screen.blit(sc2,(550,0))
                elif shotcont >=25:
                    screen.blit(sc1,(550,0))
                else: pass
                pygame.display.flip()
            
finally:
    pygame.quit()
