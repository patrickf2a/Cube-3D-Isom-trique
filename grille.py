from tkinter import *
import pickle

class Grille:

    def __init__(self, X, Y, dim, tc):
        # zone : zone graphique pour l'affichage
        # X, Y: origine de la Grille
        # dim : dimension du repere
        # tc : taille d'une case en pixels
        # ps : liste de tous les points de la grille où un cube peut être placé
        self.X, self.Y, self.__dim, self.__tc, self.__ps= X, Y, dim, tc, []

    def draw_grid(self,zone):
        """ Dessine la grille dans le canvas """
        X, Y, dim, tc = int(self.X), int(self.Y), self.__dim, self.__tc

        pos = 0 #pos sert à indiquer la position de la case dans le tag
        lg = tc * dim #longueur du repere (dimension * taille d'une case)

        for i in range(X,X-lg,-tc):
            for j in range(0,lg,tc):
                px = i + j
                py = int(Y + (j/2))
                self.__ps += [(px,py)] #ajout dans la liste des points
                zone.create_polygon([(px,py),(px+tc,py+(tc/2)),(px,py+tc),(px-tc,py+(tc/2))], fill="white", outline="black", tags=("r","p"+str(pos),"f"))
                pos += 1
            Y += (tc/2)

    def show_grid(self,zone) :
        """ Affiche la grille (met la couleur des lignes en noir)"""
        zone.itemconfig("r",outline='black')

    def mask_grid(self,zone) :
        """ Masque la grille (met la couleur des lignes en transparent)"""
        zone.itemconfig("r",outline='')

    @property
    def taillecase(self):
        """ Renvoie la taille d'une case"""
        return self.__tc

    @property
    def dim(self):
        """Renvoie dimension du repere"""
        return self.__dim

    @property
    def points(self):
        """Renvoie les points de la Grille"""
        return self.__ps
