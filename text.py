from Tkinter import *
from function import *
root=Tk()
c=Canvas(root,width=260,height=260,bg='black')
c.pack()
o=PhotoImage(file="F:\\tankgame\\obstacle.gif")
d=c.create_image(20,20,image=o,anchor='nw',tags='g')
c.delete('g')
c.create_image(20,20,image=o,anchor='nw',tags='g')
print exist(c,'g')
c.move('d',0,10)
g=['g','a']
print getposition(c,g)
