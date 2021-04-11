"""
Utilisation du paquet tkinter
Tkinter propose des widgets pour configurer et afficher des textes, boutons, images, ...
On veut afficher ici un robot d'un tableau


"""


import random
from tkinter import * 

robots = ["Achille","Hercule","Barbara","Hermione","Léonard"]
#
# creation de l'interface graphique
#
root = Tk()
#
# paramétrage de la fenetre principale
#
root.title = "Mon application"
root.geometry("800x600")
root.config(background='dodgerblue')
#
# index position robot
idxr =  random.randint(0,len(robots)-1)
#
# Ajouter un texte
un_texte = Label(text="Robot n°"+str(idxr)+" "+ robots[idxr], font=("sans-serif, 30"), bg="dodgerblue", fg="white")
un_texte.pack(side=TOP)
#
# Afficher
root.mainloop()