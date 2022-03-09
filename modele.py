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
global CAN_SIZE #la taille des canvas utilisée pour le jeu
global CELL_SIZE #la taille des cellules du canva (cad: taille des carrès de la grille )
CAN_SIZE = 405 #360, car c'est divisible par 9 et que c'est une taille convenable
CELL_SIZE = CAN_SIZE / 9 # 9, parce qu'il y'a 9 lignes et 9 colones dans une grille de bataille navale, donc on divise par 9 la taille du canva utilisé pour afficher la grille

#-------------------------------------------------------------------------------------------------------------------------------

"""
etablissement des variables globals pour le canva/grille allié et ennemi
"""
global CAN_ALLIE
global GRILLE_ALLIE
GRILLE_ALLIE = [[0 for i in range(9)] for i in range(9)] #le nombre de lignes et de colones qu'auront la grille de l'allié

global CAN_ENNEMI
global GRILLE_ENNEMI
GRILLE_ENNEMI = [[0 for i in range(9)] for i in range(9)] #le nombre de lignes et de colones qu'auront la grille de l'ennemi

#-------------------------------------------------------------------------------------------------------------------------------



