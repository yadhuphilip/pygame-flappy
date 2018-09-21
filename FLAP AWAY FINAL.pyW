import pygame
import time


import random


pygame.init()


black=(0,0,0)
white=(255,255,255)
red=(55,0,0)
bred=(255,0,0)
green=(0,55,0)
bgreen=(0,255,0)
blue=(0,0,255)
bblue=(0,162,232)
grey=(192,192,192)

dpw=800
dph=600
clock=pygame.time.Clock()
gd=pygame.display.set_mode((dpw,dph),pygame.FULLSCREEN)
bimg=pygame.image.load("bkj.png")
ico=pygame.image.load("ico.png")
pygame.display.set_icon(ico)
pygame.display.set_caption("FLAP AWAY")

gimg=pygame.image.load("char.png")
gw=48
gh=54
ox=690
oy=0
ow=100
oh=250
pause=False
gd.blit(gimg,(30,200))
pygame.mixer.music.load("bassb.mp3")
##def text_objects(text,font,color):
##     textSurface=font.render(text,True,color)
##     return textSurface,textSurface.get_rect()

def qtg():
    pygame.quit()
    quit()


def mark(cnt):
    txt=pygame.font.SysFont("arial",20)
    txte=txt.render("score: "+str(cnt),True,black)
    gd.blit(txte,(0,0))
    f=open("his.txt","r")
    q=f.read()
    f.close()
    txt=pygame.font.SysFont("arial",20)
    txte=txt.render("HI_SCORE: "+str(q),True,black)
    gd.blit(txte,(0,21))
    if int(cnt)>int(q):
        f=open("his.txt","w")
        f.write(str(cnt))
        f.close
        txt=pygame.font.SysFont("arial",20)
        txte=txt.render("HI_SCORE: "+str(q),True,black)
        gd.blit(txte,(0,21))    
    
def crash():
     pygame.mixer.music.stop()
     cra =0
     while cra==0:
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.quit()
                 quit()
         Text=pygame.font.SysFont('arial',120)

         txtsurf=Text.render("DEAD",True,bgreen)
         txtrect=txtsurf.get_rect()

         
         txtrect.center=((dpw/2),(dph/2))
         gd.blit(txtsurf,txtrect)

         btn(150,450,80,40,"PLAY",black,blue,bgreen,gm)
         btn(550,450,80,40,"QUIT",black,blue,bred,qtg)
         pygame.display.update()
         clock.tick(100)
             
    
     
   
    
    
def btn(bx,by,bw,bh,txt,txcl,ic,ac,act):
   
        mus=pygame.mouse.get_pos()
        clk=pygame.mouse.get_pressed()
        if bx<mus[0]<bx+bw and by<mus[1]<by+bh:
            pygame.draw.rect(gd,ac,[bx,by,bw,bh])
            if clk[0]==1:
                act()
                
        else:
            pygame.draw.rect(gd,ic,[bx,by,bw,bh])
        t=pygame.font.SysFont("arial",20)
        txtsurf=t.render(txt,True,txcl)
        txtrect=txtsurf.get_rect()
        txtrect.center=(bx+(bw/2),by+(bh/2 ))
        gd.blit(txtsurf,txtrect)
       
def cntin():
    global pause
    pause= False
def intro():
    g=0
    gd.fill(black)
    txt=pygame.font.SysFont("chiller",95)
    txtsurf=txt.render("FLAP AWAY",True,bblue)
    txtrect=txtsurf.get_rect()
    txtrect.center=(400,300)
    gd.blit(txtsurf,txtrect)
    while g==0:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


        btn(150,450,70,40,"PLAY",black,green,bgreen,gm)
        btn(550,450,70,40,"QUIT",black,red,bred,qtg)
        pygame.display.flip()
        clock.tick(65)
 




    
def paus():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    cntin()
        txt=pygame.font.SysFont("broadway",85)
        txte=txt.render("PAUSED",True,blue)
        txtre=txte.get_rect()
        txtre.center=(dpw/2,dph/2)
        gd.blit(txte,txtre)
        btn(150,450,90,40,"CONTINUE",black,white,bgreen,cntin)
        btn(550,450,70,40,"QUIT",black,white,bred,qtg)
        
        pygame.display.flip()
        clock.tick(65)

def obstecles(ox,oy,ow,oh):
   
    pygame.draw.rect(gd,black,(ox,oy,ow,oh))
def gm():
    global pause
    pygame.mixer.music.play(-1)
    ox=890
    oy=0
    ow=110
    oh=250
    oy1=oh+135
    oh1=dph-oy1 
    x=30
    y=200
    ych=0
    gw=48
    ch=2
    gh=54
    gd.blit(bimg,(0,0))
    cmr=0
    while True:
        for event in pygame.event.get():
            mus=pygame.mouse.get_pressed()
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
               
                if event.key==pygame.K_UP :
                    ych=-4
                if event.key==pygame.K_DOWN:
                    ych=6
                if event.key==pygame.K_SPACE:
                    pause=True
                    paus()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    ych=4
        if y<0:
            ych=2
        y=y+ych
        
        
        gd.blit(bimg,(0,0))
        btn(730,0,70,35,"QUIT",bred,bblue,black,qtg)
        gd.blit(gimg,(x,y))
        
        mark(cmr)
        obstecles(ox,oy,ow,oh)
        obstecles(ox,oy1,ow,oh1)
        ox=ox-ch
        if ox+ow<0:
            ox=801
            oh=random.randrange(100,450)
            oy1=oh+135
            oh1=dph-oy1
            cmr=cmr+1
            if cmr>1:
                if cmr%2==0:
                    ch=ch+1
        if y>dph-54:
            #while True:
          
            print("wall crash")
            crash()
        if x+gw>ox and x<ox+ow or x+gw>ox+ow and x<ox+ow:
            if y<oh or y+gw>oy1:
                print("data  ","oy  ",oy,"  oh",oh,"  oy1",oy1,"  oh1",oh1)
                print("\n ","gx",x,"gy",y,"gw+x",x+gw,"  gy+gh",y+gh)
                print("obj crash")
    
                crash()
        
                
            

        pygame.display.update()
        clock.tick(65)
        
                







intro()
gm()
pygame.quit()
quit()
