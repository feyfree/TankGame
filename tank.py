from Tkinter import *
from time import *
from function import *
from random import *


class MyTank:
    def __init__(self,c,x,y,tu,td,tl,tr,life,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8):
        c.create_image(x,y,image=td,state='hidden',anchor='nw',tags=tag1)
        c.create_image(x,y,image=tu,state='normal',anchor='nw',tags=tag2)
        c.create_image(x,y,image=tl,state='hidden',anchor='nw',tags=tag3)
        c.create_image(x,y,image=tr,state='hidden',anchor='nw',tags=tag4)
        self.tankd=tag1
        self.tanku=tag2
        self.tankl=tag3
        self.tankr=tag4
        self.bulletd=tag5
        self.bulletu=tag6
        self.bulletl=tag7
        self.bulletr=tag8
        self.life=life
    def Move(self,c,ukey,dkey,lkey,rkey,gm):
        def MoveUp(event):
            c.itemconfig(self.tankd,state='hidden')
            c.itemconfig(self.tanku,state='normal')
            c.itemconfig(self.tankl,state='hidden')
            c.itemconfig(self.tankr,state='hidden')
            if c.itemcget(self.tankd,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankd)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0-40
            if c.itemcget(self.tanku,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tanku)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0-40
            if c.itemcget(self.tankl,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankl)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0-40
            if c.itemcget(self.tankr,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankr)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0-40
            gp=getposition(c,gm)
            if (b1>=39 and gp.count((a0,b0))==0):
                c.move(self.tankd,0,-40)
                c.move(self.tanku,0,-40)
                c.move(self.tankl,0,-40)
                c.move(self.tankr,0,-40)
        def MoveDown(event):
            c.itemconfig(self.tankd,state='normal')
            c.itemconfig(self.tanku,state='hidden')
            c.itemconfig(self.tankl,state='hidden')
            c.itemconfig(self.tankr,state='hidden')
            if c.itemcget(self.tankd,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankd)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0+40
            if c.itemcget(self.tanku,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tanku)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0+40
            if c.itemcget(self.tankl,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankl)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0+40
            if c.itemcget(self.tankr,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankr)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0+40
            gp=getposition(c,gm)
            if (b2<=481 and gp.count((a0,b0))==0):
                c.move(self.tankd,0,40)
                c.move(self.tanku,0,40)
                c.move(self.tankl,0,40)
                c.move(self.tankr,0,40)
        def MoveLeft(event):
            c.itemconfig(self.tankd,state='hidden')
            c.itemconfig(self.tanku,state='hidden')
            c.itemconfig(self.tankl,state='normal')
            c.itemconfig(self.tankr,state='hidden')
            if c.itemcget(self.tankd,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankd)
                a0=(a1+a2)/2.0-40
                b0=(b1+b2)/2.0
            if c.itemcget(self.tanku,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tanku)
                a0=(a1+a2)/2.0-40
                b0=(b1+b2)/2.0
            if c.itemcget(self.tankl,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankl)
                a0=(a1+a2)/2.0-40
                b0=(b1+b2)/2.0
            if c.itemcget(self.tankr,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankr)
                a0=(a1+a2)/2.0-40
                b0=(b1+b2)/2.0
            gp=getposition(c,gm)
            if (a1>=39 and gp.count((a0,b0))==0):
                c.move(self.tankd,-40,0)
                c.move(self.tanku,-40,0)
                c.move(self.tankl,-40,0)
                c.move(self.tankr,-40,0)
        def MoveRight(event):
            c.itemconfig(self.tankd,state='hidden')
            c.itemconfig(self.tanku,state='hidden')
            c.itemconfig(self.tankl,state='hidden')
            c.itemconfig(self.tankr,state='normal')
            if c.itemcget(self.tankd,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankd)
                a0=(a1+a2)/2.0+40
                b0=(b1+b2)/2.0
            if c.itemcget(self.tanku,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tanku)
                a0=(a1+a2)/2.0+40
                b0=(b1+b2)/2.0
            if c.itemcget(self.tankl,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankl)
                a0=(a1+a2)/2.0+40
                b0=(b1+b2)/2.0
            if c.itemcget(self.tankr,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.tankr)
                a0=(a1+a2)/2.0+40
                b0=(b1+b2)/2.0
            gp=getposition(c,gm)
            if (a2<=481 and gp.count((a0,b0))==0):
                c.move(self.tankd,40,0)
                c.move(self.tanku,40,0)
                c.move(self.tankl,40,0)
                c.move(self.tankr,40,0)
        c.bind(ukey,MoveUp)
        c.bind(dkey,MoveDown)
        c.bind(lkey,MoveLeft)
        c.bind(rkey,MoveRight)

    def Shoot(self,c,Key,b):
        def CreateBullet(event):
            if (c.itemcget(self.tankd,'state')=='normal' and exist(c,self.bulletd)==False and exist(c,self.bulletu)==False and exist(c,self.bulletl)==False and exist(c,self.bulletr)==False):
                (x1,y1,x2,y2)=c.bbox(self.tankd)
                x0=(x1+x2)/2.0
                y0=y2
                c.create_image(x0,y0,image=b,tags=self.bulletd)
            if (c.itemcget(self.tanku,'state')=='normal' and exist(c,self.bulletd)==False and exist(c,self.bulletu)==False and exist(c,self.bulletl)==False and exist(c,self.bulletr)==False):
                (x1,y1,x2,y2)=c.bbox(self.tanku)
                x0=(x1+x2)/2.0
                y0=y1
                c.create_image(x0,y0,image=b,tags=self.bulletu)
            if (c.itemcget(self.tankr,'state')=='normal' and exist(c,self.bulletd)==False and exist(c,self.bulletu)==False and exist(c,self.bulletl)==False and exist(c,self.bulletr)==False):
                (x1,y1,x2,y2)=c.bbox(self.tankr)
                x0=x2
                y0=(y1+y2)/2.0
                c.create_image(x0,y0,image=b,tags=self.bulletr)
            if (c.itemcget(self.tankl,'state')=='normal' and exist(c,self.bulletd)==False and exist(c,self.bulletu)==False and exist(c,self.bulletl)==False and exist(c,self.bulletr)==False):
                (x1,y1,x2,y2)=c.bbox(self.tankl)
                x0=x1
                y0=(y1+y2)/2.0
                c.create_image(x0,y0,image=b,tags=self.bulletl)
        c.bind(Key,CreateBullet)
            
    def BulletFly(self,c,g):
        if exist(c,self.bulletd)==True:
            if (c.bbox(self.bulletd)[3]<520):
                c.move(self.bulletd,0,20)
            else:
                c.delete(self.bulletd)
            for i in g:
                if c.bbox(self.bulletd)==None:
                    break
                else:
                    (x1,y1,x2,y2)=c.bbox(self.bulletd)
                    if (c.bbox(i)==None):
                        continue
                    else:
                        (u1,v1,u2,v2)=c.bbox(i)
                        if (x1>u1 and y1>v1 and x2<u2 and y2<v2):
                            c.delete(i)
                            c.delete(self.bulletd)
                                    
        if exist(c,self.bulletu)==True:
            if (c.bbox(self.bulletu)[1]>0):
                c.move(self.bulletu,0,-20)
            else:
                c.delete(self.bulletu)
            for i in g:
                if c.bbox(self.bulletu)==None:
                    break
                else:
                    (x1,y1,x2,y2)=c.bbox(self.bulletu)
                    if (c.bbox(i)==None):
                        continue
                    else:
                        (u1,v1,u2,v2)=c.bbox(i)
                        if (x1>u1 and y1>v1 and x2<u2 and y2<v2):
                            c.delete(i)
                            c.delete(self.bulletu)
                                                
        if exist(c,self.bulletl)==True:
            if (c.bbox(self.bulletl)[0]>0):
                c.move(self.bulletl,-20,0)
            else:
                c.delete(self.bulletl)
            for i in g:
                if c.bbox(self.bulletl)==None:
                    break
                else:
                    (x1,y1,x2,y2)=c.bbox(self.bulletl)
                    if (c.bbox(i)==None):
                        continue
                    else:
                        (u1,v1,u2,v2)=c.bbox(i)
                        if (x1>u1 and y1>v1 and x2<u2 and y2<v2):
                            c.delete(i)
                            c.delete(self.bulletl)
                                            
        if exist(c,self.bulletr)==True:
            if (c.bbox(self.bulletr)[2]<520):
                c.move(self.bulletr,20,0)
            else:
                c.delete(self.bulletr)
            for i in g:
                if c.bbox(self.bulletr)==None:
                    break
                else:
                    (x1,y1,x2,y2)=c.bbox(self.bulletr)
                    if (c.bbox(i)==None):
                        continue
                    else:
                        (u1,v1,u2,v2)=c.bbox(i)
                        if (x1>u1 and y1>v1 and x2<u2 and y2<v2):
                            c.delete(i)
                            c.delete(self.bulletr)


        

        


