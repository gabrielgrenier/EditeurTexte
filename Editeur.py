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
        pass

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