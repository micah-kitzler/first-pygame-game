import pygame, sys
from pygame.locals import *
import random

pygame.init

windowSurface = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('game')

brown=(190,128,0)
black=(0,0,0)
green=(0,128,0)
blue=(0,0,255)
white=(255,255,255)
red=(255,0,0)

xtree1=[200,250,100,225,350]
ytree=[200,50,350]

x1=random.randint(0,3200)
x2=x1+50
x3=x1-100
x4=x1+25
x5=x1+150
xtree2=[x1,x2,x3,x4,x5]

x1=random.randint(0,3200)
x2=x1+50
x3=x1-100
x4=x1+25
x5=x1+150
xtree3=[x1,x2,x3,x4,x5]

x1=random.randint(0,3200)
x2=x1+50
x3=x1-100
x4=x1+25
x5=x1+150
xtree4=[x1,x2,x3,x4,x5]

x1=random.randint(0,3200)
x2=x1+50
x3=x1-100
x4=x1+25
x5=x1+150
xtree5=[x1,x2,x3,x4,x5]


orbx=400

pygame.draw.polygon(windowSurface, brown, ((xtree1[0],200), (xtree1[1],200), (xtree1[1],350), (xtree1[0],350)))
pygame.draw.polygon(windowSurface, green, ((xtree1[2],200), (xtree1[3],50), (xtree1[4],200)))

pygame.display.update()

motion=False
shooting=False

orbSize=0

def updateScreen(xtree1,ytree,orbSize,orbx,xtree2,xtree3,xtree4,xtree5,badGuyx,badGuyr):
    windowSurface.fill(black)
    pygame.draw.polygon(windowSurface, green, ((0,300),(0,600), (800,600), (800,300)))
    pygame.draw.polygon(windowSurface, brown, ((xtree1[0],ytree[0]), (xtree1[1],ytree[0]), (xtree1[1],ytree[2]), (xtree1[0],ytree[2])))
    pygame.draw.polygon(windowSurface, green, ((xtree1[2],ytree[0]), (xtree1[3],ytree[1]), (xtree1[4],ytree[0])))
    pygame.draw.polygon(windowSurface, brown, ((xtree2[0],ytree[0]), (xtree2[1],ytree[0]), (xtree2[1],ytree[2]), (xtree2[0],ytree[2])))
    pygame.draw.polygon(windowSurface, green, ((xtree2[2],ytree[0]), (xtree2[3],ytree[1]), (xtree2[4],ytree[0])))
    pygame.draw.polygon(windowSurface, brown, ((xtree3[0],ytree[0]), (xtree3[1],ytree[0]), (xtree3[1],ytree[2]), (xtree3[0],ytree[2])))
    pygame.draw.polygon(windowSurface, green, ((xtree3[2],ytree[0]), (xtree3[3],ytree[1]), (xtree3[4],ytree[0])))
    pygame.draw.polygon(windowSurface, brown, ((xtree4[0],ytree[0]), (xtree4[1],ytree[0]), (xtree4[1],ytree[2]), (xtree4[0],ytree[2])))
    pygame.draw.polygon(windowSurface, green, ((xtree4[2],ytree[0]), (xtree4[3],ytree[1]), (xtree4[4],ytree[0])))
    pygame.draw.polygon(windowSurface, brown, ((xtree5[0],ytree[0]), (xtree5[1],ytree[0]), (xtree5[1],ytree[2]), (xtree5[0],ytree[2])))
    pygame.draw.polygon(windowSurface, green, ((xtree5[2],ytree[0]), (xtree5[3],ytree[1]), (xtree5[4],ytree[0])))
    pygame.draw.circle(windowSurface, blue, (orbx,300), orbSize, 0)
    pygame.draw.circle(windowSurface, red, (badGuyx,300), badGuyr, 0)
    pygame.draw.circle(windowSurface, white, (400,300), 5, 0)
    pygame.display.update()

score=0
badShot=False
move=0
badGuyx=random.randint(0,3200)
badGuyr=1
badSpeed=1