class EnemyTank:
    def __init__(self,c,x,y,etu,etd,etl,etr,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8):
        c.create_image(x,y,image=etd,state='normal',anchor='nw',tags=tag1)
        c.create_image(x,y,image=etu,state='hidden',anchor='nw',tags=tag2)
        c.create_image(x,y,image=etl,state='hidden',anchor='nw',tags=tag3)
        c.create_image(x,y,image=etr,state='hidden',anchor='nw',tags=tag4)
        self.etankd=tag1
        self.etanku=tag2
        self.etankl=tag3
        self.etankr=tag4
        self.ebulletd=tag5
        self.ebulletu=tag6
        self.ebulletl=tag7
        self.ebulletr=tag8
        self.life=1
    def Move(self,c,gm,b,g):
        def MoveUp():
            c.itemconfig(self.etankd,state='hidden')
            c.itemconfig(self.etanku,state='normal')
            c.itemconfig(self.etankl,state='hidden')
            c.itemconfig(self.etankr,state='hidden')
            if c.itemcget(self.etankd,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankd)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0-40
            if c.itemcget(self.etanku,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etanku)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0-40
            if c.itemcget(self.etankl,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankl)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0-40
            if c.itemcget(self.etankr,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankr)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0-40
            gp=getposition(c,gm)
            if (b1>=39 and gp.count((a0,b0))==0):
                c.move(self.etankd,0,-40)
                c.move(self.etanku,0,-40)
                c.move(self.etankl,0,-40)
                c.move(self.etankr,0,-40)
        def MoveDown():
            c.itemconfig(self.etankd,state='normal')
            c.itemconfig(self.etanku,state='hidden')
            c.itemconfig(self.etankl,state='hidden')
            c.itemconfig(self.etankr,state='hidden')
            if c.itemcget(self.etankd,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankd)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0+40
            if c.itemcget(self.etanku,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etanku)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0+40
            if c.itemcget(self.etankl,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankl)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0+40
            if c.itemcget(self.etankr,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankr)
                a0=(a1+a2)/2.0
                b0=(b1+b2)/2.0+40
            gp=getposition(c,gm)
            if (b2<=481 and gp.count((a0,b0))==0):
                c.move(self.etankd,0,40)
                c.move(self.etanku,0,40)
                c.move(self.etankl,0,40)
                c.move(self.etankr,0,40)
        def MoveLeft():
            c.itemconfig(self.etankd,state='hidden')
            c.itemconfig(self.etanku,state='hidden')
            c.itemconfig(self.etankl,state='normal')
            c.itemconfig(self.etankr,state='hidden')
            if c.itemcget(self.etankd,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankd)
                a0=(a1+a2)/2.0-40
                b0=(b1+b2)/2.0
            if c.itemcget(self.etanku,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etanku)
                a0=(a1+a2)/2.0-40
                b0=(b1+b2)/2.0
            if c.itemcget(self.etankl,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankl)
                a0=(a1+a2)/2.0-40
                b0=(b1+b2)/2.0
            if c.itemcget(self.etankr,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankr)
                a0=(a1+a2)/2.0-40
                b0=(b1+b2)/2.0
            gp=getposition(c,gm)
            if (a1>=39 and gp.count((a0,b0))==0):
                c.move(self.etankd,-40,0)
                c.move(self.etanku,-40,0)
                c.move(self.etankl,-40,0)
                c.move(self.etankr,-40,0)
        def MoveRight():
            c.itemconfig(self.etankd,state='hidden')
            c.itemconfig(self.etanku,state='hidden')
            c.itemconfig(self.etankl,state='hidden')
            c.itemconfig(self.etankr,state='normal')
            if c.itemcget(self.etankd,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankd)
                a0=(a1+a2)/2.0+40
                b0=(b1+b2)/2.0
            if c.itemcget(self.etanku,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etanku)
                a0=(a1+a2)/2.0+40
                b0=(b1+b2)/2.0
            if c.itemcget(self.etankl,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankl)
                a0=(a1+a2)/2.0+40
                b0=(b1+b2)/2.0
            if c.itemcget(self.etankr,'state')=='normal':
                (a1,b1,a2,b2)=c.bbox(self.etankr)
                a0=(a1+a2)/2.0+40
                b0=(b1+b2)/2.0
            gp=getposition(c,gm)
            if (a2<=481 and gp.count((a0,b0))==0):
                c.move(self.etankd,40,0)
                c.move(self.etanku,40,0)
                c.move(self.etankl,40,0)
                c.move(self.etankr,40,0)


                
        d=randrange(1,5)
        if d==1:
            MoveUp()
        elif d==2:
            MoveDown()
        elif d==3:
            MoveLeft()
        else:
            MoveRight()


        
    def Shoot(self,c,b,g):
        def CreateBullet():
            if (c.itemcget(self.etankd,'state')=='normal' and exist(c,self.ebulletd)==False and exist(c,self.ebulletu)==False and exist(c,self.ebulletl)==False and exist(c,self.ebulletr)==False):
                (x1,y1,x2,y2)=c.bbox(self.etankd)
                x0=(x1+x2)/2.0
                y0=y2
                c.create_image(x0,y0,image=b,tags=self.ebulletd)
            if (c.itemcget(self.etanku,'state')=='normal' and exist(c,self.ebulletd)==False and exist(c,self.ebulletu)==False and exist(c,self.ebulletl)==False and exist(c,self.ebulletr)==False):
                (x1,y1,x2,y2)=c.bbox(self.etanku)
                x0=(x1+x2)/2.0
                y0=y1
                c.create_image(x0,y0,image=b,tags=self.ebulletu)
            if (c.itemcget(self.etankr,'state')=='normal' and exist(c,self.ebulletd)==False and exist(c,self.ebulletu)==False and exist(c,self.ebulletl)==False and exist(c,self.ebulletr)==False):
                (x1,y1,x2,y2)=c.bbox(self.etankr)
                x0=x2
                y0=(y1+y2)/2.0
                c.create_image(x0,y0,image=b,tags=self.ebulletr)
            if (c.itemcget(self.etankl,'state')=='normal' and exist(c,self.ebulletd)==False and exist(c,self.ebulletu)==False and exist(c,self.ebulletl)==False and exist(c,self.ebulletr)==False):
                (x1,y1,x2,y2)=c.bbox(self.etankl)
                x0=x1
                y0=(y1+y2)/2.0
                c.create_image(x0,y0,image=b,tags=self.ebulletl)
        d=randrange(1,11)
        if d<=5:
            CreateBullet()

    def BulletFly(self,c,g):
        if exist(c,self.ebulletd)==True:
            if (c.bbox(self.ebulletd)[3]<520):
                c.move(self.ebulletd,0,20)
            else:
                c.delete(self.ebulletd)
            for i in g:
                if c.bbox(self.ebulletd)==None:
                    break
                else:
                    (x1,y1,x2,y2)=c.bbox(self.ebulletd)
                    if (c.bbox(i)==None):
                        continue
                    else:
                        (u1,v1,u2,v2)=c.bbox(i)
                        if (x1>u1 and y1>v1 and x2<u2 and y2<v2):
                            c.delete(i)
                            c.delete(self.ebulletd)
                                    
        if exist(c,self.ebulletu)==True:
            if (c.bbox(self.ebulletu)[1]>0):
                c.move(self.ebulletu,0,-20)
            else:
                c.delete(self.ebulletu)
            for i in g:
                if c.bbox(self.ebulletu)==None:
                    break
                else:
                    (x1,y1,x2,y2)=c.bbox(self.ebulletu)
                    if (c.bbox(i)==None):
                        continue
                    else:
                        (u1,v1,u2,v2)=c.bbox(i)
                        if (x1>u1 and y1>v1 and x2<u2 and y2<v2):
                            c.delete(i)
                            c.delete(self.ebulletu)
                                                
        if exist(c,self.ebulletl)==True:
            if (c.bbox(self.ebulletl)[0]>0):
                c.move(self.ebulletl,-20,0)
            else:
                    c.delete(self.ebulletl)
            for i in g:
                if c.bbox(self.ebulletl)==None:
                    break
                else:
                    (x1,y1,x2,y2)=c.bbox(self.ebulletl)
                    if (c.bbox(i)==None):
                        continue
                    else:
                        (u1,v1,u2,v2)=c.bbox(i)
                        if (x1>u1 and y1>v1 and x2<u2 and y2<v2):
                            c.delete(i)
                            c.delete(self.ebulletl)
                                            
        if exist(c,self.ebulletr)==True:
            if (c.bbox(self.ebulletr)[2]<520):
                c.move(self.ebulletr,20,0)
            else:
                c.delete(self.ebulletr)
            for i in g:
                if c.bbox(self.ebulletr)==None:
                    break
                else:
                    (x1,y1,x2,y2)=c.bbox(self.ebulletr)
                    if (c.bbox(i)==None):
                        continue
                    else:
                        (u1,v1,u2,v2)=c.bbox(i)
                        if (x1>u1 and y1>v1 and x2<u2 and y2<v2):
                            c.delete(i)
                            c.delete(self.ebulletr)

       

            

            
        
            
        

