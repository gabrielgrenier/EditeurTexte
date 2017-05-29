# -*- coding: utf-8 -*-
#Auteur Gabriel Braun - Grenier
#Date : 2017-05-20
#Classe Éditeur, Tampon, TamponTexte et TamponBinaire

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
        self._tampon_courant = Tampon(None) #Le tempon du ficher ouvert

    def invite(self):
        """
        Affiche l’invite de commande ( :) et saisi une commande de l’utilisateur.
        Retour (liste de str) : Une liste de mots entrés par l’utilisateur 
        """
        choix = input(":")
        if choix == "":
            print("ce n'est pas valide")

        else:
            return choix

    def exécute_commande(self, une_commande):
        """
        Valide et exécute une commande de l’utilisateur.
        
        Paramètres :
            - une_commande (str) : la commande entrée par l’utilisateur
        
        Retour (bool) Faux si et seulement si c’était la dernière commande et que le programme doit se terminer.
        """
        liste_mots = une_commande.split() #sépare la commande en liste de mot
        commande = liste_mots[0] #la commande se trouve à la position 0

        if commande == "a": #commande pour afficher
            paramètre = liste_mots[-1]

            if paramètre.isdigit() == True: #si l'utilisateur entre en paramètre le nombre de ligne
                compteur = 0
                nombre_ligne = int(paramètre)
                contenu_str = ""

                if nombre_ligne < len(self._tampon_courant._contenu): #si il ne veut pas afficher toutes les lignes
                    while compteur <= nombre_ligne:
                        contenu_str = contenu_str + str(compteur) + " " + self._tampon_courant._contenu[compteur]
                        compteur = compteur + 1

                    print(contenu_str)

                else: #si il veut afficher toute les lignes
                    print(self._tampon_courant)

            elif paramètre == "a":# si l'utilisateur n'a pas entré de paramètre le programme affiche tout
                print(self._tampon_courant)

            if paramètre != "a" and paramètre.isdigit() == False:
                print("Veuillez entrer un paramètre numérique.")

        elif commande == "l" and liste_mots[-1] != "l": #si la commande est l et que l'utilisateur entre un chemin
            tampon_existant = False
            chemin = liste_mots[-1]

            for i in range(len(self._tampons)): #pour la longeur de la liste de tampons,
                if chemin == self._tampons[i]._fichier.get_nom(): #si le tempon est dans la liste
                    self._tampon_courant = self._tampons[i] #ouvre le tempn
                    tampon_existant = True
                    break

            if tampon_existant == False: #si le tempon n'a pas été ouvert
                nouveau_tampon = Tampon(chemin) #créé un nouveau tempon
                self._tampon_courant = nouveau_tampon
                self._tampons.append(self._tampon_courant)
                self._tampon_courant.ouvrir(chemin)


        elif commande == "b":#Binaire pas encore fait
            pass


        elif commande == "e":
            chemin = liste_mots[-1] #le chemin se trouve apres la commande
            self._tampon_courant.sauvegarder(chemin) #ouvre la fontion d'enregistrement


        elif commande == "i":
            if len(self._tampons) == 0:#si l'utilisateur n'a pas ouvert de fichier dans le tampon
                nouveau_tampon = Tampon("SansTitre.txt")  # créé un nouveau tampon SansTitre.txt
                self._tampon_courant = nouveau_tampon
                self._tampons.append(self._tampon_courant)

                no_ligne = liste_mots[-1]

                if no_ligne.isdigit() == True:
                    ajout = input(">")

                    self._tampon_courant.inserer(ajout, int(no_ligne))

                else:
                    print("Veuillez entrer un paramètre numérique.")

            else:#si l'utilisateur a chargé un fichier dans le tampon
                no_ligne = liste_mots[-1]

                if no_ligne.isdigit() == True:
                    ajout = input(">")

                    self._tampon_courant.inserer(ajout, int(no_ligne))

                else:
                    print("veuillez entrer un paramètre numérique ")

        elif commande == "r":
            if len(self._tampons) == 0:# si l'utilisateur n'a pas ouvert de fichier dans la mémoire tampon
                print("Vous devez charger un fichier dans le programme avant de pouvoir le modifier.")

            else:
                no_ligne = liste_mots[-1] #la ligne à remplacer

                if no_ligne.isdigit() == True:
                    ajout = input(">") #le contenu que l'utilisateur veut rajouter

                    self._tampon_courant._modifié = True
                    self._tampon_courant._contenu[int(no_ligne)] = ajout + "\n"

                else:
                    print("Veuillez entrer un paramètre numérique.")


        elif commande == "s":
            no_ligne = liste_mots[-1]

            if no_ligne.isdigit() == True:
                no_ligne = int(no_ligne)#le nunéro de la ligne à supprimer
                self._tampon_courant.supprimer(no_ligne)#supprime la ligne


            else:
                print("Veuillez entrer un paramètre numérique")#si l'utilisateur n'a pas entré un valeur int

        elif commande == "t" and liste_mots[-1] == "t":
            if len(self._tampons) > 0: #si l'utilisateur a au moin chargé un fichier dans la mémoire tampon
                for i in range(len(self._tampons)):#pour chaque fichier ouvert
                    if self._tampons[i]._fichier.get_nom() != self._tampon_courant._fichier.get_nom(): #si le nom afficher n'est pas le tampon ouvert
                        print(i, " ", self._tampons[i]._fichier.get_nom())#affiche le nom du fichier

                    if self._tampons[i]._fichier.get_nom() == self._tampon_courant._fichier.get_nom(): #si le nom est celui du tampon ouvert
                        print(i, ">", self._tampons[i]._fichier.get_nom())  # affiche le nom du fichier utilisé par l'utilisateur
            else:
                print("Vous n'avez pas chargé de fichier dans la mémoire tampon.")

        elif commande == "q":
            if self._tampon_courant.est_modifié() == True:
                print("Vous devez sauvegarder votre fichier avant de quitter.")

            else:
                quit()

        elif commande == "Q":
            quit()

        elif commande == "/help":
            print("--------------------------------------------------------------------  AIDE  ------------------------------------------------------------------------------")
            print("|    l NomFichier.txt = Lecture et ouverture du fichier dans l'éditeur.                                                                                   |")
            print("|    a n = Affichage des lignes 0 à n, si la commande n'a pas de paramètre, affiche le fichier au complet.                                             |")
            print("|    e NomFichier.txt = Enregistrement de votre fichier sous un nouveau nom, la commande n'a pas de paramètre, le fichier est saugarder sous le même nom. |")
            print("|    i n = Insérer du contenu à la ligne n, ne la remplace pas.                                                                                        |")
            print("|    r n = Remplace la ligne n par du nouveau contenu.                                                                                                 |")
            print("|    s n = Supprimer la ligne n.                                                                                                                       |")
            print("|    t = affiche la liste des fichiers ouvert dans la mémoire tampon.                                                                                     |")
            print("|    q = Quitter d'une manière sécuritaire, le programme vous rapelle de sauvegarder votre fichier avant de quitter.                                      |")
            print("|    Q = Quitter sans sauvegarder vos modifications.                                                                                                      |")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

        else:
            print("Ce n'est pas un choix valide.")


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
        return TamponTexte.__str__(self) #je peux pas retourner seulement TamponTexte sans le __str__(self) je comprend pas pourquoi

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
        return TamponTexte.get_ligne(self, no_ligne) #je comprend pas pourquoi il faut mettre le self

    def ouvrir(self, un_nom_fichier):
        """
        Charge le contenu d’un fichier dans le tampon.
        
        Paramètre :
            - un_nom_ficher (string) :  le chemin relatif du fichier à lire.
        """
        TamponTexte.ouvrir(self, un_nom_fichier) #Je suis obligé de mettre le self, je sais pas pourquoi


    def sauvegarder(self, un_nom_fichier):
        """
        place le contenu du tampon dans un fichier. 
        Le fichier associé au tampon est utilisé s’il existe et il est créé sinon.
        
        Paramètre :
            un_nom_fichier (str) : le chemin relatif du fichier dans lequel sauvegarder le contenu du tampon.
        """
        self._modifié = False

        if un_nom_fichier == "e": #si l'utilisateur n'a pas rentré de chemin (e = seulement la commande sans chemin nis non)
            self._fichier.écrire(self._contenu)

        else:#si l'utilisateur à entrer un nom ou un chemin
            try:
                f = open(un_nom_fichier, "w")

                for i in range(len(self._contenu)):#Écrit tout le contenu en mémoire dans le fichier
                    f.writelines(self._contenu[i])

                f.close()#ferme le fichier

            except Exception as e:#si le chemin n'est pas valide
                print("Le nom ou le chemin n'est pas valide :", e)



    def inserer(self, un_ajout, position):
        """
        Insère une donnée dans le contenu du tampon.
        
        Paramètre :
            - un_ajout (string) :  L’ajout entrée par l’utilisateur
            - position (int) :  La position à laquelle l’élément doit être placé dans le contenu.
            
        Assertion :
            La position est plus grande que la taille du tampon.
            Message : «la position dépasse la taille du tampon»

        """
        self._modifié = True


        if position < len(self._contenu):
            première_moitié = self._contenu[0:position]
            deuxième_moitié = self._contenu[position::]
            première_moitié.append(un_ajout + "\n")

            self._contenu = première_moitié + deuxième_moitié

        else:
            self._contenu.append(un_ajout + "\n")

    def supprimer(self, position):
        """
        Supprime une donnée du contenu.
        
        Paramètres :
            - position (int) : La position de l’élément à supprimer
        
         Assertion :
         La position correspond à un élément existant
         Message : «position ne représente pas un élément du contenu»
        """
        self._modifié = True
        self._contenu.pop(position)

    def est_modifié(self):
        """
        Retourne Vrai si le tampon a été modifié depuis la dernière sauvegarde ou lecture.
        Retour (bool) : Vrai si et seulement si le contenu du tampon est différent
        du contenu du fichier associé (le tampon a été modifié depuis la
        dernière lecture ou sauvegarde).
        """
        return self._modifié


