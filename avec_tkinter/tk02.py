import random
from tkinter import * 
"""
Utilisation du paquet tkinter
On veut afficher tous les robots d'un tableau

"""


#
# Tableau de robots
#
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
# ajouter un titre
#
un_titre = Label(text="les "+str(len(robots))+" Robots", font=("sans-serif, 30"), bg="dodgerblue", fg="white")
un_titre.pack()
# 
# Créer autant de label que de robots
for i, robot in enumerate(robots):
    un_texte = Label(text="N°"+str(i+1)+" "+ robot, font=("sans-serif, 20"), bg="dodgerblue", fg="white")
    un_texte.pack(side=TOP)
#
# Afficher
root.mainloop()