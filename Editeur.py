# -*- coding: utf-8 -*-

from Fichier import Fichier
from Fichier import FichierBinaire
from Fichier import FichierTexte

class Editeur():
    """
    La classe Éditeur représente une instance de ed2017 lui-même. Il permet
    d’afficher l’invite de commande en boucle puis d’exécuter les commandes.
    
    Attributs : 
        _tampons : La liste des tampons ouverts 
        _tampon_courant : le tampon en cours d’édition, c’est celui sur lequel les commandes s’appliqueront.

    """

    def __init__(self):
        """
        Initialise l’éditeur avec un tampon texte vide qui sera bien entendu le tampon courant.
        """
        self._tampons = [] #Liste des tempons ouvert
        self._tampon_courant = Tampon("vide.txt") #Le tempon du ficher ouvert

    def invite(self):
        """
        Affiche l’invite de commande ( :) et saisi une commande de l’utilisateur.
        Retour (liste de str) : Une liste de mots entrés par l’utilisateur 
        """
        choix = input(">")
        return choix

    def exécute_commande(self, une_commande):
        """
        Valide et exécute une commande de l’utilisateur.
        
        Paramètres :
            - commande (str) : la commande entrée par l’utilisateur
            - paramètre (str) : le paramètre entré par l’utilisateur ou None s’il n’y en a pas
        
        Retour (bool) Faux si et seulement si c’était la dernière commande et que le programme doit se terminer.
        """
        liste_mots = une_commande.split()
        commande = liste_mots[0]

        if commande == "a": #commande pour afficher
            paramètre = liste_mots[-1]

            if paramètre[0] == "n" and paramètre[1::].isdigit() == True: #si l'utilisateur entre en paramètre le nombre de ligne
                compteur = 0
                nombre_ligne = int(paramètre[1::])

                print("la commande :", liste_mots)  # Débug
                print("le paramètre :", paramètre)  # Débug
                print("le nombre de ligne à afficher:", nombre_ligne)  # Débug
                print("Longeur de tempon courant:", len(self._tampon_courant._contenu)) #débug

                if nombre_ligne < len(self._tampon_courant._contenu): #si il ne veut pas afficher toutes les lignes
                    while compteur < nombre_ligne:
                        print(self._tampon_courant._contenu[compteur])
                        compteur = compteur + 1

                else: #si il veut afficher toute les lignes
                    for i in range(len(self._tampon_courant._contenu)):
                        print(self._tampon_courant._contenu[i])

            if paramètre == "a":# si l'utilisateur n'a pas entré de paramètre le programme affiche tout
                for i in range(len(self._tampon_courant._contenu)):
                    print(self._tampon_courant._contenu[i])

            else: #si ce qu'il entre n'est valide
                print("ce n'est pas un choix valide")


        if commande == "l" and liste_mots[-1] != "l": #si la commande est l et que l'utilisateur entre un chemin
            chemin = liste_mots[-1]
            f = open(chemin, "r")
            print("Ouverture de", chemin)

            for line in f.readlines(): #Boucle qui rajoute toute les lignes du fichier dans le contenu du tampon courant
                self._tampon_courant._contenu.append(line)

            print("la longeur du tempon courant :", len(self._tampon_courant._contenu))#débug
            print(self._tampon_courant._contenu)#débug

        if commande == "b":#Binaire pas encore fait
            pass

        if commande == "e":
            chemin = liste_mots[-1]
            try:
                self._tampon_courant.sauvegarder(chemin)

            except:
                print("le chemin n'est pas valide.")

        if commande == "i":#pas encore fait
            pass

        if commande == "s":#pas encore fait
            pass

        if commande == "t":
            for i in range(len(self._tampons)):
                print(i, self._tampons[i])


class Tampon():
    """
    Un tampon d’édition.
    Le tampon contient les données lues d’un fichier ou entrées par l’utilisateur.
    Lorsque le tampon a été lu d’un fichier ou que son contenu est sauvegardé, il est associé à ce fichier.
    
    Attributs : 
        _contenu (list): Le contenu du tampon sous forme de liste d’éléments
        _modifié : Vrai si et seulement si le contenu du tampon est différent du contenu du fichier associé 
                   (le tampon a été modifié depuis ladernière lecture ou sauvegarde).
        _fichier (obj Fichier) : Le fichier associé au tampon
    """

    def __init__(self, un_nom_fichier):
        """
        Initialise un Tampon. Si le nom de fichier est None, le
        tampon est vide, sinon, son contenu est lu à partir dudit fichier
        
        Paramètres :
            - un_nom_fichier (str) : chemin relatif du fichier associé au Tampon. None s’il s’agit d’un Tampon vide.
        """
        self._contenu = []
        self._modifié = False
        self._fichier = Fichier(un_nom_fichier)

    def __str__(self):
        """
        Méthode abstraite (non implémentée dans la superclasse).
        Retourne le contenu du tampon dans une forme affichable

        Retour : Le contenu sous la forme d’une chaîne de caractères.
        """
        contenu = ""
        for i in range(len(self._contenu)):
            contenu = contenu + self._contenu[i]

        return contenu

    def get_fichier(self):
        """
        Accesseur du fichier associé au tampon.
        Retour : Objet fichier
        """
        return self._fichier

    def get_ligne(self, no_ligne):
        """
        Méthode abstraite. Retourne une seule ligne du tampon dans une forme affichable.
        
        Attributs :
            no_ligne (int) : un numéro d’élément à afficher
            Retour : Une ligne du contenu sous la forme d’une chaîne de caractères.
        
        Assertion :
            Le numéro de ligne correspond à un élément du tampon
            Message : «no_ligne ne représente pas un élément du contenu»
        """
        pass

    def ouvrir(self, un_nom_fichier):
        """
        Charge le contenu d’un fichier dans le tampon.
        
        Paramètre :
            - un_nom_ficher (string) :  le chemin relatif du fichier à lire.
        """
        f = open(un_nom_fichier, "r")

        for line in f.readline():
            self._contenu.append(line)

    def sauvegarder(self, un_nom_fichier):
        """
        place le contenu du tampon dans un fichier. 
        Le fichier associé au tampon est utilisé s’il existe et il est créé sinon.
        
        Paramètre :
            un_nom_fichier (str) : le chemin relatif du fichier dans lequel sauvegarder le contenu du tampon.
        """
        f = open(un_nom_fichier, "w")
        for i in range(len(self._contenu)):
            f.writelines(self._contenu[i])


    def inseré(self, un_ajout, position):
        """
        Insère une donnée dans le contenu du tampon.
        
        Paramètre :
            - un_ajout (string) :  L’ajout entrée par l’utilisateur
            - position (int) :  La position à laquelle l’élément doit être placé dans le contenu.
            
        Assertion :
            La position est plus grande que la taille du tampon.
            Message : «la position dépasse la taille du tampon»

        """
        pass

    def supprimer(self, position):
        """
        Supprime une donnée du contenu.
        
        Paramètres :
            - position (int) : La position de l’élément à supprimer
        
         Assertion :
         La position correspond à un élément existant
         Message : «position ne représente pas un élément du contenu»
        """
        pass

    def est_modifié(self):
        """
        Retourne Vrai si le tampon a été modifié depuis la dernière sauvegarde ou lecture.
        Retour (bool) : Vrai si et seulement si le contenu du tampon est différent
        du contenu du fichier associé (le tampon a été modifié depuis la
        dernière lecture ou sauvegarde).
        """
        return self._modifié

éditeur = Editeur()
while True:
    choix = éditeur.invite()
    éditeur.exécute_commande(choix)