while True:
    if badShot==True:
        badGuyx=random.randint(0,3200)
        badGuyr=0
        score+=1
    if score>15:
        badSpeed+=1
        score=0
    if orbSize==0:
        shooting=False
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key == K_RIGHT:
                motion=True
                while motion==True:
                    if orbSize==0:
                        shooting=False
                    badGuyx-=1
                    if badGuyx==0:
                        badGuyx+=3450
                    xtree1[0]-=1
                    xtree1[1]-=1
                    xtree1[2]-=1
                    xtree1[3]-=1
                    xtree1[4]-=1
                    if xtree1[4]==0:
                        xtree1[0]+=3450
                        xtree1[1]+=3450
                        xtree1[2]+=3450
                        xtree1[3]+=3450
                        xtree1[4]+=3450
                    xtree2[0]-=1
                    xtree2[1]-=1
                    xtree2[2]-=1
                    xtree2[3]-=1
                    xtree2[4]-=1
                    if xtree2[4]==0:
                        xtree2[0]+=3450
                        xtree2[1]+=3450
                        xtree2[2]+=3450
                        xtree2[3]+=3450
                        xtree2[4]+=3450
                    xtree3[0]-=1
                    xtree3[1]-=1
                    xtree3[2]-=1
                    xtree3[3]-=1
                    xtree3[4]-=1
                    if xtree3[4]==0:
                        xtree3[0]+=3450
                        xtree3[1]+=3450
                        xtree3[2]+=3450
                        xtree3[3]+=3450
                        xtree3[4]+=3450
                    xtree4[0]-=1
                    xtree4[1]-=1
                    xtree4[2]-=1
                    xtree4[3]-=1
                    xtree4[4]-=1
                    if xtree4[4]==0:
                        xtree4[0]+=3450
                        xtree4[1]+=3450
                        xtree4[2]+=3450
                        xtree4[3]+=3450
                        xtree4[4]+=3450
                    xtree5[0]-=1
                    xtree5[1]-=1
                    xtree5[2]-=1
                    xtree5[3]-=1
                    xtree5[4]-=1
                    if xtree5[4]==0:
                        xtree5[0]+=3450
                        xtree5[1]+=3450
                        xtree5[2]+=3450
                        xtree5[3]+=3450
                        xtree5[4]+=3450
                    if shooting == True:
                        orbSize-=1
                        orbx-=1
                    move+=1
                    if move==40:
                        badGuyr+=badSpeed
                        move=0
                    updateScreen(xtree1,ytree,orbSize,orbx,xtree2,xtree3,xtree4,xtree5,badGuyx,badGuyr)
                    for event in pygame.event.get():
                        if event.type==KEYUP:
                            if event.key==K_RIGHT:
                                motion=False
            if event.key == K_LEFT:
                motion=True
                while motion==True:
                    if orbSize==0:
                        shooting=False
                    badGuyx+=1
                    if badGuyx==3200:
                        badGuyx-=3450
                    xtree1[0]+=1
                    xtree1[1]+=1
                    xtree1[2]+=1
                    xtree1[3]+=1
                    xtree1[4]+=1
                    if xtree1[2]==3200:
                        xtree1[0]-=3450
                        xtree1[1]-=3450
                        xtree1[2]-=3450
                        xtree1[3]-=3450
                        xtree1[4]-=3450
                    xtree2[0]+=1
                    xtree2[1]+=1
                    xtree2[2]+=1
                    xtree2[3]+=1
                    xtree2[4]+=1
                    if xtree2[2]==3200:
                        xtree2[0]-=3450
                        xtree2[1]-=3450
                        xtree2[2]-=3450
                        xtree2[3]-=3450
                        xtree2[4]-=3450
                    xtree3[0]+=1
                    xtree3[1]+=1
                    xtree3[2]+=1
                    xtree3[3]+=1
                    xtree3[4]+=1
                    if xtree3[2]==3200:
                        xtree3[0]-=3450
                        xtree3[1]-=3450
                        xtree3[2]-=3450
                        xtree3[3]-=3450
                        xtree3[4]-=3450
                    xtree4[0]+=1
                    xtree4[1]+=1
                    xtree4[2]+=1
                    xtree4[3]+=1
                    xtree4[4]+=1
                    if xtree4[2]==3200:
                        xtree4[0]-=3450
                        xtree4[1]-=3450
                        xtree4[2]-=3450
                        xtree4[3]-=3450
                        xtree4[4]-=3450
                    xtree5[0]+=1
                    xtree5[1]+=1
                    xtree5[2]+=1
                    xtree5[3]+=1
                    xtree5[4]+=1
                    if xtree5[2]==3200:
                        xtree5[0]-=3450
                        xtree5[1]-=3450
                        xtree5[2]-=3450
                        xtree5[3]-=3450
                        xtree5[4]-=3450
                    if shooting == True:
                        orbSize-=1
                        orbx+=1
                    move+=1
                    if move==40:
                        badGuyr+=badSpeed
                        move=0
                    updateScreen(xtree1,ytree,orbSize,orbx,xtree2,xtree3,xtree4,xtree5,badGuyx,badGuyr)
                    for event in pygame.event.get():
                        if event.type==KEYUP:
                            if event.key==K_LEFT:
                                motion=False
            if event.key == K_SPACE:
                shooting=True
                orbSize=100
                orbx=400
    if shooting == True:
        orbSize-=1
    badShot=False
    move+=1
    if move==50:
        badGuyr+=badSpeed
        move=0
    if orbSize==badGuyr:
        if badGuyx>350 and badGuyx<450:
            badShot=True
    if move>100:
        move=0
    updateScreen(xtree1,ytree,orbSize,orbx,xtree2,xtree3,xtree4,xtree5,badGuyx,badGuyr)
    

