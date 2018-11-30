def exist(c,t):
    if c.bbox(t)==None:
        return False
    else:
        return True

def getposition(c,g):
    gp=[]
    for i in g:
        if c.bbox(i)==None:
            continue
        else:
            (x1,y1,x2,y2)=c.bbox(i)
            x0=(x1+x2)/2.0
            y0=(y1+y2)/2.0
            gp=gp+[(x0,y0)]
    return gp

def existbullet(c,allbullet):
    for i in allbullet:
        if exist(c,i)==True:
            return True
    return False

def existtank(c,tank):
    for i in tank:
        if exist(c,i)==True:
            return False
    return True
        



