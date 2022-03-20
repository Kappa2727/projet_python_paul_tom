# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:20:26 2022

@author: paulc
"""

from modele import *




def etablirplateau():
    fond= Canvas(frame3,width=1980,height=1080,bg="black") #le fond du jeu
    fond.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    
    CAN_ALLIE = Canvas(frame3,width=CANVA_TAIL,height=CANVA_TAIL,bg="white",highlightthickness=0) #highlightthickness=0 permet d'enlever les ombres (plus esthétique)
    CAN_ALLIE.place(relx=0.5,rely=0.25,anchor=CENTER) #la grille allie est place parallèlement a la grille ennemi sur l'axe horizontale 
    for row in range(len(GRILLE_ALLIE)):
        for col in range(len(GRILLE_ALLIE[row])):
            CAN_ALLIE.create_rectangle(col * CASE_TAIL,row * CASE_TAIL,col * CASE_TAIL + CASE_TAIL,row * CASE_TAIL + CASE_TAIL,outline="black") #utilisation de la taille des cellules pour definir le point d'origine en haut a gauche, vers le point d'arrivée en bas a droite
                

    CAN_ENNEMI = Canvas(frame3,width=CANVA_TAIL,height=CANVA_TAIL,bg="white",highlightthickness=0)
    CAN_ENNEMI.place(relx=0.5,rely=0.75,anchor=CENTER)
    for row in range(len(GRILLE_ENNEMI)):
        for col in range(len(GRILLE_ENNEMI[row])):
            CAN_ENNEMI.create_rectangle(col * CASE_TAIL,row * CASE_TAIL,col * CASE_TAIL + CASE_TAIL,row * CASE_TAIL + CASE_TAIL,outline="black")
            
def OuvrirPlacementBateaux():
    frame1.destroy() #permet de détruire la frame1, c'est a dire le menu du jeu
    frame2.pack() #permet de positionner la frame2 en avant, c'est a dire la fenêtre du placement des Bateaux
    PlacementBateaux() #appel la fonction permettant de placer les bateaux sur ça grille avant de commencer la partie
        
def menu():
    frame1.pack() #permet de positionner la frame2 en avant, c'est a dire le menu du jeu
    Boutonjouer= Button(frame1, width=10, height=2,text="jouer", command=OuvrirPlacementBateaux) #un bouton jouer qui permet d'appeler la fonction OuvrirPlacementBateaux
    BoutonQuitter= Button(frame1, width=10, height=2,text="quitter", command=main.destroy) #un bouton qui permet de  fermer le jeu
    Boutonjouer.place(relx=0.5, rely=0.40, anchor=CENTER)
    BoutonQuitter.place(relx=0.5, rely=0.60, anchor=CENTER)
    
def OuvrirLeCombat():
    frame2.destroy() #permet de détruire la frame2, c'est a dire fenêtre du placement des Bateaux
    frame3.pack() #permet de positionner la frame3 en avant, c'est a dire la zone de combat navale
    etablirplateau() #appel la fonction permettant d'établir le plateau de la zone de combat navale

def PlacementBateaux():
    can_full_plac.pack()
    BoutonCommencer= Button(frame2, width=10, height=2,text="commencer", command=OuvrirLeCombat) #un bouton qui permet d'appeler la fonction OuvrirLeCombat
    BoutonCommencer.place(relx=0.5,rely=0.75,anchor=CENTER)
    can_full_plac.bind("<B1-Motion>",glisser)
    can_full_plac.bind("<Button-1>",clic)
    can_full_plac.bind("<Button-3>",RotationBateau)
    can_full_plac.bind("<ButtonRelease-1>",SlotagedesBateaux)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def RotationBateau(event): #fonction permettant de retourner le bateau a 5 cases
    old[0]=event.x
    old[1]=event.y
    x1_1, y1_1, x2_1, y2_1 = can_full_plac.coords(Bateau1)
    x1_2, y1_2, x2_2, y2_2 = can_full_plac.coords(Bateau2)
    x1_3, y1_3, x2_3, y2_3 = can_full_plac.coords(Bateau3)
    x1_4, y1_4, x2_4, y2_4 = can_full_plac.coords(Bateau4)
    x1_5, y1_5, x2_5, y2_5 = can_full_plac.coords(Bateau5)
    if (old[0] >= x1_1 and old[0] <= x2_1 and old[1] >= y1_1 and old[1] <= y2_1):
        can_full_plac.coords(Bateau1, x1_1, y1_1, x1_1+(y2_1-y1_1), y1_1+(x2_1-x1_1))
    if (old[0] >= x1_2 and old[0] <= x2_2 and old[1] >= y1_2 and old[1] <= y2_2):
        can_full_plac.coords(Bateau2, x1_2, y1_2, x1_2+(y2_2-y1_2), y1_2+(x2_2-x1_2))
    if (old[0] >= x1_3 and old[0] <= x2_3 and old[1] >= y1_3 and old[1] <= y2_3):
        can_full_plac.coords(Bateau3, x1_3, y1_3, x1_3+(y2_3-y1_3), y1_3+(x2_3-x1_3))
    if (old[0] >= x1_4 and old[0] <= x2_4 and old[1] >= y1_4 and old[1] <= y2_4):
        can_full_plac.coords(Bateau4, x1_4, y1_4, x1_4+(y2_4-y1_4), y1_4+(x2_4-x1_4))
    if (old[0] >= x1_5 and old[0] <= x2_5 and old[1] >= y1_5 and old[1] <= y2_5):
        can_full_plac.coords(Bateau5, x1_5, y1_5, x1_5+(y2_5-y1_5), y1_5+(x2_5-x1_5))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
def clic(event):
    old[0]=event.x
    old[1]=event.y

def glisser(event):
    x1_1, y1_1, x2_1, y2_1 = can_full_plac.coords(Bateau1)
    x1_2, y1_2, x2_2, y2_2 = can_full_plac.coords(Bateau2)
    x1_3, y1_3, x2_3, y2_3 = can_full_plac.coords(Bateau3)
    x1_4, y1_4, x2_4, y2_4 = can_full_plac.coords(Bateau4)
    x1_5, y1_5, x2_5, y2_5 = can_full_plac.coords(Bateau5)
    if (old[0] >= x1_1 and old[0] <= x2_1 and old[1] >= y1_1 and old[1] <= y2_1):
        can_full_plac.move(Bateau1, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y
    if (old[0] >= x1_2 and old[0] <= x2_2 and old[1] >= y1_2 and old[1] <= y2_2):
        can_full_plac.move(Bateau2, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y
    if (old[0] >= x1_3 and old[0] <= x2_3 and old[1] >= y1_3 and old[1] <= y2_3):
        can_full_plac.move(Bateau3, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y
    if (old[0] >= x1_4 and old[0] <= x2_4 and old[1] >= y1_4 and old[1] <= y2_4):
        can_full_plac.move(Bateau4, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y
    if (old[0] >= x1_5 and old[0] <= x2_5 and old[1] >= y1_5 and old[1] <= y2_5):
        can_full_plac.move(Bateau5, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y

def SlotagedesBateaux(event):
    x1_1, y1_1, x2_1, y2_1 = can_full_plac.coords(Bateau1)
    if 192<=x1_1 and 108<=y1_1 and 732>=x2_1 and 648>=y2_1:
        minix1=((x1_1)-(192))
        minix1_indice=192
        minix1_indicetableau=0
        for coordx in range(1,10):
            if x1_1==(192+(60*coordx)):
                if ((((x1_1)-(192+(60*coordx)))))<minix1:
                    minix1=(((x1_1)-(192+(60*coordx))))
                    minix1_indice=192+(60*coordx)
                    minix1_indicetableau=coordx
            if x1_1>(192+(60*coordx)):
                if ((x1_1)-(192+(60*coordx)))<minix1:
                    minix1=((x1_1)-(192+(60*coordx)))
                    minix1_indice=192+(60*coordx)
                    minix1_indicetableau=coordx
            if x1_1<(192+(60*coordx)):
                if ((((x1_1)-(192+(60*coordx))))*-1)<minix1:
                    minix1=(((x1_1)-(192+(60*coordx)))*-1)
                    minix1_indice=192+(60*coordx)
                    minix1_indicetableau=coordx
                    
        miniy1=((y1_1)-(108))
        miniy1_indice=108
        miniy1_indicetableau=0
        for coordy in range(1,10):
            if y1_1==(108+(60*coordy)):
                if ((((y1_1)-(108+(60*coordy)))))<miniy1:
                    miniy1=(((y1_1)-(108+(60*coordy))))
                    miniy1_indice=108+(60*coordy)
                    miniy1_indicetableau=coordy
            if y1_1>(108+(60*coordy)):
                if ((y1_1)-(108+(60*coordy)))<miniy1:
                    miniy1=((y1_1)-(108+(60*coordy)))
                    miniy1_indice=108+(60*coordy)
                    miniy1_indicetableau=coordy
            else :
                if ((((y1_1)-(108+(60*coordy))))*-1)<miniy1:
                    miniy1=(((y1_1)-(108+(60*coordy)))*-1)
                    miniy1_indice=108+(60*coordy)
                    miniy1_indicetableau=coordy
        minix2=((x2_1)-(192))
        minix2_indice=192
        minix2_indicetableau=0
        for coordx in range(1,10):
            if x2_1==(192+(60*coordx)):
                if ((((x2_1)-(192+(60*coordx)))))<minix2:
                    minix2=(((x2_1)-(192+(60*coordx))))
                    minix2_indice=192+(60*coordx)
                    minix2_indicetableau=coordx
            if x2_1>(192+(60*coordx)):
                if ((x2_1)-(192+(60*coordx)))<minix2:
                    minix2=((x2_1)-(192+(60*coordx)))
                    minix2_indice=192+(60*coordx)
                    minix2_indicetableau=coordx
            else:
                if ((((x2_1)-(192+(60*coordx))))*-1)<minix2:
                    minix2=(((x2_1)-(192+(60*coordx)))*-1)
                    minix2_indice=192+(60*coordx)
                    minix2_indicetableau=coordx
                    
        miniy2=((y2_1)-(108))
        miniy2_indice=108
        miniy2_indicetableau=0
        for coordy in range(1,10):
            if y2_1==(108+(60*coordy)):
                if ((((y2_1)-(108+(60*coordy)))))<miniy2:
                    miniy2=(((y2_1)-(108+(60*coordy))))
                    miniy2_indice=108+(60*coordy)
                    miniy2_indicetableau=coordy
            if y2_1>(108+(60*coordy)):
                if ((y2_1)-(108+(60*coordy)))<miniy2:
                    print(miniy2)
                    miniy2=((y2_1)-(108+(60*coordy)))
                    print(miniy2)
                    miniy2_indice=108+(60*coordy)
                    miniy2_indicetableau=coordy
            else:
                if ((((y2_1)-(108+(60*coordy))))*-1)<miniy2:
                    print(miniy2)
                    miniy2=(((y2_1)-(108+(60*coordy)))*-1)
                    print(miniy2)
                    miniy2_indice=108+(60*coordy)
                    miniy2_indicetableau=coordy
        
        verificationbateau=True
        for i in range(minix1_indicetableau,minix1_indicetableau):
            for j in range(miniy1_indicetableau, miniy2_indicetableau):
                if GRILLE_PlacementBateaux[i][j]==1:
                    verificationbateau=False
                else:
                    GRILLE_PlacementBateaux[i][j]=1
        if verificationbateau==True:
            can_full_plac.coords(Bateau1, minix1_indice, miniy1_indice, minix2_indice, miniy2_indice)
        else:
            can_full_plac.coords(Bateau1, 1440, 810, 1440+(x2_1-x1_1), 810+(y2_1-y1_1))
        


def show():
    menu()