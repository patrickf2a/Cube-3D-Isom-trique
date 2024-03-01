from tkinter import *
from cube import *
import pickle

class MonDico(dict):
    def __setitem__(self, pos, cb):
        """Ajoute un cube <cb> dans la position <pos> dans le dico des cubes"""
        super().setdefault(pos, []).append(cb)

    def __getitem__(self, pos):
        """Retourne les cubes presents pour une position <pos>"""
        return super().__getitem__(pos)

    def get_all(self) :
        """Retourne tous les cubes du dico"""
        return super().values()

    def get_allh(self, pos):
        """Retourne toutes les hauteurs d'une position <pos>"""
        L=[]
        for cb in (self.__getitem__(pos)):
            if type(cb) == list :
                L+=[cb[0].h]
            else :
                L+=[cb.h]
        return L

    def presentpos(self, pos):
        """Retourne 1 s'il y a deja un cube pour une position <pos>, 0 sinon"""
        if (pos in list(super().keys())) and (len(self.__getitem__(pos))>0) and pos>0:
            return 1
        else:
            return 0

    def present(self, pos, h):
        """Retourn 1 s'il y a deja un cube pour la meme position <pos> et la meme hauteur <h>, 0 sinon"""
        if pos in list(super().keys()):
            #pour chaque cube, je regarde s'il y a la meme hauteur <h>
            for cbe in (self.__getitem__(pos)):
                if type(cbe) == list :
                    if cbe[0].h == h:
                        return 1
                else :
                    if cbe.h == h:
                        return 1
        return 0

    def supp(self, id):
        """Supprime un cube à partir de son <id>"""
        for pos, cb in list(super().items()):
            for i in range(len(cb)):
                #je compare l'id
                if cb[i].id == id:
                    #je supprime si je le trouve
                    cb.remove(cb[i])
                    return
        return 0


