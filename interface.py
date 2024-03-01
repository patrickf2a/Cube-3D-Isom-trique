from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfile
from PIL import Image, ImageTk
import grille
import cube
import conteneur
import pickle

class Application(Tk):
    def __init__(self):
        Tk.__init__(self) # Constructeur de la classe parent

        ############### PARAMETRAGE DE LA FENETRE ################
        self.geometry("1080x720") # Redimensionne la fenetre
        self.resizable(width=False,height=False) # Rend la modification de la taille de la fenetre impossible
        self.title("Application 3D") # Titre de la fenetre
        self.configure(bg='gray40') # Changement couleur fond
        self.update()

        ############## VARIABLE DE GESTION #####################@
        # Canvas
        self.canv = Canvas(self, width=self.winfo_width(),height=self.winfo_height()-80, bg ="white")
        self.canv.pack(side =TOP)

        self.show_grid_bool = IntVar() # variable d'etat de l'option masquer grille

        self.dim = IntVar() # variable de la dimension de la grille
        self.dim.set(8)

        #position de l'origine de la grille adapté à la taille
        X,Y = self.winfo_width()/2,self.winfo_height()/3

        #taille d'une case en pixels
        tc = 30

        #initialisation de la grille
        self.grid = grille.Grille(X, Y, self.dim.get(), tc)
        self.grid.draw_grid(self.canv)

        # conteneur
        D = {}
        self.conteneur = conteneur.Conteneur(D, self.grid)

        self.varclr = StringVar() # variable de la couleur courante du cube
        self.varclr.set("Gris") # initialiser a gris


        ########## Importation des images des boutons #############

        self.button_img= {} # Dictionnaire des image des boutons
        liste_couleur = ['Noir','Beige','Bleu','Magenta','Gris','Marine', 'Jaune', 'Orange', 'Rouge', 'Turquoise', 'Vert', 'Vert1','bois','glace','glace2','glace3','granit','herbe','sable','sable2','plus']
        for n in liste_couleur :
            img = Image.open('image/bouton/'+n+'.png')
            image = img.resize((50,50))
            self.button_img[n] = [ImageTk.PhotoImage(image)]

        ############ Importation des textures des cubes #############

        self.textures = {} # Dictionaire des textures
        liste_button_img = ('bois','glace','glace2','glace3','granit','herbe','sable','sable2')
        for n in liste_button_img :
            im = Image.open("image/bouton/"+n+".png")
            im = im.transform((300,300), Image.EXTENT,  (0, 0, 300, 300))  # selection de la region de l'image
            im.thumbnail((67,67))
            self.textures[n] = ImageTk.PhotoImage(im)


        ############# Gestion affichage du cube ####################

        def ClicGauche(event):
            """clic gauche de la souris: ajout du cube"""
            pt = self.canv.find_withtag('current')
            self.conteneur.AjouterCube(self.canv,pt[0],self.varclr.get())


        def ClicDroit(event) :
            """clic droit de la souris: suppression du cube"""
            pt = self.canv.find_withtag('current')
            self.conteneur.EffacerCube(self.canv,pt[0])

        #clic gauche : ajout du cube
        self.canv.tag_bind("f","<Button-1>", ClicGauche)

        #clic droit: suppression du cube
        self.canv.tag_bind("f","<Button-3>", ClicDroit)

        self.MenuBar() # barre de menu
        self.CubeButton() # Bouton de choix de la couleur du cube

    def CubeButton(self) :
        """Bouton de choix de la couleur du cube dans la barre de choix présente en dessous du canvas """
        cube_button_bar = Frame(self,width=1080, height=60, bg='gray15',bd=0)
        i = 0
        l_couleur = ['Gris','Beige','Rouge','Bleu','Magenta','Vert1','Marine','Jaune','Orange']
        for clr in l_couleur:

            bt1 = Radiobutton(cube_button_bar, height=52, width=50,
            offrelief=FLAT,overrelief=RAISED,image=self.button_img[clr],indicatoron=0,
            highlightthickness=0,highlightbackground='gray40',
            highlightcolor='black',bg='gray40',cursor='exchange',
            activebackground='gray40',selectcolor='gray40',
            variable=self.varclr,value=clr)

            bt1.grid(row=0, column=i)
            i+=1

        #Boutton Plus
        bt9 = Button(cube_button_bar, height=50, width=50, relief=FLAT,overrelief=RAISED,image=self.button_img['plus'],highlightthickness=0,bg='gray40',activebackground='gray40',command=self.window_cube_color)
        bt9.grid(row=0, column=i)

        cube_button_bar.pack(side=TOP)

    def window_cube_color(self):
        """Fenetre pour choisir des couleurs de cube supplementaire dans la toplevel crée pour cela"""
        #Toplevel
        cube_rgb_wind = Toplevel(self,width=150,height=100,bg="white")
        cube_rgb_wind.title('Choix Couleur RGB')
        cube_rgb_wind.resizable(width=False,height=False)

        #Canvas pour affichage des image de cube.
        cube_bis=Canvas(cube_rgb_wind,width=150,height=80)
        cube_bis.grid(row=0,column=0)

        #Dictionnaire de données des couleurs respective à chaque cube
        current_color =self.varclr.get()
        i, j = 0, 0
        liste_couleur = ['Noir', 'Turquoise', 'Vert', 'Vert1','bois','glace','glace2','glace3','granit','herbe','sable','sable2']
        l_text = ['bois','glace','glace2','glace3','granit','herbe','sable','sable2']
        for clr in liste_couleur :
            if clr in l_text :
                bt = Radiobutton(cube_bis,text = clr, bg = "white",indicatoron=0,image = self.button_img[clr],variable=self.varclr,value = self.textures[clr])
            else :
                bt = Radiobutton(cube_bis,text = clr, bg = "white",indicatoron=0,image = self.button_img[clr],variable=self.varclr,value = clr )
            bt.grid(row=i, column=j)
            i += 1
            if i == 4 :
                i = 0
                j += 1

        #Frame pour boutton Annuler et OK
        cadre=Frame(cube_rgb_wind,width=150,height=20,bg="green")

        Boutton8=Button(cadre,text="Annuler",bg="white",width =12,command = lambda :[self.varclr.set(current_color), cube_rgb_wind.destroy()])
        Boutton8.grid(row=0,column=0)

        Boutton7=Button(cadre,text="OK",bg="white",width =12, command=cube_rgb_wind.destroy)
        Boutton7.grid(row=0,column=1)

        cadre.grid()
        cube_rgb_wind.grab_set() #Toplevel bloquante


    def MenuBar(self):
        """Barre de menu de l'application"""
        barremenu = Menu(self, bg='gray25',fg='white',bd=0)

        # Menu Fichier
        fichier = Menu(barremenu, tearoff=0, fg="white")
        barremenu.add_cascade(label="Fichier", menu=fichier)
        fichier.add_command(label="Nouveau", command=self.nouveau)
        fichier.add_command(label="Ouvrir", command=self.ouvrir)
        fichier.add_command(label="Enregistrer", command=self.enregistrer)
        fichier.add_separator()
        fichier.add_command(label="Quitter", command=self.quitter)

        # Menu Option
        option = Menu(barremenu, tearoff=0, bg='gray25', fg="white")
        barremenu.add_cascade(label="Option", menu=option)
        option.add_checkbutton(label="Masquer Grille", variable=self.show_grid_bool, command=self.mask_grid)
        option.add_command(label="Tout Effacer", command=lambda: self.conteneur.Reset(self.canv))

        # Menu Aide
        aide = Menu(barremenu, tearoff=0, bg='gray25', fg="white")
        barremenu.add_cascade(label="Aide", menu=aide)
        aide.add_command(label="Fonctionnement", command=self.maide)
        aide.add_command(label="A propos", command=self.apropos)

        self.config(menu = barremenu)

    ##################### FONCTIONS DE LA BARRE DE MENU #######################

    #OUVRIR UN FICHIER

    def ouvrir(self):
        """Fonction qui charge une scene"""
        filename = askopenfilename(title="Ouvrir un fichier",
                filetypes=[("Données", ".data"), ("Tous les fichiers", ".*")])
        fichier = open(filename, "rb")
        cnt = pickle.load(fichier)
        self.conteneur.grille = cnt.grille
        self.conteneur.setid(cnt.id)
        #print(conteneur.id)
        self.conteneur.idcube  = cnt.idcube

        # on efface tout
        self.canv.delete(ALL)

        # on charge avec la fonction
        self.conteneur.load(self.canv)
        fichier.close()


    #ENREGISTRER UN FICHIER
    def enregistrer(self):
        """Fonction qui enregistre une scene"""
        file = asksaveasfile( mode = "wb", title = "Enregistrer sous ..." , filetypes = [("Fichier data",".data")] , defaultextension = ".data" )
        self.conteneur.save(file)
        file.close()

    # QUITTER L'APPLICATION
    def quitter(self):
        """Fonction pour quitter l'application"""
        if messagebox.askokcancel("Quitter","Voulez-vous vraiment quitter ?"):
            self.destroy()

    def nouveau(self) :
        """Fonction pour tout effacer et reaffiche la grille"""
        self.canv.delete(ALL) # on efface tout le contenu du canvas
        self.grid.draw_grid(self.canv) # on affiche la grille

    # MENU AIDE
    def apropos(self):
        messagebox.showinfo("Application 3D Isométrique", "ALI-HADEF Jamel \nFERNANDES DE FARIA Patrick")

    def maide(self):
        messagebox.showinfo("Fonctionnement", "Fonctionnement de l'application : \n\n - On peut placer un cube n'importe ou dans le repaire si celui-ci n'existe pas. \n - On peut supprimer n'importe qu'elle cube dans le repaire. \n- On peut choisir la couleur du cube (avec les textures ou couleur RGB prédéfinis). \n- On peut enregistrer une scène. \n- On peut charger une scène. \n -On peu effacer tout les cubes d'une scène. \n - On peut masquer la grille.")

    def mask_grid(self) :
        """Fonction pour masquer ou afficher la grille"""
        if self.show_grid_bool.get() :
            self.grid.mask_grid(self.canv)
        else :
            self.grid.show_grid(self.canv)




app = Application()
app.mainloop()
