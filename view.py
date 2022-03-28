# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:20:26 2022

@author: paulc
"""

from modele import *



def etablirplateau():
    global CAN_ALLIE
    global CAN_ENNEMI
    fond= Canvas(frame3,width=1980,height=1080,bg="black") #le fond du jeu
    fond.place(relx=0.5,rely=0.5,anchor=CENTER)
    global GRILLE_PlacementBateaux
    
    CAN_ALLIE = Canvas(frame3,width=CANVA_TAIL,height=CANVA_TAIL,bg="white",highlightthickness=0)
    CAN_ENNEMI = Canvas(frame3,width=CANVA_TAIL,height=CANVA_TAIL,bg="white",highlightthickness=0)
    CAN_ALLIE.place(relx=0.5,rely=0.25,anchor=CENTER) #la grille allie est place parallèlement a la grille ennemi sur l'axe horizontale
    CAN_ENNEMI.place(relx=0.5,rely=0.75,anchor=CENTER)
     
    for row in range(len(GRILLE_ALLIE)):
        for col in range(len(GRILLE_ALLIE[row])):
            CAN_ALLIE.create_rectangle(col * CASE_TAIL,row * CASE_TAIL,col * CASE_TAIL + CASE_TAIL,row * CASE_TAIL + CASE_TAIL,outline="black", tags="a2" + str(col) + str(row)) #utilisation de la taille des cellules pour definir le point d'origine en haut a gauche, vers le point d'arrivée en bas a droite
    
    for l in range(len(GRILLE_PlacementBateaux)):
        for c in range(len(GRILLE_PlacementBateaux[l])):
            if GRILLE_PlacementBateaux[c][l]==1:
                CAN_ALLIE.create_rectangle(CASE_TAIL*c,CASE_TAIL*l,(CASE_TAIL*c)+CASE_TAIL,(CASE_TAIL*l)+CASE_TAIL, fill="black", tags="a" + str(c) + str(l))  
                GRILLE_ALLIE[c][l]=1

    
    
    for row in range(len(GRILLE_ENNEMI)):
        for col in range(len(GRILLE_ENNEMI[row])):
            CAN_ENNEMI.create_rectangle(col * CASE_TAIL,row * CASE_TAIL,col * CASE_TAIL + CASE_TAIL,row * CASE_TAIL + CASE_TAIL,outline="black", tags="e2" + str(col) + str(row))
    
    for l in range(len(GRILLE_ENNEMI)):
        for c in range(len(GRILLE_ENNEMI[l])):
            if GRILLE_ENNEMI[l][c]==1:
                CAN_ENNEMI.create_rectangle(CASE_TAIL*l,CASE_TAIL*c,(CASE_TAIL*l)+CASE_TAIL,(CASE_TAIL*c)+CASE_TAIL, fill="black", tags="e" + str(c) + str(l))
    
    
    CAN_ALLIE.bind("<Button-1>",tirallie)
    
    
def OuvrirPlacementBateaux():
    frame1.destroy() #permet de détruire la frame1, c'est a dire le menru du jeu
    frame2.pack() #permet de positionner la frame2 en avant, c'est a dire la fenêtre du placement des Bateaux
    PlacementBateaux() #appel la fonction permettant de placer les bateaux sur ça grille avant de commencer la partie
        
def menu():
    global img
    frame1.pack() #permet de positionner la frame2 en avant, c'est a dire le menu du jeu
    
    
    can_menu.pack()
    can_menu.create_image((960,540), image=img, anchor=CENTER)
    
    
    
    Boutonjouer= Button(frame1, width=10, height=2,text="jouer", command=OuvrirPlacementBateaux) #un bouton jouer qui permet d'appeler la fonction OuvrirPlacementBateaux
    BoutonQuitter= Button(frame1, width=10, height=2,text="quitter", command=main.destroy) #un bouton qui permet de  fermer le jeu
    Boutonjouer.place(relx=0.5, rely=0.40, anchor=CENTER)
    BoutonQuitter.place(relx=0.5, rely=0.60, anchor=CENTER)
    
def OuvrirLeCombat():
    global comptb
    global can_full_plac
    if comptb!=0:
        can_full_plac.create_text(1344, 810, anchor =CENTER, text ="tous les bateaux doivent être placer avant de commencer", fill ="black", font="Arial 30 bold")
    else:
        frame2.destroy() #permet de détruire la frame2, c'est a dire fenêtre du placement des Bateaux
        frame3.pack() #permet de positionner la frame3 en avant, c'est a dire la zone de combat navale
        etablirplateau() #appel la fonction permettant d'établir le plateau de la zone de combat navale

def tirallie(event):
    global comptrecur
    global CAN_ALLIE
    global GRILLE_ALLIE
    verif3=True
    if comptrecur%2==0:
        global CASE_TAIL
        global CAN_ALLIE
        global compt1allie
        mouseX = event.x
        mouseY = event.y
         
        grilleX = int(mouseX / CASE_TAIL)
        grilleY = int(mouseY / CASE_TAIL)
    
        tag = "a" + str(grilleX) + str(grilleY)
        
        CAN_ALLIE.itemconfig(tag, fill="red")
        comptrecur=comptrecur+1
        compt1allie=compt1allie-1
    tirenemi()

def tirenemi():
    global comptrecur
    global CAN_ENNEMI
    global GRILLE_ENNEMI
    verif3=True
    if comptrecur%2!=0:
        tr=0
        while verif3==True:
            print(tr)
            global GRILLE_ENNEMI
            global compt1ennemi
            verif1=True
            verif2=True
            r1 = random.randint(0, 8)
            r2 = random.randint(0, 8)
            if GRILLE_ENNEMI[r1][r2]==2:
                verif1=False
            if GRILLE_ENNEMI[r1][r2]==3:
                verif2=False
        
            if verif1==True and verif2==True:
                if GRILLE_ENNEMI[r1][r2]==1:
                    tag = "e" + str(r2) + str(r1)
                    CAN_ENNEMI.itemconfig(tag, fill="red")
                    comptrecur=comptrecur+1
                    GRILLE_ENNEMI[r2][r1]=2
                    compt1ennemi=compt1ennemi-1
                    verif3=False
                    print("b")
                if GRILLE_ENNEMI[r1][r2]==0:
                    tag = "e2" + str(r2) + str(r1)
                    CAN_ENNEMI.itemconfig(tag, fill="gray")
                    comptrecur=comptrecur+1
                    GRILLE_ENNEMI[r2][r1]=3
                    verif3=False
                    print("c")
            tr=tr+1
                
        
   

def PlacementBateaux():
    can_full_plac.pack()
    BoutonCommencer= Button(frame2, width=10, height=2,text="commencer", command=OuvrirLeCombat) #un bouton qui permet d'appeler la fonction OuvrirLeCombat
    BoutonCommencer.place(relx=0.5,rely=0.75,anchor=CENTER)
    BoutonReset= Button(frame2, width=10, height=2, text="reset", command=SlotagedesBateauxReset)
    BoutonReset.place(relx=0.40, rely=0.75, anchor=CENTER)
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
    global comptb
    for i in range(len(Bateau)):
        verificationbateau=True
        verifgrille=True
        x1_1, y1_1, x2_1, y2_1 = can_full_plac.coords(Bateau[i])
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
                        miniy2=((y2_1)-(108+(60*coordy)))
                        miniy2_indice=108+(60*coordy)
                        miniy2_indicetableau=coordy
                else:
                    if ((((y2_1)-(108+(60*coordy))))*-1)<miniy2:
                        miniy2=(((y2_1)-(108+(60*coordy)))*-1)
                        miniy2_indice=108+(60*coordy)
                        miniy2_indicetableau=coordy
                        
                        
            for i2 in range(minix1_indicetableau,minix2_indicetableau):
                for j2 in range(miniy1_indicetableau, miniy2_indicetableau):
                    if GRILLE_PlacementBateaux[i2][j2]==1:
                        verifgrille=False
                        verificationbateau=False
            if verifgrille==True:
                for i2 in range(minix1_indicetableau,minix2_indicetableau):
                    for j2 in range(miniy1_indicetableau, miniy2_indicetableau):
                        if GRILLE_PlacementBateaux[i2][j2]==0:
                            GRILLE_PlacementBateaux[i2][j2]=1
                        
            
            if verificationbateau==True:
                comptb=comptb-1
                can_full_plac.coords(Bateau[i],0,0,0,0)
                for l in range(len(GRILLE_PlacementBateaux)):
                    for c in range(len(GRILLE_PlacementBateaux[l])):
                        if GRILLE_PlacementBateaux[c][l]==1:
                            can_full_plac.create_rectangle(192+(CASE_TAIL_Placement*c),108+(CASE_TAIL_Placement*l),(192+(CASE_TAIL_Placement*c))+60,(108+(CASE_TAIL_Placement*l))+60, fill="black")
            else:
                can_full_plac.coords(Bateau[i], 1260, 630, 1260+(x2_1-x1_1), 630+(y2_1-y1_1))

def SlotagedesBateauxReset():
    print("a")
    global frame2
    global can_full_plac
    global GRILLE_PlacementBateaux
    frame2.destroy()
    frame2= Frame(main, width=1920,height=1080,bg="red")
    frame2.pack()
    GRILLE_PlacementBateaux = [[0 for i in range(9)] for i in range(9)]
    Bateauslot=[False,False,False,False,False]
    can_full_plac.destroy()
    can_full_plac= Canvas(frame2,width=1920,height=1080, bg="red",highlightthickness=0)
    for row in range(len(GRILLE_PlacementBateaux)):
        for col in range(len(GRILLE_PlacementBateaux[row])):
            can_full_plac.create_rectangle(192+(col * CASE_TAIL_Placement),108+(row * CASE_TAIL_Placement),192+(col * CASE_TAIL_Placement + CASE_TAIL_Placement),108+(row * CASE_TAIL_Placement + CASE_TAIL_Placement),outline="black",fill="white")
    Bateau1= can_full_plac.create_rectangle(960,108,960+(5*CASE_TAIL_Placement),108+CASE_TAIL_Placement, fill="black")
    Bateau2= can_full_plac.create_rectangle(960,216,960+(4*CASE_TAIL_Placement),216+CASE_TAIL_Placement, fill="black")
    Bateau3= can_full_plac.create_rectangle(960,324,960+(3*CASE_TAIL_Placement),324+CASE_TAIL_Placement, fill="black")
    Bateau4= can_full_plac.create_rectangle(960,432,960+(3*CASE_TAIL_Placement),432+CASE_TAIL_Placement, fill="black")
    Bateau5= can_full_plac.create_rectangle(960,540,960+(2*CASE_TAIL_Placement),540+CASE_TAIL_Placement, fill="black")
    Bateau=[Bateau1,Bateau2,Bateau3,Bateau4,Bateau5]
    PlacementBateaux()
    