class Conteneur:
    def __init__(self, d, Grille):
        self.__id = MonDico(d) # dictionnaire des cubes
        self.grille = Grille
        self.idcube = ((Grille.dim)*(Grille.dim))+3 #idcube stocke l'id du dernier cube

    def AjouterCube(self,zone, id, clr):
        """Ajoute un cube au conteneur et l'affiche"""

        Points = (self.grille).points #liste des points pour placer le cube
        dim = (self.grille).dim #dimension de la grille

        tags = zone.gettags(id) #recuperation des tags de la face du cube cliqué

        if tags[0] == "r": #si on clique sur une case du repère
            pos = int(tags[1][1:]) #on recupere la position de la case
            X, Y = Points[pos][0], Points[pos][1] #on recupere les coord. de la position

            c = Cube(self.idcube, pos, X, Y, clr, 0) # On cree le cube
            self.id[pos] = c #on l'ajoute au dict de cubes
            c.draw_cube(zone,self.grille.taillecase) # on affiche le cubes

            self.GestAffic(zone,pos,0) #on revoit l'affichage des cubes

            #comme on vient de créer 3 objets graphiques (3 polygones), l'id du prochain cube sera augmenté de 3
            self.idcube += 3
            # cas ou il y a une bitmap on cree un objet graphique en plus donc on rajoute 1 a l'id du cube
            l_clr = ("Rouge","Orange","Jaune","Vert","Vert1","Turquoise","Marine","Magenta","Bleu","Beige","Gris","Noir")
            if clr not in l_clr :
                self.idcube+=1

        elif tags[0] == "c": #si on clique sur un cube

            #hp: hauteur du nouveau cube (+1tags=("c","i",t,t2,t3) seulement si on clique au dessus d'un cube)
            #dp: positionnement du nouveau cube par rapport a celui qui est clique
            hp, dp = 0, 0

            pos = int(tags[2][1:]) #pos: position du cube clique

            if tags[1] == "h": #si on clique sur le haut d'un cube
                hp = 1

            elif tags[1] == "g": #si on clique à gauche d'un cube
                dp = dim

            elif tags[1] == "d": #si on clique à droite d'un cube
                dp =  1

            if not(((dp == 1) and ((pos+1)%dim == 0)) or ((dp==dim) and (pos >= ((dim*dim)-dim)))):
                X, Y = Points[pos+dp][0], Points[pos+dp][1]

                h = int(tags[3][1:]) + hp #on recupere la hauteur du cube cliqué + hp si la hauteur est differente

                if not (self.id).present(pos+dp,h) and h < self.grille.dim: #on verifie si le cube n'est pas deja present
                    c = Cube(self.idcube, pos+dp, X, Y, clr, h) # On cree le cube
                    self.id[pos+dp] = c #on ajoute le cube dans le dico des positions
                    c.draw_cube(zone,self.grille.taillecase) # On affiche le cube

                    #comme on vient de créer 3 objets graphiques (3 polygones), l'id du prochain cube sera augmenté de 3
                    self.idcube += 3
                    # cas ou il y a une bitmap on cree un objet graphique en plus donc on rajoute 1 a l'id du cube
                    l_clr = ("Rouge","Orange","Jaune","Vert","Vert1","Turquoise","Marine","Magenta","Bleu","Beige","Gris","Noir")
                    if clr not in l_clr :
                        self.idcube+=1

                    self.GestAffic(zone,pos+dp,h) #on revoit l'affichage des cubes


    def GestAffic(self,zone, pos, h):
        """Reaffiche les voisins du cube <id> dans le bon ordre"""

        dim = (self.grille).dim #dimension de la grille

        #liste des hauteurs des cubes présents dans la position <pos> (dans l'ordre décroissant)
        #par ex si a la position 0, il y a un cube en hauteur 1 et l'autre en hauteur 3, cela va donner L = [3,1]
        L = sorted((self.id).get_allh(pos), reverse=True)

        #affiche les cubes (positionnés après) devant le cube qu'on a placé
        for i in range(dim*dim-1, pos, -1):
            zone.tag_raise("p"+str(i),"p"+str(pos)+"h"+str(L[-1]))

        #affiche les cubes qui sont a la meme position et qui sont au-dessous (en hauteur) devant
        for i in range(len(L)):
            zone.tag_raise("p"+str(pos)+"h"+str(L[i]),"p"+str(pos)+"h"+str(L[-1]))



    def EffacerCube(self, zone, id):
        """Supprime un cube du conteneur et le supprime du canvas"""

        tags = zone.gettags(id) #on recupere les tags

        if tags[0]=="c": #si on clique bien sur un cube
            pos = int(tags[2][1:]) #on prend sa position

            if tags[0] == "c": #si on clique sur un cube
                if tags[1] == "h": #si on clique sur le haut d'un cube
                    pass
                if tags[1] == "g": #si on clique à gauche d'un cube
                    id += 1
                if tags[1] == "d": #si on clique à droite d'un cube
                    id += 2
                if tags[1] == "i" : # si on clique sur une bitmap
                    id +=1

                (self.id).supp(id) #on supprime le cube dans le dico des cubes

                #si la position n'a plus de cubes alors je la supprime du dico
                if len((self.id)[pos]) == 0:
                    del (self.id)[pos]

                zone.delete(tags[4]) #on efface le cube du canvas


    def Reset(self,zone):
        """Reinitialise le dictionnaire"""
        (self.id).clear() #on efface le contenu du dictionnaire
        zone.delete("c") #on supprime tous les cubes du canvas


    def save(self,file):
        """Enregistre le conteneur dans un fichier"""
        pickle.dump(self, file)
        file.close()

    def load(self,zone):
        """"Charge le conteneur a partir d'un fichier"""
        self.grille.draw_grid(zone) # on affiche la grille
        for c in self.id.get_all() :
            for cube in c :
                cube.draw_cube(zone,self.grille.taillecase) # On affiche le cube
                self.GestAffic(zone,cube.pos,cube.h) # on revoie l'affichage des voisins

    @property
    def id(self):
        """Retourne le dictionnaire des cubes"""
        return self.__id

    def setid(self,id) :
        """ Modifie le dictionnaire des cubes"""
        # Cette fonction est necessaire car lorsque l'on charge un dictionnaire a partir
        # d'un fichier cela rajoute une liste dans la liste
        aux = MonDico({})
        for cle in id.keys() :
            for cube in id[cle][0] :
                self.__id[cle] = cube
