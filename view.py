# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:20:26 2022

@author: paulc
"""

from tkinter import *


root = Tk()
root.state("zoomed")

CAN_SIZE = 360
CELL_SIZE = CAN_SIZE / 9

grille_allie = [[0 for i in range(9)] for i in range(9)]



fond= Canvas(root,width=500,height=500,bg="black")
fond.place(relx=0.5,rely=0.5,anchor=CENTER)

can_allie = Canvas(root,
                                   width=CAN_SIZE,
                                   height=CAN_SIZE,
                                   bg="white",highlightthickness=0)
can_allie.place(relx=0.5,rely=0.25,anchor=CENTER)
 
 
for row in range(len(grille_allie)):
            for col in range(len(grille_allie[row])):
                c = can_allie.create_rectangle(col * CELL_SIZE,
                                                row * CELL_SIZE,
                                                col * CELL_SIZE + CELL_SIZE,
                                                row * CELL_SIZE + CELL_SIZE,
                                                outline="black",
                                                tags="a"+str(col)+str(row))
                

grille_ennemi = [[0 for i in range(9)] for i in range(9)]



can_ennemi = Canvas(root,
                                   width=CAN_SIZE,
                                   height=CAN_SIZE,
                                   bg="white",highlightthickness=0)
can_ennemi.place(relx=0.5,rely=0.75,anchor=CENTER)
 
 
for row in range(len(grille_ennemi)):
            for col in range(len(grille_ennemi[row])):
                c = can_ennemi.create_rectangle(col * CELL_SIZE,
                                                row * CELL_SIZE,
                                                col * CELL_SIZE + CELL_SIZE,
                                                row * CELL_SIZE + CELL_SIZE,
                                                outline="black",
                                                tags="a"+str(col)+str(row))



bit=Entry(root,fg="black",bg="white")

bit.pack()

root.mainloop()