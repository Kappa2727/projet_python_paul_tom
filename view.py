# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:20:26 2022

@author: paulc
"""

from modele import *


"""
fonction permettant d'établir le plateau de jeu avec les canvas contenant les grilles
"""
def etablirplateau():
    fond= Canvas(main,width=1980,height=1080,bg="black") #le fond du jeu
    fond.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    
    CAN_ALLIE = Canvas(main,width=CAN_SIZE,height=CAN_SIZE,bg="white",highlightthickness=0) #highlightthickness=0 permet d'enlever les ombres (plus esthétique)
    CAN_ALLIE.place(relx=0.5,rely=0.25,anchor=CENTER) #la grille allie est place parallèlement a la grille ennemi sur l'axe horizontale 
    for row in range(len(GRILLE_ALLIE)):
        for col in range(len(GRILLE_ALLIE[row])):
            CAN_ALLIE.create_rectangle(col * CELL_SIZE,row * CELL_SIZE,col * CELL_SIZE + CELL_SIZE,row * CELL_SIZE + CELL_SIZE,outline="black") #utilisation de la taille des cellules pour definir le point d'origine en haut a gauche, vers le point d'arrivée en bas a droite
                

    CAN_ENNEMI = Canvas(main,width=CAN_SIZE,height=CAN_SIZE,bg="white",highlightthickness=0)
    CAN_ENNEMI.place(relx=0.5,rely=0.75,anchor=CENTER)
    for row in range(len(GRILLE_ENNEMI)):
        for col in range(len(GRILLE_ENNEMI[row])):
            CAN_ENNEMI.create_rectangle(col * CELL_SIZE,row * CELL_SIZE,col * CELL_SIZE + CELL_SIZE,row * CELL_SIZE + CELL_SIZE,outline="black")


def show():
    etablirplateau()