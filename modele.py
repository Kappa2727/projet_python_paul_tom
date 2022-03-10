# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:20:26 2022

@author: paulc
"""

from tkinter import *

"""
définition des variables globals qui seront utilisée pour le jeu
"""
global main
main= Tk()
global CANVA_TAIL #la taille des canvas utilisée pour le jeu
global CASE_TAIL #la taille des cellules du canva (cad: taille des carrès de la grille )
CANVA_TAIL = 405 #360, car c'est divisible par 9 et que c'est une taille convenable
CASE_TAIL = CANVA_TAIL / 9 # 9, parce qu'il y'a 9 lignes et 9 colones dans une grille de bataille navale, donc on divise par 9 la taille du canva utilisé pour afficher la grille

global frame1 #la fenêtre utilisé pour le menu du jeu
global frame2
global frame3
frame1= Frame(main, width=1980,height=1080,bg="black")
frame2= Frame(main, width=1980,height=1080,bg="red")
frame3= Frame(main, width=1980,height=1080,bg="black")


#-------------------------------------------------------------------------------------------------------------------------------

"""
etablissement des variables globals pour le canva/grille allié et ennemi mais aussi pour le placement des bateaux
"""
global CAN_ALLIE
global GRILLE_ALLIE
GRILLE_ALLIE = [[0 for i in range(9)] for i in range(9)] #le nombre de lignes et de colones qu'auront la grille de l'allié

global CAN_ENNEMI
global GRILLE_ENNEMI
GRILLE_ENNEMI = [[0 for i in range(9)] for i in range(9)] #le nombre de lignes et de colones qu'auront la grille de l'ennemi

global CAN_PlacementBateaux
global GRILLE_PlacementBateaux
GRILLE_PlacementBateaux = [[0 for i in range(9)] for i in range(9)] #le nombre de lignes et de colones qu'auront la grille pour le placement des bateaux
global CANVA_TAIL_Placement #la taille des canvas utilisée pour la fenêtre du placement des bateaux
global CASE_TAIL_Placement #la taille des cellules du canva pour le placement des bateaux (cad: taille des carrès de la grille )
CANVA_TAIL_Placement = 540 #540, car c'est divisible par 9 et que c'est une taille convenable pour le placement des bateaux
CASE_TAIL_Placement = CANVA_TAIL_Placement / 9 # 9, parce qu'il y'a 9 lignes et 9 colones dans une grille de bataille navale, donc on divise par 9 la taille du canva utilisé pour afficher la grille

#-------------------------------------------------------------------------------------------------------------------------------



