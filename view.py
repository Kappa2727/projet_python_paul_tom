# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:20:26 2022

@author: paulc
"""

from modele import *
import random
import time
import pygame

def etablirplateau():
    global CAN_ALLIE
    global CAN_ENNEMI

    fond= Canvas(frame3,width=1980,height=1080,bg="black") #le fond du jeu
    fond.place(relx=0.5,rely=0.5,anchor=CENTER)
    global GRILLE_PlacementBateaux
    global compt1allie
    global imgBoutqframe1
    global imgfondcombat
    fond.create_image((960,540), image=imgfondcombat, anchor=CENTER)
    pygame.mixer.stop
    pygame.mixer.music.load("bruitcombat.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(loops=-1)


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
                GRILLE_ALLIE[l][c]=1



    for row in range(len(GRILLE_ENNEMI)):
        for col in range(len(GRILLE_ENNEMI[row])):
            CAN_ENNEMI.create_rectangle(col * CASE_TAIL,row * CASE_TAIL,col * CASE_TAIL + CASE_TAIL,row * CASE_TAIL + CASE_TAIL,outline="black", tags="e_" + str(col) + str(row))

    for l in range(len(GRILLE_ENNEMI)):
        for c in range(len(GRILLE_ENNEMI[l])):
            if GRILLE_ENNEMI[l][c]==1:
                CAN_ENNEMI.create_rectangle(CASE_TAIL*l,CASE_TAIL*c,(CASE_TAIL*l)+CASE_TAIL,(CASE_TAIL*c)+CASE_TAIL, outline="black", tags="e" + str(c) + str(l))


    can_full_eta= Canvas(frame3,width=384,height=216, bg="blue")
    can_full_eta.place(relx=0.75, rely=0.5, anchor=CENTER)
    can_full_eta.create_text(10, 50, anchor=W, text ="Il vous reste : "+str(compt1ennemi)+"\n"+" parties de Bateau a touché", fill ="red", font="Arial 20 bold")
    BoutonQuitter= Button(frame3, width=200, height=100,image=imgBoutqframe1, command=quitterjeu) #un bouton qui permet de  fermer le jeu
    BoutonQuitter.place(relx=0.25, rely=0.75, anchor=CENTER)
    CAN_ENNEMI.bind("<Button-1>",tirallie)




def findejeu():

    global compt1allie
    global compt1ennemi
    global can_full_fin
    global imgBoutqframe1
    global imgBoutRecommencer
    global imgfondetabli

    pygame.mixer.music.load("musicdebut.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
    can_full_fin.pack()
    can_full_fin.create_image((960,540), image=imgfondetabli, anchor=CENTER)
    if compt1ennemi==0:
        can_full_fin.create_text(960, 400, anchor =CENTER, text ="Vous Avez Gagner", fill ="black", font="Arial 50 bold")
    else:
        can_full_fin.create_text(960, 400, anchor =CENTER, text ="Vous Avez Perdu", fill ="black", font="Arial 50 bold")
    BoutonQuitter= Button(frame4, width=200, height=100,image=imgBoutqframe1, command=quitterjeu) #un bouton qui permet de  fermer le jeu
    BoutonQuitter.place(relx=0.5, rely=0.65, anchor=CENTER)
    BoutonReset= Button(frame4, width=200, height=100, image=imgBoutRecommencer, command=findujeuReset)
    BoutonReset.place(relx=0.5, rely=0.5, anchor=CENTER)
def OuvrirPlacementBateaux():
    frame5.destroy() #permet de détruire la frame1, c'est a dire le menru du jeu
    frame2.pack() #permet de positionner la frame2 en avant, c'est a dire la fenêtre du placement des Bateaux
    PlacementBateaux() #appel la fonction permettant de placer les bateaux sur ça grille avant de commencer la partie



def choixdifficulte():
    global frame1
    global frame5
    frame1.destroy()
    frame5.pack()
    global can_choix
    global imgBoutFacile
    global imgBoutMoyen
    global imgBoutDifficile
    global imgchoixDif
    global imgfondetabli
    can_choix.pack()
    Boutonfacile= Button(frame5, width=200, height=100,image=imgBoutFacile, command=OuvrirPlacementBateaux) #un bouton jouer qui permet d'appeler la fonction OuvrirPlacementBateaux
    Boutonmoyen= Button(frame5, width=200, height=100,image=imgBoutMoyen, command=niveaumoyen)
    Boutondifficile= Button(frame5, width=200, height=100,image=imgBoutDifficile, command=niveaudifficile)
    can_choix.create_image((960,540), image=imgfondetabli, anchor=CENTER)
    can_choix.create_image((960,300), image=imgchoixDif, anchor=CENTER)
    Boutonfacile.place(relx=0.35, rely=0.50, anchor=CENTER)
    Boutonmoyen.place(relx=0.5, rely=0.50, anchor=CENTER)
    Boutondifficile.place(relx=0.65, rely=0.50, anchor=CENTER)

def niveaumoyen():
    comptmoyen=[]
    global GRILLE_ALLIE
    i=0
    while len(comptmoyen)!=35:
        verif1=True
        r5 = random.randint(0, 8)
        r6 = random.randint(0, 8)

        if GRILLE_ALLIE[r5][r6]==1 or GRILLE_ALLIE[r5][r6]==4:
            verif1=False

        if verif1==True:
            comptmoyen.append(i)
            GRILLE_ALLIE[r5][r6]=4
        i=i+1
    OuvrirPlacementBateaux()

def niveaudifficile():
    comptdifficile=[]
    global GRILLE_ALLIE
    i=0
    while len(comptdifficile)!=55:
        verif1=True
        r5 = random.randint(0, 8)
        r6 = random.randint(0, 8)

        if GRILLE_ALLIE[r5][r6]==1 or GRILLE_ALLIE[r5][r6]==4:
            verif1=False

        if verif1==True:
            GRILLE_ALLIE[r5][r6]=4
            comptdifficile.append(i)

        i=i+1
    OuvrirPlacementBateaux()



def menu():
    global imgfondframe1
    global imgBoutjframe1
    global imgBoutqframe1
    frame1.pack() #permet de positionner la frame2 en avant, c'est a dire le menu du jeu
    pygame.mixer.init()
    pygame.mixer.music.load("musicdebut.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

    can_menu.pack()
    can_menu.create_image((960,540), image=imgfondframe1, anchor=CENTER)



    Boutonjouer= Button(frame1, width=200, height=100,image=imgBoutjframe1, command=choixdifficulte) #un bouton jouer qui permet d'appeler la fonction OuvrirPlacementBateaux
    BoutonQuitter= Button(frame1, width=200, height=100,image=imgBoutqframe1, command=quitterjeu) #un bouton qui permet de  fermer le jeu
    Boutonjouer.place(relx=0.5, rely=0.40, anchor=CENTER)
    BoutonQuitter.place(relx=0.5, rely=0.60, anchor=CENTER)

def quitterjeu():
    pygame.mixer.music.set_volume(0)
    main.destroy()



def OuvrirLeCombat():
    global comptb
    global can_full_plac
    if comptb!=0:
        can_full_plac.create_text(1344, 870, anchor =CENTER, text ="tous les bateaux doivent être placer avant de commencer", fill ="black", font="Arial 30 bold")
    else:
        frame2.destroy() #permet de détruire la frame2, c'est a dire fenêtre du placement des Bateaux
        frame3.pack() #permet de positionner la frame3 en avant, c'est a dire la zone de combat navale
        etablirplateau() #appel la fonction permettant d'établir le plateau de la zone de combat navale

def tirallie(event):
    global comptrecur
    verif3=True
    global compt1allie
    global compt1ennemi
    global frame3

    if comptrecur%2==0:
        global CASE_TAIL
        global CAN_ALLIE
        global GRILLE_ENNEMI
        global CAN_ENNEMI
        mouseX = event.x
        mouseY = event.y
        verif1=True
        verif2=True
        grilleX = int(mouseX / CASE_TAIL)
        grilleY = int(mouseY / CASE_TAIL)
        if GRILLE_ENNEMI[grilleX][grilleY]==2:
            verif1=False
        if GRILLE_ENNEMI[grilleX][grilleY]==3:
            verif2=False

        if verif1==True and verif2==True:
            if GRILLE_ENNEMI[grilleX][grilleY]==1:
                tag = "e" + str(grilleY) + str(grilleX)
                CAN_ENNEMI.itemconfig(tag, fill="red")
                CAN_ENNEMI.update()
                GRILLE_ENNEMI[grilleX][grilleY]=2
                compt1ennemi=compt1ennemi-1
                bruittir=pygame.mixer.Sound("bruitdegat.wav")
                bruittir.set_volume(0.8)
                bruittir.play()
                CAN_ENNEMI.bind("<Button-1>",tirallie)
            if GRILLE_ENNEMI[grilleX][grilleY]==0:
                tag = "e_" + str(grilleX) + str(grilleY)
                CAN_ENNEMI.itemconfig(tag, fill="gray")
                CAN_ENNEMI.update()
                comptrecur=comptrecur+1
                GRILLE_ENNEMI[grilleX][grilleY]=3
        if compt1allie == 0 or compt1ennemi==0:
            global frame4
            frame3.destroy()
            frame4.pack()
            findejeu()
        can_full_eta= Canvas(frame3,width=384,height=216, bg="blue")
        can_full_eta.place(relx=0.75, rely=0.5, anchor=CENTER)
        can_full_eta.create_text(10, 50, anchor =W, text ="Il vous reste : "+str(compt1ennemi)+"\n"+ "parties de Bateau a touché", fill ="red", font="Arial 20 bold")
        tirenemi()

def tirenemi():
    global comptrecur
    global compt1allie
    global compt1ennemi
    verif3=True
    if comptrecur%2!=0:
        tr=0
        while verif3==True:
            global CAN_ALLIE
            global GRILLE_ALLIE
            global compt1allie
            global compt1allie
            if compt1allie == 0 or compt1ennemi==0:
                verif3=False
                global frame4
                frame3.destroy()
                frame4.pack()
                findejeu()
            verif1=True
            verif2=True
            verif4=True
            r1 = random.randint(0, 8)
            r2 = random.randint(0, 8)
            if GRILLE_ALLIE[r1][r2]==2:
                verif1=False
            if GRILLE_ALLIE[r1][r2]==3:
                verif2=False
            if GRILLE_ALLIE[r1][r2]==4:
                verif3=False
                tirenemi()


            if verif1==True and verif2==True and verif4==True:
                if GRILLE_ALLIE[r1][r2]==1:
                    tag = "a" + str(r2) + str(r1)
                    CAN_ALLIE.after(250,CAN_ALLIE.itemconfig(tag, fill="red"))
                    GRILLE_ALLIE[r1][r2]=2
                    compt1allie=compt1allie-1
                    bruittir=pygame.mixer.Sound("bruitdegat.wav")
                    bruittir.set_volume(0.8)
                    bruittir.play()
                    verif3=False
                    tirenemi()
                if GRILLE_ALLIE[r1][r2]==0:
                    tag = "a2" + str(r2) + str(r1)
                    CAN_ALLIE.after(250,CAN_ALLIE.itemconfig(tag, fill="gray"))
                    comptrecur=comptrecur+1
                    GRILLE_ALLIE[r1][r2]=3
                    verif3=False
            tr=tr+1



def PlacementBateaux():
    can_full_plac.pack()
    global imgBoutcframe1
    global imgBoutReset
    global imgfondetabli
    BoutonCommencer= Button(frame2, width=200, height=100,image=imgBoutcframe1, command=OuvrirLeCombat) #un bouton qui permet d'appeler la fonction OuvrirLeCombat
    BoutonCommencer.place(relx=0.5,rely=0.75,anchor=CENTER)
    BoutonReset= Button(frame2, width=200, height=100, image=imgBoutReset, command=SlotagedesBateauxReset)
    BoutonReset.place(relx=0.35, rely=0.75, anchor=CENTER)
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
    global frame2
    global can_full_plac
    global GRILLE_PlacementBateaux
    global GRILLE_ALLIE
    global GRILLE_ENNEMI
    global comptb
    global frame4
    global imgfondetabli
    frame2.destroy()
    frame2= Frame(main, width=1920,height=1080,bg="red")
    frame2.pack()
    GRILLE_PlacementBateaux = [[0 for i in range(9)] for i in range(9)]
    Bateauslot=[False,False,False,False,False]
    can_full_plac.destroy()
    can_full_plac= Canvas(frame2,width=1920,height=1080, bg="red",highlightthickness=0)
    can_full_plac.create_image((960,540), image=imgfondetabli, anchor=CENTER)
    for row in range(len(GRILLE_PlacementBateaux)):
        for col in range(len(GRILLE_PlacementBateaux[row])):
            can_full_plac.create_rectangle(192+(col * CASE_TAIL_Placement),108+(row * CASE_TAIL_Placement),192+(col * CASE_TAIL_Placement + CASE_TAIL_Placement),108+(row * CASE_TAIL_Placement + CASE_TAIL_Placement),outline="black",fill="white")
    Bateau1= can_full_plac.create_rectangle(960,108,960+(5*CASE_TAIL_Placement),108+CASE_TAIL_Placement, fill="black")
    Bateau2= can_full_plac.create_rectangle(960,216,960+(4*CASE_TAIL_Placement),216+CASE_TAIL_Placement, fill="black")
    Bateau3= can_full_plac.create_rectangle(960,324,960+(3*CASE_TAIL_Placement),324+CASE_TAIL_Placement, fill="black")
    Bateau4= can_full_plac.create_rectangle(960,432,960+(3*CASE_TAIL_Placement),432+CASE_TAIL_Placement, fill="black")
    Bateau5= can_full_plac.create_rectangle(960,540,960+(2*CASE_TAIL_Placement),540+CASE_TAIL_Placement, fill="black")
    Bateau=[Bateau1,Bateau2,Bateau3,Bateau4,Bateau5]
    comptb=5
    PlacementBateaux()

def findujeuReset():
     #la fenêtre utilisé pour le menu du jeu
    global frame3
    global frame4
    global frame5


    global frame2
    global can_full_plac
    global GRILLE_PlacementBateaux
    global GRILLE_ALLIE
    global GRILLE_ENNEMI
    global comptb
    global comptrecur
    global comptplacementbateauennemi
    global Bateauslot
    global Bateau
    global Bateau1
    global Bateau2
    global Bateau3
    global Bateau4
    global Bateau5
    global compt1allie
    global placementalea
    global can_full_fin
    global imgfondetabli

    frame4.destroy()
    frame2= Frame(main, width=1920,height=1080,bg="red")
    frame3= Frame(main, width=1920,height=1080,bg="black")
    frame4= Frame(main, width=1920,height=1080,bg="red")
    frame5= Frame(main, width=1920,height=1080,bg="blue")

    global can_choix
    can_choix=Canvas(frame5,width=1920, height=1080,bg="blue")

    frame5.pack()
    can_full_fin= Canvas(frame4,width=1920,height=1080, bg="red",highlightthickness=0)
    compt1allie=17

    global compt1ennemi
    compt1ennemi=17
    GRILLE_ENNEMI = [[0 for i in range(9)] for i in range(9)]
    GRILLE_ALLIE = [[0 for i in range(9)] for i in range(9)]
    comptrecur=0
    comptplacementbateauennemi=[]
    GRILLE_PlacementBateaux = [[0 for i in range(9)] for i in range(9)]
    Bateauslot=[False,False,False,False,False]
    can_full_plac.destroy()
    can_full_plac= Canvas(frame2,width=1920,height=1080, bg="red",highlightthickness=0)
    can_full_plac.create_image((960,540), image=imgfondetabli, anchor=CENTER)
    for row in range(len(GRILLE_PlacementBateaux)):
        for col in range(len(GRILLE_PlacementBateaux[row])):
            can_full_plac.create_rectangle(192+(col * CASE_TAIL_Placement),108+(row * CASE_TAIL_Placement),192+(col * CASE_TAIL_Placement + CASE_TAIL_Placement),108+(row * CASE_TAIL_Placement + CASE_TAIL_Placement),outline="black",fill="white")
    Bateau1= can_full_plac.create_rectangle(960,108,960+(5*CASE_TAIL_Placement),108+CASE_TAIL_Placement, fill="black")
    Bateau2= can_full_plac.create_rectangle(960,216,960+(4*CASE_TAIL_Placement),216+CASE_TAIL_Placement, fill="black")
    Bateau3= can_full_plac.create_rectangle(960,324,960+(3*CASE_TAIL_Placement),324+CASE_TAIL_Placement, fill="black")
    Bateau4= can_full_plac.create_rectangle(960,432,960+(3*CASE_TAIL_Placement),432+CASE_TAIL_Placement, fill="black")
    Bateau5= can_full_plac.create_rectangle(960,540,960+(2*CASE_TAIL_Placement),540+CASE_TAIL_Placement, fill="black")
    Bateau=[Bateau1,Bateau2,Bateau3,Bateau4,Bateau5]
    comptb=5
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
    choixdifficulte()

