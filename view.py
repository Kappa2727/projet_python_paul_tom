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
    CAN_PlacementBateaux = Canvas(frame2,width=CANVA_TAIL_Placement,height=CANVA_TAIL_Placement,bg="white",highlightthickness=0) #canva utilisé pour le placement des bateaux
    CAN_PlacementBateaux.place(relx=0.25,rely=0.5,anchor=CENTER)
    for row in range(len(GRILLE_PlacementBateaux)):
        for col in range(len(GRILLE_PlacementBateaux[row])):
            CAN_PlacementBateaux.create_rectangle(col * CASE_TAIL_Placement,row * CASE_TAIL_Placement,col * CASE_TAIL_Placement + CASE_TAIL_Placement,row * CASE_TAIL_Placement + CASE_TAIL_Placement,outline="black") #grille du placement des bateaux
    BoutonCommencer= Button(frame2, width=10, height=2,text="commencer", command=OuvrirLeCombat) #un bouton qui permet d'appeler la fonction OuvrirLeCombat
    BoutonCommencer.place(relx=0.5,rely=0.75,anchor=CENTER)
    Bateau1.place(relx=0.5, rely=0.10)
    Bateau2.place(relx=0.5, rely=0.20)
    Bateau3.place(relx=0.5, rely=0.30)
    Bateau4.place(relx=0.5, rely=0.40)
    Bateau5.place(relx=0.5, rely=0.50)
    Bateau1.bind("<Button-3>", RotationBateau5cases) # les boutons permettant de faire un rotation du bateau quand on fais click droit dessus
    Bateau2.bind("<Button-3>", RotationBateau4cases)
    Bateau3.bind("<Button-3>", RotationBateau3cases)
    Bateau4.bind("<Button-3>", RotationBateau3cases_2)
    Bateau5.bind("<Button-3>", RotationBateau2cases)
    Bateau1.bind("<B1-Motion>", deplacement)
    


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def RotationBateau5cases(event): #fonction permettant de retourner le bateau a 5 cases
    Hauteur=Bateau1.winfo_height() #winfo_height permet d'enregistrer la hauteur du bateau choisis dans la variable Hauteur
    Largeur=Bateau1.winfo_width() #winfo_width permet d'enregistrer la largeur du bateau choisis dans la variable Largeur
    Bateau1.configure(width=Hauteur, height=Largeur)

def RotationBateau4cases(event):#fonction permettant de retourner le bateau a 4 cases
    Hauteur=Bateau2.winfo_height()
    Largeur=Bateau2.winfo_width()
    Bateau2.configure(width=Hauteur, height=Largeur)
   

def RotationBateau3cases(event):#fonction permettant de retourner le bateau a 3 cases
    Hauteur=Bateau3.winfo_height()
    Largeur=Bateau3.winfo_width()
    Bateau3.configure(width=Hauteur, height=Largeur)

def RotationBateau3cases_2(event):#fonction permettant de retourner le bateau a 3 cases(l'autre)
   Hauteur=Bateau4.winfo_height()
   Largeur=Bateau4.winfo_width()
   Bateau4.configure(width=Hauteur, height=Largeur)
    
def RotationBateau2cases(event):#fonction permettant de retourner le bateau a 2 cases
    Hauteur=Bateau5.winfo_height()
    Largeur=Bateau5.winfo_width()
    Bateau5.configure(width=Hauteur, height=Largeur)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
def DefinirCoordXYSouris(event):
    global main
    CoordSourisX= event.x
    CoordSourisY= event.y
    print(CoordSourisX, CoordSourisY)
    

def deplacement(event):
    xtruc=Bateau1.winfo_x()
    ytruc=Bateau1.winfo_y()
    dx= event.x
    dy= event.y
    print(xtruc+dx, ytruc+dy)
    #On deplace la balle :
    Bateau1.place(x=xtruc-dx, y=ytruc-dy)



def show():
    menu()