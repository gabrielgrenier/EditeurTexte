# -*- coding: utf-8 -*-
# Jean-Claude Gamarra et Gabriel Braun - Grenier
#
# TP4: Éditeur de texte - Class Texte et ses sous-Class

class Fichier:
    """
    Un fichier

        Attributs :

          - _nom : (str)(protégée) chemin relatif du fichier.

    """

    def __init__(self, un_nom):
        """
        Initialise un fichier
        """
        self._nom = un_nom


    def get_nom(self):
        """
        Accesseur du nom du fichier.

        - Retour : (str)  le chemin relatif du fichier. « [sans nom] » si le fichier n’est
        pas encore écrit sur disque.

        """
        return self._nom

    def set_nom(self, un_nom):
        """
        Mutateur du nom du fichier. Le contenu du fichier doit être sauvegardé sous le nouveau nom.

        Paramètre :

            - un_nom : (str) le chemin relatif du fichier.

        Exceptions :

            Lance une FileExistsError si le nouveau nom de fichier correspond
            à un fichier existant.

            - Message : « [un_nom] existe déjà. »

        """
        try:
            self._nom = un_nom

        except FileExistsError:
            print(un_nom, " existe déjà")#à tester

    def get_contenu(self):
        """
        Accesseur du contenu du fichier. Lit et retourne le contenu du fichier.

        - Retour : (liste) une liste d’éléments lus à partir du fichier. S’il s’agit
        d’un nouveau fichier (sans nom), retourne une liste vide.


        """
        return self._contenu #incomplet

    def set_contenu(self, un_contenu):
        """
        Mutateur du contenu du fichier. Écrit le nouveau contenu dans le fichier.

        Paramètre :

            - un_contenu : (liste) Les éléments du fichier à écrire sur disque.

        Exceptions :

            Lance une ValueError si le fichier n’a pas encore de nom et
            ne peut donc pas sauvegarder le nouveau contenu.


            - Message : « Le fichier n’a pas été nommé ».
        """
        try:
            self._contenu = un_contenu

        except ValueError:
            print(un_nom, "Le fichier n'a pas été nommée")# à tester
        

    def lire(self):
        """
        Méthode abstraite (non implémentée dans la super-classe).
        Lit et retourne le contenu d’un fichier.

        - Retour : (liste) Retourne le contenu du fichier sous forme de liste.


        """
        f = open(self._nom, "r")
        for i in range(len(self._contenu)):
            return f.readline(self._contenu[i])

    def écrire(self, un_contenu):
        """
        Méthode abstraite (non implémentée dans la super-classe).
        Écrit un nouveau contenu dans un fichier texte.


        Paramètre :

            - un_contenu : (Liste) Méthode abstraite (non implémentée dans la super-classe).
            Écrit un nouveau contenu dans un fichier texte
        """
        contenu = un_contenu
        FichierTexte.écrire(self, contenu)


class FichierTexte(Fichier):
    """
    Un fichier texte.


    - Hérite de : Fichier
    """

    def lire(self):
        """
        Lit et retourne le contenu d’un fichier texte.

        - Retour : (liste) Retourne une liste de lignes lues dans le fichier.
        """
        f = open(self._nom, "r")
        for i in range(len(self._contenu)):
            return f.readline(self._contenu[i])

    def écrire(self, un_contenu):
        """
        Écrit un nouveau contenu dans un fichier texte.

        Paramètre :

            - un_contenu : (liste) le nouveau contenu du fichier. Tout contenu antérieur est écrasé.


        """
        f = open(self.get_nom(), "w")

        for i in range(len(un_contenu)):
            f.writelines(un_contenu[i])

        f.close()



class FichierBinaire(Fichier): # Je ne sais pas trop quoi faire.
    """
    Un fichier binaire.


    - Hérite de : Fichier
    """

    def lire(self):
        """
        Lit et retourne le contenu d’un fichier binaire.

        - Retour : (liste) Retourne les octets lus dans le fichier sous forme d’une liste d’entiers.
        """
        pass

    def écrire(self):
        """
        Écrit un nouveau contenu dans un fichier binaire.

        Paramètre :

            - un_contenu : (liste d'entiers) le nouveau contenu du fichier sous forme de liste d’entiers.
            Tout contenu antérieur est écrasé.


        """
        pass
