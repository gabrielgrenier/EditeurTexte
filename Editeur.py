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
        self._tampons = []
        self._tampon_courant = Tampon()

    def invite(self):
        """
        Affiche l’invite de commande ( :) et saisi une commande de l’utilisateur.
        Retour : (liste de str) : Une liste de mots entrés par l’utilisateur 
        """
        pass

    def exécute_commande(self):
        """
        Valide et exécute une commande de l’utilisateur.
        
        Attributs :
            - commande (str) : la commande entrée par l’utilisateur
            - paramètre (str) : le paramètre entré par l’utilisateur ou None s’il n’y en a pas
        
        Retour (bool) Faux si et seulement si c’était la dernière commande et que le programme doit se terminer.
        """
        pass

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
        pass

    def __str__(self):
        """
        Méthode abstraite (non implémentée dans la superclasse).
        Retourne le contenu du tampon dans une forme affichable

        Retour : Le contenu sous la forme d’une chaîne de caractères.
        """
        pass

    def get_fichier(self):
        """
        Accesseur du fichier associé au tampon.
        Retour : Objet fichier
        """
        pass

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

    def ouvir(self, un_nom_fichier):
        """
        Charge le contenu d’un fichier dans le tampon.
        
        Paramètre :
            - un_nom_ficher (string) :  le chemin relatif du fichier à lire.
        """
        pass

    def sauvegardé(self):
        """
        place le contenu du tampon dans un fichier. 
        Le fichier associé au tampon est utilisé s’il existe et il est créé sinon.
        
        Paramètre :
            un_nom_fichier (str) : le chemin relatif du fichier dans lequel sauvegarder le contenu du tampon.
        """
        pass

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
        pass