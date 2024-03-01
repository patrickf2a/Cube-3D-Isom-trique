from tkinter import *

class Cube:
    def __init__(self, id, pos, x, y, clr, h):
        #id: id du cube dans le canvas (id de la face du haut)
        #pos: position dans la grille (0,...,100)
        #x, y: position dans le repere en pixels
        #clr: couleur du cube
        #h: hauteur du cube 
        self.__id, self.__pos, self.__x, self.__y, self.__clr, self.__h = id, pos, x, y, clr, h

    def draw_cube(self, zone, tc):
        """ Dessine un cube """
        px, py = self.x,self.y - ((tc) * self.h) #position x, y varie en fonction de la hauteur du cube
        clr = self.clr #couleur du cube

        #dico des couleurs du cube dans le cas de couleur simple
        cr = {"Rouge":["#D00207","#B00206","#FD2B30"],"Orange":["#994C00","#CC6600","#FF9933"],
        "Jaune":["#CCCC00","#FFFF00","#FFFF33"],"Vert":["#006400","#008000","#228B22"],
        "Vert1":["#8FBC8F","#90EE90","#98FB98"],"Turquoise":["#00CED1","#40E0D0","#48D1CC"],
        "Marine":["#191970","#000080","#00008B"],"Magenta":["#8B008B","#9400D3","#9932CC"],
        "Bleu":["#054EC7","#04388E","#2173FA"],"Beige":["#FFE4C4","#FFEBCD","#F5DEB3"],
        "Gris":["#9C9C9C","#4B4B4B","#E6E6E6"] ,"Noir":["#161616","#000000","#242424"]}

        t = "p"+str(self.pos) # tag pour la position du cube
        t2 = "h"+str(self.h) # tag pour la hauteur du cube
        t3 = "p"+str(self.pos)+"h"+str(self.h) # tag indiquant la position et la hauteur

        if clr in cr.keys() :
    		#face de droite
            zone.create_polygon([(px,py),(px,py+tc),(px+tc,py+(tc/2)),(px+tc,py-(tc/2))], fill=cr[clr][0], outline="black", tags=("c","d",t,t2,t3,"f"))
    		#face de gauche
            zone.create_polygon([(px,py+tc),(px,py),(px-tc,py-(tc/2)),(px-tc,py+(tc/2))], fill=cr[clr][1], outline="black", tags=("c","g",t,t2,t3,"f"))
    		#face du haut
            zone.create_polygon([(px+tc,py-(tc/2)),(px,py),(px-tc,py-(tc/2)),(px,py-tc)], fill=cr[clr][2], outline="black",  tags=("c","h",t,t2,t3,"f"))

        else :
            # bitmap
            idimg = zone.create_image(px, py, image=clr, anchor='center', tags=("c","i",t,t2,t3))

            # On dessine un cube transparent par dessus le bitmap
        	#face de droite
            zone.create_polygon([(px,py),(px,py+tc),(px+tc,py+(tc/2)),(px+tc,py-(tc/2))], fill="", outline="",tags=("c","d",t,t2,t3,"f"))
    		#face de gauche
            zone.create_polygon([(px,py+tc),(px,py),(px-tc,py-(tc/2)),(px-tc,py+(tc/2))], fill="",outline="",  tags=("c","g",t,t2,t3,"f"))
    		#face du haut
            zone.create_polygon([(px+tc,py-(tc/2)),(px,py),(px-tc,py-(tc/2)),(px,py-tc)], fill="",outline="", tags=("c","h",t,t2,t3,"f"))

    @property
    def id(self):
        """Renvoie l'id du cube (id de la face du haut)"""
        return self.__id

    @property
    def pos(self):
        """Renvoie la position dans le repere"""
        return self.__pos

    @property
    def x(self):
        """Renvoie la position en x (en pixels)"""
        return self.__x

    @property
    def y(self):
        """Renvoie la position en y (en pixels)"""
        return self.__y

    @property
    def h(self):
        """Renvoie la hauteur du cube"""
        return self.__h

    @property
    def clr(self):
        """Renvoie la couleur du cube"""
        return self.__clr
