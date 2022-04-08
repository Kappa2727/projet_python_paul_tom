# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:20:26 2022

@author: paulc
"""

from tkinter import *
import random

"""
définition des variables globals qui seront utilisée pour le jeu
"""
global main
main= Tk()
global CANVA_TAIL #la taille des canvas utilisée pour le jeu
global CASE_TAIL #la taille des cellules du canva (cad: taille des carrès de la grille )
CANVA_TAIL = 405 #360, car c'est divisible par 9 et que c'est une taille convenable
CASE_TAIL = CANVA_TAIL / 9 

global frame1 #la fenêtre utilisé pour le menu du jeu
global frame2
global frame3
global frame4
global frame5
#img= PhotoImage(file='Bg-menu.png')
frame1= Frame(main, width=1920,height=1080,bg="black")
frame2= Frame(main, width=1920,height=1080,bg="red")
frame3= Frame(main, width=1920,height=1080,bg="red")
frame4= Frame(main, width=1920,height=1080,bg="red")
frame5= Frame(main, width=1920,height=1080,bg="blue")

global can_choix
can_choix=Canvas(frame5,width=1920, height=1080,bg="blue")

global can_menu
can_menu=Canvas(frame1,width=1920, height=1080,bg="blue")

global imgfondframe1
imgfondframe1=PhotoImage(file='Bg-menu.png', master=main)

global imgBoutjframe1
imgBoutjframe1=PhotoImage(file='Play-button2.gif', master=main)

global imgBoutqframe1
imgBoutqframe1=PhotoImage(file='Leave-button2.gif', master=main)

global imgBoutcframe1
imgBoutcframe1=PhotoImage(file='Start-button2.gif', master=main)

global can_full_fin
can_full_fin= Canvas(frame4,width=1920,height=1080, bg="red",highlightthickness=0)



#-------------------------------------------------------------------------------------------------------------------------------

"""
etablissement des variables globals pour le canva/grille allié et ennemi mais aussi pour le placement et déplacement des bateaux
"""

global can_full_plac
can_full_plac= Canvas(frame2,width=1920,height=1080, bg="red",highlightthickness=0)

global can_full_eta


global CAN_ALLIE
CAN_ALLIE = Canvas(frame3,width=CANVA_TAIL,height=CANVA_TAIL,bg="white",highlightthickness=0) #highlightthickness=0 permet d'enlever les ombres (plus esthétique)
global GRILLE_ALLIE
GRILLE_ALLIE = [[0 for i in range(9)] for i in range(9)] #le nombre de lignes et de colones qu'auront la grille de l'allié

global CAN_ENNEMI
CAN_ENNEMI = Canvas(frame3,width=CANVA_TAIL,height=CANVA_TAIL,bg="white",highlightthickness=0)
global GRILLE_ENNEMI
GRILLE_ENNEMI = [[0 for i in range(9)] for i in range(9)] #le nombre de lignes et de colones qu'auront la grille de l'ennemi


global GRILLE_PlacementBateaux
GRILLE_PlacementBateaux = [[0 for i in range(9)] for i in range(9)] #le nombre de lignes et de colones qu'auront la grille pour le placement des bateaux
global CANVA_TAIL_Placement #la taille des canvas utilisée pour la fenêtre du placement des bateaux
global CASE_TAIL_Placement #la taille des cellules du canva pour le placement des bateaux (cad: taille des carrès de la grille )
CANVA_TAIL_Placement = 540 #540, car c'est divisible par 9 et que c'est une taille convenable pour le placement des bateaux
CASE_TAIL_Placement = CANVA_TAIL_Placement / 9 # 9, parce qu'il y'a 9 lignes et 9 colones dans une grille de bataille navale, donc on divise par 9 la taille du canva utilisé pour afficher la grille

for row in range(len(GRILLE_PlacementBateaux)):
    for col in range(len(GRILLE_PlacementBateaux[row])):
        can_full_plac.create_rectangle(192+(col * CASE_TAIL_Placement),108+(row * CASE_TAIL_Placement),192+(col * CASE_TAIL_Placement + CASE_TAIL_Placement),108+(row * CASE_TAIL_Placement + CASE_TAIL_Placement),outline="black",fill="white") #grille du placement des bateaux

global Bateau1
global Bateau2
global Bateau3
global Bateau4
global Bateau5

 
Bateau1= can_full_plac.create_rectangle(960,108,960+(5*CASE_TAIL_Placement),108+CASE_TAIL_Placement, fill="black")
Bateau2= can_full_plac.create_rectangle(960,216,960+(4*CASE_TAIL_Placement),216+CASE_TAIL_Placement, fill="black")
Bateau3= can_full_plac.create_rectangle(960,324,960+(3*CASE_TAIL_Placement),324+CASE_TAIL_Placement, fill="black")
Bateau4= can_full_plac.create_rectangle(960,432,960+(3*CASE_TAIL_Placement),432+CASE_TAIL_Placement, fill="black")
Bateau5= can_full_plac.create_rectangle(960,540,960+(2*CASE_TAIL_Placement),540+CASE_TAIL_Placement, fill="black")

global Bateau
Bateau=[Bateau1,Bateau2,Bateau3,Bateau4,Bateau5]
global Bateauslot
Bateauslot=[False,False,False,False,False]

global old
old=[None,None]

global comptb
comptb=5

global compt1allie
compt1allie=17

global compt1ennemi
compt1ennemi=17

global comptplacementbateauennemi
comptplacementbateauennemi=[]


global comptrecur
comptrecur=0



global placementalea
def placementalea():
    i=0
    while len(comptplacementbateauennemi)!=5:
        verif1=True
        verif2=True
        verifcontient=False
        r1 = random.randint(0, 8)
        r2 = random.randint(1,2)
        r3 = random.randint(0, 3)
        if r2==1:
            if i!=3 and i!=4:
                for j in range(r3,r3+5-i):
                    if GRILLE_ENNEMI[r1][j]==1:
                        verif1=False
            if i==3:
                for j in range(r3,r3+5-2):
                    if GRILLE_ENNEMI[r1][j]==1:
                        verif1=False
            if i==4:
                for j in range(r3,r3+5-3):
                    if GRILLE_ENNEMI[r1][j]==1:
                        verif1=False
        if r2==2:
            if i!=3 and i!=4:
                for j in range(r3,r3+(5-i)):
                    if GRILLE_ENNEMI[j][r1]==1:
                        verif2=False
            if i==3:
                for j in range(r3,r3+5-2):
                    if GRILLE_ENNEMI[j][r1]==1:
                        verif2=False
            if i==4:
                for j in range(r3,r3+5-3):
                    if GRILLE_ENNEMI[j][r1]==1:
                        verif2=False
    
        if r2==1 and verif1==True:
            if i!=3 and i!=4:
                for k in range(len(comptplacementbateauennemi)):
                    if i==comptplacementbateauennemi[k]:
                        verifcontient=True
                if verifcontient==False:
                    comptplacementbateauennemi.append(i)
                    for j in range(r3,r3+5-i):
                        GRILLE_ENNEMI[r1][j]=1
                    
            if i==3:
                for k in range(len(comptplacementbateauennemi)):
                    if i==comptplacementbateauennemi[k]:
                        verifcontient=True
                if verifcontient==False:
                    comptplacementbateauennemi.append(i)
                    for j in range(r3,r3+5-2):
                        GRILLE_ENNEMI[r1][j]=1
            if i==4:
                for k in range(len(comptplacementbateauennemi)):
                    if i==comptplacementbateauennemi[k]:
                        verifcontient=True
                if verifcontient==False:
                    comptplacementbateauennemi.append(i)
                    for j in range(r3,r3+5-3):
                        GRILLE_ENNEMI[r1][j]=1
                    
        if r2==2 and verif2==True:
            if i!=3 and i!=4:
                for k in range(len(comptplacementbateauennemi)):
                    if i==comptplacementbateauennemi[k]:
                        verifcontient=True
                if verifcontient==False:
                    comptplacementbateauennemi.append(i)
                    for j in range(r3,r3+5-i):
                        GRILLE_ENNEMI[j][r1]=1
            if i==3:
                for k in range(len(comptplacementbateauennemi)):
                    if i==comptplacementbateauennemi[k]:
                        verifcontient=True
                if verifcontient==False:
                    comptplacementbateauennemi.append(i)
                    for j in range(r3,r3+5-2):
                        GRILLE_ENNEMI[j][r1]=1
            if i==4:
                for k in range(len(comptplacementbateauennemi)):
                    if i==comptplacementbateauennemi[k]:
                        verifcontient=True
                if verifcontient==False:
                    comptplacementbateauennemi.append(i)
                    for j in range(r3,r3+5-3):
                        GRILLE_ENNEMI[j][r1]=1
        if i==4:
            i=0
        
        i=i+1
placementalea()

    




#-------------------------------------------------------------------------------------------------------------------------------



