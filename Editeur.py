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
        self._tampon_courant = Tampon() #Le tempon du ficher ouvert

    def invite(self):
        """
        Affiche l’invite de commande ( :) et saisi une commande de l’utilisateur.
        Retour (liste de str) : Une liste de mots entrés par l’utilisateur 
        """
        choix = input(">")
        return choix

    def exécute_commande(self, une_commande, un_paramètre):
        """
        Valide et exécute une commande de l’utilisateur.
        
        Paramètres :
            - commande (str) : la commande entrée par l’utilisateur
            - paramètre (str) : le paramètre entré par l’utilisateur ou None s’il n’y en a pas
        
        Retour (bool) Faux si et seulement si c’était la dernière commande et que le programme doit se terminer.
        """
        liste_mot = une_commande.split()
        paramètre = liste_commande[-1]
        commande = liste_mot[0]

        if commande == "a":#À tester
            if paramètre[0] == "n" and paramètre[1::].isdigit() == True:
                compteur = 0
                nombre_lignes = int(paramètre[1::])

                while compteur < nombre_lignes:
                    print(self._tampon_courant._contenu[compteur])
                    compteur = compteur + 1

            else:
                for line in len(self._tampon_courant._contenu):
                    print(self._tampon_courant._contenu[line])

        if commande == "l":#à travailler
            nouveau_tempon = Tempon(paramètre)
            while True:
                try:
                    self._tampons.append(nouveau_tempon)

                except:
                    print("Veuillez entrer un chemin valide.")
                    chemin = input(">")
                    self._tampons.append(chemin)

        if commande == "b":#Binaire pas encore fait
            pass

        if commande == "e":
            self._tampon_courant.sauvegarder(paramètre)

        if commande == "i":#pas encore fait
            pass

        if commande == "s":#pas encore fait
            pass

        if commande == "t":#À tester
            for i in len(self._tampons):
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
        for i in len(self._contenu):
            contenu.append(self._contenu[i])

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
        self._fichier = Fichier(un_nom_fichier)
        contenu = self._fichier.get_contenu()

        for line in len(contenu):
            self._contenu.append(contenu[line])

    def sauvegarder(self, un_nom_fichier):
        """
        place le contenu du tampon dans un fichier. 
        Le fichier associé au tampon est utilisé s’il existe et il est créé sinon.
        
        Paramètre :
            un_nom_fichier (str) : le chemin relatif du fichier dans lequel sauvegarder le contenu du tampon.
        """
        f = open(un_nom_fichier, "w")

        for line in len(self._contenu):
            f.writeline(self._contenu[line])

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