def main():
    root=Tk()
    root.title('tankgame')
    c=Canvas(root,width=520,height=520,bg='black')
    c.pack()
    tu=PhotoImage(file="F:\\tankgame\\tanku.gif")
    td=PhotoImage(file="F:\\tankgame\\tankd.gif")
    tl=PhotoImage(file="F:\\tankgame\\tankl.gif")
    tr=PhotoImage(file="F:\\tankgame\\tankr.gif")
    wtu=PhotoImage(file="F:\\tankgame\\wtanku.gif")
    wtd=PhotoImage(file="F:\\tankgame\\wtankd.gif")
    wtl=PhotoImage(file="F:\\tankgame\\wtankl.gif")
    wtr=PhotoImage(file="F:\\tankgame\\wtankr.gif")
    etu=PhotoImage(file="F:\\tankgame\\etanku.gif")
    etd=PhotoImage(file="F:\\tankgame\\etankd.gif")
    etl=PhotoImage(file="F:\\tankgame\\etankl.gif")
    etr=PhotoImage(file="F:\\tankgame\\etankr.gif")
    o=PhotoImage(file="F:\\tankgame\\obstacle.gif")
    base=PhotoImage(file="F:\\tankgame\\base.gif")
    b=PhotoImage(file="F:\\tankgame\\bullet.gif")
    win=PhotoImage(file="F:\\tankgame\\win.gif")
    lose=PhotoImage(file="F:\\tankgame\\lose.gif")
    c.create_image(40,40,image=o,anchor='nw',tags='o1')
    c.create_image(40,80,image=o,anchor='nw',tags='o2')
    c.create_image(40,120,image=o,anchor='nw',tags='o3')
    c.create_image(40,160,image=o,anchor='nw',tags='o4')
    c.create_image(120,40,image=o,anchor='nw',tags='o5')
    c.create_image(120,80,image=o,anchor='nw',tags='o6')
    c.create_image(120,120,image=o,anchor='nw',tags='o7')
    c.create_image(120,160,image=o,anchor='nw',tags='o8')
    c.create_image(200,40,image=o,anchor='nw',tags='o9')
    c.create_image(200,80,image=o,anchor='nw',tags='o10')
    c.create_image(200,120,image=o,anchor='nw',tags='o11')
    c.create_image(200,160,image=o,anchor='nw',tags='o12')
    c.create_image(280,40,image=o,anchor='nw',tags='o13')
    c.create_image(280,80,image=o,anchor='nw',tags='o14')
    c.create_image(280,120,image=o,anchor='nw',tags='o15')
    c.create_image(280,160,image=o,anchor='nw',tags='o16')
    c.create_image(360,40,image=o,anchor='nw',tags='o17')
    c.create_image(360,80,image=o,anchor='nw',tags='o18')
    c.create_image(360,120,image=o,anchor='nw',tags='o19')
    c.create_image(360,160,image=o,anchor='nw',tags='o20')
    c.create_image(440,40,image=o,anchor='nw',tags='o21')
    c.create_image(440,80,image=o,anchor='nw',tags='o22')
    c.create_image(440,120,image=o,anchor='nw',tags='o23')
    c.create_image(440,160,image=o,anchor='nw',tags='o24')
    c.create_image(0,240,image=o,anchor='nw',tags='o25')
    c.create_image(80,240,image=o,anchor='nw',tags='o26')
    c.create_image(160,240,image=o,anchor='nw',tags='o27')
    c.create_image(240,240,image=o,anchor='nw',tags='o28')
    c.create_image(320,240,image=o,anchor='nw',tags='o29')
    c.create_image(400,240,image=o,anchor='nw',tags='o30')
    c.create_image(480,240,image=o,anchor='nw',tags='o31')
    c.create_image(40,320,image=o,anchor='nw',tags='o32')
    c.create_image(40,360,image=o,anchor='nw',tags='o33')
    c.create_image(120,320,image=o,anchor='nw',tags='o34')
    c.create_image(120,360,image=o,anchor='nw',tags='o35')
    c.create_image(200,320,image=o,anchor='nw',tags='o36')
    c.create_image(200,360,image=o,anchor='nw',tags='o37')
    c.create_image(280,320,image=o,anchor='nw',tags='o38')
    c.create_image(280,360,image=o,anchor='nw',tags='o39')
    c.create_image(360,320,image=o,anchor='nw',tags='o40')
    c.create_image(360,360,image=o,anchor='nw',tags='o41')
    c.create_image(440,320,image=o,anchor='nw',tags='o42')
    c.create_image(440,360,image=o,anchor='nw',tags='o43')
    c.create_image(200,440,image=o,anchor='nw',tags='o44')
    c.create_image(200,480,image=o,anchor='nw',tags='o45')
    c.create_image(280,440,image=o,anchor='nw',tags='o46')
    c.create_image(280,480,image=o,anchor='nw',tags='o47')
    c.create_image(240,440,image=o,anchor='nw',tags='o48')
    c.create_image(240,480,image=base,anchor='nw',tags='o49')
    g=['o1','o2','o3','o4','o5','o6','o7','o8','o9','o10','o11','o12','o13','o14','o15','o16','o17','o18','o19','o20','o21','o22','o23','o24','o25','o26','o27','o28','o29','o30','o31','o32','o33','o34','o35','o36','o37','o38','o39','o40','o41','o42','o43','o44','o45','o46','o47','o48','o49']
    tankg=g+['enemytankd1','enemytanku1','enemytankl1','enemytankr1','enemytanku2','enemytankl2','enemytankr2','enemytankd2','enemytankd3','enemytanku3','enemytankl3','enemytankr3']
    enemyg=g+['tankd1','tanku1','tankl1','tankr1']
    tank1=['tankd1','tanku1','tankl1','tankr1']
    tank1gm=g+['enemytankd1','enemytanku1','enemytankl1','enemytankr1','enemytanku2','enemytankd2','enemytankl2','enemytankr2','enemytankd3','enemytanku3','enemytankl3','enemytankr3']
    enemy1gm=g+['tankd1','tanku1','tankl1','tankr1','enemytankd2','enemytanku2','enemytankl2','enemytankr2','enemytankd3','enemytanku3','enemytankl3','enemytankr3']
    enemy2gm=g+['tankd1','tanku1','tankl1','tankr1','enemytankd1','enemytanku1','enemytankl1','enemytankr1','enemytankd3','enemytanku3','enemytankl3','enemytankr3']
    enemy3gm=g+['tankd1','tanku1','tankl1','tankr1','enemytankd2','enemytanku2','enemytankl2','enemytankr2','enemytankd1','enemytanku1','enemytankl1','enemytankr1']
    mytank1=MyTank(c,160,480,tu,td,tl,tr,2,'tankd1','tanku1','tankl1','tankr1','bulletd1','bulletu1','bulletl1','bulletr1')
    allbullet=['ebulletd1','ebulletu1','ebulletl1','ebulletr1','ebulletd2','ebulletu2','ebulletl2','ebulletr2','ebulletd3','ebulletu3','ebulletl3','ebulletr3','bulletd1','bulletu1','bulletl1','bulletr1']
    mytank1.Move(c,'<Up>','<Down>','<Left>','<Right>',tank1gm)
    mytank1.Shoot(c,'<space>',b)
    c.focus_set()
    enemytank1=EnemyTank(c,0,0,etu,etd,etl,etr,'enemytankd1','enemytanku1','enemytankl1','enemytankr1','ebulletd1','ebulletu1','ebulletl1','ebulletr1')
    enemytank2=EnemyTank(c,480,0,etu,etd,etl,etr,'enemytankd2','enemytanku2','enemytankl2','enemytankr2','ebulletd2','ebulletu2','ebulletl2','ebulletr2')
    enemytank3=EnemyTank(c,240,0,etu,etd,etl,etr,'enemytankd3','enemytanku3','enemytankl3','enemytankr3','ebulletd3','ebulletu3','ebulletl3','ebulletr3')
    enemytank=['enemytankd1','enemytanku1','enemytankl1','enemytankr1','enemytankd2','enemytanku2','enemytankl2','enemytankr2','enemytankd3','enemytanku3','enemytankl3','enemytankr3']
    t=0
    while (existtank(c,tank1)==False and existtank(c,enemytank)==False and exist(c,'o49')==True):
        if (exist(c,enemytank1.etankd)==True or exist(c,enemytank1.etanku)==True or exist(c,enemytank1.etankl)==True or exist(c,enemytank1.etankr)==True):
            enemytank1.Move(c,enemy1gm,b,enemyg)
        if (exist(c,enemytank2.etankd)==True or exist(c,enemytank2.etanku)==True or exist(c,enemytank2.etankl)==True or exist(c,enemytank2.etankr)==True):
            enemytank2.Move(c,enemy2gm,b,enemyg)
        if (exist(c,enemytank3.etankd)==True or exist(c,enemytank3.etanku)==True or exist(c,enemytank3.etankl)==True or exist(c,enemytank3.etankr)==True):
            enemytank3.Move(c,enemy3gm,b,enemyg)
        enemytank1.Shoot(c,b,enemyg)
        enemytank2.Shoot(c,b,enemyg)
        enemytank3.Shoot(c,b,enemyg)
        while (existbullet(c,allbullet)==True):
            enemytank1.BulletFly(c,enemyg)
            enemytank2.BulletFly(c,enemyg)
            enemytank3.BulletFly(c,enemyg)
            mytank1.BulletFly(c,tankg)
            if existtank(c,tank1):
                if (mytank1.life>0):
                    c.delete('tankd1')
                    c.delete('tanku1')
                    c.delete('tankl1')
                    c.delete('tankr1')
                    mytank1.life=mytank1.life-1
                    c.create_image(160,480,image=td,state='hidden',anchor='nw',tags='tankd1')
                    c.create_image(160,480,image=tu,state='normal',anchor='nw',tags='tanku1')
                    c.create_image(160,480,image=tl,state='hidden',anchor='nw',tags='tankl1')
                    c.create_image(160,480,image=tr,state='hidden',anchor='nw',tags='tankr1')
                else:
                    c.create_image(260,260,image=lose)
                    break
            if existtank(c,enemytank):
                c.create_image(260,260,image=win)
                break
            if exist(c,'o49')==False:
                c.create_image(260,260,image=lose)
                break
            c.update()
            sleep(0.02)
        
            
        c.update()
        sleep(0.1)
    c.mainloop()


main()
        
        
        
        
        