class TamponTexte(Tampon):
    """
    La classe TamponTexte.
    Héritié de Tampon.
    """
    def __str__(self):
        """
        Retourne le contenu complet du tampon
        """
        contenu = ""
        for i in range(len(self._contenu)):#pour la longeur du contenu
            contenu = contenu + str(i) + " " + self._contenu[i]#écrit chaque ligne dans un str

        return contenu

    def ouvrir(self, un_nom_fichier):
        """
        Charge le contenu d'un fichier dans le tempon.
        
        Paramètre:
            - un_nom_fichier (str) : Le nom du fichier/le chemin du fichier à ouvrir
        """
        try:
            f = open(un_nom_fichier, "r")

            for line in f.readlines():  # Boucle qui rajoute toute les lignes du fichier dans le contenu du tampon courant
                self._contenu.append(line)

            return self._contenu

        except Exception as e:
            print("Ouverture impossible :", e)

    def get_ligne(self, no_ligne):
        """
        Retourne une ligne choisit par l'utilisateur
        
        Paramètre :
            - no_ligne (int) : le numéro de la ligne à afficher
        """
        if no_ligne <= len(self._contenu):
            return self._contenu[no_ligne]

        else:
            return str(no_ligne) + " " + "ne représente pas im élément du contenu"

class TamponBinaire(Tampon):
    """
    Classe TamponBinaire.
    Héritié de Tampon.
    """

    def __str__(self):
        """
        Le contenu sous la forme d’une chaîne de caractères.
        Les octets doivent être représentés sous forme hexadécimale,
        par groupes de 8, 2 groupes par ligne. Les lignes doivent être
        numérotées en hexadécimal selon le numéro du premier octet
        de la ligne. Si un paramètre position est donné, les 16 octets à
        partir de position doivent être affichés.
        """
        contenu = ""

    def ouvrir(self, un_nom_fichier):
        """
        Charge le contenu d'un fichier binaire dans le tampon.
        
        Paramètre :
            - un_nom_fichier (str) : le chemin relatif du fichier à lire
        """

    def get_ligne(self, no_ligne):
        """
        Retourne une ligne (16 octets) du tampon dans une forme affichable.
        
        Paramètre :
            - no_ligne (int) le numéro du premier élément à aficher
            
        Retourne une ligne du contenu (16 octets) sous la forme d’une chaîne de caractères.
        
        Assertion :
            - Le numéro de la ligne ne correspond pas a un élément du tampon = «no_ligne ne représente pas un élément du contenu»
        """

    def inséré(self, un_ajout, position):
        """
        Insère un élément dans le tampon, soit un octet.
        
        Paramètres :
            - un_ajout (str) : la représentation hexadécimale d’un octet.
            - position (int) : la position où le nouvel octet doit être inséré
            
        Assertions:
            - Si un_ajout ne peut pas être convertit en octet =  « [un_ajout] ne peut être converti en octet ».
            - Si la position dépasse la taille du Tampon = « la position dépasse la taille du tampon »
        """