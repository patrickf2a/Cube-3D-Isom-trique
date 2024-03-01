# Projet IHM
# FERNANDES DE FARIA PATRICK
# ALI-HADEF JAMEL


 ######### CONTENUE DOSSIER ###########

- Fichier grille.py: contient la classe Grille permettant de crée une grille dans le plan.

- Fichier cube.py : contient la classe Cube permettant de crée un cube sur une grille.

- Fichier conteneur.py : contient l'ensemble des données et fonctions pour la gestion d'affichage d'un cube dans la fenêtre ainsi que les fonctions permettant l'enregistrement et le chargement d'une scene.

- Fichier interface.py : programme principal qui regroupe l'ensemble des classes ainsi que les différentes fonctions de gestion de l'application.

######## UTILISATION DU PROGRAMME ########

 - Exécution du programme : pour ce faire il suffit simplement d'exécuter le programme interface.py pour ce faire il suffit de taper la commande suivante :
 python3 interface.py

 - Pour ajouter un cube, faites un clic gauche sur une case du repère (par défaut la couleur grise est prédéfinis).

 - Pour supprimer un cube, faites un clic droit sur le cube que vous souhaitez supprimer.

 - Pour choisir la couleur du cube il suffit de cliquer sur un cube avec une couleur prédéfinis sinon si une autre couleur est souhaité il suffit de choisir une couleur ou une textures deja prédéfinis dans la toplevel crée en cliquant sur le bouton plus et valider avec le bouton "Ok".

 - Pour effacer la grille, il suffit de cliquer sur le button de la barre menu "Option" puis "Masquer grille", faire la démarche inverse pour faire réapparaitre la grille.

 - Pour effacer tous les cubes, il suffit de cliquer sur le button de la barre menu "Option" puis "Tout Effacer".

 - Pour sauvegarder une scène il suffit de cliquer sur "enregistrer" dans la barre de menu et enregistrer au fichier .data .

 - Pour charger une scène il suffit de cliquer sur "Ouvrir" dans la barre de menu et ouvrir une scène déjà sauvegarder.



################### PROBLEME RENCONTRER ##########################

- Lors de l'enregistrement :
Quand on supprime un cube sur une scène deja enregistrer et que l'on veut enregistrer a nouveau cette scene, le cube supprimé n'est pas enregistrer.

- Au niveau des bitmap:
L'implantation des bitmaps a été réaliser avec succès, cependant lors de plusieurs placements de cube avec comme couleurs une texture l'application ne répond pas, en effet quand on clique successivement sur un cube déjà placer il se peut que le cube que l'on souhaite placer ne se place pas et après plusieurs tentatives celui-ci se place. Le problème est peut-être dû à l'utilisation d'images pour les textures, après plusieurs tentatives de résolution et le recadrage des images le problème persiste. Il faut noté que le problème est occasionnel et non récurrent.


