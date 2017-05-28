# -*- coding: utf-8 -*-
#Auteur Gabriel Braun - Grenier
#Date : 2017-05-20
#Classe Éditeur, Tampon, TamponTexte et TamponBinaire

from Editeur import Editeur
from Fichier import Fichier
from Fichier import FichierBinaire
from Fichier import FichierTexte

éditeur = Editeur()

print("Merci d'utiliser le meilleure éditeur de texte !")
print("Si vous avez besoin d'aide, veuillez entrer /help.")

while True:
    choix = éditeur.invite()
    if choix != None:
        éditeur.exécute_commande(choix)
